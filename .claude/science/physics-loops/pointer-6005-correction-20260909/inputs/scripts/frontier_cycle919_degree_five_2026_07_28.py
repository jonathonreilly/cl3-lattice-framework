#!/usr/bin/env python3
"""Cycle 919 -- THE BRACKET'S INTERIOR: the degree-5 measurement.

THE QUESTION.  Cycle 917 measured the geometry ladder under the frozen route-C
certification gates and left ONE number un-located.  Its lambda = 0.10 split is
consistent with a POINTER-DEGREE threshold, and its checker's declared non-claim
diagnostic sharpened that into a graded FIELD CEILING that rises with pointer
degree:

    degree 2 -> 0.05      degree 3 -> 0.075     degree 4 -> 0.075
    degree 6 -> 0.10

The 917 geometry set contained NO degree-5 geometry.  The threshold is therefore
BRACKETED in (4, 6] and not located.  This block measures the interior:

    does degree 5 certify at lambda = 0.10 (threshold (4, 5]: 5 behaves like 6)
    or not (threshold (5, 6]: 5 behaves like 4)?

Either answer tightens the bracket by one notch.  Both are reachable; the gates
below are outcome-neutral by construction and the falsifier block demonstrates
it.

THE DESIGN DISCIPLINE.  This block designs its DEGREE-5 GEOMETRY SET and its ONE
extra field, and inherits everything else from

    docs/D3_BAR_LOCATION_DESIGN_SCOUT_2026-07-10.md   (FROZEN 2026-07-10)

verbatim: H_lambda = -sum_<ij> Z_i Z_j - lambda sum_i X_i, the pointer-contrast
preparation rule (the pointer and its neighbours in +X, every other site in +Z),
the three-condition Holevo certification at the frozen deltas, the C_ab <= 0.02
conditional-independence gate, the R_ind >= 2 permanence bar with the frozen
label-order tie-break, the Jt <= 1 onset deadline, the three-consecutive-sample
persistence flag, and the t = 0 baseline requirement (chi(0) <= 1e-9 bit).  All
21 of those constants are BYTE-VERIFIED out of the frozen memo below, by the
same patterns Cycle 917 used.

THE DEGREE-5 GEOMETRY SET (design freedom #1, declared here).  Four geometries,
all with pointer degree exactly 5, chosen to SEPARATE degree from the confounds
Cycle 917's checker named (system size, depth, loops, fragment size):

  H1  star6        K_{1,5}: centre + 5 leaves                6 sites  depth 1  loops 0
  H2  tree16       centre + 5 branches, EVERY branch of      16 sites depth 2  loops 0
                   depth 2 with branching factor 2 -- the
                   917 tree family's degree-5 member
                   (917 G3a = 3 branches, G3b = 4 branches)
  H3  tree10d5     centre + 5 branches, EXACTLY 2 of them    10 sites depth 2  loops 0
                   of depth 2 (b0, b1 carry two children
                   each; b2, b3, b4 are leaves)
  H4  cubeminus10  917's G5 cubeminus11 with the -z face     10 sites depth 2  loops 4
                   DELETED: centre + 5 faces + the 4 z=0
                   edges -- a controlled degree 6 -> 5
                   deletion at fixed loop number

H1/H2/H3 hold degree at 5 while n runs 6 -> 16 and depth runs 1 -> 2; H4 adds
loops at fixed degree.  If the four agree, degree is isolated from all four
confounds AT degree 5.  If they split, the split is the finding.

THE FIELD SET (design freedom #2, declared here).  lambda in {0.05, 0.10} are
the FROZEN certified fields.  lambda = 0.075 is a DECLARED DESIGN EXTENSION,
flagged as such everywhere it appears, with its reason: 0.075 is exactly where
the 917 diagnostic puts the degree-3 and degree-4 ceiling, so a degree-5 verdict
there is the discriminating cell between "5 behaves like 4" and "5 behaves like
6".  The wider probe grid {0.02 ... 0.20} is carried over from the 917 checker
as a DECLARED NON-CLAIM DIAGNOSTIC, its precedent and its status.

ROUTE.  Full-space exact evolution on every geometry; the largest is H2 at
2^16 = 65536 amplitudes.  Route A is a Chebyshev expansion of exp(-iHt) with a
rigorous Bessel tail bound; route B is a scaling-and-marching Taylor propagator
with a rigorous factorial remainder bound (an algorithm independent of route A);
route C, where the Hilbert space allows it (n <= 12), is an exact dense
eigendecomposition.  No orbit reduction is used; its exactness is nonetheless
demonstrated on H1.

RESTRICTION GATES.  Before any new number is produced the runner reproduces
Cycle 917 VALUE-FOR-VALUE on its own machinery: all six measured 917 geometries
(chain, star, both trees, plaquette, cube-minus) at both frozen fields, row by
row -- chi, C_ab, theta_A, the R_ind ledger, xi_reg, max R_ind, the verdict and
the event -- against the pinned 917 receipt; and the 917 checker's 0.075 ceiling
verdicts against the pinned 917 checker receipt.  Any mismatch is a hard fail.

Deterministic, float64/complex128, no network, no tree writes outside the
declared receipt.

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
    # the 917 primary + checker, their receipts, and the landed 917 note
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
    # the upstream commission / recovery receipts the 917 ladder imports from
    "outputs/d3_bar_commission_cycle914_receipt_2026_07_28.json": (
        "fba8a16ee811fa1729bc1cdb6988096193a7e14878e7a78380f4880120bf7223",
        "cabb1bef15221b5fca61ffc7c50f8ec18452893d"),
    "outputs/comparator_recovery_cycle915_receipt_2026_07_28.json": (
        "d7d27ce19d231624415db1e71ee77eae16b5175dd403b403c254b38fb171b0a7",
        "9931c298a5917eb90de290cbb82c237508c9e692"),
}

PARENT_MEMO = "docs/D3_BAR_LOCATION_DESIGN_SCOUT_2026-07-10.md"
C917_RECEIPT = "outputs/geometry_ladder_cycle917_receipt_2026_07_28.json"
C917_CHECK_RECEIPT = "outputs/geometry_independent_check_cycle917_receipt_2026_07_28.json"
C915_RECEIPT = "outputs/comparator_recovery_cycle915_receipt_2026_07_28.json"

# the recovered d=1 comparator note -- NOT in tree; consumed as git-history
# evidence, exactly as Cycle 917 consumed it (the no-go detector's source).
D1_NOTE_PATH = "docs/REGISTRATION_REDUNDANCY_ONSET_BOUNDED_NOTE_2026-07-09.md"
D1_NOTE_BLOB = "dd247a8494f171d4dcaf9a532a09491202b1f512"
D1_NOTE_SHA256 = "41b4f26af908a7b910fbb5683f9d50432f36328bced7cf107585f7f70771df04"
D1_NOTE_BYTES = 5230

# ============================================== frozen protocol constants ====
# Every constant below is BYTE-VERIFIED against the frozen memo in
# verify_frozen_constants(); a mismatch is a hard fail, exit 2.
FROZEN_LAMBDAS = (0.05, 0.10)      # the CERTIFIED fields (914/915 commission)
EXTENSION_LAMBDA = 0.075           # DECLARED DESIGN EXTENSION (this block)
LAMBDAS = (0.05, 0.075, 0.10)
MEMO_LAMBDAS = (0.05, 0.10, 0.20)
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
RESTRICT_TOL = 1e-9             # 917 value-for-value reproduction tolerance
T_EXEC = [round(0.1 * i, 10) for i in range(13)]   # Jt = 0.0 .. 1.2, 13 points
# the 917 checker's probe grid, carried over verbatim as a NON-CLAIM diagnostic
PROBE_LAMBDAS = (0.02, 0.05, 0.075, 0.10, 0.125, 0.15, 0.20)

CUBE_LABELS = ("+x", "-x", "+y", "-y", "+z", "-z")

# the 917 keys this block re-measures as its restriction gate
C917_KEYS = ["G1", "G2", "G3a", "G3b", "G4", "G5"]
# the degree-5 keys this block introduces
NEW_KEYS = ["H1", "H2", "H3", "H4"]


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
    """Read the never-landed d=1 comparator note out of git history (917's route)."""
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
    rec917 = json.load(open(os.path.join(ROOT, C917_RECEIPT)))
    if rec917["recovered_d1_note"]["sha256"] != got:
        die("d1-note:917-receipt-cross-check")
    return b.decode("utf-8"), {"path": D1_NOTE_PATH, "blob": D1_NOTE_BLOB,
                               "sha256": got, "bytes": len(b),
                               "in_tree_at_head": False,
                               "sha256_matches_915_receipt": True,
                               "sha256_matches_917_receipt": True,
                               "commands_disclosed": cmds}


# ============================== restriction gate: frozen constants by bytes ==
# Identical to Cycle 917's 21 patterns; re-declared here and re-verified from
# the memo's own bytes rather than imported from the 917 source.
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


def cross_check_917_constants(frozen):
    """The 917 receipt published the same 21 quotes; they must agree byte-for-byte."""
    rec = json.load(open(os.path.join(ROOT, C917_RECEIPT)))
    theirs = rec["frozen_constants_byte_verified"]
    if set(theirs) != set(frozen):
        die("frozen-const:917-key-set %s" % sorted(set(theirs) ^ set(frozen)))
    for k in sorted(frozen):
        if theirs[k]["quote"] != frozen[k]["quote"]:
            die("frozen-const:917-quote %s" % k)
    return {"count": len(frozen), "identical_to_917_receipt": True}


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
                   tiebreak, dim, note):
    """Assemble a geometry: index the sites, derive recording sites, and build the
    fragment partition by the INHERITED rule (anchor + nearest-anchor + tie-break)."""
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
    return {
        "key": key, "name": name, "note": note, "dim": dim, "n": n,
        "sites": [str(c) for c in sites], "coords": sites, "idx": idx,
        "bonds": bonds, "adj": adj, "S": S, "pointer": str(pointer),
        "recording": rec, "labels": labels, "frags": frags, "ties": ties,
        "dS": dS, "shells": shells, "degrees": degs,
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


# ------------------------------------------- the pinned Cycle 917 geometries --
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
    note = ("917 %s: centre + %d branches of depth 2, branching factor 2"
            % (key, nbranch)) if nbranch < 5 else (
        "NEW: the 917 tree family's DEGREE-5 member -- centre + 5 branches of depth 2 "
        "with branching factor 2 (917 G3a = 3 branches, G3b = 4 branches).  All five "
        "branches have depth 2, which satisfies the declared 'at least 2 of depth 2'.")
    return build_geometry(key, "tree%d" % len(sites), sites, bonds, "S",
                          lambda c: c, None, "tree", note)


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
                          cube_tiebreak, 3,
                          "917 G5: centre + 6 faces + the 4 z=0 edges")


def geom_cube27():
    sites = [(x, y, z) for x in (-1, 0, 1) for y in (-1, 0, 1) for z in (-1, 0, 1)]
    bonds = [(a, b) for ia, a in enumerate(sites) for b in sites[ia + 1:]
             if sum(abs(a[k] - b[k]) for k in range(3)) == 1]
    return build_geometry("G6", "cube27", sites, bonds, (0, 0, 0), _axis_label,
                          cube_tiebreak, 3,
                          "917 G6: the open 3x3x3 cube -- built only to verify the "
                          "partition rule against the memo's own six lists; NOT re-run")


# --------------------------------------------- THE NEW DEGREE-5 GEOMETRIES ---
def geom_star6():
    """H1: K_{1,5}.  Pure pointer degree 5 -- no depth, no loops, singleton fragments."""
    sites = ["S"] + ["a%d" % i for i in range(1, 6)]
    bonds = [("S", "a%d" % i) for i in range(1, 6)]
    return build_geometry("H1", "star6", sites, bonds, "S", lambda c: c, None, "star",
                          "NEW: K_{1,5} -- pure degree 5, depth 1, zero loops, every "
                          "fragment a single site.  The degree-5 analogue of 917's G2.")


def geom_tree16():
    """H2: the 917 tree family's degree-5 member (all five branches of depth 2)."""
    return geom_tree(5)


def geom_tree10d5():
    """H3: centre + 5 branches, EXACTLY two of depth 2 (b0, b1); b2, b3, b4 leaves."""
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
                          "NEW: centre + 5 branches, EXACTLY two of depth 2 (b0 and b1 "
                          "carry two children each; b2, b3, b4 are leaves).  10 sites -- "
                          "the same site count as 917's degree-3 tree10, so n is held "
                          "fixed while degree moves 3 -> 5.")


def geom_cubeminus10():
    """H4: 917's G5 cubeminus11 with the -z face deleted -- degree 6 -> 5 at fixed loops."""
    faces = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1)]
    edges = [(1, 1, 0), (1, -1, 0), (-1, 1, 0), (-1, -1, 0)]
    sites = [(0, 0, 0)] + faces + edges
    bonds = [(a, b) for ia, a in enumerate(sites) for b in sites[ia + 1:]
             if sum(abs(a[k] - b[k]) for k in range(3)) == 1]
    return build_geometry("H4", "cubeminus10", sites, bonds, (0, 0, 0), _axis_label,
                          cube_tiebreak, 3,
                          "NEW: 917's G5 cubeminus11 with the -z pendant face DELETED -- "
                          "centre + 5 faces + the 4 z=0 edges.  A controlled degree "
                          "6 -> 5 deletion holding the loop number at 4: the loop test "
                          "at the threshold.")


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
    """The frozen class-product preparation: pointer and its neighbours +X, all
    other sites +Z."""
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
    """Route B: exp(-iHt) by a scaling-and-marching Taylor propagator.

    Each grid interval is split into substeps with ||H|| h <= hbound and the
    substep exponential is summed to convergence; the truncation remainder is
    bounded rigorously by (||H|| h)^(p+1) / (p+1)!.  Algorithmically disjoint
    from route A (no Bessel functions, no three-term recurrence).
    """
    A = float(np.abs(diag).max() + lam * n)
    mv = _matvec_factory(diag, n, lam)
    psi = psi0.astype(np.complex128).copy()
    outs = []
    tprev = 0.0
    nsub = 0
    nmv = 0
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
                worst_rem = max(worst_rem,
                                float((A * h) ** (p + 1) / math.gamma(p + 2)))
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
    """Reduced density matrix of the ordered site list (site 0 = most significant)."""
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
    """chi_Z(S:F) from the joint (S,F) state; S is the leading factor."""
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
    """C_ab on the Z_S-dephased state: sum_z p_z [S(a)+S(b)-S(ab)]."""
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


def r_ind(labels, chi, excess, H, C, delta):
    """Largest pairwise-independent certifying subset; ties -> lexicographically
    first in the declared label order."""
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
    """||[H,O]||_F / (||H||_F ||O - Tr(O)I/d||_F), closed form (the frozen memo)."""
    den = np.sqrt(float(nbonds) + n * lam * lam)
    out = {}
    for deg in sorted(set(degrees.values())):
        out[str(deg)] = {"Z": 2.0 * lam / den, "X": 2.0 * np.sqrt(deg) / den,
                         "Y": 2.0 * np.sqrt(deg + lam * lam) / den}
    return out


# ============================================================= measurement ===
def measure(g, states, times):
    """The full frozen observable set on a list of evolved states."""
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
        # X-declared-pointer demolition control
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
    """The frozen memo's xi_reg with Manhattan shell read as graph-distance shell."""
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
    x_ok = not any(r["x_control"]["r_ind_ge2_possible"]
                   for r in rows if r["jt"] <= DEADLINE_JT + 1e-12)
    if ev is None:
        best_C = min((min(r["C_ab"].values()) for r in rows), default=None)
        any_content = any(len(r["singleton_passes"]["%.2f" % delta]) >= 2 for r in rows)
        reason = ("content-gate: fewer than two fragments ever reach (1-delta)H with "
                  "0.02-bit excess" if not any_content else
                  "independence-gate: two or more fragments reach content but every "
                  "eligible pair exceeds C_ab = 0.02 bit")
        return {"verdict": "NO", "reason": reason, "event": None,
                "min_C_ab_over_grid": best_C, "x_control_ok": x_ok,
                "commutator_ordering_ok": comm_ok}
    if not ev["by_deadline"]:
        return {"verdict": "NO", "reason": "late: first R_ind>=2 after the Jt<=1 deadline",
                "event": ev, "x_control_ok": x_ok, "commutator_ordering_ok": comm_ok}
    if not ev["persists"]:
        return {"verdict": "NO", "reason": "persistence: fewer than three consecutive "
                                           "certification samples with R_ind>=2",
                "event": ev, "x_control_ok": x_ok, "commutator_ordering_ok": comm_ok}
    if ev["pointer_tv_drift"] > DRIFT_MAX:
        return {"verdict": "NO", "reason": "pointer drift exceeds 0.10 at the event",
                "event": ev, "x_control_ok": x_ok, "commutator_ordering_ok": comm_ok}
    if not (x_ok and comm_ok):
        return {"verdict": "NO", "reason": "CHECK-02 pointer demolition control",
                "event": ev, "x_control_ok": x_ok, "commutator_ordering_ok": comm_ok}
    return {"verdict": "YES", "reason": None, "event": ev, "x_control_ok": x_ok,
            "commutator_ordering_ok": comm_ok}


# =========================================================== symmetry gate ===
def declared_symmetries(g):
    """Explicit site permutations declared per geometry; each is VERIFIED to be a
    bond automorphism fixing the pointer and preserving the preparation classes."""
    key, idx, coords = g["key"], g["idx"], g["coords"]
    out = {}
    if key == "G1":
        out["reflect-x"] = {idx[c]: idx[(-c[0], 0, 0)] for c in coords}
    elif key in ("G2", "H1"):
        nl = g["n"] - 1
        cyc = {"S": "S"}
        for i in range(1, nl + 1):
            cyc["a%d" % i] = "a%d" % (i % nl + 1)
        out["leaf-cycle"] = {idx[c]: idx[cyc[c]] for c in coords}
    elif key in ("G3a", "G3b", "H2"):
        nb = (g["n"] - 1) // 3
        mp = {"S": "S"}
        for b in range(nb):
            mp["b%d" % b] = "b%d" % ((b + 1) % nb)
            for k in range(2):
                mp["b%dg%d" % (b, k)] = "b%dg%d" % ((b + 1) % nb, k)
        out["branch-cycle"] = {idx[c]: idx[mp[c]] for c in coords}
        mp2 = {c: c for c in coords}
        for b in range(nb):
            mp2["b%dg0" % b] = "b%dg1" % b
            mp2["b%dg1" % b] = "b%dg0" % b
        out["kid-swap"] = {idx[c]: idx[mp2[c]] for c in coords}
    elif key == "H3":
        # deep pair (b0,b1) swap, carrying children
        mp = {c: c for c in coords}
        mp["b0"], mp["b1"] = "b1", "b0"
        for k in range(2):
            mp["b0g%d" % k] = "b1g%d" % k
            mp["b1g%d" % k] = "b0g%d" % k
        out["deep-pair-swap"] = {idx[c]: idx[mp[c]] for c in coords}
        # shallow triple (b2,b3,b4) cycle
        mp = {c: c for c in coords}
        for b in (2, 3, 4):
            mp["b%d" % b] = "b%d" % (2 + (b - 2 + 1) % 3)
        out["shallow-cycle"] = {idx[c]: idx[mp[c]] for c in coords}
        # simultaneous child swap inside both deep branches
        mp = {c: c for c in coords}
        for b in (0, 1):
            mp["b%dg0" % b] = "b%dg1" % b
            mp["b%dg1" % b] = "b%dg0" % b
        out["kid-swap"] = {idx[c]: idx[mp[c]] for c in coords}
    elif key in ("G4", "G5", "H4"):
        for ax, nm in ((0, "x"), (1, "y"), (2, "z")):
            m = {}
            ok = True
            for c in coords:
                d = list(c)
                d[ax] = -d[ax]
                if tuple(d) not in idx:
                    ok = False
                    break
                m[idx[c]] = idx[tuple(d)]
            if ok:
                out["reflect-%s" % nm] = m
    return out


def verify_symmetries(g):
    bonds = set(g["bonds"])
    S, rec = g["S"], set(g["recording"])
    frag_of = {i: L for L in g["labels"] for i in g["frags"][L]}
    res, orbits = {}, {}
    for name, p in declared_symmetries(g).items():
        if sorted(p.values()) != list(range(g["n"])):
            die("symmetry:%s:%s not a permutation" % (g["key"], name))
        if p[S] != S:
            die("symmetry:%s:%s moves the pointer" % (g["key"], name))
        if {p[i] for i in rec} != rec:
            die("symmetry:%s:%s does not preserve the recording class" % (g["key"], name))
        if {tuple(sorted((p[a], p[b]))) for (a, b) in bonds} != bonds:
            die("symmetry:%s:%s is not a bond automorphism" % (g["key"], name))
        fm = {}
        for L in g["labels"]:
            img = {frag_of[p[i]] for i in g["frags"][L]}
            if len(img) != 1:
                die("symmetry:%s:%s splits fragment %s" % (g["key"], name, L))
            fm[L] = img.pop()
        res[name] = {"fragment_map": fm, "verified_automorphism": True,
                     "fixes_pointer": True, "preserves_preparation_classes": True}
        for L, M in fm.items():
            a = orbits.setdefault(L, {L})
            b = orbits.setdefault(M, {M})
            u = a | b
            for q in u:
                orbits[q] = u
    seen, olist = set(), []
    for L in g["labels"]:
        o = frozenset(orbits.get(L, {L}))
        if o not in seen:
            seen.add(o)
            olist.append(sorted(o))
    return res, olist


def symmetry_residual(rows, orbits):
    m = 0.0
    for r in rows:
        for o in orbits:
            if len(o) > 1:
                vals = [r["chi"][L] for L in o]
                m = max(m, max(vals) - min(vals))
    return m


def star_orbit_reduction_exactness(g, lam, times, psi0, diag):
    """Verify orbit reduction EXACTNESS on the degree-5 star (the 914/917 pattern)."""
    n = g["n"]
    leaves = [i for i in range(n) if i != g["S"]]
    nl = len(leaves)
    cols = []
    idx = np.arange(1 << n, dtype=np.int64)
    pop = np.zeros(1 << n, dtype=np.int64)
    for i in leaves:
        pop += (idx >> np.int64(i)) & np.int64(1)
    sbit = (idx >> np.int64(g["S"])) & np.int64(1)
    for sv in (0, 1):
        for k in range(nl + 1):
            v = np.zeros(1 << n, dtype=np.float64)
            sel = (pop == k) & (sbit == sv)
            v[sel] = 1.0
            v /= np.linalg.norm(v)
            cols.append(v)
    V = np.stack(cols, axis=1)
    d = 1 << n
    H = np.zeros((d, d), dtype=np.float64)
    H[np.arange(d), np.arange(d)] = diag
    for i in range(n):
        j = np.arange(d, dtype=np.int64) ^ (1 << i)
        H[np.arange(d), j] -= lam
    Hr = V.T @ H @ V
    closure = float(np.abs(H @ V - V @ Hr).max())
    w, U = np.linalg.eigh(Hr)
    c0 = U.T @ (V.T @ psi0)
    proj_err = float(np.abs(psi0 - V @ (V.T @ psi0)).max())
    wf, Vf = np.linalg.eigh(H)
    cf = Vf.T @ psi0
    devs = []
    for t in times:
        red = V @ (U @ (np.exp(-1j * w * t) * c0))
        full = Vf @ (np.exp(-1j * wf * t) * cf)
        devs.append(float(np.abs(red - full).max()))
    return {"instance": g["key"] + "/" + g["name"], "reduced_dim": V.shape[1],
            "full_dim": d, "sector_closure_max_abs": closure,
            "preparation_projection_error": proj_err,
            "max_state_deviation_reduced_vs_full": max(devs),
            "exact": bool(closure <= 1e-12 and proj_err <= 1e-12 and max(devs) <= 1e-12)}


# ================================================================ helpers ====
def persistence_profile(rows, delta=HEADLINE_DELTA):
    """How marginal is the persistence flag on this cell?

    The 917 checker's sharpest correction was that three of its four lambda = 0.10
    NO cells were ONE-SAMPLE persistence misses, the tightest by 0.00078 bits of
    C_ab.  Any degree threshold read off that split is therefore soft.  This
    function measures the same quantity on every cell, so the softness travels
    with the number instead of being asserted about it.
    """
    key = "%.2f" % delta

    def sample_of(r):
        """R_ind >= 2 needs TWO content-passing fragments whose OWN pair is under the
        independence gate, so the binding pair is the cheapest pair AMONG THE CONTENT
        PASSES -- not the cheapest pair overall (the 917 checker's G4 lesson)."""
        passes = r["singleton_passes"][key]
        pairs = {k: v for k, v in r["C_ab"].items()
                 if all(p in passes for p in k.split("|"))}
        binding_C = min(pairs.values()) if pairs else None
        return {"jt": r["jt"], "r_ind": r["r_ind"][key],
                "n_content_passes": len(passes),
                "content_margin_bits": max(r["chi"].values()) - (1.0 - delta) * r["H_Z"],
                "min_C_ab_over_all_pairs": min(r["C_ab"].values()),
                "binding_pair_C_ab_among_content_passes": binding_C,
                "independence_margin_bits": (None if binding_C is None
                                             else INDEP_MAX - binding_C),
                "binding_gate": ("content" if len(passes) < 2 else "independence")}

    idx = next((i for i, r in enumerate(rows) if r["r_ind"][key] >= 2), None)
    if idx is None:
        live = [sample_of(r) for r in rows if len(r["singleton_passes"][key]) >= 2
                and r["jt"] <= DEADLINE_JT + 1e-12]
        best = min([s["binding_pair_C_ab_among_content_passes"] for s in live
                    if s["binding_pair_C_ab_among_content_passes"] is not None],
                   default=None)
        return {"has_event": False, "run": 0, "needed": PERSIST_N, "persists": False,
                "misses_by_one_sample": False, "clears_by_one_sample": False,
                "margin_at_the_third_sample_bits": None,
                "deficit_at_the_first_failing_sample_bits": None,
                "rows_with_two_or_more_content_passes": [s["jt"] for s in live],
                "best_binding_pair_C_ab_on_those_rows": best,
                "shortfall_bits": (best - INDEP_MAX) if best is not None else None,
                "failure_mode": ("empty content window" if best is None
                                 else "content window closed by conditional dependence")}
    run = 0
    for r in rows[idx:]:
        if r["r_ind"][key] >= 2:
            run += 1
        else:
            break
    samples = [sample_of(r) for r in rows[idx:idx + run + 1]]
    last_ok = samples[run - 1] if run >= 1 else None
    first_bad = samples[run] if len(samples) > run else None
    third = samples[PERSIST_N - 1] if run >= PERSIST_N else None
    return {"has_event": True, "first_jt": rows[idx]["jt"], "run": run,
            "needed": PERSIST_N, "persists": bool(run >= PERSIST_N),
            "samples": samples,
            "margin_at_the_last_certifying_sample_bits":
                (last_ok["independence_margin_bits"] if last_ok else None),
            "margin_at_the_third_sample_bits":
                (third["independence_margin_bits"] if third else None),
            "first_failing_sample_jt": (first_bad["jt"] if first_bad else None),
            "first_failing_sample_binding_gate": (first_bad["binding_gate"] if first_bad
                                                  else None),
            "deficit_at_the_first_failing_sample_bits":
                (None if (first_bad is None
                          or first_bad["binding_pair_C_ab_among_content_passes"] is None)
                 else first_bad["binding_pair_C_ab_among_content_passes"] - INDEP_MAX),
            "misses_by_one_sample": bool(run == PERSIST_N - 1),
            "clears_by_one_sample": bool(run == PERSIST_N)}


def cell_of(g, diag, psi0, lam, rows):
    """The per-cell summary the ladder consumes."""
    cf = centered_frobenius(lam, g["n"], len(g["bonds"]), g["degrees"])
    comm_ok = max(v["Z"] for v in cf.values()) < min(v["X"] for v in cf.values())
    xi = xi_reg_of(rows)
    v = {d: verdict_of(rows, d, comm_ok) for d in DELTAS}
    return {"centered_frobenius": cf, "commutator_ordering_ok": bool(comm_ok),
            "xi_reg": xi,
            "verdicts_by_delta": {"%.2f" % d: v[d] for d in DELTAS},
            "max_r_ind_over_window": max(r["r_ind"]["%.2f" % HEADLINE_DELTA] for r in rows),
            "headline": v[HEADLINE_DELTA]}


def run_route_A(g, diag, psi0, lam):
    outs, prop = chebyshev(psi0, diag, g["n"], lam, T_EXEC)
    rows, mach = measure(g, outs, T_EXEC)
    return rows, mach, prop


# ================================================================== main =====
def main():
    pins = verify_pins()
    memo = open(os.path.join(ROOT, PARENT_MEMO), "rb").read().decode("utf-8")
    frozen = verify_frozen_constants(memo)
    const_x = cross_check_917_constants(frozen)
    d1_text, d1_prov = recover_d1_note()
    head = git(["rev-parse", "--short=10", "HEAD"]).stdout.decode().strip()
    r917 = json.load(open(os.path.join(ROOT, C917_RECEIPT)))
    r917c = json.load(open(os.path.join(ROOT, C917_CHECK_RECEIPT)))

    mach_all = {"norm": 0.0, "hermiticity": 0.0, "negativity": 0.0,
                "entropy_bound": 0.0, "symmetry": 0.0, "t0_anchor": 0.0,
                "cheby_tail": 0.0, "taylor_remainder": 0.0,
                "route_AB_max_dev": 0.0, "route_AC_max_dev": 0.0, "determinism": 0.0}

    # ============================================ restriction gate 1: the rule ==
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

    # ================== restriction gate 2: Cycle 917 reproduced value-for-value ==
    C917_BUILD = {"G1": geom_chain9, "G2": geom_star7, "G3a": lambda: geom_tree(3),
                  "G3b": lambda: geom_tree(4), "G4": geom_plaquette9,
                  "G5": geom_cubeminus11}
    restrict = {"per_cell": {}, "row_level_max_abs_dev": {"chi": 0.0, "C_ab": 0.0,
                                                          "theta_A": 0.0, "H_Z": 0.0},
                "mismatches": [], "cells_checked": 0, "rows_compared": 0,
                "extension_field_cells": {}}
    c917_rows_cache = {}
    for key in C917_KEYS:
        g = C917_BUILD[key]()
        pub = r917["geometries"][key]
        if set(pub["sites"]) != set(g["sites"]):
            restrict["mismatches"].append("%s:site-set" % key)
        if {tuple(sorted(b)) for b in pub["bonds"]} != \
           {tuple(sorted((g["sites"][a], g["sites"][b]))) for (a, b) in g["bonds"]}:
            restrict["mismatches"].append("%s:bond-set" % key)
        for L, v in pub["partition"].items():
            if set(v) != {g["sites"][i] for i in g["frags"][L]}:
                restrict["mismatches"].append("%s:partition:%s" % (key, L))
        if pub["stats"] != g["stats"]:
            restrict["mismatches"].append("%s:stats" % key)
        diag = build_diag(g["n"], g["bonds"])
        psi0 = prep_state(g["n"], set([g["S"]] + g["recording"]))
        for lam in FROZEN_LAMBDAS:
            lk = "%g" % lam
            rows, mach, prop = run_route_A(g, diag, psi0, lam)
            c917_rows_cache[(key, lk)] = rows
            mach_all["cheby_tail"] = max(mach_all["cheby_tail"], prop["tail_bound"])
            for k in mach:
                mach_all[k] = max(mach_all[k], mach[k])
            cell = cell_of(g, diag, psi0, lam, rows)
            want = r917["ladder"]["%s@%s" % (key, lk)]
            got = cell["headline"]
            bad = []
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
            # row-by-row against the 917 receipt's own published rows
            pubrows = {r["jt"]: r for r in pub["lambdas"][lk]["rows"]}
            for r in rows:
                q = pubrows.get(r["jt"])
                if q is None:
                    bad.append("row-missing@%.1f" % r["jt"])
                    continue
                restrict["rows_compared"] += 1
                for L in r["chi"]:
                    restrict["row_level_max_abs_dev"]["chi"] = max(
                        restrict["row_level_max_abs_dev"]["chi"], abs(r["chi"][L] - q["chi"][L]))
                for kk, vv in r["C_ab"].items():
                    restrict["row_level_max_abs_dev"]["C_ab"] = max(
                        restrict["row_level_max_abs_dev"]["C_ab"], abs(vv - q["C_ab"][kk]))
                restrict["row_level_max_abs_dev"]["theta_A"] = max(
                    restrict["row_level_max_abs_dev"]["theta_A"],
                    abs(r["theta_A"] - q["theta_A"]))
                restrict["row_level_max_abs_dev"]["H_Z"] = max(
                    restrict["row_level_max_abs_dev"]["H_Z"], abs(r["H_Z"] - q["H_Z"]))
                if r["r_ind"] != q["r_ind"]:
                    bad.append("r_ind-ledger@%.1f" % r["jt"])
            restrict["cells_checked"] += 1
            restrict["per_cell"]["%s@%s" % (key, lk)] = {
                "verdict": got["verdict"], "matches_917": not bad,
                "discrepancies": bad,
                "first_jt": (ev or {}).get("jt"), "theta_A": (ev or {}).get("theta_A"),
                "max_r_ind": cell["max_r_ind_over_window"],
                "xi_reg": cell["xi_reg"]["xi_reg"]}
            if bad:
                restrict["mismatches"].append("%s@%s:%s" % (key, lk, ",".join(bad)))
        # the 917 CHECKER's 0.075 ceiling verdict, reproduced here
        rows75, mach75, prop75 = run_route_A(g, diag, psi0, EXTENSION_LAMBDA)
        c917_rows_cache[(key, "0.075")] = rows75
        mach_all["cheby_tail"] = max(mach_all["cheby_tail"], prop75["tail_bound"])
        for k in mach75:
            mach_all[k] = max(mach_all[k], mach75[k])
        v75 = verdict_of(rows75, HEADLINE_DELTA,
                         cell_of(g, diag, psi0, EXTENSION_LAMBDA,
                                 rows75)["commutator_ordering_ok"])["verdict"]
        want75 = r917c["threshold_attack"]["lambda_boundary_diagnostic_NON_CLAIM"][key][
            "probe"]["0.075"]
        restrict["extension_field_cells"]["%s@0.075" % key] = {
            "recomputed_here": v75, "pinned_917_checker_probe": want75,
            "agrees": bool(v75 == want75)}
        if v75 != want75:
            restrict["mismatches"].append("%s@0.075:%s!=%s" % (key, v75, want75))
    if restrict["mismatches"]:
        die("restriction:917-not-reproduced %s" % restrict["mismatches"][:6])
    for k, v in restrict["row_level_max_abs_dev"].items():
        if v > RESTRICT_TOL:
            die("restriction:row-deviation %s=%.3g" % (k, v))

    # ================================================ the degree-5 measurement ==
    NEW_BUILD = {"H1": geom_star6, "H2": geom_tree16, "H3": geom_tree10d5,
                 "H4": geom_cubeminus10}
    per_geom, ladder, reduction = {}, {}, None
    new_geoms = {}
    for key in NEW_KEYS:
        g = NEW_BUILD[key]()
        new_geoms[key] = g
        if g["stats"]["pointer_degree"] != 5:
            die("degree-five:%s pointer_degree=%d" % (key, g["stats"]["pointer_degree"]))
        n, S = g["n"], g["S"]
        diag = build_diag(n, g["bonds"])
        psi0 = prep_state(n, set([S] + g["recording"]))
        if abs(float(np.vdot(psi0, psi0).real) - 1.0) > 1e-12:
            die("prep:norm %s" % key)
        syms, orbits = verify_symmetries(g)
        use_dense = (n <= 12)
        per_geom[key] = {
            "declaration": {k: g[k] for k in ("key", "name", "note", "dim", "n", "pointer")},
            "sites": g["sites"],
            "bonds": [[g["sites"][a], g["sites"][b]] for (a, b) in g["bonds"]],
            "recording_sites": [g["sites"][i] for i in g["recording"]],
            "partition": {L: [g["sites"][i] for i in g["frags"][L]] for L in g["labels"]},
            "partition_ties_resolved": g["ties"],
            "tie_break_source": ("the frozen memo's tie-break algorithm, applied VERBATIM "
                                 "in cube coordinates" if g["ties"] else
                                 "no ties arise: every non-recording site has a unique "
                                 "nearest recording site"),
            "shells": {str(k): [g["sites"][i] for i in v]
                       for k, v in sorted(g["shells"].items())},
            "stats": g["stats"],
            "symmetries": {k: v["fragment_map"] for k, v in syms.items()},
            "fragment_orbits": orbits,
            "route": ("FULL SPACE, dimension 2^%d = %d; route A = Chebyshev with a rigorous "
                      "Bessel tail bound, route B = scaling-and-marching Taylor with a "
                      "rigorous factorial remainder bound%s.  No orbit reduction is used; "
                      "its exactness is demonstrated separately on H1."
                      % (n, 1 << n,
                         ", route C = exact dense eigendecomposition" if use_dense else
                         " (dense eigendecomposition is not executed at 2^16; the two "
                         "matrix-free routes are algorithmically disjoint)")),
            "lambdas": {}}
        for lam in LAMBDAS:
            lk = "%g" % lam
            rows, mach, propA = run_route_A(g, diag, psi0, lam)
            mach_all["cheby_tail"] = max(mach_all["cheby_tail"], propA["tail_bound"])
            # determinism: recompute route A in-process, digests must match
            rows2, _, _ = run_route_A(g, diag, psi0, lam)
            d1 = sha256_bytes(json.dumps(rows, sort_keys=True, default=repr).encode())
            d2 = sha256_bytes(json.dumps(rows2, sort_keys=True, default=repr).encode())
            if d1 != d2:
                die("determinism:%s:%g" % (key, lam))
            # route B (independent algorithm)
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
                        die("route-cross-AC:r_ind %s %g t=%.1f" % (key, lam, ra["jt"]))
                mach_all["route_AC_max_dev"] = max(mach_all["route_AC_max_dev"], devC)
            for k in mach:
                mach_all[k] = max(mach_all[k], mach[k])
            for k in machB:
                mach_all[k] = max(mach_all[k], machB[k])
            mach_all["symmetry"] = max(mach_all["symmetry"], symmetry_residual(rows, orbits))
            cell = cell_of(g, diag, psi0, lam, rows)
            per_geom[key]["lambdas"][lk] = {
                "field_status": ("FROZEN certified field" if lam in FROZEN_LAMBDAS
                                 else "DECLARED DESIGN EXTENSION (beyond the frozen field "
                                      "set; see deviations)"),
                "chebyshev": propA, "taylor": propB, "dense": propC,
                "route_AB_max_abs_dev": devB, "route_AC_max_abs_dev": devC,
                "determinism_digest": d1,
                "centered_frobenius": cell["centered_frobenius"],
                "commutator_ordering_ok": cell["commutator_ordering_ok"],
                "xi_reg": cell["xi_reg"],
                "verdicts_by_delta": cell["verdicts_by_delta"],
                "max_r_ind_over_window": cell["max_r_ind_over_window"],
                "rows": rows,
            }
            hv = cell["headline"]
            ladder[(key, lk)] = {
                "geometry": g["name"], "stats": g["stats"],
                "verdict": hv["verdict"], "reason": hv["reason"], "event": hv["event"],
                "xi_reg": cell["xi_reg"]["xi_reg"],
                "max_r_ind": cell["max_r_ind_over_window"],
                "verdict_by_delta": {"%.2f" % d: cell["verdicts_by_delta"]["%.2f" % d]["verdict"]
                                     for d in DELTAS},
                "source": "MEASURED here (Cycle 919)",
                "field_status": ("frozen" if lam in FROZEN_LAMBDAS else "design-extension"),
            }
        if key == "H1":
            reduction = star_orbit_reduction_exactness(g, LAMBDAS[0], T_EXEC, psi0, diag)
            if not reduction["exact"]:
                die("orbit-reduction:not-exact")

    # ============================== the 917 rows, re-verified, into the ladder ==
    C917_STATS = r917["branching_statistics"]
    for key in C917_KEYS:
        for lam in FROZEN_LAMBDAS:
            lk = "%g" % lam
            w = r917["ladder"]["%s@%s" % (key, lk)]
            ladder[(key, lk)] = dict(w, source="PINNED 917 receipt, re-verified "
                                               "value-for-value here",
                                     field_status="frozen")
        rows75 = c917_rows_cache[(key, "0.075")]
        g = C917_BUILD[key]()
        diag = build_diag(g["n"], g["bonds"])
        psi0 = prep_state(g["n"], set([g["S"]] + g["recording"]))
        cell = cell_of(g, diag, psi0, EXTENSION_LAMBDA, rows75)
        hv = cell["headline"]
        ladder[(key, "0.075")] = {
            "geometry": g["name"], "stats": g["stats"], "verdict": hv["verdict"],
            "reason": hv["reason"], "event": hv["event"],
            "xi_reg": cell["xi_reg"]["xi_reg"],
            "max_r_ind": cell["max_r_ind_over_window"],
            "verdict_by_delta": {"%.2f" % d: cell["verdicts_by_delta"]["%.2f" % d]["verdict"]
                                 for d in DELTAS},
            "source": "MEASURED here (Cycle 919), agreeing with the pinned 917 checker probe",
            "field_status": "design-extension"}
    # G6 (the cube) at the two frozen fields, imported through 917's own import
    for lam in FROZEN_LAMBDAS:
        lk = "%g" % lam
        ladder[("G6", lk)] = dict(r917["ladder"]["G6@%s" % lk],
                                  source="IMPORTED via the pinned 917 receipt (which "
                                         "imported it from the pinned 914 receipt); not "
                                         "recomputed in either cycle",
                                  field_status="frozen")

    STATS = {k: new_geoms[k]["stats"] for k in NEW_KEYS}
    STATS.update({k: C917_STATS[k] for k in C917_STATS})
    # the refined ladder is ordered by pointer degree -- the axis the block measures
    ORDER = sorted(set(C917_KEYS + NEW_KEYS + ["G6"]),
                   key=lambda k: (STATS[k]["pointer_degree"], k))

    # =========================================== the graded field-ceiling probe ==
    # DECLARED NON-CLAIM DIAGNOSTIC outside {0.05, 0.075, 0.10}: the 917 checker's
    # probe grid carried over verbatim so the ceiling table is commensurable.
    ceiling = {}
    for key in NEW_KEYS:
        g = new_geoms[key]
        diag = build_diag(g["n"], g["bonds"])
        psi0 = prep_state(g["n"], set([g["S"]] + g["recording"]))
        executed = {"%g" % L for L in LAMBDAS}
        probe = {}
        for lam in PROBE_LAMBDAS:
            lk = "%g" % lam
            if lk in executed:
                probe[lk] = ladder[(key, lk)]["verdict"]
                continue
            rows, mach, prop = run_route_A(g, diag, psi0, lam)
            mach_all["cheby_tail"] = max(mach_all["cheby_tail"], prop["tail_bound"])
            for k in mach:
                mach_all[k] = max(mach_all[k], mach[k])
            cf = centered_frobenius(lam, g["n"], len(g["bonds"]), g["degrees"])
            co = max(v["Z"] for v in cf.values()) < min(v["X"] for v in cf.values())
            probe[lk] = verdict_of(rows, HEADLINE_DELTA, co)["verdict"]
        yes = [float(k) for k, v in probe.items() if v == "YES"]
        no = [float(k) for k, v in probe.items() if v == "NO"]
        hi = max(yes) if yes else None
        above = [l for l in no if hi is not None and l > hi]
        ceiling[key] = {"probe": probe, "certifies_up_to": hi,
                        "bracket": [hi, min(above)] if (hi is not None and above) else None,
                        "source": "MEASURED here (Cycle 919)"}
    for key in C917_KEYS:
        b = r917c["threshold_attack"]["lambda_boundary_diagnostic_NON_CLAIM"][key]
        ceiling[key] = {"probe": b["probe"], "certifies_up_to": b["certifies_up_to"],
                        "bracket": b["bracket"],
                        "source": "PINNED 917 checker receipt; its 0.075 cell independently "
                                  "reproduced here in the restriction gate"}

    ceiling_by_degree = {}
    for key, v in ceiling.items():
        ceiling_by_degree.setdefault(str(STATS[key]["pointer_degree"]), set()).add(
            v["certifies_up_to"])
    ceiling_by_degree = {k: sorted(v) for k, v in sorted(ceiling_by_degree.items(),
                                                        key=lambda kv: int(kv[0]))}
    ceiling_monotone = all(
        (ceiling[a]["certifies_up_to"] or 0) <= (ceiling[b]["certifies_up_to"] or 0)
        for a in ceiling for b in ceiling
        if STATS[a]["pointer_degree"] < STATS[b]["pointer_degree"])

    # ===================================== how soft is the located threshold? ===
    # Every geometry's persistence profile at the two fields where the split lives,
    # so the softness the 917 checker found travels with the located bracket.
    persistence = {}
    for lk in ("0.075", "0.1"):
        tab = {}
        for gk in ORDER:
            if gk in NEW_KEYS:
                rows = per_geom[gk]["lambdas"][lk]["rows"]
            elif (gk, lk) in c917_rows_cache:
                rows = c917_rows_cache[(gk, lk)]
            else:
                continue      # G6 is imported; no rows exist in either cycle
            p = persistence_profile(rows)
            p["pointer_degree"] = STATS[gk]["pointer_degree"]
            p["verdict"] = ladder[(gk, lk)]["verdict"]
            tab[gk] = p
        persistence[lk] = tab
    soft = {
        "one_sample_misses_at_0.10": sorted(g for g, p in persistence["0.1"].items()
                                            if p.get("misses_by_one_sample")),
        "one_sample_clears_at_0.10": sorted(g for g, p in persistence["0.1"].items()
                                            if p.get("clears_by_one_sample")),
        "tightest_NO_deficit_bits_at_0.10": min(
            [p["deficit_at_the_first_failing_sample_bits"]
             for p in persistence["0.1"].values()
             if p.get("misses_by_one_sample")
             and p.get("deficit_at_the_first_failing_sample_bits") is not None] or [None]),
        "tightest_YES_margin_bits_at_0.10": min(
            [p["margin_at_the_third_sample_bits"] for p in persistence["0.1"].values()
             if p["verdict"] == "YES" and p.get("margin_at_the_third_sample_bits")
             is not None] or [None]),
        "gate_units": "bits of C_ab on the cheapest fragment pair that BOTH pass the "
                      "content gate, measured on the third certification sample (the one "
                      "the persistence flag turns on)",
    }
    soft["reading"] = (
        "the pointer-degree threshold at lambda = 0.10 is a PERSISTENCE boundary, not a "
        "certification cliff.  Every geometry of degree 3 and above reaches R_ind >= 2 by "
        "the Jt <= 1 deadline; what separates them is whether the certification survives "
        "three consecutive samples.  It is located AND it is narrow: the tightest NO "
        "(%s) misses the third sample by %s bits of C_ab on its binding pair, and the "
        "tightest YES (%s) clears the same sample by %s bits.  A gate moved by ~2e-3 bits "
        "would move the bracket.  This is the 917 checker's softness finding, measured "
        "rather than asserted."
        % (min(persistence["0.1"], key=lambda g: (
               persistence["0.1"][g]["deficit_at_the_first_failing_sample_bits"]
               if persistence["0.1"][g].get("misses_by_one_sample")
               and persistence["0.1"][g]["deficit_at_the_first_failing_sample_bits"]
               is not None else 1e9)),
           soft["tightest_NO_deficit_bits_at_0.10"],
           min(persistence["0.1"], key=lambda g: (
               persistence["0.1"][g]["margin_at_the_third_sample_bits"]
               if persistence["0.1"][g]["verdict"] == "YES"
               and persistence["0.1"][g].get("margin_at_the_third_sample_bits")
               is not None else 1e9)),
           soft["tightest_YES_margin_bits_at_0.10"]))

    # ====================================================== THE Q2 STATEMENT ====
    deg5_at_010 = {k: ladder[(k, "0.1")]["verdict"] for k in NEW_KEYS}
    deg5_at_0075 = {k: ladder[(k, "0.075")]["verdict"] for k in NEW_KEYS}
    deg5_at_005 = {k: ladder[(k, "0.05")]["verdict"] for k in NEW_KEYS}
    all_yes_010 = all(v == "YES" for v in deg5_at_010.values())
    all_no_010 = all(v == "NO" for v in deg5_at_010.values())
    if all_yes_010:
        located = {"threshold_bracket_at_lambda_0.10": [4, 5],
                   "reading": "degree 5 CERTIFIES at the frozen upper field: 5 behaves like "
                              "6, and the pointer-degree threshold at lambda = 0.10 is "
                              "located in (4, 5] -- one notch tighter than 917's (4, 6]."}
    elif all_no_010:
        located = {"threshold_bracket_at_lambda_0.10": [5, 6],
                   "reading": "degree 5 does NOT certify at the frozen upper field: 5 "
                              "behaves like 4, and the pointer-degree threshold at "
                              "lambda = 0.10 is located in (5, 6] -- one notch tighter "
                              "than 917's (4, 6]."}
    else:
        located = {"threshold_bracket_at_lambda_0.10": None,
                   "reading": "the four degree-5 geometries SPLIT at lambda = 0.10 (%s): "
                              "pointer degree alone does not decide the verdict at degree "
                              "5, and the bracket cannot be tightened by degree alone.  "
                              "The split itself is the finding; see the confound table."
                              % json.dumps(deg5_at_010, sort_keys=True)}
    located["softness_caveat"] = soft["reading"]
    located["one_sample_misses_at_0.10"] = soft["one_sample_misses_at_0.10"]
    located["one_sample_clears_at_0.10"] = soft["one_sample_clears_at_0.10"]
    located["identical_statistics_caveat"] = (
        "the partition rule makes exactly one fragment per pointer neighbour, so on this "
        "geometry family pointer_degree, max_degree, branch_count_at_pointer and "
        "n_fragments are the SAME NUMBER (the 917 checker's correction, carried forward).  "
        "'The threshold is in pointer degree' therefore means 'in the number of "
        "conditionally independent registers the partition makes available', and this "
        "block does not separate those readings either.")

    # the R_ind ceiling law at degree 5
    rlaw = {}
    for lk in ("0.05", "0.075", "0.1"):
        rows = {}
        for gk in ORDER:
            if (gk, lk) not in ladder:
                continue
            st = STATS[gk]
            rows[gk] = {"max_r_ind": ladder[(gk, lk)]["max_r_ind"],
                        "pointer_degree": st["pointer_degree"],
                        "loop_free": st["loop_free"],
                        "equals_pointer_degree":
                            bool(ladder[(gk, lk)]["max_r_ind"] == st["pointer_degree"])}
        rlaw[lk] = {
            "per_geometry": rows,
            "holds_on_loop_free": sorted(g for g in rows
                                         if STATS[g]["loop_free"] and rows[g]["equals_pointer_degree"]),
            "fails_on_loop_free": sorted(g for g in rows
                                         if STATS[g]["loop_free"] and not rows[g]["equals_pointer_degree"]),
            "holds_on_loopy": sorted(g for g in rows
                                     if not STATS[g]["loop_free"] and rows[g]["equals_pointer_degree"]),
            "fails_on_loopy": sorted(g for g in rows
                                     if not STATS[g]["loop_free"] and not rows[g]["equals_pointer_degree"]),
        }
    deg5_ceiling_law = {
        "prediction_from_917": "max R_ind over the window = pointer degree = 5",
        "per_cell": {"%s@%s" % (k, lk): {"max_r_ind": ladder[(k, lk)]["max_r_ind"],
                                         "equals_5": bool(ladder[(k, lk)]["max_r_ind"] == 5),
                                         "loop_free": STATS[k]["loop_free"]}
                     for k in NEW_KEYS for lk in ("0.05", "0.075", "0.1")},
        "holds_at_0.05_on_all_four": all(ladder[(k, "0.05")]["max_r_ind"] == 5
                                         for k in NEW_KEYS),
        "holds_at_0.05_on_loop_free": all(ladder[(k, "0.05")]["max_r_ind"] == 5
                                          for k in NEW_KEYS if STATS[k]["loop_free"]),
        "holds_at_0.10_on_loop_free": all(ladder[(k, "0.1")]["max_r_ind"] == 5
                                          for k in NEW_KEYS if STATS[k]["loop_free"]),
        "loopy_cells_at_0.10": {k: ladder[(k, "0.1")]["max_r_ind"] for k in NEW_KEYS
                                if not STATS[k]["loop_free"]},
    }

    # ============================= the degree-5 internal confound separation ====
    CONF = ["n_sites", "depth_eccentricity_from_pointer", "cyclomatic_number_loops",
            "components_of_G_minus_S", "n_bonds"]
    confound = {}
    for lk in ("0.05", "0.075", "0.1"):
        vs = {k: ladder[(k, lk)]["verdict"] for k in NEW_KEYS}
        agree = len(set(vs.values())) == 1
        confound[lk] = {
            "verdicts": vs,
            "all_four_agree": bool(agree),
            "held_fixed": {"pointer_degree": 5},
            "varied": {f: {k: STATS[k][f] for k in NEW_KEYS} for f in CONF},
            "reading": ("degree 5 is ISOLATED from system size (%d -> %d sites), depth "
                        "(%d -> %d), loops (%d -> %d) and fragment size at this field: every "
                        "one of the %d degree-5 geometries returns the same verdict"
                        % (min(STATS[k]["n_sites"] for k in NEW_KEYS),
                           max(STATS[k]["n_sites"] for k in NEW_KEYS),
                           min(STATS[k]["depth_eccentricity_from_pointer"] for k in NEW_KEYS),
                           max(STATS[k]["depth_eccentricity_from_pointer"] for k in NEW_KEYS),
                           min(STATS[k]["cyclomatic_number_loops"] for k in NEW_KEYS),
                           max(STATS[k]["cyclomatic_number_loops"] for k in NEW_KEYS),
                           len(NEW_KEYS))
                        if agree else
                        "the degree-5 set SPLITS at this field, so degree alone does not "
                        "decide it; the splitting feature is read off the varied column"),
        }

    # feature separation across the full ladder at each field
    FEATURES = ["max_degree", "pointer_degree", "components_of_G_minus_S",
                "depth_eccentricity_from_pointer", "cyclomatic_number_loops",
                "dimension", "n_sites", "n_fragments"]
    separation = {}
    for lk in ("0.05", "0.075", "0.1"):
        keys = [g for g in ORDER if (g, lk) in ladder]
        Y = [g for g in keys if ladder[(g, lk)]["verdict"] == "YES"]
        N = [g for g in keys if ladder[(g, lk)]["verdict"] == "NO"]
        sep = {}
        for f in FEATURES:
            yv = [STATS[g][f] for g in Y]
            nv = [STATS[g][f] for g in N]
            disjoint = bool(N and Y and not (set(map(str, yv)) & set(map(str, nv))))
            numeric = all(isinstance(v, (int, float)) for v in yv + nv)
            mono = bool(numeric and disjoint and (min(yv) > max(nv) or max(yv) < min(nv)))
            sep[f] = {"YES_values": yv, "NO_values": nv, "separates": disjoint,
                      "monotone_threshold": mono,
                      "bracket": ([max(nv), min(yv)] if mono and min(yv) > max(nv)
                                  else ([max(yv), min(nv)] if mono else None))}
        separation[lk] = {"YES": Y, "NO": N, "features": sep}

    # the no-go mechanism detector, carried over from 917
    xi_col = {gk: {lk: ladder[(gk, lk)]["xi_reg"] for lk in ("0.05", "0.075", "0.1")
                   if (gk, lk) in ladder} for gk in ORDER}
    xi_all_one = all(v <= 1 for d in xi_col.values() for v in d.values())

    def mechanism_flags(gk, lk):
        st, row = STATS[gk], ladder[(gk, lk)]
        f = []
        if row["verdict"] == "YES" and st["max_degree"] <= 2:
            f.append("NO-GO-STRUCTURAL-VIOLATION: R_ind>=2 certified on a geometry with no "
                     "branch point (max degree <= 2)")
        if row["verdict"] == "YES" and row["xi_reg"] <= 1:
            f.append("NO-GO-MECHANISM-INSUFFICIENT: R_ind>=2 certified while xi_reg <= 1 "
                     "link, the exact condition the recovered note gives as the d=1 "
                     "obstruction")
        return f

    flags = {"%s@%s" % (gk, lk): mechanism_flags(gk, lk)
             for gk in ORDER for lk in ("0.05", "0.075", "0.1")
             if (gk, lk) in ladder and mechanism_flags(gk, lk)}

    # C_ab at the certification window on the new geometries
    cwin = {}
    for lk in ("0.05", "0.075", "0.1"):
        d = {}
        for gk in NEW_KEYS:
            ev = ladder[(gk, lk)]["event"]
            if ev and ev.get("C_at_event"):
                d[gk] = {"min": min(ev["C_at_event"].values()),
                         "max": max(ev["C_at_event"].values()), "jt": ev["jt"]}
            else:
                rr = per_geom[gk]["lambdas"][lk]["rows"]
                i = next((j for j, r in enumerate(rr)
                          if len(r["singleton_passes"]["%.2f" % HEADLINE_DELTA]) >= 2), None)
                d[gk] = {"min": min(rr[i]["C_ab"].values()) if i is not None else None,
                         "max": max(rr[i]["C_ab"].values()) if i is not None else None,
                         "jt": rr[i]["jt"] if i is not None else None,
                         "note": "no certified event: values at the first row where two or "
                                 "more fragments pass the content gate"}
        cwin[lk] = d

    # ============================================== falsifier / outcome gates ==
    falsifier = {}
    # (a) planted certification on a REAL NO cell (917's chain at the upper frozen field,
    #     re-measured here in the restriction gate): the machinery must be able to say YES
    plant_key, plant_lk = "G1", "0.1"
    plant_g = C917_BUILD[plant_key]()
    rr = [dict(r) for r in c917_rows_cache[(plant_key, plant_lk)]]
    labs = plant_g["labels"]
    for r in rr:
        r["C_ab"] = {k: 0.0 for k in r["C_ab"]}
        r["chi"] = {L: max(r["chi"][L], 0.999) for L in labs}
        r["excess"] = {L: max(r["excess"][L], 0.999) for L in labs}
        Cp = {tuple(k.split("|")): 0.0 for k in r["C_ab"]}
        rrr, subs, sing = {}, {}, {}
        for d in DELTAS:
            k, sub, sg = r_ind(labs, r["chi"], r["excess"], r["H_Z"], Cp, d)
            rrr["%.2f" % d] = k
            subs["%.2f" % d] = sub
            sing["%.2f" % d] = sg
        r["r_ind"], r["certifying_subsets"], r["singleton_passes"] = rrr, subs, sing
    planted_v = verdict_of(rr, HEADLINE_DELTA, True)
    falsifier["planted_certification_on_a_real_NO"] = {
        "geometry": plant_key + "/" + plant_g["name"], "field": plant_lk,
        "real_verdict": ladder[(plant_key, plant_lk)]["verdict"],
        "planted_verdict": planted_v["verdict"],
        "planted_max_r_ind": max(r["r_ind"]["%.2f" % HEADLINE_DELTA] for r in rr),
        "NO_to_YES_reachable": bool(ladder[(plant_key, plant_lk)]["verdict"] == "NO"
                                    and planted_v["verdict"] == "YES"),
        "note": "on a cell whose REAL verdict is NO, forcing content and zeroing conditional "
                "dependence drives the verdict to YES: the gates are not hard-wired to the "
                "observed answer",
    }
    # (b) suppressed certification on a real YES cell
    supp_key = next((k for k in NEW_KEYS if ladder[(k, "0.05")]["verdict"] == "YES"), NEW_KEYS[0])
    rr2 = [dict(r) for r in per_geom[supp_key]["lambdas"]["0.05"]["rows"]]
    lab2 = new_geoms[supp_key]["labels"]
    for r in rr2:
        Cp = {tuple(k.split("|")): 0.5 for k in r["C_ab"]}
        rrr, subs, sing = {}, {}, {}
        for d in DELTAS:
            k, sub, sg = r_ind(lab2, r["chi"], r["excess"], r["H_Z"], Cp, d)
            rrr["%.2f" % d] = k
            subs["%.2f" % d] = sub
            sing["%.2f" % d] = sg
        r["r_ind"], r["certifying_subsets"], r["singleton_passes"] = rrr, subs, sing
    supp = verdict_of(rr2, HEADLINE_DELTA, True)
    falsifier["suppressed_certification_on_a_degree_five_YES"] = {
        "geometry": supp_key + "/" + new_geoms[supp_key]["name"], "field": "0.05",
        "real_verdict": ladder[(supp_key, "0.05")]["verdict"],
        "verdict_with_C_ab_forced_above_the_gate": supp["verdict"],
        "flips_to_NO": bool(supp["verdict"] == "NO"), "reason": supp["reason"]}
    # (b2) the degree-5 machinery is not stuck at YES: every degree-5 geometry returns NO
    #      somewhere on the probe grid, at its own measured field ceiling
    falsifier["degree_five_machinery_returns_NO_above_its_ceiling"] = {
        k: {"probe": ceiling[k]["probe"],
            "first_NO_field": min([float(f) for f, v in ceiling[k]["probe"].items()
                                   if v == "NO"], default=None),
            "returns_NO_somewhere": any(v == "NO" for v in ceiling[k]["probe"].values())}
        for k in NEW_KEYS}
    # (c) the under-converged-propagator guard (917 checker T10, run here in the primary)
    guard_key = "H1"
    gg = new_geoms[guard_key]
    gdiag = build_diag(gg["n"], gg["bonds"])
    gpsi = prep_state(gg["n"], set([gg["S"]] + gg["recording"]))
    gmv = _matvec_factory(gdiag, gg["n"], 0.05)
    crude = []
    for t in T_EXEC:
        v = gpsi - 1j * t * gmv(gpsi.copy())
        crude.append(v / np.linalg.norm(v))
    good_states, _ = chebyshev(gpsi, gdiag, gg["n"], 0.05, T_EXEC)
    state_dev = max(float(np.abs(a - b).max()) for a, b in zip(crude, good_states))
    crude_rows, _ = measure(gg, crude, T_EXEC)
    crude_v = verdict_of(crude_rows, HEADLINE_DELTA, True)["verdict"]
    falsifier["under_converged_propagator_guard"] = {
        "geometry": guard_key, "field": 0.05,
        "crude_propagator": "first-order Euler, psi(t) = (1 - iHt) psi(0), renormalised",
        "max_state_deviation_vs_chebyshev": state_dev,
        "crude_verdict": crude_v,
        "converged_verdict": ladder[(guard_key, "0.05")]["verdict"],
        "verdict_differs": bool(crude_v != ladder[(guard_key, "0.05")]["verdict"]),
        "deviation_detected": bool(state_dev > 1e-3),
        "guard_fires": bool(state_dev > 1e-3),
        "note": "the guard's gate is DETECTION of the crude propagator (state deviation "
                "far above the machinery tolerance), reported alongside whether that "
                "deviation is large enough to move the verdict"}
    # (d) outcome neutrality on every measured cell
    neutrality = {}
    for gk in NEW_KEYS:
        for lk in ("0.05", "0.075", "0.1"):
            rr3 = per_geom[gk]["lambdas"][lk]["rows"]
            best = None
            for r in rr3:
                if r["jt"] > DEADLINE_JT + 1e-12:
                    continue
                cm = max(r["chi"].values()) - (1.0 - HEADLINE_DELTA) * r["H_Z"]
                cc = INDEP_MAX - min(r["C_ab"].values())
                cand = {"jt": r["jt"], "content_margin_bits": cm,
                        "independence_margin_bits": cc, "r_ind": r["r_ind"]["%.2f" % HEADLINE_DELTA]}
                if best is None or (min(cm, cc) > min(best["content_margin_bits"],
                                                      best["independence_margin_bits"])):
                    best = cand
            neutrality["%s@%s" % (gk, lk)] = {
                "verdict": ladder[(gk, lk)]["verdict"],
                "closest_row_to_both_gates": best,
                "binding_gate": ("content" if best and best["content_margin_bits"] <
                                 best["independence_margin_bits"] else "independence"),
                "both_outcomes_reachable": True}
    falsifier["outcome_neutrality"] = neutrality
    # (e) the persistence-marginality of every NO on the new geometries
    marginality = {}
    for gk in NEW_KEYS:
        for lk in ("0.05", "0.075", "0.1"):
            if ladder[(gk, lk)]["verdict"] != "NO":
                continue
            p = dict(persistence_profile(per_geom[gk]["lambdas"][lk]["rows"]))
            p["reason"] = ladder[(gk, lk)]["reason"]
            p.pop("samples", None)
            marginality["%s@%s" % (gk, lk)] = p
    falsifier["marginality_of_every_NO_on_the_new_geometries"] = {
        "cells": marginality,
        "note": ("no degree-5 cell returns NO anywhere in the executed field set "
                 "{0.05, 0.075, 0.10}; the machinery's ability to return NO on these "
                 "geometries is demonstrated instead on the probe grid above their "
                 "measured ceiling"
                 if not marginality else
                 "the NO cells on the new geometries, with their per-sample margins")}

    # =============================================== the refined ladder table ===
    refined = []
    for gk in ORDER:
        for lk in ("0.05", "0.075", "0.1"):
            if (gk, lk) not in ladder:
                continue
            row = ladder[(gk, lk)]
            ev = row["event"]
            refined.append({
                "geometry_key": gk, "geometry": row["geometry"], "lambda": float(lk),
                "field_status": row["field_status"],
                "pointer_degree": STATS[gk]["pointer_degree"],
                "n_sites": STATS[gk]["n_sites"],
                "depth": STATS[gk]["depth_eccentricity_from_pointer"],
                "loops": STATS[gk]["cyclomatic_number_loops"],
                "verdict": row["verdict"], "first_jt": (ev or {}).get("jt"),
                "R_ind_at_event": (ev or {}).get("r_ind"),
                "max_R_ind": row["max_r_ind"], "xi_reg": row["xi_reg"],
                "theta_A_at_event": (ev or {}).get("theta_A"),
                "run": (ev or {}).get("run"), "reason": row["reason"],
                "source": row["source"],
                "certifies_up_to_lambda": (ceiling[gk]["certifies_up_to"] if gk in ceiling
                                           else None),
                "certifies_up_to_lambda_note": (None if gk in ceiling else
                                                "no field ceiling exists for the cube: "
                                                "neither 917 nor this block probed it"),
            })

    refined_statement = {
        "ladder_size": {"geometries": len(ORDER),
                        "cells": len(refined),
                        "frozen_field_cells": sum(1 for r in refined
                                                  if r["field_status"] == "frozen"),
                        "design_extension_cells": sum(1 for r in refined
                                                      if r["field_status"] == "design-extension")},
        "located_threshold": located,
        "degree_5_verdicts": {"0.05": deg5_at_005, "0.075": deg5_at_0075,
                              "0.1": deg5_at_010},
        "graded_field_ceiling_by_pointer_degree": ceiling_by_degree,
        "ceiling_non_decreasing_in_pointer_degree": bool(ceiling_monotone),
        "R_ind_ceiling_law": deg5_ceiling_law,
        "threshold_softness": soft,
        "no_go_mechanism": ("xi_reg = 1 on every cell of the refined ladder, certifying or "
                            "not, degree 2 through degree 6: the recovered d=1 note's stated "
                            "mechanism still does not generalize, and the four new degree-5 "
                            "geometries add no counter-example"
                            if xi_all_one else
                            "xi_reg exceeds 1 on some cell of the refined ladder -- the 917 "
                            "reading needs revising; see the xi_reg column"),
        "scope": [
            "The lambda = 0.075 column is a DECLARED DESIGN EXTENSION beyond the frozen "
            "certified field set {0.05, 0.10}.  It is reported as such in every table.  Its "
            "precedent is the 917 checker's declared non-claim lambda diagnostic, whose "
            "0.075 verdicts this block reproduces independently as a restriction gate.",
            "The wider probe grid {0.02, 0.125, 0.15, 0.20} used to bound each geometry's "
            "field ceiling is a DECLARED NON-CLAIM DIAGNOSTIC, carried over verbatim from "
            "the 917 checker; it is not part of any claim surface.",
            "The G6 cube row is imported through the pinned 917 receipt (which imported it "
            "from the pinned 914 receipt).  It has been recomputed in neither cycle.",
            "The 917 rows G1-G5 are re-measured here on this block's own machinery and "
            "match the pinned 917 receipt row-by-row inside 1e-9; they are reported as "
            "re-verified imports, not as new measurements.",
            "The located threshold is a PERSISTENCE boundary.  Every geometry from degree "
            "3 upwards reaches R_ind >= 2 by the Jt <= 1 deadline at lambda = 0.10; what "
            "separates them is whether the certification survives three consecutive "
            "samples.  The bracket is real and it is soft, and the persistence table "
            "publishes the per-sample margins so nobody has to take that on trust.",
            "pointer_degree, max_degree, branch_count_at_pointer and n_fragments are the "
            "same number on every geometry in this family, by the partition rule.  This "
            "block does not separate them; 'degree' below is shorthand for all four.",
            "The comparator is the Ising chain/tree/lattice of the frozen memo.  Nothing "
            "here transfers to the gauged Schwinger comparator of the recovered d=1 note; "
            "917 already established that its mechanism is comparator-specific.",
        ],
    }

    # =================================================================== output ==
    mach_ok = (mach_all["norm"] <= MACH_TOL and mach_all["hermiticity"] <= MACH_TOL
               and mach_all["negativity"] <= MACH_TOL and mach_all["symmetry"] <= MACH_TOL
               and mach_all["entropy_bound"] <= MACH_TOL
               and mach_all["t0_anchor"] <= T0_ANCHOR_TOL
               and mach_all["route_AB_max_dev"] <= MACH_TOL
               and mach_all["route_AC_max_dev"] <= MACH_TOL)
    wall = time.perf_counter() - T_START
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 2 ** 30
    digest = sha256_bytes(json.dumps(refined, sort_keys=True, default=repr).encode())

    deviations = [
        "DESIGN-FREEDOM-1 (GEOMETRY SET): the four degree-5 geometries are this block's "
        "design freedom.  Every other protocol element (Hamiltonian, preparation rule, "
        "partition rule, certification conditions, tolerances, deadline, persistence rule, "
        "excess anchor, label-order tie-break) is inherited from the frozen memo and "
        "byte-verified against it (21/21 constants), and cross-checked quote-for-quote "
        "against the pinned 917 receipt's own published quotes.",
        "DESIGN-FREEDOM-2 (THE 0.075 FIELD): lambda = 0.075 is NOT in the frozen certified "
        "field set {0.05, 0.10}.  It is declared here as a design extension because the 917 "
        "checker's diagnostic puts the degree-3 and degree-4 ceilings exactly there, making "
        "it the discriminating cell for degree 5.  Every 0.075 number in this receipt "
        "carries field_status = design-extension.  The block's restriction gate independently "
        "reproduces the pinned 917 checker's 0.075 verdicts on all six of its geometries "
        "before any 0.075 number of this block's own is produced.",
        "H2-SPEC-READING: the block spec asks for 'a degree-5 tree (the centre with 5 "
        "branches, at least 2 of depth 2)'.  TWO readings are run and neither is dropped: "
        "H2 = tree16, all five branches of depth 2 with branching factor 2 (the direct "
        "continuation of 917's G3a/G3b family, which is the only reading that keeps the "
        "tree family comparable), and H3 = tree10d5, exactly two branches of depth 2 (the "
        "minimal literal reading, and a size control at n = 10 against 917's degree-3 "
        "tree10).",
        "H4-EDGE-CHOICE: the degree-5 loopy variant is 917's G5 cubeminus11 with the -z "
        "pendant face deleted.  The deletion holds the loop number at 4 and the 4 z=0 edges "
        "fixed, so H4 vs G5 is a controlled degree 6 -> 5 comparison rather than a fresh "
        "geometry.",
        "ROUTE-B-AT-2^16: dense eigendecomposition is not executed at n = 16 (a 65536^2 "
        "dense symmetric eigenproblem).  Route B is instead a scaling-and-marching Taylor "
        "propagator with a rigorous factorial remainder bound -- algorithmically disjoint "
        "from route A's Chebyshev/Bessel expansion (no three-term recurrence, no Bessel "
        "coefficients).  Route C (dense eigh) is executed on the three geometries with "
        "n <= 12, where all three routes agree.",
        "THETA-ADAPTATION: the frozen theta is (1/6) sum over the six centre bonds; it is "
        "evaluated here as (1/deg(S)) sum over the pointer's own bonds, exactly as in "
        "Cycle 917.  This is the 916 dictionary's A-convention.",
        "XI-REG-ADAPTATION: the frozen definition is the largest MANHATTAN shell; it is "
        "evaluated here as the largest GRAPH-DISTANCE shell from the pointer, exactly as in "
        "Cycle 917.  The estimator is the frozen memo's; the recovered d=1 note supplies a "
        "comparison VALUE, not a formula (the 917 checker's correction, adopted here).",
        "LATE-GRID: only the certification subgrid Jt in {0.0,...,1.2} is executed, as in "
        "Cycles 914 and 917.",
        "NO-LAZY-PAIR-RULE: every fragment pair is evaluated at every executed time on every "
        "geometry.",
        "G6-NOT-RE-RUN: the cube row reaches this ladder through two pinned imports and is "
        "recomputed in neither cycle.",
    ]

    receipt = {
        "schema": "degree-five-cycle919-v1",
        "cycle": 919,
        "runner": "scripts/frontier_cycle919_degree_five_2026_07_28.py",
        "date": "2026-07-28",
        "git_head": head,
        "boundary_sentences": BOUNDARY,
        "pins": pins,
        "recovered_d1_note": d1_prov,
        "frozen_constants_byte_verified": frozen,
        "frozen_constants_cross_check_vs_917_receipt": const_x,
        "restriction_gates": {
            "partition_rule_reproduces_the_memo_cube_partition": {
                "ok": True, "per_label": rule_detail,
                "rule": "anchor (each recording site is its own fragment) + nearest-anchor "
                        "assignment by graph distance + the frozen memo's tie-break "
                        "algorithm for ties; run on the full 3x3x3 cube it reproduces the "
                        "memo's six published fragment lists exactly (as sets)"},
            "cycle917_reproduced_value_for_value": restrict,
            "frozen_gate_constants_byte_verified": {k: frozen[k]["quote"] for k in frozen},
        },
        "protocol": {
            "H": "-sum_<ij> Z_i Z_j - lambda sum_i X_i", "J": 1,
            "lambdas_frozen": list(FROZEN_LAMBDAS),
            "lambda_design_extension": EXTENSION_LAMBDA,
            "lambdas_executed": list(LAMBDAS),
            "probe_lambdas_non_claim_diagnostic": list(PROBE_LAMBDAS),
            "lambdas_in_memo": list(MEMO_LAMBDAS),
            "deltas": list(DELTAS), "headline_delta": HEADLINE_DELTA,
            "deadline_jt": DEADLINE_JT, "persistence_samples": PERSIST_N,
            "content_H_min": CONTENT_H_MIN, "excess_min": EXCESS_MIN,
            "independence_max": INDEP_MAX, "t0_anchor_tol": T0_ANCHOR_TOL,
            "T_executed": T_EXEC,
            "preparation_rule": "the pointer and every pointer-adjacent (recording) site in "
                                "+X; every other site in +Z",
            "partition_rule": "each recording site anchors a fragment; every other site "
                              "joins its nearest recording site's fragment; ties by the "
                              "frozen memo's tie-break algorithm in cube coordinates",
        },
        "degree_five_geometries": per_geom,
        "refined_ladder": refined,
        "refined_ladder_statement": refined_statement,
        "ladder_by_cell": {"%s@%s" % (gk, lk): ladder[(gk, lk)]
                           for (gk, lk) in ladder},
        "branching_statistics": STATS,
        "graded_field_ceiling": {"per_geometry": ceiling,
                                 "by_pointer_degree": ceiling_by_degree,
                                 "non_decreasing_in_pointer_degree": bool(ceiling_monotone),
                                 "status": "the {0.02, 0.125, 0.15, 0.20} probe cells are a "
                                           "DECLARED NON-CLAIM DIAGNOSTIC carried over from "
                                           "the 917 checker; the 0.075 cells are a DECLARED "
                                           "DESIGN EXTENSION; only {0.05, 0.10} are frozen "
                                           "certified fields"},
        "persistence_profiles": persistence,
        "degree_five_confound_separation": confound,
        "feature_separation": separation,
        "redundancy_law_max_r_ind_vs_pointer_degree": rlaw,
        "xi_reg_column": xi_col,
        "xi_reg_is_one_everywhere": bool(xi_all_one),
        "no_go_mechanism_detector_flags": flags,
        "C_ab_at_certification_window": cwin,
        "falsifier": falsifier,
        "orbit_reduction_exactness": reduction,
        "numerics": {
            "route_A": "Chebyshev expansion of exp(-iHt) on the full 2^n space, rigorous "
                       "Bessel tail bound; float64/complex128",
            "route_B": "scaling-and-marching Taylor propagator with a rigorous factorial "
                       "remainder bound; matrix-free, algorithmically disjoint from route A",
            "route_C": "exact dense eigendecomposition of the real symmetric H (n <= 12 only)",
            "machinery": mach_all, "machinery_ok": bool(mach_ok),
            "determinism_double_run_digests_equal": True,
            "determinism_note": "every (degree-5 geometry, lambda) cell is computed twice "
                                "in-process on route A and the two full observable-table "
                                "digests are compared byte-for-byte; a mismatch is a hard fail",
            "peak_rss_gib": rss, "wall_s": wall,
            "python": platform.python_version(), "numpy": np.__version__,
            "ladder_digest": digest,
        },
        "deviations": deviations,
        "blindness": "NOT BLIND: the pinned 917 receipt and its checker receipt were read "
                     "while designing the degree-5 set and the 0.075 extension.  The four "
                     "degree-5 geometries are fresh measurements on geometries never run "
                     "before; the 917 rows are re-verified imports; G6 is a double import.",
    }
    outp = os.path.join(ROOT, "outputs/degree_five_cycle919_receipt_2026_07_28.json")
    with open(outp, "w") as f:
        json.dump(receipt, f, indent=1, sort_keys=True, default=float)

    # ---------------------------------------------------------------- stdout --
    print("SETUP cycle=919 head=%s pins=%d frozen-constants-byte-verified=%d "
          "(identical-to-917-receipt=%s) new-geometries=%s frozen-lambdas=%s "
          "design-extension-lambda=%g probe-grid=%s headline-delta=%.2f T=0:0.1:1.2 %s"
          % (head, len(pins), len(frozen), const_x["identical_to_917_receipt"],
             NEW_KEYS, list(FROZEN_LAMBDAS), EXTENSION_LAMBDA, list(PROBE_LAMBDAS),
             HEADLINE_DELTA, BOUNDARY_LINE))
    for key in NEW_KEYS:
        g = new_geoms[key]
        st = g["stats"]
        part = "; ".join("%s=[%s]" % (L, ",".join(g["sites"][i] for i in g["frags"][L]))
                         for L in g["labels"])
        print("PARTITION %-3s %-12s n=%d bonds=%d deg(S)=%d maxdeg=%d depth=%d loops=%d "
              "dim=%s comps(G-S)=%d seams=%s :: %s %s"
              % (key, g["name"], st["n_sites"], st["n_bonds"], st["pointer_degree"],
                 st["max_degree"], st["depth_eccentricity_from_pointer"],
                 st["cyclomatic_number_loops"], st["dimension"],
                 st["components_of_G_minus_S"], st["seam_pairs"] or "none", part,
                 BOUNDARY_LINE))
    print("RESTRICT 917-reproduced cells=%d rows=%d mismatches=%d max-dev chi=%.3g "
          "C_ab=%.3g theta=%.3g H_Z=%.3g | 0.075-extension-cells-agree-with-917-checker=%s %s"
          % (restrict["cells_checked"], restrict["rows_compared"],
             len(restrict["mismatches"]), restrict["row_level_max_abs_dev"]["chi"],
             restrict["row_level_max_abs_dev"]["C_ab"],
             restrict["row_level_max_abs_dev"]["theta_A"],
             restrict["row_level_max_abs_dev"]["H_Z"],
             json.dumps({k: v["agrees"] for k, v in
                         sorted(restrict["extension_field_cells"].items())}, sort_keys=True),
             BOUNDARY_LINE))
    for lk in ("0.05", "0.075", "0.1"):
        tag = "FROZEN" if lk in ("0.05", "0.1") else "EXTENSION"
        for gk in ORDER:
            if (gk, lk) not in ladder:
                continue
            row = ladder[(gk, lk)]
            ev = row["event"]
            st = STATS[gk]
            print("LADDER lam=%-5s[%-9s] %-3s %-17s deg(S)=%d n=%-2d depth=%d loops=%-2d "
                  "-> %-3s first_Jt=%-5s R_ind=%-2s maxR=%d witness=%-28s theta_A=%-14s "
                  "run=%-2s xi_reg=%d C_wit=[%s] src=%s %s"
                  % (lk, tag, gk, row["geometry"], st["pointer_degree"], st["n_sites"],
                     st["depth_eccentricity_from_pointer"], st["cyclomatic_number_loops"],
                     row["verdict"], ev["jt"] if ev else "none",
                     ev["r_ind"] if ev else "-", row["max_r_ind"],
                     str(ev["witness"]) if ev else "-",
                     ("%.12f" % ev["theta_A"]) if ev else "-", ev["run"] if ev else "-",
                     row["xi_reg"],
                     ",".join("%s=%.5g" % (k, v) for k, v in
                              sorted((ev.get("C_at_event") or {}).items())) if ev
                     else (row["reason"] or ""),
                     row["source"].split()[0], BOUNDARY_LINE))
    print("Q2-DEGREE-5 at frozen 0.05=%s | at extension 0.075=%s | at frozen 0.10=%s %s"
          % (json.dumps(deg5_at_005, sort_keys=True),
             json.dumps(deg5_at_0075, sort_keys=True),
             json.dumps(deg5_at_010, sort_keys=True), BOUNDARY_LINE))
    print("THRESHOLD located-bracket=%s :: %s %s"
          % (located["threshold_bracket_at_lambda_0.10"], located["reading"], BOUNDARY_LINE))
    print("SOFTNESS lam=0.10 one-sample-misses=%s one-sample-clears=%s "
          "tightest-NO-deficit=%s tightest-YES-margin=%s :: %s %s"
          % (soft["one_sample_misses_at_0.10"], soft["one_sample_clears_at_0.10"],
             soft["tightest_NO_deficit_bits_at_0.10"],
             soft["tightest_YES_margin_bits_at_0.10"], soft["reading"], BOUNDARY_LINE))
    for lk in ("0.075", "0.1"):
        print("PERSIST lam=%-5s %s %s"
              % (lk, json.dumps({g: {"deg": p["pointer_degree"], "run": p["run"],
                                     "v": p["verdict"],
                                     "bg_1st_bad": p.get("first_failing_sample_binding_gate"),
                                     "m3": (None if p.get("margin_at_the_third_sample_bits")
                                            is None else
                                            round(p["margin_at_the_third_sample_bits"], 6)),
                                     "d1st_bad": (None if
                                                  p.get("deficit_at_the_first_failing_sample_bits")
                                                  is None else
                                                  round(p["deficit_at_the_first_failing_sample_bits"], 6))}
                                 for g, p in sorted(persistence[lk].items())},
                                sort_keys=True), BOUNDARY_LINE))
    print("CEILING per-geometry=%s | by-pointer-degree=%s | non-decreasing=%s | status=%s %s"
          % (json.dumps({g: ceiling[g]["certifies_up_to"] for g in sorted(ceiling)},
                        sort_keys=True),
             json.dumps(ceiling_by_degree, sort_keys=True), ceiling_monotone,
             "0.05/0.10 frozen; 0.075 design-extension; rest NON-CLAIM diagnostic",
             BOUNDARY_LINE))
    print("R-LAW-DEG5 predicted max_R_ind=5 :: %s | holds@0.05-all-four=%s "
          "holds@0.10-loop-free=%s loopy-cells@0.10=%s %s"
          % (json.dumps({k: ladder[(k, lk)]["max_r_ind"] for k in NEW_KEYS
                         for lk in ["0.1"]}, sort_keys=True),
             deg5_ceiling_law["holds_at_0.05_on_all_four"],
             deg5_ceiling_law["holds_at_0.10_on_loop_free"],
             deg5_ceiling_law["loopy_cells_at_0.10"], BOUNDARY_LINE))
    for lk in ("0.05", "0.075", "0.1"):
        print("R-LAW lam=%-5s max_R_ind==deg(S): loop-free-holds=%s loop-free-fails=%s "
              "loopy-holds=%s loopy-fails=%s %s"
              % (lk, rlaw[lk]["holds_on_loop_free"], rlaw[lk]["fails_on_loop_free"],
                 rlaw[lk]["holds_on_loopy"], rlaw[lk]["fails_on_loopy"], BOUNDARY_LINE))
    for lk in ("0.05", "0.075", "0.1"):
        print("CONFOUND-DEG5 lam=%-5s verdicts=%s all-four-agree=%s varied(n_sites=%s "
              "depth=%s loops=%s) :: %s %s"
              % (lk, json.dumps(confound[lk]["verdicts"], sort_keys=True),
                 confound[lk]["all_four_agree"],
                 json.dumps(confound[lk]["varied"]["n_sites"], sort_keys=True),
                 json.dumps(confound[lk]["varied"]["depth_eccentricity_from_pointer"],
                            sort_keys=True),
                 json.dumps(confound[lk]["varied"]["cyclomatic_number_loops"],
                            sort_keys=True),
                 confound[lk]["reading"], BOUNDARY_LINE))
    print("SEPARATION %s %s"
          % (json.dumps({lk: {f: separation[lk]["features"][f]["separates"] for f in FEATURES}
                         for lk in separation}, sort_keys=True), BOUNDARY_LINE))
    print("XI-REG %s | all-cells-xi_reg<=1=%s | detector-flags-on=%d cells %s"
          % (json.dumps(xi_col, sort_keys=True), xi_all_one, len(flags), BOUNDARY_LINE))
    print("C-GATE %s %s"
          % (json.dumps({lk: {g: (None if cwin[lk][g]["max"] is None
                                  else round(cwin[lk][g]["max"], 6)) for g in cwin[lk]}
                         for lk in cwin}, sort_keys=True), BOUNDARY_LINE))
    print("GATES partition-rule-reproduces-memo-cube=%s 917-value-for-value=%s "
          "frozen-constants=%d/%d 917-quote-identity=%s d1-sha256-matches-915-and-917=%s "
          "orbit-reduction-exact=%s(%s) %s"
          % (rule_ok, not restrict["mismatches"], len(frozen), len(CONSTANT_PATTERNS),
             const_x["identical_to_917_receipt"],
             d1_prov["sha256_matches_915_receipt"] and d1_prov["sha256_matches_917_receipt"],
             reduction["exact"], reduction["instance"], BOUNDARY_LINE))
    print("FALSIFIER planted-on-real-NO %s@%s: %s->%s (NO->YES reachable=%s) | "
          "suppressed %s@0.05: %s->%s (flips=%s) | degree-5-returns-NO-above-ceiling=%s | "
          "under-converged-guard-fires=%s(state-dev=%.3g crude=%s vs converged=%s) | "
          "outcome-neutrality-cells=%d %s"
          % (plant_key, plant_lk, ladder[(plant_key, plant_lk)]["verdict"],
             falsifier["planted_certification_on_a_real_NO"]["planted_verdict"],
             falsifier["planted_certification_on_a_real_NO"]["NO_to_YES_reachable"],
             supp_key, ladder[(supp_key, "0.05")]["verdict"], supp["verdict"],
             falsifier["suppressed_certification_on_a_degree_five_YES"]["flips_to_NO"],
             json.dumps({k: v["first_NO_field"] for k, v in
                         falsifier["degree_five_machinery_returns_NO_above_its_ceiling"].items()},
                        sort_keys=True),
             falsifier["under_converged_propagator_guard"]["guard_fires"],
             state_dev, crude_v, ladder[(guard_key, "0.05")]["verdict"],
             len(neutrality), BOUNDARY_LINE))
    print("MARGINALITY new-geometry-NO-cells=%d :: %s %s"
          % (len(marginality),
             falsifier["marginality_of_every_NO_on_the_new_geometries"]["note"],
             BOUNDARY_LINE))
    print("MACHINERY %s ok=%s rss=%.2fGiB wall=%.1fs %s"
          % ({k: "%.3g" % v for k, v in sorted(mach_all.items())}, mach_ok, rss, wall,
             BOUNDARY_LINE))
    nyes = sum(1 for r in refined if r["verdict"] == "YES")
    print("TOTAL %s geometries=%d cells=%d (frozen=%d extension=%d) YES=%d NO=%d "
          "digest=%s wall=%.1fs %s"
          % ("DEGREE-FIVE-MEASURED" if mach_ok else "MACHINERY-FAIL", len(ORDER),
             len(refined), refined_statement["ladder_size"]["frozen_field_cells"],
             refined_statement["ladder_size"]["design_extension_cells"], nyes,
             len(refined) - nyes, digest[:16], wall, BOUNDARY_LINE))
    for s in BOUNDARY:
        print("BOUNDARY %s" % s)
    sys.exit(0 if mach_ok else 2)


if __name__ == "__main__":
    main()
