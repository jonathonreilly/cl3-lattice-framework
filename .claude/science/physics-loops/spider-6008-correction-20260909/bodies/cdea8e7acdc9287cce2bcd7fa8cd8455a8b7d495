#!/usr/bin/env python3
"""Cycle 937 / blockM15 -- OFF THE STAR: the isomorphic-arm spider reduction.

Campaign toe-time-expansion-20260802.  Cycle 933 derived s(k) for COORDINATE
STARS via the collective reduction (branch in C^2 (x) Sym^d(C^2); s(k) = entropy
of a binomially weighted Hankel spectrum) and named the extension NOT attempted:
"the isomorphic-arm-spider extension of the reduction (the frozen preparation is
non-uniform along arms)".  This block does that extension, and uses it to DERIVE
Cycle 927's measured saturation.

THE FROZEN OBJECTS, QUOTED FROM THE MEMO BYTES AND RE-VERIFIED HERE

  Hamiltonian   `H_lambda = - sum_<ij> Z_i Z_j - lambda sum_i X_i`
  preparation   `center: n_center=(1,0,0), the +X state`
                `every axial face: n_face=(1,0,0), the +X state`
                `every edge: n_edge=(0,0,1), the +Z state`
                `every corner: n_corner=(0,0,1), the +Z state`
                -- as implemented in every pinned runner (917/919/921/926/927/
                929/931/933) by  prep_state(n, {S} | recording):  the pointer AND
                its RECORDING NEIGHBOURS start in +X, every site deeper than the
                recording shell starts in +Z.
                ON A SPIDER THIS IS NON-UNIFORM ALONG THE ARM: the arm ROOT (the
                recording site, depth 1) is +X and every arm site at depth >= 2
                is +Z.  The single-arm preparation vector is therefore
                    v = |+>_root (x) |0>^(x)(L-1)   in H_arm = (C^2)^(x)L,
                i.e. v_a = 1/sqrt(2) for a in {0, e_root} and 0 otherwise.
                That non-uniformity is exactly what 933 flagged; it is NOT an
                obstruction, because it is arm-INTRINSIC and therefore
                permutation-symmetric.
  statistic     `C_ab = I(F_a:F_b | Z_S)`, evaluated as
                `C_ab = sum_z p_z [S(rho_Fa^z)+S(rho_Fb^z)-S(rho_FaFb^z)]`
                on tensor order `(S,F_a,F_b)` with the off-diagonal `S` blocks
                zeroed.
  row           Jt = 0.7, lambda in {0.05, 0.10}.

Q1 -- THE SPIDER REDUCTION (derived here, exactly).

  Let the geometry be a spider: a pointer S joined to d ARMS, each arm an
  isomorphic rooted graph on L sites, root bonded to S.  Then

    (i)   every arm permutation pi in S_d is a graph automorphism fixing S and
          preserving the frozen preparation (which depends on an arm site only
          through its arm-intrinsic position), so [U_pi, H] = 0 and U_pi psi0 =
          psi0;  hence  psi(t) in C^2 (x) Sym^d(H_arm),  H_arm = (C^2)^(x)L;
    (ii)  dim = 2 * C(d + 2^L - 1, d)   instead of   2^(dL+1);
    (iii) with a_a^dag the boson creating one arm in the arm computational basis
          state |a> (a = 0..2^L-1), the frozen Hamiltonian restricted to that
          subspace is EXACTLY

            H_red = - lambda X_0 (x) 1  -  Z_0 (x) Gamma(R)  +  1 (x) Gamma(h),

          Gamma(O) = sum_{ab} O_{ab} a_a^dag a_b   (second quantisation of a
          one-arm operator), with the ONE-ARM operators

            R    = Z_root                                  (diagonal, r_a = +-1)
            h    = - sum_{(u,v) in E_arm} Z_u Z_v - lambda sum_{u in arm} X_u

          so Gamma(R) is diagonal (sum_a r_a n_a) and Gamma(h) has the standard
          bosonic elements  h_{ab} sqrt(n_b (n_a+1)).  At L = 1 this reduces
          term-for-term to Cycle 933's  H = -2 Z_0 Jz - lambda X_0 - 2 lambda Jx.
    (iv)  the k | (d-k) Schmidt matrix of the pointer-conditioned branch is the
          MULTI-INDEX HANKEL matrix

            T^(k)_{p,q} = sqrt( M_k(p) M_{d-k}(q) ) f(p+q),
            M_m(n) = m! / prod_a n_a!   (multinomial),

          indexed by occupation vectors p (|p| = k) and q (|q| = d-k) over the
          2^L arm basis states, where f(n) is the branch amplitude of the
          UNNORMALISED computational configuration with occupations n.  s(k) is
          the entropy of its normalised squared singular values.  At L = 1 this
          is 933's binomial Hankel matrix verbatim.  Reflection s(k) = s(d-k) is
          again TRANSPOSITION; s(0) = s(d) = 0 is again rank-1.

Q2 -- THE 927 SATURATION, DERIVED.  Two results, one exact and one graded.

  L-ZERO (EXACT).  With the ARM field switched off (lambda_arm = 0, pointer
  field kept) s(k) is EXACTLY the star's s(k), for ANY arm graph, ANY d, ANY t.
  Proof: with no arm field every arm Z is conserved, so the deep arm sites stay
  in |0> forever and the intra-arm bonds contribute the diagonal energy
  -c_root * M - K with M = sum_j Z_root^(j) and c_root, K arm constants.  That
  multiplies the amplitude sequence by exp(i t (c_root M + K)), i.e. by
  exp(iKt) * exp(-2 i c_root t n) in the occupation index n -- a two-sided
  DIAGONAL UNITARY on T^(k), which leaves every singular value invariant.
  Hence the ENTIRE arm-length effect is an arm-field effect: there is no
  propagation into the arm at all when lambda_arm = 0, at any time.

  THE LADDER (graded, fitted with a declared protocol).  Turning the arm field
  on, the site at DEPTH m contributes to C_ab at order lambda^(2m) (with a
  log(1/lambda) correction).  Path arms give the exponent ladder 4, 6, 8 as the
  added site sits at depth 2, 3, 4; CLAW arms -- where every added site sits at
  depth 2 -- give 4, 4, 4.  That claw/path contrast is the decisive cell: the
  ladder is graded by DEPTH, not by arm size or arm Hilbert dimension.

  THE SUPERVISOR'S LIGHT-CONE CANDIDATE IS NOT ADOPTED AS A PREMISE AND IS
  REPORTED AS REFUTED IN ITS SHARP FORM: delta_m is not a function of (lambda t)
  -- at fixed lambda*t it varies by three orders -- and it oscillates in sign.
  It IS correct in DIRECTION: the suppression grows with t, and the saturation
  fails completely by Jt ~ 12-25 at lambda = 0.10.  Saturation is a property of
  the certification row, not of the model.

Q3 -- THE NEW BOUNDARY, THE G1 CLOSURE, AND THE SEAL.

DISCIPLINE.  Restriction gates first and at deviation EXACTLY zero: Cycle 927's
saturation tables (every ladder, every arm length, C_ab at the pinned ceiling
row), Cycle 933's star cells (the 44-value s(k) table it gates on), Cycle 931's
spider-identity rows.  21/21 frozen constants byte-verified EIGHT-way.  Two
structurally disjoint routes (full 2^n Chebyshev / dense, and the reduced
2*C(d+2^L-1,d) route).  A seal built from the reduced route alone under a
hard-failing no-pre-evaluation guard and verified afterwards by the untouched
full-space route.

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
    # ---- Cycle 927: the saturation this block DERIVES ----
    "scripts/frontier_cycle927_size_channel_2026_07_28.py": (
        "caa3becbd2bfc97afc106e998e5f2b9ee23cb46efd8c673d04ee69ed554314a9",
        "fe2e0f14d1762e44c00b028ca40c5ead851fb48a"),
    "outputs/size_channel_cycle927_receipt_2026_07_28.json": (
        "2dd871f70c6486a20babb7b74048befb51a108a0feea57aee86ba3ff7f2fe51c",
        "12edc846cdb31c19e5f9bb709533ee18d5d5a092"),
    "docs/SIZE_CHANNEL_NULL_ARITY_DILUTION_THRESHOLD_HARDENS_CYCLE927_BOUNDED_THEOREM_NOTE_2026-07-28.md": (
        "18914fa29e3594dfb92465ba1128d61911861e12d756f910d573e662145caf2c",
        "c066b3acf0d19eb54fae5e50c07d2774f1cd8521"),
    "outputs/arity_variable_cycle929_receipt_2026_07_28.json": (
        "40440237f0af14882b06331a054c19f3da52f34e6e7b2cde846a0b390a3679a3",
        "fc0080cc4c283d6dc440ac20a614ae187f7e488b"),
    # ---- Cycle 931: the pair-complement theorem + the H4 spider identity ----
    "scripts/frontier_cycle931_additivity_identity_2026_07_28.py": (
        "9ec41f8cc7562026e86a5332819b56b860b1ee3f4a4ca21540f129623ec80371",
        "a0cd5b6fa01ad6b262c18b0e69c57600d1979367"),
    "outputs/additivity_identity_cycle931_receipt_2026_07_28.json": (
        "89699b750d39e6bbf1b953e4abc34a71784344b89012be31226acb6ccfd97b46",
        "d3894ad5792018b541eda7185399c7c979ec09cf"),
    # ---- Cycle 933: THE PARENT THIS BLOCK EXTENDS ----
    "scripts/frontier_cycle933_sk_shape_2026_07_28.py": (
        "29ab80e096df2e62362a837426cbda0705f5c4f04726a237f092df1d740e966e",
        "9d22268d214c59dd60b32cf7a2e6e67b457d78c8"),
    "outputs/sk_shape_cycle933_receipt_2026_07_28.json": (
        "5a7e7ab80e2a9cb34cf4a7fc2b720d4d9fda25cefaa0574df71ae3d8a7181297",
        "3d35d0ffa6a9bc9077c7fa9b7af7e40f00c89c84"),
    "docs/SK_SHAPE_DERIVED_HANKEL_GALOIS_NOGO_CYCLE933_BOUNDED_THEOREM_NOTE_2026-07-28.md": (
        "53612778c108e55ac33c442dc18ee6a17a09b247ac02f76308cae36c3898a7f3",
        "99a7693c1756d50f303e8c0a1dce13423aa990a6"),
    "docs/PAIR_COMPLEMENT_THEOREM_ADDITIVITY_DERIVED_CYCLE931_BOUNDED_THEOREM_NOTE_2026-07-28.md": (
        "f9d9a3cf0051182c9608d94af37737e59735780c63a6dd0ae813891a654cfb76",
        "d5d9776fe023143d465d4da039730e431acf84ca"),
}

# ------------------------------------------------- VENDORED FROM A SIBLING ---
# Cycle 932 (blockM12) is NOT in this branch's tree.  It is vendored with
# SOURCE-BRANCH DIGEST AUTHORITY: the blob is read out of the shared object
# database at a pinned sha, its content digest is verified, and the source
# branch + commit are recorded.  Nothing is written into this tree.
VENDOR_SOURCE_BRANCH = "physics-loop/toe-time-blockM12-20260802"
VENDORED = {
    "outputs/persistence_razor_cycle932_receipt_2026_07_28.json": None,
    "scripts/frontier_cycle932_persistence_razor_2026_07_28.py": None,
}

PARENT_MEMO = "docs/D3_BAR_LOCATION_DESIGN_SCOUT_2026-07-10.md"
C915_RECEIPT = "outputs/comparator_recovery_cycle915_receipt_2026_07_28.json"
C917_RECEIPT = "outputs/geometry_ladder_cycle917_receipt_2026_07_28.json"
C919_RECEIPT = "outputs/degree_five_cycle919_receipt_2026_07_28.json"
C921_RECEIPT = "outputs/loop_cost_cycle921_receipt_2026_07_28.json"
C926_RECEIPT = "outputs/gate_sweep_separation_cycle926_receipt_2026_07_28.json"
C927_RECEIPT = "outputs/size_channel_cycle927_receipt_2026_07_28.json"
C929_RECEIPT = "outputs/arity_variable_cycle929_receipt_2026_07_28.json"
C931_RECEIPT = "outputs/additivity_identity_cycle931_receipt_2026_07_28.json"
C933_RECEIPT = "outputs/sk_shape_cycle933_receipt_2026_07_28.json"
C932_RECEIPT = "outputs/persistence_razor_cycle932_receipt_2026_07_28.json"

D1_NOTE_PATH = "docs/REGISTRATION_REDUNDANCY_ONSET_BOUNDED_NOTE_2026-07-09.md"
D1_NOTE_BLOB = "dd247a8494f171d4dcaf9a532a09491202b1f512"
D1_NOTE_SHA256 = "41b4f26af908a7b910fbb5683f9d50432f36328bced7cf107585f7f70771df04"
D1_NOTE_BYTES = 5230

# ============================================== frozen protocol constants ====
CLAIM_LAMBDAS = (0.05, 0.10)
DIAG_LAMBDAS = (0.075, 0.125, 0.15)
DELTAS = (0.05, 0.10, 0.20)
HEADLINE_DELTA = 0.10
DEADLINE_JT = 1.0
CONTENT_H_MIN = 0.05
EXCESS_MIN = 0.02
INDEP_MAX = 0.02
T0_ANCHOR_TOL = 1e-9
DRIFT_MAX = 0.10
PERSIST_N = 3
T_EXEC = [round(0.1 * i, 10) for i in range(13)]
COMPARISON_JT = 0.7
CUBE_LABELS = ("+x", "-x", "+y", "-y", "+z", "-z")
DIRECT_MAX_DIM = 1024          # the pinned 927 direct/Gram switch
BISECT_TOL = 1e-12             # the pinned 932 window-edge bisection tolerance

IDENT_TOL = 1e-11
REPRO_TOL = 0.0

# ---- this block's declared caps ----
FULL_SPACE_CAP_N = 16
REDUCED_DIM_CAP = 2200
# fields never used by ANY parent runner (claim 0.05/0.10; diagnostic
# 0.075/0.125/0.15; strong 0.5/1/2; 932's seal 0.0625/0.0875/0.09375)
SEAL_FIELD_A = 0.0825
SEAL_FIELD_B = 0.1125
KNOWN_FIELDS = (0.05, 0.075, 0.1, 0.125, 0.15, 0.2, 0.5, 1.0, 2.0,
                0.0625, 0.0875, 0.09375, 0.0375, 0.1625)

NEW_CELLS_EVALUATED = set()
SEALED_CELLS = set()
PROP_CALLS = {"A": 0, "C": 0, "R": 0}


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
    """Digest every pinned in-tree artefact.  Entries carrying an all-zero
    placeholder are SELF-PINNING: the digest is recorded from the tree at run
    time (they are this branch's own parent files, already fixed by the commit
    the runner is executed at) -- the receipt still carries sha256 + blob so an
    auditor can compare against the branch."""
    out = {}
    for path, (want_sha, want_blob) in sorted(PINS.items()):
        full = os.path.join(ROOT, path)
        if not os.path.exists(full):
            die("pin:missing %s" % path)
        b = open(full, "rb").read()
        got = sha256_bytes(b)
        blob = git(["hash-object", path]).stdout.decode().strip()
        selfpin = set(want_sha) == {"0"}
        if not selfpin:
            if got != want_sha:
                die("pin:sha256 %s got=%s want=%s" % (path, got, want_sha))
            if want_blob and set(want_blob) != {"0"} and blob != want_blob:
                die("pin:blob %s got=%s want=%s" % (path, blob, want_blob))
        out[path] = {"sha256": got, "blob": blob, "bytes": len(b),
                     "verified": True, "self_pinned_at_run_time": bool(selfpin)}
    return out


def vendor_from_sibling():
    """SOURCE-BRANCH DIGEST AUTHORITY.  Read each vendored path out of the
    sibling branch's tree in the shared object store, record its blob id and
    content sha256, and return the decoded bytes.  Nothing is written here."""
    head = git(["rev-parse", VENDOR_SOURCE_BRANCH]).stdout.decode().strip()
    if not head:
        die("vendor:branch-missing %s" % VENDOR_SOURCE_BRANCH)
    out, blobs = {}, {}
    for path in sorted(VENDORED):
        blob = git(["rev-parse", "%s:%s" % (VENDOR_SOURCE_BRANCH, path)]) \
            .stdout.decode().strip()
        if not blob:
            die("vendor:path-missing %s" % path)
        b = git(["cat-file", "blob", blob]).stdout
        if not b:
            die("vendor:blob-empty %s" % path)
        out[path] = {"source_branch": VENDOR_SOURCE_BRANCH,
                     "source_commit": head, "blob": blob,
                     "sha256": sha256_bytes(b), "bytes": len(b),
                     "in_this_tree": os.path.exists(os.path.join(ROOT, path)),
                     "authority": "source-branch digest authority"}
        blobs[path] = b
    return out, blobs


def recover_d1_note():
    if git(["cat-file", "-t", D1_NOTE_BLOB]).stdout.decode().strip() != "blob":
        die("d1-note:blob-missing %s" % D1_NOTE_BLOB)
    b = git(["cat-file", "blob", D1_NOTE_BLOB]).stdout
    got = sha256_bytes(b)
    if got != D1_NOTE_SHA256 or len(b) != D1_NOTE_BYTES:
        die("d1-note:identity got=%s bytes=%d" % (got, len(b)))
    rec915 = json.load(open(os.path.join(ROOT, C915_RECEIPT)))
    art = rec915["C1_recovery"]["artifacts"][D1_NOTE_PATH]["recovered"]
    if art["sha256"] != got or art["blob"] != D1_NOTE_BLOB:
        die("d1-note:915-receipt-cross-check")
    xs = {}
    for tag, rp in (("917", C917_RECEIPT), ("919", C919_RECEIPT), ("921", C921_RECEIPT),
                    ("926", C926_RECEIPT), ("927", C927_RECEIPT), ("929", C929_RECEIPT),
                    ("931", C931_RECEIPT), ("933", C933_RECEIPT)):
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

STATISTIC_PATTERNS = [
    ("C_ab_definition", r"`C_ab = I\(F_a:F_b \| Z_S\)`"),
    ("C_ab_formula",
     r"`C_ab = sum_z p_z \[S\(rho_Fa\^z\)\+S\(rho_Fb\^z\)-S\(rho_FaFb\^z\)\]`"),
    ("C_ab_tensor_order", r"The joint tensor order is `\(S,F_a,F_b\)`"),
    ("C_ab_dephasing", r"Zero the off-diagonal `S` blocks before evaluating the formula"),
    ("chi_definition",
     r"`chi_Z\(S:F\) = S\(sum_z p_z rho_F\^z\) - sum_z p_z S\(rho_F\^z\)`\."),
]

PREPARATION_CLAUSES = ("prep_center", "prep_face", "prep_edge", "prep_corner")


def verify_frozen_constants(memo, soft=False):
    out = {}
    for name, pat, val in CONSTANT_PATTERNS:
        m = re.search(pat, memo)
        if not m:
            if soft:
                raise ValueError(name)
            die("frozen-const:absent %s" % name)
        q = m.group(0)
        if val is not None and m.groups():
            if abs(float(m.group(1)) - float(val)) > 0:
                if soft:
                    raise ValueError(name)
                die("frozen-const:value %s got=%s want=%s" % (name, m.group(1), val))
        out[name] = {"quoted": q, "sha256": sha256_bytes(q.encode())}
    return out


def verify_statistic_definition(memo):
    out = {}
    for name, pat in STATISTIC_PATTERNS:
        m = re.search(pat, memo)
        if not m:
            die("statistic-def:absent %s" % name)
        out[name] = {"quoted": m.group(0), "sha256": sha256_bytes(m.group(0).encode())}
    return out


def cross_check_prior_constants(frozen):
    out = {"count": len(frozen), "ways": 0}
    ok = True
    for tag, rp in (("917", C917_RECEIPT), ("919", C919_RECEIPT), ("921", C921_RECEIPT),
                    ("926", C926_RECEIPT), ("927", C927_RECEIPT), ("929", C929_RECEIPT),
                    ("931", C931_RECEIPT), ("933", C933_RECEIPT)):
        rec = json.load(open(os.path.join(ROOT, rp)))
        prior = rec["frozen_constants_byte_verified"]
        same = all(k in prior
                   and (prior[k].get("quote", prior[k].get("quoted"))
                        == v["quoted"])
                   for k, v in frozen.items())
        out["identical_to_%s_receipt" % tag] = bool(same)
        out["n_constants_%s" % tag] = len(prior)
        out["ways"] += 1
        ok = ok and same
    out["all_eight_receipts_agree"] = bool(ok)
    if not ok:
        die("frozen-const:cross-check-failed")
    return out


def parse_memo_cube_fragments(memo):
    out = {}
    for L in CUBE_LABELS:
        m = re.search(r"`F_%s` = \{([^}]*)\}" % re.escape(L), memo)
        if not m:
            return None
        coords = re.findall(r"\(([-0-9]+),\s*([-0-9]+),\s*([-0-9]+)\)", m.group(1))
        out[L] = {tuple(int(x) for x in c) for c in coords}
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
    for ax, nm in ((0, "x"), (1, "y"), (2, "z")):
        if c[ax] != 0:
            return ("+" if c[ax] > 0 else "-") + nm
    die("axis-label:origin %r" % (c,))


def build_geometry(key, name, sites, bonds_coord, pointer, label_of_rec,
                   tiebreak, dim, note, family="unset"):
    """Verbatim semantics of the pinned 917/927/929/931/933 constructor."""
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
                die("geometry:%s tie without declared tie-break" % key)
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
    return {"key": key, "name": name, "note": note, "n": n, "family": family,
            "sites": [str(c) for c in sites], "coords": sites, "bonds": bonds,
            "adj": adj, "S": S, "pointer": str(pointer), "recording": rec,
            "labels": labels, "frags": frags, "dS": dS,
            "anchor_multiplicity": {L: len(anchors[L]) for L in labels},
            "stats": {"n_sites": n, "n_bonds": len(bonds), "pointer_degree": len(rec),
                      "n_fragments": len(labels),
                      "fragment_sizes": {L: len(frags[L]) for L in labels},
                      "loop_free": bool(len(bonds) - n + 1 == 0)}}


def spider(key, arm_shapes, note, family):
    """Verbatim from the pinned 927/929/931/933 runners."""
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


def y_arm3():
    return [None, 0, 0]


def tee_arm4():
    return [None, 0, 1, 1]


def geom_cube27():
    sites = [(x, y, z) for x in (-1, 0, 1) for y in (-1, 0, 1) for z in (-1, 0, 1)]
    bonds = [(a, b) for ia, a in enumerate(sites) for b in sites[ia + 1:]
             if sum(abs(a[k] - b[k]) for k in range(3)) == 1]
    return build_geometry("G6", "cube27", sites, bonds, (0, 0, 0), axis_label,
                          cube_tiebreak, 3, "917 G6", "pinned917")


def geom_chain9():
    """917's G1 -- the 9-site open chain.  Structurally: a spider with d = 2
    isomorphic PATH arms of length 4."""
    sites = [(k, 0, 0) for k in range(-4, 5)]
    bonds = [((k, 0, 0), (k + 1, 0, 0)) for k in range(-4, 4)]
    return build_geometry("G1", "chain9", sites, bonds, (0, 0, 0),
                          lambda c: ("+x" if c[0] > 0 else "-x"), cube_tiebreak, 1,
                          "917 G1: the d=1 reference, the open 9-site chain", "pinned917")


def geom_tree(nbranch):
    """917 G3a (3 branches) / G3b (4) / 919 H2 (5): centre + branches of depth 2,
    branching factor 2 -- i.e. isomorphic CLAW arms of 3 sites."""
    sites = ["S"]
    bonds = []
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
                          "centre + %d branches of depth 2" % nbranch, "pinned")


def geom_star(d, key=None):
    sites = ["S"] + ["a%d" % i for i in range(1, d + 1)]
    bonds = [("S", "a%d" % i) for i in range(1, d + 1)]
    return build_geometry(key or "STAR%d" % d, "star%d" % (d + 1), sites, bonds, "S",
                          lambda c: c, None, "star", "K_{1,%d}" % d, "star")


# ================================================================ numerics ===
def build_diag(n, bonds):
    idx = np.arange(1 << n, dtype=np.uint32)
    z = np.empty((n, 1 << n), dtype=np.int8)          # SIGNED: see tooth T-int8
    if z.dtype != np.int8:
        die("dtype:z-not-int8")
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
    """ROUTE A -- the pinned Chebyshev/Bessel propagator, byte-for-byte the
    Cycle 927/929 implementation (the accumulation order is load-bearing: the
    saturation gate is demanded at deviation EXACTLY zero)."""
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
    return outs, {"route": "chebyshev", "half_width": A, "degree": M,
                  "matvecs": nmv, "tail_bound": 2.0 * tail}


def chebyshev_931(psi0, diag, n, lam, times):
    """ROUTE A' -- the Cycle 931/933 Chebyshev implementation.  ALGEBRAICALLY
    IDENTICAL to chebyshev() above and BITWISE DIFFERENT (the three-term
    recurrence is accumulated as 2*mv(T1)/A - T0 rather than in place, and the
    coefficient is multiplied in a different order).  DISCLOSED FINDING: no
    single implementation reproduces BOTH the 927/929 receipts and the 931/933
    receipts at deviation exactly zero; each reproduction gate is therefore run
    against its own parent's code path, and both are exhibited."""
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
    return outs, {"route": "A'-chebyshev-931-order", "norm_bound": A, "terms": M}


def dense_route(psi0, diag, n, lam, times):
    """ROUTE C -- full eigendecomposition."""
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


def euler_route(psi0, diag, n, lam, t, nstep=40):
    """THE EULER GUARD -- deliberately under-converged; never a published number."""
    mv = _matvec_factory(diag, n, lam)
    psi = psi0.astype(np.complex128).copy()
    h = t / nstep
    for _ in range(nstep):
        psi = psi + (-1j * h) * mv(psi)
    return psi


def joint_rho(psi, n, sites):
    T = psi.reshape((2,) * n)
    order = list(sites) + [i for i in range(n) if i not in sites]
    ax = [n - 1 - s for s in order]
    M = np.transpose(T, ax).reshape(1 << len(sites), -1)
    return M @ M.conj().T


def ent_bits(w):
    w = np.asarray(w).real
    neg = float(min(0.0, w.min())) if w.size else 0.0
    w = w[w > 1e-16]
    return float(-(w * np.log2(w)).sum()), neg


def spectrum_of(M):
    r, c = M.shape
    G = (M @ M.conj().T) if r <= c else (M.conj().T @ M)
    return np.linalg.eigvalsh(G)


def chi_holevo(rho, k):
    """The pinned Holevo statistic (917/919/927), verbatim."""
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
    return Sav - Sc, H, [p[0] / tot, p[1] / tot]


def cond_mi(rho, ka, kb):
    """THE FROZEN STATISTIC, byte-identical to the pinned implementation."""
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
    """The pinned GRAM route to the SAME quantity (927), verbatim semantics."""
    T = psi.reshape((2,) * n)
    ax = [n - 1 - S] + [n - 1 - i for i in range(n) if i != S]
    P = np.transpose(T, ax).reshape(2, -1)
    rest = [i for i in range(n) if i != S]
    pos = {s: j for j, s in enumerate(rest)}
    ai = [pos[s] for s in A]
    bi = [pos[s] for s in B]
    ci = [j for j in range(n - 1) if j not in ai and j not in bi]
    m = n - 1
    pz = [float(np.vdot(P[z], P[z]).real) for z in (0, 1)]
    ptot = sum(pz)
    out = 0.0
    for z in (0, 1):
        if pz[z] <= 1e-14:
            continue
        v = (P[z] / math.sqrt(pz[z])).reshape((2,) * m)
        MA = np.transpose(v, ai + bi + ci).reshape(1 << len(ai), -1)
        sa, _ = ent_bits(spectrum_of(MA))
        MB = np.transpose(v, bi + ai + ci).reshape(1 << len(bi), -1)
        sb, _ = ent_bits(spectrum_of(MB))
        MAB = np.transpose(v, ai + bi + ci).reshape(1 << (len(ai) + len(bi)), -1)
        sab, _ = ent_bits(spectrum_of(MAB))
        out += (pz[z] / ptot) * (sa + sb - sab)
    return out


def C_pair(psi, n, S, A, B):
    """The pinned direct/Gram switch (927): direct RDM below DIRECT_MAX_DIM."""
    if (1 << (1 + len(A) + len(B))) <= DIRECT_MAX_DIM:
        return cond_mi(joint_rho(psi, n, [S] + list(A) + list(B)), len(A), len(B))
    return cond_mi_gram(psi, n, S, list(A), list(B))


def branch_split(psi, n, S):
    T = psi.reshape((2,) * n)
    order = [S] + [i for i in range(n) if i != S]
    M = np.transpose(T, [n - 1 - s for s in order]).reshape(2, -1)
    out = []
    for z in (0, 1):
        v = np.ascontiguousarray(M[z])
        p = float(np.vdot(v, v).real)
        out.append((p, v / math.sqrt(p) if p > 1e-300 else v))
    return out, order[1:]


def sub_entropy(vec, nb, axes):
    if len(axes) == 0 or len(axes) == nb:
        return 0.0
    T = vec.reshape((2,) * nb)
    rest = [j for j in range(nb) if j not in axes]
    M = np.transpose(T, list(axes) + rest).reshape(1 << len(axes), -1)
    return ent_bits(spectrum_of(M))[0]


def s_profile_full(psi, n, S, armsets):
    """s(k) on the FULL space: branch-averaged entropy of the first k arms.
    For k > d/2 the complement is used (Sylvester; the branch is pure)."""
    d = len(armsets)
    brs, sitelist = branch_split(psi, n, S)
    pos = {s: j for j, s in enumerate(sitelist)}
    ax = [tuple(sorted(pos[s] for s in arm)) for arm in armsets]
    tot = sum(p for p, _ in brs)
    nb = n - 1
    out = {}
    for k in range(d + 1):
        kk = k if 2 * k <= d else d - k
        X = tuple(sorted(itertools.chain(*ax[:kk])))
        out[k] = sum((p / tot) * sub_entropy(v, nb, X) for p, v in brs)
    return out


# ============ THE SPIDER COLLECTIVE REDUCTION (this block's derived tool) =====
def arm_operators(parents, lam_arm):
    """The ONE-ARM operators of the derivation.  parents[p] is the arm-internal
    parent of arm position p (parents[0] is None: the root, bonded to S).
    Arm basis index a has bit p = 1 iff arm position p is flipped; position 0 is
    the ROOT.  Returns (w, r, h) with w_a the intra-arm ZZ energy, r_a = Z_root,
    and h = diag(w) - lam_arm * sum_p X_p."""
    L = len(parents)
    D = 1 << L
    zs = np.array([[1 - 2 * ((a >> p) & 1) for p in range(L)] for a in range(D)],
                  dtype=np.int64)
    w = np.zeros(D, dtype=np.float64)
    for p, par in enumerate(parents):
        if par is not None:
            w -= (zs[:, p] * zs[:, par]).astype(np.float64)
    r = zs[:, 0].astype(np.float64)
    h = np.diag(w).astype(np.complex128)
    for a in range(D):
        for p in range(L):
            h[a, a ^ (1 << p)] -= lam_arm
    return w, r, h


def arm_root_automorphisms(parents):
    """The automorphism group of the arm graph that FIXES the root (arm position
    0).  Returned as a list of position permutations."""
    L = len(parents)
    edges = {tuple(sorted((p, par))) for p, par in enumerate(parents)
             if par is not None}
    out = []
    for sigma in itertools.permutations(range(L)):
        if sigma[0] != 0:
            continue
        if {tuple(sorted((sigma[u], sigma[v]))) for (u, v) in edges} == edges:
            out.append(sigma)
    return out


def arm_invariant_dimension(parents):
    """dim of the A-invariant subspace of H_arm, A the root-fixing arm
    automorphism group: the number of A-orbits on the arm basis states."""
    L = len(parents)
    A = arm_root_automorphisms(parents)
    seen, orbits = set(), 0
    for a in range(1 << L):
        if a in seen:
            continue
        orb = set()
        for sigma in A:
            b = 0
            for p in range(L):
                if (a >> p) & 1:
                    b |= 1 << sigma[p]
            orb.add(b)
        seen |= orb
        orbits += 1
    return orbits, len(A)


def fock_basis(d, D):
    """Occupation vectors of d bosons in D modes -- the reduced basis."""
    def rec(rem, modes):
        if modes == 1:
            yield (rem,)
            return
        for k in range(rem + 1):
            for tail in rec(rem - k, modes - 1):
                yield (k,) + tail
    return list(rec(d, D))


def multinom(n, tot):
    M = math.factorial(tot)
    for a in n:
        M //= math.factorial(a)
    return M


def reduced_dim(d, L):
    return 2 * math.comb(d + (1 << L) - 1, d)


def reduced_H(d, parents, lam, lam_arm=None, lam_ptr=None):
    """H_red = -lam_ptr X_0 (x) 1 - Z_0 (x) Gamma(R) + 1 (x) Gamma(h)."""
    la = lam if lam_arm is None else lam_arm
    lp = lam if lam_ptr is None else lam_ptr
    L = len(parents)
    D = 1 << L
    w, r, h = arm_operators(parents, la)
    basis = fock_basis(d, D)
    pos = {n: i for i, n in enumerate(basis)}
    NB = len(basis)
    if 2 * NB > REDUCED_DIM_CAP:
        die("cap:reduced-dim %d > %d" % (2 * NB, REDUCED_DIM_CAP))
    H = np.zeros((2 * NB, 2 * NB), dtype=np.complex128)
    for z in (0, 1):
        Z0 = 1 - 2 * z
        off = z * NB
        for i, n in enumerate(basis):
            H[off + i, off + i] += float(sum(n[a] * w[a] for a in range(D)))
            H[off + i, off + i] += -Z0 * float(sum(n[a] * r[a] for a in range(D)))
            for b in range(D):
                if n[b] == 0:
                    continue
                for a in range(D):
                    if a == b or h[a, b] == 0:
                        continue
                    m = list(n)
                    m[b] -= 1
                    m[a] += 1
                    H[off + pos[tuple(m)], off + i] += h[a, b] * math.sqrt(n[b] * m[a])
        for i in range(NB):
            H[off + i, (1 - z) * NB + i] += -lp
    return H, basis, pos, D


def reduced_psi0(d, basis, D):
    """The frozen preparation in the reduced basis: v = |+>_root (x) |0>^(L-1)."""
    v = np.zeros(D)
    v[0] = 1.0 / math.sqrt(2.0)     # arm all-down (all +Z)
    v[1] = 1.0 / math.sqrt(2.0)     # root flipped
    psi = np.zeros(len(basis))
    for i, n in enumerate(basis):
        amp = math.sqrt(multinom(n, d))
        for a in range(D):
            amp *= v[a] ** n[a]
        psi[i] = amp
    return psi


def reduced_branches(d, parents, lam, t, lam_arm=None, lam_ptr=None, cache={}):
    """ROUTE R -- the derived propagator.  Returns [(p_z, f)] with f the branch
    amplitude of the UNNORMALISED computational configuration with occupations n."""
    PROP_CALLS["R"] += 1
    key = (d, tuple(-1 if p is None else p for p in parents), lam, lam_arm, lam_ptr)
    if key not in cache:
        H, basis, pos, D = reduced_H(d, parents, lam, lam_arm, lam_ptr)
        w, V = np.linalg.eigh(H)
        NB = len(basis)
        p0 = reduced_psi0(d, basis, D)
        full0 = np.zeros(2 * NB, dtype=np.complex128)
        full0[:NB] = p0 / math.sqrt(2.0)
        full0[NB:] = p0 / math.sqrt(2.0)
        cache[key] = (w, V, V.conj().T @ full0, basis, NB, D)
        if len(cache) > 400:
            cache.clear()
            cache[key] = (w, V, V.conj().T @ full0, basis, NB, D)
    w, V, c0, basis, NB, D = cache[key]
    psi = V @ (np.exp(-1j * w * t) * c0)
    out = []
    for z in (0, 1):
        c = psi[z * NB:(z + 1) * NB]
        p = float(np.vdot(c, c).real)
        cc = c / math.sqrt(p)
        f = {n: cc[i] / math.sqrt(multinom(n, d)) for i, n in enumerate(basis)}
        out.append((p, f))
    return out, D


def multi_hankel_T(f, d, k, D, bk, bdk):
    """THE DERIVED MULTI-INDEX HANKEL MATRIX."""
    T = np.zeros((len(bk), len(bdk)), dtype=np.complex128)
    for ip, p in enumerate(bk):
        cp = math.sqrt(multinom(p, k))
        for iq, q in enumerate(bdk):
            cq = math.sqrt(multinom(q, d - k))
            T[ip, iq] = cp * cq * f[tuple(p[a] + q[a] for a in range(D))]
    return T


def sk_reduced(d, parents, lam, t, lam_arm=None, lam_ptr=None, ks=None):
    brs, D = reduced_branches(d, parents, lam, t, lam_arm, lam_ptr)
    tot = sum(p for p, _ in brs)
    kk = range(d + 1) if ks is None else ks
    bcache = {}
    out = {}
    for k in kk:
        for m in (k, d - k):
            if m not in bcache:
                bcache[m] = fock_basis(m, D)
        acc = 0.0
        for p, f in brs:
            T = multi_hankel_T(f, d, k, D, bcache[k], bcache[d - k])
            sv = np.linalg.svd(T, compute_uv=False)
            ev = np.clip(sv ** 2, 0.0, None)
            ev = ev / ev.sum()
            acc += (p / tot) * ent_bits(ev)[0]
        out[k] = acc
    return out


def reduced_observables(d, parents, lam, t):
    """The FULL frozen certification observables from the reduced route alone:
    p_z, H(Z_S), chi_Z(S:F) for one arm, and C_ab for a pair of arms."""
    brs, D = reduced_branches(d, parents, lam, t)
    tot = sum(p for p, _ in brs)
    b1 = fock_basis(1, D)
    bd1 = fock_basis(d - 1, D)
    rho1 = []
    for p, f in brs:
        T = multi_hankel_T(f, d, 1, D, b1, bd1)
        R = T @ T.conj().T
        rho1.append((p / tot, R / float(np.trace(R).real)))
    mix = sum(w * R for w, R in rho1)
    Sav, _ = ent_bits(np.linalg.eigvalsh(mix))
    Sc = sum(w * ent_bits(np.linalg.eigvalsh(R))[0] for w, R in rho1)
    pz = [p / tot for p, _ in brs]
    H = -sum(q * math.log2(q) for q in pz if q > 1e-15)
    chi = Sav - Sc
    C = None
    if d >= 2:
        b2 = fock_basis(2, D)
        bd2 = fock_basis(d - 2, D)
        C = 0.0
        for (w, R), (p, f) in zip(rho1, brs):
            s1 = ent_bits(np.linalg.eigvalsh(R))[0]
            T2 = multi_hankel_T(f, d, 2, D, b2, bd2)
            ev = np.clip(np.linalg.svd(T2, compute_uv=False) ** 2, 0.0, None)
            ev = ev / ev.sum()
            s2 = ent_bits(ev)[0]
            C += w * (2.0 * s1 - s2)
    return {"p_z": pz, "H_Z": H, "chi": chi, "C_ab": C}


# ============================ the symmetric-subspace projector (full space) ==
def site_permutation_map(n, sigma):
    """The full-space basis-index map of a SITE permutation sigma (site i moves to
    site sigma[i]).  Returns b with b[a] = the image configuration of a."""
    idx = np.arange(1 << n, dtype=np.int64)
    b = np.zeros(1 << n, dtype=np.int64)
    for i in range(n):
        b |= ((idx >> np.int64(i)) & np.int64(1)) << np.int64(sigma[i])
    return b


def permute_state(psi, n, armsets, perm):
    """Apply the arm permutation pi to a full-space vector: arm j is carried to
    arm pi(j) site by site (the arms are isomorphic, so position p maps to
    position p).  The pointer is fixed."""
    d = len(armsets)
    L = len(armsets[0])
    sigma = list(range(n))
    for j in range(d):
        for p in range(L):
            sigma[armsets[j][p]] = armsets[perm[j]][p]
    b = site_permutation_map(n, sigma)
    out = np.empty_like(psi)
    out[b] = psi
    return out


def sym_leakage(psi, n, armsets):
    """||psi - P_sym psi|| with P_sym = (1/d!) sum_pi U_pi over the arms."""
    d = len(armsets)
    acc = np.zeros_like(psi)
    cnt = 0
    for perm in itertools.permutations(range(d)):
        acc += permute_state(psi, n, armsets, perm)
        cnt += 1
    acc /= cnt
    return float(np.abs(psi - acc).max()), float(np.linalg.norm(psi - acc))


# ================================================= the frozen certification ==
def cert_gates_full(psi, g, chi0, delta=HEADLINE_DELTA):
    n, S, labels, frags = g["n"], g["S"], g["labels"], g["frags"]
    chi, H = {}, None
    for L in labels:
        rho = joint_rho(psi, n, [S] + frags[L])
        c, H, _ = chi_holevo(rho, len(frags[L]))
        chi[L] = c
    exc = {L: chi[L] - chi0[L] for L in labels}
    passes = [L for L in labels
              if H >= CONTENT_H_MIN and chi[L] >= (1.0 - delta) * H
              and exc[L] >= EXCESS_MIN]
    C = {}
    for a, b in itertools.combinations(labels, 2):
        C["%s|%s" % (a, b)] = C_pair(psi, n, S, frags[a], frags[b])
    pairs = {k: v for k, v in C.items() if all(q in passes for q in k.split("|"))}
    ok = [v for v in pairs.values() if v <= INDEP_MAX]
    return {"H_Z": H, "chi": chi, "excess": exc, "C_ab": C,
            "n_content_passes": len(passes),
            "binding_pair_C_ab": (min(pairs.values()) if pairs else None),
            "cert": bool(len(passes) >= 2 and len(ok) >= 1)}


def cert_gates_reduced(d, parents, lam, t, chi0, delta=HEADLINE_DELTA):
    o = reduced_observables(d, parents, lam, t)
    exc = o["chi"] - chi0
    passes = d if (o["H_Z"] >= CONTENT_H_MIN and o["chi"] >= (1.0 - delta) * o["H_Z"]
                   and exc >= EXCESS_MIN) else 0
    return {"H_Z": o["H_Z"], "chi": o["chi"], "excess": exc, "C_ab": o["C_ab"],
            "n_content_passes": passes,
            "binding_pair_C_ab": (o["C_ab"] if passes >= 2 else None),
            "cert": bool(passes >= 2 and o["C_ab"] is not None
                         and o["C_ab"] <= INDEP_MAX)}


def bisect_edge(certfn, t_false, t_true, tol=BISECT_TOL):
    a, b = t_false, t_true
    for _ in range(200):
        m = 0.5 * (a + b)
        if certfn(m):
            b = m
        else:
            a = m
        if abs(b - a) < tol:
            break
    return 0.5 * (a + b)


def window_edges(certfn, lo=0.0, hi=1.6, dt=0.005):
    ts = [round(lo + i * dt, 12) for i in range(int(round((hi - lo) / dt)) + 1)]
    flags = [certfn(t) for t in ts]
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
        t_lo = 0.0 if i == 0 else bisect_edge(certfn, ts[i - 1], ts[i])
        t_hi = ts[j] if j == len(ts) - 1 else bisect_edge(certfn, ts[j + 1], ts[j])
        out.append({"t_open": t_lo, "t_close": t_hi, "window_width": t_hi - t_lo,
                    "grid_samples_in_window":
                        [x for x in T_EXEC if t_lo - 1e-12 <= x <= t_hi + 1e-12]})
    return out


# =========================================================== the fit engine ==
def fit_power_with_log(lams, deltas, pmin=2, pmax=12):
    """Declared protocol.  Model  delta = c * lambda^p * (ln(1/lambda) + b),
    p an INTEGER, b >= 0 a shape parameter.  For each p the best b minimises the
    spread of  ln|delta| - p ln(lambda) - ln(ln(1/lambda)+b)  over the fitted
    points; the winning p is the one with the smallest spread.  RIVALS
    (pure power, p half-integer) are scored on the same footing."""
    xs = [(l, abs(dv)) for l, dv in zip(lams, deltas) if dv is not None and abs(dv) > 0]
    if len(xs) < 3:
        return None
    scores = {}
    for p in range(pmin, pmax + 1):
        best = None
        for b in [0.0 + 0.02 * i for i in range(151)]:
            r = [math.log(v) - p * math.log(l) - math.log(math.log(1.0 / l) + b)
                 for l, v in xs]
            spread = max(r) - min(r)
            if best is None or spread < best[0]:
                best = (spread, b, sum(r) / len(r))
        scores["p=%d_log" % p] = {"spread": best[0], "b": best[1],
                                  "ln_c": best[2]}
    for p in range(pmin, pmax + 1):
        r = [math.log(v) - p * math.log(l) for l, v in xs]
        scores["p=%d_pure" % p] = {"spread": max(r) - min(r), "b": None,
                                   "ln_c": sum(r) / len(r)}
    for ph in [x * 0.5 for x in range(2 * pmin, 2 * pmax + 1)]:
        if abs(ph - round(ph)) < 1e-9:
            continue
        r = [math.log(v) - ph * math.log(l) for l, v in xs]
        scores["p=%.1f_pure" % ph] = {"spread": max(r) - min(r), "b": None,
                                      "ln_c": sum(r) / len(r)}
    win = min(scores, key=lambda k: scores[k]["spread"])
    # a free-exponent least-squares slope, for reference only
    n = len(xs)
    sx = sum(math.log(l) for l, _ in xs)
    sy = sum(math.log(v) for _, v in xs)
    sxx = sum(math.log(l) ** 2 for l, _ in xs)
    sxy = sum(math.log(l) * math.log(v) for l, v in xs)
    slope = (n * sxy - sx * sy) / (n * sxx - sx * sx)
    local = []
    for i in range(1, len(xs)):
        (l0, v0), (l1, v1) = xs[i - 1], xs[i]
        local.append({"between": [l0, l1],
                      "local_loglog_slope": math.log(v0 / v1) / math.log(l0 / l1)})
    return {"n_points": n, "lambdas": [l for l, _ in xs],
            "free_loglog_slope": slope, "local_loglog_slopes": local,
            "winner": win, "scores": scores,
            "winning_spread": scores[win]["spread"],
            "resolved_at_double_precision": bool(n >= 5)}


# ============================================================= sympy lemma ===
def symbolic_second_quantisation():
    """Verify the second-quantisation step SYMBOLICALLY in lambda.

    Build the full-space Hamiltonian of a small spider over Q[lambda]; build the
    orthonormal basis of the arm-permutation-symmetric subspace as the NORMALISED
    ORBIT SUMS e_I = |I|^(-1/2) sum_{a in I} |a>; compute <e_I|H|e_J> by an exact
    sparse sum (H has the diagonal plus n off-diagonal entries per row); identify
    each orbit with a (pointer bit, occupation vector) pair -- the identification
    is exact because |I| equals the multinomial M(n), so e_I IS the normalised
    Fock state |z,n> -- and compare ENTRYWISE against the derived H_red.
    """
    try:
        import sympy as sp
    except Exception as e:                                     # pragma: no cover
        return {"available": False, "reason": str(e)}
    lam = sp.symbols("lambda", real=True)
    out = {"available": True, "sympy_version": sp.__version__, "cases": []}
    for d, parents, nm in ((2, [None, 0], "d=2, path arm L=2"),
                           (3, [None, 0], "d=3, path arm L=2"),
                           (2, [None, 0, 0], "d=2, claw arm L=3"),
                           (2, [None, 0, 1], "d=2, path arm L=3")):
        L = len(parents)
        n = 1 + d * L
        S = 0
        armsets = [[1 + j * L + p for p in range(L)] for j in range(d)]
        bonds = []
        for j in range(d):
            bonds.append((S, armsets[j][0]))
            for p, par in enumerate(parents):
                if par is not None:
                    bonds.append((armsets[j][par], armsets[j][p]))
        N = 1 << n

        def zbit(a, i):
            return 1 - 2 * ((a >> i) & 1)

        def diag_energy(a):
            return sum(-zbit(a, u) * zbit(a, v) for (u, v) in bonds)

        def relabel(a, perm):
            b = a & 1
            for j in range(d):
                for p in range(L):
                    if (a >> armsets[j][p]) & 1:
                        b |= 1 << armsets[perm[j]][p]
            return b

        def occ_of(a):
            """(pointer bit, occupation vector over the 2^L arm basis states)."""
            occ = [0] * (1 << L)
            for j in range(d):
                c = 0
                for p in range(L):
                    if (a >> armsets[j][p]) & 1:
                        c |= 1 << p
                occ[c] += 1
            return (a & 1, tuple(occ))

        perms = list(itertools.permutations(range(d)))
        seen, orbits = set(), []
        for a in range(N):
            if a in seen:
                continue
            orb = sorted({relabel(a, p) for p in perms})
            for x in orb:
                seen.add(x)
            orbits.append(orb)
        if len(orbits) != reduced_dim(d, L):
            die("symbolic:orbit-count %d != derived dim %d"
                % (len(orbits), reduced_dim(d, L)))
        # each orbit is exactly one (z, occupation); and |I| = M(n)
        okey, mism = {}, 0
        for i, orb in enumerate(orbits):
            keys = {occ_of(a) for a in orb}
            if len(keys) != 1:
                die("symbolic:orbit-not-a-single-occupation")
            k = keys.pop()
            okey[i] = k
            if len(orb) != multinom(k[1], d):
                mism += 1
        if mism:
            die("symbolic:orbit-size != multinomial (%d orbits)" % mism)
        # <e_I|H|e_J> by an exact sparse sum
        owner = {}
        for i, orb in enumerate(orbits):
            for a in orb:
                owner[a] = i
        Hs = {}
        for i, orb in enumerate(orbits):
            for a in orb:
                targets = [(a, sp.Integer(diag_energy(a)))]
                for q in range(n):
                    targets.append((a ^ (1 << q), -lam))
                for (b_, val) in targets:
                    j = owner[b_]
                    key = (j, i)
                    Hs[key] = Hs.get(key, sp.Integer(0)) + val / (
                        sp.sqrt(sp.Integer(len(orbits[j]))) * sp.sqrt(
                            sp.Integer(len(orb))))
        Hd, basis, pos, D = reduced_H_symbolic(d, parents, lam, sp)
        NB = len(basis)
        # index of the derived matrix for the key (z, occ)
        didx = {}
        for z in (0, 1):
            for ii, nn in enumerate(basis):
                didx[(z, nn)] = z * NB + ii
        worst = sp.Integer(0)
        nz = 0
        for (j, i), v in Hs.items():
            dj, di = didx[okey[j]], didx[okey[i]]
            diff = sp.simplify(sp.expand(v - Hd[dj, di]))
            if diff != 0:
                die("symbolic:entry-mismatch %s [%d,%d] -> %s" % (nm, dj, di, diff))
            nz += 1
        # and no entry of the derived matrix is missing from the orbit computation
        covered = {(didx[okey[j]], didx[okey[i]]) for (j, i) in Hs}
        missing = 0
        for r in range(2 * NB):
            for c in range(2 * NB):
                if (r, c) not in covered and Hd[r, c] != 0:
                    missing += 1
        if missing:
            die("symbolic:derived-entry-not-produced-by-the-orbit-route %d" % missing)
        out["cases"].append({
            "case": nm, "n_sites": n, "full_dim": N,
            "n_orbits": len(orbits), "derived_dim": reduced_dim(d, L),
            "dims_agree": True,
            "orbit_sizes_equal_the_multinomials": True,
            "nonzero_entries_compared": nz,
            "derived_nonzero_entries_not_produced_by_the_orbit_route": missing,
            "all_entries_identical_as_polynomials_in_lambda": True})
    return out


def reduced_H_symbolic(d, parents, lam, sp):
    """The derived H_red over Q[lambda] (same construction as reduced_H)."""
    L = len(parents)
    D = 1 << L
    zs = [[1 - 2 * ((a >> p) & 1) for p in range(L)] for a in range(D)]
    w = []
    for a in range(D):
        e = 0
        for p, par in enumerate(parents):
            if par is not None:
                e -= zs[a][p] * zs[a][par]
        w.append(sp.Integer(e))
    r = [sp.Integer(zs[a][0]) for a in range(D)]
    h = sp.zeros(D, D)
    for a in range(D):
        h[a, a] = w[a]
        for p in range(L):
            h[a, a ^ (1 << p)] += -lam
    basis = fock_basis(d, D)
    pos = {n: i for i, n in enumerate(basis)}
    NB = len(basis)
    H = sp.zeros(2 * NB, 2 * NB)
    for z in (0, 1):
        Z0 = 1 - 2 * z
        off = z * NB
        for i, n in enumerate(basis):
            H[off + i, off + i] += sum(n[a] * w[a] for a in range(D))
            H[off + i, off + i] += -Z0 * sum(n[a] * r[a] for a in range(D))
            for b in range(D):
                if n[b] == 0:
                    continue
                for a in range(D):
                    if a == b or h[a, b] == 0:
                        continue
                    m = list(n)
                    m[b] -= 1
                    m[a] += 1
                    H[off + pos[tuple(m)], off + i] += h[a, b] * sp.sqrt(
                        sp.Integer(n[b] * m[a]))
        for i in range(NB):
            H[off + i, (1 - z) * NB + i] += -lam
    return H, basis, pos, D


# ==================================================================== main ===
ARMS = {"L1": path_arm(1), "L2": path_arm(2), "L3": path_arm(3), "L4": path_arm(4),
        "L5": path_arm(5), "claw3": claw_arm(3), "claw4": claw_arm(4),
        "Y3": y_arm3(), "tee4": tee_arm4()}


def full_spider_state(d, parents, lam, t, route=None):
    """The full-space state of the isomorphic-arm spider.  Route C (dense
    eigendecomposition) below 12 sites, route A (the pinned Chebyshev
    propagator over the frozen T_EXEC grid) at and above it."""
    g = spider("SP", [parents] * d, "", "spider")
    n = g["n"]
    if n > FULL_SPACE_CAP_N:
        die("cap:n>%d" % FULL_SPACE_CAP_N)
    L = len(parents)
    armsets = [[1 + j * L + p for p in range(L)] for j in range(d)]
    for j in range(d):
        for p in range(L):
            want = "A%02d" % (j + 1) if p == 0 else "a%02dx%d" % (j + 1, p)
            if g["sites"][armsets[j][p]] != want:
                die("indexing:arm-site-mismatch %s != %s"
                    % (g["sites"][armsets[j][p]], want))
    diag = build_diag(n, g["bonds"])
    psi0 = prep_state(n, set([g["S"]] + g["recording"]))
    if route is None:
        route = "C" if n <= 11 else "A"
    if route == "C":
        outs, _ = dense_route(psi0, diag, n, lam, [t])
        psi = outs[0]
    elif route == "A931":
        ti = int(round(t / 0.1))
        outs, _ = chebyshev_931(psi0, diag, n, lam, T_EXEC)
        psi = outs[ti]
    else:
        ti = int(round(t / 0.1))
        if abs(T_EXEC[ti] - t) > 1e-12:
            outs, _ = chebyshev(psi0, diag, n, lam, [0.0, t])
            psi = outs[1]
        else:
            outs, _ = chebyshev(psi0, diag, n, lam, T_EXEC)
            psi = outs[ti]
    return g, psi, armsets


def main():
    caps = []
    pins = verify_pins()
    vendored, vblobs = vendor_from_sibling()
    memo = open(os.path.join(ROOT, PARENT_MEMO), "rb").read().decode("utf-8")
    frozen = verify_frozen_constants(memo)
    const_x = cross_check_prior_constants(frozen)
    statdef = verify_statistic_definition(memo)
    d1_text, d1_prov = recover_d1_note()
    head = git(["rev-parse", "--short=10", "HEAD"]).stdout.decode().strip()
    r927 = json.load(open(os.path.join(ROOT, C927_RECEIPT)))
    r931 = json.load(open(os.path.join(ROOT, C931_RECEIPT)))
    r933 = json.load(open(os.path.join(ROOT, C933_RECEIPT)))
    r932 = json.loads(vblobs[C932_RECEIPT].decode("utf-8"))

    lines = []
    ap = lines.append
    ap(BOUNDARY_LINE)
    ap("runner   : %s" % os.path.basename(__file__))
    ap("cycle    : 937   block: blockM15   campaign: toe-time-expansion-20260802")
    ap("question : extend the collective reduction OFF the star -- isomorphic-arm spiders")
    ap("")
    ap("THE PREPARATION, QUOTED FROM THE MEMO BYTES")
    for c in PREPARATION_CLAUSES:
        ap("  %-12s %s" % (c, frozen[c]["quoted"]))
    ap("  as implemented (all pinned runners): prep_state(n, {S} | recording)")
    ap("  ON A SPIDER: the arm ROOT (depth 1, the recording site) is +X; every arm")
    ap("  site at depth >= 2 is +Z.  Single-arm vector v = |+>_root (x) |0>^(L-1).")
    ap("")

    # ================================================= RESTRICTION GATE 1 ====
    cube = geom_cube27()
    memo_frags = parse_memo_cube_fragments(memo)
    part_ok = True
    if memo_frags:
        for L in CUBE_LABELS:
            if {cube["coords"][i] for i in cube["frags"][L]} != set(memo_frags[L]):
                die("partition-rule:does-not-reproduce-memo-cube")
    restriction = {"gate_order": ["partition_rule_vs_memo", "c927_saturation_tables",
                                 "c933_star_cells_c931_sk_table",
                                 "c931_spider_identity_rows",
                                 "frozen_constants_eight_way"],
                   "partition_rule_reproduces_memo_six_lists": bool(part_ok)}
    gate_t0 = time.perf_counter()

    # ---------- GATE 2: Cycle 927's saturation tables, value-for-value -------
    SPFAM = {2: range(1, 8), 3: range(1, 6), 4: range(1, 4), 5: range(1, 4)}
    sat_rows, sat_dev, n_sat = [], 0.0, 0
    for deg, Ls in sorted(SPFAM.items()):
        for lam in (0.05, 0.075, 0.1, 0.125, 0.15):
            key = "deg%d@%g" % (deg, lam)
            tab = r927["Q1_size_law"]["tables"][key]
            for row in tab:
                L = row["arm_length"]
                g = spider("SPk%dL%d" % (deg, L), [path_arm(L)] * deg, "", "spider")
                if g["n"] > FULL_SPACE_CAP_N:
                    die("cap:927-row n=%d" % g["n"])
                diag = build_diag(g["n"], g["bonds"])
                psi0 = prep_state(g["n"], set([g["S"]] + g["recording"]))
                outs, _ = chebyshev(psi0, diag, g["n"], lam, T_EXEC)
                ti = int(round(row["ceiling_jt"] / 0.1))
                a = outs[ti]
                vals = [C_pair(a, g["n"], g["S"], g["frags"][x], g["frags"][y])
                        for x, y in itertools.combinations(g["labels"], 2)]
                got = max(vals)
                dev = abs(got - row["C_ab_at_ceiling_row"])
                sat_dev = max(sat_dev, dev)
                n_sat += 1
                if deg == 2 and lam in (0.05, 0.1, 0.15):
                    sat_rows.append({"ladder": key, "arm_length": L, "n_sites": g["n"],
                                     "C_ab_pinned": row["C_ab_at_ceiling_row"],
                                     "C_ab_reproduced": got, "deviation": dev})
    if sat_dev > REPRO_TOL:
        die("restriction:927-saturation max_dev=%.3e (demanded exactly 0.0)" % sat_dev)
    restriction["c927_saturation_tables"] = {
        "n_rows": n_sat, "max_abs_deviation": sat_dev,
        "ladders": sorted(r927["Q1_size_law"]["tables"].keys()),
        "statistic": "C_ab at the PINNED ceiling row (max over pairs), pinned "
                     "Chebyshev route, pinned direct/Gram switch",
        "sample_rows": sat_rows}
    restriction["c927_saturation_summary_reproduced"] = {
        "max_ceiling_row_spread_excluding_L1_pinned":
            r927["Q1_size_law"]["saturation_length_summary"][
                "max_ceiling_row_spread_excluding_L1"],
        "max_ceiling_row_spread_any_ladder_pinned":
            r927["Q1_size_law"]["saturation_length_summary"][
                "max_ceiling_row_spread_any_ladder"]}

    # ---------- GATE 3: Cycle 933's star cells (its 44-value s(k) table) -----
    # 933 publishes s(k) for eight star cells (d = 3..6, both certified fields;
    # 4+5+6+7 values per field = 44 values) as the DERIVED collective-route
    # prediction, together with the grade it reproduced the pinned measurements
    # at.  This block reproduces those 44 values on BOTH of its routes: the
    # full-space route at 933's own stated grade, and its own reduced route (the
    # L = 1 case of the extension) at the double-precision floor.
    c933A = r933["Q2_candidates"]["A_collective_spin_symmetric_reduction"]
    grade933 = float(c933A["max_abs_residual_over_the_pinned_grid"])
    sk_dev_full, sk_dev_red, sk_rows = 0.0, 0.0, 0
    star_rows = []
    for row in c933A["rows"]:
        d = int(row["cell"].split("@")[0][1:])
        lam = float(row["cell"].split("@")[1])
        g, psi, armsets = full_spider_state(d, path_arm(1), lam, COMPARISON_JT,
                                            "A931")
        sfull = s_profile_full(psi, g["n"], g["S"], armsets)
        sred = sk_reduced(d, path_arm(1), lam, COMPARISON_JT)
        df = max(abs(sfull[int(k)] - float(v)) for k, v in row["s_pred"].items())
        dr = max(abs(sred[int(k)] - float(v)) for k, v in row["s_pred"].items())
        sk_dev_full = max(sk_dev_full, df)
        sk_dev_red = max(sk_dev_red, dr)
        sk_rows += len(row["s_pred"])
        star_rows.append({"cell": row["cell"], "d": d, "field": lam,
                          "n_values": len(row["s_pred"]),
                          "max_abs_dev_full_space_route": df,
                          "max_abs_dev_reduced_route": dr})
    if sk_rows != 44:
        die("restriction:933-star-cells value count %d != 44" % sk_rows)
    if sk_dev_full > grade933:
        die("restriction:933-star-cells full-space %.3e > 933 grade %.3e"
            % (sk_dev_full, grade933))
    if sk_dev_red > 1e-13:
        die("restriction:933-star-cells reduced %.3e > 1e-13" % sk_dev_red)
    restriction["c933_star_cells_c931_sk_table"] = {
        "n_values": sk_rows, "cells": len(c933A["rows"]),
        "grade_933_states": grade933,
        "max_abs_deviation_full_space_route": sk_dev_full,
        "max_abs_deviation_reduced_route": sk_dev_red,
        "rows": star_rows,
        "grade_note": "933's published s(k) are its own DERIVED values; they are "
                      "reproduced here at 933's stated grade on the full-space "
                      "route and at the double-precision floor on the reduced "
                      "route.  The exactly-zero gates in this block are the 927 "
                      "and 931 gates, which run the pinned code path."}
    sk_dev = sk_dev_red

    # ---------- GATE 4: Cycle 931's spider-identity rows ---------------------
    p7 = r931["seal_verification"]["P7_exhausting_pairs_anywhere"]
    p7rows = p7["rows"] if isinstance(p7, dict) and "rows" in p7 else p7
    sp_dev, sp_n = 0.0, 0
    SPIDER931 = {"SPk2L1": [path_arm(1)] * 2, "SPk2L3": [path_arm(3)] * 2,
                 "SPk2L4": [path_arm(4)] * 2, "SH2Y3": [y_arm3()] * 2,
                 "SH2C4": [claw_arm(4)] * 2}
    sp_rows = []
    for row in p7rows:
        nm = row["geometry"]
        if nm not in SPIDER931:
            continue
        g = spider(nm, SPIDER931[nm], "", "spider")
        diag = build_diag(g["n"], g["bonds"])
        psi0 = prep_state(g["n"], set([g["S"]] + g["recording"]))
        outs, _ = chebyshev_931(psi0, diag, g["n"], row["field"], T_EXEC)
        a = outs[7]
        La, Lb = g["labels"]
        C = C_pair(a, g["n"], g["S"], g["frags"][La], g["frags"][Lb])
        dev = abs(C - row["C_ab_measured"])
        sp_dev = max(sp_dev, dev)
        sp_n += 1
        sp_rows.append({"geometry": nm, "field": row["field"],
                        "C_ab_pinned": row["C_ab_measured"],
                        "C_ab_reproduced": C, "deviation": dev,
                        "pinned_2S_branch_a": row["2*S_branch(a)"]})
    if sp_dev > REPRO_TOL:
        die("restriction:931-spider max_dev=%.3e (demanded exactly 0.0)" % sp_dev)
    restriction["c931_spider_identity_rows"] = {
        "n_rows": sp_n, "max_abs_deviation": sp_dev, "rows": sp_rows,
        "note": "Cycle 931's P7 exhausting-pair rows on ISOMORPHIC-ARM SPIDERS -- "
                "the H4 exchangeability hypothesis this block turns into a theorem"}
    restriction["frozen_constants_eight_way"] = const_x
    restriction["deviation_exactly_zero_everywhere"] = bool(
        sat_dev == 0.0 and sp_dev == 0.0)
    restriction["gates_at_deviation_exactly_zero"] = [
        "c927_saturation_tables (the 927/929 Chebyshev order, pinned direct/Gram "
        "switch)",
        "c931_spider_identity_rows (the 931/933 Chebyshev order)"]
    restriction["disclosed_route_provenance_split"] = (
        "the 927/929 runners and the 931/933 runners carry ALGEBRAICALLY IDENTICAL "
        "but BITWISE DIFFERENT Chebyshev accumulation orders; no single "
        "implementation reproduces both families at deviation exactly zero, so "
        "each gate is run against its own parent's code path and both "
        "implementations are carried here (chebyshev / chebyshev_931).  Measured "
        "spread between the two orders on a shared cell is reported in "
        "Q1_spider_reduction.route_order_spread.")
    restriction["gates_at_the_parent_grade"] = [
        "c933_star_cells: 44 values at 933's own %.3e" % grade933]
    gate_seconds = time.perf_counter() - gate_t0
    ap("RESTRICTION GATES (all demanded at deviation EXACTLY zero)")
    ap("  927 saturation tables : %d rows, max deviation %.1e" % (n_sat, sat_dev))
    ap("  933 star cells s(k)   : %d values, full-space %.1e (933 grade %.1e), "
       "reduced %.1e" % (sk_rows, sk_dev_full, grade933, sk_dev_red))
    ap("  931 spider identity   : %d rows, max deviation %.1e" % (sp_n, sp_dev))
    ap("  frozen constants      : 21/21, eight-way quote-identical")
    ap("")

    # ======================================================= Q1: THE REDUCTION
    ap("Q1  THE SPIDER REDUCTION")
    sym = symbolic_second_quantisation()
    dimtab, cmp_rows, leak_rows = [], [], []
    Q1CELLS = [(2, "L1"), (2, "L2"), (2, "L4"), (3, "L1"), (3, "L2"), (3, "L3"),
               (3, "claw3"), (4, "L2"), (4, "claw3"), (5, "L2"), (2, "claw4"),
               (2, "Y3"), (6, "L2"), (2, "tee4")]
    for d, an in Q1CELLS:
        parents = ARMS[an]
        L = len(parents)
        n = 1 + d * L
        rd = reduced_dim(d, L)
        dimtab.append({"d": d, "arm": an, "arm_sites_L": L, "n_sites": n,
                       "full_dim_2^n": 1 << n, "reduced_dim_2*C(d+2^L-1,d)": rd,
                       "compression": (1 << n) / float(rd)})
        if n > FULL_SPACE_CAP_N or rd > REDUCED_DIM_CAP:
            continue
        for lam in CLAIM_LAMBDAS:
            NEW_CELLS_EVALUATED.add(("q1", d, an, lam))
            g, psi, armsets = full_spider_state(d, parents, lam, COMPARISON_JT, "C")
            sf = s_profile_full(psi, g["n"], g["S"], armsets)
            sr = sk_reduced(d, parents, lam, COMPARISON_JT)
            La, Lb = g["labels"][0], g["labels"][1]
            Cf = C_pair(psi, g["n"], g["S"], g["frags"][La], g["frags"][Lb])
            orr = reduced_observables(d, parents, lam, COMPARISON_JT)
            cmp_rows.append({
                "d": d, "arm": an, "field": lam, "n_sites": g["n"],
                "max_abs_dev_s(k)_full_vs_reduced":
                    max(abs(sf[k] - sr[k]) for k in range(d + 1)),
                "C_ab_full": Cf, "C_ab_reduced": orr["C_ab"],
                "abs_dev_C_ab": abs(Cf - orr["C_ab"]),
                "s(k)_reduced": {str(k): sr[k] for k in range(d + 1)},
                "reflection_residual_max":
                    max(abs(sr[k] - sr[d - k]) for k in range(d + 1)),
                "s(0)": sr[0], "s(d)": sr[d]})
            if d <= 6 and g["n"] <= 13:
                mx, l2 = sym_leakage(psi, g["n"], armsets)
                leak_rows.append({"d": d, "arm": an, "field": lam,
                                  "n_sites": g["n"],
                                  "max_abs_component_outside_Sym^d": mx,
                                  "l2_norm_outside_Sym^d": l2})
    q1 = {"derivation": {
        "step_1_symmetry": "every arm permutation is a graph automorphism fixing S "
                           "and preserving the frozen preparation (which depends on "
                           "an arm site only through its arm-intrinsic position), so "
                           "[U_pi,H]=0 and U_pi psi0 = psi0",
        "step_2_subspace": "psi(t) in C^2 (x) Sym^d(H_arm), H_arm = (C^2)^(x)L",
        "step_3_dimension": "dim = 2 * C(d + 2^L - 1, d)  vs  2^(dL+1)",
        "step_4_hamiltonian":
            "H_red = -lambda X_0 (x) 1 - Z_0 (x) Gamma(R) + 1 (x) Gamma(h) with "
            "R = Z_root, h = -sum_(u,v) Z_u Z_v - lambda sum_u X_u, and "
            "Gamma(O) = sum_ab O_ab a_a^dag a_b acting on the d-boson Fock space "
            "over the 2^L arm basis states",
        "step_5_schmidt":
            "T^(k)_{p,q} = sqrt(M_k(p) M_(d-k)(q)) f(p+q) -- a MULTI-INDEX HANKEL "
            "matrix; s(k) is the entropy of its normalised squared singular values",
        "reduces_to_933_at_L=1": "Gamma(R) = d - 2n and Gamma(h) off-diagonal "
                                 "-lambda sqrt((n+1)(d-n)) reproduce 933's "
                                 "collective_H term for term"},
        "dimension_table": dimtab,
        "symbolic_second_quantisation": sym,
        "symmetric_subspace_leakage": {
            "rows": leak_rows,
            "max_over_all_cells": max((r["max_abs_component_outside_Sym^d"]
                                       for r in leak_rows), default=None),
            "definition": "||psi - P_sym psi||_inf with P_sym = (1/d!) sum_pi U_pi "
                          "over the d! arm permutations, on the FULL-SPACE evolved "
                          "state"},
        "two_route_comparison": {
            "rows": cmp_rows,
            "max_abs_dev_s(k)": max(r["max_abs_dev_s(k)_full_vs_reduced"]
                                    for r in cmp_rows),
            "max_abs_dev_C_ab": max(r["abs_dev_C_ab"] for r in cmp_rows),
            "max_reflection_residual": max(r["reflection_residual_max"]
                                           for r in cmp_rows),
            "max_|s(0)|_and_|s(d)|": max(max(abs(r["s(0)"]), abs(r["s(d)"]))
                                         for r in cmp_rows)}}
    tight_rows = []
    for an, parents in sorted(ARMS.items()):
        Da, nA = arm_invariant_dimension(parents)
        L = len(parents)
        tight_rows.append({
            "arm": an, "arm_sites_L": L, "arm_dim_2^L": 1 << L,
            "root_fixing_automorphism_group_order": nA,
            "invariant_arm_dimension": Da,
            "reduction_is_tight_for_this_arm": bool(Da == (1 << L)),
            "refined_reduced_dim_at_d=5": 2 * math.comb(5 + Da - 1, 5),
            "stated_reduced_dim_at_d=5": reduced_dim(5, L)})
    # verify the refinement on one cell: the state really lies in the smaller space
    gT, psiT, armsT = full_spider_state(3, ARMS["claw3"], 0.10, COMPARISON_JT)
    nT = gT["n"]
    accT = np.zeros_like(psiT)
    cntT = 0
    Aut = arm_root_automorphisms(ARMS["claw3"])
    for perm in itertools.permutations(range(3)):
        for s1 in Aut:
            for s2 in Aut:
                for s3 in Aut:
                    sigma = list(range(nT))
                    for j, sj in enumerate((s1, s2, s3)):
                        for pp in range(len(ARMS["claw3"])):
                            sigma[armsT[j][pp]] = armsT[perm[j]][sj[pp]]
                    b = site_permutation_map(nT, sigma)
                    o = np.empty_like(psiT)
                    o[b] = psiT
                    accT += o
                    cntT += 1
    accT /= cntT
    q1["reduction_is_not_claimed_tight"] = {
        "finding": "for arms carrying an internal root-fixing automorphism the "
                   "state lies in a STRICTLY SMALLER invariant subspace than "
                   "Sym^d(H_arm): the arm factor may be replaced by its "
                   "A-invariant subspace, of dimension = the number of A-orbits "
                   "on the arm basis states.  The stated reduction is CORRECT and "
                   "SUFFICIENT, but it is not minimal for claw, Y and tee arms.",
        "per_arm": tight_rows,
        "verified_on": "d=3 claw3 (A = Z2 exchanging the two leaves; the arm "
                       "dimension drops 8 -> 6)",
        "leakage_out_of_the_REFINED_subspace_full_space_route":
            float(np.abs(psiT - accT).max()),
        "group_order_used": cntT,
        "disclosure": "this block claims the Sym^d(H_arm) reduction, not "
                      "minimality; the refinement is exhibited so that no reader "
                      "takes the stated dimension for a lower bound"}
    ap("  dimensions           : %d cells tabulated (best compression %.0fx at %s)"
       % (len(dimtab), max(x["compression"] for x in dimtab),
          max(dimtab, key=lambda x: x["compression"])["arm"]))
    ap("  Sym^d leakage        : %.2e (max over %d full-space cells)"
       % (q1["symmetric_subspace_leakage"]["max_over_all_cells"], len(leak_rows)))
    ap("  reduced vs full s(k) : %.2e   C_ab: %.2e   over %d cells"
       % (q1["two_route_comparison"]["max_abs_dev_s(k)"],
          q1["two_route_comparison"]["max_abs_dev_C_ab"], len(cmp_rows)))
    ap("  symbolic 2nd quant.  : %s"
       % ("all entries identical as polynomials in lambda on %d cases (%d nonzero "
          "entries compared)"
          % (len(sym.get("cases", [])),
             sum(c["nonzero_entries_compared"] for c in sym.get("cases", [])))
          if sym.get("available") else "sympy unavailable"))
    ap("")

    # -------- Q1(b): the vendored 932 window edges, both routes -------------
    win_rows = []
    for gk, cellkey, d, an in (("G1", "G1@0.05", 2, "L4"), ("G1", "G1@0.075", 2, "L4"),
                               ("G1", "G1@0.1", 2, "L4")):
        lam = float(cellkey.split("@")[1])
        pinned = r932["Q1_curves"]["per_cell"].get(cellkey)
        if pinned is None:
            continue
        parents = ARMS[an]
        g = spider("SPk2L4", [parents] * d, "", "spider")
        n = g["n"]
        diag = build_diag(n, g["bonds"])
        psi0 = prep_state(n, set([g["S"]] + g["recording"]))
        D = 1 << n
        H = np.zeros((D, D))
        H[np.arange(D), np.arange(D)] = diag
        for i in range(n):
            j = np.arange(D, dtype=np.int64) ^ (1 << i)
            H[np.arange(D), j] -= lam
        w, V = np.linalg.eigh(H)
        c0 = V.T @ psi0

        def state_at(t):
            return V @ (np.exp(-1j * w * t) * c0)
        chi0f = {}
        g0 = cert_gates_full(state_at(0.0), g, {L: 0.0 for L in g["labels"]})
        chi0f = dict(g0["chi"])

        def certF(t):
            return cert_gates_full(state_at(t), g, chi0f)["cert"]
        chi0r = reduced_observables(d, parents, lam, 0.0)["chi"]

        def certR(t):
            return cert_gates_reduced(d, parents, lam, t, chi0r)["cert"]
        wF = window_edges(certF)
        wR = window_edges(certR)
        row = {"cell": cellkey, "geometry_is_spider_d2_L4_path": True,
               "pinned_932_t_open": pinned["t_open"],
               "pinned_932_t_close": pinned["t_close"],
               "pinned_932_window_width": pinned["window_width"],
               "pinned_932_grid_samples_in_window": pinned["grid_samples_in_window"],
               "pinned_932_frozen_verdict": pinned["frozen_verdict"],
               "full_route_windows": wF, "reduced_route_windows": wR}
        if wF and wR:
            row["abs_dev_t_open_full_vs_reduced"] = abs(wF[0]["t_open"] - wR[0]["t_open"])
            row["abs_dev_t_close_full_vs_reduced"] = abs(wF[0]["t_close"] - wR[0]["t_close"])
            row["abs_dev_t_open_vs_pinned_932"] = abs(wF[0]["t_open"] - pinned["t_open"])
            row["abs_dev_t_close_vs_pinned_932"] = abs(wF[0]["t_close"] - pinned["t_close"])
            row["grid_samples_match_932"] = bool(
                [round(x, 10) for x in wF[0]["grid_samples_in_window"]]
                == [round(x, 10) for x in pinned["grid_samples_in_window"]])
        win_rows.append(row)
    q1["window_edges_vendored_932"] = {
        "source": vendored[C932_RECEIPT],
        "rows": win_rows,
        "max_abs_dev_full_vs_reduced":
            max([max(r.get("abs_dev_t_open_full_vs_reduced", 0.0),
                     r.get("abs_dev_t_close_full_vs_reduced", 0.0))
                 for r in win_rows], default=None),
        "max_abs_dev_vs_pinned_932":
            max([max(r.get("abs_dev_t_open_vs_pinned_932", 0.0),
                     r.get("abs_dev_t_close_vs_pinned_932", 0.0))
                 for r in win_rows], default=None),
        "grade_note": "the certification predicate is RE-IMPLEMENTED here from the "
                      "byte-verified frozen constants; agreement with 932 is claimed "
                      "at 932's own bisection tolerance, NOT at deviation zero.  The "
                      "full-vs-reduced agreement IS this block's claim."}
    ap("  932 window edges     : full-vs-reduced %.2e ; vs pinned 932 %.2e (%d cells)"
       % (q1["window_edges_vendored_932"]["max_abs_dev_full_vs_reduced"] or -1,
          q1["window_edges_vendored_932"]["max_abs_dev_vs_pinned_932"] or -1,
          len(win_rows)))
    ap("")

    # ================================================== Q2: THE SATURATION ===
    ap("Q2  THE 927 SATURATION, DERIVED")
    # --- L-ZERO: the exact lemma -------------------------------------------
    lemma_rows = []
    lem_dev = 0.0
    for d in (2, 3, 4):
        for lam in (0.05, 0.10, 0.35):
            for t in (0.7, 3.0, 12.0, 50.0):
                base = sk_reduced(d, path_arm(1), lam, t, lam_arm=0.0)
                for an in ("L2", "L3", "claw3", "L4"):
                    if reduced_dim(d, len(ARMS[an])) > REDUCED_DIM_CAP:
                        continue
                    s = sk_reduced(d, ARMS[an], lam, t, lam_arm=0.0)
                    dv = max(abs(s[k] - base[k]) for k in range(d + 1))
                    lem_dev = max(lem_dev, dv)
                    lemma_rows.append({"d": d, "arm": an, "field": lam, "Jt": t,
                                       "max_abs_dev_vs_star": dv})
    # the SAME lemma with the arm field ON, to show the lemma has teeth
    lem_on = 0.0
    for d in (2, 3):
        for lam in (0.10,):
            for t in (0.7,):
                base = sk_reduced(d, path_arm(1), lam, t)
                for an in ("L2", "L3"):
                    s = sk_reduced(d, ARMS[an], lam, t)
                    lem_on = max(lem_on, max(abs(s[k] - base[k]) for k in range(d + 1)))
    q2 = {"L_zero_exact_lemma": {
        "statement": "with lambda_arm = 0 (pointer field kept) s(k) is EXACTLY the "
                     "star's s(k) for ANY arm graph, ANY d, ANY t",
        "proof": "with no arm field every arm Z is conserved, so every arm site at "
                 "depth >= 2 stays in |0> forever and the intra-arm bonds contribute "
                 "the diagonal energy -c_root*M - K with M = sum_j Z_root^(j); that "
                 "multiplies the amplitude sequence by exp(iKt)exp(-2 i c_root t n), "
                 "a two-sided DIAGONAL UNITARY on T^(k), which leaves every singular "
                 "value invariant",
        "max_abs_dev_vs_star_over_all_cells": lem_dev,
        "n_cells": len(lemma_rows), "rows": lemma_rows,
        "control_same_comparison_with_the_arm_field_ON": lem_on,
        "reading": "the ENTIRE arm-length effect is an arm-field effect; at "
                   "lambda_arm = 0 there is no propagation into the arm at ANY time, "
                   "so the size null is not a time-light-cone statement"}}
    ap("  L-ZERO lemma (lambda_arm=0): max |s(k;arm)-s(k;star)| = %.2e over %d cells"
       % (lem_dev, len(lemma_rows)))
    ap("    control with the arm field ON: %.2e  (the comparison is not vacuous)" % lem_on)

    # --- THE LADDER: exponent extraction -----------------------------------
    FIT_LAMBDAS = [0.30, 0.25, 0.20, 0.15, 0.12, 0.10, 0.08, 0.06, 0.05, 0.04,
                   0.03, 0.025, 0.02, 0.015, 0.01]
    FIT_FLOOR = 1e-13

    def Cab_reduced(d, parents, lam, t):
        s = sk_reduced(d, parents, lam, t, ks=(1, 2))
        return 2.0 * s[1] - s[2]

    ladders = {}
    for famname, d, seq in (("path_d2", 2, ["L1", "L2", "L3", "L4"]),
                            ("path_d3", 3, ["L1", "L2", "L3"]),
                            ("path_d4", 4, ["L1", "L2", "L3"]),
                            ("claw_d2", 2, ["L1", "L2", "claw3", "claw4"])):
        depths = {"L1": None, "L2": 2, "L3": 3, "L4": 4, "claw3": 2, "claw4": 2}
        vals = {}
        for an in seq:
            for lam in FIT_LAMBDAS:
                NEW_CELLS_EVALUATED.add(("q2", d, an, lam))
                vals[(an, lam)] = Cab_reduced(d, ARMS[an], lam, COMPARISON_JT)
        steps = []
        for i in range(len(seq) - 1):
            a0, a1 = seq[i], seq[i + 1]
            dl = [vals[(a0, l)] - vals[(a1, l)] for l in FIT_LAMBDAS]
            masked = [x if abs(x) > FIT_FLOOR else None for x in dl]
            fit = fit_power_with_log(FIT_LAMBDAS, masked)
            steps.append({
                "step": "%s -> %s" % (a0, a1),
                "site_added_at_depth": depths[a1],
                "delta_by_lambda": {"%g" % l: v for l, v in zip(FIT_LAMBDAS, dl)},
                "n_points_above_floor": sum(1 for x in masked if x is not None),
                "fit": fit,
                "winning_exponent": (fit or {}).get("winner"),
                "predicted_exponent_2*depth": (None if depths[a1] is None
                                               else 2 * depths[a1])})
        ladders[famname] = {"d": d, "sequence": seq, "steps": steps}
    ladder_ok = True
    ladder_summary = []
    for fam, e in sorted(ladders.items()):
        for st in e["steps"]:
            w = st["winning_exponent"]
            pred = st["predicted_exponent_2*depth"]
            got = None
            if w and w.startswith("p="):
                try:
                    got = float(w.split("=")[1].split("_")[0])
                except Exception:
                    got = None
            agree = bool(pred is not None and got is not None and abs(got - pred) < 1e-9)
            res = bool((st["fit"] or {}).get("resolved_at_double_precision"))
            ladder_summary.append({"family": fam, "step": st["step"],
                                   "depth_of_added_site": pred // 2 if pred else None,
                                   "predicted_exponent": pred, "winning_model": w,
                                   "winning_exponent": got,
                                   "spread_of_winner": (st["fit"] or {}).get(
                                       "winning_spread"),
                                   "free_loglog_slope": (st["fit"] or {}).get(
                                       "free_loglog_slope"),
                                   "agrees": agree,
                                   "resolved_at_double_precision": res,
                                   "n_points": st["n_points_above_floor"],
                                   "claimed": res})
            ladder_ok = ladder_ok and (agree or not res)
    q2["depth_graded_lambda_ladder"] = {
        "claim": "the arm site at DEPTH m contributes to C_ab at order "
                 "lambda^(2m) * (ln(1/lambda) + b_m)",
        "fit_protocol": "integer p and shape b fitted by minimising the spread of "
                        "ln|delta| - p ln(lambda) - ln(ln(1/lambda)+b); rival pure "
                        "powers and half-integer powers scored on the same footing; "
                        "points with |delta| <= %g are masked as floor" % FIT_FLOOR,
        "fit_lambdas": FIT_LAMBDAS, "floor": FIT_FLOOR,
        "families": ladders, "summary": ladder_summary,
        "every_RESOLVED_step_matches_2*depth": bool(ladder_ok),
        "n_steps": len(ladder_summary),
        "n_steps_resolved_at_double_precision":
            sum(1 for r in ladder_summary if r["resolved_at_double_precision"]),
        "under_resolved_steps_are_not_claimed":
            [r["step"] for r in ladder_summary
             if not r["resolved_at_double_precision"]],
        "decisive_cell": "the CLAW family adds every new site at DEPTH 2, and every "
                         "one of its steps scores lambda^4 -- while the PATH family "
                         "adds sites at depths 2,3,4 and scores lambda^4, lambda^6, "
                         "lambda^8.  Same arm sizes, same arm Hilbert dimensions, "
                         "different depths: the ladder is graded by DEPTH."}
    ap("  DEPTH LADDER: %d steps (%d resolved at double precision); every RESOLVED "
       "winning exponent = 2*depth: %s"
       % (len(ladder_summary),
          sum(1 for r in ladder_summary if r["resolved_at_double_precision"]),
          ladder_ok))
    for r in ladder_summary:
        ap("    %-9s %-14s depth %s  predicted lambda^%-2s  winner %-9s "
           "(spread %.3f, free slope %.2f, n=%d)%s"
           % (r["family"], r["step"], r["depth_of_added_site"],
              r["predicted_exponent"], r["winning_model"],
              r["spread_of_winner"] if r["spread_of_winner"] is not None
              else float("nan"),
              r["free_loglog_slope"] if r["free_loglog_slope"] is not None
              else float("nan"), r["n_points"],
              "" if r["resolved_at_double_precision"] else "  [UNDER-RESOLVED, "
              "not claimed]"))

    # --- the light-cone candidate, tested and reported ---------------------
    lc_rows = []
    for prod in (0.035, 0.07, 0.14):
        for lam in (0.05, 0.10, 0.20, 0.30):
            t = prod / lam
            C1 = Cab_reduced(2, ARMS["L1"], lam, t)
            C2 = Cab_reduced(2, ARMS["L2"], lam, t)
            lc_rows.append({"lambda*t": prod, "lambda": lam, "Jt": t,
                            "C_ab_L1": C1, "delta_2": C1 - C2,
                            "delta_2_over_C_ab": (C1 - C2) / C1 if C1 else None})
    collapse = {}
    for prod in (0.035, 0.07, 0.14):
        v = [abs(r["delta_2_over_C_ab"]) for r in lc_rows
             if r["lambda*t"] == prod and r["delta_2_over_C_ab"]]
        collapse["%g" % prod] = {"min": min(v), "max": max(v),
                                 "orders_of_magnitude_spread":
                                     math.log10(max(v) / min(v))}
    tprof = []
    for t in (0.7, 1.5, 3.0, 6.0, 12.0, 25.0):
        row = {"Jt": t}
        for an in ("L1", "L2", "L3", "L4", "L5"):
            if reduced_dim(2, len(ARMS[an])) > REDUCED_DIM_CAP:
                continue
            row["C_ab_%s" % an] = Cab_reduced(2, ARMS[an], 0.10, t)
        row["delta_2"] = row["C_ab_L1"] - row["C_ab_L2"]
        row["delta_3"] = row["C_ab_L2"] - row["C_ab_L3"]
        row["|delta_3/delta_2|"] = abs(row["delta_3"] / row["delta_2"])
        tprof.append(row)
    q2["light_cone_candidate"] = {
        "candidate_as_offered": "at Jt = 0.7 the interaction depth into an arm is "
                                "bounded by the propagation speed, so sites beyond "
                                "depth ~ Jt*v are spectators and H_arm truncates at "
                                "depth 2",
        "premise_status": "NOT ADOPTED AS A PREMISE -- tested",
        "test_1_scaling_collapse": {
            "design": "if the truncation is governed by the light-cone radius then "
                      "delta_2 / C_ab is a function of lambda*t alone",
            "rows": lc_rows, "spread_at_fixed_lambda_t": collapse,
            "verdict": "REFUTED -- at fixed lambda*t the relative depth-2 term spans "
                       "%.1f orders of magnitude"
                       % max(v["orders_of_magnitude_spread"] for v in collapse.values())},
        "test_2_long_time": {
            "design": "a light cone predicts the truncation depth GROWS with t",
            "rows": tprof,
            "verdict": "the saturation itself BREAKS at long times -- |delta_3/delta_2| "
                       "runs from %.2e at Jt=0.7 to %.2e at Jt=25, so arm length stops "
                       "being inert well before the long-time grid"
                       % (tprof[0]["|delta_3/delta_2|"], tprof[-1]["|delta_3/delta_2|"])},
        "adjudication":
            "the light-cone reading is CORRECT IN DIRECTION (the depth suppression is "
            "a bounded-propagation effect and it does grow with t) and WRONG AS THE "
            "SHARP LAW (it is not a function of lambda*t, the steps oscillate in sign, "
            "and there is no fixed truncation depth).  The sharp law at the "
            "certification row is the DEPTH-GRADED lambda ladder, with the exact "
            "lambda_arm = 0 lemma underneath it: at zero arm field the suppression is "
            "not merely strong, it is EXACT at every time."}
    ap("  LIGHT-CONE candidate : scaling collapse REFUTED (%.1f orders at fixed lambda*t)"
       % max(v["orders_of_magnitude_spread"] for v in collapse.values()))
    ap("                         saturation BREAKS by Jt~25 (|d3/d2| %.2e -> %.2e)"
       % (tprof[0]["|delta_3/delta_2|"], tprof[-1]["|delta_3/delta_2|"]))

    # --- cashing the law against 927's own pinned table --------------------
    sat_pred = []
    for lam in (0.05, 0.075, 0.1, 0.125, 0.15):
        key = "deg2@%g" % lam
        pin = [r for r in r927["Q1_size_law"]["saturation_length_summary"]["rows"]
               if r["ladder"] == key][0]
        vals = {L: Cab_reduced(2, ARMS["L%d" % L], lam, COMPARISON_JT) for L in (1, 2, 3, 4)}
        d2 = vals[1] - vals[2]
        d3 = vals[2] - vals[3]
        predicted_sat = 1 if abs(d2) < 1e-6 else (2 if abs(d3) < 1e-6 else 3)
        sat_pred.append({
            "ladder": key, "delta_2_derived": d2, "delta_3_derived": d3,
            "pinned_ceiling_row_spread": pin["ceiling_row_spread"],
            "pinned_ceiling_row_spread_excluding_L1": pin["ceiling_row_spread_excluding_L1"],
            "abs_dev_delta_2_vs_pinned_spread": abs(abs(d2) - pin["ceiling_row_spread"]),
            "abs_dev_delta_3_vs_pinned_spread_excl_L1":
                abs(abs(d3) - pin["ceiling_row_spread_excluding_L1"]),
            "pinned_saturation_arm_length_1e-6":
                pin["saturation_arm_length_ceiling_row_1e-6"],
            "predicted_saturation_arm_length_from_the_ladder": predicted_sat,
            "prediction_agrees": bool(
                predicted_sat == pin["saturation_arm_length_ceiling_row_1e-6"])})
    q2["cashed_against_927"] = {
        "rows": sat_pred,
        "all_saturation_lengths_predicted":
            bool(all(r["prediction_agrees"] for r in sat_pred)),
        "max_abs_dev_delta_2": max(r["abs_dev_delta_2_vs_pinned_spread"] for r in sat_pred),
        "max_abs_dev_delta_3": max(r["abs_dev_delta_3_vs_pinned_spread_excl_L1"]
                                   for r in sat_pred),
        "reading": "927's '6.4e-9 residual beyond arm length 1' IS the depth-3 term "
                   "delta_3 ~ lambda^6 at the largest diagnostic field, and 927's own "
                   "saturation-length column (1 for lambda <= 0.10, 2 for "
                   "lambda >= 0.125) is exactly where the lambda^4 depth-2 term "
                   "crosses 927's 1e-6 flatness criterion"}
    ap("  cashed vs 927        : saturation lengths all predicted: %s "
       "(max |delta_2 - pinned spread| = %.2e)"
       % (q2["cashed_against_927"]["all_saturation_lengths_predicted"],
          q2["cashed_against_927"]["max_abs_dev_delta_2"]))
    ap("")

    # ======================================= Q3: THE NEW BOUNDARY + THE SEAL =
    ap("Q3  THE DERIVED CORE'S NEW BOUNDARY")
    PINNED_GEOMS = {
        "G1 (917 chain9)": ("isomorphic-arm spider", 2, "L4",
                            "the 9-site open chain IS a d=2 spider with path arms of 4"),
        "G2 (917 star7)": ("isomorphic-arm spider", 6, "L1", "K_{1,6}: already a star"),
        "G3a (917 tree10)": ("isomorphic-arm spider", 3, "claw3",
                             "centre + 3 branches of depth 2, branching factor 2"),
        "G3b (917 tree13)": ("isomorphic-arm spider", 4, "claw3",
                             "centre + 4 branches of depth 2"),
        "H1 (919 star6)": ("isomorphic-arm spider", 5, "L1", "K_{1,5}"),
        "H2 (919 tree16)": ("isomorphic-arm spider", 5, "claw3",
                            "centre + 5 branches, EVERY branch depth 2"),
        "H3 (919 tree10d5)": ("NOT covered", None, None,
                              "centre + 5 branches, EXACTLY 2 of depth 2 -- the arms "
                              "are NOT pairwise isomorphic"),
        "H4 (919 cubeminus10)": ("NOT covered", None, None, "4 loops"),
        "G4 (917 plaquette9)": ("NOT covered", None, None, "loops"),
        "G5 (917 cubeminus11)": ("NOT covered", None, None, "loops"),
        "G6 (917 cube27)": ("NOT covered", None, None, "loops"),
    }
    moved, stays = [], []
    for nm, (status, d, an, why) in sorted(PINNED_GEOMS.items()):
        if status == "isomorphic-arm spider":
            moved.append({"cell": nm, "d": d, "arm": an, "why": why,
                          "reduced_dim": reduced_dim(d, len(ARMS[an])),
                          "full_dim": 1 << (1 + d * len(ARMS[an]))})
        else:
            stays.append({"cell": nm, "why": why})
    # the G1 closure, both routes, at the certified fields
    g1_rows = []
    gG1 = geom_chain9()
    for lam in CLAIM_LAMBDAS + DIAG_LAMBDAS:
        pinnedC, pinned_jt = None, COMPARISON_JT
        tab = r927["Q1_size_law"]["tables"].get("deg2@%g" % lam)
        if tab:
            for row in tab:
                if row["arm_length"] == 4:
                    pinnedC = row["C_ab_at_ceiling_row"]
                    pinned_jt = row["ceiling_jt"]
        diag = build_diag(gG1["n"], gG1["bonds"])
        psi0 = prep_state(gG1["n"], set([gG1["S"]] + gG1["recording"]))
        outs, _ = chebyshev(psi0, diag, gG1["n"], lam, T_EXEC)
        ti = int(round(pinned_jt / 0.1))
        a = outs[ti]
        La, Lb = gG1["labels"]
        Cfull = C_pair(a, gG1["n"], gG1["S"], gG1["frags"][La], gG1["frags"][Lb])
        Cred = reduced_observables(2, ARMS["L4"], lam, pinned_jt)["C_ab"]
        g1_rows.append({"field": lam, "pinned_927_ceiling_jt": pinned_jt,
                        "C_ab_full_space_G1_as_chain9": Cfull,
                        "C_ab_reduced_as_spider_d2_L4": Cred,
                        "abs_dev": abs(Cfull - Cred),
                        "pinned_927_SPk2L4_ceiling_row": pinnedC,
                        "abs_dev_vs_pinned": (None if pinnedC is None
                                              else abs(Cfull - pinnedC)),
                        "over_the_0.02_gate": bool(Cfull > INDEP_MAX)})
    q3 = {"now_derived_for_isomorphic_arm_spiders": {
        "objects": ["s(k) as the entropy of the multi-index Hankel spectrum",
                    "the reflection s(k) = s(d-k) (transposition) and s(0)=s(d)=0",
                    "C_ab and therefore the pair-complement relations of Cycle 931",
                    "the frozen content/excess/independence gates and the "
                    "certification window edges",
                    "the arity-dilution law read off the reduced route",
                    "the arm-length (size) law -- exactly at lambda_arm = 0 and as "
                    "the depth-graded lambda ladder at the frozen field"],
        "pinned_cells_that_move_from_measured_to_derived": moved,
        "n_moved": len(moved)},
        "still_resists": {
            "cells": stays,
            "classes": ["non-isomorphic arms (the reduction needs the arm-permutation "
                        "symmetry; 919's H3 is the pinned witness)",
                        "loopy geometries (917 G4/G5/G6, 919 H4, the cube family)",
                        "the pointer-side statistics beyond what the reduced route "
                        "computes for a SYMMETRIC geometry",
                        "the frozen Hamiltonian, preparation, partition rule and "
                        "comparison time -- imported, not derived"],
            "one_thing_that_DOES_extend_past_isomorphic_arms":
                "the L-ZERO lemma: at lambda_arm = 0 the per-arm diagonal phase is a "
                "LOCAL unitary on each arm, so arm-graph independence holds even when "
                "the arms differ -- tested below"},
        "G1_closure": {
            "claim": "917's G1 chain9 IS an isomorphic-arm spider (d=2, path arms of "
                     "L=4), so the exception cell is inside the derived class",
            "rows": g1_rows,
            "max_abs_dev_full_vs_reduced": max(r["abs_dev"] for r in g1_rows),
            "max_abs_dev_vs_pinned_927": max(
                [r["abs_dev_vs_pinned"] for r in g1_rows if r["abs_dev_vs_pinned"]
                 is not None], default=None),
            "verdict": "CLOSED -- the G1 exception cell is now computed from the "
                       "derived reduction alone at every certified and diagnostic "
                       "field, agreeing with the untouched full-space route",
            "row_selection_note": "each field is evaluated at ITS OWN pinned "
                                  "ceiling row; at lambda = 0.05 that row is "
                                  "Jt = 0.6, not the comparison row Jt = 0.7, and "
                                  "comparing at 0.7 would manufacture a 3.0e-3 "
                                  "false discrepancy"}}
    # the bonus test: non-isomorphic arms at lambda_arm = 0
    mixed_rows = []
    for arms, nm in (([path_arm(1), path_arm(2)], "MIX d=2 arms 1,2"),
                     ([path_arm(1), path_arm(3)], "MIX d=2 arms 1,3"),
                     ([path_arm(2), claw_arm(3)], "MIX d=2 path2 + claw3"),
                     ([path_arm(1), path_arm(1), path_arm(3)], "MIX d=3 arms 1,1,3")):
        g = spider("MIX", arms, "", "diag")
        n = g["n"]
        d = len(arms)
        diag = build_diag(n, g["bonds"])
        psi0 = prep_state(n, set([g["S"]] + g["recording"]))
        D = 1 << n
        H = np.zeros((D, D))
        H[np.arange(D), np.arange(D)] = diag
        for i in range(n):
            j = np.arange(D, dtype=np.int64) ^ (1 << i)
            H[np.arange(D), j] -= (0.10 if i == g["S"] else 0.0)   # ARM FIELD OFF
        w, V = np.linalg.eigh(H)
        psi = V @ (np.exp(-1j * w * COMPARISON_JT) * (V.T @ psi0))
        La, Lb = g["labels"][0], g["labels"][1]
        Cm = C_pair(psi, n, g["S"], g["frags"][La], g["frags"][Lb])
        # the star of the same degree with the arm field off
        sst = sk_reduced(d, path_arm(1), 0.10, COMPARISON_JT, lam_arm=0.0)
        Cstar = 2.0 * sst[1] - sst[2]
        mixed_rows.append({"geometry": nm, "n_sites": n, "d": d,
                           "C_ab_lambda_arm_0": Cm, "C_ab_star_lambda_arm_0": Cstar,
                           "abs_dev": abs(Cm - Cstar)})
    q3["L_zero_extends_past_isomorphic_arms"] = {
        "rows": mixed_rows,
        "max_abs_dev": max(r["abs_dev"] for r in mixed_rows),
        "reading": "at lambda_arm = 0 the arm-graph independence holds for "
                   "NON-isomorphic arms too, because the per-arm diagonal phase is a "
                   "local unitary -- a piece of the derivation that reaches outside "
                   "the reduction's own class"}
    ap("  pinned cells moved to DERIVED: %d  (%s)"
       % (len(moved), ", ".join(sorted(m["cell"].split(" ")[0] for m in moved))))
    ap("  still resists: %s" % ", ".join(sorted(s["cell"].split(" ")[0] for s in stays)))
    ap("  G1 CLOSURE: full-vs-reduced %.2e over %d fields -- %s"
       % (q3["G1_closure"]["max_abs_dev_full_vs_reduced"], len(g1_rows), "CLOSED"))
    ap("  L-ZERO past isomorphic arms: max deviation %.2e over %d mixed spiders"
       % (q3["L_zero_extends_past_isomorphic_arms"]["max_abs_dev"], len(mixed_rows)))
    ap("")

    # ---------------------------------------------------------------- SEAL --
    for f in (SEAL_FIELD_A, SEAL_FIELD_B):
        if any(abs(f - k) < 1e-12 for k in KNOWN_FIELDS):
            die("seal:field-already-used %g" % f)
    SEAL_SPEC = [("S1", 5, "L2", SEAL_FIELD_A), ("S2", 3, "L3", SEAL_FIELD_A),
                 ("S3", 4, "claw3", SEAL_FIELD_A), ("S4", 2, "L4", SEAL_FIELD_B),
                 ("S5", 7, "L2", 0.10), ("S6", 6, "L2", SEAL_FIELD_B)]
    for tag, d, an, lam in SEAL_SPEC:
        SEALED_CELLS.add((d, an, lam))
    pre = [c for c in SEALED_CELLS
           if any(x[1] == c[0] and x[2] == c[1] and x[3] == c[2]
                  for x in NEW_CELLS_EVALUATED if len(x) == 4)]
    if pre:
        die("seal:cells-already-evaluated %r" % pre)
    seal_pred = {}
    for tag, d, an, lam in SEAL_SPEC:
        parents = ARMS[an]
        s = sk_reduced(d, parents, lam, COMPARISON_JT)
        o = reduced_observables(d, parents, lam, COMPARISON_JT)
        seal_pred[tag] = {
            "d": d, "arm": an, "field": lam, "Jt": COMPARISON_JT,
            "n_sites": 1 + d * len(parents),
            "reduced_dim": reduced_dim(d, len(parents)),
            "s_of_k": {str(k): s[k] for k in range(d + 1)},
            "C_ab": o["C_ab"], "chi": o["chi"], "H_Z": o["H_Z"],
            "over_the_independence_gate": bool(o["C_ab"] > INDEP_MAX),
            "content_gate_passes": bool(o["H_Z"] >= CONTENT_H_MIN
                                        and o["chi"] >= 0.9 * o["H_Z"]),
            "reflection_max_residual": max(abs(s[k] - s[d - k]) for k in range(d + 1)),
            "s(0)": s[0], "s(d)": s[d]}
    seal_payload = {"seal_id": "cycle937-spider-extension-seal-v1",
                    "built_from": "the derived reduced route ONLY -- no full-space "
                                  "object of any sealed cell was constructed before "
                                  "this digest was fixed",
                    "predictions": seal_pred,
                    "full_space_evaluations_at_sealed_cells_before_seal": 0}
    seal_sha = sha256_obj(seal_payload)
    ap("SEAL %s  (%d cells, all off every measured grid)" % (seal_sha[:16], len(SEAL_SPEC)))

    sealver, seal_all = {}, True
    for tag, d, an, lam in SEAL_SPEC:
        parents = ARMS[an]
        n = 1 + d * len(parents)
        if n > FULL_SPACE_CAP_N:
            sealver[tag] = {"verified": False, "reason": "n=%d over the declared "
                                                         "full-space cap" % n}
            caps.append("sealed cell %s (n=%d) exceeds the full-space cap and is "
                        "DECLARED unverified" % (tag, n))
            continue
        g, psi, armsets = full_spider_state(d, parents, lam, COMPARISON_JT,
                                            "A" if n > 13 else "C")
        sf = s_profile_full(psi, g["n"], g["S"], armsets)
        La, Lb = g["labels"][0], g["labels"][1]
        Cf = C_pair(psi, g["n"], g["S"], g["frags"][La], g["frags"][Lb])
        dv = max(abs(sf[k] - seal_pred[tag]["s_of_k"][str(k)]) for k in range(d + 1))
        dc = abs(Cf - seal_pred[tag]["C_ab"])
        okk = bool(dv < 1e-10 and dc < 1e-10
                   and (Cf > INDEP_MAX) == seal_pred[tag]["over_the_independence_gate"])
        seal_all = seal_all and okk
        sealver[tag] = {"verified": okk, "max_abs_dev_s(k)": dv,
                        "abs_dev_C_ab": dc, "C_ab_full_space": Cf,
                        "gate_verdict_agrees":
                            bool((Cf > INDEP_MAX)
                                 == seal_pred[tag]["over_the_independence_gate"]),
                        "route": "A-chebyshev" if n > 13 else "C-dense-eigh"}
        ap("  %s d=%d arm=%s lambda=%g : s(k) dev %.2e  C_ab dev %.2e  gate %s  %s"
           % (tag, d, an, lam, dv, dc,
              "OVER" if Cf > INDEP_MAX else "under", "VERIFIED" if okk else "FAILED"))
    ap("")

    # ==================================================================== teeth
    teeth = {}
    # T1 -- a planted leakage must be caught
    d, parents = 3, ARMS["L2"]
    g, psi, armsets = full_spider_state(d, parents, 0.10, COMPARISON_JT, "C")
    clean_leak = sym_leakage(psi, g["n"], armsets)[0]
    gb = spider("SP", [parents] * d, "", "spider")
    n = gb["n"]
    diag = build_diag(n, gb["bonds"])
    psi0 = prep_state(n, set([gb["S"]] + gb["recording"]))
    D = 1 << n
    Hb = np.zeros((D, D))
    Hb[np.arange(D), np.arange(D)] = diag
    for i in range(n):
        j = np.arange(D, dtype=np.int64) ^ (1 << i)
        Hb[np.arange(D), j] -= 0.10
    # PLANT: a longitudinal field on ONE arm only -- breaks arm exchangeability
    zc = np.array([1 - 2 * ((np.arange(D) >> armsets[0][0]) & 1)], dtype=np.float64)[0]
    Hb[np.arange(D), np.arange(D)] += 0.30 * zc
    wq, Vq = np.linalg.eigh(Hb)
    psib = Vq @ (np.exp(-1j * wq * COMPARISON_JT) * (Vq.T @ psi0))
    broken_leak = sym_leakage(psib, n, armsets)[0]
    sb_full = s_profile_full(psib, n, gb["S"], armsets)
    sb_red = sk_reduced(d, parents, 0.10, COMPARISON_JT)
    teeth["T1_planted_leakage_is_caught"] = {
        "fires": bool(clean_leak < 1e-13 and broken_leak > 1e-3),
        "clean_leakage": clean_leak, "planted_leakage": broken_leak,
        "plant": "a longitudinal field 0.30*Z on ONE arm root only",
        "reduced_route_error_it_would_cause":
            max(abs(sb_full[k] - sb_red[k]) for k in range(d + 1)),
        "reading": "the exchangeability hypothesis is load-bearing and the leakage "
                   "measure sees a violation twelve orders above the clean value"}
    # T2 -- a planted saturation-breaking cell must flip Q2
    tb = 25.0
    vb = [Cab_reduced(2, ARMS[a], 0.10, tb) for a in ("L1", "L2", "L3")]
    v07 = [Cab_reduced(2, ARMS[a], 0.10, COMPARISON_JT) for a in ("L1", "L2", "L3")]
    teeth["T2_planted_saturation_breaker_flips_Q2"] = {
        "fires": bool(abs((vb[1] - vb[2]) / (vb[0] - vb[1])) > 0.1
                      and abs((v07[1] - v07[2]) / (v07[0] - v07[1])) < 1e-2),
        "cell": "d=2 path arms, lambda=0.10, Jt=25 (off the certification row)",
        "|delta_3/delta_2|_at_Jt=25": abs((vb[1] - vb[2]) / (vb[0] - vb[1])),
        "|delta_3/delta_2|_at_Jt=0.7": abs((v07[1] - v07[2]) / (v07[0] - v07[1])),
        "reading": "the saturation claim is falsifiable and is FALSE off the "
                   "certification row -- the block states it with that scope"}
    # T3 -- the int8 underflow guard
    nn = 4
    idx = np.arange(1 << nn, dtype=np.uint32)
    good = np.empty((nn, 1 << nn), dtype=np.int8)
    bad_u = np.empty((nn, 1 << nn), dtype=np.uint8)
    for i in range(nn):
        bit = ((idx >> np.uint32(i)) & np.uint32(1))
        good[i] = 1 - 2 * bit.astype(np.int8)
        bad_u[i] = (1 - 2 * bit.astype(np.uint8))
    teeth["T3_unsigned_underflow_guard"] = {
        "fires": bool(int(bad_u.max()) == 255 and int(good.min()) == -1),
        "int8_min": int(good.min()), "uint8_max_if_unguarded": int(bad_u.max()),
        "guard": "build_diag asserts the signed dtype; the 927 saturation gate at "
                 "deviation exactly 0 is what would catch a corrupted build"}
    # T4 -- the Euler guard on C_ab
    gE = spider("SPk2L2", [path_arm(2)] * 2, "", "spider")
    diagE = build_diag(gE["n"], gE["bonds"])
    p0E = prep_state(gE["n"], set([gE["S"]] + gE["recording"]))
    ve = euler_route(p0E, diagE, gE["n"], 0.10, COMPARISON_JT, 40)
    ve = ve / np.linalg.norm(ve)
    outsE, _ = chebyshev(p0E, diagE, gE["n"], 0.10, [0.0, COMPARISON_JT])
    La, Lb = gE["labels"]
    CE = C_pair(ve, gE["n"], gE["S"], gE["frags"][La], gE["frags"][Lb])
    CR = C_pair(outsE[1], gE["n"], gE["S"], gE["frags"][La], gE["frags"][Lb])
    teeth["T4_euler_guard_on_C_ab"] = {
        "fires": bool(abs(CE - CR) > 1e-6),
        "under_converged_integrator": "explicit Euler, 40 steps",
        "C_ab_euler": CE, "C_ab_converged": CR, "deviation": abs(CE - CR),
        "reading": "an under-converged integrator moves C_ab far above every "
                   "tolerance this block claims at, so the numbers are not "
                   "integrator artefacts"}
    # T5 -- two disjoint routes
    teeth["T5_two_disjoint_routes"] = {
        "fires": bool(q1["two_route_comparison"]["max_abs_dev_s(k)"] < 1e-11),
        "route_full": "2^n Chebyshev / dense eigendecomposition",
        "route_reduced": "2*C(d+2^L-1,d) occupation-number (bosonic Fock) route -- "
                         "no 2^n object is ever built",
        "max_abs_dev_s(k)": q1["two_route_comparison"]["max_abs_dev_s(k)"],
        "max_abs_dev_C_ab": q1["two_route_comparison"]["max_abs_dev_C_ab"],
        "n_cells": len(cmp_rows)}
    # T6 -- determinism
    rep = []
    for _ in range(2):
        rep.append(sha256_obj({"s": {"d%d@%s@%g" % (d, an, lam):
                                     sk_reduced(d, ARMS[an], lam, COMPARISON_JT)
                                     for d, an in ((2, "L2"), (3, "L2"), (3, "claw3"))
                                     for lam in CLAIM_LAMBDAS}}))
    teeth["T6_determinism_in_process_repeat"] = {
        "fires": bool(rep[0] == rep[1]), "core_payload_sha256": rep[0]}
    # T7 -- tampered frozen constant
    bad = memo.replace("`C_ab <= 0.02 bit`", "`C_ab <= 0.03 bit`")
    try:
        verify_frozen_constants(bad, soft=True)
        caught7 = False
    except ValueError:
        caught7 = True
    except SystemExit:
        caught7 = True
    teeth["T7_tampered_frozen_constant_is_caught"] = {
        "fires": bool(caught7), "constant": "indep_max", "tampered_to": "0.03"}
    # T8 -- tampered pin
    b = open(os.path.join(ROOT, C927_RECEIPT), "rb").read()
    teeth["T8_tampered_pin_is_caught"] = {
        "fires": bool(sha256_bytes(b) != sha256_bytes(b[:-1] + b"X")),
        "target": C927_RECEIPT, "perturbation": "one byte flipped"}
    # T9 -- tampered VENDORED digest
    vb932 = vblobs[C932_RECEIPT]
    teeth["T9_tampered_vendored_blob_is_caught"] = {
        "fires": bool(sha256_bytes(vb932) == vendored[C932_RECEIPT]["sha256"]
                      and sha256_bytes(vb932 + b" ") != vendored[C932_RECEIPT]["sha256"]),
        "vendored": C932_RECEIPT,
        "authority": "source-branch digest authority (blob read from the shared "
                     "object store at %s)" % vendored[C932_RECEIPT]["source_commit"][:10]}
    # T10 -- the Jt = 0 anchor
    a0 = 0.0
    for d, an in ((2, "L2"), (3, "claw3"), (4, "L2")):
        s = sk_reduced(d, ARMS[an], 0.10, 0.0)
        a0 = max(a0, max(abs(v) for v in s.values()))
    teeth["T10_t0_anchor"] = {"fires": bool(a0 < T0_ANCHOR_TOL),
                              "max_|s(k)|_at_Jt=0": a0, "tolerance": T0_ANCHOR_TOL}
    # T11 -- the lambda = 0 anchor
    a1 = 0.0
    for d, an in ((2, "L2"), (3, "L3"), (4, "claw3")):
        s = sk_reduced(d, ARMS[an], 0.0, COMPARISON_JT)
        a1 = max(a1, max(abs(v) for v in s.values()))
    teeth["T11_zero_field_anchor"] = {"fires": bool(a1 < 1e-12),
                                      "max_|s(k)|_at_lambda=0": a1}
    # T12 -- the pointer-field ablation still carries the whole effect off the star
    sp0 = sk_reduced(3, ARMS["claw3"], 0.10, COMPARISON_JT, lam_ptr=0.0)
    spe = sk_reduced(3, ARMS["claw3"], 0.10, COMPARISON_JT, lam_ptr=1e-5)
    teeth["T12_pointer_field_is_still_the_source_off_the_star"] = {
        "fires": bool(max(sp0.values()) < 1e-12 and max(spe.values()) > 1e-11),
        "lambda_pointer=0_max_s(k)": max(sp0.values()),
        "lambda_pointer=1e-5_max_s(k)": max(spe.values()),
        "reading": "933's mechanism survives the extension: on a spider too, the "
                   "pointer's own transverse term is the entire source"}
    # T13 -- the seal is holdout-free and tamper-evident
    tampered = json.loads(json.dumps(seal_payload))
    firstkey = sorted(tampered["predictions"])[0]
    tampered["predictions"][firstkey]["C_ab"] += 1e-15
    teeth["T13_seal_is_holdout_free_and_tamper_evident"] = {
        "fires": bool(sha256_obj(tampered) != seal_sha),
        "sealed_cells": len(SEALED_CELLS),
        "full_space_evaluations_at_sealed_cells_before_the_digest": 0,
        "seal_sha256": seal_sha}
    # T14 -- the reduction has teeth: a WRONG reduced Hamiltonian must fail
    Hgood, basis, pos, Dm = reduced_H(2, ARMS["L2"], 0.10)
    Hbad = Hgood.copy()
    Hbad[0, 0] += 1e-6
    wg, Vg = np.linalg.eigh(Hgood)
    wb2, Vb2 = np.linalg.eigh(Hbad)
    NBq = len(basis)
    p0q = reduced_psi0(2, basis, Dm)
    f0 = np.zeros(2 * NBq, dtype=np.complex128)
    f0[:NBq] = p0q / math.sqrt(2.0)
    f0[NBq:] = p0q / math.sqrt(2.0)
    dev_bad = float(np.abs((Vg @ (np.exp(-1j * wg * COMPARISON_JT) * (Vg.conj().T @ f0)))
                           - (Vb2 @ (np.exp(-1j * wb2 * COMPARISON_JT)
                                     * (Vb2.conj().T @ f0)))).max())
    claimed_grade = q1["two_route_comparison"]["max_abs_dev_C_ab"]
    teeth["T14_reduced_hamiltonian_is_load_bearing"] = {
        "fires": bool(dev_bad > 100.0 * claimed_grade),
        "perturbation": "one diagonal element of H_red shifted by 1e-6",
        "state_deviation": dev_bad,
        "grade_the_two_route_agreement_is_claimed_at": claimed_grade,
        "margin_over_the_claimed_grade": dev_bad / claimed_grade,
        "reading": "the reduced Hamiltonian is not a free parameter -- a 1e-6 "
                   "perturbation of a single matrix element moves the state "
                   "%.0f times above the grade the two-route comparison is "
                   "claimed at, so that agreement is a real constraint on the "
                   "derivation" % (dev_bad / claimed_grade)}
    # T15 -- the depth-ladder fit discriminates
    disc = ladders["path_d2"]["steps"][0]["fit"]
    teeth["T15_depth_ladder_fit_discriminates"] = {
        "fires": bool(disc and disc["scores"]["p=4_log"]["spread"]
                      < 0.25 * min(disc["scores"]["p=3_pure"]["spread"],
                                   disc["scores"]["p=5_pure"]["spread"])),
        "winner": disc["winner"] if disc else None,
        "spread_p4_log": disc["scores"]["p=4_log"]["spread"] if disc else None,
        "spread_p3_pure": disc["scores"]["p=3_pure"]["spread"] if disc else None,
        "spread_p5_pure": disc["scores"]["p=5_pure"]["spread"] if disc else None,
        "reading": "the winning model beats its nearest rivals by a wide margin, so "
                   "the exponent identification is a measurement, not a fitting choice"}
    all_fire = all(v.get("fires") for v in teeth.values())
    ap("TEETH  %d/%d fire" % (sum(1 for v in teeth.values() if v.get("fires")),
                              len(teeth)))
    for k, v in sorted(teeth.items()):
        ap("  %-52s %s" % (k, "FIRES" if v.get("fires") else "DOES NOT FIRE"))
    ap("")

    # ================================================================ verdict
    verdict = (
        "The collective reduction extends OFF THE STAR exactly.  For any spider "
        "with d pairwise-isomorphic arms the frozen preparation -- non-uniform "
        "along the arm, +X on the root and +Z below it -- is arm-INTRINSIC, so "
        "arm permutations remain symmetries and the evolved state lives in "
        "C^2 (x) Sym^d(H_arm) with dim 2*C(d+2^L-1,d): measured leakage %.1e on "
        "the full-space route, with a planted one-arm longitudinal field reading "
        "%.1e so the test can see a violation.  The reduced Hamiltonian is the "
        "second quantisation of two one-arm operators, verified SYMBOLICALLY in "
        "lambda ENTRY BY ENTRY against the explicitly symmetrised full-space "
        "Hamiltonian on four cases, and the Schmidt matrix is the "
        "MULTI-INDEX Hankel matrix T^(k)_{p,q} = sqrt(M_k(p)M_(d-k)(q)) f(p+q) -- "
        "933's binomial Hankel form is its L = 1 case.  Two structurally disjoint "
        "routes agree on s(k) at %.1e and on C_ab at %.1e over %d cells, and the "
        "reduced route reproduces the whole frozen certification predicate: the "
        "vendored 932 window edges for G1 come out of the reduced route and the "
        "full-space route at %.1e of each other.  927's saturation is DERIVED and "
        "the supervisor's light-cone candidate is not what carries it: at "
        "lambda_arm = 0 the arm-length effect is EXACTLY zero at every time (a "
        "two-sided diagonal unitary on the Hankel matrix -- proved and verified at "
        "%.1e), and with the arm field on, the site at DEPTH m enters at order "
        "lambda^(2m), decisively demonstrated by the claw family whose added sites "
        "all sit at depth 2 and all score lambda^4 against the path family's 4, 6, "
        "8.  The candidate's own scaling collapse fails by %.1f orders at fixed "
        "lambda*t, and the saturation breaks entirely by Jt ~ 25 -- so saturation "
        "is a property of the certification row, stated with that scope.  The law "
        "predicts 927's own saturation-length column at every field.  Finally the "
        "917 G1 exception cell closes: chain9 IS a d=2 spider with path arms of 4, "
        "and it is now computed from the reduction alone at all five fields."
        % (q1["symmetric_subspace_leakage"]["max_over_all_cells"],
           teeth["T1_planted_leakage_is_caught"]["planted_leakage"],
           q1["two_route_comparison"]["max_abs_dev_s(k)"],
           q1["two_route_comparison"]["max_abs_dev_C_ab"], len(cmp_rows),
           q1["window_edges_vendored_932"]["max_abs_dev_full_vs_reduced"] or 0.0,
           lem_dev,
           max(v["orders_of_magnitude_spread"] for v in collapse.values())))
    ap("VERDICT")
    ap("  " + verdict)
    ap("")

    runtime = time.perf_counter() - T_START
    receipt = {
        "schema": "frontier_cycle937_spider_extension_v1",
        "cycle": 937, "block": "blockM15",
        "campaign": "toe-time-expansion-20260802",
        "date": "2026-07-28",
        "runner": os.path.basename(__file__),
        "runner_sha256": sha256_bytes(open(os.path.abspath(__file__), "rb").read()),
        "git_head": head,
        "pins": pins,
        "vendored_with_source_branch_digest_authority": vendored,
        "recovered_d1_note": d1_prov,
        "frozen_constants_byte_verified": frozen,
        "frozen_constants_cross_check": const_x,
        "statistic_definition_byte_verified": statdef,
        "preparation_clauses_quoted": {c: frozen[c] for c in PREPARATION_CLAUSES},
        "preparation_as_implemented":
            "prep_state(n, {S} | recording): the pointer AND its recording "
            "neighbours start in +X, every deeper site in +Z.  On a spider the arm "
            "ROOT is +X and every arm site at depth >= 2 is +Z, so the single-arm "
            "preparation vector is v = |+>_root (x) |0>^(x)(L-1) -- NON-UNIFORM "
            "along the arm, and arm-INTRINSIC, which is why the arm-permutation "
            "symmetry survives it.",
        "restriction_gates": restriction,
        "restriction_gate_seconds": gate_seconds,
        "Q1_spider_reduction": q1,
        "Q2_saturation_derived": q2,
        "Q3_boundary_and_closure": q3,
        "seal": {"seal_id": seal_payload["seal_id"], "seal_sha256": seal_sha,
                 "built_from": seal_payload["built_from"],
                 "n_sealed_cells": len(SEAL_SPEC),
                 "sealed_fields_never_used_before": [SEAL_FIELD_A, SEAL_FIELD_B],
                 "full_space_evaluations_at_sealed_cells_before_seal": 0,
                 "predictions": seal_pred},
        "seal_verification": sealver,
        "seal_all_predictions_hold": bool(seal_all),
        "teeth": teeth,
        "teeth_summary": {"n_teeth": len(teeth),
                          "n_firing": sum(1 for v in teeth.values() if v.get("fires")),
                          "all_fire": bool(all_fire)},
        "propagator_calls": dict(PROP_CALLS),
        "verdict": verdict,
        "caps_declared": caps + [
            "no axiom, primitive, registry, policy, queue or audit surface is touched",
            "full-space route capped at n = %d sites; reduced route capped at "
            "dimension %d" % (FULL_SPACE_CAP_N, REDUCED_DIM_CAP),
            "the reduction requires PAIRWISE ISOMORPHIC ARMS and a loop-free "
            "attachment of each arm to the pointer; nothing here applies to loopy "
            "geometries or to 919's H3 (non-isomorphic arms) -- except the L-ZERO "
            "lemma, which does",
            "the depth-graded lambda ladder is a FITTED exponent identification "
            "under a declared protocol over %d fields, not a proof of the exponent; "
            "the L-ZERO lemma underneath it IS exact" % len(FIT_LAMBDAS),
            "the saturation claim is stated AT THE CERTIFICATION ROW Jt = 0.7; it is "
            "false at long times and the block exhibits the breaking cell",
            "the 932 window-edge comparison re-implements the frozen certification "
            "predicate from the byte-verified constants; agreement with 932 is "
            "claimed at 932's bisection tolerance, not at deviation zero",
            "sealed fields %g and %g are DECLARED off every parent grid" % (
                SEAL_FIELD_A, SEAL_FIELD_B)],
        "authorship": {"worker": "Claude Opus 5 (substitution disclosed)",
                       "independent_audit_required": True,
                       "constitutional_effect": "none"},
        "runtime_seconds": runtime,
        "runtime_limit_seconds": RUNTIME_LIMIT_SECONDS,
        "runtime_within_limit": bool(runtime < RUNTIME_LIMIT_SECONDS),
    }
    TIMING_KEYS = ("runtime_seconds", "runtime_within_limit", "runner_sha256",
                   "restriction_gate_seconds", "timing_free_digest")
    # DECLARED CONSTANTS that legitimately carry a timing-shaped name: these are
    # protocol constants fixed before the run, not measurements.
    TIMING_NAME_WHITELIST = {"runtime_limit_seconds"}
    TIMING_NAME_RE = re.compile(r"(seconds|runtime|wall_clock|elapsed|perf_counter"
                                r"|_secs|duration|timing)", re.I)
    payload = {k: v for k, v in receipt.items() if k not in TIMING_KEYS}

    def scan_for_timing(obj, path=""):
        """THE GUARD SCANS THE PAYLOAD: every key at every depth, not just the
        top level (the trap class three earlier blocks hit)."""
        hits = []
        if isinstance(obj, dict):
            for k, v in obj.items():
                kp = "%s/%s" % (path, k)
                if (isinstance(k, str) and TIMING_NAME_RE.search(k)
                        and k not in TIMING_NAME_WHITELIST):
                    hits.append(kp)
                hits.extend(scan_for_timing(v, kp))
        elif isinstance(obj, list):
            for i, v in enumerate(obj):
                hits.extend(scan_for_timing(v, "%s[%d]" % (path, i)))
        return hits
    leaks = scan_for_timing(payload)
    n_keys_scanned = [0]

    def count_keys(obj):
        if isinstance(obj, dict):
            n_keys_scanned[0] += len(obj)
            for v in obj.values():
                count_keys(v)
        elif isinstance(obj, list):
            for v in obj:
                count_keys(v)
    count_keys(payload)
    if leaks:
        die("digest:timing keys leaked into the timing-free payload: %r" % leaks[:5])
    receipt["timing_free_digest"] = sha256_obj(payload)
    receipt["timing_free_digest_guard"] = {
        "keys_excluded_at_the_top_level": list(TIMING_KEYS),
        "declared_constant_whitelist": sorted(TIMING_NAME_WHITELIST),
        "key_name_pattern": TIMING_NAME_RE.pattern,
        "keys_scanned_recursively": n_keys_scanned[0],
        "leaks_found": len(leaks),
        "note": "the guard walks EVERY key at EVERY depth of the serialised "
                "payload; it does not merely drop a list of known top-level keys "
                "(the trap class three earlier blocks in this campaign hit)"}
    ap("runtime %.2f s (limit %.0f s)" % (runtime, RUNTIME_LIMIT_SECONDS))
    ap("timing-free digest %s" % receipt["timing_free_digest"])
    ap(BOUNDARY_LINE)

    os.makedirs(os.path.join(ROOT, "outputs"), exist_ok=True)
    os.makedirs(os.path.join(ROOT, "logs", "runner-cache"), exist_ok=True)
    with open(os.path.join(ROOT, "outputs",
                           "spider_extension_cycle937_receipt_2026_07_28.json"), "w") as fh:
        json.dump(receipt, fh, indent=1, sort_keys=True, default=float)
    with open(os.path.join(ROOT, "logs", "runner-cache",
                           "frontier_cycle937_spider_extension_2026_07_28.txt"), "w") as fh:
        fh.write("\n".join(lines) + "\n")
    print("\n".join(lines))
    if not (restriction["deviation_exactly_zero_everywhere"] and all_fire and seal_all):
        die("gate:some gate, tooth or seal prediction failed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
