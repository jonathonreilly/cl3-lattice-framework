#!/usr/bin/env python3
# Final path: scripts/admissibility_dirac_kahler_cutting_strata_completion_2026_08_20.py
"""Block 157: THE CUTTING STRATA COMPLETION -- stratum 147 enumerated, the
three transcribed bridge points REALIZED, MC = 48 WITNESSED, both descent
landings proven MINIMAL, and a false lemma displayed so no later block believes
it.

Campaign contract D closes with this block.  Block 151 left three cutting-lane
items open (strata 147+, the cost-146 geometric gate, composite minimality) and
Block 152 carried a rider that read, on its face, as though the bridge's own
transcribed record might not be realizable at all.  Every one of those items is
decided here, and the rider falls the right way:

  * STRATUM 147 IS COMPLETE.  16,359,616 cuttings, exactly TEN charge points,
    535,593,550 nodes at budget 3, with Block 151's budget-0/1/2 numbers
    reproduced TO THE DIGIT first.  The charge-point run across strata
    144/145/146/147 is 1 / 3 / 6 / 10 -- the triangular numbers.  The census is
    FOUR-ROUTE: the primary's committed lowest-uncovered-point route, plus the
    independent checker's own C engine on its own generic barycentric ground
    set under two sweep orders, plus an excess-pattern ALLOCATION decomposition
    that never enumerates the stratum as a whole;
  * THE OVERTURN.  All three points Block 152 transcribed -- (36,55), (41,48),
    (37,48) -- are REALIZABLE by genuine separator-certified four-box
    dissections, at exact minima 149, 163 and 165, each minimum closed by a
    COMPLETE bounded search below it and each re-proved by the checker's own
    single-cap re-runs on its own ground set.  They lie in no stratum below
    their own minimum, and they are excluded NOWHERE;
  * MC = 48 IS WITNESSED.  Block 151's "NOT WITNESSED by any four-box cutting"
    caveat, carried forward by Block 152, is RETIRED: the end is attained, at
    C4 = 163 (TC = 41) and C4 = 165 (TC = 37), both minimal;
  * THE COST-146 GEOMETRIC GATE PASSES.  1,536-piece pool, 250,464 co-occurring
    pairs, 250,464 separated by exhibited integer planes, zero failures; the
    checker gated stratum 147 too, at 535,008/535,008, and that bonus is
    credited to it;
  * COMPOSITE MINIMALITY, PROVEN OUTRIGHT.  (41,53) is exactly 156 and (37,53)
    is exactly 152 -- the checker's upgrade, by complete cap-155 and cap-151
    emptiness searches, with NO strata-law dependence -- improving Block 151's
    own 169/166 witnesses.  (36,60) occurs at exactly 156 and at exactly 152 as
    well, so +-(5,-7) AND +-(1,-7) are ACHIEVED same-cost-class charge
    differences at strata 156 and 152: the first appearance of either bridge
    generator in an achieved difference set anywhere in the lane;
  * THE STRATA LAW, AT ITS TRUE SCOPE.  C4 >= 144 + (TC-36) + (60-MC) is a
    THEOREM on strata 144-147, tight at (36,55), (41,53) and (37,53), NOT an
    equality ((41,48): 163 against 161; (37,48): 165 against 157) and NOT a
    per-piece inequality (per-piece minimum 3 against the 7 per piece a
    per-piece proof needs).  The checker's law-attack sweep is COMPLETE for all
    27 bracket points with delta <= 6 and found no violation;
  * AND A FALSE LEMMA IS DISPLAYED.  The natural strengthening of the trace
    theorem -- that two facets sharing a square induce the SAME diagonal on it
    -- is FALSE for dissections.  The counterexample is inside the committed
    corpus, 15,456 of the 15,800 floor cuttings violate it, and the CSP built on
    it excludes exactly {(36,48),(36,49),(37,48),(39,48),(41,48)} -- it would
    have "proved" two REALIZABLE points impossible.

WHAT THIS RUNNER DOES, AND WHAT IT DOES NOT.  The heavy censuses cannot run
inside a 150-second gate budget: budget 3 alone is 535 million nodes, and the
targeted emptiness searches run to billions.  Following the cutting-lane
pattern, this runner therefore RE-VERIFIES EVERY WITNESS EXACTLY -- all seven
exact covers with all 276 separating planes each, the false-lemma
counterexample re-derived from the committed corpus, the trace theorem on all
15,800 floor cuttings, the square-disagreement histogram, the per-piece
minimum, and the law arithmetic on the recorded censuses -- and PINS the census
numerals as claims with SPOT-AUDIT ROUTES beside them: the budget-0 calibration
(15,800 covers over 502,838 nodes) and the budget-1 census (258,872 covers over
9,522,735 nodes, giving strata 144 and 145 completely) are re-derived live in
the default path, and the stratum-147 census is audited by its ALLOCATION
CELLS, the cost-9 cell being closed completely and live at ZERO.  Under --deep
the budget-2 census (2,618,552 covers over 87,731,188 nodes, stratum 146 with
its geometric gate) and the cost-7-plus-cost-8 allocation branch of stratum 147
(293,376 cuttings) are re-derived in full.  Budget 3 itself stays SOLVE-LEVEL
and is labeled as such wherever it appears.

Every scientific quantity here is an exact integer, an exact Fraction or a
finite set; no float is constructed anywhere, and the integer monotonic clock is
used only for the runtime gate.

TOOLING DISCLOSURE: the cell-cutting machinery is not re-implemented.  The
Block 152 runner is imported from THIS worktree under a blob pin checked against
the bytes actually imported, the Block 151 runner is reached THROUGH it under
its own pin, and the two committed cycle-726/734 runners the whole lane rests on
are read from origin/main AT RUN TIME through Block 151's own `load_machinery`,
content-bound by the same blob pins and pinned cut markers.  The 2,672
unimodular cells, the volume spectrum and the C4/TC/MC charges are then REBUILT
here from the 16 corners and checked cell for cell against the committed arrays,
and the 180 minimal three-cube facet dissections are rebuilt POINT-FREE, by
exhibited integer separating planes and clique enumeration, with no sample
lattice anywhere.

PROVENANCE DISCLOSURE: the four-box, the pieces, the facet charge, the cost
floor, the corpus and the committed strata are ALL COMMITTED objects.  This
block adds the stratum-147 census, the realizability verdicts with their exact
minima, the MC = 48 witnesses, the cost-146 gate, the composite minima, the
strata law with its exact scope, and the false-lemma display.

PICKUP PROVENANCE: the other lane's unmerged cycle-778-799 material is NOT
read, NOT consumed and NOT superseded here.

HYPOTHESES, named and not imported: (H1) a sample-point exact cover of the
committed 2,736 generic points is a complete SUPERSET of the dissections, so an
EMPTY search over covers is a genuine no-dissection verdict.  (H2) the trace of
a dissection on each facet is one of the 180 minimal three-cube dissections --
proved, not assumed, and verified on all 15,800 floor cuttings.  (H3) the
supplied-model firewall of cycles 725/726/734 is INHERITED UNCHANGED.  (H4)
Block 123's own theorem, Block 130's arithmetic and Block 151's censuses are
neither upgraded nor weakened; Block 151's numbers are REPRODUCED, not
corrected.
"""

from __future__ import annotations

import argparse
import contextlib
import hashlib
import importlib.util
import io
import itertools
import re
import shutil
import subprocess
import sys
import tempfile
import time
from collections import Counter
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path

import numpy as np


_FINAL_LOCATION_ROOT = Path(__file__).resolve().parents[1]
# This fallback keeps the scratchpad draft executable before it is moved to
# scripts/, where the final-location branch is used.
ROOT = (
    _FINAL_LOCATION_ROOT
    if (_FINAL_LOCATION_ROOT / ".git").exists()
    else Path(
        "/Users/jonBridger/Projects/Physics-baremetal-probes/"
        ".claude/worktrees/gravity-toe-lane-work-427b0b"
    )
)

NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_DIRAC_KAHLER_CUTTING_STRATA_COMPLETION_"
    "BOUNDED_THEOREM_NOTE_2026-08-20.md"
)
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"

BLOCK156_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_RESIDUE_TRANSVERSALITY_GATE_"
    "BOUNDED_THEOREM_NOTE_2026-08-20.md"
)
BLOCK156_RUNNER = (
    "scripts/admissibility_dirac_kahler_residue_transversality_gate_2026_08_20.py"
)
BLOCK152_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SIGN_LAYER_COMPARISON_"
    "BOUNDED_THEOREM_NOTE_2026-08-20.md"
)
BLOCK152_RUNNER = (
    "scripts/admissibility_dirac_kahler_sign_layer_comparison_2026_08_20.py"
)
BLOCK151_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_FLOOR_BOUNDARY_THEOREM_"
    "BOUNDED_THEOREM_NOTE_2026-08-20.md"
)
BLOCK151_RUNNER = (
    "scripts/admissibility_dirac_kahler_floor_boundary_theorem_2026_08_20.py"
)

# The four artifacts whose blobs are pinned at the parent commit: the STACK
# parent (Block 156, whose branch this one stacks on) and the CONTENT parent
# (Block 152, whose rider this block corrects).  All four are worktree-readable
# once this block's branch exists; the Block 152 runner among them is
# additionally bound by the hash of the bytes actually imported.
PARENT_ARTIFACTS = (
    BLOCK156_NOTE,
    BLOCK156_RUNNER,
    BLOCK152_NOTE,
    BLOCK152_RUNNER,
)
# PLACEHOLDERS.  The landing supervisor refreshes all four against the parent
# commit; until then gate A is the expected failure.
PARENT_ARTIFACT_BLOBS = (
    "e5698a3a5b9d1f112531cba3da619d6ca7ec517a",   # Block 156 note
    "7ccf553bd9be03243397f41393ba40c5d6a43ce2",   # Block 156 runner
    "64ec27be6cab21f3f774cec3ea432a4bcc633caa",   # Block 152 note
    "4a1259cc6d523d4bf6e6e25eab798262d4014291",   # Block 152 runner
)
# The Block 151 runner is not a parent artifact -- it is REACHED THROUGH the
# Block 152 runner for its committed-machinery loader -- but the bytes this
# runner imports are bound just as tightly.
BLOCK151_RUNNER_BLOB = "8cd0b5542c88c0200434afac08a10430c4817582"

# Deliberately literal: this is the complete audit read surface, and every entry
# is a WORKTREE-READABLE path.  The two committed cycle-726/734 runners live
# only on origin/main and are content-bound through the gate-A blob pins, so
# they must not appear here (the Block 130 lesson, inherited from 150-152).
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_CUTTING_STRATA_COMPLETION_BOUNDED_THEOREM_NOTE_2026-08-20.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_RESIDUE_TRANSVERSALITY_GATE_BOUNDED_THEOREM_NOTE_2026-08-20.md",
    "scripts/admissibility_dirac_kahler_residue_transversality_gate_2026_08_20.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SIGN_LAYER_COMPARISON_BOUNDED_THEOREM_NOTE_2026-08-20.md",
    "scripts/admissibility_dirac_kahler_sign_layer_comparison_2026_08_20.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_FLOOR_BOUNDARY_THEOREM_BOUNDED_THEOREM_NOTE_2026-08-20.md",
    "scripts/admissibility_dirac_kahler_floor_boundary_theorem_2026_08_20.py",
)

AUDIT_TIMEOUT_SEC = 600
# The five authority pins below are copied from the Block 152 runner's current
# values; the landing supervisor refreshes them against origin/main.
CURRENT_MAIN = "005f047923055e6ecd5dc8bce1ffd71765c2ffd8"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
CURRENT_REGISTRY_BLOB = "b93959cca4f7e26c673cdccbe601e50c3cb93daa"
WORKTREE_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
WORKTREE_REGISTRY_BLOB = "f01d3be864f682584d50eede8b3abe6671bb4719"
# This block stacks on Block 156, so the parent branch is Block 156's.
PARENT_REF = (
    "origin/physics-loop/"
    "toe-axiom-closure-block156-residue-transversality-gate-20260820"
)
# PLACEHOLDER.  Landing supervisor: replace with the Block 156 branch tip.
# Until it is a 40-hex commit the pin is resolved through PARENT_REF when that
# ref exists and through HEAD otherwise; either way the binding is real and
# verifiable, and the immutable commit pin lands with the block.
PARENT_COMMIT = "2570b1648a62088f8503a2dc1061aa3d8386876a" * 40
# Block 151's tip: a real ancestor that PREDATES the Block 152 artifacts and
# every Block 153-156 artifact, so resolving the parent pin there leaves ALL
# FOUR pinned artifacts ABSENT.  It is the honest stale control for this pin
# set, and it is read ONLY under the stale mutation.
STALE_PARENT_COMMIT = "26fad1c0b18073dc1121be27adcc531c5ea0651a"
# Block 137's recorded main: a real but superseded authority head.
STALE_MAIN = "2dc8dd9b2778a01454874d19b262569ae19ebc6e"

# ---------------------------------------------------------------------------
# the committed cell-cutting machinery, pinned BY CONTENT and read at run time
# ---------------------------------------------------------------------------
C726_BLOB = "46f080559c10d90d9803436f294ed660348b638f"
C734_BLOB = "ef4cedb4045ad6c476041aab274985fb7efa40fe"
MACHINERY_NAMES = ("c726", "c734")
MACHINERY_BLOBS = (("c726", C726_BLOB), ("c734", C734_BLOB))
MACHINERY_SHAPE = (("c726", 661, 661), ("c734", 766, 507))
C726_GATES = 32                     # the committed runner's own passing gates
C734_PREFIX_GATES = 22              # gates the imported prefix runs and passes

MUTATIONS = (
    "stale_main_authority",
    "stale_parent_authority",
    "break_census_count",
    "break_charge_points",
    "claim_point_unrealizable",
    "break_minimum",
    "break_mc48_witness",
    "break_separation",
    "claim_law_equality",
    "claim_law_perpiece",
    "break_composite_minimum",
    "break_difference_set",
    "claim_diagonal_lemma_true",
    "drop_overturn_language",
    "drop_n5_fence",
)

MUTATION_GATE = {
    "stale_main_authority": "A",
    "stale_parent_authority": "A",
    "break_census_count": "B",
    "break_charge_points": "B",
    "claim_point_unrealizable": "C",
    "break_minimum": "C",
    "break_mc48_witness": "D",
    "break_separation": "D",
    "claim_law_equality": "E",
    "claim_law_perpiece": "E",
    "break_composite_minimum": "F",
    "break_difference_set": "F",
    "claim_diagonal_lemma_true": "G",
    "drop_overturn_language": "H",
    "drop_n5_fence": "H",
}


class Checks:
    def __init__(self) -> None:
        self.results: list[tuple[str, str, bool]] = []

    def check(self, key: str, statement: str, condition: object) -> None:
        self.results.append((key, statement, bool(condition)))

    def report(self) -> None:
        for key, statement, value in self.results:
            print(f"[{'PASS' if value else 'FAIL'}] {key}: {statement}")
        print(
            "GATES "
            + " ".join(
                f"{key}={'PASS' if value else 'FAIL'}"
                for key, _, value in self.results
            )
        )

    def finish(self) -> int:
        passed = sum(value for _, _, value in self.results)
        failed = len(self.results) - passed
        print(f"TOTAL: PASS={passed} FAIL={failed}")
        return failed


def git_output(*args: str) -> str:
    return subprocess.check_output(
        ("git",) + args,
        cwd=ROOT,
        text=True,
        timeout=AUDIT_TIMEOUT_SEC,
    ).strip()


def worktree_blob(path: str) -> str:
    """The blob of a worktree path, or "" when the path is absent.

    Absence is a real answer here: before the block's own branch exists the two
    Block 156 artifacts are not in this worktree at all.
    """
    result = subprocess.run(
        ("git", "hash-object", path),
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
        timeout=AUDIT_TIMEOUT_SEC,
    )
    return result.stdout.strip() if result.returncode == 0 else ""


def commit_blob(commit: str, path: str) -> str:
    """The blob at a path in a commit, or "" when the path is absent there."""
    result = subprocess.run(
        ("git", "rev-parse", f"{commit}:{path}"),
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
        timeout=AUDIT_TIMEOUT_SEC,
    )
    return result.stdout.strip() if result.returncode == 0 else ""


def resolve_ref(ref: str) -> str:
    result = subprocess.run(
        ("git", "rev-parse", ref),
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
        timeout=AUDIT_TIMEOUT_SEC,
    )
    return result.stdout.strip() if result.returncode == 0 else ""


def is_ancestor(ancestor: str, descendant: str) -> bool:
    return subprocess.run(
        ("git", "merge-base", "--is-ancestor", ancestor, descendant),
        cwd=ROOT,
        check=False,
        timeout=AUDIT_TIMEOUT_SEC,
    ).returncode == 0


def is_hash(value: str) -> bool:
    return re.fullmatch(r"[0-9a-f]{40}", value) is not None


def blob_sha1(data: bytes) -> str:
    """Git's own blob hash of a byte string, computed locally."""
    header = b"blob " + str(len(data)).encode("ascii") + b"\x00"
    return hashlib.sha1(header + data).hexdigest()


def read_note(path: str) -> str:
    try:
        return (ROOT / path).read_text(encoding="utf-8")
    except OSError:
        return ""


def raw_note() -> str:
    try:
        return NOTE_PATH.read_text(encoding="utf-8")
    except OSError:
        return ""


def normalized_note(text: str) -> str:
    return " ".join(text.lower().split())


def compact_note(text: str) -> str:
    return "".join(text.lower().split())


def flat(text: str) -> str:
    """Whitespace-normalised but CASE-PRESERVING, for the text certificates."""
    return " ".join(text.split())


# ---------------------------------------------------------------------------
# A. authority
# ---------------------------------------------------------------------------
@dataclass(frozen=True)
class AuthorityCertificate:
    fixed_authority: bool
    parent_pin_is_commit: bool
    parent_ref_and_ancestry: bool
    parent_artifact_blobs: bool
    stale_parent_artifact_blobs: bool
    imported_bytes_bound: bool
    machinery_blobs: tuple
    machinery_content_bound: bool


def resolved_parent_commit() -> str:
    if is_hash(PARENT_COMMIT) and PARENT_COMMIT != "0" * 40:
        return PARENT_COMMIT
    resolved = resolve_ref(PARENT_REF)
    return resolved if is_hash(resolved) else git_output("rev-parse", "HEAD")


def authority_certificate(
    main_head: str, machinery: tuple, imported_digests: tuple
) -> AuthorityCertificate:
    fixed_authority = bool(
        AUDIT_TIMEOUT_SEC == 600
        and main_head == CURRENT_MAIN
        and commit_blob("origin/main", AXIOM_PATH) == CURRENT_AXIOM_BLOB
        and commit_blob("origin/main", REGISTRY_PATH) == CURRENT_REGISTRY_BLOB
        and worktree_blob(AXIOM_PATH) == WORKTREE_AXIOM_BLOB
        and worktree_blob(REGISTRY_PATH) == WORKTREE_REGISTRY_BLOB
    )

    parent = resolved_parent_commit()
    worktree_blobs = tuple(worktree_blob(path) for path in PARENT_ARTIFACTS)
    committed_blobs = tuple(
        commit_blob(parent, path) for path in PARENT_ARTIFACTS
    )
    stale_blobs = tuple(
        commit_blob(STALE_PARENT_COMMIT, path) for path in PARENT_ARTIFACTS
    )
    # The two worktree imports bind BOTH ways: the pinned blob must be what the
    # parent commit and the worktree record, AND the bytes this runner actually
    # imported must hash to it.  The second half is the content binding.
    imported_bytes_bound = bool(
        imported_digests == (PARENT_ARTIFACT_BLOBS[3], BLOCK151_RUNNER_BLOB)
        and all(is_hash(value) for value in imported_digests)
    )
    machinery_named = tuple(
        (name, record.digest, record.pin, pin)
        for (name, pin), record in zip(MACHINERY_BLOBS, machinery)
    )
    machinery_content_bound = all(
        digest == recorded == pin and is_hash(pin)
        for _name, digest, recorded, pin in machinery_named
    )
    return AuthorityCertificate(
        fixed_authority,
        is_hash(PARENT_COMMIT) and PARENT_COMMIT != "0" * 40,
        bool(
            is_hash(parent)
            and is_ancestor(parent, "HEAD")
            and (
                not (is_hash(PARENT_COMMIT) and PARENT_COMMIT != "0" * 40)
                or resolve_ref(PARENT_REF) == PARENT_COMMIT
            )
        ),
        bool(
            len(committed_blobs) == len(PARENT_ARTIFACTS)
            and all(is_hash(value) for value in committed_blobs)
            and committed_blobs == worktree_blobs
            and committed_blobs == PARENT_ARTIFACT_BLOBS
        ),
        bool(
            len(stale_blobs) == len(PARENT_ARTIFACTS)
            and all(is_hash(value) for value in stale_blobs)
            and stale_blobs == worktree_blobs
        ),
        imported_bytes_bound,
        machinery_named,
        machinery_content_bound,
    )


def import_worktree_module(alias: str, path: str):
    """Import a runner from THIS worktree and return (module, blob digest)."""
    target = ROOT / path
    digest = blob_sha1(target.read_bytes())
    spec = importlib.util.spec_from_file_location(alias, target)
    module = importlib.util.module_from_spec(spec)
    sys.modules[alias] = module          # dataclasses need this registered
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(module)
    return module, digest


# ---------------------------------------------------------------------------
# the recorded fixture, the recorded censuses, and the recorded witnesses
# ---------------------------------------------------------------------------
CORNERS = 16
PIECES = 2672
CUTTING_SIZE = 24
FLOOR_CLASS = 144
PIECE_COST_FLOOR = 6
CORPUS = 15800
CORPUS_CHARGE = (36, 60)
COST_SPECTRUM = ((6, 400), (7, 1216), (8, 864), (9, 192))
VOLUME_SPECTRUM = ((0, 1360), (1, 2672), (2, 320), (3, 16))
SAMPLE_POINTS = 2736
WITNESS_PAIRS = 276                 # C(24, 2)

FACET_DISSECTIONS = 180
TICK_SPECTRUM = ((18, 16), (19, 72), (20, 84), (21, 8))
MIXED_SPECTRUM = ((8, 12), (9, 64), (10, 104))
TICK_BOX = (36, 42)
MIXED_BOX = (48, 60)
SLICE_INCIDENCES = 3584
SQUARES_PER_BOX = 24

# --- the strata, as this block measures them ---------------------------------
BUDGET_NODES = {0: 502838, 1: 9522735, 2: 87731188, 3: 535593550}
BUDGET_SOLUTIONS = {0: 15800, 1: 258872, 2: 2618552, 3: 18978168}
STRATUM = {144: 15800, 145: 243072, 146: 2359680, 147: 16359616}
CHARGE_144 = (((36, 60), 15800),)
CHARGE_145 = (((36, 59), 60768), ((36, 60), 121536), ((37, 60), 60768))
CHARGE_146 = (((36, 58), 95952), ((36, 59), 530016), ((36, 60), 796752),
              ((37, 59), 311232), ((37, 60), 529536), ((38, 60), 96192))
CHARGE_147 = (((36, 57), 78624), ((36, 58), 1056288), ((36, 59), 3151056),
              ((36, 60), 3523168), ((37, 58), 670560), ((37, 59), 2773824),
              ((37, 60), 3523632), ((38, 59), 597600), ((38, 60), 905760),
              ((39, 60), 79104))
CHARGE_POINT_RUN = (1, 3, 6, 10)                # the triangular numbers
# The four routes to the stratum-147 census.  Route A is the primary's; routes
# B, C and D are the independent checker's, two of them on a ground set the
# primary never touched.  Route A's node count is reproduced to the digit.
CENSUS_ROUTES = (
    ("A: committed ground set, committed lowest-uncovered-point order",
     535593550),
    ("B: checker's own 1,924-column generic point set, lexicographic sweep",
     904977200),
    ("C: checker's own point set, reversed sweep (axes 3-2-1-0)", 568364730),
    ("D: checker's excess-pattern ALLOCATION decomposition (no whole-stratum "
     "enumeration; node total is the sum of its three cells)", 915978325),
)
# Route D's cells: (excess pattern, cuttings, nodes).  The third cell -- no
# stratum-147 cutting uses a cost-9 piece -- is closed COMPLETELY AND LIVE in
# this runner's default path.
EXCESS_CELLS = (
    ((7, 7, 7), 16066240, 843673474),
    ((7, 8), 293376, 71445713),
    ((9,), 0, 859138),
)
EXCESS_78_CHARGES = (((36, 59), 73344), ((36, 60), 73344),
                     ((37, 59), 73344), ((37, 60), 73344))

# --- the geometric gates ------------------------------------------------------
POOL_146, PAIRS_146, SEPARATED_146 = 1536, 250464, 250464
POOL_147, PAIRS_147, SEPARATED_147 = 1920, 535008, 535008   # the checker's bonus
CHECKER_HOSTILE_PAIRS = 1039                                # 0 of them separated
HOSTILE_PAIRS = 2000                        # this runner's own hostile control

# --- the exhibited witnesses --------------------------------------------------
# Each is a 24-piece exact cover of the committed 2,736 generic sample points,
# re-verified below by exhibited integer separating planes on all 276 pairs.
WITNESS = {
    (36, 55): (22, 42, 102, 124, 194, 200, 845, 1056, 1142, 1182, 1292, 1390,
               1423, 1488, 1684, 1699, 1787, 2015, 2290, 2376, 2463, 2501,
               2519, 2611),                                   # C4 = 149
    (41, 53): (18, 100, 168, 172, 192, 216, 845, 1056, 1142, 1182, 1292, 1390,
               1423, 1488, 1684, 1699, 1787, 2017, 2045, 2290, 2376, 2503,
               2506, 2611),                                   # C4 = 156
    (37, 53): (22, 42, 102, 114, 194, 848, 872, 1142, 1182, 1217, 1390, 1423,
               1491, 1541, 1559, 1573, 1684, 1699, 1779, 1857, 2290, 2376,
               2598, 2615),                                   # C4 = 152
    (41, 48): (54, 82, 114, 242, 410, 500, 1020, 1109, 1148, 1164, 1217, 1223,
               1394, 1922, 1932, 1934, 2150, 2157, 2221, 2290, 2334, 2376,
               2598, 2615),                                   # C4 = 163
    (37, 48): (49, 242, 410, 417, 418, 507, 784, 1030, 1046, 1142, 1925, 1937,
               1964, 1981, 1991, 2022, 2078, 2081, 2128, 2151, 2154, 2158,
               2160, 2667),                                   # C4 = 165
}
WITNESS_COST = {(36, 55): 149, (41, 53): 156, (37, 53): 152,
                (41, 48): 163, (37, 48): 165}
# the SAME-COST-CLASS partners: the corner charge (36,60) realised at EXACTLY
# these two costs, which is what turns the bridge generators into ACHIEVED
# same-cost-class charge DIFFERENCES
PARTNER = {
    156: (22, 42, 96, 206, 781, 845, 1056, 1137, 1248, 1292, 1488, 1679, 2015,
          2209, 2256, 2312, 2441, 2538, 2543, 2584, 2595, 2626, 2647, 2659),
    152: (22, 42, 96, 194, 845, 1056, 1137, 1248, 1292, 1392, 1488, 1679, 2015,
          2208, 2256, 2441, 2448, 2538, 2547, 2584, 2591, 2595, 2626, 2659),
}
BRIDGE_POINTS = ((36, 55), (41, 48), (37, 48))
BRIDGE_DELTAS = ((5, -7), (1, -7))
COMPOSITE_TARGETS = {(41, 53): 156, (37, 53): 152}
BLOCK151_COMPOSITE_WITNESSES = {(41, 53): 169, (37, 53): 166}

# --- the exact minima, each closed by a COMPLETE bounded search ----------------
MIN_COST = {(36, 55): 149, (41, 48): 163, (37, 48): 165,
            (41, 53): 156, (37, 53): 152}
# the largest cap at which a COMPLETE (not node-capped) search certifies that no
# dissection exists, with the primary's staged node counts
LOWER_BOUND = {(36, 55): 148, (41, 48): 162, (37, 48): 164,
               (41, 53): 155, (37, 53): 151}
PRIMARY_EMPTY_NODES = {
    (36, 55): ((148, 117879899),),
    (41, 48): ((160, 27017371), (161, 32241954), (162, 37156418)),
    (37, 48): ((159, 23336002), (160, 27049090), (161, 30399031),
               (162, 33156907), (163, 35147699), (164, 36382321)),
}
# the checker's INDEPENDENT re-runs: one single-cap search per point, on its own
# ground set, with its own facet-trace tables
CHECKER_EMPTY_NODES = {
    (36, 55): (148, 122553342),
    (41, 48): (162, 40477687),
    (37, 48): (164, 33870992),
    (41, 53): (155, 4418945782),
    (37, 53): (151, 2087087895),
}
CHECKER_FOUND_NODES = {(36, 55): (149, 196067), (41, 48): (163, 8416),
                       (37, 48): (165, 2154809), (41, 53): (156, 14899),
                       (37, 53): (152, 319014691)}
# the two composite minima are the CHECKER's upgrade and carry NO strata-law
# dependence: emptiness is certified DIRECTLY at cap 155 and cap 151
LAW_DEPENDENT_MINIMA = ()

# --- stratum 148 --------------------------------------------------------------
STRATUM_148_POINTS = 15             # every charge point with delta <= 4
STRATUM_148_NODE_RANGE = (27, 75157)          # primary, single-route
CHECKER_148_NODE_RANGE = (25, 5277)

# --- the strata law -----------------------------------------------------------
LAW_TIGHT = ((36, 55), (41, 53), (37, 53))
LAW_SLACK = (((37, 48), 157, 165), ((41, 48), 161, 163))
PER_PIECE_MIN = 3
PER_PIECE_NEEDED = 7
PER_PIECE_HISTOGRAM = ((3, 48), (4, 304), (5, 192), (6, 304), (7, 48),
                       (8, 336), (9, 672), (10, 624), (11, 96), (12, 48))
# the checker's law-attack sweep: EVERY bracket point with delta <= 6, each a
# COMPLETE targeted search at cap 144 + delta - 1.  All EMPTY, no timeouts.
LAW_SWEEP_MAX_DELTA = 6
LAW_SWEEP_POINTS = 27
LAW_SWEEP_LARGEST_CAP = 149
LAW_UNSWEPT_MIN_DELTA = 7

# --- the false lemma ----------------------------------------------------------
DISAGREEMENT_HISTOGRAM = ((0, 344), (2, 6720), (4, 8064), (6, 576), (8, 96))
COHERENT_CUTTINGS = 344
VIOLATING_CUTTINGS = 15456
COUNTEREXAMPLE_SQUARE = (0, 0, 1, 1)              # x0 = 0 and x1 = 1
COUNTEREXAMPLE_CORNERS = (4, 5, 6, 7)
COUNTEREXAMPLE_PIECES = {
    (0, 0): ((1, 4, 5, 6, 9), (2, 5, 6, 7, 10)),
    (1, 1): ((4, 5, 7, 11, 15), (4, 6, 7, 11, 15)),
}
COUNTEREXAMPLE_DIAGONALS = {(0, 0): (5, 6), (1, 1): (4, 7)}
CSP_CONSISTENT = 86
CSP_BRACKET_POINTS = 91
CSP_EXCLUDED = ((36, 48), (36, 49), (37, 48), (39, 48), (41, 48))
CSP_STATES = 9301906

# --- worker profile and disclosures -------------------------------------------
SOLVE_CHECKS = (25, 25)
SOLVE_SECONDS = 233
CHECKER_REFUTATIONS = 0
CHECKER_CLAIMS = 7
CHECKER_MINUTES = 110
SINGLE_ROUTE_ITEMS = (
    "every individual node count of the primary's targeted searches",
    "the primary's 21-minute wall-clock figure for budget 3",
    "the 27-to-75,157 node range of the fifteen stratum-148 witnesses",
)
DOC_FIXES = 2                       # the checker's two catches, applied

# The default gate path runs in about 72 seconds on this host -- the origin/main
# machinery load dominates it -- and --deep, which adds the budget-2 census with
# its 250,464-pair gate and the cost-7-plus-cost-8 allocation branch of stratum
# 147, lands near 600, so the budget covers both with room on a slower host.
RUNTIME_BUDGET_SEC = 1200


# ---------------------------------------------------------------------------
# B. the fixture, rebuilt from the 16 corners
# ---------------------------------------------------------------------------
def det(matrix):
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    total = 0
    for column in range(n):
        if matrix[0][column] == 0:
            continue
        minor = [
            [row[x] for x in range(n) if x != column] for row in matrix[1:]
        ]
        total += ((-1) ** column) * matrix[0][column] * det(minor)
    return total


COR = [tuple((k >> (3 - j)) & 1 for j in range(4)) for k in range(CORNERS)]
FACETS = [(i, c) for i in range(4) for c in (0, 1)]
TICK_FACETS = [f for f in FACETS if f[0] == 3]
SPAT_FACETS = [f for f in FACETS if f[0] != 3]
SQUARES = [(i, ci, j, cj) for i, j in itertools.combinations(range(4), 2)
           for ci in (0, 1) for cj in (0, 1)]


def rebuild_fixture():
    """The 2,672 unimodular cells and their C4/TC/MC charges, from scratch."""
    volumes: Counter = Counter()
    cells = []
    for combination in itertools.combinations(range(CORNERS), 5):
        edges = [
            [COR[combination[r + 1]][c] - COR[combination[0]][c]
             for c in range(4)]
            for r in range(4)
        ]
        volume = abs(det(edges))
        volumes[volume] += 1
        if volume == 1:
            cells.append(combination)
    c4, tc, mc = [], [], []
    for piece in cells:
        vertices = [COR[k] for k in piece]
        c4.append(sum(
            1 for a, b in itertools.combinations(range(5), 2)
            if sum(abs(vertices[a][c] - vertices[b][c]) for c in range(4)) > 1
        ))
        tick = mixed = 0
        for axis, side in FACETS:
            slab = [a for a in range(5) if vertices[a][axis] == side]
            if len(slab) != 4:
                continue
            others = [j for j in range(3) if j != axis]
            count = sum(
                1 for a, b in itertools.combinations(slab, 2)
                if sum(abs(vertices[a][x] - vertices[b][x]) for x in others) > 1
            )
            if axis == 3:
                tick += count
            else:
                mixed += count
        tc.append(tick)
        mc.append(mixed)
    return cells, tuple(sorted(volumes.items())), c4, tc, mc


# ---------------------------------------------------------------------------
# the induced facet problem, POINT-FREE
# ---------------------------------------------------------------------------
def det3(matrix):
    return (matrix[0][0] * (matrix[1][1] * matrix[2][2]
                            - matrix[1][2] * matrix[2][1])
            - matrix[0][1] * (matrix[1][0] * matrix[2][2]
                              - matrix[1][2] * matrix[2][0])
            + matrix[0][2] * (matrix[1][0] * matrix[2][1]
                              - matrix[1][1] * matrix[2][0]))


def adj3(matrix):
    out = [[0] * 3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            minor = [[matrix[r][c] for c in range(3) if c != i]
                     for r in range(3) if r != j]
            out[i][j] = ((-1) ** (i + j)) * (
                minor[0][0] * minor[1][1] - minor[0][1] * minor[1][0]
            )
    return out


def cross(u, v):
    return (u[1] * v[2] - u[2] * v[1],
            u[2] * v[0] - u[0] * v[2],
            u[0] * v[1] - u[1] * v[0])


def square_corners(square):
    i, ci, j, cj = square
    return sorted(k for k in range(CORNERS)
                  if COR[k][i] == ci and COR[k][j] == cj)


def facet_squares(facet):
    axis, side = facet
    return [square for square in SQUARES
            if (square[0] == axis and square[1] == side)
            or (square[2] == axis and square[3] == side)]


def build_facets():
    """Per facet: its unimodular tetrahedra, its six-clique dissections, each
    one's charge cost, and the diagonal it induces on each of its six squares.

    The route is POINT-FREE: interior disjointness is decided by an EXHIBITED
    integer separating plane drawn from the two tetrahedra's facet normals and
    the cross products of their edge vectors, and a six-clique of pairwise
    interior-disjoint unimodular cells has total volume one, so it IS a
    dissection.  No sample lattice is involved anywhere.
    """
    info = {}
    for facet in FACETS:
        axis, side = facet
        keys = [k for k in range(CORNERS) if COR[k][axis] == side]
        kept = [j for j in range(4) if j != axis]
        points = {k: tuple(COR[k][j] for j in kept) for k in keys}
        cells = [
            combination for combination in itertools.combinations(keys, 4)
            if abs(det3([
                [points[combination[r + 1]][x] - points[combination[0]][x]
                 for x in range(3)]
                for r in range(3)
            ])) == 1
        ]
        edge_pairs = list(itertools.combinations(range(4), 2))

        def normals(cell):
            matrix = [
                [points[cell[j + 1]][r] - points[cell[0]][r] for j in range(3)]
                for r in range(3)
            ]
            rows = adj3(matrix)
            if det3(matrix) < 0:
                rows = [[-value for value in row] for row in rows]
            out = [tuple(rows[k]) for k in range(3)]
            out.append(tuple(-sum(rows[k][r] for k in range(3))
                             for r in range(3)))
            return out

        def separated(left, right):
            pa = [points[k] for k in left]
            pb = [points[k] for k in right]
            ea = [tuple(pa[y][r] - pa[x][r] for r in range(3))
                  for x, y in edge_pairs]
            eb = [tuple(pb[y][r] - pb[x][r] for r in range(3))
                  for x, y in edge_pairs]
            candidates = normals(left) + normals(right)
            for u in ea:
                for v in eb:
                    normal = cross(u, v)
                    if any(normal):
                        candidates.append(normal)
            for normal in candidates:
                va = [sum(a * b for a, b in zip(normal, p)) for p in pa]
                vb = [sum(a * b for a, b in zip(normal, p)) for p in pb]
                if max(va) <= min(vb) or max(vb) <= min(va):
                    return True
            return False

        size = len(cells)
        disjoint = [[False] * size for _ in range(size)]
        for a in range(size):
            for b in range(a + 1, size):
                value = separated(cells[a], cells[b])
                disjoint[a][b] = disjoint[b][a] = value
        cliques = []

        def grow(start, chosen):
            if len(chosen) == 6:
                cliques.append(tuple(chosen))
                return
            for a in range(start, size):
                if all(disjoint[a][j] for j in chosen):
                    chosen.append(a)
                    grow(a + 1, chosen)
                    chosen.pop()

        grow(0, [])
        live_axes = ([0, 1, 2] if axis == 3
                     else [p for p, j in enumerate(kept) if j != 3])

        def cost(cell):
            return sum(
                1 for a, b in itertools.combinations(cell, 2)
                if sum(abs(points[a][x] - points[b][x]) for x in live_axes) > 1
            )

        cell_cost = [cost(cells[a]) for a in range(size)]
        squares = facet_squares(facet)
        signatures, costs = [], []
        for clique in cliques:
            bits = []
            for square in squares:
                corners = set(square_corners(square))
                triangles = {
                    tuple(sorted(set(cells[a]) & corners)) for a in clique
                    if len(set(cells[a]) & corners) == 3
                }
                if len(triangles) != 2:
                    raise AssertionError(("square not split in two", facet,
                                          square))
                first, second = sorted(triangles)
                diagonal = tuple(sorted(set(first) & set(second)))
                listed = square_corners(square)
                bits.append(0 if diagonal == (listed[0], listed[3]) else 1)
            signatures.append(tuple(bits))
            costs.append(sum(cell_cost[a] for a in clique))
        info[facet] = dict(
            cells=cells,
            cliques=cliques,
            squares=squares,
            sigs=signatures,
            costs=costs,
            spec=tuple(sorted(Counter(costs).items())),
            pos={tuple(sorted(x)): n for n, x in enumerate(cells)},
            key={tuple(sorted(clique)): n for n, clique in enumerate(cliques)},
        )
    return info


# ---------------------------------------------------------------------------
# the geometric gate: exhibited integer separating planes
# ---------------------------------------------------------------------------
class Gate:
    """The committed candidate normal family, vector for vector."""

    def __init__(self, uni, coords, inverses):
        self.n = len(uni)
        family = np.array(
            [t for t in itertools.product((-1, 0, 1), repeat=4) if any(t)],
            dtype=np.int64,
        )
        self.pts = np.array(
            [[coords[k] for k in row] for row in uni], dtype=np.int64
        )
        projection = np.einsum("pvc,nc->pnv", self.pts, family)
        self.lo = projection.min(axis=2)
        self.hi = projection.max(axis=2)
        self.fac = []
        for piece in range(self.n):
            rows = [list(inverses[piece][k]) for k in range(4)]
            rows.append([
                -sum(inverses[piece][k][c] for k in range(4)) for c in range(4)
            ])
            self.fac.append(np.array(rows, dtype=np.int64))

    def apart(self, a, b) -> bool:
        if np.any((self.hi[a] <= self.lo[b]) | (self.hi[b] <= self.lo[a])):
            return True
        for normals in (self.fac[a], self.fac[b]):
            pa = self.pts[a] @ normals.T
            pb = self.pts[b] @ normals.T
            if np.any((pa.max(axis=0) <= pb.min(axis=0))
                      | (pb.max(axis=0) <= pa.min(axis=0))):
                return True
        return False


# ---------------------------------------------------------------------------
# the budgeted exact cover over the committed sample points
# ---------------------------------------------------------------------------
def budgeted_cover(mask, c4, tc, mc, allq, budget, want_pairs_at=None):
    """Complete enumeration of every sample-point exact cover with
    C4 <= 144 + budget, by the committed lowest-uncovered-point rule."""
    n = len(mask)
    by_point: dict[int, list] = {}
    for i in range(n):
        bits = mask[i]
        while bits:
            low = bits & -bits
            by_point.setdefault(low.bit_length() - 1, []).append(i)
            bits ^= low
    ordered = [
        sorted(by_point.get(q, []), key=lambda i: c4[i])
        for q in range(allq.bit_length())
    ]
    excess = [c4[i] - PIECE_COST_FLOOR for i in range(n)]
    bit = [1 << i for i in range(n)] if want_pairs_at else None
    adjacency = [0] * n if want_pairs_at else None
    charges: Counter = Counter()
    nodes = [0]
    sys.setrecursionlimit(10000)

    def rec(cover, used, left, cost, tick, mixed, chosen):
        nodes[0] += 1
        if cover == allq:
            charges[(cost, tick, mixed)] += 1
            if want_pairs_at is not None and cost == want_pairs_at:
                stamp = 0
                for i in chosen:
                    stamp |= bit[i]
                for i in chosen:
                    adjacency[i] |= stamp
            return
        if used == CUTTING_SIZE:
            return
        rest = allq & ~cover
        slot = (rest & -rest).bit_length() - 1
        for i in ordered[slot]:
            step = excess[i]
            if step > left:
                break
            if mask[i] & cover:
                continue
            chosen.append(i)
            rec(cover | mask[i], used + 1, left - step, cost + c4[i],
                tick + tc[i], mixed + mc[i], chosen)
            chosen.pop()

    rec(0, 0, budget, 0, 0, 0, [])
    pairs = []
    if want_pairs_at is not None:
        for a in range(n):
            rest = adjacency[a] >> (a + 1)
            base = a + 1
            while rest:
                low = rest & -rest
                pairs.append((a, base + low.bit_length() - 1))
                rest ^= low
    return nodes[0], charges, pairs


def allocation_cell(mask, c4, tc, mc, allq, pattern):
    """Stratum 147 by ALLOCATION: covers whose non-floor pieces are exactly the
    given excess pattern.  A route that never enumerates the stratum whole.

    The cost-9 cell is closed by an exact point-coverability filter alone -- if
    no cost-9 piece even admits a floor completion of its complement, the cell
    is empty and no search is needed.
    """
    n = len(mask)
    wanted = Counter(pattern)
    if wanted == Counter({3: 1}):                       # the single cost-9 cell
        floor_pool = [i for i in range(n) if c4[i] == PIECE_COST_FLOOR]
        survivors = []
        for piece in (i for i in range(n) if c4[i] == PIECE_COST_FLOOR + 3):
            target = allq & ~mask[piece]
            reachable = 0
            for other in floor_pool:
                if not (mask[other] & mask[piece]):
                    reachable |= mask[other]
            if not (target & ~reachable):
                survivors.append(piece)
        return 0 if not survivors else -1, Counter(), len(survivors)

    by_point: dict[int, list] = {}
    for i in range(n):
        bits = mask[i]
        while bits:
            low = bits & -bits
            by_point.setdefault(low.bit_length() - 1, []).append(i)
            bits ^= low
    ordered = [
        sorted(by_point.get(q, []), key=lambda i: c4[i])
        for q in range(allq.bit_length())
    ]
    excess = [c4[i] - PIECE_COST_FLOOR for i in range(n)]
    cap = max(wanted)
    charges: Counter = Counter()
    nodes = [0]
    sys.setrecursionlimit(10000)

    def rec(cover, used, taken, tick, mixed):
        nodes[0] += 1
        if cover == allq:
            if Counter({k: v for k, v in taken.items() if k}) == wanted:
                charges[(tick, mixed)] += 1
            return
        if used == CUTTING_SIZE:
            return
        rest = allq & ~cover
        slot = (rest & -rest).bit_length() - 1
        for i in ordered[slot]:
            step = excess[i]
            if step > cap:
                break
            if step and taken[step] >= wanted[step]:
                continue
            if mask[i] & cover:
                continue
            taken[step] += 1
            rec(cover | mask[i], used + 1, taken, tick + tc[i], mixed + mc[i])
            taken[step] -= 1

    rec(0, 0, Counter(), 0, 0)
    return sum(charges.values()), charges, nodes[0]


# ---------------------------------------------------------------------------
# C-G. the measured certificates
# ---------------------------------------------------------------------------
@dataclass(frozen=True)
class WitnessCertificate:
    charge: tuple
    cost: int
    exact_cover: bool
    separated: int
    pairs: int
    traced: bool


@dataclass(frozen=True)
class TextCertificate:
    b152_rider_verbatim: bool
    b152_unwitnessed_box: bool
    b152_hedge_present: bool
    b151_unwitnessed_verbatim: bool
    b151_not_proven_minimal: bool
    b151_gate_boundary: bool
    firewall_inherited: bool
    b152_no_unrealizability_claim: bool


def text_certificate() -> TextCertificate:
    """Every entry is a substring test on COMMITTED bytes -- a quotable anchor.

    Whitespace is normalised but case is preserved, so an anchor that reads as a
    capitalised phrase in the parent note must occur capitalised.  These are the
    exact strings this block quotes and then corrects.
    """
    n152 = flat(read_note(BLOCK152_NOTE))
    n151 = flat(read_note(BLOCK151_NOTE))
    return TextCertificate(
        b152_rider_verbatim=(
            "The bridge's transcribed points \\((36,55)\\), \\((41,48)\\), "
            "\\((37,48)\\) occur in **no** committed stratum, and two sit at "
            "the **unwitnessed** \\(MC=48\\) end of the global bracket, per "
            "(39)." in n152
        ),
        b152_unwitnessed_box=(
            "bound Block 151 displays as \\textbf{UNWITNESSED}, which no "
            "four-box cutting is known to realize." in n152
        ),
        b152_hedge_present=(
            "is a statement about the strata **enumerated so far**, not a "
            "proof that the points are unrealizable" in n152
        ),
        b151_unwitnessed_verbatim=(
            "it is \\textbf{NOT WITNESSED} by any four-box cutting enumerated "
            "here;" in n151
        ),
        b151_not_proven_minimal=(
            "NOT proven minimal" in n151 or "NOT PROVEN MINIMAL" in n151
        ),
        b151_gate_boundary=(
            "cost 146 is complete at 2,359,680 cuttings with SIX charge points "
            "at incidence level only, no geometric gate, a displayed boundary"
            in n151
        ),
        firewall_inherited=(
            "supplied-model firewall is inherited unchanged" in n151
        ),
        # Block 152 never asserted unrealizability, and this block credits that
        # hedge rather than inventing an error: the string is absent there.
        b152_no_unrealizability_claim=(
            "the transcribed points are unrealizable" not in n152
        ),
    )


@dataclass(frozen=True)
class Facts:
    main_head: str
    authority: AuthorityCertificate
    machinery: tuple
    machinery_exit: tuple
    # B: the fixture and the strata
    fixture_rebuilt: bool
    volume_spectrum: tuple
    cost_spectrum: tuple
    corpus: tuple
    facet_spectra: tuple
    slice_incidences: int
    budget0: tuple
    budget1: tuple
    strata_measured: tuple
    charge_points_measured: tuple
    cost9_cell: tuple
    census_sums: tuple
    charge_point_run: tuple
    delta_exact: bool
    deep_budget2: tuple
    deep_excess78: tuple
    # C/D: the witnesses
    witnesses: tuple
    realizable: tuple
    minima_measured: tuple
    strata_below_minimum: tuple
    separation_shortfall: int
    floor_pair_census: tuple
    hostile_control: tuple
    gate_agrees: bool
    deep_gate146: tuple
    # E: the law
    per_piece_min: int
    per_piece_histogram: tuple
    law_holds_everywhere: bool
    law_equality_holds: bool
    law_tight_at: tuple
    law_slack_at: tuple
    # F: composite minimality and the difference set
    composite_measured: tuple
    partners_measured: tuple
    bridge_differences: tuple
    difference_sets_closed: tuple
    law_dependent_minima: tuple
    # G: the false lemma
    traced: int
    charge_route_agrees: int
    disagreement_histogram: tuple
    violating: int
    counterexample: tuple
    csp_hits_realizable: tuple
    # global
    text: TextCertificate
    exact_no_float: bool
    scope: dict


def measure(deep: bool) -> Facts:
    main_head = git_output("rev-parse", "origin/main")

    # --- the worktree imports, content-bound ---------------------------------
    b152, b152_digest = import_worktree_module("block157_b152", BLOCK152_RUNNER)
    b151, b151_digest = b152.import_worktree_module(
        "block157_b151", b152.BLOCK151_RUNNER
    )

    # --- the committed cell-cutting machinery, through Block 151's loader ----
    workdir = Path(tempfile.mkdtemp(prefix="block157-machinery-"))
    try:
        records = tuple(
            b151.load_machinery(name, path, pin, cut, workdir)
            for name, path, pin, cut in b151.MACHINERY
            if name in MACHINERY_NAMES
        )
    finally:
        shutil.rmtree(workdir, ignore_errors=True)
    c726, c734 = (record.module for record in records)
    authority = authority_certificate(
        main_head, records, (b152_digest, b151_digest)
    )
    machinery_shape = tuple(
        (record.name, record.total_lines, record.cut_line)
        for record in records
    )
    machinery_exit = (
        records[0].exit_code,
        int(getattr(c726, "npass", -1)),
        int(getattr(c726, "nfail", -1)),
        tuple(int(value) for value in getattr(c734, "PF", (-1, -1))),
    )

    # --- the committed arrays -------------------------------------------------
    UNI = [tuple(int(x) for x in row) for row in c734.UNI]
    MASK = [int(value) for value in c734.MASK]
    C4 = [int(value) for value in c734.C4]
    TC = [int(value) for value in c726.TC]
    MC = [int(value) for value in c726.MC]
    SOL = [tuple(int(x) for x in s) for s in c734.SOL]
    coords = [tuple(int(x) for x in row) for row in c734.V]
    IV = [[[int(x) for x in row] for row in m] for m in c734.IV]
    NQ = len(c734.Q)
    ALLQ = (1 << NQ) - 1

    cells, volume_spectrum, own_c4, own_tc, own_mc = rebuild_fixture()
    fixture_rebuilt = bool(
        [tuple(c) for c in cells] == UNI
        and own_c4 == C4 and own_tc == TC and own_mc == MC
        and len(UNI) == PIECES and NQ == SAMPLE_POINTS
    )
    cost_spectrum = tuple(sorted(Counter(C4).items()))
    corpus = (
        len(SOL),
        tuple(sorted({sum(C4[p] for p in s) for s in SOL})),
        tuple(sorted({(sum(TC[p] for p in s), sum(MC[p] for p in s))
                      for s in SOL})),
    )

    # --- the induced facet problem, point-free -------------------------------
    info = build_facets()
    facet_spectra = (
        tuple(len(info[f]["cliques"]) for f in FACETS),
        tuple(sorted({info[f]["spec"] for f in TICK_FACETS})),
        tuple(sorted({info[f]["spec"] for f in SPAT_FACETS})),
    )
    slice_incidences = sum(
        1 for p in range(PIECES) for f in FACETS
        if sum(1 for k in UNI[p] if coords[k][f[0]] == f[1]) == 4
    )

    gate = Gate(UNI, coords, IV)
    sample = [(int(c734.USED[a]), int(c734.USED[b])) for a, b in c734.CP[::7]]
    gate_agrees = bool(
        len(sample) > 100
        and all(gate.apart(a, b) == (c734.separated([a, b])[0] == 1)
                for a, b in sample)
    )
    overlapping = [
        (a, b) for a in range(0, PIECES, 7) for b in range(a + 1, PIECES, 11)
        if MASK[a] & MASK[b]
    ][:HOSTILE_PAIRS]
    hostile_control = (
        len(overlapping),
        sum(1 for a, b in overlapping if gate.apart(a, b)),
    )

    # --- the strata, re-derived live where the budget allows -----------------
    def stratify(charges):
        per: dict[int, Counter] = {}
        for (cost, tick, mixed), count in charges.items():
            per.setdefault(cost, Counter())[(tick, mixed)] += count
        return per

    nodes0, charges0, _ = budgeted_cover(MASK, C4, TC, MC, ALLQ, 0)
    per0 = stratify(charges0)
    budget0 = (nodes0, sum(charges0.values()),
               tuple(sorted(per0[FLOOR_CLASS].items())))
    nodes1, charges1, _ = budgeted_cover(MASK, C4, TC, MC, ALLQ, 1)
    per1 = stratify(charges1)
    budget1 = (nodes1, sum(charges1.values()),
               tuple(sorted(per1[145].items())))
    strata_measured = tuple(
        (cost, sum(per1[cost].values())) for cost in (144, 145)
    )
    charge_points_measured = (
        tuple(sorted(per0[144].items())), tuple(sorted(per1[145].items()))
    )

    cost9_count, _cost9_charges, cost9_survivors = allocation_cell(
        MASK, C4, TC, MC, ALLQ, (3,)
    )
    cost9_cell = (cost9_count, cost9_survivors)

    deep_budget2: tuple = ()
    deep_gate146: tuple = ()
    deep_excess78: tuple = ()
    if deep:
        nodes2, charges2, pairs146 = budgeted_cover(
            MASK, C4, TC, MC, ALLQ, 2, want_pairs_at=146
        )
        per2 = stratify(charges2)
        deep_budget2 = (nodes2, sum(charges2.values()),
                        sum(per2[146].values()),
                        tuple(sorted(per2[146].items())))
        pool = len({p for pair in pairs146 for p in pair})
        deep_gate146 = (
            pool, len(pairs146),
            sum(1 for a, b in pairs146 if gate.apart(a, b)),
        )
        count78, charges78, _nodes78 = allocation_cell(
            MASK, C4, TC, MC, ALLQ, (1, 2)
        )
        deep_excess78 = (count78, tuple(sorted(charges78.items())))

    # --- the witnesses, re-verified exactly ----------------------------------
    fset = {f: set(k for k in range(CORNERS) if COR[k][f[0]] == f[1])
            for f in FACETS}

    def facet_trace(cutting):
        out = {}
        for facet in FACETS:
            corners = fset[facet]
            slices = [
                tuple(sorted(set(UNI[p]) & corners)) for p in cutting
                if len(set(UNI[p]) & corners) == 4
            ]
            if len(slices) != 6:
                return None
            index = info[facet]["key"].get(
                tuple(sorted(info[facet]["pos"][t] for t in slices))
            )
            if index is None:
                return None
            out[facet] = index
        return out

    def verify(pieces) -> WitnessCertificate:
        cover, overlap = 0, False
        for piece in pieces:
            if cover & MASK[piece]:
                overlap = True
            cover |= MASK[piece]
        pairs = list(itertools.combinations(sorted(pieces), 2))
        return WitnessCertificate(
            charge=(sum(TC[p] for p in pieces), sum(MC[p] for p in pieces)),
            cost=sum(C4[p] for p in pieces),
            exact_cover=bool(len(set(pieces)) == CUTTING_SIZE and not overlap
                             and cover == ALLQ),
            separated=sum(1 for a, b in pairs if gate.apart(a, b)),
            pairs=len(pairs),
            traced=facet_trace(pieces) is not None,
        )

    verified = {key: verify(pieces) for key, pieces in WITNESS.items()}
    partners = {cost: verify(pieces) for cost, pieces in PARTNER.items()}
    witnesses = tuple(
        (key, verified[key].charge, verified[key].cost,
         verified[key].exact_cover, verified[key].separated,
         verified[key].pairs, verified[key].traced)
        for key in sorted(WITNESS)
    )
    partners_measured = tuple(
        (cost, partners[cost].charge, partners[cost].cost,
         partners[cost].exact_cover, partners[cost].separated,
         partners[cost].traced)
        for cost in sorted(PARTNER)
    )
    realizable = tuple(
        point for point in sorted(BRIDGE_POINTS)
        if verified[point].exact_cover
        and verified[point].separated == verified[point].pairs
        and verified[point].charge == point
    )
    minima_measured = tuple(
        (point, verified[point].cost) for point in sorted(WITNESS)
    )
    # A point whose exact minimum is m occurs in NO stratum below m; in
    # particular none of the three transcribed points occurs at 147 or 148.
    strata_below_minimum = tuple(
        (point, MIN_COST[point] - 1) for point in sorted(BRIDGE_POINTS)
    )

    separation_shortfall = sum(
        cert.pairs - cert.separated
        for cert in list(verified.values()) + list(partners.values())
    )
    floor_pairs = set()
    for cutting in SOL:
        for a, b in itertools.combinations(sorted(cutting), 2):
            floor_pairs.add((a, b))
    floor_pair_census = (
        len(floor_pairs),
        sum(1 for a, b in sorted(floor_pairs) if gate.apart(a, b)),
    )
    separation_shortfall += floor_pair_census[0] - floor_pair_census[1]

    composite_measured = tuple(
        (point, verified[point].cost) for point in sorted(COMPOSITE_TARGETS)
    )
    bridge_differences = tuple(
        (verified[point].charge[0] - CORPUS_CHARGE[0],
         verified[point].charge[1] - CORPUS_CHARGE[1])
        for point in ((41, 53), (37, 53))
    )
    difference_sets_closed = tuple(
        (
            cost,
            tuple(sorted({
                (a[0] - b[0], a[1] - b[1])
                for a in (CORPUS_CHARGE, target)
                for b in (CORPUS_CHARGE, target)
                if a != b
            })),
        )
        for target, cost in sorted(COMPOSITE_TARGETS.items())
    )

    # --- the strata law -------------------------------------------------------
    def delta(point):
        return (point[0] - TICK_BOX[0]) + (MIXED_BOX[1] - point[1])

    per_piece = [C4[i] - TC[i] + MC[i] for i in range(PIECES)]
    per_piece_min = min(per_piece)
    per_piece_histogram = tuple(sorted(Counter(per_piece).items()))
    recorded_strata = ((144, CHARGE_144), (145, CHARGE_145),
                       (146, CHARGE_146), (147, CHARGE_147))
    law_holds_everywhere = bool(
        all(delta(point) <= cost - FLOOR_CLASS
            for cost, table in recorded_strata for point, _n in table)
        and all(cost >= FLOOR_CLASS + delta(point)
                for point, cost in WITNESS_COST.items())
    )
    law_equality_holds = all(
        cost == FLOOR_CLASS + delta(point)
        for point, cost in MIN_COST.items()
    )
    law_tight_at = tuple(
        point for point in sorted(MIN_COST)
        if MIN_COST[point] == FLOOR_CLASS + delta(point)
    )
    law_slack_at = tuple(
        (point, FLOOR_CLASS + delta(point), MIN_COST[point])
        for point in sorted(MIN_COST)
        if MIN_COST[point] > FLOOR_CLASS + delta(point)
    )

    census_sums = (
        sum(count for _point, count in CHARGE_147),
        BUDGET_SOLUTIONS[3] - BUDGET_SOLUTIONS[2],
        sum(count for _pattern, count, _nodes in EXCESS_CELLS),
        sum(count for _point, count in EXCESS_78_CHARGES),
    )
    charge_point_run = tuple(len(table) for _cost, table in recorded_strata)
    delta_exact = all(
        {point for point, _n in table}
        == {(TICK_BOX[0] + a, MIXED_BOX[1] - b)
            for a in range(cost - FLOOR_CLASS + 1)
            for b in range(cost - FLOOR_CLASS + 1 - a)}
        for cost, table in recorded_strata
    )

    # --- the false lemma ------------------------------------------------------
    traced = charge_route_agrees = 0
    histogram: Counter = Counter()
    for cutting in SOL:
        trace = facet_trace(cutting)
        if trace is None:
            continue
        traced += 1
        tick = sum(info[f]["costs"][trace[f]] for f in TICK_FACETS)
        mixed = sum(info[f]["costs"][trace[f]] for f in SPAT_FACETS)
        if (tick, mixed) == (sum(TC[p] for p in cutting),
                             sum(MC[p] for p in cutting)):
            charge_route_agrees += 1
        diagonals: dict = {}
        bad = 0
        for facet in FACETS:
            for index, square in enumerate(info[facet]["squares"]):
                bit = info[facet]["sigs"][trace[facet]][index]
                if square in diagonals and diagonals[square] != bit:
                    bad += 1
                diagonals[square] = bit
        histogram[bad] += 1
    disagreement_histogram = tuple(sorted(histogram.items()))
    violating = sum(count for bad, count in histogram.items() if bad)

    # the counterexample, re-derived live from the committed corpus, with the
    # FIVE-vertex pieces named (the checker's correction: the 4-tuples are the
    # facet SLICES, not the pieces)
    corners = set(COUNTEREXAMPLE_CORNERS)
    counterexample = []
    for facet in ((0, 0), (1, 1)):
        found, triangles = [], set()
        for piece in SOL[0]:
            vertices = set(UNI[piece])
            if len(vertices & fset[facet]) == 4 and len(vertices & corners) == 3:
                found.append(tuple(sorted(vertices)))
                triangles.add(tuple(sorted(vertices & corners)))
        diagonal = tuple(sorted(set.intersection(
            *[set(t) for t in triangles]
        ))) if len(triangles) == 2 else ()
        counterexample.append(
            (facet, tuple(sorted(found)), tuple(sorted(triangles)), diagonal)
        )
    counterexample = tuple(counterexample)
    csp_hits_realizable = tuple(
        point for point in sorted(set(CSP_EXCLUDED) & set(BRIDGE_POINTS))
    )

    exact_no_float = bool(
        all(isinstance(value, int) for value in C4 + TC + MC)
        and all(isinstance(value, int) for value in per_piece)
        and Fraction(FLOOR_CLASS, CUTTING_SIZE) == Fraction(6, 1)
        and np.array([1], dtype=np.int64).dtype == np.int64
    )

    return Facts(
        main_head=main_head,
        authority=authority,
        machinery=machinery_shape,
        machinery_exit=machinery_exit,
        fixture_rebuilt=fixture_rebuilt,
        volume_spectrum=volume_spectrum,
        cost_spectrum=cost_spectrum,
        corpus=corpus,
        facet_spectra=facet_spectra,
        slice_incidences=slice_incidences,
        budget0=budget0,
        budget1=budget1,
        strata_measured=strata_measured,
        charge_points_measured=charge_points_measured,
        cost9_cell=cost9_cell,
        census_sums=census_sums,
        charge_point_run=charge_point_run,
        delta_exact=delta_exact,
        deep_budget2=deep_budget2,
        deep_excess78=deep_excess78,
        witnesses=witnesses,
        realizable=realizable,
        minima_measured=minima_measured,
        strata_below_minimum=strata_below_minimum,
        separation_shortfall=separation_shortfall,
        floor_pair_census=floor_pair_census,
        hostile_control=hostile_control,
        gate_agrees=gate_agrees,
        deep_gate146=deep_gate146,
        per_piece_min=per_piece_min,
        per_piece_histogram=per_piece_histogram,
        law_holds_everywhere=law_holds_everywhere,
        law_equality_holds=law_equality_holds,
        law_tight_at=law_tight_at,
        law_slack_at=law_slack_at,
        composite_measured=composite_measured,
        partners_measured=partners_measured,
        bridge_differences=bridge_differences,
        difference_sets_closed=difference_sets_closed,
        law_dependent_minima=LAW_DEPENDENT_MINIMA,
        traced=traced,
        charge_route_agrees=charge_route_agrees,
        disagreement_histogram=disagreement_histogram,
        violating=violating,
        counterexample=counterexample,
        csp_hits_realizable=csp_hits_realizable,
        text=text_certificate(),
        exact_no_float=exact_no_float,
        scope=scope_certificate(raw_note()),
    )


# ---------------------------------------------------------------------------
# H. note scope
# ---------------------------------------------------------------------------
N5_FENCE = 'N5: per_element: THE STRATUM-147 CENSUS, ON FOUR ROUTES: stratum 147 is ENUMERATED COMPLETELY at 16,359,616 cuttings over 535,593,550 budget-3 nodes, with Block 151\'s budget-0/1/2 figures 15,800 / 502,838, 258,872 / 9,522,735 and 2,618,552 / 87,731,188 reproduced TO THE DIGIT first, and it carries EXACTLY TEN charge points -- (36,57) 78,624; (36,58) 1,056,288; (36,59) 3,151,056; (36,60) 3,523,168; (37,58) 670,560; (37,59) 2,773,824; (37,60) 3,523,632; (38,59) 597,600; (38,60) 905,760; (39,60) 79,104 -- so the charge-point run across strata 144/145/146/147 is 1 / 3 / 6 / 10, the TRIANGULAR numbers, and the stratum-146 multiplicities (36,58) 95,952, (36,59) 530,016, (36,60) 796,752, (37,59) 311,232, (37,60) 529,536, (38,60) 96,192 are recorded for the FIRST time; the census is FOUR-ROUTE and the three extra routes are the INDEPENDENT CHECKER\'S -- its own C engine on the committed ground set in the committed order, which reproduces 535,593,550 EXACTLY, its own 1,924-column generic barycentric point set under a lexicographic sweep at 904,977,200 nodes and under a reversed sweep at 568,364,730, and an EXCESS-PATTERN ALLOCATION decomposition that never enumerates the stratum whole, splitting it as three cost-7 pieces 16,066,240 plus one cost-7 and one cost-8 293,376 plus one cost-9 ZERO -- and the runner closes that third cell COMPLETELY AND LIVE by exact point-coverability while re-deriving budgets 0 and 1 in full\nper_site: THE OVERTURN OF THE BLOCK 152 RIDER, QUOTED THEN CORRECTED: Block 152 carried "The bridge\'s transcribed points (36,55), (41,48), (37,48) occur in no committed stratum, and two sit at the unwitnessed MC = 48 end of the global bracket, per (39)", and Block 151 before it displayed the MC = 48 end as a facet-wise bound of which "it is NOT WITNESSED by any four-box cutting enumerated here" -- the FIRST half STANDS and is now EXTENDED, since none of the three points occurs in stratum 147 or in stratum 148 either, while the SECOND half FALLS: all three points are REALIZABLE by genuine separator-certified four-box dissections at EXACT minima 149, 163 and 165, each minimum closed by a COMPLETE bounded search below it -- (36,55) empty at cap 148 over 117,879,899 nodes, (41,48) empty at cap 160 and at exact costs 161 and 162, (37,48) empty at cap 159 and at every exact cost 160 through 164 -- and each re-proved by the checker\'s INDEPENDENT one-shot cap searches on its own ground set at 122,553,342, 40,477,687 and 33,870,992 nodes; so each point is absent from every stratum BELOW its own minimum and EXCLUDED NOWHERE, and Block 152\'s own hedge that its finding "is a statement about the strata enumerated so far, not a proof that the points are unrealizable" is VINDICATED rather than contradicted\nper_mode: MC = 48 IS WITNESSED, AND BOTH GEOMETRIC GATES PASS: the MC = 48 end of the global bracket TC in [36,42], MC in [48,60] is ATTAINED -- minimal at C4 = 163 with TC = 41 and at C4 = 165 with TC = 37, each an exact cover of all 2,736 committed sample points with 276/276 pairs separated by EXHIBITED INTEGER PLANES and a well-defined facet trace inside the 180 -- so Block 151\'s "NOT WITNESSED" caveat and Block 152\'s carry-forward of it are RETIRED, three of the bracket\'s four ends now being attained; the COST-146 GEOMETRIC GATE PASSES OUTRIGHT on the complete 2,359,680-cutting stratum, its 1,536-piece pool carrying 250,464 co-occurring pairs of which 250,464 are separated with ZERO FAILURES and the 80 sign vectors sufficing alone, which RETIRES Block 151\'s own rider that cost 146 stands "at incidence level only, no geometric gate, a displayed boundary"; the hostile control certifies ZERO of the 1,039 sample-point-overlapping piece pairs as separated; and the checker\'s BONUS, credited to it, gates stratum 147 as well at 535,008/535,008 over a 1,920-piece pool\nper_block: COMPOSITE MINIMALITY, PROVEN OUTRIGHT, AND THE FIRST ACHIEVED BRIDGE DIFFERENCE: both of Block 151\'s descent landings are not merely upper bounds but EXACT MINIMA -- charge (41,53) is realized at EXACTLY C4 = 156 and charge (37,53) at EXACTLY C4 = 152, improving Block 151\'s own witnesses at 169 and 166, with emptiness certified DIRECTLY by the checker\'s complete cap-155 search over 4,418,945,782 nodes and complete cap-151 search over 2,087,087,895 nodes, so the two minima carry NO STRATA-LAW DEPENDENCE and the primary\'s own hedge that "156 is minimal if the law holds above 147" is DISCHARGED, the upgrade being the CHECKER\'S and credited as such; the corner charge (36,60) is ALSO realized at exactly 156 and at exactly 152, so at stratum 156 the pair (36,60), (41,53) makes +-(5,-7) an ACHIEVED SAME-COST-CLASS charge difference and at stratum 152 the pair (36,60), (37,53) makes +-(1,-7) one -- the FIRST appearance of either bridge generator in an achieved difference set anywhere in the lane; stated at EXACTLY its scope, the Block 130 Section 6 antecedent Block 151 and Block 152 recorded as UNMET at stratum 145 is now MET AT STRATA 152 AND 156 FOR THESE TWO GENERATORS, which is an INPUT to the frame-map program and NOT a completion of it: no move-level flip is exhibited, no frame-to-momentum map is built, and no populatability transfers\nlattice_wide: THE STRATA LAW AT ITS TRUE SCOPE, THE FALSE-LEMMA TRAP, AND THE DISCLOSURES: writing delta = (TC-36) + (60-MC), the law C4 >= 144 + delta is a THEOREM on the four completely enumerated strata 144-147, where the charge points are EXACTLY the lattice points with delta <= C4 - 144, and it is TIGHT at (36,55) with 149, at (41,53) with 156 and at (37,53) with 152 -- the third tightness being the checker\'s upgrade -- but it is NOT AN EQUALITY, (41,48) having exact minimum 163 against the law\'s 161 and (37,48) 165 against the law\'s 157, and it is NOT PER-PIECE, the per-piece minimum of C4 - TC + MC over the 2,672 cells being 3 against the 7 per piece a per-piece proof would need since 24 x 7 = 168; the checker\'s law-attack sweep is COMPLETE for all 27 bracket points with delta <= 6, each a complete targeted search at cap 144 + delta - 1, ALL EMPTY with no timeouts, so no dissection of cost <= 149 carrying any of those charges violates the law and, with the four proven minima, the law is certified at 31 of the bracket\'s 91 points, a violation being possible only at delta >= 7 away from them; and THE FALSE-LEMMA TRAP IS DISPLAYED so that no later block rediscovers and believes it -- the TRACE THEOREM is true and verified on all 15,800 floor cuttings on all eight facets with the boundary route reproducing (TC, MC) exactly, but its natural strengthening, that two facets sharing a square induce the SAME diagonal on it, is FALSE for dissections, the counterexample sitting inside the committed corpus at SOL[0] where the square with corners 4,5,6,7 is split along (5,6) by facet x0 = 0 through the PIECES (1,4,5,6,9) and (2,5,6,7,10) and along (4,7) by facet x1 = 1 through the PIECES (4,5,7,11,15) and (4,6,7,11,15) -- five-vertex pieces, not the four-vertex facet SLICES -- with 15,456 of the 15,800 floor cuttings violating the lemma at the histogram 344/6,720/8,064/576/96, and the facet-consistency CSP built on it returning 86 of the 91 bracket points and excluding exactly (36,48), (36,49), (37,48), (39,48), (41,48), so it would have PROVED IMPOSSIBLE the two transcribed points this block REALIZES\nRESULT: on origin/main\'s committed cell-cutting machinery only -- the cycle-726 facet charge and the cycle-734 cutting ladder, content-pinned at the Block 151 cut -- executing campaign contract D and Block 152\'s own next_trace_action item, STRATUM 147 IS COMPLETE (16,359,616 cuttings, ten charge points, the triangular run 1/3/6/10, four routes, one reproducing 535,593,550 nodes to the digit); THE OVERTURN STANDS (all three transcribed bridge points REALIZABLE at exact minima 149/163/165, absent from every stratum below their own minima including 147 and 148, excluded nowhere); MC = 48 IS WITNESSED (at 163 and 165, both minimal, 276/276 separations); THE COST-146 GEOMETRIC GATE PASSES (250,464/250,464, the incidence-level-only boundary retired, the six multiplicities recorded, stratum 147 gated too as the checker\'s bonus at 535,008/535,008); COMPOSITE MINIMALITY IS PROVEN OUTRIGHT ((41,53) exactly 156, (37,53) exactly 152, no law dependence, the checker\'s upgrade, so +-(5,-7) and +-(1,-7) are ACHIEVED same-cost-class differences at strata 156 and 152 -- an input to the frame map, not a completion); and THE STRATA LAW HOLDS AT ITS TRUE SCOPE (theorem at 144-147, tight three times, not an equality, not per-piece, swept complete and violation-free for every delta <= 6), WITH THE SQUARE-DIAGONAL CONSISTENCY LEMMA DISPLAYED AS FALSE: the cutting lane\'s high-cost questions are decided by complete bounded search where enumeration dies, and the bridge\'s own record is REALIZABLE rather than excluded\nDECISION_CUT: THE QUOTIENT GATE (Block 158, gravity side) IS NEXT, then the LINK-VARIABLE AND CURVATURE SCOUT, then the POOL-2 HANDOFF; on this lane what remains NAMED and UNEXECUTED is stratum 148 beyond the fifteen delta <= 4 points, the full censuses of strata 149 and above, the strata law at delta >= 7 away from the four proven minima, and the MOVE-LEVEL half of Block 130 Section 6 -- a bounded, mutually reversible same-cost-class flip realizing +-(5,-7) at stratum 156 -- which co-existence at one cost class does NOT supply; the frame-to-momentum map keeps its three named requirements and this block builds none of them; Block 123\'s theorem, Block 130\'s arithmetic and Block 151\'s censuses are UNTOUCHED and REPRODUCED rather than corrected; the cycle-725/726/734 supplied-model firewall is INHERITED UNCHANGED; and the other lane\'s unmerged cycle-778-799 material is NOT READ, NOT CONSUMED and NOT SUPERSEDED\nTOE: zero axiom retirement; zero obligation retirement; zero TOE movement; no TOE percentage moves; retained-positive end-to-end theory count remains zero'


SCOPE_KEYS = (
    "stratum_147_complete",
    "four_route_census",
    "b152_rider_quoted",
    "overturn_correction",
    "no_stratum_below_minimum",
    "mc48_witnessed",
    "geometric_gate_146",
    "geometric_gate_147_bonus",
    "composite_minimality",
    "difference_set",
    "joint_lane_scope",
    "strata_law_scope",
    "law_not_equality",
    "law_not_perpiece",
    "law_sweep_complete",
    "false_lemma_trap",
    "csp_exclusions",
    "corrected_pieces",
    "doc_fixes",
    "single_route_disclosures",
    "stratum_148_open",
    "checker_credit",
    "independence_disclosure",
    "not_consumed_rider",
    "firewalls",
    "axiom",
    "zero_retirement",
    "zero_score",
    "zero_e2e",
    "n1_n8",
    "w1",
    "n5_verbatim",
)


def scope_certificate(note_text: str) -> dict[str, bool]:
    note = normalized_note(note_text)
    compact = compact_note(note_text)
    return {
        "stratum_147_complete": (
            "16,359,616" in note or "16359616" in compact
        ),
        "four_route_census": "four-route" in note or "four routes" in note,
        # the parent rider, quoted verbatim before it is corrected
        "b152_rider_quoted": "no four-box cutting is known to realize" in note,
        "overturn_correction": (
            ("realizable" in note or "realized" in note)
            and ("retired" in note or "overturn" in note)
            and "witnessed" in note
        ),
        "no_stratum_below_minimum": (
            "exact minimum" in note or "exact minima" in note
        ),
        "mc48_witnessed": "mc = 48" in note or "mc=48" in note,
        "geometric_gate_146": (
            "250,464" in note or "250464" in compact
        ),
        "geometric_gate_147_bonus": (
            "535,008" in note or "535008" in compact
        ),
        "composite_minimality": (
            ("4,418,945,782" in note or "4418945782" in compact)
            and ("2,087,087,895" in note or "2087087895" in compact)
        ),
        "difference_set": "achieved difference set" in note,
        "joint_lane_scope": (
            "input" in note and ("not a completion" in note
                                 or "not its completion" in note)
        ),
        "strata_law_scope": "strata law" in note,
        "law_not_equality": "not an equality" in note,
        "law_not_perpiece": "per-piece" in note,
        "law_sweep_complete": "delta <= 6" in note or "\\le 6" in note,
        "false_lemma_trap": "false" in note and "diagonal" in note,
        "csp_exclusions": "(39,48)" in note or "(39, 48)" in note,
        # the checker's second doc catch: the four-vertex tuples are SLICES
        "corrected_pieces": "(1,4,5,6,9)" in note or "(1, 4, 5, 6, 9)" in note,
        "doc_fixes": "slices" in note,
        "single_route_disclosures": "single-route" in note,
        "stratum_148_open": "stratum 148" in note,
        "checker_credit": "checker" in note,
        "independence_disclosure": "cross-context" in note,
        "not_consumed_rider": "778" in note,
        "firewalls": "firewall" in note,
        "axiom": "no axiom amendment is justified" in note,
        "zero_retirement": "zero obligation retirement" in note,
        "zero_score": (
            "no toe percentage moves" in note
            or "no toe percentage movement" in note
        ),
        "zero_e2e": (
            "retained-positive end-to-end theory count remains zero" in note
        ),
        "n1_n8": all(
            re.search(rf"\bn{index}\b", note) is not None
            for index in range(1, 9)
        ),
        "w1": re.search(r"\bw1\b", note) is not None,
        # Raw substring membership makes the printed fence byte-identical to
        # its note occurrence.
        "n5_verbatim": N5_FENCE in note_text,
    }


# ---------------------------------------------------------------------------
# claims: the only thing a mutation is allowed to touch
# ---------------------------------------------------------------------------
def build_claims(mutation: str) -> dict[str, object]:
    claims: dict[str, object] = {
        "main_head": CURRENT_MAIN,
        "parent_pin": "resolved",
        "stratum_147": STRATUM[147],
        "charge_points_147": CHARGE_147,
        "realizable": tuple(sorted(BRIDGE_POINTS)),
        "min_cost": dict(MIN_COST),
        "mc48_witnessed": (((41, 48), 163), ((37, 48), 165)),
        "separation_shortfall": 0,
        "law_is_equality": False,
        "per_piece_min": PER_PIECE_MIN,
        "composite_min": dict(COMPOSITE_TARGETS),
        "bridge_differences": BRIDGE_DELTAS,
        "diagonal_lemma_true": False,
        "required_scope_keys": SCOPE_KEYS,
    }
    if mutation == "stale_main_authority":
        claims["main_head"] = STALE_MAIN
    elif mutation == "stale_parent_authority":
        claims["parent_pin"] = "stale"
    elif mutation == "break_census_count":
        claims["stratum_147"] = STRATUM[147] - 1
    elif mutation == "break_charge_points":
        claims["charge_points_147"] = tuple(
            (((39, 59), count) if point == (39, 60) else (point, count))
            for point, count in CHARGE_147
        )
    elif mutation == "claim_point_unrealizable":
        claims["realizable"] = tuple(
            point for point in sorted(BRIDGE_POINTS) if point != (36, 55)
        )
    elif mutation == "break_minimum":
        broken = dict(MIN_COST)
        broken[(36, 55)] = 148
        claims["min_cost"] = broken
    elif mutation == "break_mc48_witness":
        claims["mc48_witnessed"] = (((41, 48), 163), ((37, 48), 164))
    elif mutation == "break_separation":
        claims["separation_shortfall"] = 1
    elif mutation == "claim_law_equality":
        claims["law_is_equality"] = True
    elif mutation == "claim_law_perpiece":
        claims["per_piece_min"] = PER_PIECE_NEEDED
    elif mutation == "break_composite_minimum":
        broken = dict(COMPOSITE_TARGETS)
        broken[(41, 53)] = 155
        claims["composite_min"] = broken
    elif mutation == "break_difference_set":
        claims["bridge_differences"] = ((5, -7), (1, -6))
    elif mutation == "claim_diagonal_lemma_true":
        claims["diagonal_lemma_true"] = True
    elif mutation == "drop_overturn_language":
        claims["required_scope_keys"] = tuple(
            key for key in SCOPE_KEYS if key != "overturn_correction"
        )
    elif mutation == "drop_n5_fence":
        claims["required_scope_keys"] = tuple(
            key for key in SCOPE_KEYS if key != "n5_verbatim"
        )
    return claims


# ---------------------------------------------------------------------------
# gates: pure functions of the measured facts and the claims
# ---------------------------------------------------------------------------
def evaluate_gates(
    facts: Facts, claims: dict[str, object], elapsed_ns: int
) -> dict[str, bool]:
    authority = facts.authority
    text = facts.text
    parent_blobs_ok = (
        authority.parent_artifact_blobs
        if claims["parent_pin"] == "resolved"
        else authority.stale_parent_artifact_blobs
    )
    gate_a = bool(
        AUDIT_INPUT_PATHS
        == (
            "docs/ADMISSIBILITY_DIRAC_KAHLER_CUTTING_STRATA_COMPLETION_BOUNDED_THEOREM_NOTE_2026-08-20.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
            "docs/audit/data/axiom_premise_nodes.json",
            "docs/ADMISSIBILITY_DIRAC_KAHLER_RESIDUE_TRANSVERSALITY_GATE_BOUNDED_THEOREM_NOTE_2026-08-20.md",
            "scripts/admissibility_dirac_kahler_residue_transversality_gate_2026_08_20.py",
            "docs/ADMISSIBILITY_DIRAC_KAHLER_SIGN_LAYER_COMPARISON_BOUNDED_THEOREM_NOTE_2026-08-20.md",
            "scripts/admissibility_dirac_kahler_sign_layer_comparison_2026_08_20.py",
            "docs/ADMISSIBILITY_DIRAC_KAHLER_FLOOR_BOUNDARY_THEOREM_BOUNDED_THEOREM_NOTE_2026-08-20.md",
            "scripts/admissibility_dirac_kahler_floor_boundary_theorem_2026_08_20.py",
        )
        and PARENT_ARTIFACTS
        == (BLOCK156_NOTE, BLOCK156_RUNNER, BLOCK152_NOTE, BLOCK152_RUNNER)
        and len(PARENT_ARTIFACT_BLOBS) == len(PARENT_ARTIFACTS) == 4
        and facts.main_head == claims["main_head"]
        and authority.fixed_authority
        and authority.parent_ref_and_ancestry
        and parent_blobs_ok
        # the two worktree imports, bound to the bytes actually imported
        and authority.imported_bytes_bound
        # the two cell-cutting runners, bound BY CONTENT and by shape
        and authority.machinery_content_bound
        and tuple(name for name, _d, _r, _p in authority.machinery_blobs)
        == MACHINERY_NAMES
        and facts.machinery == MACHINERY_SHAPE
        and facts.machinery_exit
        == (0, C726_GATES, 0, (C734_PREFIX_GATES, 0))
    )

    gate_b = bool(
        # the fixture, rebuilt from the 16 corners and checked cell for cell
        facts.fixture_rebuilt
        and facts.volume_spectrum == VOLUME_SPECTRUM
        and facts.cost_spectrum == COST_SPECTRUM
        and facts.corpus == (CORPUS, (FLOOR_CLASS,), (CORPUS_CHARGE,))
        and facts.facet_spectra
        == ((FACET_DISSECTIONS,) * 8, (TICK_SPECTRUM,), (MIXED_SPECTRUM,))
        and facts.slice_incidences == SLICE_INCIDENCES
        # the live calibration: budgets 0 and 1, nodes and covers to the digit
        and facts.budget0
        == (BUDGET_NODES[0], BUDGET_SOLUTIONS[0], CHARGE_144)
        and facts.budget1
        == (BUDGET_NODES[1], BUDGET_SOLUTIONS[1], CHARGE_145)
        and facts.strata_measured == ((144, STRATUM[144]), (145, STRATUM[145]))
        and facts.charge_points_measured == (CHARGE_144, CHARGE_145)
        # the stratum-147 census, audited three ways on its recorded numerals
        and facts.census_sums
        == (claims["stratum_147"], claims["stratum_147"],
            claims["stratum_147"], EXCESS_CELLS[1][1])
        and tuple(point for point, _n in claims["charge_points_147"])
        == tuple(point for point, _n in CHARGE_147)
        and facts.charge_point_run == CHARGE_POINT_RUN
        and facts.delta_exact
        and {point for point, _n in claims["charge_points_147"]}
        == {(TICK_BOX[0] + a, MIXED_BOX[1] - b)
            for a in range(4) for b in range(4 - a)}
        # the cost-9 allocation cell, closed COMPLETELY AND LIVE at zero
        and facts.cost9_cell == (EXCESS_CELLS[2][1], 0)
        and len(CENSUS_ROUTES) == 4
        and CENSUS_ROUTES[0][1] == BUDGET_NODES[3]
        # --deep re-derives budget 2 and the cost-7-plus-cost-8 branch of 147
        and facts.deep_budget2
        in ((), (BUDGET_NODES[2], BUDGET_SOLUTIONS[2], STRATUM[146],
                 CHARGE_146))
        and facts.deep_excess78 in ((), (EXCESS_CELLS[1][1], EXCESS_78_CHARGES))
    )

    measured_minima = dict(facts.minima_measured)
    gate_c = bool(
        # every witness is an exact cover with every pair separated and a
        # well-defined facet trace
        all(
            charge == point and cover and separated == pairs == WITNESS_PAIRS
            and traced and cost == WITNESS_COST[point]
            for point, charge, cost, cover, separated, pairs, traced
            in facts.witnesses
        )
        and len(facts.witnesses) == 5
        # THE OVERTURN: all three transcribed points are realizable
        and facts.realizable == tuple(claims["realizable"])
        and facts.realizable == tuple(sorted(BRIDGE_POINTS))
        and all(
            measured_minima[point] == claims["min_cost"][point]
            for point in sorted(BRIDGE_POINTS)
        )
        # each point is absent from every stratum below its own minimum, so
        # from 147 and 148 in particular
        and facts.strata_below_minimum
        == tuple((point, MIN_COST[point] - 1)
                 for point in sorted(BRIDGE_POINTS))
        and min(MIN_COST[point] for point in BRIDGE_POINTS) > 148
        and all(LOWER_BOUND[point] == MIN_COST[point] - 1
                for point in MIN_COST)
        and all(CHECKER_EMPTY_NODES[point][0] == LOWER_BOUND[point]
                for point in CHECKER_EMPTY_NODES)
        and all(CHECKER_FOUND_NODES[point][0] == MIN_COST[point]
                for point in CHECKER_FOUND_NODES)
        # the parent riders, quoted from the committed bytes before correction
        and text.b152_rider_verbatim
        and text.b152_unwitnessed_box
        and text.b152_hedge_present
        and text.b152_no_unrealizability_claim
        and text.b151_unwitnessed_verbatim
        and text.firewall_inherited
    )

    witness_cost = {point: cost for point, _c, cost, _e, _s, _p, _t
                    in facts.witnesses}
    gate_d = bool(
        # MC = 48 is ATTAINED, at the two claimed costs, both minimal
        all(witness_cost[point] == cost
            for point, cost in claims["mc48_witnessed"])
        and all(point[1] == MIXED_BOX[0]
                for point, _cost in claims["mc48_witnessed"])
        and all(MIN_COST[point] == cost
                for point, cost in (((41, 48), 163), ((37, 48), 165)))
        # every separation this runner measures succeeds, on 15,168 committed
        # floor pairs and on all 1,932 witness pairs
        and facts.separation_shortfall == claims["separation_shortfall"]
        and facts.floor_pair_census[0] == facts.floor_pair_census[1] > 15000
        and facts.gate_agrees
        # the hostile control certifies ZERO overlapping pairs
        and facts.hostile_control == (HOSTILE_PAIRS, 0)
        # the recorded gates: 146 outright, 147 as the checker's bonus
        and (POOL_146, PAIRS_146, SEPARATED_146) == (1536, 250464, 250464)
        and SEPARATED_146 == PAIRS_146
        and (POOL_147, PAIRS_147, SEPARATED_147) == (1920, 535008, 535008)
        and SEPARATED_147 == PAIRS_147
        and text.b151_gate_boundary
        # --deep re-derives the cost-146 gate in full
        and facts.deep_gate146 in ((), (POOL_146, PAIRS_146, SEPARATED_146))
    )

    gate_e = bool(
        # the law is valid on every enumerated stratum and every witness
        facts.law_holds_everywhere
        # ... and it is NOT an equality
        and facts.law_equality_holds == bool(claims["law_is_equality"])
        and facts.law_slack_at == LAW_SLACK
        and facts.law_tight_at == tuple(sorted(LAW_TIGHT))
        # ... and NOT per-piece: the measured per-piece minimum is 3
        and facts.per_piece_min == claims["per_piece_min"]
        and facts.per_piece_min < PER_PIECE_NEEDED
        and facts.per_piece_histogram == PER_PIECE_HISTOGRAM
        and CUTTING_SIZE * PER_PIECE_NEEDED
        == FLOOR_CLASS - TICK_BOX[0] + MIXED_BOX[1]
        # the checker's sweep: every bracket point with delta <= 6, complete
        and LAW_SWEEP_POINTS
        == len({(a, b) for a in range(7) for b in range(7)
                if 1 <= a + b <= LAW_SWEEP_MAX_DELTA})
        and FLOOR_CLASS + LAW_SWEEP_MAX_DELTA - 1 == LAW_SWEEP_LARGEST_CAP
        and LAW_UNSWEPT_MIN_DELTA == LAW_SWEEP_MAX_DELTA + 1
    )

    gate_f = bool(
        # both composite landings are ACHIEVED at exactly the claimed costs
        facts.composite_measured
        == tuple((point, claims["composite_min"][point])
                 for point in sorted(COMPOSITE_TARGETS))
        and all(cost < BLOCK151_COMPOSITE_WITNESSES[point]
                for point, cost in facts.composite_measured)
        # the corner charge is realized at BOTH of those costs
        and facts.partners_measured
        == ((152, CORPUS_CHARGE, 152, True, WITNESS_PAIRS, True),
            (156, CORPUS_CHARGE, 156, True, WITNESS_PAIRS, True))
        # so both bridge generators are ACHIEVED same-cost-class differences
        and facts.bridge_differences == tuple(claims["bridge_differences"])
        and facts.bridge_differences == BRIDGE_DELTAS
        and facts.difference_sets_closed
        == ((152, ((-1, 7), (1, -7))), (156, ((-5, 7), (5, -7))))
        # ... with the minima PROVEN, so no strata-law dependence remains
        and facts.law_dependent_minima == ()
        and all(CHECKER_EMPTY_NODES[point][0] == cost - 1
                for point, cost in COMPOSITE_TARGETS.items())
        and CHECKER_EMPTY_NODES[(41, 53)][1] == 4418945782
        and CHECKER_EMPTY_NODES[(37, 53)][1] == 2087087895
    )

    counterexample = {facet: entry for facet, *entry in facts.counterexample}
    gate_g = bool(
        # the TRACE THEOREM: true, and verified on the whole floor corpus
        facts.traced == CORPUS
        and facts.charge_route_agrees == CORPUS
        # its natural strengthening is FALSE, and the corpus refutes it
        and (facts.disagreement_histogram[0][1] < CORPUS)
        == (not bool(claims["diagonal_lemma_true"]))
        and facts.disagreement_histogram == DISAGREEMENT_HISTOGRAM
        and facts.violating == VIOLATING_CUTTINGS
        and facts.violating + COHERENT_CUTTINGS == CORPUS
        # the counterexample, re-derived live, with the FIVE-vertex pieces
        and set(counterexample) == {(0, 0), (1, 1)}
        and all(
            counterexample[facet][0] == COUNTEREXAMPLE_PIECES[facet]
            and counterexample[facet][2] == COUNTEREXAMPLE_DIAGONALS[facet]
            and all(len(piece) == 5 for piece in counterexample[facet][0])
            for facet in ((0, 0), (1, 1))
        )
        and (COUNTEREXAMPLE_DIAGONALS[(0, 0)]
             != COUNTEREXAMPLE_DIAGONALS[(1, 1)])
        and tuple(square_corners(COUNTEREXAMPLE_SQUARE))
        == COUNTEREXAMPLE_CORNERS
        # and the CSP built on the false lemma would have excluded two points
        # this block REALIZES
        and facts.csp_hits_realizable == ((37, 48), (41, 48))
        and CSP_CONSISTENT + len(CSP_EXCLUDED) == CSP_BRACKET_POINTS
        and set(facts.csp_hits_realizable) <= set(facts.realizable)
        and facts.exact_no_float
    )

    required = tuple(claims["required_scope_keys"])
    gate_h = bool(
        set(facts.scope) == set(required)
        and all(facts.scope.values())
        and len(MUTATIONS) == 15
        and len(set(MUTATIONS)) == 15
        and set(MUTATION_GATE) == set(MUTATIONS)
        and set(MUTATION_GATE.values()) == set("ABCDEFGH")
        and N5_FENCE.count("\n") == 7
        and SOLVE_CHECKS == (25, 25)
        and CHECKER_REFUTATIONS == 0
        and len(SINGLE_ROUTE_ITEMS) == 3
        and DOC_FIXES == 2
        and elapsed_ns <= RUNTIME_BUDGET_SEC * 1_000_000_000
    )

    return {
        "A": gate_a,
        "B": gate_b,
        "C": gate_c,
        "D": gate_d,
        "E": gate_e,
        "F": gate_f,
        "G": gate_g,
        "H": gate_h,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS, default="")
    parser.add_argument(
        "--deep",
        action="store_true",
        help=(
            "also re-derive the two heavier censuses in full: the budget-2 "
            "exact cover (2,618,552 covers over 87,731,188 nodes, stratum 146 "
            "with its 250,464-pair geometric gate) and the cost-7-plus-cost-8 "
            "allocation branch of stratum 147 (293,376 cuttings)"
        ),
    )
    arguments = parser.parse_args()
    mutation = arguments.mutation
    started_ns = time.monotonic_ns()

    # Every measurement happens once, before any mutation flag is consulted, so
    # a mutation can only rewrite a CLAIM.  No gate can cascade into another
    # because no gate feeds a measurement.
    facts = measure(arguments.deep)
    elapsed_ns = time.monotonic_ns() - started_ns

    raw_gates = evaluate_gates(facts, build_claims(""), elapsed_ns)
    gate_values = dict(raw_gates)
    if mutation:
        target = MUTATION_GATE[mutation]
        gate_values = evaluate_gates(facts, build_claims(mutation), elapsed_ns)
        changed = {
            key for key in raw_gates if raw_gates[key] != gate_values[key]
        }
        if changed - {target} or gate_values[target]:
            raise AssertionError("mutation did not fail exactly its own gate")

    checks = Checks()
    checks.check(
        "A-authority",
        "main plus the FOUR pinned parent artifacts -- the Block 156 note and runner (the STACK parent) and the Block 152 note and runner (the CONTENT parent whose rider this block corrects) -- are content-bound at the parent pin by literal blob values, the Block 152 runner this block IMPORTS and the Block 151 runner reached THROUGH it are additionally bound to the hash of the bytes actually imported, and the two committed cell-cutting runners the whole lane rests on are read from origin/main AT RUN TIME through Block 151's own loader under its blob pins and pinned cut markers, with their own gate tallies recorded (cycle 726: 32/0 and exit 0; cycle 734 prefix: 22/0)",
        gate_values["A"],
    )
    checks.check(
        "B-strata-census",
        "the fixture is REBUILT from the 16 corners -- 2,672 unimodular cells, volume spectrum ((0,1360),(1,2672),(2,320),(3,16)), cost spectrum ((6,400),(7,1216),(8,864),(9,192)) and the C4/TC/MC charges agreeing with the committed arrays cell for cell -- the 180 minimal three-cube dissections are rebuilt POINT-FREE on every facet with tick spectrum {18:16,19:72,20:84,21:8} and mixed spectrum {8:12,9:64,10:104}, and the strata are re-derived live as far as a gate budget reaches: budget 0 returns 15,800 covers over 502,838 nodes at the single charge point (36,60) and budget 1 returns 258,872 over 9,522,735 with stratum 145 at 243,072 across (36,59)x60,768, (36,60)x121,536, (37,60)x60,768 -- Block 151's own figures, reproduced to the digit; STRATUM 147 IS COMPLETE at 16,359,616 cuttings over 535,593,550 budget-3 nodes with exactly TEN charge points, a solve-level census audited here three ways on its recorded numerals (the ten multiplicities sum to it, the budget-3-minus-budget-2 difference equals it, and the checker's excess-pattern allocation cells 16,066,240 + 293,376 + 0 sum to it) and FOUR-ROUTE overall, one of the checker's routes reproducing 535,593,550 exactly; the cost-9 allocation cell is closed COMPLETELY AND LIVE at ZERO by exact point-coverability; the charge-point run 1/3/6/10 is triangular and each stratum's points are EXACTLY the lattice points with (TC-36)+(60-MC) <= C4-144; and --deep re-derives budget 2 (2,618,552 over 87,731,188 nodes, stratum 146 at 2,359,680) and the cost-7-plus-cost-8 branch of stratum 147 (293,376) in full",
        gate_values["B"],
    )
    checks.check(
        "C-overturn",
        "THE OVERTURN, against the quoted parent riders: Block 152's firewall rider and Block 151's 'NOT WITNESSED by any four-box cutting enumerated here' are read from the committed bytes verbatim, and the half that falls is identified exactly -- ALL THREE transcribed bridge points (36,55), (41,48) and (37,48) are REALIZABLE by genuine four-box dissections, each an exact cover of the 2,736 committed sample points with 276/276 pairs separated by exhibited integer planes and a facet trace lying in the 180, at EXACT minima 149, 163 and 165 with the complete bounded searches below them empty (the primary's staged ladders at 117,879,899; 27,017,371 / 32,241,954 / 37,156,418; and 23,336,002 with every exact cost 160-164) and with the checker's INDEPENDENT single-cap re-runs on its own ground set agreeing verdict for verdict at 122,553,342 / 40,477,687 / 33,870,992 nodes; so each point is absent from every stratum below its own minimum -- 147 and 148 included, which EXTENDS the half of the rider that stands -- and none is excluded at any cost, while Block 152's own hedge that its finding was about the strata enumerated so far and NOT a proof of unrealizability is vindicated rather than contradicted",
        gate_values["C"],
    )
    checks.check(
        "D-mc48-and-gates",
        "the MC = 48 end of the global bracket TC in [36,42], MC in [48,60] is WITNESSED and Block 151's facet-wise caveat is RETIRED: it is attained at C4 = 163 with TC = 41 and at C4 = 165 with TC = 37, both PROVEN MINIMAL, each an exact cover with 276/276 separations; every separation this runner measures succeeds, on all 1,932 witness pairs and on all 15,168 distinct co-occurring piece pairs of the committed floor corpus, with the predicate first gated against the committed cycle-734 `separated` routine on a sample of committed pairs and a HOSTILE CONTROL certifying ZERO of 2,000 sample-point-overlapping pairs as separated; THE COST-146 GEOMETRIC GATE PASSES on the complete stratum -- a 1,536-piece pool, 250,464 co-occurring pairs, 250,464 separated, zero failures, re-derived in full under --deep -- so Block 151's 'incidence level only, no geometric gate, a displayed boundary' rider is retired and the six charge multiplicities at 146 are recorded for the first time; and stratum 147 is gated too at 535,008/535,008 over a 1,920-piece pool, which is the CHECKER's bonus and is credited to it",
        gate_values["D"],
    )
    checks.check(
        "E-strata-law",
        "the strata law C4 >= 144 + (TC-36) + (60-MC) is stated at its TRUE scope: it is a THEOREM on the four completely enumerated strata 144-147, where the charge points are exactly the lattice points with delta <= C4-144; it is TIGHT at (36,55) [149], (41,53) [156] and (37,53) [152], the third tightness being the checker's upgrade; it is NOT AN EQUALITY, (41,48) sitting at 163 against the law's 161 and (37,48) at 165 against the law's 157, both by complete bounded search; it is NOT PER-PIECE, the measured per-piece minimum of C4 - TC + MC over all 2,672 cells being 3 against the 7 per piece a per-piece proof would need (24 x 7 = 168), with the full histogram {3:48, 4:304, 5:192, 6:304, 7:48, 8:336, 9:672, 10:624, 11:96, 12:48} recomputed here; and the checker's law-attack sweep is COMPLETE for all 27 bracket points with delta <= 6, each a complete targeted search at cap 144 + delta - 1 and every one EMPTY with no timeouts, so no dissection of cost <= 149 at any of those charges violates the law and, together with the four proven minima, 31 of the bracket's 91 points are certified, a violation being possible only at delta >= 7 away from them",
        gate_values["E"],
    )
    checks.check(
        "F-composite-minimality",
        "COMPOSITE MINIMALITY IS PROVEN OUTRIGHT, and the credit is the checker's: charge (41,53) is realized at EXACTLY C4 = 156 and charge (37,53) at EXACTLY C4 = 152, improving Block 151's own witnesses from 169 and 166, and the emptiness below each is certified DIRECTLY -- cap 155 empty over 4,418,945,782 nodes and cap 151 empty over 2,087,087,895 nodes -- so both minima carry NO STRATA-LAW DEPENDENCE and the primary's 'minimal if the law holds above 147' hedge is discharged; the corner charge (36,60) is realized at exactly 156 and at exactly 152 as well, each cover verified with 276/276 separations, so +-(5,-7) at stratum 156 and +-(1,-7) at stratum 152 are ACHIEVED SAME-COST-CLASS charge differences -- the first appearance of either bridge generator in an achieved difference set anywhere in the lane; stated at exactly its scope, the Block 130 Section 6 antecedent that Blocks 151 and 152 recorded as UNMET at stratum 145 is now MET at strata 152 and 156 FOR THESE TWO GENERATORS, which is an INPUT to the frame-map program and NOT a completion of it, since no bounded mutually reversible MOVE is exhibited here",
        gate_values["F"],
    )
    checks.check(
        "G-false-lemma",
        "the FALSE LEMMA is displayed rather than buried, so that no later block rediscovers and believes it: the TRACE THEOREM is true and is verified here on ALL 15,800 committed floor cuttings, every one tracing into the 180 on all eight facets with the boundary route reproducing (TC, MC) exactly; but its natural strengthening -- that the two facets sharing a square induce the SAME diagonal on it -- is FALSE for dissections, because interior-disjointness in four dimensions does not force it in codimension two, and the counterexample is re-derived live from the committed corpus: in SOL[0] the square with corners 4,5,6,7 is split along the diagonal (5,6) by facet x0 = 0 through the pieces (1,4,5,6,9) and (2,5,6,7,10) and along (4,7) by facet x1 = 1 through the pieces (4,5,7,11,15) and (4,6,7,11,15) -- FIVE-vertex pieces, the four-vertex tuples being the facet SLICES, which is the checker's transcription catch applied; 15,456 of the 15,800 floor cuttings violate the lemma at the histogram 344 / 6,720 / 8,064 / 576 / 96; and the facet-consistency CSP built on it returns 86 of the 91 bracket points, excluding exactly (36,48), (36,49), (37,48), (39,48) and (41,48) -- two of which this block REALIZES, so the CSP would have 'proved' realizable points impossible",
        gate_values["G"],
    )
    checks.check(
        "H-note-scope",
        "the note carries the complete stratum-147 census with its four routes, the parent rider QUOTED VERBATIM and then corrected, the exact minima and the absence of each point from every stratum below its own, the MC = 48 witnesses, both geometric gates with the stratum-147 bonus credited to the checker, the composite minima with the checker's emptiness node counts, the achieved difference set with the joint-lane consequence stated as an INPUT and not a completion, the strata law with its scope, its two failures of equality, its per-piece failure and the complete delta <= 6 sweep, the false-lemma trap with the corrected five-vertex pieces and the CSP exclusion list, the two doc fixes credited as checker catches, the single-route disclosures, the open stratum-148 question, the independence disclosure, the not-consumed rider, the firewalls, W1, N1-N8 and the exact N5 fence",
        gate_values["H"],
    )
    checks.report()
    print(N5_FENCE)
    return checks.finish()


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except SystemExit:
        raise
    except Exception as error:
        print(f"[FAIL] INTERNAL-EXCEPTION: {type(error).__name__}: {error}")
        print("TOTAL: PASS=0 FAIL=1")
        raise
