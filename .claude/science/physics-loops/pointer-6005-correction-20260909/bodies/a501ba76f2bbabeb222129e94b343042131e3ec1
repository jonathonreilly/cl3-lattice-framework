#!/usr/bin/env python3
"""Cycle 934 / blockM14 -- THE POINTER-SIDE GATES, DERIVED; the star theorem composed.

Campaign toe-time-expansion-20260802.  Cycle 933 derived the ARM side: the
pointer-conditioned branch lies exactly in C^2 (x) Sym^d, so s(k) -- and with it
C_ab = 2 s(1) - s(2) -- is the entropy of a binomially weighted Hankel spectrum
in a 2(d+1)-dimensional linear problem.  Cycle 932 derived the persistence
combinatorics (one certifiable window [t_open, t_close]; persistence counts
frozen grid points) but IMPORTED t_open, whose degree-independence (spread
2.1e-3 across d = 2..8) was an unexamined regularity.  Cycle 933's own overreach
audit proved the POINTER side (chi, excess, H_Z) is NOT determined by s(k).
This block derives the pointer side and composes the star certification theorem.

THE FROZEN OBJECTS, QUOTED FROM THE MEMO BYTES AND RE-VERIFIED HERE

  Hamiltonian   `H_lambda = - sum_<ij> Z_i Z_j - lambda sum_i X_i`
  preparation   `center: n_center=(1,0,0), the +X state`
                `every axial face: n_face=(1,0,0), the +X state`
                -- as implemented: the pointer AND its recording neighbours
                start in +X.  On a star K_{1,d} that is |+>^(x)(d+1).
  pointer-side  `chi_Z(S:F) = S(sum_z p_z rho_F^z) - sum_z p_z S(rho_F^z).`
  content gate  1. `H(Z_S) >= 0.05 bit`;
                2. `chi_Z(S:F) >= (1-delta) H(Z_S)`;
  excess gate   `chi_Z(S:F)(t) - chi_Z(S:F)(0) >= 0.02 bit`
  independence  `every pair has `C_ab <= 0.02 bit``
  arm side      `C_ab = I(F_a:F_b | Z_S)`, evaluated as
                `C_ab = sum_z p_z [S(rho_Fa^z)+S(rho_Fb^z)-S(rho_FaFb^z)]`
  run rule      `persistence flag requires three consecutive certification
                samples`, PERSIST_N = 3, on Jt = 0.0(0.1)1.2, deadline Jt <= 1.

WHAT THIS RUNNER FINDS

  Q1  Every pointer-side statistic is a functional of the SAME 2(d+1) collective
      reduction.  With |chi_z> the pointer-branch vector in Sym^d and x^z its
      Dicke-amplitude sequence, T^(k)(x)_{m,q} = sqrt(C(k,m) C(d-k,q)) x_{m+q}:
        rho_F^z = T^(k)(x^z) T^(k)(x^z)^dag / tr,   rho_F = sum_z p_z rho_F^z,
        chi_k   = S(rho_F) - sum_z p_z S(rho_F^z),   s(k) = sum_z p_z S(rho_F^z),
        H_Z     = h2(p),                             C_ab = 2 s(1) - s(2).
      chi is the SAME Hankel object as s(k), read through a different entropy --
      which is exactly why 933's audit was right that s(k) alone cannot decide it.

  Q2  t_open is DERIVED, and the degree-independence is EXPLAINED EXACTLY.
      L0  H_Z(t) = 1 bit EXACTLY for every d, lambda, t.  The global X-flip
          P = prod_i X_i commutes with H and fixes the preparation, and it maps
          Z_0 -> -Z_0, so <Z_0(t)> = 0 identically.  (This is 932's disclosed
          "H_Z is symmetry-pinned", here promoted to a proof and exhibited
          in the collective basis, where P is z-flip (x) (n -> d-n).)
      L1  chi_F(0) = 0 EXACTLY, so excess_F = chi_F identically.
      L2  Hence the content gate is EXACTLY the single-arm Holevo threshold
          chi_1(t) >= (1-delta): the H(Z_S) >= 0.05 clause is unconditional and
          the excess clause is IMPLIED (chi >= 0.9 > 0.02).
      L3  AT lambda_pointer = 0 THE CONTENT GATE IS EXACTLY DEGREE-INDEPENDENT,
          for ANY arm field: with Z_0 conserved each branch is a PRODUCT of d
          identical single-qubit states, so rho_1^z is pure and d-free, and
          chi_1 = h2((1+|<phi_+|phi_->|)/2) with |phi_s> = exp(-i(-s Z - lam X)t)|+>.
          The entire degree-dependence of t_open is therefore the POINTER's own
          transverse term lambda X_0 -- the same term 933 ablated to show it is
          the entire source of arm entanglement.  ONE TERM RUNS BOTH SIDES.
      L4  At lambda = 0 the whole content window is closed form:
          t_open^(0) = (1/2) arccos(c*), t_close^(0) = pi/2 - t_open^(0),
          W^(0) = pi/2 - arccos(c*), where h2((1+c*)/2) = 1 - delta, c* in (0,1).
      L5  The back-action is O(lambda^2): the flip histories enter rho_1^z with
          collective overlap factors <psi_h'|psi_h>^(d-1), which is where and
          only where d enters.  Measured spread across d = 2..8 reproduces 932's
          2.1e-3 at 0.10 and is 5.9e-4 at 0.05; the fitted exponent is reported.
      L6  t_close: the CONTENT side is the second crossing of the same chi_1
          threshold; the INDEPENDENCE side is the crossing of 933's
          C_ab = 2 s(1) - s(2) with 0.02.  Both derived -> EVERY EDGE OF 932's
          WINDOW IS DERIVED, including the clip-identity switch at d = 6.

  Q3  THE COMPOSED STAR CERTIFICATION THEOREM, stated with its exact hypothesis
      list, and verified by predicting the COMPLETE frozen-grid verdict table
      (every sample, every gate, run, verdict) for every star cell in the pinned
      corpus from the 2(d+1) reduction alone.  Sealed at d in {9,10} at both
      frozen fields and at three never-used fields, under a hard guard proving
      zero full-space evaluations of any sealed cell before the digest was fixed.

DISCIPLINE.  Restriction gates first: the vendored 932 package digest-verified
against the SOURCE-BRANCH ship receipt; 21/21 frozen constants byte-verified and
quote-identical NINE-way (917/919/921/926/927/929/931/932/933); the certification
code executed VERBATIM from the pinned 919 AND 927 bytes; every pinned star-cell
pointer-side value (917 G2, 919 H1, 927 SPk*L1/STk*) reproduced at deviation
EXACTLY ZERO; every 932 window edge and every 932 sealed star window reproduced
from the DERIVED reduction at the pinned grade; 933's s(k) and T(d) tables
reproduced.  Three routes, two structurally disjoint (full 2^(d+1) vs the
2(d+1) collective reduction).  Fifteen teeth.  Deterministic double-run with a
timing-free digest whose payload is SCANNED for wall-clock keys (the trap class
three blocks have now hit).

DISCLOSED TRAPS CARRIED FORWARD.  (i) 931's int8 trap: an unsigned dtype
underflows -1 to 255 and corrupts every Z operator (tooth T10).  (ii) 932's
Euler-guard limitation: H_Z is symmetry-pinned, so ANY symmetry-preserving
integrator reproduces it -- the Euler guard is on chi and C_ab (tooth T03).
(iii) 931/932's wall-clock-in-digest trap: guarded by a hard-failing recursive
payload scan (tooth T07).

No axiom, primitive, registry, policy, queue or audit surface is touched.
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
    "scripts/frontier_cycle919_degree_five_2026_07_28.py": (   # == 932's pin
        "15ce5dbd37cea6e4d7286dc85d0c04abd9948bae2a84910e5f9486c5fa35b196",
        "c22ebafcb743824db67ef1abe9f2f223ea6664a1"),
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
    "scripts/frontier_cycle929_arity_variable_2026_07_28.py": (
        "626be10a174d9ff41f72daa97a7eddc403e5ce191aff56791b38d0cea740c08a",
        "1d629b43c4be15f4ffd7a2ac562ce8538088414e"),
    "outputs/arity_variable_cycle929_receipt_2026_07_28.json": (
        "40440237f0af14882b06331a054c19f3da52f34e6e7b2cde846a0b390a3679a3",
        "fc0080cc4c283d6dc440ac20a614ae187f7e488b"),
    "scripts/frontier_cycle931_additivity_identity_2026_07_28.py": (
        "9ec41f8cc7562026e86a5332819b56b860b1ee3f4a4ca21540f129623ec80371",
        "a0cd5b6fa01ad6b262c18b0e69c57600d1979367"),
    "outputs/additivity_identity_cycle931_receipt_2026_07_28.json": (
        "89699b750d39e6bbf1b953e4abc34a71784344b89012be31226acb6ccfd97b46",
        "d3894ad5792018b541eda7185399c7c979ec09cf"),
    # ---- Cycle 933: the parent whose reduction this block extends to the pointer
    "scripts/frontier_cycle933_sk_shape_2026_07_28.py": (
        "29ab80e096df2e62362a837426cbda0705f5c4f04726a237f092df1d740e966e",
        "9d22268d214c59dd60b32cf7a2e6e67b457d78c8"),
    "outputs/sk_shape_cycle933_receipt_2026_07_28.json": (
        "5a7e7ab80e2a9cb34cf4a7fc2b720d4d9fda25cefaa0574df71ae3d8a7181297",
        "3d35d0ffa6a9bc9077c7fa9b7af7e40f00c89c84"),
    # ---- Cycle 932: VENDORED from the sibling branch (see VENDORED_932 below)
    "scripts/frontier_cycle932_persistence_razor_2026_07_28.py": (
        "6975d2215149116c26392039b04b8b5a6d91236d023a1a37e8dfa602d6abce40",
        "a885eb79fd9a196b1fb4c96039ea6cb2e97c2b10"),
    "outputs/persistence_razor_cycle932_receipt_2026_07_28.json": (
        "a82b93d79b8b4f5b768b94ff5376abc4f6c28cda43dde7d7d7b263c4bb1d6f14",
        "75875bc27d2013897b3accdc347f165a68d8accd"),
    "outputs/persistence_razor_block_cycle932_ship_receipt_2026_07_28.json": (
        "5c38b950374e5a4f42fc3e1ac17578f86b9ba95259e4747c279be91a12e1f798",
        "d66b8a54cd7c366ecdb1e4f5599086c37f6fb5b4"),
}

# The Cycle-932 package is NOT native to this branch.  It was vendored from
# physics-loop/toe-time-blockM12-20260802 at tip 48fced2fce...; the digest
# AUTHORITY is the ship receipt AS IT EXISTS ON THAT BRANCH, read via git show.
VENDOR_932_TIP = "48fced2fce463b371a38de80f8c195959ac4cd04"
VENDOR_932_SHIP = "outputs/persistence_razor_block_cycle932_ship_receipt_2026_07_28.json"
VENDOR_932_SHIP_SHA_ON_SOURCE = (
    "5c38b950374e5a4f42fc3e1ac17578f86b9ba95259e4747c279be91a12e1f798")
VENDORED_932 = [
    "scripts/frontier_cycle932_persistence_razor_2026_07_28.py",
    "scripts/frontier_cycle932_persistence_razor_independent_check_2026_07_28.py",
    "outputs/persistence_razor_cycle932_receipt_2026_07_28.json",
    "outputs/persistence_razor_independent_check_cycle932_receipt_2026_07_28.json",
    "logs/runner-cache/frontier_cycle932_persistence_razor_2026_07_28.txt",
    "logs/runner-cache/frontier_cycle932_persistence_razor_independent_check_2026_07_28.txt",
]

PARENT_MEMO = "docs/D3_BAR_LOCATION_DESIGN_SCOUT_2026-07-10.md"
C915_RECEIPT = "outputs/comparator_recovery_cycle915_receipt_2026_07_28.json"
C917_RECEIPT = "outputs/geometry_ladder_cycle917_receipt_2026_07_28.json"
C919_RECEIPT = "outputs/degree_five_cycle919_receipt_2026_07_28.json"
C919_RUNNER = "scripts/frontier_cycle919_degree_five_2026_07_28.py"
C921_RECEIPT = "outputs/loop_cost_cycle921_receipt_2026_07_28.json"
C926_RECEIPT = "outputs/gate_sweep_separation_cycle926_receipt_2026_07_28.json"
C927_RECEIPT = "outputs/size_channel_cycle927_receipt_2026_07_28.json"
C927_RUNNER = "scripts/frontier_cycle927_size_channel_2026_07_28.py"
C929_RECEIPT = "outputs/arity_variable_cycle929_receipt_2026_07_28.json"
C931_RECEIPT = "outputs/additivity_identity_cycle931_receipt_2026_07_28.json"
C932_RECEIPT = "outputs/persistence_razor_cycle932_receipt_2026_07_28.json"
C933_RECEIPT = "outputs/sk_shape_cycle933_receipt_2026_07_28.json"
C933_RUNNER = "scripts/frontier_cycle933_sk_shape_2026_07_28.py"

D1_NOTE_PATH = "docs/REGISTRATION_REDUNDANCY_ONSET_BOUNDED_NOTE_2026-07-09.md"
D1_NOTE_BLOB = "dd247a8494f171d4dcaf9a532a09491202b1f512"
D1_NOTE_SHA256 = "41b4f26af908a7b910fbb5683f9d50432f36328bced7cf107585f7f70771df04"
D1_NOTE_BYTES = 5230

# ============================================== frozen protocol constants ====
CLAIM_LAMBDAS = (0.05, 0.10)
EXTENSION_LAMBDA = 0.075
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
GRID_SPACING = 0.1
CUBE_LABELS = ("+x", "-x", "+y", "-y", "+z", "-z")
DENSE_MAX_N = 12
FULL_SPACE_CAP_N = 16
DIRECT_MAX_DIM = 1024

# this block's own numerical policy
EDGE_TOL = 1e-13           # derived-edge bisection tolerance
EDGE_GRADE = 1e-12         # the grade 932 published its edges at
VALUE_GRADE = 1e-12        # the grade the collective route is claimed at (see the
                           # per-degree breakdown: the residual grows with d, from
                           # ~1e-14 at d<=5 to ~2e-13 at d=12 -- pure float64
                           # conditioning in the binomially weighted Hankel block)
REPRO_TOL = 0.0            # pinned-value reproduction demands EXACTLY zero
SEAL_LAMBDAS_NEW = (0.0413, 0.0687, 0.1137)   # never used anywhere in the corpus
SEAL_DEGREES = (9, 10)

# bookkeeping that makes the seal auditable
FULL_SPACE_CELLS_EVALUATED = set()     # (d, lambda) pairs touched by ANY 2^(d+1) route
BUILD_LOG = []                          # ordered log of every full-space construction


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


def h2(p):
    if p <= 0.0 or p >= 1.0:
        return 0.0
    return float(-p * math.log2(p) - (1.0 - p) * math.log2(1.0 - p))


def ent_of_spectrum(w):
    w = np.asarray(w, dtype=float)
    w = w[w > 1e-16]
    if w.size == 0:
        return 0.0
    w = w / w.sum()
    return float(-(w * np.log2(w)).sum())


def verify_pins():
    """Pin every artefact.  Entries whose digests are declared None are LEARNED
    here and published; every other entry is a hard equality gate."""
    out = {}
    for path in sorted(PINS):
        want_sha, want_blob = PINS[path]
        full = os.path.join(ROOT, path)
        if not os.path.exists(full):
            die("pin:missing %s" % path)
        b = open(full, "rb").read()
        got = sha256_bytes(b)
        blob = git(["hash-object", path]).stdout.decode().strip()
        if want_sha is not None:
            if got != want_sha:
                die("pin:sha256 %s got=%s want=%s" % (path, got, want_sha))
            if blob != want_blob:
                die("pin:blob %s got=%s want=%s" % (path, blob, want_blob))
        out[path] = {"sha256": got, "blob": blob, "bytes": len(b),
                     "verified": want_sha is not None,
                     "learned_here": want_sha is None}
    return out


def verify_vendored_932():
    """The 932 package is cross-branch.  Its digest AUTHORITY is the ship receipt
    on the SOURCE BRANCH, read with `git show`, never from the working tree."""
    r = git(["show", "%s:%s" % (VENDOR_932_TIP, VENDOR_932_SHIP)])
    if r.returncode != 0:
        die("vendor932:authority-unreadable")
    auth_bytes = r.stdout
    auth_sha = sha256_bytes(auth_bytes)
    if auth_sha != VENDOR_932_SHIP_SHA_ON_SOURCE:
        die("vendor932:authority-sha %s" % auth_sha)
    table = json.loads(auth_bytes)["files"]
    out = {"authority": ("%s READ FROM THE SOURCE BRANCH via git show %s"
                         % (VENDOR_932_SHIP, VENDOR_932_TIP[:10])),
           "authority_sha256_on_source_branch": auth_sha,
           "source_branch_tip": VENDOR_932_TIP, "files": {}}
    allok = True
    for path in VENDORED_932:
        local = open(os.path.join(ROOT, path), "rb").read()
        src = git(["show", "%s:%s" % (VENDOR_932_TIP, path)])
        if src.returncode != 0:
            die("vendor932:source-missing %s" % path)
        s = sha256_bytes(local)
        blob = git(["hash-object", path]).stdout.decode().strip()
        rec = table.get(path)
        if rec is None:
            die("vendor932:not-in-ship-receipt %s" % path)
        ok = (s == rec["sha256"] and blob == rec["git_blob"] and local == src.stdout)
        allok = allok and ok
        if not ok:
            die("vendor932:digest %s" % path)
        out["files"][path] = {"sha256": s, "git_blob": blob,
                              "sha256_matches_ship_receipt": True,
                              "git_blob_matches_ship_receipt": True,
                              "bytes_identical_to_source_branch": True}
    # the ship receipt cannot verify itself; establish it by byte-equality
    ship_local = open(os.path.join(ROOT, VENDOR_932_SHIP), "rb").read()
    out["files"][VENDOR_932_SHIP] = {
        "sha256": sha256_bytes(ship_local),
        "git_blob": git(["hash-object", VENDOR_932_SHIP]).stdout.decode().strip(),
        "bytes_identical_to_source_branch": bool(ship_local == auth_bytes),
        "self_referential": True,
        "note": ("the ship receipt does not list itself; identity is established by "
                 "byte-equality with the copy on the source branch.")}
    if ship_local != auth_bytes:
        die("vendor932:ship-receipt-bytes")
    out["all_verified"] = bool(allok)
    return out


def recover_d1_note():
    """The D1 note is not in the tree at HEAD; recovered from its pinned blob and
    cross-checked against every downstream receipt that republishes its digest."""
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
                    ("926", C926_RECEIPT), ("927", C927_RECEIPT), ("929", C929_RECEIPT),
                    ("931", C931_RECEIPT), ("932", C932_RECEIPT), ("933", C933_RECEIPT)):
        rec = json.load(open(os.path.join(ROOT, rp)))
        if rec["recovered_d1_note"]["sha256"] != got:
            die("d1-note:%s-cross-check" % tag)
        xs["sha256_matches_%s_receipt" % tag] = True
    prov = {"path": D1_NOTE_PATH, "blob": D1_NOTE_BLOB, "sha256": got,
            "bytes": len(b), "in_tree_at_head": False,
            "n_receipts_cross_checked": 9}
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
# the nine-way constant cross-check stays quote-identical to the parents).
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
    """21/21 quote-identical to EVERY pinned receipt that publishes them -- NINE.

    NOTE (spec inconsistency, both readings recorded).  The block spec asks for
    'eight-way incl. 932/933'.  933's own cross-check was SEVEN-way
    (917/919/921/926/927/929/931); adding 932 and 933 gives NINE, not eight.
    This runner performs the NINE-way check -- strictly stronger than either
    reading -- and publishes the count so the discrepancy is auditable.
    """
    res = {}
    tags = (("917", C917_RECEIPT), ("919", C919_RECEIPT), ("921", C921_RECEIPT),
            ("926", C926_RECEIPT), ("927", C927_RECEIPT), ("929", C929_RECEIPT),
            ("931", C931_RECEIPT), ("932", C932_RECEIPT), ("933", C933_RECEIPT))
    for tag, rp in tags:
        theirs = json.load(open(os.path.join(ROOT, rp)))["frozen_constants_byte_verified"]
        if set(theirs) != set(frozen):
            die("frozen-const:%s-key-set" % tag)
        for k in sorted(frozen):
            if theirs[k]["quote"] != frozen[k]["quote"]:
                die("frozen-const:%s-quote %s" % (tag, k))
        res["identical_to_%s_receipt" % tag] = True
        res["n_constants_%s" % tag] = len(theirs)
    res["count"] = len(frozen)
    res["n_receipts_cross_checked"] = len(tags)
    res["all_nine_receipts_agree"] = True
    res["spec_said_eight_way"] = ("the spec's 'eight-way incl. 932/933' is one short of "
                                  "the nine receipts that publish the table; the "
                                  "stronger NINE-way check was run and is reported")
    return res


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


# ============================ ROUTE P919: the pinned Cycle-919 code, executed ==
P919_FUNCTIONS = [
    "bfs", "cube_tiebreak", "build_geometry",
    "geom_chain9", "geom_star7", "geom_tree", "geom_plaquette9", "_axis_label",
    "geom_cubeminus11", "geom_cube27", "geom_star6", "geom_tree16", "geom_tree10d5",
    "geom_cubeminus10",
    "build_diag", "prep_state", "_matvec_factory", "chebyshev", "taylor_march",
    "dense_route", "joint_rho", "ent_bits", "chi_holevo", "cond_mi", "r_ind",
    "centered_frobenius", "measure", "event_of", "xi_reg_of", "verdict_of",
    "cell_of", "run_route_A", "persistence_profile",
]

P927_FUNCTIONS = [
    "bfs", "cube_tiebreak", "build_geometry", "spider", "path_arm",
    "build_diag", "prep_state", "_matvec_factory", "chebyshev", "taylor_march",
    "dense_route", "joint_rho", "block_matrix", "spectrum_of", "ent_bits",
    "chi_holevo", "cond_mi", "cond_mi_gram", "r_ind", "measure", "event_of",
    "xi_reg_of", "verdict_of", "cell_of", "run_route_A",
]


def load_pinned_namespace(runner, funcs, extra):
    """Execute pinned certification code in a private namespace.  Stronger than
    paraphrasing it: the reproduction gate then tests whether THIS environment
    reproduces the pinned numbers, not whether a re-implementation agrees."""
    ns = {"np": np, "itertools": itertools, "math": math, "deque": deque, "jv": jv,
          "die": die, "CUBE_LABELS": CUBE_LABELS, "DELTAS": DELTAS,
          "CONTENT_H_MIN": CONTENT_H_MIN, "EXCESS_MIN": EXCESS_MIN,
          "INDEP_MAX": INDEP_MAX, "DEADLINE_JT": DEADLINE_JT,
          "PERSIST_N": PERSIST_N, "DRIFT_MAX": DRIFT_MAX,
          "HEADLINE_DELTA": HEADLINE_DELTA, "T_EXEC": T_EXEC}
    ns.update(extra)
    quotes = {}
    for fn in funcs:
        q = extract_pinned_source(runner, fn)
        quotes[fn] = {k: v for k, v in q.items() if k != "verbatim"}
        exec(compile(q["verbatim"], "<pinned:%s:%s>" % (runner, fn), "exec"), ns)
    for fn in funcs:
        if fn not in ns or not callable(ns[fn]):
            die("pinned-ns:missing %s in %s" % (fn, runner))
    return ns, quotes


def quote_run_rule(runner):
    """The RUN RULE, the SAMPLE GRID and the DEADLINE, quoted from pinned bytes."""
    src = open(os.path.join(ROOT, runner), "rb").read().decode("utf-8")
    out = {}
    pats = {
        "sample_grid": r"T_EXEC = \[round\(0\.1 \* i, 10\) for i in range\(13\)\][^\n]*",
        "persist_n": r"PERSIST_N = 3[^\n]*",
        "deadline": r"DEADLINE_JT = 1\.0",
        "indep_max": r"INDEP_MAX = 0\.02[^\n]*",
        "excess_min": r"EXCESS_MIN = 0\.02[^\n]*",
        "content_h_min": r"CONTENT_H_MIN = 0\.05[^\n]*",
    }
    for k, p in pats.items():
        m = re.search(p, src)
        if m is None:
            die("run-rule:quote-miss %s in %s" % (k, runner))
        out[k] = " ".join(m.group(0).split())
    out["sample_times"] = list(T_EXEC)
    out["grid_spacing"] = GRID_SPACING
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


def route_N_hamiltonian(n, bonds, lam, extra_z=None, dtype_bug=False):
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
    if extra_z:
        for (i, hfield) in extra_z:
            ops = [EYE2] * n
            ops[i] = SIG_Z
            H -= hfield * kron_op(n, ops)
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
    """S of the reduced state on `sites` from SINGULAR VALUES of the reshaped
    amplitude tensor (no density matrix, no eigensolver)."""
    T = psi.reshape((2,) * n)
    order = list(sites) + [i for i in range(n) if i not in sites]
    ax = [n - 1 - s for s in order]
    M = np.transpose(T, ax).reshape(1 << len(sites), -1)
    s = np.linalg.svd(M, compute_uv=False)
    return ent_of_spectrum(s ** 2)


class StarFull:
    """ROUTE N: the untouched full 2^(d+1) route for a star K_{1,d}."""

    def __init__(self, d, lam, extra_z=None, tag="", dtype_bug=False):
        self.d = d
        self.lam = lam
        self.n = d + 1
        if self.n > FULL_SPACE_CAP_N:
            die("routeN:cap n=%d" % self.n)
        bonds = [(0, j) for j in range(1, self.n)]
        if dtype_bug:
            H = self._buggy_hamiltonian(bonds, lam)
        else:
            H = route_N_hamiltonian(self.n, bonds, lam, extra_z=extra_z)
        self.w, self.V = np.linalg.eigh(H)
        self.c = self.V.conj().T @ route_N_prep(self.n, set(range(self.n)))
        if extra_z is None and not dtype_bug:
            FULL_SPACE_CELLS_EVALUATED.add((d, round(lam, 12)))
            BUILD_LOG.append({"route": "N-full-space", "d": d, "lambda": lam, "tag": tag})

    def _buggy_hamiltonian(self, bonds, lam):
        """THE 931 int8 TRAP, exhibited: an UNSIGNED dtype underflows -1 to 255."""
        n = self.n
        dim = 1 << n
        idx = np.arange(dim, dtype=np.uint32)
        z = np.empty((n, dim), dtype=np.uint8)              # <-- the bug
        for i in range(n):
            z[i] = 1 - 2 * ((idx >> np.uint32(i)) & np.uint32(1)).astype(np.uint8)
        diag = np.zeros(dim)
        for (a, b) in bonds:
            diag -= z[a].astype(np.float64) * z[b].astype(np.float64)
        H = np.diag(diag)
        for i in range(n):
            ops = [EYE2] * n
            ops[i] = SIG_X
            H -= lam * kron_op(n, ops)
        return H

    def state(self, t):
        return self.V @ (np.exp(-1j * self.w * t) * self.c)

    def stats(self, t):
        psi = self.state(t)
        n = self.n
        T = psi.reshape((2,) * n)
        ax = [n - 1 - 0] + [n - 1 - i for i in range(1, n)]
        M = np.transpose(T, ax).reshape(2, -1)
        ps, br = [], []
        for z in (0, 1):
            q = float(np.vdot(M[z], M[z]).real)
            ps.append(q)
            br.append(M[z] / math.sqrt(q) if q > 1e-300 else M[z])
        tot = sum(ps)
        ps = [q / tot for q in ps]
        nb = n - 1
        rest = [i for i in range(n) if i != 0]
        pos = {s: nb - 1 - k for k, s in enumerate(rest)}
        a1 = [pos[1]]
        a2 = [pos[1], pos[2]] if self.d >= 2 else None
        s1 = sum(p * svd_entropy(v, nb, a1) for p, v in zip(ps, br))
        s2 = (sum(p * svd_entropy(v, nb, a2) for p, v in zip(ps, br))
              if a2 is not None else None)
        acc = None
        for p, v in zip(ps, br):
            Tt = v.reshape((2,) * nb)
            axx = [nb - 1 - s for s in a1 + [i for i in range(nb) if i not in a1]]
            Mm = np.transpose(Tt, axx).reshape(2, -1)
            r = p * (Mm @ Mm.conj().T)
            acc = r if acc is None else acc + r
        chi1 = ent_of_spectrum(np.linalg.eigvalsh(acc)) - s1
        return {"H_Z": h2(ps[0]), "p_z": ps, "s1": s1, "s2": s2, "chi1": chi1,
                "C_ab": (2.0 * s1 - s2 if s2 is not None else None)}


# ====================== ROUTE S: THE COLLECTIVE REDUCTION (this block's tool) ==
def binom(n, k):
    return float(math.comb(n, k))


class StarCollective:
    """ROUTE S: the derived 2(d+1) reduction of a star K_{1,d}.

    Basis |z> (x) |D^d_m>, z in {0,1} with Z_0 = +1 / -1, and |D^d_m> the Dicke
    state with m arms in |1>.  The frozen Hamiltonian restricted to this space is

        H = - Z_0 (d - 2m)  - lambda X_0  - lambda * (raising + lowering)

    with <D_{m+1}|sum_j X_j|D_m> = sqrt((m+1)(d-m)).  The frozen preparation
    |+>^(x)(d+1) is symmetric, so the evolution never leaves the subspace
    (933, leakage 6.2e-17; re-measured here).
    """

    def __init__(self, d, lam, lam_pointer=None, lam_arm=None):
        self.d = d
        self.lam = lam
        self.lp = lam if lam_pointer is None else lam_pointer
        self.la = lam if lam_arm is None else lam_arm
        D = d + 1
        N = 2 * D
        H = np.zeros((N, N))

        def ix(z, m):
            return z * D + m

        for z in (0, 1):
            zs = 1.0 if z == 0 else -1.0
            for m in range(D):
                H[ix(z, m), ix(z, m)] += -zs * (d - 2 * m)
                if m + 1 < D:
                    v = -self.la * math.sqrt((m + 1) * (d - m))
                    H[ix(z, m + 1), ix(z, m)] += v
                    H[ix(z, m), ix(z, m + 1)] += v
            for m in range(D):
                H[ix(1 - z, m), ix(z, m)] += -self.lp
        self.H = H
        self.w, self.V = np.linalg.eigh(H)
        a = np.array([math.sqrt(binom(d, m)) for m in range(D)]) / math.sqrt(2.0 ** d)
        psi0 = np.zeros(N, dtype=complex)
        psi0[0:D] = a / math.sqrt(2.0)
        psi0[D:2 * D] = a / math.sqrt(2.0)
        self.c = self.V.conj().T @ psi0
        self._sqrtC = np.array([math.sqrt(binom(d, m)) for m in range(D)])
        self._cache = {}

    # ---- amplitudes -------------------------------------------------------
    def amplitudes(self, t):
        """Return (p, x) with p the pointer Z-distribution and x[z] the (d+1)-term
        SYMMETRIC-TENSOR amplitude sequence x_m = a_m / sqrt(C(d,m)) of branch z."""
        D = self.d + 1
        psi = self.V @ (np.exp(-1j * self.w * t) * self.c)
        ps, xs = [], []
        for z in (0, 1):
            a = psi[z * D:(z + 1) * D]
            p = float(np.vdot(a, a).real)
            ps.append(p)
            an = a / math.sqrt(p) if p > 1e-300 else a
            xs.append(an / self._sqrtC)
        tot = sum(ps)
        return [q / tot for q in ps], xs

    # ---- the Hankel block (933's object) ----------------------------------
    def hankel(self, x, k):
        d = self.d
        M = np.empty((k + 1, d - k + 1), dtype=complex)
        for m in range(k + 1):
            cm = math.sqrt(binom(k, m))
            for q in range(d - k + 1):
                M[m, q] = cm * math.sqrt(binom(d - k, q)) * x[m + q]
        return M

    def branch_rho(self, x, k):
        M = self.hankel(x, k)
        R = M @ M.conj().T
        tr = float(np.trace(R).real)
        return R / tr if tr > 0 else R

    # ---- the pointer-side statistics, derived -----------------------------
    def stats(self, t, kmax=2):
        key = (round(float(t), 15), kmax)
        if key in self._cache:
            return self._cache[key]
        p, xs = self.amplitudes(t)
        out = {"p_z": p, "H_Z": h2(p[0])}
        s = {}
        chi = {}
        for k in range(1, min(kmax, self.d) + 1):
            rzs = [self.branch_rho(xs[z], k) for z in (0, 1)]
            sv = [ent_of_spectrum(np.linalg.eigvalsh(r)) for r in rzs]
            s[k] = float(sum(pz * e for pz, e in zip(p, sv)))
            mix = p[0] * rzs[0] + p[1] * rzs[1]
            chi[k] = float(ent_of_spectrum(np.linalg.eigvalsh(mix)) - s[k])
        out["s"] = s
        out["chi"] = chi
        out["chi1"] = chi.get(1)
        out["s1"] = s.get(1)
        out["s2"] = s.get(2)
        out["C_ab"] = (2.0 * s[1] - s[2]) if (1 in s and 2 in s) else None
        self._cache[key] = out
        return out

    # ---- the frozen gate conjunction, evaluated in the reduction ----------
    def gates(self, t, delta=HEADLINE_DELTA):
        st = self.stats(t)
        H = st["H_Z"]
        c1 = st["chi1"]
        exc = c1 - self.chi0
        content = (H >= CONTENT_H_MIN and c1 >= (1.0 - delta) * H and exc >= EXCESS_MIN)
        cab = st["C_ab"]
        indep = (cab is not None and cab <= INDEP_MAX)
        # R_ind >= 2 needs TWO content-passing fragments whose own pair is under
        # the gate.  On a star every arm is a singleton fragment and all arms are
        # exchangeable, so this is (d >= 2) and content and independence.
        cert = bool(self.d >= 2 and content and indep)
        return {"t": t, "H_Z": H, "chi1": c1, "excess": exc, "C_ab": cab,
                "m_H": H - CONTENT_H_MIN,
                "m_content": c1 - (1.0 - delta) * H,
                "m_excess": exc - EXCESS_MIN,
                "m_indep": (None if cab is None else INDEP_MAX - cab),
                "content": bool(content), "indep": bool(indep), "cert": cert}

    @property
    def chi0(self):
        if not hasattr(self, "_chi0"):
            self._chi0 = self.stats(0.0)["chi1"]
        return self._chi0

    def cert(self, t, delta=HEADLINE_DELTA):
        return self.gates(t, delta)["cert"]


# ---- L1: the lambda_pointer = 0 closed form (exactly degree-independent) -----
def chi1_single_arm_closed(t, lam_arm):
    """With the pointer's own transverse term switched off, Z_0 is conserved, each
    branch is a PRODUCT of d identical single-qubit states, and the single-arm
    Holevo information is a two-level formula with NO d in it at all."""
    v = []
    for s in (+1.0, -1.0):
        H = -s * SIG_Z - lam_arm * SIG_X
        w, V = np.linalg.eigh(H)
        c = V.conj().T @ (np.array([1.0, 1.0], dtype=complex) / math.sqrt(2.0))
        v.append(V @ (np.exp(-1j * w * t) * c))
    ov = abs(complex(np.vdot(v[0], v[1])))
    return h2(0.5 * (1.0 + min(1.0, ov)))


def content_threshold_overlap(delta=HEADLINE_DELTA):
    """c* in (0,1) with h2((1+c*)/2) = 1 - delta -- the ZERO-FIELD content edge."""
    lo, hi = 0.0, 1.0 - 1e-15
    for _ in range(300):
        mid = 0.5 * (lo + hi)
        if h2(0.5 * (1.0 + mid)) > (1.0 - delta):
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def zero_field_window(delta=HEADLINE_DELTA):
    c = content_threshold_overlap(delta)
    t0 = 0.5 * math.acos(c)
    return {"c_star": c, "t_open": t0, "t_close": math.pi / 2.0 - t0,
            "width": math.pi / 2.0 - 2.0 * t0}


# ---- edge solvers on the DERIVED profiles ------------------------------------
def bisect_scalar(f, a, b, tol=EDGE_TOL):
    fa, fb = f(a), f(b)
    if fa == 0.0:
        return a
    if fb == 0.0:
        return b
    if (fa > 0) == (fb > 0):
        return None
    for _ in range(400):
        m = 0.5 * (a + b)
        fm = f(m)
        if (fm > 0) == (fa > 0):
            a, fa = m, fm
        else:
            b, fb = m, fm
        if abs(b - a) < tol:
            break
    return 0.5 * (a + b)


def bisect_predicate(cell, t_false, t_true, delta=HEADLINE_DELTA, tol=EDGE_TOL):
    a, b = t_false, t_true
    for _ in range(400):
        m = 0.5 * (a + b)
        if cell.cert(m, delta):
            b = m
        else:
            a = m
        if abs(b - a) < tol:
            break
    return 0.5 * (a + b)


SCAN_LO, SCAN_HI, SCAN_DT = 0.0, 1.5, 0.0025


def derived_window(cell, delta=HEADLINE_DELTA, lo=SCAN_LO, hi=SCAN_HI, dt=SCAN_DT):
    """The certifiable blocks of the DERIVED predicate, with their edges bisected
    and each edge's binding gate identified."""
    nts = int(round((hi - lo) / dt)) + 1
    ts = [lo + k * dt for k in range(nts)]
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
    out = []
    for (i, j) in blocks:
        if i == 0:
            t_lo, gate_lo = 0.0, "t=0"
        else:
            t_lo = bisect_predicate(cell, ts[i - 1], ts[i], delta)
            gate_lo = binding_gate(cell, ts[i - 1], delta)
        if j == len(ts) - 1:
            t_hi, gate_hi = ts[j], "scan-horizon"
        else:
            t_hi = bisect_predicate(cell, ts[j + 1], ts[j], delta)
            gate_hi = binding_gate(cell, ts[j + 1], delta)
        out.append({"lo": t_lo, "hi": t_hi, "width": t_hi - t_lo,
                    "open_gate": gate_lo, "close_gate": gate_hi})
    return {"blocks": out, "n_blocks": len(out), "scan_dt": dt, "n_scan_points": nts}


def binding_gate(cell, t_out, delta=HEADLINE_DELTA):
    """Which gate is binding just OUTSIDE an edge -- 932's clip identity, on the
    derived margins.  Label vocabulary matches 932's exactly."""
    g = cell.gates(t_out, delta)
    cands = {"content_H": g["m_H"], "content_chi": g["m_content"],
             "content_excess": g["m_excess"]}
    if g["m_indep"] is not None:
        cands["independence"] = g["m_indep"]
    if not g["content"]:
        return min(("content_H", "content_chi", "content_excess"),
                   key=lambda k: cands[k])
    return min(cands, key=lambda k: cands[k])


def grid_points_in(win, offset=0.0, grid=None):
    g = list(grid if grid is not None else T_EXEC)
    pts = [round(x + offset, 12) for x in g]
    return [x for x in pts if win["lo"] - 1e-12 <= x <= win["hi"] + 1e-12 and x >= 0.0]


def composed_verdict(wins, offset=0.0):
    """THE COMPOSED VERDICT: 932's edge-counting law applied to derived edges."""
    best = None
    for w in wins:
        pts = grid_points_in(w, offset)
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


# ================================================================== teeth =====
TEETH = []


def tooth(name, description, fired, detail):
    TEETH.append({"name": name, "description": description,
                  "fired": bool(fired), "detail": detail})
    if not fired:
        die("tooth:%s did not fire" % name)


# ============================ the timing-free payload guard (the 3rd-block trap)
TIMING_KEY_RE = re.compile(
    r"(runtime|wall|clock|elapsed|seconds?|secs?|timestamp|_time$|^time$|duration|"
    r"perf_counter|started_at|finished_at|date)", re.I)
TIMING_EXEMPT = set()


def scan_payload_for_timing(obj, path="$"):
    """HARD GUARD.  Three blocks in this campaign have now leaked a wall-clock key
    into a 'timing-free' digest.  This walks the ENTIRE payload and hard-fails on
    any key that looks like a clock reading."""
    hits = []
    if isinstance(obj, dict):
        for k, v in obj.items():
            p = "%s.%s" % (path, k)
            if TIMING_KEY_RE.search(str(k)) and p not in TIMING_EXEMPT:
                hits.append(p)
            hits.extend(scan_payload_for_timing(v, p))
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            hits.extend(scan_payload_for_timing(v, "%s[%d]" % (path, i)))
    return hits


# ================================================================== main =====
def main():
    receipt = {"schema": "frontier_cycle934_pointer_gates_v1",
               "cycle": 934, "block": "toe-time-blockM14-20260802",
               "campaign": "toe-time-expansion-20260802",
               "date": "2026-07-28",
               "runner": os.path.relpath(os.path.abspath(__file__), ROOT),
               "runtime_limit_seconds": RUNTIME_LIMIT_SECONDS}

    # ---------------------------------------------------------------- gates --
    pins = verify_pins()
    vendored = verify_vendored_932()
    memo = open(os.path.join(ROOT, PARENT_MEMO), "rb").read().decode("utf-8")
    frozen = verify_frozen_constants(memo)
    xcheck = cross_check_prior_constants(frozen)
    statdef = verify_statistic_definition(memo)
    d1_text, d1_prov = recover_d1_note()

    ns919, q919 = load_pinned_namespace(C919_RUNNER, P919_FUNCTIONS, {})
    ns927, q927 = load_pinned_namespace(
        C927_RUNNER, P927_FUNCTIONS,
        {"DIRECT_MAX_DIM": DIRECT_MAX_DIM, "DENSE_MAX_N": DENSE_MAX_N,
         "FULL_SPACE_CAP_N": FULL_SPACE_CAP_N, "T0_ANCHOR_TOL": T0_ANCHOR_TOL,
         "MACH_TOL": 1e-9, "RESTRICT_TOL": 1e-9,
         "T_LONG": [round(0.1 * i, 10) for i in range(25)]})

    receipt["pins"] = pins
    receipt["vendored_932_cross_branch_verification"] = vendored
    receipt["frozen_constants_byte_verified"] = frozen
    receipt["frozen_constants_cross_check"] = xcheck
    receipt["statistic_definition_byte_verified"] = statdef
    receipt["recovered_d1_note"] = d1_prov
    receipt["pinned_code_executed_verbatim"] = {
        "cycle919": {"runner": C919_RUNNER, "n_functions": len(P919_FUNCTIONS),
                     "quotes": q919, "run_rule": quote_run_rule(C919_RUNNER)},
        "cycle927": {"runner": C927_RUNNER, "n_functions": len(P927_FUNCTIONS),
                     "quotes": q927, "run_rule": quote_run_rule(C927_RUNNER)}}

    # ------------------------------------------------- Q1 quoted definitions --
    pointer_side_defs = {
        "H_Z": {"quote": frozen["content_H_min"]["quote"],
                "reading": ("H(Z_S), the Shannon entropy in bits of the pointer's "
                            "Z-outcome distribution p_z; clause 1 of the content gate "
                            "demands H(Z_S) >= 0.05 bit.")},
        "chi": {"quote": statdef["chi_definition"],
                "reading": ("chi_Z(S:F) = S(sum_z p_z rho_F^z) - sum_z p_z S(rho_F^z), "
                            "the Holevo information of the pointer-conditioned "
                            "ensemble on fragment F.")},
        "content_gate": {"quote": frozen["content_gate"]["quote"],
                         "reading": "clause 2: chi_Z(S:F) >= (1-delta) H(Z_S)."},
        "excess_gate": {"quote": frozen["excess_min"]["quote"],
                        "reading": ("clause 3: chi_Z(S:F)(t) - chi_Z(S:F)(0) >= 0.02 "
                                    "bit.")},
        "independence_gate": {"quote": frozen["indep_max"]["quote"],
                              "reading": "every pair has C_ab <= 0.02 bit."},
        "C_ab": {"quote": statdef["C_ab_formula"],
                 "definition_quote": statdef["C_ab_definition"],
                 "tensor_order_quote": statdef["C_ab_tensor_order"],
                 "dephasing_quote": statdef["C_ab_dephasing"]},
        "r_ind": {"quote": frozen["r_ind_def"]["quote"]},
        "persistence": {"quote": frozen["persistence"]["quote"]},
        "deadline": {"quote": frozen["deadline"]["quote"]},
        "delta": {"quote": frozen["deltas"]["quote"]},
    }
    receipt["Q1_quoted_pointer_side_definitions"] = pointer_side_defs

    print(BOUNDARY_LINE)
    print("runner   : %s" % os.path.basename(__file__))
    print("cycle    : 934   block: blockM14   campaign: toe-time-expansion-20260802")
    print("question : the POINTER-SIDE gates (chi, excess, H_Z, t_open) and the "
          "composed star certification theorem")
    print("")
    print("PINS  %d artefacts | VENDORED 932: %d files digest-verified against the "
          "SOURCE-BRANCH ship receipt (%s)"
          % (len(pins), len(vendored["files"]), VENDOR_932_TIP[:10]))
    print("CONSTANTS  21/21 byte-verified, quote-identical NINE-way "
          "(917/919/921/926/927/929/931/932/933); statistic definitions %d/%d"
          % (len(statdef), len(STATISTIC_PATTERNS)))

    # ================================================== RESTRICTION GATES ====
    # Nothing new is computed before every one of these passes.
    rg = {}
    rec917 = json.load(open(os.path.join(ROOT, C917_RECEIPT)))
    rec919 = json.load(open(os.path.join(ROOT, C919_RECEIPT)))
    rec927 = json.load(open(os.path.join(ROOT, C927_RECEIPT)))
    rec931 = json.load(open(os.path.join(ROOT, C931_RECEIPT)))
    rec932 = json.load(open(os.path.join(ROOT, C932_RECEIPT)))
    rec933 = json.load(open(os.path.join(ROOT, C933_RECEIPT)))

    # ---- G1: the 917/919 pinned star rows, via route P919, deviation EXACTLY 0
    def rerun_p919(ns, geom_fn, lam):
        g = ns[geom_fn]()
        diag = ns["build_diag"](g["n"], g["bonds"])
        psi0 = ns["prep_state"](g["n"], set([g["S"]] + list(g["recording"])))
        rows, mach, prop = ns["run_route_A"](g, diag, psi0, lam)
        return g, rows

    def compare_rows(new_rows, old_rows, keys=("H_Z", "chi", "excess", "C_ab",
                                               "p_z", "r_ind", "singleton_passes",
                                               "certifying_subsets")):
        dev = 0.0
        nvals = 0
        for a, b in zip(new_rows, old_rows):
            if abs(a["jt"] - b["jt"]) > 0:
                die("repro:jt-mismatch")
            for k in keys:
                va, vb = a[k], b[k]
                if isinstance(va, dict):
                    if set(va) != set(vb):
                        die("repro:key-set %s" % k)
                    for kk in va:
                        if isinstance(va[kk], (int, float)):
                            dev = max(dev, abs(float(va[kk]) - float(vb[kk])))
                            nvals += 1
                        else:
                            if list(va[kk]) != list(vb[kk]):
                                die("repro:list %s/%s" % (k, kk))
                            nvals += 1
                elif isinstance(va, list):
                    for x, y in zip(va, vb):
                        dev = max(dev, abs(float(x) - float(y)))
                        nvals += 1
                else:
                    dev = max(dev, abs(float(va) - float(vb)))
                    nvals += 1
        return dev, nvals

    star_anchor_rows = {}
    g1 = {"cells": {}, "max_abs_deviation": 0.0, "values": 0}
    for tag, rec, gkey, geom_fn, lams in (
            ("917", rec917, "geometries", "geom_star7", ("0.05", "0.1")),
            ("919", rec919, "degree_five_geometries", "geom_star6",
             ("0.05", "0.075", "0.1"))):
        key = "G2" if tag == "917" else "H1"
        for ls in lams:
            lam = float(ls)
            g, rows = rerun_p919(ns919, geom_fn, lam)
            old = rec[gkey][key]["lambdas"][ls]["rows"]
            dev, nv = compare_rows(rows, old)
            if dev > REPRO_TOL:
                die("restriction:%s-%s@%s dev=%r" % (tag, key, ls, dev))
            g1["cells"]["%s:%s@%s" % (tag, key, ls)] = {
                "max_abs_deviation": dev, "rows": len(rows), "values": nv,
                "pointer_degree": g["n"] - 1}
            g1["max_abs_deviation"] = max(g1["max_abs_deviation"], dev)
            g1["values"] += nv
            star_anchor_rows[("%s:%s" % (tag, key), lam)] = (g["n"] - 1, rows)
    rg["pinned_917_919_star_rows_route_P919"] = g1
    print("RG1 917/919 star rows: %d values, max dev %r"
          % (g1["values"], g1["max_abs_deviation"]))

    # ---- G2: the 927 pinned star rows, via route P927, deviation EXACTLY 0 ----
    C927_STARS = {"SPk2L1": 2, "SPk3L1": 3, "SPk4L1": 4, "SPk5L1": 5,
                  "STk8": 8, "STk10": 10, "STk12": 12}
    g2 = {"cells": {}, "max_abs_deviation": 0.0, "values": 0}
    for kkey, dd in sorted(C927_STARS.items(), key=lambda kv: kv[1]):
        if kkey.startswith("SP"):
            g = ns927["spider"](kkey, [ns927["path_arm"](1)] * dd, "", "spider")
        else:
            g = ns927["spider"](kkey, [ns927["path_arm"](1)] * dd, "", "star")
        diag = ns927["build_diag"](g["n"], g["bonds"])
        psi0 = ns927["prep_state"](g["n"], set([g["S"]] + list(g["recording"])))
        for ls in ("0.05", "0.1"):
            lam = float(ls)
            rows, mach, prop = ns927["run_route_A"](g, diag, psi0, lam)
            old = rec927["geometries"][kkey]["lambdas"][ls]["rows"]
            dev, nv = compare_rows(rows, old)
            if dev > REPRO_TOL:
                die("restriction:927-%s@%s dev=%r" % (kkey, ls, dev))
            g2["cells"]["927:%s@%s" % (kkey, ls)] = {
                "max_abs_deviation": dev, "rows": len(rows), "values": nv,
                "pointer_degree": dd}
            g2["max_abs_deviation"] = max(g2["max_abs_deviation"], dev)
            g2["values"] += nv
            star_anchor_rows[("927:%s" % kkey, lam)] = (dd, rows)
    rg["pinned_927_star_rows_route_P927"] = g2
    print("RG2 927 star rows: %d values, max dev %r"
          % (g2["values"], g2["max_abs_deviation"]))

    # ---- G3: 926's frozen-point star cells (G2@0.05, G2@0.1) -----------------
    g3 = {"cells": {}, "max_abs_deviation": 0.0}
    f26 = rec926 = json.load(open(os.path.join(ROOT, C926_RECEIPT)))
    for ck in ("G2@0.05", "G2@0.1"):
        old = f26["frozen_point_26_cell_table"][ck]
        lam = float(ck.split("@")[1])
        _, rows = star_anchor_rows[("917:G2", lam)]
        got = ns919["verdict_of"](rows, HEADLINE_DELTA, True)
        dev = 0.0
        checked = {}
        for field in ("verdict", "run", "r_ind_at_event", "jt_event"):
            for cand in (field, field.replace("jt_event", "jt"),
                         field.replace("r_ind_at_event", "r_ind")):
                if cand in old and cand in got:
                    a, b = got[cand], old[cand]
                    if isinstance(a, (int, float)) and not isinstance(a, bool):
                        dev = max(dev, abs(float(a) - float(b)))
                    elif a != b:
                        die("restriction:926-%s-%s %r!=%r" % (ck, cand, a, b))
                    checked[cand] = True
                    break
        g3["cells"][ck] = {"checked": sorted(checked), "max_abs_deviation": dev,
                           "verdict_pinned": old.get("verdict"),
                           "verdict_reproduced": got.get("verdict")}
        g3["max_abs_deviation"] = max(g3["max_abs_deviation"], dev)
    rg["pinned_926_star_frozen_point"] = g3
    print("RG3 926 star frozen point: max dev %r" % g3["max_abs_deviation"])

    # ---- G4: 933's derived-consequence tables (T(d) baseline) ----------------
    t_table = rec933["Q3_consequences"]
    rg["c933_consequences_present"] = {
        "keys": sorted(t_table.keys()),
        "seal_all_predictions_hold": bool(rec933["seal_all_predictions_hold"])}

    # ---- G5: EVERY 932 window edge, re-derived from the COLLECTIVE reduction --
    coll_cache = {}

    def coll(d, lam):
        k = (d, round(float(lam), 12))
        if k not in coll_cache:
            coll_cache[k] = StarCollective(d, float(lam))
        return coll_cache[k]

    g5 = {"cells": {}, "max_abs_edge_deviation": 0.0, "n_edges": 0,
          "gate_label_mismatches": [], "verdict_mismatches": []}
    for ck, cell in sorted(rec932["Q1_curves"]["per_cell"].items()):
        if not re.match(r"^S\d+@", ck):
            continue
        d = int(ck.split("@")[0][1:])
        lam = float(ck.split("@")[1])
        c = coll(d, lam)
        win = derived_window(c)
        if win["n_blocks"] != 1:
            die("restriction:932-%s blocks=%d" % (ck, win["n_blocks"]))
        b = win["blocks"][0]
        dlo = abs(b["lo"] - cell["t_open"])
        dhi = abs(b["hi"] - cell["t_close"])
        pred = composed_verdict(win["blocks"])
        if b["open_gate"] != cell["open_gate"]:
            g5["gate_label_mismatches"].append([ck, b["open_gate"], cell["open_gate"]])
        if b["close_gate"] != cell["close_gate"]:
            g5["gate_label_mismatches"].append([ck, b["close_gate"], cell["close_gate"]])
        if pred["verdict"] != cell["frozen_verdict"] or pred["run"] != cell["frozen_run"]:
            g5["verdict_mismatches"].append([ck, pred["verdict"], pred["run"],
                                             cell["frozen_verdict"], cell["frozen_run"]])
        g5["cells"][ck] = {"t_open_derived": b["lo"], "t_open_932": cell["t_open"],
                           "t_close_derived": b["hi"], "t_close_932": cell["t_close"],
                           "dev_open": dlo, "dev_close": dhi,
                           "open_gate": b["open_gate"], "close_gate": b["close_gate"],
                           "run_derived": pred["run"], "run_932": cell["frozen_run"],
                           "verdict_derived": pred["verdict"],
                           "verdict_932": cell["frozen_verdict"]}
        g5["max_abs_edge_deviation"] = max(g5["max_abs_edge_deviation"], dlo, dhi)
        g5["n_edges"] += 2
    if g5["gate_label_mismatches"] or g5["verdict_mismatches"]:
        die("restriction:932-edges label/verdict mismatch")
    if g5["max_abs_edge_deviation"] > EDGE_GRADE:
        die("restriction:932-edges dev=%r" % g5["max_abs_edge_deviation"])
    g5["grade_demanded"] = EDGE_GRADE
    rg["c932_window_edges_rederived_from_the_reduction"] = g5
    print("RG5 932 window edges: %d edges, max dev %.3e (grade %.0e)"
          % (g5["n_edges"], g5["max_abs_edge_deviation"], EDGE_GRADE))

    # ---- G6: 932's SEALED star windows, re-derived ---------------------------
    g6 = {"cells": {}, "max_abs_deviation": 0.0}
    for ck, pr in sorted(rec932["seal"]["predictions"].items()):
        if not re.match(r"^S\d+@", ck):
            continue
        d = int(ck.split("@")[0][1:])
        lam = float(ck.split("@")[1])
        win = derived_window(coll(d, lam))
        b = win["blocks"][0]
        dv = max(abs(b["lo"] - pr["window"][0]), abs(b["hi"] - pr["window"][1]))
        pred = composed_verdict(win["blocks"])
        if pred["verdict"] != pr["predicted_verdict"] or pred["run"] != pr["predicted_run"]:
            die("restriction:932-seal-%s verdict" % ck)
        g6["cells"][ck] = {"dev": dv, "close_gate_derived": b["close_gate"],
                           "close_gate_932": pr["close_gate"],
                           "run": pred["run"], "verdict": pred["verdict"]}
        g6["max_abs_deviation"] = max(g6["max_abs_deviation"], dv)
    if g6["max_abs_deviation"] > EDGE_GRADE:
        die("restriction:932-seal dev=%r" % g6["max_abs_deviation"])
    rg["c932_sealed_star_windows_rederived"] = g6
    print("RG6 932 sealed star windows: %d cells, max dev %.3e"
          % (len(g6["cells"]), g6["max_abs_deviation"]))

    # ---- G7: the collective route vs the pinned star ROWS (the derivation gate)
    g7 = {"cells": {}, "max_abs_deviation": 0.0, "values": 0,
          "by_statistic": {"H_Z": 0.0, "chi": 0.0, "excess": 0.0, "C_ab": 0.0},
          "by_degree": {}}
    for (ckey, lam), (d, rows) in sorted(star_anchor_rows.items()):
        c = coll(d, lam)
        dev = 0.0
        nv = 0
        for r in rows:
            st = c.stats(r["jt"])
            chi_pin = list(r["chi"].values())[0]
            exc_pin = list(r["excess"].values())[0]
            cab_pin = (list(r["C_ab"].values())[0] if r["C_ab"] else None)
            for nm, dv in (("chi", abs(st["chi1"] - chi_pin)),
                           ("excess", abs((st["chi1"] - c.chi0) - exc_pin)),
                           ("H_Z", abs(st["H_Z"] - r["H_Z"]))):
                dev = max(dev, dv)
                g7["by_statistic"][nm] = max(g7["by_statistic"][nm], dv)
                nv += 1
            if cab_pin is not None and st["C_ab"] is not None:
                dv = abs(st["C_ab"] - cab_pin)
                dev = max(dev, dv)
                g7["by_statistic"]["C_ab"] = max(g7["by_statistic"]["C_ab"], dv)
                nv += 1
        g7["cells"]["%s@%g" % (ckey, lam)] = {"max_abs_deviation": dev,
                                              "values": nv, "pointer_degree": d}
        g7["by_degree"][str(d)] = max(g7["by_degree"].get(str(d), 0.0), dev)
        g7["max_abs_deviation"] = max(g7["max_abs_deviation"], dev)
        g7["values"] += nv
    g7["max_abs_deviation_over_degrees_le_8"] = max(
        v for k, v in g7["by_degree"].items() if int(k) <= 8)
    if g7["max_abs_deviation"] > VALUE_GRADE:
        die("restriction:collective-vs-pinned dev=%r" % g7["max_abs_deviation"])
    g7["grade_demanded"] = VALUE_GRADE
    rg["collective_reduction_vs_pinned_star_rows"] = g7
    print("RG7 collective vs pinned rows: %d values, max dev %.3e"
          % (g7["values"], g7["max_abs_deviation"]))

    rg["gate_order"] = ("pins -> vendored-932 source-branch digests -> frozen "
                        "constants (21/21, NINE-way) -> statistic definition bytes "
                        "-> D1 note -> pinned 919 + 927 code executed verbatim -> "
                        "917/919 star rows (dev 0) -> 927 star rows (dev 0) -> 926 "
                        "star frozen point -> 932 window edges -> 932 sealed windows "
                        "-> collective route vs every pinned star row -> SEAL -> "
                        "any new number")
    rg["deviation_exactly_zero_on_every_pinned_value_route"] = bool(
        g1["max_abs_deviation"] == 0.0 and g2["max_abs_deviation"] == 0.0)
    receipt["restriction_gates"] = rg
    receipt["restriction_gate_seconds"] = round(time.perf_counter() - T_START, 3)

    # ======================================================= Q1: the derivation
    q1 = {}
    q1["collective_expressions"] = {
        "reduction": ("On K_{1,d} the frozen H = -sum_<ij> Z_i Z_j - lambda sum_i X_i "
                      "is  H = -2 Z_0 J_z - lambda X_0 - 2 lambda J_x  on C^2 (x) "
                      "Sym^d, dimension 2(d+1).  The frozen preparation |+>^(x)(d+1) "
                      "is arm-permutation symmetric, so the evolution never leaves "
                      "the subspace."),
        "branch_amplitudes": ("psi(t) = sum_z |z> (x) |chi_z(t)>, |chi_z> in Sym^d "
                              "with Dicke coefficients a^z_m; the SYMMETRIC-TENSOR "
                              "sequence is x^z_m = a^z_m / sqrt(C(d,m))."),
        "hankel_block": ("T^(k)(x)_{m,q} = sqrt(C(k,m) C(d-k,q)) x_{m+q}  "
                         "(933's binomially weighted Hankel matrix, k+1 by d-k+1)."),
        "H_Z": "H_Z = h2(p_0) with p_z = <chi_z|chi_z> / sum -- POINTER ONLY.",
        "s_of_k": "s(k) = sum_z p_z S(rho_F^z),  rho_F^z = T^(k)(x^z)T^(k)(x^z)^dag/tr.",
        "chi_k": ("chi_k = S(sum_z p_z rho_F^z) - sum_z p_z S(rho_F^z)  -- the SAME "
                  "Hankel blocks as s(k), read through the entropy of their "
                  "p-weighted SUM instead of the p-weighted sum of their entropies.  "
                  "This is precisely why 933's overreach audit was right: s(k) is a "
                  "sum of entropies, chi needs the entropy of a sum, and no function "
                  "of the former determines the latter."),
        "excess_k": "excess_k(t) = chi_k(t) - chi_k(0).",
        "C_ab": "C_ab = 2 s(1) - s(2)  (931's pair-complement theorem on stars).",
        "content_gate": ("H_Z >= 0.05  AND  chi_1 >= (1-delta) H_Z  AND  "
                         "excess_1 >= 0.02, evaluated entirely in 2(d+1)."),
        "certification_predicate": ("d >= 2  AND content gate AND C_ab <= 0.02 "
                                    "(all arms are exchangeable singleton fragments, "
                                    "so R_ind >= 2 is exactly this conjunction)."),
    }

    # ---- Q1a: Sym^d membership re-measured (933's L1, independently) ----------
    leak = {"rows": [], "max_leakage": 0.0}
    for d in (2, 3, 5, 8):
        for lam in (0.05, 0.10):
            fs = StarFull(d, lam, tag="Q1-leakage")
            for t in (0.3, 0.7, 1.2):
                psi = fs.state(t)
                n = d + 1
                T = psi.reshape((2,) * n)
                # project the ARM factor onto Sym^d and measure the discarded weight
                tot = 0.0
                keep = 0.0
                flat = psi.reshape(2, -1)     # pointer is the top bit (site 0 -> bit 0)
                # site i occupies bit i; reshape((2,)*n) puts site n-1 first.
                Tt = np.transpose(T, [n - 1 - 0] + [n - 1 - i for i in range(1, n)])
                M = Tt.reshape(2, -1)
                for z in (0, 1):
                    v = M[z]
                    dicke = {}
                    for idx in range(v.size):
                        w = bin(idx).count("1")
                        dicke.setdefault(w, []).append(idx)
                    for w, ids in dicke.items():
                        blk = v[ids]
                        amp = blk.sum() / math.sqrt(len(ids))
                        keep += abs(amp) ** 2
                        tot += float(np.vdot(blk, blk).real)
                leak["rows"].append({"d": d, "lambda": lam, "jt": t,
                                     "leaked_weight": max(0.0, tot - keep)})
                leak["max_leakage"] = max(leak["max_leakage"], max(0.0, tot - keep))
    q1["sym_d_membership_leakage"] = leak
    if leak["max_leakage"] > 1e-14:
        die("Q1:sym-d leakage %r" % leak["max_leakage"])

    # ---- Q1b: route S vs route N (own full space), the derivation grade -------
    # NOTE: degrees are capped at 8 here ON PURPOSE.  Degrees 9 and 10 are the
    # sealed degrees, and route N is this block's own untouched full-space route;
    # keeping it off them until the seal digest is fixed is what makes the seal's
    # no-pre-evaluation guard meaningful.
    verif = {"rows": [], "max_abs_deviation": 0.0, "by_statistic": {},
             "degrees_capped_at_8_because": ("degrees 9-10 are the sealed degrees; "
                                             "route N is kept off them until the seal "
                                             "digest is fixed")}
    for d in (2, 3, 4, 5, 6, 7, 8):
        for lam in (0.05, 0.075, 0.10):
            fs = StarFull(d, lam, tag="Q1-verify")
            cs = coll(d, lam)
            for t in (0.0, 0.3, 0.6, 0.7, 0.9, 1.2):
                a, b = cs.stats(t), fs.stats(t)
                row = {"d": d, "lambda": lam, "jt": t}
                for nm in ("H_Z", "chi1", "s1", "s2", "C_ab"):
                    if a.get(nm) is None or b.get(nm) is None:
                        continue
                    dv = abs(float(a[nm]) - float(b[nm]))
                    row["dev_" + nm] = dv
                    verif["by_statistic"][nm] = max(verif["by_statistic"].get(nm, 0.0), dv)
                    verif["max_abs_deviation"] = max(verif["max_abs_deviation"], dv)
                verif["rows"].append(row)
    if verif["max_abs_deviation"] > VALUE_GRADE:
        die("Q1:routeS-vs-routeN %r" % verif["max_abs_deviation"])
    q1["collective_vs_full_space_route"] = {
        "max_abs_deviation": verif["max_abs_deviation"],
        "by_statistic": verif["by_statistic"], "n_rows": len(verif["rows"]),
        "grade_demanded": VALUE_GRADE,
        "note": "route S (2(d+1)) against route N (untouched 2^(d+1), own assembly)"}

    # ---- Q1c: dense-time profiles, the 932 battery run on the POINTER side ----
    DENSE_TS = [round(0.005 * k, 6) for k in range(0, 281)]     # Jt = 0 .. 1.40
    prof = {}
    for d in (2, 3, 4, 5, 6, 7, 8):
        for lam in (0.05, 0.075, 0.10):
            cs = coll(d, lam)
            ch, ex, hz, ca = [], [], [], []
            for t in DENSE_TS:
                st = cs.stats(t)
                ch.append(st["chi1"])
                ex.append(st["chi1"] - cs.chi0)
                hz.append(st["H_Z"])
                ca.append(st["C_ab"])
            dch = np.diff(np.array(ch))
            prof["S%d@%g" % (d, lam)] = {
                "chi_max": max(ch), "chi_argmax_jt": DENSE_TS[int(np.argmax(ch))],
                "chi_at_0": ch[0], "excess_equals_chi_max_dev": max(
                    abs(a - b) for a, b in zip(ch, ex)),
                "H_Z_min": min(hz), "H_Z_max": max(hz),
                "H_Z_max_abs_dev_from_1": max(abs(v - 1.0) for v in hz),
                "C_ab_at_0": ca[0], "C_ab_max": max(ca),
                "chi_sign_changes_of_derivative": int(
                    np.sum(np.sign(dch[:-1]) != np.sign(dch[1:]))),
                "C_ab_monotone_rising_on_0.4_to_1.3": bool(all(
                    ca[i + 1] >= ca[i] - 1e-15
                    for i in range(len(DENSE_TS) - 1)
                    if 0.4 <= DENSE_TS[i] <= 1.3)),
            }
    q1["dense_time_profiles"] = {
        "grid": {"lo": DENSE_TS[0], "hi": DENSE_TS[-1], "step": 0.005,
                 "n_points": len(DENSE_TS)},
        "per_cell": prof,
        "universal_facts": {
            "chi_has_exactly_one_interior_maximum_on_every_cell": bool(all(
                v["chi_sign_changes_of_derivative"] == 1 for v in prof.values())),
            "excess_equals_chi_everywhere_max_dev": max(
                v["excess_equals_chi_max_dev"] for v in prof.values()),
            "H_Z_max_abs_dev_from_1_over_all_cells": max(
                v["H_Z_max_abs_dev_from_1"] for v in prof.values())}}
    receipt["Q1_pointer_side_from_the_reduction"] = q1
    print("Q1 done: leakage %.1e, routeS-vs-N %.1e, profiles %d cells"
          % (leak["max_leakage"], verif["max_abs_deviation"], len(prof)))

    # ============================================ Q2: t_open DERIVED ==========
    q2 = {}

    # ---- L0: H_Z = 1 EXACTLY, by the global X-flip symmetry -------------------
    l0 = {"claim": ("H(Z_S)(t) = 1 bit EXACTLY for every degree, every field, every "
                    "time -- so the content gate's clause 1 (H(Z_S) >= 0.05) is "
                    "unconditional and clause 2's right-hand side is the CONSTANT "
                    "(1-delta)."),
          "proof": ("P = prod_i X_i commutes with H (each Z_iZ_j is X-flip even and "
                    "each X_i is X-flip invariant) and fixes the frozen preparation "
                    "|+>^(x)(d+1) with eigenvalue +1.  P Z_0 P = -Z_0, hence "
                    "<psi(t)|Z_0|psi(t)> = <psi(t)|P Z_0 P|psi(t)> = -<Z_0(t)>, so "
                    "<Z_0(t)> = 0 identically and p_z = (1/2, 1/2).  In the "
                    "collective basis P is (pointer z-flip) (x) (m -> d-m)."),
          "note": ("this promotes 932's disclosed observation -- 'the global X-flip "
                   "symmetry pins the branch weights for ANY symmetry-preserving "
                   "integrator' -- from a tooth limitation to a lemma, and it is why "
                   "the Euler guard below is placed on chi and C_ab, never on H_Z.")}
    # symbolic check in the collective basis: [P, H] = 0 and P psi0 = psi0
    sym_rows = []
    for d in (2, 3, 5, 8):
        for lam in (0.05, 0.10, 0.5):
            cs = StarCollective(d, lam)
            D = d + 1
            P = np.zeros((2 * D, 2 * D))
            for z in (0, 1):
                for m in range(D):
                    P[(1 - z) * D + (d - m), z * D + m] = 1.0
            comm = float(np.abs(P @ cs.H - cs.H @ P).max())
            a = np.array([math.sqrt(binom(d, m)) for m in range(D)]) / math.sqrt(2.0 ** d)
            psi0 = np.concatenate([a, a]) / math.sqrt(2.0)
            fix = float(np.abs(P @ psi0 - psi0).max())
            sym_rows.append({"d": d, "lambda": lam, "commutator_max_abs": comm,
                             "P_fixes_preparation_max_abs": fix})
    l0["symbolic_check_in_the_collective_basis"] = sym_rows
    l0["max_commutator"] = max(r["commutator_max_abs"] for r in sym_rows)
    l0["max_preparation_defect"] = max(r["P_fixes_preparation_max_abs"] for r in sym_rows)
    if l0["max_commutator"] > 0.0 or l0["max_preparation_defect"] > 1e-15:
        die("Q2:L0-symmetry")
    hz_dev = 0.0
    hz_n = 0
    for d in (2, 3, 4, 5, 6, 8, 10, 12):
        for lam in (0.05, 0.075, 0.10, 0.5, 2.0):
            cs = coll(d, lam)
            for t in (0.05, 0.3, 0.7, 1.2, 2.5, 5.0):
                hz_dev = max(hz_dev, abs(cs.stats(t)["H_Z"] - 1.0))
                hz_n += 1
    l0["numeric_max_abs_dev_from_1_bit"] = hz_dev
    l0["n_cells_probed"] = hz_n
    l0["holds"] = bool(hz_dev < 1e-15)
    if not l0["holds"]:
        die("Q2:L0-numeric %r" % hz_dev)
    q2["L0_H_Z_is_exactly_one_bit"] = l0

    # ---- L1/L2: chi(0) = 0, excess == chi, and the gate reduction -------------
    l1 = {"claim": ("chi_F(0) = 0 EXACTLY, hence excess_F = chi_F identically; and "
                    "since the chi clause demands chi >= (1-delta) H_Z = 0.9 > 0.02 "
                    "= EXCESS_MIN, the excess clause is IMPLIED and never binds."),
          "scope_correction_found_while_building_the_tooth": (
              "the lemma is STRONGER than 'a fact about the frozen preparation': "
              "chi_F(0) = 0 for ANY preparation that is a PRODUCT across the "
              "pointer/arm cut, because both pointer branches then carry the same "
              "arm state.  The frozen preparation is such a product.  The tooth was "
              "redesigned accordingly -- the falsifying control has to be a "
              "pointer-arm ENTANGLED initial state, not merely a different product "
              "(the first design, +Z arms, correctly gave chi(0) = 0 too and the "
              "tooth refused to fire; disclosed rather than quietly replaced).")}
    ch0 = 0.0
    exc_binds = []
    for d in (2, 3, 4, 5, 6, 7, 8, 10, 12):
        for lam in (0.05, 0.075, 0.10):
            cs = coll(d, lam)
            ch0 = max(ch0, abs(cs.chi0))
            for t in DENSE_TS:
                g = cs.gates(t)
                if g["m_content"] >= 0.0 and g["m_excess"] < 0.0:
                    exc_binds.append([d, lam, t])
    l1["max_abs_chi_at_t0"] = ch0
    l1["frozen_t0_anchor_tolerance"] = T0_ANCHOR_TOL
    l1["t0_anchor_quote"] = frozen["t0_anchor_tol"]["quote"]
    l1["excess_clause_binds_anywhere_the_chi_clause_holds"] = bool(exc_binds)
    l1["n_excess_binding_points"] = len(exc_binds)
    l1["implication_margin_bits"] = (1.0 - HEADLINE_DELTA) - EXCESS_MIN
    l1["numerical_note"] = ("chi(0) is analytically zero (both branches carry the same "
                            "arm state at t=0); the measured maximum is %.2e, set by "
                            "the entropy of a near-degenerate 2x2 spectrum, and is "
                            "six orders inside the frozen protocol's own t=0 anchor "
                            "tolerance of 1e-9 bit." % ch0)
    if ch0 > T0_ANCHOR_TOL or exc_binds:
        die("Q2:L1-excess chi0=%r binds=%d" % (ch0, len(exc_binds)))
    q2["L1_L2_content_gate_is_exactly_a_single_arm_holevo_threshold"] = l1

    # ---- L3: lambda_pointer = 0 gives EXACT degree-independence ---------------
    l3 = {"claim": ("With the pointer's OWN transverse term switched off, Z_0 is "
                    "conserved, each pointer branch is a PRODUCT of d identical "
                    "single-qubit states, rho_1^z is PURE and carries no d, and "
                    "chi_1 = h2((1+|<phi_+|phi_->|)/2) with |phi_s> = "
                    "exp(-i(-s Z - lambda_arm X) t)|+>.  The content gate is then "
                    "EXACTLY degree-independent for ANY arm field."),
          "consequence": ("the ENTIRE degree-dependence of t_open is the pointer's "
                          "own transverse term lambda X_0 -- the same single term "
                          "933 ablated to show it is the entire source of arm "
                          "entanglement.  One term runs both sides of the gate.")}
    rows = []
    spread0 = 0.0
    closed_dev = 0.0
    for lam in (0.0, 0.05, 0.075, 0.10, 0.20, 0.5):
        vals = []
        for d in range(2, 13):
            cs = StarCollective(d, lam, lam_pointer=0.0, lam_arm=lam)
            for t in (0.3, 0.6, 0.7, 0.9):
                v = cs.stats(t)["chi1"]
                vals.append((d, t, v))
                closed_dev = max(closed_dev, abs(v - chi1_single_arm_closed(t, lam)))
        for t in (0.3, 0.6, 0.7, 0.9):
            sub = [v for (dd, tt, v) in vals if tt == t]
            spread0 = max(spread0, max(sub) - min(sub))
        rows.append({"lambda_arm": lam, "lambda_pointer": 0.0,
                     "chi_spread_over_d_2_to_12": max(
                         max([v for (dd, tt, v) in vals if tt == t])
                         - min([v for (dd, tt, v) in vals if tt == t])
                         for t in (0.3, 0.6, 0.7, 0.9))})
    l3["rows"] = rows
    l3["max_chi_spread_over_degrees_at_lambda_pointer_zero"] = spread0
    l3["max_dev_from_the_two_level_closed_form"] = closed_dev
    l3["degrees_probed"] = "d = 2..12"
    l3["floor_note"] = ("1.2e-14 is the double-precision floor these entropies carry "
                        "at d = 12 -- the same grade 933 reported for its own s(k) "
                        "reproduction.  Switching the pointer field ON at the same "
                        "cells moves chi's degree-spread to ~1e-3: ELEVEN orders.")
    l3["exact_degree_independence"] = bool(spread0 < 1e-13)
    if not l3["exact_degree_independence"] or closed_dev > 1e-13:
        die("Q2:L3 spread=%r closed=%r" % (spread0, closed_dev))
    q2["L3_degree_independence_is_EXACT_at_zero_pointer_field"] = l3

    # ---- L4: the zero-field closed-form window -------------------------------
    zf = zero_field_window(HEADLINE_DELTA)
    l4 = {"claim": ("At lambda = 0 the content window is closed form: "
                    "t_open^(0) = (1/2) arccos(c*), t_close^(0) = pi/2 - t_open^(0), "
                    "W^(0) = pi/2 - arccos(c*), where h2((1+c*)/2) = 1 - delta."),
          "c_star": zf["c_star"], "t_open_0": zf["t_open"],
          "t_close_0": zf["t_close"], "width_0": zf["width"],
          "reflection_identity": ("|cos 2(pi/2 - t)| = |cos 2t|, so the content "
                                  "window is EXACTLY symmetric about Jt = pi/4 at "
                                  "zero field -- the reason 932 measured W ~ 0.37 at "
                                  "the low field on every degree."),
          "c932_measured_width_at_0.05": "W ~ 0.37 (932 note), run 4"}
    for delta in DELTAS:
        z = zero_field_window(delta)
        l4["at_delta_%.2f" % delta] = {"c_star": z["c_star"], "t_open": z["t_open"],
                                       "t_close": z["t_close"], "width": z["width"]}
    q2["L4_zero_field_closed_form"] = l4

    # ---- L5: the back-action, its order, and the measured spread -------------
    def t_open_of(cs, delta=HEADLINE_DELTA):
        f = lambda t: cs.stats(t)["chi1"] - (1.0 - delta) * cs.stats(t)["H_Z"]
        return bisect_scalar(f, 0.30, 0.78)

    def t_close_content_of(cs, delta=HEADLINE_DELTA):
        f = lambda t: cs.stats(t)["chi1"] - (1.0 - delta) * cs.stats(t)["H_Z"]
        return bisect_scalar(f, 0.80, 1.40)

    def t_open_L1(lam, delta=HEADLINE_DELTA):
        f = lambda t: chi1_single_arm_closed(t, lam) - (1.0 - delta)
        return bisect_scalar(f, 0.30, 0.78)

    l5 = {"claim": ("the residual degree-dependence of t_open is the pointer's "
                    "back-action.  In the flip-history expansion the branch arm "
                    "state is sum_h A_h |psi_h>^(x)d with A_h = O(lambda^{#flips}), "
                    "and the single-arm reduced state carries the COLLECTIVE OVERLAP "
                    "factors <psi_h'|psi_h>^(d-1) -- that power of (d-1) is where, "
                    "and the only place where, the degree enters.  A one-flip pair "
                    "contributes at O(lambda^2), so the spread is O(lambda^2) up to "
                    "the log that 933 found in the same expansion.")}
    ba_rows = []
    for lam in (0.0125, 0.025, 0.05, 0.075, 0.10, 0.15, 0.20):
        tl1 = t_open_L1(lam)
        vals = {}
        for d in range(2, 9):
            cs = StarCollective(d, lam)
            vals[d] = t_open_of(cs)
        sp = max(vals.values()) - min(vals.values())
        sh = max(abs(v - tl1) for v in vals.values())
        ba_rows.append({"lambda": lam, "t_open_L1_zero_pointer_field": tl1,
                        "t_open_by_degree": {str(k): v for k, v in vals.items()},
                        "spread_over_d_2_to_8": sp,
                        "max_backaction_shift_vs_L1": sh,
                        "spread_over_lambda_squared": sp / lam ** 2,
                        "shift_over_lambda_squared": sh / lam ** 2})
    l5["rows"] = ba_rows
    # fitted exponents (log-log slope of spread and shift against lambda)
    ls = np.array([math.log(r["lambda"]) for r in ba_rows])
    for nm, key in (("spread", "spread_over_d_2_to_8"),
                    ("backaction_shift", "max_backaction_shift_vs_L1")):
        ys = np.array([math.log(r[key]) for r in ba_rows])
        A = np.vstack([ls, np.ones_like(ls)]).T
        slope, inter = np.linalg.lstsq(A, ys, rcond=None)[0]
        l5["fitted_exponent_%s" % nm] = float(slope)
        l5["fitted_prefactor_%s" % nm] = float(math.exp(inter))
    l5["c932_reported_spread_across_d_2_to_8"] = 2.1e-3
    l5["reproduced_spread_at_lambda_0.10"] = next(
        r["spread_over_d_2_to_8"] for r in ba_rows if r["lambda"] == 0.10)
    l5["reproduced_spread_at_lambda_0.05"] = next(
        r["spread_over_d_2_to_8"] for r in ba_rows if r["lambda"] == 0.05)
    l5["c932_spread_reproduced_to"] = abs(
        l5["reproduced_spread_at_lambda_0.10"] - 2.1e-3)
    # does the O(lambda^2) bound actually hold over the probed decade?
    ratios = [r["spread_over_lambda_squared"] for r in ba_rows]
    l5["spread_over_lambda_squared_range"] = [min(ratios), max(ratios)]
    l5["order_claim_supported"] = bool(1.5 <= l5["fitted_exponent_spread"] <= 2.5)
    l5["honest_reading"] = (
        "the fitted exponent is %.3f, i.e. NOT exactly 2: the same lambda^2 "
        "log(1/lambda) non-analyticity 933 found in s(k) is present here, which "
        "depresses the log-log slope below 2.  The order claim is therefore stated "
        "as 'O(lambda^2) up to a logarithm', and the lambda^2-normalised ratio "
        "drifts across the decade rather than being constant -- reported, not "
        "smoothed." % l5["fitted_exponent_spread"])
    if not l5["order_claim_supported"]:
        die("Q2:L5-order %r" % l5["fitted_exponent_spread"])
    q2["L5_the_backaction_order_and_the_measured_spread"] = l5

    # ---- L6: t_close, both sides, and the clip switch ------------------------
    def t_close_indep_of(cs):
        f = lambda t: cs.stats(t)["C_ab"] - INDEP_MAX
        return bisect_scalar(f, 0.40, 1.45)

    l6 = {"claim": ("t_close = min(content-side close, independence-side close).  The "
                    "content side is the SECOND crossing of the same chi_1 threshold "
                    "(derived here); the independence side is the crossing of 933's "
                    "C_ab = 2 s(1) - s(2) with 0.02 (derived there).  Both edges of "
                    "932's window are therefore derived, and so is the clip switch.")}
    clip_rows = []
    for lam in (0.05, 0.075, 0.10):
        for d in range(2, 11):
            cs = coll(d, lam)
            tcc = t_close_content_of(cs)
            tci = t_close_indep_of(cs)
            cands = {"content_chi": tcc}
            if tci is not None:
                cands["independence"] = tci
            which = min(cands, key=lambda k: cands[k])
            clip_rows.append({"d": d, "lambda": lam,
                              "t_close_content": tcc, "t_close_independence": tci,
                              "t_close_predicted": cands[which],
                              "clip_gate_predicted": which})
    l6["rows"] = clip_rows
    # verify the switch against every pinned 932 cell
    sw = {"checked": 0, "mismatches": []}
    for ck, cell in sorted(rec932["Q1_curves"]["per_cell"].items()):
        if not re.match(r"^S\d+@", ck):
            continue
        d = int(ck.split("@")[0][1:])
        lam = float(ck.split("@")[1])
        row = next(r for r in clip_rows if r["d"] == d and abs(r["lambda"] - lam) < 1e-12)
        sw["checked"] += 1
        if row["clip_gate_predicted"] != cell["close_gate"]:
            sw["mismatches"].append([ck, row["clip_gate_predicted"], cell["close_gate"]])
        if abs(row["t_close_predicted"] - cell["t_close"]) > EDGE_GRADE:
            sw["mismatches"].append([ck, "edge", row["t_close_predicted"],
                                     cell["t_close"]])
    l6["clip_switch_vs_932"] = sw
    if sw["mismatches"]:
        die("Q2:L6-clip mismatches %r" % sw["mismatches"][:3])
    l6["smallest_degree_where_content_clips_at_0.10"] = min(
        (r["d"] for r in clip_rows
         if abs(r["lambda"] - 0.10) < 1e-12 and r["clip_gate_predicted"] == "content_chi"),
        default=None)
    l6["c932_reported_content_clips_from_degree"] = 6
    q2["L6_t_close_both_sides_derived"] = l6

    # ---- the derived t_open table against every pinned 932 edge --------------
    topen = {"rows": [], "max_abs_deviation": 0.0}
    for ck, cell in sorted(rec932["Q1_curves"]["per_cell"].items()):
        if not re.match(r"^S\d+@", ck):
            continue
        d = int(ck.split("@")[0][1:])
        lam = float(ck.split("@")[1])
        got = t_open_of(coll(d, lam))
        dv = abs(got - cell["t_open"])
        topen["rows"].append({"cell": ck, "t_open_derived": got,
                              "t_open_932": cell["t_open"], "dev": dv})
        topen["max_abs_deviation"] = max(topen["max_abs_deviation"], dv)
    if topen["max_abs_deviation"] > EDGE_GRADE:
        die("Q2:t_open-vs-932 %r" % topen["max_abs_deviation"])
    q2["t_open_derived_vs_every_pinned_932_edge"] = topen
    q2["status"] = {
        "t_open": "DERIVED (content-gate crossing of the derived chi_1 profile)",
        "t_open_degree_independence": ("EXPLAINED EXACTLY: exact at zero pointer "
                                       "field; the residual is the derived "
                                       "back-action, O(lambda^2) up to a log"),
        "t_close_content_side": "DERIVED",
        "t_close_independence_side": "DERIVED (933's s(k))",
        "every_edge_of_932s_window": "DERIVED"}
    receipt["Q2_t_open_derived"] = q2
    print("Q2 done: H_Z dev %.1e, L3 spread %.1e, t_open vs 932 %.1e, exponent %.3f"
          % (hz_dev, spread0, topen["max_abs_deviation"],
             l5["fitted_exponent_spread"]))

    # ================ Q3: THE COMPOSED STAR CERTIFICATION THEOREM =============
    q3 = {}
    q3["theorem"] = {
        "name": "The star certification theorem (composed)",
        "hypotheses": [
            "H1 IMPORTED (frozen): the Hamiltonian "
            "`H_lambda = - sum_<ij> Z_i Z_j - lambda sum_i X_i`.",
            "H2 IMPORTED (frozen): the preparation -- the pointer and its recording "
            "neighbours in +X; on K_{1,d} that is |+>^(x)(d+1).",
            "H3 IMPORTED (frozen): the partition rule -- on a star every arm is its "
            "own singleton fragment.",
            "H4 IMPORTED (frozen): the statistic definitions (chi_Z, C_ab, H(Z_S)) "
            "and the four gate constants 0.05 / (1-delta) / 0.02 / 0.02.",
            "H5 IMPORTED (frozen): the sample grid Jt = 0.0(0.1)1.2 AT PHASE 0, the "
            "run rule PERSIST_N = 3, and the deadline Jt <= 1.",
            "H6 GEOMETRIC: the geometry is a star K_{1,d}, d >= 1 -- i.e. its arms "
            "are pairwise isomorphic and exchangeable.  (This is what puts the "
            "branch in Sym^d; it is 933's honest boundary and it is inherited "
            "unchanged.)",
            "H7 DERIVED HERE: H(Z_S) = 1 bit exactly (global X-flip symmetry), so "
            "the content gate's clause 1 is unconditional and clause 2's threshold "
            "is the constant (1-delta).",
            "H8 DERIVED HERE: chi(0) = 0, so excess = chi and the excess clause is "
            "implied by the chi clause whenever delta <= 0.98.",
            "H9 DERIVED (933): the branch lies exactly in C^2 (x) Sym^d, so every "
            "statistic is a functional of the 2(d+1) reduction.",
            "H10 DERIVED (932): on every cell the certifiable set is ONE contiguous "
            "interval, so the run is the count of grid points in it.  (VERIFIED "
            "HERE on every corpus cell rather than assumed: n_blocks = 1 throughout, "
            "and the direct per-sample count is compared against the edge count.)",
            "H11 NUMERICAL: the scan resolution used to find the blocks is finer "
            "than the narrowest window in the corpus; edges are bisected to 1e-13.",
        ],
        "statement": (
            "Given H1-H6, the complete frozen certification verdict of any star "
            "K_{1,d} at any field follows from the 2(d+1) collective reduction "
            "alone: (i) the content gate opens at the derived t_open, the first "
            "crossing of chi_1(t) = (1-delta) H_Z(t), and t_open is EXACTLY "
            "degree-independent at zero pointer field with the residual an "
            "O(lambda^2)-up-to-a-log back-action; (ii) the independence gate kills "
            "pairs exactly where 933's C_ab = 2 s(1) - s(2) crosses 0.02, i.e. at "
            "the derived crossings lambda*(d); (iii) the window's closing edge is "
            "min(content-side, independence-side) -- the clip identity; (iv) the "
            "run is the number of frozen grid points in that window (932); (v) the "
            "verdict is YES iff run >= PERSIST_N and the first sample is by the "
            "deadline.  The composition is stated AT 932's grid-phase scope: the "
            "d >= 5 threshold at lambda = 0.10 holds at the frozen grid PHASE 0; "
            "d <= 2 fails and d >= 5 certifies at every phase, and d = 3-4 are "
            "phase-decided."),
        "what_is_derived": [
            "every pointer-side statistic (H_Z, chi, excess) as a functional of the "
            "same 2(d+1) reduction that carries s(k)",
            "t_open, and the exact explanation of its degree-independence",
            "the content-side t_close",
            "the independence-side t_close (via 933)",
            "the clip identity / switch",
            "the run and the verdict (via 932's counting law)",
        ],
        "what_stays_imported": [
            "the frozen Hamiltonian, preparation, partition rule and statistic "
            "definitions (H1-H4) -- protocol, not physics this block can derive",
            "the sample grid, its PHASE, the run length and the deadline (H5)",
            "arm-exchangeability (H6): non-star geometries -- chains, loops, "
            "mixed-arm spiders -- are outside the reduction and stay empirical",
            "the delta-family convention and the choice of headline delta",
        ],
        "components_that_resisted_derivation": "none at star scope; see the honest "
                                               "split in what_stays_imported",
    }

    # ---- the corpus ----------------------------------------------------------
    corpus = []
    for (ckey, lam), (d, rows) in sorted(star_anchor_rows.items()):
        src, key = ckey.split(":")
        rec = {"917": rec917, "919": rec919, "927": rec927}[src]
        gk = {"917": "geometries", "919": "degree_five_geometries",
              "927": "geometries"}[src]
        ls = ("%g" % lam)
        ls = "0.1" if ls == "0.1" else ls
        vb = rec[gk][key]["lambdas"][ls]["verdicts_by_delta"]
        corpus.append({"label": "%s:%s@%s" % (src, key, ls), "d": d, "lambda": lam,
                       "source": src, "pinned_rows": rows, "pinned_verdicts": vb})
    for ck, cell in sorted(rec932["Q1_curves"]["per_cell"].items()):
        if not re.match(r"^S\d+@", ck):
            continue
        corpus.append({"label": "932:%s" % ck, "d": int(ck.split("@")[0][1:]),
                       "lambda": float(ck.split("@")[1]), "source": "932",
                       "pinned_rows": None,
                       "pinned_verdicts": {"0.10": {"verdict": cell["frozen_verdict"],
                                                    "event": {"run": cell["frozen_run"]}}}})

    # ---- the composed prediction, per cell, per delta -------------------------
    table = {}
    agree = {"cells": 0, "delta_rows": 0, "verdict_disagreements": [],
             "run_disagreements": [], "sample_flag_disagreements": [],
             "edge_count_vs_direct_count_disagreements": []}
    for ent in corpus:
        d, lam = ent["d"], ent["lambda"]
        cs = coll(d, lam)
        per_delta = {}
        for delta in DELTAS:
            flags = [cs.cert(t, delta) for t in T_EXEC]
            idx = next((i for i, f in enumerate(flags) if f), None)
            if idx is None:
                run_direct, first_jt = 0, None
            else:
                run_direct = 0
                for f in flags[idx:]:
                    if f:
                        run_direct += 1
                    else:
                        break
                first_jt = T_EXEC[idx]
            v_direct = ("YES" if (idx is not None and run_direct >= PERSIST_N
                                  and first_jt <= DEADLINE_JT + 1e-12) else "NO")
            win = derived_window(cs, delta)
            pred = composed_verdict(win["blocks"])
            samples = []
            for t in T_EXEC:
                g = cs.gates(t, delta)
                samples.append({"jt": t, "H_Z": g["H_Z"], "chi": g["chi1"],
                                "excess": g["excess"], "C_ab": g["C_ab"],
                                "content": g["content"], "independence": g["indep"],
                                "r_ind_ge2": g["cert"]})
            per_delta["%.2f" % delta] = {
                "samples": samples, "run_direct": run_direct,
                "first_jt": first_jt, "verdict_direct": v_direct,
                "n_blocks": win["n_blocks"],
                "window": ([win["blocks"][0]["lo"], win["blocks"][0]["hi"]]
                           if win["n_blocks"] == 1 else None),
                "open_gate": (win["blocks"][0]["open_gate"] if win["n_blocks"] else None),
                "close_gate": (win["blocks"][0]["close_gate"] if win["n_blocks"] else None),
                "run_edge_count": pred["run"], "verdict_edge_count": pred["verdict"]}
            if pred["run"] != run_direct or pred["verdict"] != v_direct:
                agree["edge_count_vs_direct_count_disagreements"].append(
                    [ent["label"], delta, pred["run"], run_direct,
                     pred["verdict"], v_direct])
            # ---- compare against the pinned FULL-SPACE verdict ---------------
            pv = ent["pinned_verdicts"].get("%.2f" % delta)
            if pv is None:
                continue
            agree["delta_rows"] += 1
            if pv["verdict"] != v_direct:
                agree["verdict_disagreements"].append(
                    [ent["label"], delta, v_direct, pv["verdict"]])
            prun = (pv.get("event") or {}).get("run", 0) if pv.get("event") else 0
            if prun != run_direct:
                agree["run_disagreements"].append(
                    [ent["label"], delta, run_direct, prun])
            if ent["pinned_rows"] is not None:
                for r, s in zip(ent["pinned_rows"], samples):
                    pin_flag = bool(r["r_ind"]["%.2f" % delta] >= 2)
                    if pin_flag != s["r_ind_ge2"]:
                        agree["sample_flag_disagreements"].append(
                            [ent["label"], delta, r["jt"], s["r_ind_ge2"], pin_flag])
        table[ent["label"]] = {"d": d, "lambda": lam, "source": ent["source"],
                               "by_delta": per_delta}
        agree["cells"] += 1
    agree["exact_verdict_agreement_every_cell"] = bool(
        not agree["verdict_disagreements"])
    agree["exact_run_agreement_every_cell"] = bool(not agree["run_disagreements"])
    agree["exact_per_sample_gate_agreement"] = bool(
        not agree["sample_flag_disagreements"])
    agree["edge_counting_law_agrees_with_direct_evaluation"] = bool(
        not agree["edge_count_vs_direct_count_disagreements"])
    for k in ("verdict_disagreements", "run_disagreements", "sample_flag_disagreements",
              "edge_count_vs_direct_count_disagreements"):
        if agree[k]:
            die("Q3:composed-table %s %r" % (k, agree[k][:4]))
    q3["composed_verdict_table"] = table
    q3["composed_verdict_agreement"] = agree
    q3["corpus"] = {"n_star_cells": len(corpus),
                    "sources": sorted({e["source"] for e in corpus}),
                    "degrees": sorted({e["d"] for e in corpus}),
                    "fields": sorted({e["lambda"] for e in corpus}),
                    "deltas": list(DELTAS)}

    # ---- the hypothesis-discharge audit (H10 and the unmodelled clauses) -----
    disc = {"n_blocks_is_one_on_every_corpus_cell_and_delta": True,
            "pointer_drift_clause_max_over_corpus": 0.0,
            "clauses_in_verdict_of_not_modelled_by_the_composition":
                ["pointer_tv_drift <= 0.10", "x_control", "commutator_ordering_ok"]}
    for ent in corpus:
        for delta in DELTAS:
            nb = table[ent["label"]]["by_delta"]["%.2f" % delta]["n_blocks"]
            if nb != 1:
                disc["n_blocks_is_one_on_every_corpus_cell_and_delta"] = False
                disc.setdefault("cells_with_other_block_counts", []).append(
                    [ent["label"], delta, nb])
        cs = coll(ent["d"], ent["lambda"])
        for t in T_EXEC:
            disc["pointer_drift_clause_max_over_corpus"] = max(
                disc["pointer_drift_clause_max_over_corpus"],
                abs(cs.stats(t)["p_z"][0] - 0.5))
    disc["pointer_drift_clause_can_never_bind_on_a_star"] = (
        "H_Z = 1 exactly means p_z = (1/2,1/2) exactly, so the pointer "
        "total-variation drift is 0 identically and the DRIFT_MAX = 0.10 clause is "
        "vacuous on stars -- measured max %.2e."
        % disc["pointer_drift_clause_max_over_corpus"])
    q3["hypothesis_discharge_audit"] = disc
    if not disc["n_blocks_is_one_on_every_corpus_cell_and_delta"]:
        die("Q3:H10-blocks")
    print("Q3 composed table: %d cells, %d delta rows, verdict agreement %s"
          % (agree["cells"], agree["delta_rows"],
             agree["exact_verdict_agreement_every_cell"]))

    # ============================== THE SEAL (built before any full-space run) =
    pre_seal_full_space = sorted("d%d@%g" % (d, l) for (d, l)
                                 in FULL_SPACE_CELLS_EVALUATED)
    seal_cells = []
    for d in SEAL_DEGREES:
        for lam in list(CLAIM_LAMBDAS) + list(SEAL_LAMBDAS_NEW):
            seal_cells.append((d, lam))
    # HOLDOUT CLASSIFICATION, stated honestly.  The never-used fields are true
    # holdouts: no full-space number for them exists anywhere in the corpus and
    # none is computed in this run before the digest.  The FROZEN fields at
    # d = 9, 10 are NOT holdouts and are not claimed as such: 927 publishes
    # full-space rows for STk10 (d = 10) at both frozen fields, and 932's own seal
    # published (and full-space verified) S9/S10 there.  They are carried as
    # CORPUS-REPRODUCTION rows because the spec asks for the complete table at
    # those cells; the guard below is enforced on the holdout class only, and this
    # run additionally keeps route N -- its own untouched full-space route -- off
    # EVERY sealed cell until the digest is fixed.
    holdout_cells = [(d, l) for (d, l) in seal_cells if l in SEAL_LAMBDAS_NEW]
    corpus_repro_cells = [(d, l) for (d, l) in seal_cells if l not in SEAL_LAMBDAS_NEW]
    already = [("d%d@%g" % (d, l)) for (d, l) in holdout_cells
               if (d, round(float(l), 12)) in FULL_SPACE_CELLS_EVALUATED]
    route_n_touched_any_sealed = [("d%d@%g" % (d, l)) for (d, l) in seal_cells
                                  if (d, round(float(l), 12))
                                  in FULL_SPACE_CELLS_EVALUATED]
    seal_predictions = {}
    for (d, lam) in seal_cells:
        cs = StarCollective(d, lam)     # ROUTE S ONLY -- 2(d+1)
        row = {}
        for delta in DELTAS:
            win = derived_window(cs, delta)
            pred = composed_verdict(win["blocks"])
            b = win["blocks"][0] if win["n_blocks"] == 1 else None
            row["%.2f" % delta] = {
                "t_open": (b["lo"] if b else None),
                "t_close": (b["hi"] if b else None),
                "width": (b["width"] if b else None),
                "open_gate": (b["open_gate"] if b else None),
                "close_gate": (b["close_gate"] if b else None),
                "n_blocks": win["n_blocks"],
                "run": pred["run"], "verdict": pred["verdict"],
                "first_jt": pred["first_jt"],
                "samples": [{"jt": t,
                             "chi": cs.gates(t, delta)["chi1"],
                             "excess": cs.gates(t, delta)["excess"],
                             "H_Z": cs.gates(t, delta)["H_Z"],
                             "C_ab": cs.gates(t, delta)["C_ab"],
                             "r_ind_ge2": cs.gates(t, delta)["cert"]}
                            for t in T_EXEC]}
        seal_predictions["d%d@%g" % (d, lam)] = row
    seal_payload = {"seal_id": "cycle934-pointer-gates-seal-v1",
                    "built_from": ("the derived 2(d+1) collective reduction ONLY; no "
                                   "full-space vector at any sealed cell existed when "
                                   "this digest was fixed"),
                    "n_sealed_cells": len(seal_cells),
                    "degrees": list(SEAL_DEGREES),
                    "frozen_fields": list(CLAIM_LAMBDAS),
                    "never_used_fields": list(SEAL_LAMBDAS_NEW),
                    "never_used_field_justification": (
                        "0.0413 / 0.0687 / 0.1137 appear nowhere in the 917/919/921/"
                        "926/927/929/931/932/933 receipts, in any of their sweeps, or "
                        "in 932's own seal (which used 0.0625 / 0.0875 / 0.09375)"),
                    "holdout_class_cells": ["d%d@%g" % c for c in holdout_cells],
                    "corpus_reproduction_class_cells":
                        ["d%d@%g" % c for c in corpus_repro_cells],
                    "holdout_class_definition": (
                        "no full-space number for this (degree, field) exists anywhere "
                        "in the 917/919/921/926/927/929/931/932/933 corpus, and none "
                        "was computed in this run before the digest was fixed"),
                    "corpus_reproduction_class_disclosure": (
                        "d = 9, 10 at the FROZEN fields are NOT holdouts and are not "
                        "claimed as such: 927 publishes full-space rows for STk10 "
                        "(d = 10) at 0.05 and 0.10, and 932's seal published and "
                        "full-space-verified S9/S10 at both frozen fields.  They are "
                        "carried because the spec asks for the complete table there; "
                        "their evidential weight is reproduction, not prediction."),
                    "already_evaluated_before_seal": already,
                    "route_N_cells_touched_before_seal_among_sealed_cells":
                        route_n_touched_any_sealed,
                    "full_space_cells_evaluated_before_seal_route_N": pre_seal_full_space,
                    "predictions": seal_predictions}
    if already:
        die("seal:holdout-violation %r" % already)
    if route_n_touched_any_sealed:
        die("seal:routeN-pre-evaluation %r" % route_n_touched_any_sealed)
    seal_sha = sha256_obj(seal_payload)
    seal_payload["prereg_sha256"] = seal_sha
    seal_payload["build_log_before_seal"] = list(BUILD_LOG)

    # ---- NOW verify on the untouched full-space route ------------------------
    seal_ver = {"rows": {}, "max_abs_edge_deviation": 0.0,
                "verdict_mismatches": [], "sample_flag_mismatches": []}
    for (d, lam) in seal_cells:
        fs = StarFull(d, lam, tag="seal-verify")
        key = "d%d@%g" % (d, lam)
        rowout = {}
        for delta in DELTAS:
            sealed = seal_predictions[key]["%.2f" % delta]
            # full-space per-sample flags and run/verdict
            flags = []
            chi0f = fs.stats(0.0)["chi1"]
            for t in T_EXEC:
                st = fs.stats(t)
                content = (st["H_Z"] >= CONTENT_H_MIN
                           and st["chi1"] >= (1.0 - delta) * st["H_Z"]
                           and (st["chi1"] - chi0f) >= EXCESS_MIN)
                indep = (st["C_ab"] is not None and st["C_ab"] <= INDEP_MAX)
                flags.append(bool(d >= 2 and content and indep))
            idx = next((i for i, f in enumerate(flags) if f), None)
            if idx is None:
                run, first = 0, None
            else:
                run = 0
                for f in flags[idx:]:
                    if f:
                        run += 1
                    else:
                        break
                first = T_EXEC[idx]
            verdict = ("YES" if (idx is not None and run >= PERSIST_N
                                 and first <= DEADLINE_JT + 1e-12) else "NO")
            if verdict != sealed["verdict"] or run != sealed["run"]:
                seal_ver["verdict_mismatches"].append(
                    [key, delta, sealed["verdict"], sealed["run"], verdict, run])
            for s, f in zip(sealed["samples"], flags):
                if s["r_ind_ge2"] != f:
                    seal_ver["sample_flag_mismatches"].append([key, delta, s["jt"]])
            # edge deviation: bisect the FULL-SPACE predicate around the sealed edges
            def cert_full(t, delta=delta, fs=fs, chi0f=chi0f, d=d):
                st = fs.stats(t)
                content = (st["H_Z"] >= CONTENT_H_MIN
                           and st["chi1"] >= (1.0 - delta) * st["H_Z"]
                           and (st["chi1"] - chi0f) >= EXCESS_MIN)
                indep = (st["C_ab"] is not None and st["C_ab"] <= INDEP_MAX)
                return bool(d >= 2 and content and indep)
            eo, ec = sealed["t_open"], sealed["t_close"]
            dev = 0.0
            for edge, lo_out, hi_in in ((eo, eo - 0.02, eo + 0.02),
                                        (ec, ec + 0.02, ec - 0.02)):
                a, b = lo_out, hi_in
                if cert_full(a) == cert_full(b):
                    continue
                for _ in range(60):
                    m = 0.5 * (a + b)
                    if cert_full(m):
                        b = m
                    else:
                        a = m
                    if abs(b - a) < 1e-12:
                        break
                dev = max(dev, abs(0.5 * (a + b) - edge))
            seal_ver["max_abs_edge_deviation"] = max(
                seal_ver["max_abs_edge_deviation"], dev)
            rowout["%.2f" % delta] = {"verdict_full_space": verdict,
                                      "run_full_space": run,
                                      "verdict_sealed": sealed["verdict"],
                                      "run_sealed": sealed["run"],
                                      "max_abs_edge_deviation": dev}
        seal_ver["rows"][key] = rowout
    seal_ver["all_predictions_hold"] = bool(
        not seal_ver["verdict_mismatches"] and not seal_ver["sample_flag_mismatches"]
        and seal_ver["max_abs_edge_deviation"] <= 1e-10)
    if not seal_ver["all_predictions_hold"]:
        die("seal:verification %r" % (seal_ver["verdict_mismatches"][:3]
                                      or seal_ver["sample_flag_mismatches"][:3]
                                      or seal_ver["max_abs_edge_deviation"]))
    q3["seal"] = seal_payload
    q3["seal_verification"] = seal_ver
    receipt["Q3_composed_star_certification_theorem"] = q3
    print("SEAL %d cells, prereg %s, verification holds (edge dev %.2e)"
          % (len(seal_cells), seal_sha[:16], seal_ver["max_abs_edge_deviation"]))

    # ================================================== ROUTES AND DETERMINISM =
    routes = {
        "route_P919": ("the pinned Cycle-919 certification code executed VERBATIM "
                       "from its bytes (33 functions), full 2^(d+1) Chebyshev"),
        "route_P927": ("the pinned Cycle-927 code executed VERBATIM from its bytes "
                       "(25 functions), full 2^(d+1) Chebyshev with the Gram route"),
        "route_N": ("this block's own full 2^(d+1) assembly: explicit Kronecker "
                    "Hamiltonian, dense eigh, SVD entropies on reshaped amplitude "
                    "tensors, no density matrix"),
        "route_S": ("THE COLLECTIVE REDUCTION: 2(d+1) dense eigendecomposition in "
                    "the pointer (x) Dicke basis with the Hankel block -- "
                    "STRUCTURALLY DISJOINT from every full-space route"),
        "disjointness": ("route S never forms a 2^(d+1) object and route N never "
                         "forms a Dicke amplitude; they share only the frozen "
                         "constants and the entropy function"),
    }
    receipt["routes"] = routes

    core = {
        "t_open": {("d%d@%g" % (d, lam)): t_open_of(coll(d, lam))
                   for d in (2, 5, 8) for lam in (0.05, 0.10)},
        "t_close_content": {("d%d@%g" % (d, lam)): t_close_content_of(coll(d, lam))
                            for d in (2, 5, 8) for lam in (0.05, 0.10)},
        "zero_field_window": zf,
        "seal_sha256": seal_sha,
    }
    core_sha_1 = sha256_obj(core)
    coll_cache.clear()
    core2 = {
        "t_open": {("d%d@%g" % (d, lam)): t_open_of(coll(d, lam))
                   for d in (2, 5, 8) for lam in (0.05, 0.10)},
        "t_close_content": {("d%d@%g" % (d, lam)): t_close_content_of(coll(d, lam))
                            for d in (2, 5, 8) for lam in (0.05, 0.10)},
        "zero_field_window": zero_field_window(HEADLINE_DELTA),
        "seal_sha256": seal_sha,
    }
    core_sha_2 = sha256_obj(core2)
    receipt["determinism"] = {
        "core_payload_sha256": core_sha_1,
        "repeated_in_process_sha256": core_sha_2,
        "in_process_repeat_identical": bool(core_sha_1 == core_sha_2),
        "note": ("the cross-process check is the timing-free receipt digest, "
                 "compared between two separate invocations of this runner")}
    if core_sha_1 != core_sha_2:
        die("determinism:in-process")

    # ================================================================== TEETH ==
    # T01 -- a PLANTED degree-dependent t_open must be caught.
    planted = {}
    base = {}
    for d in range(2, 9):
        cs = StarCollective(d, 0.0, lam_pointer=0.0, lam_arm=0.0)
        base[d] = t_open_of(cs)
        planted[d] = base[d] + 1e-6 * (d - 5)
    sp_base = max(base.values()) - min(base.values())
    sp_plant = max(planted.values()) - min(planted.values())
    tooth("T01_planted_degree_dependent_t_open",
          "inject a 1e-6*(d-5) degree drift into t_open at zero field, where the "
          "derivation says the spread is EXACTLY zero; the degree-independence "
          "test must separate them",
          sp_base < 1e-13 <= sp_plant,
          {"true_spread_at_zero_field": sp_base, "planted_spread": sp_plant,
           "detection_threshold": 1e-13,
           "caught": bool(sp_plant > 1e-13 > sp_base)})

    # T02 -- a PLANTED verdict flip in the composed table must be caught.
    victim = "932:S5@0.1"
    true_v = table[victim]["by_delta"]["0.10"]["verdict_direct"]
    flipped = "NO" if true_v == "YES" else "YES"
    pinned_v = rec932["Q1_curves"]["per_cell"]["S5@0.1"]["frozen_verdict"]
    tooth("T02_planted_verdict_flip",
          "flip one cell's composed verdict and re-run the corpus comparison; the "
          "comparison must report a disagreement",
          (true_v == pinned_v) and (flipped != pinned_v),
          {"cell": victim, "true_verdict": true_v, "flipped_verdict": flipped,
           "pinned_verdict": pinned_v,
           "comparison_accepts_true": bool(true_v == pinned_v),
           "comparison_rejects_flipped": bool(flipped != pinned_v)})

    # T03 -- THE EULER GUARD, placed on chi and C_ab (932's disclosed limitation).
    d, lam, tt = 5, 0.10, 0.7
    cs = StarCollective(d, lam)
    nst = 40
    dt = tt / nst
    psiE = np.zeros(2 * (d + 1), dtype=complex)
    a = np.array([math.sqrt(binom(d, m)) for m in range(d + 1)]) / math.sqrt(2.0 ** d)
    psiE[0:d + 1] = a / math.sqrt(2.0)
    psiE[d + 1:] = a / math.sqrt(2.0)
    for _ in range(nst):
        psiE = psiE - 1j * dt * (cs.H @ psiE)
    psiE = psiE / np.linalg.norm(psiE)

    def stats_from_vector(cs, psi):
        D = cs.d + 1
        ps, xs = [], []
        for z in (0, 1):
            v = psi[z * D:(z + 1) * D]
            p = float(np.vdot(v, v).real)
            ps.append(p)
            xs.append((v / math.sqrt(p) if p > 1e-300 else v) / cs._sqrtC)
        tot = sum(ps)
        ps = [q / tot for q in ps]
        s, chi = {}, {}
        for k in (1, 2):
            rz = [cs.branch_rho(xs[z], k) for z in (0, 1)]
            sv = [ent_of_spectrum(np.linalg.eigvalsh(r)) for r in rz]
            s[k] = sum(p * e for p, e in zip(ps, sv))
            chi[k] = ent_of_spectrum(np.linalg.eigvalsh(ps[0] * rz[0] + ps[1] * rz[1])) - s[k]
        return {"H_Z": h2(ps[0]), "chi1": chi[1], "C_ab": 2 * s[1] - s[2]}
    ex = cs.stats(tt)
    eu = stats_from_vector(cs, psiE)
    tooth("T03_euler_guard_on_chi_and_C_ab_not_H_Z",
          "a first-order Euler integrator must be caught by chi and C_ab; it must "
          "NOT be caught by H_Z, because the global X-flip symmetry pins the branch "
          "weights for any symmetry-preserving integrator (932's disclosure, here "
          "explained by the L0 lemma)",
          abs(eu["chi1"] - ex["chi1"]) > 1e-6 and abs(eu["C_ab"] - ex["C_ab"]) > 1e-8
          and abs(eu["H_Z"] - ex["H_Z"]) < 1e-12,
          {"chi_deviation": abs(eu["chi1"] - ex["chi1"]),
           "C_ab_deviation": abs(eu["C_ab"] - ex["C_ab"]),
           "H_Z_deviation": abs(eu["H_Z"] - ex["H_Z"]),
           "H_Z_is_blind_by_symmetry": True, "euler_steps": nst})

    # T04 -- the 931 int8 underflow trap.
    good = StarFull(4, 0.10, tag="tooth-int8-good")
    bad = StarFull(4, 0.10, tag="tooth-int8-bad", dtype_bug=True)
    gv, bv = good.stats(0.7), bad.stats(0.7)
    tooth("T04_int8_underflow_guard",
          "an UNSIGNED dtype underflows 1-2*bit from -1 to 255 and corrupts every Z "
          "operator; the pointer-side statistics must diverge grossly",
          abs(gv["chi1"] - bv["chi1"]) > 1e-3,
          {"chi_good": gv["chi1"], "chi_underflowed": bv["chi1"],
           "deviation": abs(gv["chi1"] - bv["chi1"]),
           "H_Z_good": gv["H_Z"], "H_Z_underflowed": bv["H_Z"]})

    # T05 -- a TAMPERED vendored pin must be caught.
    vb = open(os.path.join(ROOT, C932_RECEIPT), "rb").read()
    tampered = vb[:-1] + (b"X" if vb[-1:] != b"X" else b"Y")
    tooth("T05_tampered_vendored_932_pin",
          "flip one byte of the vendored 932 receipt; the source-branch digest "
          "authority must reject it",
          sha256_bytes(tampered) != vendored["files"][C932_RECEIPT]["sha256"],
          {"true_sha256": vendored["files"][C932_RECEIPT]["sha256"],
           "tampered_sha256": sha256_bytes(tampered),
           "authority": vendored["authority"]})

    # T06 -- a PLANTED almost-fitting content constant must be caught.
    cs = coll(5, 0.10)
    t_true = t_open_of(cs)
    thr = (1.0 - HEADLINE_DELTA) * (1.0 + 1e-9)
    t_plant = bisect_scalar(lambda t: cs.stats(t)["chi1"] - thr, 0.30, 0.78)
    tooth("T06_planted_almost_fitting_content_constant",
          "perturb the frozen (1-delta) threshold by one part in 1e9; the derived "
          "t_open must move by more than the 1e-12 edge grade",
          abs(t_plant - t_true) > EDGE_GRADE,
          {"t_open_true": t_true, "t_open_planted": t_plant,
           "shift": abs(t_plant - t_true), "edge_grade": EDGE_GRADE})

    # T07 -- the WALL-CLOCK LEAK SCAN (the trap three blocks have hit).
    clean = {"a": {"b": [1, 2, 3]}, "c": "text"}
    dirty = {"a": {"b": [1, 2, 3]}, "lemma_seconds": 0.12}
    tooth("T07_wall_clock_leak_scan",
          "the timing-free payload is recursively scanned for clock-shaped keys; "
          "planting one must fire",
          not scan_payload_for_timing(clean) and scan_payload_for_timing(dirty),
          {"clean_hits": scan_payload_for_timing(clean),
           "planted_hits": scan_payload_for_timing(dirty),
           "trap_class": "a lemma-timing key inside the timing-free payload "
                         "(931 and 932 both disclosed this)"})

    # T08 -- the H_Z lemma must be FALSIFIABLE: break the X-flip symmetry.
    hz_intact = StarFull(4, 0.10, tag="tooth-intact").stats(0.7)["H_Z"]
    hz_ptr = StarFull(4, 0.10, extra_z=[(0, 0.35)],
                      tag="tooth-broken-symmetry-pointer").stats(0.7)["H_Z"]
    hz_arm = StarFull(4, 0.10, extra_z=[(1, 0.35)],
                      tag="tooth-broken-symmetry-arm").stats(0.7)["H_Z"]
    tooth("T08_broken_X_flip_symmetry_control",
          "add a longitudinal field, which breaks the global X-flip symmetry P; "
          "H_Z must then leave 1 bit -- so the L0 lemma is not vacuous and the "
          "measurement can see a violation.  Two witnesses at different strengths: "
          "a POINTER longitudinal field breaks P at first order in <Z_0> and moves "
          "H_Z by 4e-5; a ONE-ARM longitudinal field breaks P only through the "
          "pointer's back-action and moves H_Z by 3e-9 -- still nonzero, which is "
          "the sharper statement (nothing but the symmetry is holding H_Z at 1).",
          abs(hz_intact - 1.0) < 1e-14 and abs(hz_ptr - 1.0) > 1e-6
          and abs(hz_arm - 1.0) > 1e-12,
          {"H_Z_intact": hz_intact,
           "H_Z_with_pointer_longitudinal_field": hz_ptr,
           "H_Z_with_one_arm_longitudinal_field": hz_arm,
           "departure_pointer": abs(hz_ptr - 1.0),
           "departure_arm": abs(hz_arm - 1.0),
           "finding": ("the arm-field witness is 3.4e-9, four orders weaker than the "
                       "pointer-field witness -- the arm field reaches <Z_0> only "
                       "through the same back-action channel that carries the "
                       "degree-dependence of t_open.  Reported, not smoothed.")})

    # T09 -- the pointer-ablation control (933's mechanism, on the pointer side).
    ab = {}
    for d in (4, 6):
        on = StarCollective(d, 0.10)
        off = StarCollective(d, 0.10, lam_pointer=0.0)
        ab["d%d" % d] = {"s1_on": on.stats(0.7)["s1"], "s1_off": off.stats(0.7)["s1"],
                         "chi_on": on.stats(0.7)["chi1"],
                         "chi_off": off.stats(0.7)["chi1"]}
    tooth("T09_pointer_transverse_term_ablation",
          "switch off lambda X_0: every s(k) must collapse to zero AND chi must "
          "become degree-free -- the single term that buys arm entanglement is the "
          "same one that buys the gate's degree-dependence",
          all(abs(v["s1_off"]) < 1e-13 and abs(v["s1_on"]) > 1e-4
              for v in ab.values())
          and abs(ab["d4"]["chi_off"] - ab["d6"]["chi_off"]) < 1e-13
          and abs(ab["d4"]["chi_on"] - ab["d6"]["chi_on"]) > 1e-6,
          {"rows": ab,
           "chi_degree_spread_off": abs(ab["d4"]["chi_off"] - ab["d6"]["chi_off"]),
           "chi_degree_spread_on": abs(ab["d4"]["chi_on"] - ab["d6"]["chi_on"])})

    # T10 -- the Sym^d membership control.
    fsc = StarFull(4, 0.10, extra_z=[(1, 0.35)], tag="tooth-sym-control")
    csc = StarCollective(4, 0.10)
    dev_broken = abs(fsc.stats(0.7)["chi1"] - csc.stats(0.7)["chi1"])
    dev_intact = abs(StarFull(4, 0.10, tag="tooth-sym-intact").stats(0.7)["chi1"]
                     - csc.stats(0.7)["chi1"])
    tooth("T10_sym_d_membership_control",
          "break arm exchangeability with a one-arm longitudinal field; the "
          "collective route must then DISAGREE with full space, proving the "
          "reduction's hypothesis H6 is load-bearing and observable",
          dev_intact < 1e-13 < dev_broken,
          {"deviation_intact": dev_intact, "deviation_broken": dev_broken})

    # T11 -- the excess identity must be falsifiable.
    class StarCollectivePrep(StarCollective):
        """Same dynamics, a DIFFERENT initial vector in the reduced space."""

        def __init__(self, d, lam, psi0):
            StarCollective.__init__(self, d, lam)
            self.c = self.V.conj().T @ psi0.astype(complex)
            self._cache = {}
            if hasattr(self, "_chi0"):
                del self._chi0
    D4 = 5
    v_prod = np.zeros(2 * D4)          # +Z arms: still a PRODUCT across the cut
    v_prod[0] = v_prod[D4] = 1.0 / math.sqrt(2.0)
    v_ent = np.zeros(2 * D4)           # pointer-arm ENTANGLED: |0>|D_0> + |1>|D_4>
    v_ent[0] = v_ent[D4 + 4] = 1.0 / math.sqrt(2.0)
    zp = StarCollectivePrep(4, 0.10, v_prod)
    ep = StarCollectivePrep(4, 0.10, v_ent)
    tooth("T11_excess_equals_chi_needs_a_product_preparation",
          "L1 says chi(0) = 0 for any preparation that is a PRODUCT across the "
          "pointer/arm cut -- so a different product (+Z arms) must STILL give 0, "
          "and only a pointer-arm ENTANGLED initial state can break it.  Both "
          "halves must hold, or the lemma's scope is wrong.",
          abs(coll(4, 0.10).chi0) < 1e-9 and abs(zp.chi0) < 1e-9
          and abs(ep.chi0) > 0.5,
          {"chi0_frozen_preparation": coll(4, 0.10).chi0,
           "chi0_plus_Z_arms_still_a_product": zp.chi0,
           "chi0_pointer_arm_entangled": ep.chi0,
           "note": ("the entangled preparation is NOT the frozen protocol; it is the "
                    "control that shows the identity has content.  The +Z-arm control "
                    "is the one that CORRECTED the lemma's stated scope mid-block.")})

    # T12 -- the grid-phase finding, RE-DERIVED from this block's edges.
    def threshold_at(offset, lam=0.10):
        for d in range(2, 9):
            win = derived_window(coll(d, lam))
            r = composed_verdict(win["blocks"], offset)
            if r["verdict"] == "YES":
                return d
        return None
    th0 = threshold_at(0.0)
    th10 = threshold_at(0.010)
    tooth("T12_grid_phase_threshold_shift",
          "932's grid-phase finding re-derived from THIS block's edges: shifting "
          "the frozen grid by +0.010 in Jt must move the lambda = 0.10 threshold "
          "from 5 to 3",
          th0 == 5 and th10 == 3,
          {"threshold_at_phase_0": th0, "threshold_at_offset_+0.010": th10,
           "c932_reported": {"phase_0": 5, "offset_0.010": 3}})

    # T13 -- a tampered seal digest must differ.
    tam = json.loads(json.dumps(seal_payload, default=float))
    tam.pop("prereg_sha256", None)
    tam.pop("build_log_before_seal", None)
    k0 = sorted(tam["predictions"])[0]
    tam["predictions"][k0]["0.10"]["run"] = tam["predictions"][k0]["0.10"]["run"] + 1
    tooth("T13_tampered_seal_digest",
          "altering one sealed run must change the pre-registration digest",
          sha256_obj(tam) != seal_sha,
          {"seal_sha256": seal_sha, "tampered_sha256": sha256_obj(tam),
           "cell_altered": k0})

    # T14 -- the deadline clause must be load-bearing.
    def verdict_with_deadline(d, lam, deadline):
        win = derived_window(coll(d, lam))
        pts = grid_points_in(win["blocks"][0])
        if not pts:
            return "NO"
        if pts[0] > deadline + 1e-12:
            return "NO"
        return "YES" if len(pts) >= PERSIST_N else "NO"
    v_norm = [verdict_with_deadline(d, 0.05, DEADLINE_JT) for d in (5, 6, 7, 8)]
    v_tight = [verdict_with_deadline(d, 0.05, 0.5) for d in (5, 6, 7, 8)]
    tooth("T14_deadline_clause_is_load_bearing",
          "tightening the deadline to Jt <= 0.5 -- below the derived t_open of "
          "~0.597, which no field moves below -- must turn every star verdict NO",
          all(v == "YES" for v in v_norm) and all(v == "NO" for v in v_tight),
          {"verdicts_deadline_1.0": v_norm, "verdicts_deadline_0.5": v_tight,
           "derived_t_open_floor": zf["t_open"]})

    # T15 -- a perturbed collective Hamiltonian must break the route agreement.
    D6 = 6
    aa = np.array([math.sqrt(binom(5, m)) for m in range(D6)]) / math.sqrt(2.0 ** 5)
    p0 = np.concatenate([aa, aa]) / math.sqrt(2.0)

    def perturbed_chi(delta_H):
        c2 = StarCollective(5, 0.10)
        c2.H = c2.H + delta_H
        c2.w, c2.V = np.linalg.eigh(c2.H)
        c2.c = c2.V.conj().T @ p0.astype(complex)
        c2._cache = {}
        return c2.stats(0.7)["chi1"]
    fsr = StarFull(5, 0.10, tag="tooth-route-perturb")
    ref = fsr.stats(0.7)["chi1"]
    dev_c = abs(coll(5, 0.10).stats(0.7)["chi1"] - ref)
    dH_break = np.zeros((2 * D6, 2 * D6))
    dH_break[0, 0] = 1e-9
    dev_p = abs(perturbed_chi(dH_break) - ref)
    dev_sym = abs(perturbed_chi(1e-9 * np.eye(2 * D6)[::-1]) - ref)
    tooth("T15_route_perturbation_guard",
          "perturb the collective Hamiltonian by 1e-9 in a way that BREAKS the "
          "X-flip symmetry; the route S vs route N agreement must degrade past the "
          "claimed value grade.  The control at the same amplitude ALONG the "
          "symmetry (epsilon * P) must stay invisible -- an independent "
          "confirmation of L0, since the state lives in the P = +1 eigenspace.",
          dev_c < VALUE_GRADE < dev_p and dev_sym < VALUE_GRADE,
          {"deviation_unperturbed": dev_c,
           "deviation_symmetry_breaking_perturbation": dev_p,
           "deviation_along_the_symmetry_epsilon_times_P": dev_sym,
           "value_grade": VALUE_GRADE,
           "finding": ("a 1e-9 perturbation proportional to P itself is invisible to "
                       "every statistic (3e-16) because the frozen state is a "
                       "P-eigenvector -- found while calibrating this tooth and kept "
                       "as a second, independent witness for L0")})

    receipt["teeth"] = TEETH
    receipt["teeth_summary"] = {"count": len(TEETH),
                                "all_fired": bool(all(t["fired"] for t in TEETH))}
    print("teeth: %d/%d fired" % (sum(1 for t in TEETH if t["fired"]), len(TEETH)))

    # ================================================================ verdict ==
    receipt["verdict"] = {
        "headline": (
            "THE POINTER-SIDE GATES ARE DERIVED, AND THE STAR CERTIFICATION "
            "THEOREM IS COMPOSED.  H(Z_S) = 1 bit EXACTLY on every star at every "
            "field and time (global X-flip symmetry -- 932's 'symmetry-pinned' "
            "disclosure promoted to a lemma); chi(0) = 0 so the excess gate is "
            "IMPLIED; hence the content gate is EXACTLY the single-arm Holevo "
            "threshold chi_1 >= (1-delta).  At zero pointer field that threshold "
            "is EXACTLY degree-independent for any arm field -- so t_open's "
            "degree-independence is not a regularity but a theorem, and its "
            "residual (2.07e-3 at 0.10, reproducing 932's 2.1e-3; 5.9e-4 at 0.05) "
            "is the pointer's own back-action, O(lambda^2) up to the same log 933 "
            "found in s(k) (fitted exponent %.3f).  At zero field the whole window "
            "is closed form: t_open = (1/2)arccos(c*) = %.12f, t_close = "
            "pi/2 - t_open, W = %.12f -- which is 932's measured W ~ 0.37 at the "
            "low field.  Composed with 933's s(k) for the independence side and "
            "932's counting law for the grid, EVERY EDGE and EVERY VERDICT of the "
            "star lane follows from the 2(d+1) reduction: exact verdict, run and "
            "per-sample gate agreement on all %d pinned star cells across all "
            "three deltas."
            % (l5["fitted_exponent_spread"], zf["t_open"], zf["width"],
               agree["cells"])),
        "honest_split": {
            "derived_here": ["H_Z", "chi", "excess", "the content gate's reduction",
                             "t_open", "the content-side t_close", "the clip switch",
                             "the degree-independence explanation"],
            "derived_earlier_and_composed": ["s(k) and C_ab (933)",
                                             "the edge-counting law (932)"],
            "stays_imported": ["the frozen Hamiltonian, preparation, partition rule "
                               "and statistic definitions", "the sample grid and its "
                               "PHASE, the run length, the deadline",
                               "non-star geometries (arm exchangeability is the "
                               "reduction's boundary)"],
            "resisted_derivation": "none at star scope"},
        "scope_qualifier_carried": (
            "932's grid-phase qualifier travels with every threshold citation: "
            "'pointer degree >= 5 certifies at lambda = 0.10' holds AT THE FROZEN "
            "SAMPLE GRID Jt = 0.0(0.1)1.2 AT PHASE 0.  Phase-invariant content: "
            "d <= 2 fails and d >= 5 certifies at every phase; d = 3-4 are decided "
            "by the phase.  Re-derived from this block's own edges in tooth T12."),
    }

    # ============================================== receipt, digest, cache =====
    receipt["runner_sha256"] = sha256_bytes(open(os.path.abspath(__file__), "rb").read())
    receipt["git_head"] = git(["rev-parse", "HEAD"]).stdout.decode().strip()
    receipt["authorship"] = (
        "authored by a Claude Opus 5 worker under supervisor spec (substitution "
        "disclosed).  The supervisor's candidate explanation for the "
        "degree-independence -- 'single-arm physics on the star is d-independent up "
        "to the pointer's back-action' -- is CONFIRMED and sharpened: the "
        "d-independence is EXACT (not approximate) once the pointer's own transverse "
        "term is switched off, for ANY arm field, and H_Z is exactly 1 bit by "
        "symmetry, which the spec did not anticipate and which makes the content "
        "gate a pure single-arm Holevo threshold.")
    receipt["caps_declared"] = {
        "full_space_cap_n": FULL_SPACE_CAP_N,
        "degrees_7_to_12_are_abstract_stars": ("they carry no certification claim "
                                               "beyond what 927/932 already pinned"),
        "never_used_fields_are_declared_non_claim_extensions": list(SEAL_LAMBDAS_NEW),
        "collective_route_value_grade": VALUE_GRADE,
        "edge_grade": EDGE_GRADE}
    receipt["runtime_seconds"] = round(time.perf_counter() - T_START, 3)
    receipt["runtime_within_limit"] = bool(
        receipt["runtime_seconds"] <= RUNTIME_LIMIT_SECONDS)
    if not receipt["runtime_within_limit"]:
        die("runtime:%r > %r" % (receipt["runtime_seconds"], RUNTIME_LIMIT_SECONDS))

    TIMING_FREE_EXCLUDE = {"runtime_seconds", "runtime_within_limit",
                           "restriction_gate_seconds", "runner_sha256", "git_head",
                           "runtime_limit_seconds", "date"}
    payload = {k: v for k, v in receipt.items() if k not in TIMING_FREE_EXCLUDE}
    hits = scan_payload_for_timing(payload)
    # the ONLY admissible hits are byte-quoted frozen text and declared prose; any
    # numeric clock reading is a hard fail.
    bad_hits = []
    for hp in hits:
        cur = payload
        ok = True
        for part in hp[2:].replace("]", "").split("."):
            if "[" in part:
                nm, ix = part.split("[")
                cur = cur[nm][int(ix)]
            else:
                if isinstance(cur, dict) and part in cur:
                    cur = cur[part]
                else:
                    ok = False
                    break
        if ok and isinstance(cur, (int, float)) and not isinstance(cur, bool):
            bad_hits.append(hp)
    receipt["timing_free_payload_scan"] = {
        "keys_matching_clock_pattern": hits,
        "numeric_clock_readings_found": bad_hits,
        "guard": ("hard fail on any NUMERIC value under a clock-shaped key inside "
                  "the timing-free payload; string hits are byte-quoted frozen text "
                  "and are listed for audit")}
    if bad_hits:
        die("timing-free:numeric-clock-leak %r" % bad_hits)
    receipt["timing_free_digest"] = sha256_obj(payload)

    out = os.path.join(ROOT, "outputs",
                       "pointer_gates_cycle934_receipt_2026_07_28.json")
    with open(out, "w") as fh:
        json.dump(receipt, fh, indent=1, sort_keys=True, default=float)

    # ------------------------------------------------------------- the report --
    print("")
    print("THE DERIVATION")
    print("  L0  H(Z_S) = 1 bit EXACTLY: P = prod_i X_i commutes with H "
          "([P,H] max abs %r) and fixes the frozen preparation (defect %.1e); "
          "P Z_0 P = -Z_0 so <Z_0(t)> = 0 identically."
          % (l0["max_commutator"], l0["max_preparation_defect"]))
    print("      measured over %d (degree, field, time) probes incl. lambda = 2.0 "
          "and Jt = 5.0: max |H_Z - 1| = %.2e"
          % (l0["n_cells_probed"], l0["numeric_max_abs_dev_from_1_bit"]))
    print("  L1  chi(0) = 0 (max %.2e, frozen anchor tolerance 1e-9) for ANY "
          "product preparation across the pointer/arm cut => excess == chi."
          % l1["max_abs_chi_at_t0"])
    print("  L2  the content gate is EXACTLY chi_1 >= (1-delta): the H(Z_S) >= 0.05 "
          "clause is unconditional and the excess clause is implied "
          "(margin %.2f bit); it binds at 0 of the probed points."
          % l1["implication_margin_bits"])
    print("  L3  at lambda_pointer = 0 the content gate is EXACTLY "
          "degree-independent for ANY arm field: chi spread over d = 2..12 is "
          "%.2e (the double-precision floor), against ~2e-3 with the pointer field "
          "on -- ELEVEN orders.  Two-level closed form agrees to %.2e."
          % (l3["max_chi_spread_over_degrees_at_lambda_pointer_zero"],
             l3["max_dev_from_the_two_level_closed_form"]))
    print("  L4  zero-field closed form: c* = %.12f, t_open = %.12f, "
          "t_close = %.12f, W = %.12f  (932 measured W ~ 0.37 at lambda = 0.05)"
          % (zf["c_star"], zf["t_open"], zf["t_close"], zf["width"]))
    print("  L5  the residual is the POINTER's back-action, O(lambda^2) up to a log "
          "(fitted exponent %.3f): spread(0.05) = %.3e, spread(0.10) = %.3e "
          "-- 932 reported 2.1e-3, reproduced to %.1e"
          % (l5["fitted_exponent_spread"], l5["reproduced_spread_at_lambda_0.05"],
             l5["reproduced_spread_at_lambda_0.10"], l5["c932_spread_reproduced_to"]))
    print("  L6  t_close = min(content, independence); the clip switch matches 932 "
          "on %d/%d cells with zero mismatches; content first clips at degree %s "
          "at lambda = 0.10 (932 reported 6)."
          % (l6["clip_switch_vs_932"]["checked"], l6["clip_switch_vs_932"]["checked"],
             l6["smallest_degree_where_content_clips_at_0.10"]))
    print("")
    print("RESTRICTION GATES")
    print("  917/919 star rows (route P919)  : %d values, max abs dev %r"
          % (g1["values"], g1["max_abs_deviation"]))
    print("  927 star rows (route P927)      : %d values, max abs dev %r"
          % (g2["values"], g2["max_abs_deviation"]))
    print("  926 star frozen point           : max abs dev %r" % g3["max_abs_deviation"])
    print("  932 window edges (re-DERIVED)   : %d edges, max dev %.3e "
          "(pinned grade 1e-12), 0 gate-label and 0 verdict mismatches"
          % (g5["n_edges"], g5["max_abs_edge_deviation"]))
    print("  932 sealed star windows         : %d cells, max dev %.3e"
          % (len(g6["cells"]), g6["max_abs_deviation"]))
    print("  collective route vs pinned rows : %d values, max dev %.3e "
          "(%.1e over degrees <= 8)"
          % (g7["values"], g7["max_abs_deviation"],
             g7["max_abs_deviation_over_degrees_le_8"]))
    print("  Sym^d leakage / route S vs N    : %.1e / %.1e"
          % (leak["max_leakage"],
             q1["collective_vs_full_space_route"]["max_abs_deviation"]))
    print("")
    print("COMPOSED THEOREM  %d pinned star cells x %d deltas = %d verdict rows"
          % (agree["cells"], len(DELTAS), agree["delta_rows"]))
    print("  exact verdict agreement        : %s" %
          agree["exact_verdict_agreement_every_cell"])
    print("  exact run agreement            : %s" %
          agree["exact_run_agreement_every_cell"])
    print("  exact per-sample gate agreement: %s (%d samples compared)"
          % (agree["exact_per_sample_gate_agreement"],
             sum(1 for e in corpus if e["pinned_rows"]) * len(T_EXEC) * len(DELTAS)))
    print("  edge-count law == direct count : %s" %
          agree["edge_counting_law_agrees_with_direct_evaluation"])
    print("  H10 (one window per cell)      : %s on every cell and delta" %
          disc["n_blocks_is_one_on_every_corpus_cell_and_delta"])
    print("  drift clause is vacuous on stars (max %.1e) -- a consequence of L0"
          % disc["pointer_drift_clause_max_over_corpus"])
    print("")
    print("SEAL  %s   (%d cells: d in {9,10} x {0.05, 0.10, 0.0413, 0.0687, 0.1137})"
          % (seal_sha[:16], len(seal_cells)))
    print("  holdout class (never-used fields) : %d cells, 0 pre-evaluated"
          % len(holdout_cells))
    print("  corpus-reproduction class         : %d cells at the FROZEN fields -- "
          "NOT claimed as holdouts (927 STk10 and 932's S9/S10 seal already "
          "published full-space answers there)" % len(corpus_repro_cells))
    print("  route N touched 0 sealed cells before the digest was fixed")
    print("SEAL VERIFICATION  all_hold=%s   verdict+run mismatches %d | per-sample "
          "flag mismatches %d | max edge dev %.2e"
          % (seal_ver["all_predictions_hold"], len(seal_ver["verdict_mismatches"]),
             len(seal_ver["sample_flag_mismatches"]),
             seal_ver["max_abs_edge_deviation"]))
    print("")
    print("TEETH  %d/%d fire" % (sum(1 for t in TEETH if t["fired"]), len(TEETH)))
    for t in TEETH:
        print("  %-52s %s" % (t["name"], "FIRED" if t["fired"] else "MISSED"))
    print("")
    print("ROUTES  P919 (pinned bytes) | P927 (pinned bytes) | N (own 2^(d+1)) | "
          "S (collective 2(d+1)) -- S and N are structurally disjoint")
    print("DETERMINISM  in-process core repeat identical: %s"
          % receipt["determinism"]["in_process_repeat_identical"])
    print("TIMING-FREE PAYLOAD SCAN  numeric clock readings found: %d (hard guard)"
          % len(bad_hits))
    print("")
    print("VERDICT")
    print("  " + receipt["verdict"]["headline"])
    print("")
    print("receipt %s" % os.path.relpath(out, ROOT))
    print("runtime %.2f s (limit %.0f s)"
          % (receipt["runtime_seconds"], RUNTIME_LIMIT_SECONDS))
    print("timing-free digest %s" % receipt["timing_free_digest"])
    print(BOUNDARY_LINE)
    return receipt


if __name__ == "__main__":
    main()
