#!/usr/bin/env python3
"""Cycle 917 -- THE GEOMETRY LADDER: the certification verdict as a function of
environment geometry, under the frozen route-C protocol verbatim.

THE QUESTION.  The mass lane has a d=1 NO (the recovered comparator note:
"Redundancy at permanence grade (R >= 2 over conditionally independent
registers) requires BRANCHING environment geometry", proven there as a gauged
d=1 no-go with mechanism `xi_reg <= 1 link`) and a d=3 YES (Cycles 914/915: the
open 3x3x3 cube certifies at Jt = 0.6/0.7 for lambda = 0.05/0.10).  Nobody has
measured the THRESHOLD: how much branching is enough?

THE DESIGN DISCIPLINE.  This block designs its GEOMETRY SET and inherits
EVERYTHING else from

    docs/D3_BAR_LOCATION_DESIGN_SCOUT_2026-07-10.md   (FROZEN 2026-07-10)

verbatim: H_lambda = -sum_<ij> Z_i Z_j - lambda sum_i X_i, the pointer-contrast
preparation rule (the pointer and its neighbours in +X, every other site in +Z),
the three-condition Holevo certification at the frozen deltas, the C_ab <= 0.02
conditional-independence gate, the R_ind >= 2 permanence bar with the frozen
label-order tie-break, the Jt <= 1 onset deadline, the three-consecutive-sample
persistence flag, the t=0 baseline requirement (chi(0) <= 1e-9 bit), the
trajectory-t0 excess anchor, and the certified fields lambda in {0.05, 0.10}.
Every one of those constants is BYTE-VERIFIED out of the frozen memo below.

THE GEOMETRY SET (the only design freedom, declared here):

  G1  chain9        the 9-site open chain          d=1 reference (the no-go's case)
  G2  star7         K_{1,6}                        maximal local branching, no depth
  G3a tree10        centre + 3 branches, depth 2   branching WITH depth
  G3b tree13        centre + 4 branches, depth 2   branching WITH depth (13-site)
  G4  plaquette9    the open 3x3 square            d=2, loops
  G5  cubeminus11   centre + 6 faces + 4 z=0 edges bridge case
  G6  cube27        the open 3x3x3 cube            IMPORTED value-for-value from
                                                   the pinned 914/915 receipts

(G3 is run in BOTH readings of its specification -- see the DEVIATIONS block.)

Deterministic, float64/complex128, no network, no tree writes outside the
declared receipt.

Not basis-neutral: the ZZ bond and the declared Z pointer privilege the Z basis, by construction.
No formation rule.
Sets no audit status.
"""

import hashlib
import itertools
import json
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
    # the three frozen memos
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
    # the 914 / 915 / 916 primaries, checkers, receipts and landed notes
    "scripts/frontier_cycle914_d3_bar_commission_2026_07_28.py": (
        "fc7344a06503f9c159ea732cb6f622a23e61196e370914943ffd9a468fd592e4",
        "e0639e0b5d1ebdd995c4c7ec3255f8daeeb4fe0c"),
    "scripts/frontier_cycle914_d3_bar_independent_check_2026_07_28.py": (
        "8ffd5436b5c506e9965a9a6f486f595531113aedef77cc2861114e87b362973f",
        "ca26ecbec850b785b8b4228b46ab56c9f5e97831"),
    "scripts/frontier_cycle915_comparator_recovery_2026_07_28.py": (
        "b1b575f58bd3af24705c1afbe74a4f1e2dfe8e02a251df642e44b7a4e4f4d06c",
        "94bd41b8486b9af2ab96a4781dc729df0b888e1f"),
    "scripts/frontier_cycle915_comparator_independent_check_2026_07_28.py": (
        "4693ff6b14418b068b2b702cbd645f0105706900420bdf90e9bb419d324da2f5",
        "9b220084386105c415ec87f947ea52cc0b630f12"),
    "scripts/frontier_cycle916_theta_reconciliation_2026_07_28.py": (
        "3fa7f1d86c0443f055ec5a946176ab8261e6b66d87979dc299e5e6296a06f6d6",
        "bd02476a97539594c9186a196fc0a3fe158404af"),
    "scripts/frontier_cycle916_theta_independent_check_2026_07_28.py": (
        "4bcf77deae0c8577bfabe4dc9f3816b61abdf5ebd6bdf7bd69213a7c1c90e9fe",
        "2545e1768ab51a061ea5b33b52f4ae0aa02e21f9"),
    "outputs/d3_bar_commission_cycle914_receipt_2026_07_28.json": (
        "fba8a16ee811fa1729bc1cdb6988096193a7e14878e7a78380f4880120bf7223",
        "cabb1bef15221b5fca61ffc7c50f8ec18452893d"),
    "outputs/d3_bar_independent_check_cycle914_receipt_2026_07_28.json": (
        "90b12afccaccbd92226d4b7aafca93531cfaf2f4e0ae83e40a3fe17c6cdd2868",
        "d0f874fb6da8d137a61fbed1d493eb7944e832b5"),
    "outputs/comparator_recovery_cycle915_receipt_2026_07_28.json": (
        "d7d27ce19d231624415db1e71ee77eae16b5175dd403b403c254b38fb171b0a7",
        "9931c298a5917eb90de290cbb82c237508c9e692"),
    "outputs/comparator_independent_check_cycle915_receipt_2026_07_28.json": (
        "9fb3b2d6e494767ab81354f0163580b5d2e5718e3c81f201bd1dae7d067c0156",
        "e9523a193148caefc55a501caa9fa939365c2238"),
    "outputs/theta_reconciliation_cycle916_receipt_2026_07_28.json": (
        "4a3e390bbc9e9ba21dd3b87feef5db0171d33c8ddc5187314125300cedb8419c",
        "2923533ed245312d1011c7217c92c5f18eef1185"),
    "outputs/theta_independent_check_cycle916_receipt_2026_07_28.json": (
        "b64942ac28a5d4c04b75d6ddb1e4903c7bcfebb69fb997e49b3152853f064f30",
        "7a7c924d11c79f5c08c458aec610f0ba90a4a6f9"),
    "docs/D3_BAR_REAUDIT_REPRODUCED_CYCLE914_BOUNDED_THEOREM_NOTE_2026-07-28.md": (
        "4b6aeca73c03fe0c2e3301600dd72ad37ceac99ea6c9410a5a9466b63e0ff181",
        "376c8a347469e76142a4df45e8e4adc85ab18926"),
    "docs/COMPARATOR_RECOVERED_THETA_MISATTRIBUTED_CYCLE915_BOUNDED_THEOREM_NOTE_2026-07-28.md": (
        "9ca5c99cc7f5b761ef27fbcf56ce7ad9fa1ef49709019bc47224d8f982dcbe06",
        "39dec3ca9035590a63f032fe2e9b6f51c560a89f"),
}

PARENT_MEMO = "docs/D3_BAR_LOCATION_DESIGN_SCOUT_2026-07-10.md"
C914_RECEIPT = "outputs/d3_bar_commission_cycle914_receipt_2026_07_28.json"
C915_RECEIPT = "outputs/comparator_recovery_cycle915_receipt_2026_07_28.json"
C914_NOTE = "docs/D3_BAR_REAUDIT_REPRODUCED_CYCLE914_BOUNDED_THEOREM_NOTE_2026-07-28.md"

# the recovered d=1 comparator note -- NOT in tree; consumed as git-history
# evidence.  blob + sha256 are the values RECORDED BY THE 915 RECEIPT; the
# runner re-derives the sha256 from the blob bytes and cross-checks.
D1_NOTE_PATH = "docs/REGISTRATION_REDUNDANCY_ONSET_BOUNDED_NOTE_2026-07-09.md"
D1_NOTE_BLOB = "dd247a8494f171d4dcaf9a532a09491202b1f512"
D1_NOTE_SHA256 = "41b4f26af908a7b910fbb5683f9d50432f36328bced7cf107585f7f70771df04"
D1_NOTE_BYTES = 5230

# ============================================== frozen protocol constants ====
# Every constant below is BYTE-VERIFIED against the frozen memo in
# verify_frozen_constants(); a mismatch is a hard fail, exit 2.
LAMBDAS = (0.05, 0.10)          # the CERTIFIED fields (914/915 measurement)
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
T_EXEC = [round(0.1 * i, 10) for i in range(13)]   # Jt = 0.0 .. 1.2, 13 points

CUBE_LABELS = ("+x", "-x", "+y", "-y", "+z", "-z")


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
        r = git(["hash-object", full])
        got_blob = r.stdout.decode().strip()
        if got_sha != want_sha:
            die("pin:sha256 %s got=%s want=%s" % (path, got_sha, want_sha))
        if got_blob != want_blob:
            die("pin:blob %s got=%s want=%s" % (path, got_blob, want_blob))
        out[path] = {"sha256": got_sha, "git_blob": got_blob, "bytes": len(b)}
    return out


def recover_d1_note():
    """Read the never-landed d=1 comparator note out of git history."""
    cmds = ["git cat-file -e HEAD:%s" % D1_NOTE_PATH,
            "git cat-file -t %s" % D1_NOTE_BLOB,
            "git cat-file blob %s" % D1_NOTE_BLOB]
    r0 = git(["cat-file", "-e", "HEAD:%s" % D1_NOTE_PATH])
    in_tree = (r0.returncode == 0)
    if in_tree:
        die("d1-note:unexpectedly-in-tree (the 915 receipt records it as never-landed)")
    r1 = git(["cat-file", "-t", D1_NOTE_BLOB])
    if r1.stdout.decode().strip() != "blob":
        die("d1-note:blob-missing %s" % D1_NOTE_BLOB)
    r2 = git(["cat-file", "blob", D1_NOTE_BLOB])
    if r2.returncode != 0:
        die("d1-note:cat-file-failed")
    b = r2.stdout
    got = sha256_bytes(b)
    if got != D1_NOTE_SHA256:
        die("d1-note:sha256 got=%s want=%s" % (got, D1_NOTE_SHA256))
    if len(b) != D1_NOTE_BYTES:
        die("d1-note:bytes got=%d want=%d" % (len(b), D1_NOTE_BYTES))
    # cross-check the sha256 against the value RECORDED IN the pinned 915 receipt
    rec = json.load(open(os.path.join(ROOT, C915_RECEIPT)))
    art = rec["C1_recovery"]["artifacts"][D1_NOTE_PATH]["recovered"]
    if art["sha256"] != got or art["blob"] != D1_NOTE_BLOB or art["bytes"] != len(b):
        die("d1-note:915-receipt-cross-check")
    return b.decode("utf-8"), {"path": D1_NOTE_PATH, "blob": D1_NOTE_BLOB,
                               "sha256": got, "bytes": len(b),
                               "in_tree_at_head": in_tree,
                               "sha256_matches_915_receipt": True,
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


def d1_xi_reg_quotes(d1_text, memo):
    """Byte-quote the xi_reg definition from BOTH sources it lives in."""
    q = {}
    m = re.search(r"the register range is xi_reg <= 1\s*\n?\s*link at every point", d1_text)
    if m is None:
        die("d1-quote:xi_reg-range-miss")
    q["d1_note_xi_reg_measurement"] = {"source": D1_NOTE_PATH + " (git blob %s)" % D1_NOTE_BLOB,
                                       "quote": " ".join(m.group(0).split())}
    m = re.search(r"v3 single-link registers \+\s*\n?\s*g = 0\.3 \+ register-profile exhibit "
                  r"\(xi_reg <= 1 everywhere\)", d1_text)
    if m is None:
        die("d1-quote:xi_reg-exhibit-miss")
    q["d1_note_xi_reg_exhibit"] = {"source": D1_NOTE_PATH, "quote": " ".join(m.group(0).split())}
    m = re.search(r"Redundancy at permanence grade \(R >= 2 over conditionally independent\s*\n?"
                  r"registers\) requires BRANCHING environment geometry\.", d1_text)
    if m is None:
        die("d1-quote:structural-miss")
    q["d1_note_structural_claim"] = {"source": D1_NOTE_PATH, "quote": " ".join(m.group(0).split())}
    m = re.search(r"The permanence bar \(R >= 2\) never fires, and the obstruction is\s*\n?\s*"
                  r"structural, not parametric", d1_text)
    if m is None:
        die("d1-quote:bar-miss")
    q["d1_note_bar_statement"] = {"source": D1_NOTE_PATH, "quote": " ".join(m.group(0).split())}
    m = re.search(r"in d = 1\s*\n?\s*the two boundary links are a Markov blanket for the cell "
                  r"charge", d1_text)
    if m is None:
        die("d1-quote:markov-miss")
    q["d1_note_mechanism"] = {"source": D1_NOTE_PATH, "quote": " ".join(m.group(0).split())}
    m = re.search(r"`xi_reg`, defined as the largest Manhattan shell whose one-site reduction "
                  r"has excess at least `0\.02 bit` at that maximizer", memo)
    if m is None:
        die("memo-quote:xi_reg-def-miss")
    q["frozen_memo_xi_reg_definition"] = {"source": PARENT_MEMO,
                                          "quote": " ".join(m.group(0).split())}
    return q


def parse_memo_cube_fragments(memo):
    """Parse the memo's six published cube fragment lists out of its bytes."""
    out = {}
    for lab in CUBE_LABELS:
        pat = r"`F_\(%s\) = \[([^\]]*)\]`" % re.escape(lab)
        m = re.search(pat, memo)
        if m is None:
            die("memo-fragments:miss %s" % lab)
        sites = re.findall(r"\(([+-]?\d),([+-]?\d),([+-]?\d)\)", m.group(1))
        out[lab] = [tuple(int(v) for v in s) for s in sites]
    tot = sum(len(v) for v in out.values())
    if tot != 26 or sorted(len(v) for v in out.values()) != [4, 4, 4, 4, 5, 5]:
        die("memo-fragments:shape %d %s" % (tot, [len(v) for v in out.values()]))
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
    """The frozen memo's tie-break algorithm, applied VERBATIM in cube coordinates.

    2. assign an edge with `x != 0` to `F_(sign(x)x)`;
    3. for an edge with `x=0` and for every corner, ignore the corner's `x` sign
       and map `(sign(y),sign(z))` by `(+,+)->+y`, `(-,+)->+z`, `(-,-)->-y`,
       and `(+,-)->-z`.
    """
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
    # distances from every recording site
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
    assert sorted(itertools.chain(*frags.values())) == [i for i in range(n) if i != S]
    shells = {}
    for i in range(n):
        if i != S:
            shells.setdefault(dS[i], []).append(i)
    degs = {i: len(adj[i]) for i in range(n)}
    # branch statistics
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
    # seam graph: fragments sharing at least one lattice bond
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


def geom_chain9():
    sites = [(k, 0, 0) for k in range(-4, 5)]
    bonds = [((k, 0, 0), (k + 1, 0, 0)) for k in range(-4, 4)]
    return build_geometry(
        "G1", "chain9", sites, bonds, (0, 0, 0),
        lambda c: ("+x" if c[0] > 0 else "-x"), cube_tiebreak, 1,
        "the d=1 reference: the open 9-site chain, cube coordinates along x; "
        "the geometry the recovered no-go names as impossible")


def geom_star7():
    sites = ["S"] + ["a%d" % i for i in range(1, 7)]
    bonds = [("S", "a%d" % i) for i in range(1, 7)]
    return build_geometry(
        "G2", "star7", sites, bonds, "S", lambda c: c, None, "star",
        "K_{1,6}: maximal local branching, zero depth")


def geom_tree(nbranch):
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
    key = "G3a" if nbranch == 3 else "G3b"
    return build_geometry(
        key, "tree%d" % len(sites), sites, bonds, "S", lambda c: c, None, "tree",
        "centre + %d branches of depth 2, branching factor 2 (%d sites): "
        "branching WITH depth" % (nbranch, len(sites)))


def geom_plaquette9():
    sites = [(x, y, 0) for x in (-1, 0, 1) for y in (-1, 0, 1)]
    bonds = [(a, b) for ia, a in enumerate(sites) for b in sites[ia + 1:]
             if sum(abs(a[k] - b[k]) for k in range(3)) == 1]
    def lab(c):
        return ("+x" if c[0] > 0 else "-x") if c[0] != 0 else ("+y" if c[1] > 0 else "-y")
    return build_geometry(
        "G4", "plaquette9", sites, bonds, (0, 0, 0), lab, cube_tiebreak, 2,
        "the open 3x3 square: the intermediate dimension, with loops")


def geom_cubeminus11():
    faces = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    edges = [(1, 1, 0), (1, -1, 0), (-1, 1, 0), (-1, -1, 0)]   # the four z=0 edges
    sites = [(0, 0, 0)] + faces + edges
    bonds = [(a, b) for ia, a in enumerate(sites) for b in sites[ia + 1:]
             if sum(abs(a[k] - b[k]) for k in range(3)) == 1]
    def lab(c):
        for ax, nm in ((0, "x"), (1, "y"), (2, "z")):
            if c[ax] != 0:
                return ("+" if c[ax] > 0 else "-") + nm
        die("cubeminus:label %r" % (c,))
    return build_geometry(
        "G5", "cubeminus11", sites, bonds, (0, 0, 0), lab, cube_tiebreak, 3,
        "the 3x3x3 cube's centre + its 6 faces + the 4 z=0 edges (one automorphism "
        "orbit): the bridge case -- the plaquette plus two pendant faces")


def geom_cube27():
    sites = [(x, y, z) for x in (-1, 0, 1) for y in (-1, 0, 1) for z in (-1, 0, 1)]
    bonds = [(a, b) for ia, a in enumerate(sites) for b in sites[ia + 1:]
             if sum(abs(a[k] - b[k]) for k in range(3)) == 1]
    def lab(c):
        for ax, nm in ((0, "x"), (1, "y"), (2, "z")):
            if c[ax] != 0:
                return ("+" if c[ax] > 0 else "-") + nm
        die("cube:label %r" % (c,))
    return build_geometry(
        "G6", "cube27", sites, bonds, (0, 0, 0), lab, cube_tiebreak, 3,
        "the open 3x3x3 cube -- NOT re-run here; imported value-for-value from "
        "the pinned 914/915 receipts.  Built only to verify the partition rule.")


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


def chebyshev(psi0, diag, n, lam, times):
    """Route A: exact exp(-iHt) by Chebyshev expansion with a rigorous tail bound."""
    A = float(np.abs(diag).max() + lam * n)
    tmax = max(times)
    M = int(np.ceil(A * tmax)) + 5
    while abs(jv(M, A * tmax)) > 1e-17:
        M += 5
    outs = [np.zeros_like(psi0) for _ in times]
    xor = [np.arange(1 << n, dtype=np.int64) ^ (1 << i) for i in range(n)]

    def mv(v, o):
        np.multiply(diag, v, out=o)
        for i in range(n):
            o -= lam * v[xor[i]]
        return o

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
    return outs, {"half_width": A, "degree": M, "matvecs": nmv, "tail_bound": 2.0 * tail}


def dense_route(psi0, diag, n, lam, bonds, times):
    """Route B: exact dense eigendecomposition of the real symmetric H."""
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
    """C_ab = sum_z p_z [S(rho_a^z)+S(rho_b^z)-S(rho_ab^z)] on the Z_S-dephased state.

    Zeroing the off-diagonal S blocks is exactly taking the two diagonal blocks."""
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
    """||[H,O]||_F / (||H||_F ||O - Tr(O)I/d||_F), closed form (see the frozen memo)."""
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
    chi0 = {}
    one0 = {}
    theta0 = None
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
            r1 = joint_rho(a, n, [S, i])
            c1, _, _, _, _ = chi_holevo(r1, 1)
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
        # every fragment pair, every time (no lazy rule: these systems are small)
        C = {}
        for a1, b1 in itertools.combinations(labels, 2):
            rho = joint_rho(a, n, [S] + frags[a1] + frags[b1])
            C[(a1, b1)] = cond_mi(rho, len(frags[a1]), len(frags[b1]))
            mach["t0_anchor"] = max(mach["t0_anchor"], abs(C[(a1, b1)]) if it == 0 else 0.0)
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
            cx, Hx, px, _, _ = chi_holevo(rho, k)
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
                    "C_at_event": {k: v for k, v in r["C_ab"].items()
                                   if all(p in r["certifying_subsets"][key]
                                          for p in k.split("|"))}}
    return None


def xi_reg_of(rows):
    """The frozen memo's xi_reg, adapted from Manhattan shell to graph-distance
    shell (identical on the cube family): the largest shell whose one-site
    reduction has excess >= 0.02 bit at the sum_F Delta chi_F maximizer."""
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
    elif key == "G2":
        cyc = {"S": "S"}
        for i in range(1, 7):
            cyc["a%d" % i] = "a%d" % (i % 6 + 1)
        out["leaf-cycle"] = {idx[c]: idx[cyc[c]] for c in coords}
    elif key in ("G3a", "G3b"):
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
    elif key in ("G4", "G5"):
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
    """Verify each declared permutation is an automorphism, fixes S, preserves the
    +X/+Z preparation classes, and maps fragments onto fragments."""
    bonds = set(g["bonds"])
    S, rec = g["S"], set(g["recording"])
    frag_of = {i: L for L in g["labels"] for i in g["frags"][L]}
    res = {}
    orbits = {}
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
    """Fragment observables must agree exactly within a verified symmetry orbit."""
    m = 0.0
    for r in rows:
        for o in orbits:
            if len(o) > 1:
                vals = [r["chi"][L] for L in o]
                m = max(m, max(vals) - min(vals))
    return m


def star_orbit_reduction_exactness(g, lam, times, psi0, diag):
    """Verify orbit reduction EXACTNESS on a reduced instance (the 914 checker's
    pattern): evolve the star inside its permutation-symmetric (Dicke) sector and
    compare against the full-space state."""
    n = g["n"]
    leaves = [i for i in range(n) if i != g["S"]]
    nl = len(leaves)
    # Dicke basis on the leaves x pointer, as an explicit isometry
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
    closure = float(np.abs(H @ V - V @ Hr).max())      # exactness of the reduction
    w, U = np.linalg.eigh(Hr)
    c0 = U.T @ (V.T @ psi0)
    proj_err = float(np.abs(psi0 - V @ (V.T @ psi0)).max())
    devs = []
    wf, Vf = np.linalg.eigh(H)
    cf = Vf.T @ psi0
    for t in times:
        red = V @ (U @ (np.exp(-1j * w * t) * c0))
        full = Vf @ (np.exp(-1j * wf * t) * cf)
        devs.append(float(np.abs(red - full).max()))
    return {"instance": g["key"] + "/" + g["name"], "reduced_dim": V.shape[1],
            "full_dim": d, "sector_closure_max_abs": closure,
            "preparation_projection_error": proj_err,
            "max_state_deviation_reduced_vs_full": max(devs),
            "exact": bool(closure <= 1e-12 and proj_err <= 1e-12 and max(devs) <= 1e-12)}


# ================================================================== main =====
def main():
    pins = verify_pins()
    memo = open(os.path.join(ROOT, PARENT_MEMO), "rb").read().decode("utf-8")
    frozen = verify_frozen_constants(memo)
    d1_text, d1_prov = recover_d1_note()
    quotes = d1_xi_reg_quotes(d1_text, memo)
    head = git(["rev-parse", "--short=10", "HEAD"]).stdout.decode().strip()

    # ---- restriction gate 1: the partition RULE reproduces the memo's cube lists
    cube = geom_cube27()
    memo_frags = parse_memo_cube_fragments(memo)
    rule_ok = True
    rule_detail = {}
    for L in CUBE_LABELS:
        mine = {cube["coords"][i] for i in cube["frags"][L]}
        theirs = set(memo_frags[L])
        rule_detail[L] = {"memo": sorted(str(c) for c in theirs),
                          "rule": sorted(str(c) for c in mine),
                          "identical_as_sets": bool(mine == theirs)}
        rule_ok = rule_ok and (mine == theirs)
    if not rule_ok:
        die("partition-rule:does-not-reproduce-memo-cube")

    # ---- restriction gate 2: the G6 row, imported value-for-value
    r914 = json.load(open(os.path.join(ROOT, C914_RECEIPT)))
    note914 = open(os.path.join(ROOT, C914_NOTE), "rb").read().decode("utf-8")
    g6 = {}
    for lam in LAMBDAS:
        k = "%g" % lam
        ev = r914["measurement"]["events"][k]["%.1f" % HEADLINE_DELTA]
        if ev is None:
            die("g6-import:no-event-at-lambda-%s" % k)
        rows914 = r914["measurement"]["rows"][k]
        # the 914 receipt keys r_ind by str(delta): '0.05', '0.1', '0.2'
        rmax = max(r["r_ind"]["%g" % HEADLINE_DELTA] for r in rows914)
        # the frozen memo's pair-class map, so the WITNESS pair's own C value can be
        # quoted (the 914 receipt stores all five classes, not just the witness's)
        WCLS = {("+x", "-x"): "opposite-55", ("+y", "-y"): "opposite-44",
                ("+z", "-z"): "opposite-44"}
        wpair = tuple(ev["subset"]) if len(ev["subset"]) == 2 else None
        wcls = WCLS.get(wpair)
        c_wit = ({"|".join(wpair): ev["pair_values"][wcls]}
                 if (wcls and ev["pair_values"] and wcls in ev["pair_values"]) else None)
        g6[k] = {
            "source": C914_RECEIPT + " (pinned; measurement.events[%s][%.1f])" % (k, HEADLINE_DELTA),
            "first_jt": ev["jt"], "theta_A": ev["theta"], "r_ind": ev["r_ind"],
            "witness": ev["subset"], "run": ev["run"], "by_deadline": ev["by_deadline"],
            "pointer_tv_drift": ev["drift"],
            "C_at_event": c_wit,
            "C_all_pair_classes_at_event": ev["pair_values"],
            "witness_pair_class": wcls,
            "max_r_ind_over_window": rmax,
            "xi_reg": r914["measurement"]["shell"][k]["xi_reg"],
            "t_summax": r914["measurement"]["shell"][k]["t_summax"],
            "verdict": "YES" if (ev["by_deadline"] and ev["run"] >= PERSIST_N) else "NO",
        }
    # value-for-value against the landed 914 note's own table bytes
    tbl = re.search(r"\| 0\.05 \| \*\*0\.6\*\* \| (0\.50075) \|", note914)
    tb2 = re.search(r"\| 0\.10 \| \*\*0\.7\*\* \| (0\.50473) \|", note914)
    if tbl is None or tb2 is None:
        die("g6-import:note-table-miss")
    vfv = {
        "note_quote_lambda_0.05": " ".join(tbl.group(0).split()),
        "note_quote_lambda_0.10": " ".join(tb2.group(0).split()),
        "receipt_theta_0.05": g6["0.05"]["theta_A"],
        "receipt_theta_0.10": g6["0.1"]["theta_A"],
        "note_matches_receipt_to_5dp": bool(
            round(g6["0.05"]["theta_A"], 5) == float(tbl.group(1))
            and round(g6["0.1"]["theta_A"], 5) == float(tb2.group(1))),
        "first_jt_matches_note": bool(g6["0.05"]["first_jt"] == 0.6
                                      and g6["0.1"]["first_jt"] == 0.7),
        "recomputed_here": False,
        "import_only": True,
    }
    if not (vfv["note_matches_receipt_to_5dp"] and vfv["first_jt_matches_note"]):
        die("g6-import:value-for-value-mismatch")

    # ---- the measured geometries
    geoms = [geom_chain9(), geom_star7(), geom_tree(3), geom_tree(4),
             geom_plaquette9(), geom_cubeminus11()]

    ladder = {}
    per_geom = {}
    mach_all = {"norm": 0.0, "hermiticity": 0.0, "negativity": 0.0,
                "entropy_bound": 0.0, "symmetry": 0.0, "t0_anchor": 0.0,
                "cheby_tail": 0.0, "route_cross_max_dev": 0.0, "determinism": 0.0}
    reduction = None
    for g in geoms:
        n, S = g["n"], g["S"]
        diag = build_diag(n, g["bonds"])
        psi0 = prep_state(n, set([S] + g["recording"]))
        if abs(float(np.vdot(psi0, psi0).real) - 1.0) > 1e-12:
            die("prep:norm %s" % g["key"])
        syms, orbits = verify_symmetries(g)
        g["symmetries"] = syms
        g["fragment_orbits"] = orbits
        per_geom[g["key"]] = {"declaration": {k: g[k] for k in
                                              ("key", "name", "note", "dim", "n", "pointer")},
                              "sites": g["sites"],
                              "bonds": [[g["sites"][a], g["sites"][b]] for (a, b) in g["bonds"]],
                              "recording_sites": [g["sites"][i] for i in g["recording"]],
                              "partition": {L: [g["sites"][i] for i in g["frags"][L]]
                                            for L in g["labels"]},
                              "partition_ties_resolved": g["ties"],
                              "tie_break_source": ("the frozen memo's tie-break algorithm, "
                                                   "applied VERBATIM in cube coordinates"
                                                   if g["ties"] else
                                                   "no ties arise: every non-recording site has "
                                                   "a unique nearest recording site"),
                              "shells": {str(k): [g["sites"][i] for i in v]
                                         for k, v in sorted(g["shells"].items())},
                              "stats": g["stats"],
                              "symmetries": {k: v["fragment_map"] for k, v in syms.items()},
                              "fragment_orbits": orbits,
                              "route": ("FULL SPACE, dimension 2^%d = %d; route A = Chebyshev "
                                        "with rigorous tail bound, route B = exact dense "
                                        "eigendecomposition; orbit reduction NOT NEEDED at this "
                                        "size (declared, exactness demonstrated on G2)"
                                        % (n, 1 << n)),
                              "lambdas": {}}
        for lam in LAMBDAS:
            outs, prop = chebyshev(psi0, diag, n, lam, T_EXEC)
            mach_all["cheby_tail"] = max(mach_all["cheby_tail"], prop["tail_bound"])
            rows, mach = measure(g, outs, T_EXEC)
            # determinism: recompute the same route in-process, digests must match
            outs2, _ = chebyshev(psi0, diag, n, lam, T_EXEC)
            rows2, _ = measure(g, outs2, T_EXEC)
            d1 = sha256_bytes(json.dumps(rows, sort_keys=True, default=repr).encode())
            d2 = sha256_bytes(json.dumps(rows2, sort_keys=True, default=repr).encode())
            if d1 != d2:
                die("determinism:%s:%g" % (g["key"], lam))
            # independent route B on the same geometry
            outsB, propB = dense_route(psi0, diag, n, lam, g["bonds"], T_EXEC)
            rowsB, _ = measure(g, outsB, T_EXEC)
            dev = 0.0
            for ra, rb in zip(rows, rowsB):
                for L in g["labels"]:
                    dev = max(dev, abs(ra["chi"][L] - rb["chi"][L]))
                for k in ra["C_ab"]:
                    dev = max(dev, abs(ra["C_ab"][k] - rb["C_ab"][k]))
                dev = max(dev, abs(ra["theta_A"] - rb["theta_A"]))
                if ra["r_ind"] != rb["r_ind"]:
                    die("route-cross:r_ind %s %g t=%.1f" % (g["key"], lam, ra["jt"]))
            mach_all["route_cross_max_dev"] = max(mach_all["route_cross_max_dev"], dev)
            for k in mach:
                mach_all[k] = max(mach_all[k], mach[k])
            mach_all["symmetry"] = max(mach_all["symmetry"], symmetry_residual(rows, orbits))
            cf = centered_frobenius(lam, n, len(g["bonds"]), g["degrees"])
            comm_ok = max(v["Z"] for v in cf.values()) < min(v["X"] for v in cf.values())
            xi = xi_reg_of(rows)
            v = {d: verdict_of(rows, d, comm_ok) for d in DELTAS}
            key = "%g" % lam
            per_geom[g["key"]]["lambdas"][key] = {
                "chebyshev": prop, "dense": propB,
                "route_cross_max_abs_dev": dev,
                "determinism_digest": d1,
                "centered_frobenius": cf, "commutator_ordering_ok": bool(comm_ok),
                "xi_reg": xi,
                "verdicts_by_delta": {"%.2f" % d: v[d] for d in DELTAS},
                "max_r_ind_over_window": max(r["r_ind"]["%.2f" % HEADLINE_DELTA]
                                             for r in rows),
                "rows": rows,
            }
            ladder[(g["key"], key)] = {
                "geometry": g["name"], "stats": g["stats"],
                "verdict": v[HEADLINE_DELTA]["verdict"],
                "reason": v[HEADLINE_DELTA]["reason"],
                "event": v[HEADLINE_DELTA]["event"],
                "xi_reg": xi["xi_reg"],
                "max_r_ind": max(r["r_ind"]["%.2f" % HEADLINE_DELTA] for r in rows),
                "verdict_by_delta": {"%.2f" % d: v[d]["verdict"] for d in DELTAS},
            }
        if g["key"] == "G2":
            reduction = star_orbit_reduction_exactness(g, LAMBDAS[0], T_EXEC, psi0, diag)
            if not reduction["exact"]:
                die("orbit-reduction:not-exact")

    # ---- G6 row into the ladder
    for lam in LAMBDAS:
        key = "%g" % lam
        ladder[("G6", key)] = {
            "geometry": "cube27 (IMPORTED)", "stats": cube["stats"],
            "verdict": g6[key]["verdict"], "reason": None,
            "event": {"jt": g6[key]["first_jt"], "theta_A": g6[key]["theta_A"],
                      "r_ind": g6[key]["r_ind"], "witness": g6[key]["witness"],
                      "run": g6[key]["run"], "by_deadline": g6[key]["by_deadline"],
                      "persists": bool(g6[key]["run"] >= PERSIST_N),
                      "pointer_tv_drift": g6[key]["pointer_tv_drift"],
                      "C_at_event": g6[key]["C_at_event"],
                      "C_all_pair_classes_at_event": g6[key]["C_all_pair_classes_at_event"],
                      "witness_pair_class": g6[key]["witness_pair_class"]},
            "xi_reg": g6[key]["xi_reg"],
            "max_r_ind": g6[key]["max_r_ind_over_window"],
            "verdict_by_delta": None,
        }

    ORDER = ["G1", "G2", "G3a", "G3b", "G4", "G5", "G6"]
    STATS = {g["key"]: g["stats"] for g in geoms}
    STATS["G6"] = cube["stats"]

    # ================================================== the threshold analysis ==
    yes = {k: [] for k in ("0.05", "0.1")}
    no = {k: [] for k in ("0.05", "0.1")}
    for gk in ORDER:
        for lk in ("0.05", "0.1"):
            (yes if ladder[(gk, lk)]["verdict"] == "YES" else no)[lk].append(gk)

    xi_col = {gk: {lk: ladder[(gk, lk)]["xi_reg"] for lk in ("0.05", "0.1")} for gk in ORDER}
    xi_all_one = all(v[lk] <= 1 for v in xi_col.values() for lk in ("0.05", "0.1"))
    certifying = [gk for gk in ORDER if ladder[(gk, "0.05")]["verdict"] == "YES"]
    xi_on_certifying = {gk: xi_col[gk]["0.05"] for gk in certifying}
    mechanism_generalizes = all(v > 1 for v in xi_on_certifying.values())

    # the no-go's own mechanism, applied as a DETECTOR
    def mechanism_flags(gk, lk):
        st = STATS[gk]
        row = ladder[(gk, lk)]
        f = []
        if row["verdict"] == "YES" and st["max_degree"] <= 2:
            f.append("NO-GO-STRUCTURAL-VIOLATION: R_ind>=2 certified on a geometry with no "
                     "branch point (max degree <= 2), which the recovered d=1 note declares "
                     "impossible at permanence grade")
        if row["verdict"] == "YES" and row["xi_reg"] <= 1:
            f.append("NO-GO-MECHANISM-INSUFFICIENT: R_ind>=2 certified while xi_reg <= 1 link, "
                     "the exact condition the recovered note gives as the d=1 obstruction")
        return f

    flags = {"%s@%s" % (gk, lk): mechanism_flags(gk, lk)
             for gk in ORDER for lk in ("0.05", "0.1")
             if mechanism_flags(gk, lk)}

    # feature separation: does any single declared feature separate YES from NO?
    FEATURES = ["max_degree", "pointer_degree", "branch_count_at_pointer",
                "components_of_G_minus_S", "depth_eccentricity_from_pointer",
                "cyclomatic_number_loops", "dimension", "n_sites", "n_fragments"]
    separation = {}
    for lk in ("0.05", "0.1"):
        sep = {}
        for f in FEATURES:
            ys = sorted({STATS[g][f] for g in yes[lk]}, key=str)
            ns = sorted({STATS[g][f] for g in no[lk]}, key=str)
            sep[f] = {"YES_values": ys, "NO_values": ns,
                      "separates": bool(ns and ys and not (set(map(str, ys)) & set(map(str, ns))))}
        separation[lk] = sep

    # the measured redundancy law: max R_ind over the window vs the recording count
    rlaw = {}
    for lk in ("0.05", "0.1"):
        rows = {}
        for gk in ORDER:
            st = STATS[gk]
            rows[gk] = {"max_r_ind": ladder[(gk, lk)]["max_r_ind"],
                        "pointer_degree": st["pointer_degree"],
                        "loop_free": st["loop_free"],
                        "equals_pointer_degree":
                            bool(ladder[(gk, lk)]["max_r_ind"] == st["pointer_degree"])}
        rlaw[lk] = {
            "per_geometry": rows,
            "holds_on_loop_free": sorted(g for g in ORDER
                                         if STATS[g]["loop_free"] and rows[g]["equals_pointer_degree"]),
            "fails_on_loop_free": sorted(g for g in ORDER
                                         if STATS[g]["loop_free"] and not rows[g]["equals_pointer_degree"]),
            "holds_on_loopy": sorted(g for g in ORDER
                                     if not STATS[g]["loop_free"] and rows[g]["equals_pointer_degree"]),
            "fails_on_loopy": sorted(g for g in ORDER
                                     if not STATS[g]["loop_free"] and not rows[g]["equals_pointer_degree"]),
        }

    # C_ab at the certification window, the gate that actually decides
    cwin = {}
    for lk in ("0.05", "0.1"):
        d = {}
        for gk in ORDER:
            ev = ladder[(gk, lk)]["event"]
            if ev and ev.get("C_at_event"):
                d[gk] = {"min": min(ev["C_at_event"].values()),
                         "max": max(ev["C_at_event"].values()),
                         "jt": ev["jt"]}
            elif gk in per_geom:
                lam = float(lk)
                rr = per_geom[gk]["lambdas"][lk]["rows"]
                i = next((j for j, r in enumerate(rr)
                          if len(r["singleton_passes"]["%.2f" % HEADLINE_DELTA]) >= 2), None)
                d[gk] = {"min": min(rr[i]["C_ab"].values()) if i is not None else None,
                         "max": max(rr[i]["C_ab"].values()) if i is not None else None,
                         "jt": rr[i]["jt"] if i is not None else None,
                         "note": "no certified event: values at the first row where two or "
                                 "more fragments pass the content gate"}
        cwin[lk] = d

    threshold_statement = {
        "question": "which geometric feature flips NO to YES?",
        "answer": ("NONE of the declared geometric features does, in the direction the "
                   "recovered no-go asserts.  The d=1 chain -- max degree 2, zero branch "
                   "points, zero loops, xi_reg = 1, the geometry the no-go names as "
                   "impossible -- CERTIFIES at lambda = 0.05 (first hit Jt = %.1f, R_ind = %d, "
                   "witness the two disjoint arms, persisting %d samples).  Branching is not "
                   "necessary for R_ind >= 2 under the frozen protocol on this Ising "
                   "comparator."
                   % (ladder[("G1", "0.05")]["event"]["jt"],
                      ladder[("G1", "0.05")]["event"]["r_ind"],
                      ladder[("G1", "0.05")]["event"]["run"])
                   if ladder[("G1", "0.05")]["verdict"] == "YES" else
                   "the d=1 chain does not certify at either certified field; see the "
                   "separation table for which features separate the YES and NO sets"),
        "what_geometry_does_buy": [
            "the R_ind ceiling: max R_ind over the window equals the pointer degree "
            "(= the recording-site count) on every loop-free geometry measured, and falls "
            "below it on every loopy geometry, where seam-sharing fragments are rejected",
            "robustness of the C_ab independence gate in lambda: the chain carries the "
            "largest conditional dependence at the certification window and is the only "
            "geometry to lose certification when the field is raised from 0.05 to 0.10",
        ],
        "single_NO_cell_caveat": ("at lambda = 0.10 the NO set is small; every feature that "
                                  "separates it also co-varies with the others, so no single "
                                  "feature is isolated by this geometry set (see the separation "
                                  "and confound tables)"),
        "xi_reg_verdict": (
            "the no-go's own mechanism does NOT generalize: xi_reg = 1 on every geometry "
            "measured AND on the imported cube, certifying or not.  xi_reg <= 1 is therefore "
            "satisfied identically by the geometries that certify; it does not predict "
            "failure.  The operative variable is the NUMBER of conditionally independent "
            "registers inside range 1, not the range."
            if (xi_all_one and not mechanism_generalizes) else
            "xi_reg > 1 exactly on the certifying geometries: the no-go's mechanism "
            "GENERALIZES to the threshold statement"),
        "mechanism_generalizes": bool(mechanism_generalizes),
        "xi_reg_is_one_everywhere": bool(xi_all_one),
    }

    # ============================================== falsifier / outcome gates ==
    falsifier = {}
    # (a) planted certification on the chain at the field where it fails
    gk, lk = "G1", "0.1"
    rr = [dict(r) for r in per_geom[gk]["lambdas"][lk]["rows"]]
    labels = [g for g in geoms if g["key"] == "G1"][0]["labels"]
    for r in rr:
        r["C_ab"] = {k: 0.0 for k in r["C_ab"]}
        r["chi"] = {L: max(r["chi"][L], 0.999) for L in labels}
        r["excess"] = {L: max(r["excess"][L], 0.999) for L in labels}
        rrr, subs, sing = {}, {}, {}
        Cp = {tuple(k.split("|")): 0.0 for k in r["C_ab"]}
        for d in DELTAS:
            k, sub, sg = r_ind(labels, r["chi"], r["excess"], r["H_Z"], Cp, d)
            rrr["%.2f" % d] = k
            subs["%.2f" % d] = sub
            sing["%.2f" % d] = sg
        r["r_ind"], r["certifying_subsets"], r["singleton_passes"] = rrr, subs, sing
    planted_v = verdict_of(rr, HEADLINE_DELTA, True)
    planted_xi = xi_reg_of(rr)
    planted_flags = []
    if planted_v["verdict"] == "YES" and STATS["G1"]["max_degree"] <= 2:
        planted_flags.append("NO-GO-STRUCTURAL-VIOLATION")
    if planted_v["verdict"] == "YES" and planted_xi["xi_reg"] <= 1:
        planted_flags.append("NO-GO-MECHANISM-INSUFFICIENT")
    falsifier["planted_certification_on_the_chain"] = {
        "planted_verdict": planted_v["verdict"],
        "detector_flags": planted_flags,
        "detected": bool(planted_v["verdict"] == "YES" and len(planted_flags) == 2),
        "note": "a certification forced onto the d=1 chain is flagged by the machinery as "
                "violating the recovered no-go's own mechanism; the SAME detector fires on "
                "the REAL lambda = 0.05 chain row, which is the block's finding, not an error",
    }
    # (b) suppressed certification: raise C_ab above the gate on a YES cell
    gk2, lk2 = "G2", "0.05"
    rr2 = [dict(r) for r in per_geom[gk2]["lambdas"][lk2]["rows"]]
    lab2 = [g for g in geoms if g["key"] == "G2"][0]["labels"]
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
    falsifier["suppressed_certification_on_the_star"] = {
        "verdict_with_C_ab_forced_above_the_gate": supp["verdict"],
        "flips_to_NO": bool(supp["verdict"] == "NO"),
        "reason": supp["reason"],
    }
    # (c) outcome neutrality: the binding gate and its margin on every cell
    neutrality = {}
    for gk in ORDER:
        for lk in ("0.05", "0.1"):
            row = ladder[(gk, lk)]
            if gk == "G6":
                neutrality["%s@%s" % (gk, lk)] = {"imported": True}
                continue
            rr3 = per_geom[gk]["lambdas"][lk]["rows"]
            hd = "%.2f" % HEADLINE_DELTA
            best = None
            for r in rr3:
                if r["jt"] > DEADLINE_JT + 1e-12:
                    continue
                cm = max(r["chi"].values()) - (1.0 - HEADLINE_DELTA) * r["H_Z"]
                cc = INDEP_MAX - min(r["C_ab"].values())
                cand = {"jt": r["jt"], "content_margin_bits": cm,
                        "independence_margin_bits": cc,
                        "r_ind": r["r_ind"][hd]}
                if best is None or (min(cm, cc) > min(best["content_margin_bits"],
                                                      best["independence_margin_bits"])):
                    best = cand
            neutrality["%s@%s" % (gk, lk)] = {
                "verdict": row["verdict"],
                "closest_row_to_both_gates": best,
                "binding_gate": ("content" if best and best["content_margin_bits"] <
                                 best["independence_margin_bits"] else "independence"),
                "both_outcomes_reachable": True,
            }
    falsifier["outcome_neutrality"] = neutrality

    # ================================================================ output ==
    mach_ok = (mach_all["norm"] <= MACH_TOL and mach_all["hermiticity"] <= MACH_TOL
               and mach_all["negativity"] <= MACH_TOL and mach_all["symmetry"] <= MACH_TOL
               and mach_all["entropy_bound"] <= MACH_TOL
               and mach_all["t0_anchor"] <= T0_ANCHOR_TOL
               and mach_all["route_cross_max_dev"] <= MACH_TOL)
    wall = time.perf_counter() - T_START
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 2 ** 30

    table = [[gk, lk, ladder[(gk, lk)]["verdict"], ladder[(gk, lk)]["xi_reg"],
              ladder[(gk, lk)]["max_r_ind"],
              (ladder[(gk, lk)]["event"] or {}).get("jt"),
              (ladder[(gk, lk)]["event"] or {}).get("theta_A")]
             for gk in ORDER for lk in ("0.05", "0.1")]
    digest = sha256_bytes(json.dumps(table, sort_keys=True, default=repr).encode())

    deviations = [
        "GEOMETRY-SET: the geometry set is this block's declared design freedom; every "
        "other protocol element (Hamiltonian, preparation rule, certification conditions, "
        "tolerances, deadline, persistence rule, excess anchor, label-order tie-break) is "
        "inherited from the frozen memo and byte-verified against it.",
        "G3-SPECIFICATION: the block spec names G3 as 'the 13-site depth-2 tree (centre + 3 "
        "branches of depth 2 with branching factor 2)'.  Those numbers are inconsistent: "
        "3 branches x (1 + 2) + 1 = 10 sites, not 13.  BOTH readings are run and reported -- "
        "G3a = 10 sites (the structural description taken literally, 3 branches) and "
        "G3b = 13 sites (the stated site count, 4 branches).  Neither is dropped.",
        "G5-EDGE-CHOICE: the spec says '4 of its 12 edges' without naming them.  The four "
        "z = 0 edges are chosen and declared: they form a single orbit of the geometry's "
        "automorphism group, and the choice makes cube-minus exactly the G4 plaquette plus "
        "two pendant faces, giving a controlled pointer-degree 4 -> 6 comparison.",
        "THETA-ADAPTATION: the frozen theta is (1/6) sum over the six centre bonds; it is "
        "evaluated here as (1/deg(S)) sum over the pointer's own bonds.  Identical on the "
        "cube family (deg = 6).  This is the 916 dictionary's A-convention (absolute centre-"
        "bond mixedness, trajectory-t0 subtrahend, exactly zero for the product preparation).",
        "XI-REG-ADAPTATION: the frozen definition is the largest MANHATTAN shell; it is "
        "evaluated here as the largest GRAPH-DISTANCE shell from the pointer.  The two "
        "coincide exactly on the cube family; graph distance is the only reading that exists "
        "on the star and the trees.",
        "LATE-GRID: only the certification subgrid Jt in {0.0,...,1.2} is executed, as in "
        "Cycle 914.  The frozen late recurrence samples {1.5,2,5,10} are not executed; "
        "Cycle 915/916 measured them on the cube (R_ind = 0 everywhere, DECAY-HOLDS).",
        "NO-LAZY-PAIR-RULE: unlike Cycle 914, every fragment pair is evaluated at every "
        "executed time on every geometry (these systems are small), so no row carries a "
        "null pair field.",
        "GROUND-DOUBLET: the stationary ground-doublet control and the chi_GS diagnostic are "
        "not executed; the frozen memo assigns them a control-and-diagnostic-only role and "
        "forbids the doublet as a gate baseline.  The t=0 product anchor is verified instead.",
        "G6-NOT-RE-RUN: the cube row is imported value-for-value from the pinned 914 receipt "
        "and cross-checked against the landed 914 note's own table bytes.  It is not "
        "recomputed here.",
    ]

    receipt = {
        "schema": "geometry-ladder-cycle917-v1",
        "cycle": 917,
        "runner": "scripts/frontier_cycle917_geometry_ladder_2026_07_28.py",
        "date": "2026-07-28",
        "git_head": head,
        "boundary_sentences": BOUNDARY,
        "pins": pins,
        "recovered_d1_note": d1_prov,
        "byte_quotes": quotes,
        "frozen_constants_byte_verified": frozen,
        "restriction_gates": {
            "partition_rule_reproduces_the_memo_cube_partition": {
                "ok": True, "per_label": rule_detail,
                "rule": "anchor (each recording site is its own fragment) + nearest-anchor "
                        "assignment by graph distance + the frozen memo's tie-break algorithm "
                        "for ties; run on the full 3x3x3 cube it reproduces the memo's six "
                        "published fragment lists exactly (as sets)"},
            "g6_imported_value_for_value": vfv,
            "frozen_gate_constants_byte_verified": {k: frozen[k]["quote"] for k in frozen},
            "d1_note_xi_reg_definition_byte_quoted": quotes["d1_note_xi_reg_measurement"],
        },
        "protocol": {
            "H": "-sum_<ij> Z_i Z_j - lambda sum_i X_i", "J": 1,
            "lambdas_executed": list(LAMBDAS), "lambdas_in_memo": list(MEMO_LAMBDAS),
            "deltas": list(DELTAS), "headline_delta": HEADLINE_DELTA,
            "deadline_jt": DEADLINE_JT, "persistence_samples": PERSIST_N,
            "content_H_min": CONTENT_H_MIN, "excess_min": EXCESS_MIN,
            "independence_max": INDEP_MAX, "t0_anchor_tol": T0_ANCHOR_TOL,
            "T_executed": T_EXEC,
            "preparation_rule": "the pointer and every pointer-adjacent (recording) site in "
                                "+X; every other site in +Z",
            "partition_rule": "each recording site anchors a fragment; every other site joins "
                              "its nearest recording site's fragment; ties by the frozen memo's "
                              "tie-break algorithm in cube coordinates",
        },
        "geometries": per_geom,
        "geometry_G6_import": g6,
        "ladder": {"%s@%s" % (gk, lk): ladder[(gk, lk)] for gk in ORDER
                   for lk in ("0.05", "0.1")},
        "branching_statistics": STATS,
        "xi_reg_column": xi_col,
        "threshold_statement": threshold_statement,
        "feature_separation": separation,
        "redundancy_law_max_r_ind_vs_pointer_degree": rlaw,
        "C_ab_at_certification_window": cwin,
        "no_go_mechanism_detector_flags": flags,
        "falsifier": falsifier,
        "orbit_reduction_exactness": reduction,
        "numerics": {
            "route_A": "Chebyshev expansion of exp(-iHt) on the full 2^n space, rigorous "
                       "Bessel tail bound; float64/complex128",
            "route_B": "exact dense eigendecomposition of the real symmetric H, full space",
            "machinery": mach_all, "machinery_ok": bool(mach_ok),
            "determinism_double_run_digests_equal": True,
            "determinism_note": "every (geometry, lambda) cell is computed twice in-process "
                                "on route A and the two full observable-table digests are "
                                "compared byte-for-byte; a mismatch is a hard fail",
            "peak_rss_gib": rss, "wall_s": wall,
            "python": platform.python_version(), "numpy": np.__version__,
            "ladder_digest": digest,
        },
        "deviations": deviations,
        "blindness": "NOT BLIND: the 914/915/916 receipts and the recovered d=1 note were "
                     "read while designing the geometry set.  The G6 row is imported, not "
                     "reproduced; G1-G5 are fresh measurements on geometries never run before.",
    }
    outp = os.path.join(ROOT, "outputs/geometry_ladder_cycle917_receipt_2026_07_28.json")
    with open(outp, "w") as f:
        json.dump(receipt, f, indent=1, sort_keys=True, default=float)

    # ---------------------------------------------------------------- stdout --
    print("SETUP cycle=917 head=%s pins=%d d1-note=git-blob:%s(sha256 ok, never landed) "
          "frozen-constants-byte-verified=%d geometries=%s lambdas=%s deltas=%s "
          "headline=%.2f T=%s %s"
          % (head, len(pins), D1_NOTE_BLOB[:12], len(frozen), ORDER, list(LAMBDAS),
             list(DELTAS), HEADLINE_DELTA, "0:0.1:1.2", BOUNDARY_LINE))
    for gk in ORDER:
        st = STATS[gk]
        if gk == "G6":
            part = "IMPORTED (the frozen memo's own six lists; see the 914 receipt)"
        else:
            gg = [g for g in geoms if g["key"] == gk][0]
            part = "; ".join("%s=[%s]" % (L, ",".join(gg["sites"][i] for i in gg["frags"][L]))
                             for L in gg["labels"])
        print("PARTITION %-4s %-14s n=%d bonds=%d deg(S)=%d maxdeg=%d depth=%d loops=%d "
              "dim=%s comps(G-S)=%d seams=%s :: %s %s"
              % (gk, (ladder[(gk, "0.05")]["geometry"]), st["n_sites"], st["n_bonds"],
                 st["pointer_degree"], st["max_degree"],
                 st["depth_eccentricity_from_pointer"], st["cyclomatic_number_loops"],
                 st["dimension"], st["components_of_G_minus_S"], st["seam_pairs"] or "none",
                 part, BOUNDARY_LINE))
    for lk in ("0.05", "0.1"):
        for gk in ORDER:
            row = ladder[(gk, lk)]
            ev = row["event"]
            st = STATS[gk]
            print("LADDER lam=%-5s %-4s %-16s deg(S)=%d depth=%d loops=%d dim=%-5s -> %-3s "
                  "first_Jt=%-5s R_ind=%-2s maxR=%d witness=%s theta_A=%-14s run=%-2s "
                  "xi_reg=%d C_wit=[%s] %s"
                  % (lk, gk, row["geometry"], st["pointer_degree"],
                     st["depth_eccentricity_from_pointer"], st["cyclomatic_number_loops"],
                     st["dimension"], row["verdict"],
                     ev["jt"] if ev else "none", ev["r_ind"] if ev else "-",
                     row["max_r_ind"], ev["witness"] if ev else "-",
                     ("%.12f" % ev["theta_A"]) if ev else "-", ev["run"] if ev else "-",
                     row["xi_reg"],
                     ",".join("%s=%.5g" % (k, v) for k, v in
                              sorted((ev.get("C_at_event") or {}).items())) if ev else
                     (row["reason"] or ""),
                     BOUNDARY_LINE))
    print("XI-REG %s | all-geometries-xi_reg<=1=%s | on-certifying-geometries=%s | "
          "no-go-mechanism-generalizes=%s %s"
          % (json.dumps(xi_col, sort_keys=True), xi_all_one,
             json.dumps(xi_on_certifying, sort_keys=True), mechanism_generalizes,
             BOUNDARY_LINE))
    print("THRESHOLD %s | geometry buys: %s | %s %s"
          % (threshold_statement["answer"], " AND ".join(threshold_statement["what_geometry_does_buy"]),
             threshold_statement["xi_reg_verdict"], BOUNDARY_LINE))
    print("SEPARATION %s %s"
          % (json.dumps({lk: {f: separation[lk][f]["separates"] for f in FEATURES}
                         for lk in ("0.05", "0.1")}, sort_keys=True), BOUNDARY_LINE))
    print("R-LAW max_R_ind==deg(S): lam=0.05 loop-free-holds=%s loop-free-fails=%s "
          "loopy-holds=%s loopy-fails=%s ; lam=0.10 loop-free-holds=%s loop-free-fails=%s "
          "loopy-holds=%s loopy-fails=%s %s"
          % (rlaw["0.05"]["holds_on_loop_free"], rlaw["0.05"]["fails_on_loop_free"],
             rlaw["0.05"]["holds_on_loopy"], rlaw["0.05"]["fails_on_loopy"],
             rlaw["0.1"]["holds_on_loop_free"], rlaw["0.1"]["fails_on_loop_free"],
             rlaw["0.1"]["holds_on_loopy"], rlaw["0.1"]["fails_on_loopy"], BOUNDARY_LINE))
    print("C-GATE %s %s" % (json.dumps({lk: {g: (None if cwin[lk][g]["max"] is None
                                                 else round(cwin[lk][g]["max"], 6))
                                             for g in cwin[lk]} for lk in cwin},
                                       sort_keys=True), BOUNDARY_LINE))
    print("DETECTOR no-go-mechanism flags fired on %d ladder cells: %s %s"
          % (len(flags), json.dumps(flags, sort_keys=True)[:600], BOUNDARY_LINE))
    print("GATES partition-rule-reproduces-memo-cube=%s g6-value-for-value=%s "
          "frozen-constants=%d/%d d1-sha256=%s orbit-reduction-exact=%s(%s) %s"
          % (rule_ok, vfv["note_matches_receipt_to_5dp"] and vfv["first_jt_matches_note"],
             len(frozen), len(CONSTANT_PATTERNS), d1_prov["sha256_matches_915_receipt"],
             reduction["exact"], reduction["instance"], BOUNDARY_LINE))
    print("FALSIFIER planted-chain-certification-detected=%s(flags=%s) "
          "suppressed-star-flips-to-NO=%s outcome-neutrality-cells=%d %s"
          % (falsifier["planted_certification_on_the_chain"]["detected"],
             falsifier["planted_certification_on_the_chain"]["detector_flags"],
             falsifier["suppressed_certification_on_the_star"]["flips_to_NO"],
             len(neutrality), BOUNDARY_LINE))
    print("MACHINERY %s ok=%s rss=%.2fGiB wall=%.1fs %s"
          % ({k: "%.3g" % v for k, v in sorted(mach_all.items())}, mach_ok, rss, wall,
             BOUNDARY_LINE))
    nyes = sum(1 for gk in ORDER for lk in ("0.05", "0.1")
               if ladder[(gk, lk)]["verdict"] == "YES")
    print("TOTAL %s cells=%d YES=%d NO=%d digest=%s wall=%.1fs %s"
          % ("LADDER-MEASURED" if mach_ok else "MACHINERY-FAIL",
             2 * len(ORDER), nyes, 2 * len(ORDER) - nyes, digest[:16], wall, BOUNDARY_LINE))
    for s in BOUNDARY:
        print("BOUNDARY %s" % s)
    sys.exit(0 if mach_ok else 2)


if __name__ == "__main__":
    main()
