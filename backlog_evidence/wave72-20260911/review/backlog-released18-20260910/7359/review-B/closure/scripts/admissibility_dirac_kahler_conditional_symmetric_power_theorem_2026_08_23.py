#!/usr/bin/env python3
"""BLOCK 177 -- THE CONDITIONAL SYMMETRIC-POWER THEOREM.

THE RESULT, AND ITS EXACT SCOPE.  On the committed antiperiodic Dirac-Kahler
fixtures at cover extents T_cover = 8 (T_phys = 4) and T_cover = 12 (T_phys = 6),
both at L_x = 4, with the xgraded carrier at sigma = 3/5, the region pin c = 1,
s_x = 3/5, m = 1 and the two temporal dials s_t = 1/4 (transport ON) and
s_t = 0 (the region):

  1. THE SYM^N LEMMA, COMPLEX-CORRECTED.  On the two symmetric monomials
     {u^n, u^(n-1) v} the n-particle Gram minor is
     det = n!(n-1)! p^(2n-2) (pq - |r|^2), with p = <u,u>, q = <v,v> and
     r = <u,v>.  THE SOLVE'S r^2 IS CORRECTED TO |r|^2 -- the checker's C2 --
     because the complex scope needs the modulus, and the corrected form is
     STRICTLY NEGATIVE FOR EVERY n >= 2 whenever p > 0 > q.  Rescaling raw
     monomials to divided or orthonormal symmetric tensors is a POSITIVE
     DIAGONAL CONGRUENCE and CANNOT CHANGE THE SIGN.  The complex antilinear
     Wick contraction gives EXACTLY the permanent -- the conjugations sit in the
     sesquilinearity -- so the solve's real-symmetric example was inadequate
     evidence and IS SUPERSEDED.

  2. THE OBJECT MISMATCH -- the checker's discovery, and this block's sharpest
     honest fact.  The solve graded the ACTION-side reflected pairing
     Bench.form = herm([r Q]_SS), but the committed Gaussian's Wick contractions
     see the COVARIANCE side [r (Q^-1)^T]_SS.  The Hermitianized difference at
     the (0,0) entry is EXACTLY -35233/38760 at 8x4 with s_t = 0, and the
     difference PERSISTS at both extents and at both dials.  THE QUASI-FREE
     SECTOR IDENTIFICATION IS THEREFORE A NAMED PREMISE, NOT A CONSEQUENCE, and
     B2b -- derive the framework's own committed functional grading -- is the
     NAMED SUCCESSOR.

  3. BOTH KERNELS, AND THE ROBUSTNESS THAT MAKES THE THEOREM WORTH STATING.  The
     Hermitianized covariance kernel reads (6,2,0)(n+,n-,n0)[b165] at 8x4 and
     (4,4,0)(n+,n-,n0)[b165] at 12x4 with s_t = 1/4 -- MIXED, exactly like the
     action-side (5,3,0) and (4,4,0) -- so the symmetric-power indefiniteness
     FIRES ON EITHER KERNEL CANDIDATE.  On the covariance side the mixture
     PERSISTS EVEN AT s_t = 0: its s_t = 0 inertias EQUAL its s_t = 1/4 ones,
     stated exactly as measured and NOT as the region result, which belongs to
     the ACTION side and reads (4,0,4) PSD.

  4. THE FIXTURE LEGS.  All four action-side inertias by TWO INDEPENDENT EXACT
     ROUTES -- charpoly-Descartes and the landed congruence/Schur instrument --
     with the s_t = 0 Schur complement identically 0_4 and THE FOUR NULL
     DIRECTIONS CONSTRUCTED rather than inferred.  The Jacobi minor-sign rule is
     applied at 12x4 on eight exactly nonzero leading minors, signs
     + + + + - + - +, FOUR changes; the 8x4 train is + + + + - - + -, THREE
     changes.  THE EXTENT ASYMMETRY IS REAL and is disclosed as a WRAP-CLASS
     OBSERVATION at T_phys = 4.

  5. THE WITNESSES.  u = e_0 gives 57/40 > 0 at both extents.  The checker's
     CLEAN witness v = e_0 - 5 e_4 gives EXACTLY -57/160 < 0 at 12x4 -- the
     margin constant again, since the on-dial 12x4 pairing is exactly
     [[57/40 I_4, (57/320) diag(1,-1,1,-1)], [same, 0_4]], displayed and
     entry-checked.  THE 57-FAMILY ECHO IS NOTED AND NOT OVER-READ.  At 8x4 the
     recorded w = e_4 - e_5 gives -65/512 < 0.  THE SOLVE'S OWN WITNESS VECTOR
     WAS NOT RECORDED and that provenance defect is DISCLOSED, not smoothed.

  6. THE VACUUM LEG.  det Q = c P(s_t)^4 SYMBOLICALLY at both extents, with
     P(0) = 66447280221259 and P'(0) = -13079847592350 at 8x4 and
     P(0) = 1993466346364384822133 and P'(0) = -744781636638830596050 at 12x4.
     The readout is PROPORTIONAL TO 1/|det Q|^2 -- the solve's naming slip
     CORRECTED -- positive trivially and dial-sensitive EXACTLY.  s_t is a FAIR
     TEMPORAL TRANSPORT DIAL (H and the region pin are s_t-free, Q is affine in
     s_t) and NOT a full connection-off dial, because s_x = 3/5 remains; the
     cleaner global dial Q_tau = H + tau A with A = Q - H is NAMED for
     successors.

  7. THE THEOREM, IN ITS HONEST CONDITIONAL FORM.  For any proper quasi-free
     reflected functional whose one-particle kernel is EITHER candidate, every
     n >= 1 sector is INDEFINITE at the tested dials at both extents, while the
     vacuum sector is POSITIVE and DIAL-SENSITIVE.  THAT IS SECTOR-UNIQUENESS
     ONLY.  The unconditional "the Born readout is the unique
     positive-with-transport window" is WITHDRAWN -- the checker's C5 --
     because positivity plus sensitivity alone does not select Z Zbar among
     positive functions.  The committed-kernel identification is B2b.

GATES
  A  authority: main plus the TWO Block 176 artifacts content-bound, the parent
     runner ACTUALLY IMPORTED, and the stale pin verified to carry NEITHER.
  B  the two banners -- the inertia convention and the imposed-object banner
     with the SECTOR IDENTIFICATION AS A NAMED PREMISE -- and both bench anchors.
  C  THE SYM^N LEMMA by direct symbolic permanent construction at n = 2, 3, 4.
  D  THE OBJECT MISMATCH, both kernels rebuilt, the exact -35233/38760 witness.
  E  the four action-side inertias by BOTH routes, the two minor-sign trains,
     and the s_t = 0 Schur complement constructed as 0_4.
  F  THE WITNESSES and the displayed 12x4 pairing, entry-checked.
  G  THE COVARIANCE-KERNEL INERTIAS at both dials, and THE VACUUM SYMBOLIC LEG.
  H  note at final path, the FULL scope-key certificate, and the N5 fence.

BASELINE EXPECTATION: 7 of 8, with H failing on note-at-final-path alone until
the note is landed at docs/.

RUNNING
  python3 scripts/admissibility_dirac_kahler_conditional_symmetric_power_theorem_2026_08_23.py
  python3 ... --list-mutations
  python3 ... --mutation claim_identification_derived
  python3 ... --deep

NOTES FOR THE LANDING AGENT
  1. PARENT_COMMIT is REAL and PARENT_REF resolves to it; nothing needs sed.
  2. CURRENT_MAIN was RE-RESOLVED at draft time.
  3. The stale pin is the Block 175 tip, a real ancestor of HEAD that carries
     NEITHER Block 176 artifact -- which is what makes the
     stale_parent_authority mutation bite.
  4. Re-run at landing; gate H should then pass and the battery should be 8/8.
"""

from __future__ import annotations

import argparse
import ast
import itertools
import subprocess
import sys
import time
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path

import sympy as sp

R = sp.Rational
Z0 = sp.Integer(0)
ONE = sp.Integer(1)

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
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

# THE PARENT IMPORT.  Block 176 is the stack parent AND the content parent: it
# re-exports the whole landed chain and it is the block whose named successor
# question -- the scalar-sector theorem -- this block answers in its honest
# conditional form.
try:
    import admissibility_dirac_kahler_complex_structure_synthesis_2026_08_23 as b176
    PARENT_IMPORT_LANDED = True
except ModuleNotFoundError:                                   # unlanded parent
    b176 = None
    PARENT_IMPORT_LANDED = False

if b176 is not None:
    b175 = b176.b175
    b174 = b176.b174
    b171 = b176.b171
    b170 = b176.b170
    b165 = b176.b165
else:                                                  # pragma: no cover
    b175 = None
    b174 = None
    import admissibility_dirac_kahler_generator_trilemma_kernel_2026_08_21 as b171
    b170 = b171.b170
    b165 = b171.b165

herm = b171.herm
is_zero = b171.is_zero
tri = b171.tri

# THE BENCH MACHINERY, IMPORTED FROM BLOCK 170 AND NEVER REBUILT HERE.  Bench
# carries the committed region pin, the cover Hodge, the quotient action Q, the
# committed reflection r and the committed law form = herm([r Q]_{S,S}).
Bench = b170.Bench
ST = b170.ST

FINAL_NOTE_NAME = (
    "ADMISSIBILITY_DIRAC_KAHLER_CONDITIONAL_SYMMETRIC_POWER_THEOREM_"
    "NOTE_2026-08-23.md"
)
NOTE_PATH = ROOT / "docs" / FINAL_NOTE_NAME
# DECLARED DRAFT FALLBACK, read ONLY when the final path is absent.  Gate H
# requires the final path, so the fallback never makes a gate pass.
DRAFT_NOTE_PATH = Path(
    "/private/tmp/claude-502/"
    "-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-"
    "gravity-toe-lane-work-427b0b/25068357-42e8-431c-96c9-c149512f0305/"
    "scratchpad/block177_note_draft.md"
)
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"

# THE SINGLE-PARENT PIN.  Block 176 (the complex-structure synthesis) is BOTH
# the stack parent and the content parent, so there are exactly TWO artifact
# pins.
BLOCK176_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_COMPLEX_STRUCTURE_SYNTHESIS_"
    "BOUNDED_THEOREM_NOTE_2026-08-23.md"
)
BLOCK176_RUNNER = (
    "scripts/admissibility_dirac_kahler_complex_structure_synthesis_"
    "2026_08_23.py"
)
PARENT_ARTIFACTS = (BLOCK176_NOTE, BLOCK176_RUNNER)
PARENT_ARTIFACT_BLOBS = (
    "895e4c5b8b6480cea0b171c6d8a336d8c0c0fc68",   # Block 176 note
    "83478366805fd54843edc673dd3230eac5e9ff10",   # Block 176 runner
)

# Deliberately literal: this is the complete audit read surface.  Every entry is
# a WORKTREE-READABLE path at landing time.
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_CONDITIONAL_SYMMETRIC_POWER_THEOREM_NOTE_2026-08-23.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_COMPLEX_STRUCTURE_SYNTHESIS_BOUNDED_THEOREM_NOTE_2026-08-23.md",
    "scripts/admissibility_dirac_kahler_complex_structure_synthesis_2026_08_23.py",
    "scripts/admissibility_dirac_kahler_closure_audit_two_2026_08_21.py",
)

AUDIT_TIMEOUT_SEC = 600
# THE FIVE-PIN AUTHORITY BLOCK, single-line hex literals refreshed by anchored
# sed at landing.  CURRENT_MAIN WAS RE-RESOLVED AT DRAFT TIME.
CURRENT_MAIN = "0e212ee4c66019a9dc8dae204680d7c45a0ae8ab"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
CURRENT_REGISTRY_BLOB = "b93959cca4f7e26c673cdccbe601e50c3cb93daa"
WORKTREE_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
WORKTREE_REGISTRY_BLOB = "f01d3be864f682584d50eede8b3abe6671bb4719"
# This block stacks on the Block 176 tip, so the parent branch is that.
PARENT_REF = ("origin/physics-loop/toe-axiom-closure-block176-"
              "complex-structure-synthesis-20260823")
PARENT_COMMIT = "63b865d02d37f89f5515adaf948e7e39a4392ecf"
# The Block 175 tip: a real ancestor of HEAD that predates Block 176 and
# therefore carries NEITHER Block 176 artifact.  Read ONLY under the stale
# mutation, where the missing blobs are exactly what makes it bite.
STALE_PARENT_COMMIT = "d950324a53b84e320aeb69f59194d705542c054f"
# Block 137's recorded main: a real but superseded authority head.
STALE_MAIN = "2dc8dd9b2778a01454874d19b262569ae19ebc6e"

MUTATIONS = (
    "stale_main_authority",
    "stale_parent_authority",
    "claim_identification_registered",
    "claim_lemma_real_only",
    "claim_identification_derived",
    "break_mismatch_witness",
    "claim_routes_disagree",
    "claim_no_extent_asymmetry",
    "claim_margin_witness_positive",
    "claim_corner_witness_extent_free",
    "claim_covariance_region_psd",
    "claim_vacuum_dial_blind",
    "claim_born_unique_unconditional",
    "drop_provenance_disclosure",
    "drop_n5_fence",
)

MUTATION_GATE = {
    "stale_main_authority": "A",
    "stale_parent_authority": "A",
    "claim_identification_registered": "B",
    "claim_lemma_real_only": "C",
    "claim_identification_derived": "D",
    "break_mismatch_witness": "D",
    "claim_routes_disagree": "E",
    "claim_no_extent_asymmetry": "E",
    "claim_margin_witness_positive": "F",
    "claim_corner_witness_extent_free": "F",
    "claim_covariance_region_psd": "G",
    "claim_vacuum_dial_blind": "G",
    "claim_born_unique_unconditional": "H",
    "drop_provenance_disclosure": "H",
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
        print("GATES " + " ".join(
            f"{key}={'PASS' if value else 'FAIL'}"
            for key, _, value in self.results))

    def finish(self) -> int:
        passed = sum(value for _, _, value in self.results)
        failed = len(self.results) - passed
        print(f"TOTAL: PASS={passed} FAIL={failed}")
        return failed


# ---------------------------------------------------------------------------
# A. authority
# ---------------------------------------------------------------------------
def git_output(*args: str) -> str:
    return subprocess.check_output(
        ("git",) + args, cwd=ROOT, text=True, timeout=AUDIT_TIMEOUT_SEC).strip()


def worktree_blob(path: str) -> str:
    result = subprocess.run(
        ("git", "hash-object", path), cwd=ROOT, text=True,
        capture_output=True, check=False, timeout=AUDIT_TIMEOUT_SEC)
    return result.stdout.strip() if result.returncode == 0 else ""


def commit_blob(commit: str, path: str) -> str:
    result = subprocess.run(
        ("git", "rev-parse", f"{commit}:{path}"), cwd=ROOT, text=True,
        capture_output=True, check=False, timeout=AUDIT_TIMEOUT_SEC)
    return result.stdout.strip() if result.returncode == 0 else ""


def resolve_ref(ref: str) -> str:
    result = subprocess.run(
        ("git", "rev-parse", ref), cwd=ROOT, text=True,
        capture_output=True, check=False, timeout=AUDIT_TIMEOUT_SEC)
    return result.stdout.strip() if result.returncode == 0 else ""


def is_ancestor(ancestor: str, descendant: str) -> bool:
    return subprocess.run(
        ("git", "merge-base", "--is-ancestor", ancestor, descendant),
        cwd=ROOT, check=False, capture_output=True,
        timeout=AUDIT_TIMEOUT_SEC).returncode == 0


def is_hash(value: str) -> bool:
    import re as _re
    return _re.fullmatch(r"[0-9a-f]{40}", value) is not None


def is_placeholder(value: str) -> bool:
    """A DECLARED placeholder is 40 hex characters that are all zero but the
    trailing block tag.  It is hash-SHAPED and is never a resolvable commit."""
    return is_hash(value) and value.startswith("0" * 30)


def raw_note() -> tuple:
    """(text, at_final_path).  The fallback is DECLARED and never hidden."""
    try:
        return NOTE_PATH.read_text(encoding="utf-8"), True
    except OSError:
        pass
    try:
        return DRAFT_NOTE_PATH.read_text(encoding="utf-8"), False
    except OSError:
        return "", False


def normalized_note(text: str) -> str:
    return " ".join(text.lower().split())


def no_float(value: object) -> bool:
    """The committed exactness predicate, reached through the landed chain."""
    return b165.no_float(value)


# THE AST GATE'S READ SURFACE.  It covers EVERY FILE THIS RUNNER READS CODE FROM
# in the runner chain -- this file AND the imported runner modules -- which is
# the Block 176 convention.  IT IS NOT the full transitive module closure; gate
# A reports the residual count outside the surface rather than claiming the
# corpus clean.
def audit_source_paths() -> tuple:
    paths = [Path(__file__).resolve()]
    for module in (b176, b175, b174, b171):
        if module is None:
            continue
        source = getattr(module, "__file__", None)
        if source:
            resolved = Path(source).resolve()
            if resolved not in paths:
                paths.append(resolved)
    return tuple(paths)


def source_float_literals() -> int:
    """AST self-check: NO float literal in ANY file read for code."""
    total = 0
    for path in audit_source_paths():
        tree = ast.parse(path.read_text(encoding="utf-8"))
        total += sum(1 for node in ast.walk(tree)
                     if isinstance(node, ast.Constant)
                     and isinstance(node.value, float))
    return total


BANNED_CALLS = ("nsim" + "plify", "evalf", "Float", "RealNumber")
_NS = BANNED_CALLS[0]


def source_forbidden_calls() -> int:
    """AST self-check: no nsimplify, no evalf, no Float in ANY such file."""
    banned = set(BANNED_CALLS)
    total = 0
    for path in audit_source_paths():
        tree = ast.parse(path.read_text(encoding="utf-8"))
        total += sum(1 for node in ast.walk(tree)
                     if (isinstance(node, ast.Attribute) and node.attr in banned)
                     or (isinstance(node, ast.Name) and node.id in banned))
    return total


def call_sites(text: str) -> int:
    """LIVE CALL SITES, not text mentions."""
    try:
        tree = ast.parse(text)
    except SyntaxError:
        return -1
    return sum(1 for node in ast.walk(tree)
               if (isinstance(node, ast.Attribute) and node.attr == _NS)
               or (isinstance(node, ast.Name) and node.id == _NS))


def residue_report() -> dict:
    """The hygiene residue below the audit surface, COUNTED and never hidden."""
    chain = {}
    for name, module in (("b176", b176), ("b175", b175), ("b174", b174),
                         ("b171", b171), ("b170", b170), ("b165", b165)):
        source = getattr(module, "__file__", None) if module is not None else None
        if source:
            text = Path(source).read_text(encoding="utf-8")
            chain[name] = (text.count(_NS), call_sites(text))
        else:
            chain[name] = (-1, -1)
    return {
        "per_module": chain,
        "call_sites_in_audit_surface": sum(
            chain[name][1] for name in ("b176", "b175", "b174", "b171")),
        "call_sites_below_audit_surface": sum(
            chain[name][1] for name in ("b170", "b165")),
    }


@dataclass(frozen=True)
class AuthorityCertificate:
    fixed_authority: bool
    parent_pin_is_commit: bool
    parent_ref_and_ancestry: bool
    parent_artifact_blobs: bool
    stale_parent_artifact_blobs: bool
    stale_is_real_ancestor: bool
    stale_carries_neither_artifact: bool
    parent_import_landed: bool
    residue: dict


def resolved_parent_commit() -> str:
    if is_hash(PARENT_COMMIT) and not is_placeholder(PARENT_COMMIT):
        return PARENT_COMMIT
    resolved = resolve_ref(PARENT_REF)
    return resolved if is_hash(resolved) else git_output("rev-parse", "HEAD")


def authority_certificate(main_head: str) -> AuthorityCertificate:
    fixed_authority = bool(
        AUDIT_TIMEOUT_SEC == 600
        and main_head == CURRENT_MAIN
        and commit_blob("origin/main", AXIOM_PATH) == CURRENT_AXIOM_BLOB
        and commit_blob("origin/main", REGISTRY_PATH) == CURRENT_REGISTRY_BLOB
        and worktree_blob(AXIOM_PATH) == WORKTREE_AXIOM_BLOB
        and worktree_blob(REGISTRY_PATH) == WORKTREE_REGISTRY_BLOB)
    parent = resolved_parent_commit()
    worktree_blobs = tuple(worktree_blob(path) for path in PARENT_ARTIFACTS)
    committed_blobs = tuple(commit_blob(parent, p) for p in PARENT_ARTIFACTS)
    stale_blobs = tuple(
        commit_blob(STALE_PARENT_COMMIT, p) for p in PARENT_ARTIFACTS)
    return AuthorityCertificate(
        fixed_authority,
        is_hash(PARENT_COMMIT) and not is_placeholder(PARENT_COMMIT),
        bool(is_hash(parent) and is_ancestor(parent, "HEAD")
             and (is_placeholder(PARENT_COMMIT)
                  or resolve_ref(PARENT_REF) == PARENT_COMMIT)),
        bool(len(committed_blobs) == len(PARENT_ARTIFACTS) == 2
             and all(is_hash(v) for v in committed_blobs)
             and committed_blobs == worktree_blobs
             and committed_blobs == PARENT_ARTIFACT_BLOBS),
        # THE STALE LEG.  At the Block 175 tip NEITHER Block 176 artifact
        # exists, so this is False and the stale mutation fails gate A.
        bool(all(is_hash(v) for v in stale_blobs)
             and stale_blobs == worktree_blobs),
        is_ancestor(STALE_PARENT_COMMIT, "HEAD"),
        not any(is_hash(v) for v in stale_blobs),
        PARENT_IMPORT_LANDED,
        residue_report())


# ---------------------------------------------------------------------------
# the 177-specific layer
# ---------------------------------------------------------------------------
NUMERALS: list = []


def record(value):
    """Every reported numeral passes through here for the no-float gate."""
    NUMERALS.append(value)
    return value


COVER_EXTENTS = (("8x4", 8, 4), ("12x4", 12, 4))
ON_DIAL = R(1, 4)
REGION_DIAL = Z0
DIALS = (ON_DIAL, REGION_DIAL)
SLICE_SIZE = 8
T_PHYS_SHORT = 4
RUNTIME_BUDGET_SEC = 150
DEEP_RUNTIME_BUDGET_SEC = 600
POOL_TWO_LEADS = 4
HANDOFF_ITEMS = 3

# THE IMPOSED OBJECTS OF THIS BLOCK, declared as a literal so the banner is a
# measured object and not only prose.  NONE of them is registered or adopted.
IMPOSED_OBJECTS = (
    "the symmetric-power grading Sym^n of a one-particle Hermitian kernel, and its permanent Gram rule",
    "the two one-particle kernel CANDIDATES: the action-side herm([r Q]_SS) and the Hermitianized covariance-side herm([r (Q^-1)^T]_SS)",
    "the two temporal dials s_t = 1/4 and s_t = 0 read as transport-on and region",
    "the witness vectors e_0, e_0 - 5 e_4 and e_4 - e_5 in the committed slice basis",
    "the vacuum readout read as a function of det Q, and its factorization det Q = c P(s_t)^4",
    "the committed reflection r, the region pin, the slice index set S and the menu, class map CM-SITE, slot order and record-slice scope, inherited",
)
REGISTERED_OBJECTS = ()
ADOPTED_OBJECTS = ()
# THE NAMED PREMISE.  It is the whole point of this block's honesty: the
# identification of the committed Gaussian's Wick sectors with Sym^n of either
# displayed kernel is STIPULATED, never derived.
NAMED_PREMISES = (
    "THE QUASI-FREE SECTOR IDENTIFICATION: that the committed functional's "
    "graded reflected Gram is the direct sum of Sym^n of one of the two "
    "displayed one-particle kernels.  IT IS A NAMED PREMISE AND NOT A "
    "CONSEQUENCE -- the exact -35233/38760 mismatch is the measurement that "
    "forbids calling it derived -- and B2b is the named successor that would "
    "derive the framework's own committed functional grading",
)
# THE DECISION that belongs to the owner and is NOT taken here.
OWNER_DECISIONS = (
    "THE PREMISE DECISION: whether the quasi-free sector identification is ever "
    "registered, adopted or written into a premise class -- it stays a NAMED "
    "PREMISE here",
)
WITHDRAWN_CLAIMS = (
    "THE UNCONDITIONAL BORN-SELECTION CLAIM: that the Born readout is the "
    "unique positive-with-transport window over readouts.  WITHDRAWN on the "
    "checker's C5 -- positivity plus dial-sensitivity alone does not select "
    "Z Zbar among positive functions; what survives is SECTOR-UNIQUENESS "
    "INSIDE the stipulated graded sum",
    "THE REAL-ONLY LEMMA FORM: the minor determinant written with r^2.  "
    "CORRECTED to |r|^2 on the checker's C2; the sign conclusion survives the "
    "correction unchanged",
)

# ---------------------------------------------------------------------------
# THE EXACT LITERALS.  Every one is recomputed in the measurement pass and
# compared here; none is a certificate the note asserts about itself.
# ---------------------------------------------------------------------------
MISMATCH_WITNESS = R(-35233, 38760)
ACTION_INERTIA = {
    ("8x4", ON_DIAL): (5, 3, 0),
    ("12x4", ON_DIAL): (4, 4, 0),
    ("8x4", REGION_DIAL): (4, 0, 4),
    ("12x4", REGION_DIAL): (4, 0, 4),
}
COVARIANCE_INERTIA = {
    ("8x4", ON_DIAL): (6, 2, 0),
    ("12x4", ON_DIAL): (4, 4, 0),
    ("8x4", REGION_DIAL): (6, 2, 0),
    ("12x4", REGION_DIAL): (4, 4, 0),
}
MINORS_12x4 = (
    R(57, 40), R(3249, 1600), R(185193, 64000), R(10556001, 2560000),
    R(-601692057, 6553600000), R(34296447249, 16777216000000),
    R(-1954897493193, 42949672960000000),
    R(111429157112001, 109951162777600000000),
)
MINORS_8x4 = (
    R(57, 40), R(3249, 1600), R(185193, 64000), R(10556001, 2560000),
    R(-601692057, 6553600000), R(-977791816629, 67108864000000),
    R(59643928534239, 85899345920000000),
    R(-438891635445453, 13743895347200000000),
)
SIGNS_12x4 = (1, 1, 1, 1, -1, 1, -1, 1)
SIGNS_8x4 = (1, 1, 1, 1, -1, -1, 1, -1)
CHANGES_12x4 = 4
CHANGES_8x4 = 3
MARGIN = R(57, 40)
OFF_MARGIN = R(57, 320)
CLEAN_WITNESS_VALUE = R(-57, 160)
CORNER_WITNESS_VALUE = R(-65, 512)
VACUUM_EXPONENT = 4
VACUUM_P = {
    "8x4": (sp.Integer(66447280221259), sp.Integer(-13079847592350)),
    "12x4": (sp.Integer(1993466346364384822133),
             sp.Integer(-744781636638830596050)),
}
# The disjoint spot-check nodes: NOT interpolation nodes, so agreement there is
# an independent confirmation of the factorization rather than a tautology.
SPOT_NODES = (R(-1, 3), R(1, 7), R(5, 2))


# ---------------------------------------------------------------------------
# C. THE SYM^N LEMMA -- direct symbolic permanent construction
# ---------------------------------------------------------------------------
LEM_P = sp.Symbol("p", positive=True)
LEM_QQ = sp.Symbol("qq", positive=True)
LEM_A = sp.Symbol("a", real=True)
LEM_B = sp.Symbol("b", real=True)
LEM_Q = -LEM_QQ                     # the STRICTLY NEGATIVE diagonal entry
LEM_R = LEM_A + sp.I * LEM_B
LEM_RBAR = LEM_A - sp.I * LEM_B
LEM_MOD2 = LEM_A ** 2 + LEM_B ** 2  # |r|^2, the complex correction


def permanent(matrix: sp.MatrixBase) -> sp.Expr:
    """perm(M) = sum over ALL permutations, every sign +1.  Written out rather
    than cited: this is the object the quasi-free Wick contraction produces."""
    n = matrix.rows
    return sp.expand(sum(
        sp.prod([matrix[i, s[i]] for i in range(n)])
        for s in itertools.permutations(range(n))))


def monomial_gram(rows: tuple, cols: tuple) -> sp.Matrix:
    """[<x_i, y_j>] for two length-n words in the letters u and v.

    THE SESQUILINEARITY IS WHERE THE CONJUGATION LIVES: <v,u> = conj(<u,v>),
    which is exactly the checker's C1 point -- no extra entrywise conjugate is
    applied on top of the permanent.
    """
    table = {("u", "u"): LEM_P, ("u", "v"): LEM_R,
             ("v", "u"): LEM_RBAR, ("v", "v"): LEM_Q}
    return sp.Matrix(len(rows), len(cols),
                     lambda i, j: table[(rows[i], cols[j])])


def measure_lemma() -> dict:
    """THE LEMMA, BUILT AND NOT CITED, at n = 2, 3 and 4."""
    orders = (2, 3, 4)
    entries = {}
    closed_form_agrees = {}
    hermitian = {}
    for n in orders:
        word_a = ("u",) * n
        word_b = ("u",) * (n - 1) + ("v",)
        big_a = permanent(monomial_gram(word_a, word_a))
        big_b = permanent(monomial_gram(word_a, word_b))
        big_b_star = permanent(monomial_gram(word_b, word_a))
        big_d = permanent(monomial_gram(word_b, word_b))
        det = sp.expand(big_a * big_d - big_b * big_b_star)
        closed = sp.expand(
            sp.factorial(n) * sp.factorial(n - 1) * LEM_P ** (2 * n - 2)
            * (LEM_P * LEM_Q - LEM_MOD2))
        entries[n] = (big_a, big_b, big_d)
        closed_form_agrees[n] = sp.expand(det - closed) == 0
        # HERMITICITY of the two-monomial block, measured: B* is the conjugate
        # of B, which is what makes the minor a real determinant.
        hermitian[n] = sp.expand(big_b_star - sp.conjugate(big_b)) == 0
    # THE WICK/PERMANENT IDENTITY at n = 2, on a GENERIC complex Hermitian
    # one-particle kernel: G2_(ij),(kl) = G_ik G_jl + G_il G_jk is EXACTLY the
    # permanent of the 2x2 overlap matrix.  Checker C1, rebuilt.
    letters = ("u", "v")
    wick_agrees = True
    wick_hermitian = True
    sym2_basis = (("u", "u"), ("u", "v"), ("v", "v"))
    sym2 = sp.zeros(3, 3)
    for i, left in enumerate(sym2_basis):
        for j, right in enumerate(sym2_basis):
            block = monomial_gram(left, right)
            wick = sp.expand(block[0, 0] * block[1, 1] + block[0, 1] * block[1, 0])
            if sp.expand(permanent(block) - wick) != 0:
                wick_agrees = False
            sym2[i, j] = sp.expand(wick)
    if sp.expand(sym2 - sym2.H) != sp.zeros(3, 3):
        wick_hermitian = False
    # THE SIGN CONCLUSION, as a SYMBOLIC assertion under p > 0 > q: the closed
    # form is n!(n-1)! p^(2n-2) (pq - |r|^2) with pq < 0 and |r|^2 >= 0.
    defect = sp.expand(LEM_P * LEM_Q - LEM_MOD2)
    sign_conclusion = {n: sp.expand(
        sp.factorial(n) * sp.factorial(n - 1) * LEM_P ** (2 * n - 2) * defect
    ).is_negative for n in orders}
    # THE RENORMALIZATION LEG: a positive diagonal congruence D M D multiplies
    # the 2x2 determinant by (d1 d2)^2 > 0 and cannot change its sign.
    d1 = sp.Symbol("d1", positive=True)
    d2 = sp.Symbol("d2", positive=True)
    gen = sp.Matrix([[sp.Symbol("m11", real=True), sp.Symbol("m12")],
                     [sp.conjugate(sp.Symbol("m12")),
                      sp.Symbol("m22", real=True)]])
    scale = sp.diag(d1, d2)
    congruence_factor = sp.expand(
        sp.expand((scale.H * gen * scale).det()) - (d1 * d2) ** 2 * gen.det())
    return {
        "orders": orders,
        "entries": entries,
        "closed_form_agrees": closed_form_agrees,
        "all_closed_form_agree": all(closed_form_agrees.values()),
        "hermitian_block": hermitian,
        "all_hermitian": all(hermitian.values()),
        "wick_equals_permanent": wick_agrees,
        "sym2_hermitian": wick_hermitian,
        "sign_conclusion": sign_conclusion,
        "all_strictly_negative": all(v is True for v in sign_conclusion.values()),
        "defect_is_negative": defect.is_negative is True,
        "modulus_form": sp.expand(LEM_MOD2 - LEM_R * LEM_RBAR) == 0,
        # THE CORRECTION, MEASURED: r^2 and |r|^2 are DIFFERENT objects, so the
        # solve's real-only form is not merely a notation variant.
        "real_form_differs": sp.expand(LEM_R ** 2 - LEM_MOD2) != 0,
        "congruence_factor_defect": congruence_factor,
        "congruence_cannot_change_sign": congruence_factor == 0,
        "letters": letters,
    }


# ---------------------------------------------------------------------------
# D/E/F/G. THE TWO KERNELS at both extents and both dials
# ---------------------------------------------------------------------------
def selected(bench, matrix: sp.MatrixBase) -> sp.Matrix:
    """[r X]_{S,S}: the committed selection, WITHOUT the Hermitianization, so
    the raw non-Hermiticity of the covariance side is measurable."""
    prod = sp.expand(bench.r * matrix)
    rows = bench.rows
    out = sp.zeros(len(rows), len(rows))
    for a, i in enumerate(rows):
        for b, j in enumerate(rows):
            out[a, b] = prod[i, j]
    return sp.expand(out)


def leading_minors(matrix: sp.MatrixBase) -> tuple:
    return tuple(sp.expand(matrix[:k, :k].det())
                 for k in range(1, matrix.rows + 1))


def sign_train(values) -> tuple:
    return tuple(int(sp.sign(v)) for v in values)


def sign_changes(values) -> int:
    """Jacobi's rule: count sign changes in the sequence 1, D_1, ..., D_n."""
    train = (1,) + sign_train(values)
    return sum(1 for a, b in zip(train, train[1:]) if a != b)


def quad(matrix: sp.MatrixBase, vector: sp.Matrix) -> sp.Expr:
    return sp.expand((vector.H * matrix * vector)[0, 0])


def basis_vector(n: int, index: int) -> sp.Matrix:
    return sp.Matrix([ONE if k == index else Z0 for k in range(n)])


def measure_kernels(deep: bool) -> dict:
    """BOTH KERNEL CANDIDATES, rebuilt at both extents and both dials.

    ACTION SIDE:      Bench.form = herm([r Q]_{S,S}) -- what the solve graded.
    COVARIANCE SIDE:  herm([r (Q^-1)^T]_{S,S}) -- what the committed Gaussian's
                      Wick contractions actually see under H1-170b's index order.
    THE DIFFERENCE IS THE BLOCK'S SHARPEST HONEST FACT and it is measured, not
    argued.
    """
    out: dict = {"extents": tuple(name for name, _, _ in COVER_EXTENTS)}
    for name, cover_t, lx in COVER_EXTENTS:
        bench = Bench(f"b177-{name}", cover_t, lx)
        out[(name, "N")] = bench.N
        out[(name, "T_phys")] = bench.T
        out[(name, "lx")] = bench.lx
        out[(name, "rows")] = tuple(bench.rows)
        out[(name, "slice_size")] = len(bench.rows)
        out[(name, "form_shape")] = tuple(bench.form.shape)
        for dial in DIALS:
            env = bench.carrier(st=dial)
            action = sp.expand(bench.form.subs(env))
            action_direct = bench.pair(sp.expand(bench.Q.subs(env)))
            q_numeric = sp.expand(bench.Q.subs(env))
            q_inverse = sp.expand(q_numeric.inv(method="LU"))
            raw_cov = selected(bench, q_inverse.T)
            cov = herm(raw_cov)
            key = (name, dial)
            out[(key, "action")] = action
            out[(key, "action_is_form")] = is_zero(action - action_direct)
            out[(key, "action_hermitian")] = is_zero(action - action.H)
            out[(key, "inverse_residual_zero")] = is_zero(
                sp.expand(q_numeric * q_inverse) - sp.eye(bench.N))
            out[(key, "raw_cov_hermitian")] = is_zero(raw_cov - raw_cov.H)
            out[(key, "cov")] = cov
            out[(key, "cov_hermitian")] = is_zero(cov - cov.H)
            out[(key, "action_inertia_charpoly")] = tuple(
                b165.real_symmetric_inertia(action))
            out[(key, "action_inertia_congruence")] = tuple(
                b170.cong_inertia(action))
            out[(key, "cov_inertia_charpoly")] = tuple(
                b165.real_symmetric_inertia(cov))
            out[(key, "cov_inertia_congruence")] = tuple(
                b170.cong_inertia(cov))
            out[(key, "mismatch_00")] = sp.expand(cov[0, 0] - action[0, 0])
            out[(key, "mismatch_nonzero")] = sp.expand(cov - action) != sp.zeros(
                *action.shape)
            if deep:
                # THE SECOND EXACT ROUTE for the inverse: the landed
                # DomainMatrix instrument, entry for entry against LU.
                second = b171.exact_inv(q_numeric)
                out[(key, "deep_inverse_agrees")] = is_zero(second - q_inverse)
            else:
                out[(key, "deep_inverse_agrees")] = None
    return out


def measure_fixture_legs(kernels: dict) -> dict:
    """THE MINOR TRAINS, THE TWO ROUTES, AND THE REGION SCHUR CONSTRUCTION."""
    out: dict = {}
    routes_agree = True
    for name, _, _ in COVER_EXTENTS:
        for dial in DIALS:
            key = (name, dial)
            if (kernels[(key, "action_inertia_charpoly")]
                    != kernels[(key, "action_inertia_congruence")]):
                routes_agree = False
    out["routes_agree"] = routes_agree
    out["action_inertias"] = {
        (name, dial): kernels[((name, dial), "action_inertia_charpoly")]
        for name, _, _ in COVER_EXTENTS for dial in DIALS}
    out["action_inertias_agree"] = out["action_inertias"] == ACTION_INERTIA
    for name in ("8x4", "12x4"):
        action = kernels[((name, ON_DIAL), "action")]
        minors = leading_minors(action)
        out[(name, "minors")] = minors
        out[(name, "all_nonzero")] = all(m != 0 for m in minors)
        out[(name, "signs")] = sign_train(minors)
        out[(name, "changes")] = sign_changes(minors)
    out["minors_12x4_agree"] = out[("12x4", "minors")] == MINORS_12x4
    out["minors_8x4_agree"] = out[("8x4", "minors")] == MINORS_8x4
    out["signs_12x4_agree"] = out[("12x4", "signs")] == SIGNS_12x4
    out["signs_8x4_agree"] = out[("8x4", "signs")] == SIGNS_8x4
    out["changes_12x4_agree"] = out[("12x4", "changes")] == CHANGES_12x4
    out["changes_8x4_agree"] = out[("8x4", "changes")] == CHANGES_8x4
    # JACOBI CONSISTENCY: the change count IS the negative index.
    out["jacobi_matches_inertia"] = (
        out[("12x4", "changes")] == ACTION_INERTIA[("12x4", ON_DIAL)][1]
        and out[("8x4", "changes")] == ACTION_INERTIA[("8x4", ON_DIAL)][1])
    # THE EXTENT ASYMMETRY, MEASURED rather than asserted.
    out["trains_differ"] = out[("12x4", "signs")] != out[("8x4", "signs")]
    out["changes_differ"] = out[("12x4", "changes")] != out[("8x4", "changes")]
    # THE REGION SCHUR CONSTRUCTION: at s_t = 0 the leading 4x4 block is
    # (57/40) I_4, the coupling block is 0 and the trailing block is 0, so the
    # Schur complement is IDENTICALLY 0_4 and the four null directions are
    # CONSTRUCTED, not inferred from a rank count.
    schur = {}
    nulls = {}
    for name in ("8x4", "12x4"):
        action = kernels[((name, REGION_DIAL), "action")]
        head = action[:4, :4]
        coupling = action[:4, 4:]
        tail = action[4:, 4:]
        complement = sp.expand(tail - coupling.H * head.inv() * coupling)
        schur[name] = {
            "head_is_margin_identity": sp.expand(head - MARGIN * sp.eye(4))
            == sp.zeros(4, 4),
            "coupling_zero": is_zero(coupling),
            "tail_zero": is_zero(tail),
            "complement": complement,
            "complement_zero": is_zero(complement),
            "head_pivots": tuple(sp.expand(head[i, i]) for i in range(4)),
            "head_pivots_positive": all(
                sp.sign(sp.expand(head[i, i])) == 1 for i in range(4)),
        }
        vectors = tuple(basis_vector(action.rows, k) for k in range(4, 8))
        nulls[name] = {
            "count": len(vectors),
            "annihilated": all(
                sp.expand(action * v) == sp.zeros(action.rows, 1)
                for v in vectors),
            "independent": sp.Matrix.hstack(*vectors).rank() == 4,
        }
    out["schur"] = schur
    out["nulls"] = nulls
    out["schur_all_zero"] = all(schur[n]["complement_zero"] for n in schur)
    out["nulls_all_constructed"] = all(
        nulls[n]["annihilated"] and nulls[n]["independent"] and
        nulls[n]["count"] == 4 for n in nulls)
    return out


def measure_witnesses(kernels: dict) -> dict:
    """THE WITNESSES, and the DISPLAYED 12x4 pairing, entry-checked."""
    out: dict = {}
    displayed = sp.zeros(8, 8)
    signs = (1, -1, 1, -1)
    for i in range(4):
        displayed[i, i] = MARGIN
        displayed[i, i + 4] = signs[i] * OFF_MARGIN
        displayed[i + 4, i] = signs[i] * OFF_MARGIN
    out["displayed"] = displayed
    for name in ("8x4", "12x4"):
        action = kernels[((name, ON_DIAL), "action")]
        n = action.rows
        e0 = basis_vector(n, 0)
        clean = basis_vector(n, 0) - 5 * basis_vector(n, 4)
        corner = basis_vector(n, 4) - basis_vector(n, 5)
        out[(name, "positive_witness")] = quad(action, e0)
        out[(name, "clean_witness")] = quad(action, clean)
        out[(name, "corner_witness")] = quad(action, corner)
    out["positive_agrees"] = (out[("12x4", "positive_witness")] == MARGIN
                              and out[("8x4", "positive_witness")] == MARGIN)
    out["clean_agrees"] = out[("12x4", "clean_witness")] == CLEAN_WITNESS_VALUE
    out["clean_negative"] = sp.sign(out[("12x4", "clean_witness")]) == -1
    out["corner_agrees"] = out[("8x4", "corner_witness")] == CORNER_WITNESS_VALUE
    out["corner_negative"] = sp.sign(out[("8x4", "corner_witness")]) == -1
    # THE EXTENT-SPECIFICITY OF THE CORNER WITNESS, MEASURED: at 12x4 the very
    # same vector gives EXACTLY ZERO, because the reflected corner is hollow
    # there.  A witness is a witness at the extent where it was measured.
    out["corner_is_extent_specific"] = (
        out[("12x4", "corner_witness")] == 0
        and out[("8x4", "corner_witness")] != 0)
    out["display_agrees"] = sp.expand(
        kernels[(("12x4", ON_DIAL), "action")] - displayed) == sp.zeros(8, 8)
    # THE MIXED PAIR the lemma needs: one positive and one negative direction on
    # the SAME kernel.
    out["mixed_pair_exists"] = (
        sp.sign(out[("12x4", "positive_witness")]) == 1
        and sp.sign(out[("12x4", "clean_witness")]) == -1
        and sp.sign(out[("8x4", "positive_witness")]) == 1
        and sp.sign(out[("8x4", "corner_witness")]) == -1)
    # THE PROVENANCE DEFECT, declared as a measured object: the solve's own
    # quoted eigendirection value with NO components recorded.
    out["unrecorded_value"] = R(-24656243, 1124404640)
    out["unrecorded_value_negative"] = sp.sign(out["unrecorded_value"]) == -1
    out["provenance_defect_owned"] = True
    return out


def measure_vacuum(deep: bool) -> dict:
    """THE VACUUM LEG: det Q = c P(s_t)^4 SYMBOLICALLY at both extents.

    The determinant is a polynomial in s_t of degree at most N because Q is
    AFFINE in s_t, so exact Lagrange interpolation through N+1 integer nodes is
    an exact determination and not a sample.  It is then FACTORED, and the
    factorization is confirmed at DISJOINT rational nodes that were never
    interpolation nodes.
    """
    out: dict = {}
    for name, cover_t, lx in COVER_EXTENTS:
        bench = Bench(f"b177-vac-{name}", cover_t, lx)
        q_symbolic = sp.expand(bench.Q.subs(bench.carrier()))
        out[(name, "free_symbols")] = tuple(
            str(s) for s in q_symbolic.free_symbols)
        # AFFINE IN THE DIAL, measured: the second derivative vanishes
        # identically, which is what licenses exact interpolation below.
        out[(name, "affine_in_dial")] = sp.expand(
            sp.diff(q_symbolic, ST, 2)) == sp.zeros(bench.N, bench.N)
        nodes = [sp.Integer(k) for k in range(bench.N + 1)]
        values = [sp.expand(sp.Matrix(q_symbolic.subs({ST: node})).det(
            method="berkowitz")) for node in nodes]
        poly = sp.expand(sp.interpolate(list(zip(nodes, values)), ST))
        constant, factors = sp.factor_list(sp.Poly(poly, ST))
        quartic = [base for base, mult in factors if mult == VACUUM_EXPONENT]
        out[(name, "degree")] = sp.degree(sp.Poly(poly, ST))
        out[(name, "det_is_real")] = sp.expand(sp.im(poly)) == 0
        out[(name, "factor_count")] = len(factors)
        out[(name, "exponents")] = tuple(mult for _, mult in factors)
        out[(name, "single_quartic_factor")] = len(quartic) == 1
        out[(name, "constant")] = constant
        if quartic:
            base = quartic[0].as_expr()
            out[(name, "P")] = base
            out[(name, "P0")] = sp.expand(base.subs(ST, Z0))
            out[(name, "P_prime_0")] = sp.expand(sp.diff(base, ST).subs(ST, Z0))
            out[(name, "reconstructs")] = sp.expand(
                poly - constant * base ** VACUUM_EXPONENT) == 0
            # THE DISJOINT SPOT CHECK: nodes that were never interpolated.
            spot = []
            for node in SPOT_NODES:
                direct = sp.expand(sp.Matrix(q_symbolic.subs({ST: node})).det(
                    method="berkowitz"))
                spot.append(sp.expand(
                    direct - constant * base.subs(ST, node) ** VACUUM_EXPONENT)
                    == 0)
            out[(name, "spot_checks")] = tuple(spot)
            out[(name, "spot_all_agree")] = all(spot)
        else:                                              # pragma: no cover
            out[(name, "P")] = Z0
            out[(name, "P0")] = Z0
            out[(name, "P_prime_0")] = Z0
            out[(name, "reconstructs")] = False
            out[(name, "spot_checks")] = ()
            out[(name, "spot_all_agree")] = False
        out[(name, "P_agrees")] = (
            (out[(name, "P0")], out[(name, "P_prime_0")]) == VACUUM_P[name])
        out[(name, "dial_sensitive")] = out[(name, "P_prime_0")] != 0
        out[(name, "det_at_zero_nonzero")] = sp.expand(
            poly.subs(ST, Z0)) != 0
        # THE READOUT ITSELF: |Z|^2 is PROPORTIONAL TO 1/|det Q|^2, positive
        # trivially because it is a modulus of a nonzero complex number.
        out[(name, "readout_positive")] = sp.sign(
            sp.expand(poly.subs(ST, Z0)) ** 2) == 1
        if deep:
            extra = []
            for node in (R(2, 5), R(-3, 7)):
                direct = sp.expand(sp.Matrix(q_symbolic.subs({ST: node})).det(
                    method="berkowitz"))
                extra.append(sp.expand(direct - poly.subs(ST, node)) == 0)
            out[(name, "deep_spot")] = tuple(extra)
        else:
            out[(name, "deep_spot")] = ()
    # THE DIAL'S HONEST SCOPE, declared: H and the region pin are s_t-free and
    # only s_t moves between the two carriers, so it is a fair TEMPORAL dial and
    # NOT a full connection-off dial, because s_x = 3/5 remains.
    out["dial_is_temporal_only"] = True
    out["sx_remains"] = b170.BENCH_SX
    out["global_dial_named"] = "Q_tau = H + tau A, A = Q - H"
    return out


# ---------------------------------------------------------------------------
# the scope-key certificate
# ---------------------------------------------------------------------------
SCOPE_KEYS = (
    # --- N0 ---------------------------------------------------------------
    "convention_banner",
    "convention_hazard_order",
    "convention_collision_named",
    "convention_literal_collision",
    "neither_helper_wrong",
    "imposed_object_banner",
    "nothing_registered",
    "measured_never_registered",
    "sector_identification_named_premise",
    "premise_not_a_consequence",
    "b2b_named",
    "nothing_adopted",
    "owner_bar",
    "proposals_stay_proposals",
    # --- W1 ---------------------------------------------------------------
    "w1",
    "campaign_thesis",
    "parent_block",
    "parent_pr",
    "open_gates_content",
    "graded_sector_theorem",
    "honest_conditional_form",
    # --- N1 ---------------------------------------------------------------
    "sym_n_lemma",
    "permanent_construction",
    "closed_form_det",
    "modulus_correction",
    "orders_two_three_four",
    "strictly_negative_every_n",
    "positive_congruence",
    "renormalization_cannot_change_sign",
    "antilinear_wick_gives_permanent",
    "conjugations_in_sesquilinearity",
    "real_example_superseded",
    # --- N2 ---------------------------------------------------------------
    "object_mismatch",
    "action_side_named",
    "covariance_side_named",
    "mismatch_witness",
    "mismatch_persists",
    "raw_covariance_not_hermitian",
    "checker_discovery",
    "identification_not_derived",
    # --- N3 ---------------------------------------------------------------
    "either_kernel_candidate",
    "covariance_inertia_8x4",
    "covariance_inertia_12x4",
    "covariance_mixed_at_region",
    "covariance_region_equals_on_dial",
    "region_result_is_action_side",
    "action_region_psd",
    # --- N4 ---------------------------------------------------------------
    "two_independent_routes",
    "charpoly_descartes",
    "congruence_schur",
    "schur_complement_zero",
    "null_directions_constructed",
    "jacobi_rule",
    "minors_displayed",
    "sign_train_twelve",
    "sign_train_eight",
    "four_changes",
    "three_changes",
    "extent_asymmetry_real",
    "wrap_class_observation",
    "t_phys_four",
    # --- N5 ---------------------------------------------------------------
    "n5_verbatim",
    # --- N6 ---------------------------------------------------------------
    "positive_witness",
    "clean_witness",
    "clean_witness_vector",
    "margin_constant",
    "displayed_pairing",
    "fifty_seven_family_noted",
    "corner_witness",
    "corner_witness_vector",
    "provenance_defect_disclosed",
    # --- N7 ---------------------------------------------------------------
    "vacuum_factorization",
    "exponent_four",
    "p_zero_eight",
    "p_prime_eight",
    "p_zero_twelve",
    "p_prime_twelve",
    "readout_inverse_modulus",
    "naming_slip_corrected",
    "fair_temporal_dial",
    "not_connection_off",
    "q_tau_named",
    # --- N8 ---------------------------------------------------------------
    "conditional_theorem",
    "every_sector_indefinite",
    "vacuum_positive_and_sensitive",
    "sector_uniqueness_only",
    "born_uniqueness_withdrawn",
    "positivity_plus_sensitivity_insufficient",
    "successor_question",
    "cycle913_caution",
    "non_supply_never_necessity",
    "candidacy_never_nature",
    "worker_profile",
    "supervisor_inline_science",
    "codex_refute_check",
    "two_overclaims_cut",
    "checker_credited",
    "opus_mechanical_only",
    "common_mode",
    "two_extents",
    "not_re_verified",
    "not_continuum",
    "os_no_go",
    "not_a_born_derivation",
    "not_a_fock_construction",
    "no_priority_claim",
    "n1_n8",
    "ast_surface_disclosed",
    "no_float",
    "scope_key_certificate",
    "no_volume_average",
    "rho_guard",
    "zero_retirement",
    "zero_score",
    "zero_e2e",
    "axiom",
    "campaign_cited",
)


def scope_certificate(note_text: str) -> dict:
    note = normalized_note(note_text)
    return {
        # --- N0 ---------------------------------------------------------------
        "convention_banner": "(n_+, n_-, n_0)" in note,
        "convention_hazard_order": "(n_+, n_0, n_-)" in note,
        "convention_collision_named": "congruence_inertia" in note
        and "real_symmetric_inertia" in note,
        "convention_literal_collision": "(4,4,0)" in note,
        "neither_helper_wrong": "neither helper is wrong" in note,
        "imposed_object_banner": "imposed measured object" in note,
        "nothing_registered": "nothing here is registered" in note,
        "measured_never_registered": "measured" in note
        and "never registered" in note,
        "sector_identification_named_premise":
            "the quasi-free sector identification is a named premise" in note,
        "premise_not_a_consequence": "a named premise, not a consequence"
        in note,
        "b2b_named": "b2b" in note,
        "nothing_adopted": "nothing is adopted" in note,
        "owner_bar": "the owner's bar" in note,
        "proposals_stay_proposals": "proposals stay proposals" in note,
        # --- W1 ---------------------------------------------------------------
        "w1": __import__("re").search(r"\bw1\b", note) is not None,
        "campaign_thesis": "the campaign thesis" in note,
        "parent_block": "block 176" in note,
        "parent_pr": "#7330" in note,
        "open_gates_content": "open-gates content" in note,
        "graded_sector_theorem": "the graded-sector theorem" in note,
        "honest_conditional_form": "its honest conditional form" in note,
        # --- N1 ---------------------------------------------------------------
        "sym_n_lemma": "the sym^n lemma" in note,
        "permanent_construction": "direct permanent construction" in note,
        "closed_form_det": "n!(n-1)! p^(2n-2) (pq - |r|^2)" in note,
        "modulus_correction": "the solve's r^2 is corrected to |r|^2" in note,
        "orders_two_three_four": "n = 2, 3, 4" in note,
        "strictly_negative_every_n":
            "strictly negative for every n >= 2" in note,
        "positive_congruence": "a positive congruence" in note,
        "renormalization_cannot_change_sign":
            "cannot change the sign" in note,
        "antilinear_wick_gives_permanent":
            "the complex antilinear wick contraction gives exactly the "
            "permanent" in note,
        "conjugations_in_sesquilinearity":
            "the conjugations sit in the sesquilinearity" in note,
        "real_example_superseded":
            "the solve's real-symmetric example was inadequate evidence and is "
            "superseded" in note,
        # --- N2 ---------------------------------------------------------------
        "object_mismatch": "the object mismatch" in note,
        "action_side_named": "the action-side reflected pairing" in note,
        "covariance_side_named": "the covariance side" in note,
        "mismatch_witness": "-35233/38760" in note,
        "mismatch_persists":
            "persists at both extents and at both dials" in note,
        "raw_covariance_not_hermitian":
            "is not even hermitian on these fixtures" in note,
        "checker_discovery": "the checker's discovery" in note,
        "identification_not_derived":
            "the sector identification is not derived here" in note,
        # --- N3 ---------------------------------------------------------------
        "either_kernel_candidate": "either kernel candidate" in note,
        "covariance_inertia_8x4": "(6,2,0)" in note,
        "covariance_inertia_12x4": "(4,4,0)" in note,
        "covariance_mixed_at_region":
            "on the covariance side the mixture persists even at s_t = 0"
            in note,
        "covariance_region_equals_on_dial":
            "its s_t = 0 inertias equal its s_t = 1/4 ones" in note,
        "region_result_is_action_side":
            "the region result belongs to the action side" in note,
        "action_region_psd": "(4,0,4)" in note,
        # --- N4 ---------------------------------------------------------------
        "two_independent_routes": "two independent exact routes" in note,
        "charpoly_descartes": "charpoly-descartes" in note,
        "congruence_schur": "congruence/schur" in note,
        "schur_complement_zero":
            "the s_t = 0 schur complement is identically 0_4" in note,
        "null_directions_constructed":
            "the four null directions are constructed" in note,
        "jacobi_rule": "jacobi" in note,
        "minors_displayed": "111429157112001/109951162777600000000" in note
        and "-438891635445453/13743895347200000000" in note,
        "sign_train_twelve": "+ + + + - + - +" in note,
        "sign_train_eight": "+ + + + - - + -" in note,
        "four_changes": "four changes" in note,
        "three_changes": "three changes" in note,
        "extent_asymmetry_real": "the extent asymmetry is real" in note,
        "wrap_class_observation": "a wrap-class observation" in note,
        "t_phys_four": "t_phys = 4" in note,
        # --- N5 ---------------------------------------------------------------
        # Raw substring membership makes the printed fence byte-identical to its
        # note occurrence.
        "n5_verbatim": N5_FENCE in note_text,
        # --- N6 ---------------------------------------------------------------
        "positive_witness": "57/40" in note,
        "clean_witness": "-57/160" in note,
        "clean_witness_vector": "e_0 - 5 e_4" in note,
        "margin_constant": "the margin constant" in note,
        "displayed_pairing": "57/320" in note,
        "fifty_seven_family_noted":
            "the 57-family echo is noted and not over-read" in note,
        "corner_witness": "-65/512" in note,
        "corner_witness_vector": "e_4 - e_5" in note,
        "provenance_defect_disclosed":
            "the solve recorded no components for its own witness vector"
            in note,
        # --- N7 ---------------------------------------------------------------
        "vacuum_factorization": "det q = c p(s_t)^4" in note,
        "exponent_four": "the exponent is exactly 4" in note,
        "p_zero_eight": "66447280221259" in note,
        "p_prime_eight": "-13079847592350" in note,
        "p_zero_twelve": "1993466346364384822133" in note,
        "p_prime_twelve": "-744781636638830596050" in note,
        "readout_inverse_modulus": "proportional to 1/|det q|^2" in note,
        "naming_slip_corrected": "the solve's naming slip is corrected" in note,
        "fair_temporal_dial": "a fair temporal transport dial" in note,
        "not_connection_off":
            "not a full connection-off dial, because s_x = 3/5 remains" in note,
        "q_tau_named": "q_tau = h + tau a" in note,
        # --- N8 ---------------------------------------------------------------
        "conditional_theorem": "the conditional symmetric-power theorem" in note,
        "every_sector_indefinite":
            "every n >= 1 sector is indefinite" in note,
        "vacuum_positive_and_sensitive":
            "the vacuum sector is positive and dial-sensitive" in note,
        "sector_uniqueness_only": "sector-uniqueness only" in note,
        "born_uniqueness_withdrawn":
            "the unconditional born-selection claim is withdrawn" in note,
        "positivity_plus_sensitivity_insufficient":
            "positivity plus sensitivity alone does not select z zbar among "
            "positive functions" in note,
        "successor_question": "the successor question" in note,
        "cycle913_caution": "cycle913" in note,
        "non_supply_never_necessity":
            "non-supply within this formalism" in note
            and "never metaphysical necessity" in note,
        "candidacy_never_nature": "candidacy within this formalism" in note
        and "never a claim about nature" in note,
        "worker_profile": "worker profile" in note,
        "supervisor_inline_science": "all solve-side science" in note,
        "codex_refute_check": "codex 5.6-sol xhigh" in note,
        "two_overclaims_cut": "two overclaims were cut" in note,
        "checker_credited": "the checker is credited" in note,
        "opus_mechanical_only": "mechanical drafting only" in note,
        "common_mode": "common-mode" in note,
        "two_extents": "two extents" in note,
        "not_re_verified": "not re-verified" in note,
        "not_continuum": "not a continuum statement" in note,
        "os_no_go": "not an os no-go" in note,
        "not_a_born_derivation": "not a derivation of the born rule" in note,
        "not_a_fock_construction":
            "not a construction of a fock space" in note,
        # NEGATIVE key, inherited from Blocks 164-176.
        "no_priority_claim": ("first positive" not in note
                              and "novel" not in note
                              and "unprecedented" not in note
                              and "for the first time" not in note),
        "n1_n8": all(__import__("re").search(rf"\bn{index}\b", note) is not None
                     for index in range(1, 9)),
        "ast_surface_disclosed": "ast surface" in note,
        "no_float": "no float" in note,
        "scope_key_certificate": "scope-key certificate" in note,
        # NEGATIVE key, inherited from Blocks 164-176.
        "no_volume_average": "volume average" not in note,
        # The LaTeX rho guard: a line-wrapped \rho leaves a stray "ho_" at the
        # start of a line and silently mangles a modulus name.
        "rho_guard": "\nho_" not in note_text,
        "zero_retirement": "zero obligation retirement" in note,
        "zero_score": ("no toe percentage moves" in note
                       or "no toe percentage movement" in note),
        "zero_e2e": "retained-positive end-to-end theory count remains zero"
        in note,
        "axiom": "no axiom amendment is justified" in note,
        "campaign_cited": "campaign_20260823_complex_structure" in note,
    }


N5_FENCE = "N5: per_element: THE TWO BANNERS, FIRST AND WITH TEETH. THE INERTIA CONVENTION: every triple in this note is labelled and read in the (n_+, n_-, n_0) order of the LANDED Block 165 helper real_symmetric_inertia, while the landed b163/b164 helper congruence_inertia returns (n_+, n_0, n_-), measured on identical matrices, so THE LITERAL STRING (4,4,0) MEANS PSD in Block 164's landed fence and FULLY HYPERBOLIC here; NEITHER HELPER IS WRONG and no landed verdict changes. AND THE IMPOSED-OBJECT BANNER: NOTHING HERE IS REGISTERED OR ADOPTED -- the symmetric-power grading, the two one-particle kernel candidates, the two temporal dials, the three witness vectors, the vacuum factorization and the inherited reflection, region pin, slice index set, menu, class map CM-SITE, slot order and record-slice scope are IMPOSED MEASURED OBJECTS OF THIS BLOCK; AND THE QUASI-FREE SECTOR IDENTIFICATION IS A NAMED PREMISE, NOT A CONSEQUENCE -- it is stipulated here, the exact -35233/38760 mismatch is what forbids calling it derived, B2b is the named successor, and NOTHING IS REGISTERED AND NOTHING IS ADOPTED.\nper_site: THE SYM^N LEMMA, COMPLEX-CORRECTED AND BUILT RATHER THAN CITED. On the two symmetric monomials {u^n, u^(n-1) v} the Gram minor is det = n!(n-1)! p^(2n-2) (pq - |r|^2), verified by DIRECT PERMANENT CONSTRUCTION at n = 2, 3, 4 with p = <u,u>, q = <v,v> and r = <u,v>. THE SOLVE'S r^2 IS CORRECTED TO |r|^2 -- the checker's C2 -- and with p > 0 > q the determinant is STRICTLY NEGATIVE FOR EVERY n >= 2, so every symmetric power of a MIXED one-particle kernel is INDEFINITE. Passing from raw monomials to divided or orthonormal symmetric tensors is A POSITIVE CONGRUENCE and CANNOT CHANGE THE SIGN. And the complex scope is settled the other way from the solve's guess: THE COMPLEX ANTILINEAR WICK CONTRACTION GIVES EXACTLY THE PERMANENT, because THE CONJUGATIONS SIT IN THE SESQUILINEARITY, so the solve's real-symmetric example was inadequate evidence and is superseded.\nper_mode: THE OBJECT MISMATCH IS THE CHECKER'S DISCOVERY AND THIS BLOCK'S SHARPEST HONEST FACT. The solve graded THE ACTION-SIDE REFLECTED PAIRING herm([r Q]_SS), but the committed Gaussian's Wick contractions see THE COVARIANCE SIDE herm([r (Q^-1)^T]_SS); the raw covariance selection IS NOT EVEN HERMITIAN ON THESE FIXTURES, and after Hermitianization the (0,0) difference is EXACTLY -35233/38760 at 8x4 with s_t = 0 and PERSISTS AT BOTH EXTENTS AND AT BOTH DIALS. THE SECTOR IDENTIFICATION IS NOT DERIVED HERE: it is A NAMED PREMISE, NOT A CONSEQUENCE, and B2b -- derive the framework's own committed functional grading -- is the named successor question.\nper_block: BOTH KERNELS CARRY THE MIXTURE, WHICH IS WHY THE THEOREM IS WORTH STATING AT ALL. The Hermitianized covariance kernel reads (6,2,0)(n+,n-,n0)[b165] at 8x4 and (4,4,0)(n+,n-,n0)[b165] at 12x4 with s_t = 1/4 -- MIXED, exactly like the action-side (5,3,0)(n+,n-,n0)[b165] and (4,4,0)(n+,n-,n0)[b165] -- so THE SYMMETRIC-POWER INDEFINITENESS FIRES ON EITHER KERNEL CANDIDATE. On the covariance side the mixture persists even at s_t = 0: ITS s_t = 0 INERTIAS EQUAL ITS s_t = 1/4 ONES, stated exactly as measured. THE REGION RESULT BELONGS TO THE ACTION SIDE, where the pairing reads (4,0,4)(n+,n-,n0)[b165] PSD at both extents, and it is NOT a covariance-side statement.\nlattice_wide: THE FIXTURE LEGS, BY TWO ROUTES AND WITH THE NULL SPACE CONSTRUCTED. All four action-side inertias are taken by TWO INDEPENDENT EXACT ROUTES -- charpoly-Descartes and congruence/Schur -- and they agree; at the region THE s_t = 0 SCHUR COMPLEMENT IS IDENTICALLY 0_4 after four positive pivots of 57/40, so THE FOUR NULL DIRECTIONS ARE CONSTRUCTED rather than inferred from a rank count. The Jacobi minor-sign rule applies at 12x4 on eight exactly nonzero leading minors 57/40, 3249/1600, 185193/64000, 10556001/2560000, -601692057/6553600000, 34296447249/16777216000000, -1954897493193/42949672960000000 and 111429157112001/109951162777600000000, signs + + + + - + - +, FOUR CHANGES; the 8x4 train is + + + + - - + - with THREE CHANGES. THE EXTENT ASYMMETRY IS REAL and it is disclosed as A WRAP-CLASS OBSERVATION at T_phys = 4, not smoothed away and not read as a size limit.\nper_scope: THE WITNESSES, THE VACUUM, AND THE DIAL'S HONEST SCOPE. u = e_0 gives 57/40 > 0 at both extents; the checker's CLEAN witness v = e_0 - 5 e_4 gives EXACTLY -57/160 < 0 at 12x4, THE MARGIN CONSTANT AGAIN, since the on-dial 12x4 pairing is exactly [[57/40 I_4, (57/320) diag(1,-1,1,-1)], [same, 0_4]] entry for entry; THE 57-FAMILY ECHO IS NOTED AND NOT OVER-READ. At 8x4 the recorded w = e_4 - e_5 gives -65/512 < 0, and at 12x4 the same vector gives exactly zero, so that witness is extent-specific and is reported as such. THE SOLVE RECORDED NO COMPONENTS FOR ITS OWN WITNESS VECTOR and that provenance defect is OWNED AND DISCLOSED. THE VACUUM LEG IS SYMBOLIC: det Q = c P(s_t)^4 with THE EXPONENT EXACTLY 4, P(0) = 66447280221259 and P'(0) = -13079847592350 at 8x4, P(0) = 1993466346364384822133 and P'(0) = -744781636638830596050 at 12x4, so the readout -- PROPORTIONAL TO 1/|det Q|^2, THE SOLVE'S NAMING SLIP CORRECTED -- is positive trivially and dial-sensitive exactly. s_t is A FAIR TEMPORAL TRANSPORT DIAL and NOT A FULL CONNECTION-OFF DIAL, BECAUSE s_x = 3/5 REMAINS; the cleaner global dial Q_tau = H + tau A is NAMED for successors.\nRESULT: THE CONDITIONAL SYMMETRIC-POWER THEOREM. For any proper quasi-free reflected functional whose one-particle kernel is EITHER CANDIDATE -- the action-side pairing or the Hermitianized covariance -- EVERY n >= 1 SECTOR IS INDEFINITE at the tested dials at both extents, while THE VACUUM SECTOR IS POSITIVE AND DIAL-SENSITIVE. THAT IS SECTOR-UNIQUENESS ONLY, inside the stipulated graded sum. THE UNCONDITIONAL BORN-SELECTION CLAIM IS WITHDRAWN on the checker's C5: POSITIVITY PLUS SENSITIVITY ALONE DOES NOT SELECT Z ZBAR AMONG POSITIVE FUNCTIONS. THE COMMITTED-KERNEL IDENTIFICATION IS B2b, THE SUCCESSOR QUESTION. EVERY NEGATIVE HERE IS NON-SUPPLY WITHIN THIS FORMALISM AND NEVER METAPHYSICAL NECESSITY -- the CYCLE913 CAUTION, CARRIED VERBATIM -- and EVERY POSITIVE HERE IS CANDIDACY WITHIN THIS FORMALISM AND NEVER A CLAIM ABOUT NATURE.\nDECISION_CUT: NOTHING IS REGISTERED AND NOTHING IS ADOPTED. No premise-class change is registered; no landed note is edited; no earlier block is corrected; the quasi-free sector identification stays A NAMED PREMISE and the bar items stay PROPOSALS, and PROPOSALS STAY PROPOSALS. THIS BLOCK'S OWN DEFECTS ARE DISCLOSED: the sector identification is a premise and the -35233/38760 mismatch is why; TWO OVERCLAIMS WERE CUT by the cross-model refute-check and THE CHECKER IS CREDITED for both, for the mismatch discovery and for the clean witness; the solve recorded no components for its own witness vector; it is TWO EXTENTS and no ladder; s_t is a temporal dial only; and the AST surface is this runner plus the imported runner chain and NOT every landed module the chain reaches, with residual sites counted rather than claimed repaired. PROVENANCE: CAMPAIGN_20260823_COMPLEX_STRUCTURE.md sections B2 PROOF SKETCH, B2 SOLVE COMPLETE and B2 CHECKER VERDICTS, with b177_check_findings.md preserved in generator-program-20260821/. HANDOFF: B2b, the committed functional grading; the global dial Q_tau; the interference arm J(a).\nTOE: zero axiom retirement; zero obligation retirement; zero TOE movement; no TOE percentage moves; retained-positive end-to-end theory count remains zero."


def build_claims(mutation: str) -> dict:
    claims: dict = {
        "main_head": CURRENT_MAIN,
        "parent_pin": "resolved",
        "identification_registered": False,
        "lemma_uses_modulus": True,
        "identification_derived": False,
        "mismatch_witness": MISMATCH_WITNESS,
        "routes_agree": True,
        "extent_asymmetry": True,
        "clean_witness_negative": True,
        "corner_witness_extent_specific": True,
        "covariance_region_psd": False,
        "vacuum_dial_sensitive": True,
        "born_unique_unconditional": False,
        "required_scope_keys": SCOPE_KEYS,
    }
    if mutation == "stale_main_authority":
        claims["main_head"] = STALE_MAIN
    elif mutation == "stale_parent_authority":
        claims["parent_pin"] = "stale"
    elif mutation == "claim_identification_registered":
        # THE BANNER DENIED: the named premise asserted REGISTERED, which zero
        # registered and zero adopted objects forbid.
        claims["identification_registered"] = True
    elif mutation == "claim_lemma_real_only":
        # THE COMPLEX CORRECTION DENIED: the minor asserted to carry r^2 rather
        # than |r|^2, which the symbolic permanent construction forbids.
        claims["lemma_uses_modulus"] = False
    elif mutation == "claim_identification_derived":
        # THE PREMISE OVERCLAIMED: the quasi-free sector identification asserted
        # DERIVED, which the exact nonzero kernel mismatch forbids.
        claims["identification_derived"] = True
    elif mutation == "break_mismatch_witness":
        # THE WITNESS BROKEN: a wrong exact rational asserted for the (0,0)
        # difference, which the rebuilt kernels forbid.
        claims["mismatch_witness"] = R(-35233, 38761)
    elif mutation == "claim_routes_disagree":
        # THE TWO ROUTES DENIED: the charpoly and congruence routes asserted to
        # disagree, which four exact agreements forbid.
        claims["routes_agree"] = False
    elif mutation == "claim_no_extent_asymmetry":
        # THE ASYMMETRY DENIED: the two minor-sign trains asserted identical,
        # which + + + + - + - + against + + + + - - + - forbids.
        claims["extent_asymmetry"] = False
    elif mutation == "claim_margin_witness_positive":
        # THE MARGIN WITNESS DENIED: e_0 - 5 e_4 asserted positive, which the
        # exact -57/160 forbids.
        claims["clean_witness_negative"] = False
    elif mutation == "claim_corner_witness_extent_free":
        # THE EXTENT SPECIFICITY DENIED: e_4 - e_5 asserted a witness at BOTH
        # extents, which the exact zero at 12x4 forbids.
        claims["corner_witness_extent_specific"] = False
    elif mutation == "claim_covariance_region_psd":
        # THE COVARIANCE REGION DENIED: the covariance kernel asserted PSD at
        # s_t = 0, which its measured (6,2,0) and (4,4,0) forbid.
        claims["covariance_region_psd"] = True
    elif mutation == "claim_vacuum_dial_blind":
        # THE VACUUM SENSITIVITY DENIED: P'(0) asserted zero, which two exact
        # nonzero integers forbid.
        claims["vacuum_dial_sensitive"] = False
    elif mutation == "claim_born_unique_unconditional":
        # THE WITHDRAWN CLAIM REASSERTED: Born uniqueness over readouts, which
        # gate H's withdrawal certificate and the note's own wording forbid.
        claims["born_unique_unconditional"] = True
    elif mutation == "drop_provenance_disclosure":
        claims["required_scope_keys"] = tuple(
            key for key in SCOPE_KEYS if key != "provenance_defect_disclosed")
    elif mutation == "drop_n5_fence":
        claims["required_scope_keys"] = tuple(
            key for key in SCOPE_KEYS if key != "n5_verbatim")
    return claims


# ---------------------------------------------------------------------------
# gates: pure functions of the measured facts and the claims
# ---------------------------------------------------------------------------
@dataclass(frozen=True)
class Facts:
    deep: bool
    main_head: str
    authority: AuthorityCertificate
    note_at_final_path: bool
    scope: dict
    banners: dict
    lemma: dict
    kernels: dict
    legs: dict
    witnesses: dict
    vacuum: dict
    exact_no_float: bool
    source_files: int
    source_floats: int
    source_forbidden: int


def evaluate_gates(facts: Facts, claims: dict, elapsed_ns: int) -> dict:
    authority = facts.authority
    parent_blobs_ok = (authority.parent_artifact_blobs
                       if claims["parent_pin"] == "resolved"
                       else authority.stale_parent_artifact_blobs)
    gate_a = bool(
        AUDIT_INPUT_PATHS == (
            "docs/ADMISSIBILITY_DIRAC_KAHLER_CONDITIONAL_SYMMETRIC_POWER_THEOREM_NOTE_2026-08-23.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
            "docs/audit/data/axiom_premise_nodes.json",
            "docs/ADMISSIBILITY_DIRAC_KAHLER_COMPLEX_STRUCTURE_SYNTHESIS_BOUNDED_THEOREM_NOTE_2026-08-23.md",
            "scripts/admissibility_dirac_kahler_complex_structure_synthesis_2026_08_23.py",
            "scripts/admissibility_dirac_kahler_closure_audit_two_2026_08_21.py",
        )
        and PARENT_ARTIFACTS == (BLOCK176_NOTE, BLOCK176_RUNNER)
        and len(PARENT_ARTIFACT_BLOBS) == len(PARENT_ARTIFACTS) == 2
        and facts.main_head == claims["main_head"]
        and authority.fixed_authority
        and authority.parent_import_landed
        and authority.parent_pin_is_commit
        and authority.parent_ref_and_ancestry
        and parent_blobs_ok
        # THE STALE PIN: a REAL ancestor of HEAD that carries NEITHER Block 176
        # artifact, which is exactly what makes the stale mutation bite.
        and authority.stale_is_real_ancestor
        and authority.stale_carries_neither_artifact)

    ban = facts.banners
    ker = facts.kernels
    gate_b = bool(
        # THE CONVENTION COLLISION, MEASURED on identical matrices.
        ban["convention"]["pairs"] == EXPECTED_CONVENTION
        and ban["convention"]["landed_psd"] and ban["convention"]["here_psd"]
        and ban["convention"]["orders_differ"]
        # THE IMPOSED-OBJECT BANNER and THE NAMED PREMISE, as measured objects.
        and ban["imposed_objects"] == 6
        and ban["registered_objects"] == 0
        and ban["adopted_objects"] == 0
        and ban["named_premises"] == 1
        and ban["owner_decisions"] == 1
        and ban["withdrawn_claims"] == 2
        and (ban["registered_objects"] == 0 and ban["adopted_objects"] == 0)
        == (not claims["identification_registered"])
        # BOTH BENCH ANCHORS, rebuilt through the LANDED Block 170 machinery.
        and ker[("8x4", "N")] == 16 and ker[("8x4", "T_phys")] == 4
        and ker[("12x4", "N")] == 24 and ker[("12x4", "T_phys")] == 6
        and ker[("8x4", "lx")] == 4 and ker[("12x4", "lx")] == 4
        and ker[("8x4", "slice_size")] == SLICE_SIZE
        and ker[("12x4", "slice_size")] == SLICE_SIZE
        and ker[("8x4", "form_shape")] == (SLICE_SIZE, SLICE_SIZE)
        and ker[("12x4", "form_shape")] == (SLICE_SIZE, SLICE_SIZE)
        and all(ker[((name, dial), "action_is_form")]
                for name, _, _ in COVER_EXTENTS for dial in DIALS)
        and all(ker[((name, dial), "action_hermitian")]
                for name, _, _ in COVER_EXTENTS for dial in DIALS)
        and all(ker[((name, dial), "inverse_residual_zero")]
                for name, _, _ in COVER_EXTENTS for dial in DIALS)
        and facts.exact_no_float
        and facts.source_floats == 0 and facts.source_forbidden == 0
        and facts.source_files >= 2)

    lem = facts.lemma
    gate_c = bool(
        lem["orders"] == (2, 3, 4)
        # THE PERMANENT CONSTRUCTION, at every order, against the closed form.
        and lem["all_closed_form_agree"]
        and all(lem["closed_form_agrees"][n] for n in (2, 3, 4))
        and lem["all_hermitian"]
        # THE WICK IDENTITY: the antilinear contraction IS the permanent, and
        # the resulting Sym^2 block is Hermitian.
        and lem["wick_equals_permanent"] and lem["sym2_hermitian"]
        # THE SIGN CONCLUSION, symbolic and strict.
        and lem["all_strictly_negative"] and lem["defect_is_negative"]
        # THE RENORMALIZATION LEG.
        and lem["congruence_cannot_change_sign"]
        and lem["congruence_factor_defect"] == 0
        # THE CLAIM-BOUND LEG: the minor carries |r|^2 and NOT r^2, and the two
        # are measurably different objects.
        and lem["modulus_form"] and lem["real_form_differs"]
        and lem["modulus_form"] == claims["lemma_uses_modulus"]
        and facts.exact_no_float)

    gate_d = bool(
        # BOTH KERNELS REBUILT, and the raw covariance selection measured
        # NON-Hermitian on these fixtures.
        all(not ker[((name, dial), "raw_cov_hermitian")]
            for name, _, _ in COVER_EXTENTS for dial in DIALS)
        and all(ker[((name, dial), "cov_hermitian")]
                for name, _, _ in COVER_EXTENTS for dial in DIALS)
        # THE EXACT WITNESS at 8x4 with s_t = 0, and the SAME exact rational at
        # 12x4 with s_t = 0.
        and ker[(("8x4", REGION_DIAL), "mismatch_00")] == claims[
            "mismatch_witness"]
        and ker[(("12x4", REGION_DIAL), "mismatch_00")] == MISMATCH_WITNESS
        # PERSISTENCE at the other dial and at both extents.
        and ker[(("8x4", ON_DIAL), "mismatch_00")] != 0
        and ker[(("12x4", ON_DIAL), "mismatch_00")] != 0
        and all(ker[((name, dial), "mismatch_nonzero")]
                for name, _, _ in COVER_EXTENTS for dial in DIALS)
        # THE STATUS: A PREMISE, NEVER A CONSEQUENCE.
        and ban["identification_is_derived"] == claims["identification_derived"]
        and ban["named_premises"] == 1
        and facts.scope["sector_identification_named_premise"]
        and facts.scope["premise_not_a_consequence"]
        and facts.scope["b2b_named"]
        and (all(ker[((name, dial), "deep_inverse_agrees")] is True
                 for name, _, _ in COVER_EXTENTS for dial in DIALS)
             if facts.deep else True)
        and facts.exact_no_float)

    legs = facts.legs
    gate_e = bool(
        # THE FOUR ACTION-SIDE INERTIAS, by BOTH exact routes.
        legs["action_inertias_agree"]
        and legs["routes_agree"] == claims["routes_agree"]
        # THE TWO MINOR TRAINS, exact and all-nonzero.
        and legs[("12x4", "all_nonzero")] and legs[("8x4", "all_nonzero")]
        and legs["minors_12x4_agree"] and legs["minors_8x4_agree"]
        and legs["signs_12x4_agree"] and legs["signs_8x4_agree"]
        and legs["changes_12x4_agree"] and legs["changes_8x4_agree"]
        and legs["jacobi_matches_inertia"]
        # THE REGION SCHUR CONSTRUCTION and THE FOUR NULL DIRECTIONS.
        and legs["schur_all_zero"] and legs["nulls_all_constructed"]
        and all(legs["schur"][name]["head_is_margin_identity"]
                and legs["schur"][name]["head_pivots_positive"]
                and legs["schur"][name]["coupling_zero"]
                and legs["schur"][name]["tail_zero"]
                for name in ("8x4", "12x4"))
        # THE CLAIM-BOUND LEG: the extent asymmetry is REAL.
        and (legs["trains_differ"] and legs["changes_differ"])
        == claims["extent_asymmetry"]
        and facts.scope["extent_asymmetry_real"]
        and facts.scope["wrap_class_observation"]
        and facts.exact_no_float)

    wit = facts.witnesses
    gate_f = bool(
        # THE DISPLAYED 12x4 PAIRING, entry for entry.
        wit["display_agrees"]
        # THE THREE WITNESSES, exact.
        and wit["positive_agrees"] and wit["clean_agrees"] and wit["corner_agrees"]
        and wit["mixed_pair_exists"]
        and wit["unrecorded_value_negative"]
        and wit["provenance_defect_owned"]
        # THE TWO CLAIM-BOUND LEGS.
        and wit["clean_negative"] == claims["clean_witness_negative"]
        and wit["corner_is_extent_specific"]
        == claims["corner_witness_extent_specific"]
        and facts.exact_no_float)

    vac = facts.vacuum
    covariance_psd = any(
        ker[((name, dial), "cov_inertia_charpoly")][1] == 0
        for name, _, _ in COVER_EXTENTS for dial in DIALS)
    gate_g = bool(
        # THE COVARIANCE KERNEL, at BOTH dials and by BOTH routes.
        all(ker[((name, dial), "cov_inertia_charpoly")]
            == COVARIANCE_INERTIA[(name, dial)]
            for name, _, _ in COVER_EXTENTS for dial in DIALS)
        and all(ker[((name, dial), "cov_inertia_charpoly")]
                == ker[((name, dial), "cov_inertia_congruence")]
                for name, _, _ in COVER_EXTENTS for dial in DIALS)
        # THE MIXTURE PERSISTS AT s_t = 0 on the covariance side, and its two
        # dials AGREE -- stated exactly as measured.
        and all(ker[((name, REGION_DIAL), "cov_inertia_charpoly")]
                == ker[((name, ON_DIAL), "cov_inertia_charpoly")]
                for name, _, _ in COVER_EXTENTS)
        # THE VACUUM SYMBOLIC LEG.
        and all(vac[(name, "single_quartic_factor")] for name in ("8x4", "12x4"))
        and all(vac[(name, "reconstructs")] for name in ("8x4", "12x4"))
        and all(vac[(name, "spot_all_agree")] for name in ("8x4", "12x4"))
        and all(vac[(name, "P_agrees")] for name in ("8x4", "12x4"))
        and all(vac[(name, "det_is_real")] for name in ("8x4", "12x4"))
        and all(vac[(name, "det_at_zero_nonzero")] for name in ("8x4", "12x4"))
        and all(vac[(name, "readout_positive")] for name in ("8x4", "12x4"))
        and (all(value is True for name in ("8x4", "12x4")
                 for value in vac[(name, "deep_spot")])
             if facts.deep else True)
        and (all(len(vac[(name, "deep_spot")]) == 2 for name in ("8x4", "12x4"))
             if facts.deep else True)
        # THE TWO CLAIM-BOUND LEGS.
        and covariance_psd == claims["covariance_region_psd"]
        and all(vac[(name, "dial_sensitive")] for name in ("8x4", "12x4"))
        == claims["vacuum_dial_sensitive"]
        and facts.scope["covariance_region_equals_on_dial"]
        and facts.scope["region_result_is_action_side"]
        and facts.exact_no_float)

    required = tuple(claims["required_scope_keys"])
    budget = DEEP_RUNTIME_BUDGET_SEC if facts.deep else RUNTIME_BUDGET_SEC
    gate_h = bool(
        # THE NOTE AT ITS FINAL PATH.  An unlanded draft fails HERE and only
        # here; the scope certificate is still computed from the declared draft
        # fallback so the supervisor can see every key before landing.
        facts.note_at_final_path
        and NOTE_PATH.name == FINAL_NOTE_NAME
        and set(facts.scope) == set(SCOPE_KEYS)
        # THE FULL KEY SET IS REQUIRED, not a subset.  That is what gives the
        # drop mutations their teeth once the note is landed.
        and required == SCOPE_KEYS
        and all(facts.scope[key] for key in required)
        # THE WITHDRAWAL CERTIFICATE: the unconditional Born-selection claim is
        # WITHDRAWN, and asserting it back is refused here.
        and ban["born_unique_unconditional"] == claims[
            "born_unique_unconditional"]
        and ban["withdrawn_claims"] == 2
        and facts.scope["born_uniqueness_withdrawn"]
        and facts.scope["sector_uniqueness_only"]
        and facts.scope["provenance_defect_disclosed"]
        and len(MUTATIONS) == 15
        and len(set(MUTATIONS)) == 15
        and set(MUTATION_GATE) == set(MUTATIONS)
        and set(MUTATION_GATE.values()) == set("ABCDEFGH")
        # THE N5 FENCE: N5-prefixed, 9 to 12 lines, the standard sections.
        and N5_FENCE.startswith("N5: ")
        and 9 <= N5_FENCE.count("\n") + 1 <= 12
        and all(N5_FENCE.count(f"\n{name}:") == 1
                for name in ("per_site", "per_mode", "per_block",
                             "lattice_wide", "per_scope", "RESULT",
                             "DECISION_CUT", "TOE"))
        and POOL_TWO_LEADS == 4
        and HANDOFF_ITEMS == 3
        and elapsed_ns <= budget * 1_000_000_000)

    return {"A": gate_a, "B": gate_b, "C": gate_c, "D": gate_d,
            "E": gate_e, "F": gate_f, "G": gate_g, "H": gate_h}


EXPECTED_CONVENTION = (((4, 4, 0), (4, 0, 4)),
                       ((4, 0, 4), (4, 4, 0)),
                       ((0, 3, 0), (0, 0, 3)))


# ---------------------------------------------------------------------------
# the measurement pass: every gate reads it, no gate feeds it
# ---------------------------------------------------------------------------
def measure(deep: bool) -> Facts:
    note_text, at_final_path = raw_note()
    main_head = resolve_ref("origin/main")
    scope = scope_certificate(note_text)
    lemma = measure_lemma()
    kernels = measure_kernels(deep)
    legs = measure_fixture_legs(kernels)
    witnesses = measure_witnesses(kernels)
    vacuum = measure_vacuum(deep)
    banners = {
        "convention": b176.measure_convention() if b176 is not None else {},
        "imposed_objects": len(IMPOSED_OBJECTS),
        "registered_objects": len(REGISTERED_OBJECTS),
        "adopted_objects": len(ADOPTED_OBJECTS),
        "named_premises": len(NAMED_PREMISES),
        "owner_decisions": len(OWNER_DECISIONS),
        "withdrawn_claims": len(WITHDRAWN_CLAIMS),
        # THE TWO DECLARED STATUS FLAGS, so the mutations bite on a measured
        # object and not on prose.
        "identification_is_derived": False,
        "born_unique_unconditional": False,
    }
    for name, _, _ in COVER_EXTENTS:
        for dial in DIALS:
            record(kernels[((name, dial), "mismatch_00")])
            record(kernels[((name, dial), "action_inertia_charpoly")])
            record(kernels[((name, dial), "cov_inertia_charpoly")])
    for value in legs[("12x4", "minors")] + legs[("8x4", "minors")]:
        record(value)
    for name in ("8x4", "12x4"):
        record(witnesses[(name, "positive_witness")])
        record(witnesses[(name, "clean_witness")])
        record(witnesses[(name, "corner_witness")])
        record(vacuum[(name, "P0")])
        record(vacuum[(name, "P_prime_0")])
    record(witnesses["unrecorded_value"])
    return Facts(
        deep=deep,
        main_head=main_head,
        authority=authority_certificate(main_head),
        note_at_final_path=at_final_path,
        scope=scope,
        banners=banners,
        lemma=lemma,
        kernels=kernels,
        legs=legs,
        witnesses=witnesses,
        vacuum=vacuum,
        exact_no_float=all(no_float(v) for v in NUMERALS),
        source_files=len(audit_source_paths()),
        source_floats=source_float_literals(),
        source_forbidden=source_forbidden_calls(),
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS, default="")
    parser.add_argument(
        "--list-mutations", action="store_true",
        help="print the declared mutation names, one per line, and exit")
    parser.add_argument(
        "--deep", action="store_true",
        help="recompute every quotient-action inverse by a SECOND exact route "
             "-- the landed DomainMatrix instrument against the landed LU route "
             "-- and spot-check the vacuum factorization at two further "
             "disjoint rational nodes; the runtime budget is lengthened")
    arguments = parser.parse_args()
    if arguments.list_mutations:
        for name in MUTATIONS:
            print(name)
        return 0
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
        changed = {k for k in raw_gates if raw_gates[k] != gate_values[k]}
        if changed - {target} or gate_values[target]:
            raise AssertionError("mutation did not fail exactly its own gate")

    ban = facts.banners
    lem, ker = facts.lemma, facts.kernels
    legs, wit, vac = facts.legs, facts.witnesses, facts.vacuum
    res = facts.authority.residue

    print("MEASURED, before any gate is read:")
    print(f"  PARENT IMPORT: the Block 176 runner imported "
          f"{facts.authority.parent_import_landed}; PARENT_COMMIT "
          f"{PARENT_COMMIT} is REAL and PARENT_REF resolves to it. "
          f"CURRENT_MAIN was RE-RESOLVED at draft time to {CURRENT_MAIN}")
    print(f"  THE STALE PIN: {STALE_PARENT_COMMIT[:12]} is a REAL ancestor of "
          f"HEAD {facts.authority.stale_is_real_ancestor} and carries NEITHER "
          f"Block 176 artifact {facts.authority.stale_carries_neither_artifact}"
          f" -- it is the Block 175 tip, which PREDATES both artifacts, and "
          f"that absence is exactly what makes the stale_parent_authority "
          f"mutation bite. AND THE HYGIENE RESIDUE IS COUNTED, NOT HIDDEN, as "
          f"(text mentions, LIVE CALL SITES): {res['per_module']}, which is "
          f"{record(res['call_sites_in_audit_surface'])} live call sites inside "
          f"this runner's AST audit surface and "
          f"{record(res['call_sites_below_audit_surface'])} BELOW it, in landed "
          f"modules the chain reaches transitively. REPORTED, and NEVER claimed "
          f"repaired")
    print(f"  THE NOTE: read at its FINAL PATH {facts.note_at_final_path} -- "
          f"when False this is an UNLANDED DRAFT reading the DECLARED FALLBACK "
          f"{DRAFT_NOTE_PATH.name}, gate H is EXPECTED to fail, and the gate-H "
          f"mutations are UNTESTABLE until the note lands; gates A-G are "
          f"unaffected.  Scope keys satisfied: "
          f"{sum(1 for v in facts.scope.values() if v)} of "
          f"{len(facts.scope)}; unsatisfied "
          f"{tuple(key for key, value in facts.scope.items() if not value)}")
    print(f"  THE INERTIA CONVENTION, FIRST: the landed b163/b164 helper and "
          f"the landed Block 165 helper on IDENTICAL matrices "
          f"{ban['convention'].get('pairs')} -- each pair (b163/b164, this "
          f"note); the region normal form is PSD under both readings and the "
          f"tuple ORDERS DIFFER {ban['convention'].get('orders_differ')}, so "
          f"the literal string (4,4,0) means PSD in Block 164's landed fence "
          f"and FULLY HYPERBOLIC here")
    print(f"  THE IMPOSED-OBJECT BANNER AND THE NAMED PREMISE: "
          f"{record(ban['imposed_objects'])} objects built by this block or its "
          f"parents, {record(ban['registered_objects'])} registered and "
          f"{record(ban['adopted_objects'])} adopted; "
          f"{record(ban['named_premises'])} NAMED PREMISE -- {NAMED_PREMISES} "
          f"-- and {record(ban['owner_decisions'])} decision belongs to the "
          f"OWNER: {OWNER_DECISIONS}. The imposed objects are "
          f"{IMPOSED_OBJECTS}. AND {record(ban['withdrawn_claims'])} CLAIMS OF "
          f"THE SOLVE ARE WITHDRAWN OR CORRECTED BY THE CROSS-MODEL CHECK, "
          f"CARRIED HERE VERBATIM: {WITHDRAWN_CLAIMS}")
    print(f"  THE TWO BENCHES, rebuilt through the LANDED Block 170 machinery: "
          f"8x4 (N = {record(ker[('8x4', 'N')])}, T_phys = "
          f"{record(ker[('8x4', 'T_phys')])}) and 12x4 (N = "
          f"{record(ker[('12x4', 'N')])}, T_phys = "
          f"{record(ker[('12x4', 'T_phys')])}), both reading the slice index "
          f"set {ker[('12x4', 'rows')]} of size "
          f"{record(ker[('12x4', 'slice_size')])}, so BOTH reflected pairings "
          f"are 8x8 and directly comparable")
    print(f"  THE SYM^N LEMMA, BUILT AND NOT CITED: at orders {lem['orders']} "
          f"the direct permanent construction on {{u^n, u^(n-1) v}} gives A = "
          f"n! p^n, B = n! p^(n-1) r and D = (n-1)![p^(n-1) q + (n-1) p^(n-2) "
          f"|r|^2], so det = n!(n-1)! p^(2n-2) (pq - |r|^2) EXACTLY at every "
          f"order {lem['all_closed_form_agree']} with the two-monomial block "
          f"Hermitian {lem['all_hermitian']}. THE COMPLEX ANTILINEAR WICK "
          f"CONTRACTION GIVES EXACTLY THE PERMANENT {lem['wick_equals_permanent']}"
          f" -- the conjugations sit in the sesquilinearity -- and the Sym^2 "
          f"block is Hermitian {lem['sym2_hermitian']}. THE CORRECTION IS "
          f"MEASURED: |r|^2 = r conj(r) {lem['modulus_form']} and r^2 is a "
          f"DIFFERENT object {lem['real_form_differs']}. WITH p > 0 > q THE "
          f"DETERMINANT IS STRICTLY NEGATIVE AT EVERY ORDER "
          f"{lem['all_strictly_negative']}, and a positive diagonal congruence "
          f"multiplies it by (d1 d2)^2 > 0 so it CANNOT CHANGE THE SIGN "
          f"{lem['congruence_cannot_change_sign']}")
    print(f"  THE OBJECT MISMATCH, THE CHECKER'S DISCOVERY: the raw covariance "
          f"selection [r (Q^-1)^T]_SS is NOT Hermitian at any extent or dial "
          f"{tuple(not ker[((n, d), 'raw_cov_hermitian')] for n, _, _ in COVER_EXTENTS for d in DIALS)}"
          f", and after Hermitianization the (0,0) difference against the "
          f"action-side herm([r Q]_SS) is 8x4/s_t=0 "
          f"{ker[(('8x4', REGION_DIAL), 'mismatch_00')]}, 12x4/s_t=0 "
          f"{ker[(('12x4', REGION_DIAL), 'mismatch_00')]}, 8x4/s_t=1/4 "
          f"{ker[(('8x4', ON_DIAL), 'mismatch_00')]} and 12x4/s_t=1/4 "
          f"{ker[(('12x4', ON_DIAL), 'mismatch_00')]} -- EXACTLY -35233/38760 "
          f"at the region at BOTH extents and NONZERO everywhere. THE "
          f"QUASI-FREE SECTOR IDENTIFICATION IS THEREFORE A NAMED PREMISE AND "
          f"NOT A CONSEQUENCE, declared derived = "
          f"{ban['identification_is_derived']}, and B2b is the named successor")
    print(f"  THE FOUR ACTION-SIDE INERTIAS BY TWO INDEPENDENT EXACT ROUTES -- "
          f"charpoly-Descartes and the landed congruence/Schur instrument -- "
          f"agreeing {legs['routes_agree']}: 8x4/s_t=1/4 "
          f"{tri(ker[(('8x4', ON_DIAL), 'action_inertia_charpoly')])}, "
          f"12x4/s_t=1/4 {tri(ker[(('12x4', ON_DIAL), 'action_inertia_charpoly')])}"
          f", 8x4/s_t=0 {tri(ker[(('8x4', REGION_DIAL), 'action_inertia_charpoly')])}"
          f" and 12x4/s_t=0 {tri(ker[(('12x4', REGION_DIAL), 'action_inertia_charpoly')])}"
          f". AT THE REGION THE SCHUR COMPLEMENT IS CONSTRUCTED, NOT INFERRED: "
          f"four positive pivots of {record(MARGIN)} and an exactly zero "
          f"coupling block leave the complement identically 0_4 "
          f"{legs['schur_all_zero']}, and the FOUR NULL DIRECTIONS e_4..e_7 are "
          f"exhibited, annihilated and independent {legs['nulls_all_constructed']}")
    print(f"  THE JACOBI MINOR TRAINS: at 12x4 the eight leading minors are "
          f"{legs[('12x4', 'minors')]} -- all nonzero "
          f"{legs[('12x4', 'all_nonzero')]} -- with signs + + + + - + - + and "
          f"{record(legs[('12x4', 'changes')])} sign changes; at 8x4 they are "
          f"{legs[('8x4', 'minors')]} with signs + + + + - - + - and "
          f"{record(legs[('8x4', 'changes')])} changes. THE CHANGE COUNT IS THE "
          f"NEGATIVE INDEX IN BOTH CASES {legs['jacobi_matches_inertia']}, AND "
          f"THE EXTENT ASYMMETRY IS REAL {legs['trains_differ']} -- a "
          f"WRAP-CLASS OBSERVATION at T_phys = {record(T_PHYS_SHORT)}, "
          f"disclosed and not smoothed")
    print(f"  THE WITNESSES: the on-dial 12x4 pairing is EXACTLY [[57/40 I_4, "
          f"(57/320) diag(1,-1,1,-1)], [same, 0_4]] entry for entry "
          f"{wit['display_agrees']}; u = e_0 gives "
          f"{wit[('12x4', 'positive_witness')]} at 12x4 and "
          f"{wit[('8x4', 'positive_witness')]} at 8x4; the checker's CLEAN "
          f"witness v = e_0 - 5 e_4 gives EXACTLY "
          f"{wit[('12x4', 'clean_witness')]} at 12x4 -- THE MARGIN CONSTANT "
          f"AGAIN, and the 57-family echo is NOTED AND NOT OVER-READ; at 8x4 "
          f"w = e_4 - e_5 gives {wit[('8x4', 'corner_witness')]} while the SAME "
          f"vector gives {wit[('12x4', 'corner_witness')]} at 12x4, so that "
          f"witness is EXTENT-SPECIFIC {wit['corner_is_extent_specific']}. A "
          f"MIXED PAIR EXISTS ON EACH EXTENT {wit['mixed_pair_exists']}, which "
          f"is exactly the lemma's hypothesis. AND THE PROVENANCE DEFECT IS "
          f"OWNED: the solve quoted {wit['unrecorded_value']} with NO "
          f"components recorded for the vector, so that value is not "
          f"reproducible as a claim about any named vector")
    print(f"  THE COVARIANCE KERNEL, ON EITHER DIAL: 8x4/s_t=1/4 "
          f"{tri(ker[(('8x4', ON_DIAL), 'cov_inertia_charpoly')])}, 12x4/s_t=1/4 "
          f"{tri(ker[(('12x4', ON_DIAL), 'cov_inertia_charpoly')])}, 8x4/s_t=0 "
          f"{tri(ker[(('8x4', REGION_DIAL), 'cov_inertia_charpoly')])} and "
          f"12x4/s_t=0 {tri(ker[(('12x4', REGION_DIAL), 'cov_inertia_charpoly')])}"
          f" -- MIXED EVERYWHERE, with the s_t = 0 readings EQUAL to the "
          f"s_t = 1/4 readings, which is the checker's measurement and is NOT "
          f"the region result; THE REGION RESULT BELONGS TO THE ACTION SIDE. "
          f"So the symmetric-power indefiniteness FIRES ON EITHER KERNEL "
          f"CANDIDATE, which is the whole reason the conditional theorem is "
          f"worth stating")
    for name in ("8x4", "12x4"):
        print(f"  THE VACUUM LEG AT {name}: det Q is a degree-"
              f"{record(vac[(name, 'degree')])} polynomial in s_t, real "
              f"{vac[(name, 'det_is_real')]}, and it factors as c P(s_t)^4 with "
              f"a SINGLE factor at exponent {record(VACUUM_EXPONENT)} "
              f"{vac[(name, 'single_quartic_factor')]}, reconstructing exactly "
              f"{vac[(name, 'reconstructs')]} and confirmed at "
              f"{len(vac[(name, 'spot_checks')])} DISJOINT rational nodes that "
              f"were never interpolation nodes {vac[(name, 'spot_all_agree')]}. "
              f"P(0) = {vac[(name, 'P0')]} and P'(0) = "
              f"{vac[(name, 'P_prime_0')]}, so the derivative is EXACTLY "
              f"NONZERO {vac[(name, 'dial_sensitive')]} and the readout -- "
              f"PROPORTIONAL TO 1/|det Q|^2, the solve's naming slip corrected "
              f"-- is positive trivially {vac[(name, 'readout_positive')]} and "
              f"dial-sensitive exactly")
    print(f"  THE DIAL'S HONEST SCOPE: H and the region pin are s_t-free and Q "
          f"is affine in s_t, so s_t is A FAIR TEMPORAL TRANSPORT DIAL "
          f"{vac['dial_is_temporal_only']} and NOT a full connection-off dial, "
          f"because s_x = {record(vac['sx_remains'])} REMAINS. The cleaner "
          f"global dial {vac['global_dial_named']} is NAMED for successors and "
          f"is NOT run here")
    print(f"  EXACTNESS: no float in any measured object "
          f"{facts.exact_no_float} over {record(len(NUMERALS))} numerals; the "
          f"AST scan covers {record(facts.source_files)} FILES -- this runner "
          f"AND the imported runner chain -- and finds "
          f"{record(facts.source_floats)} float literals and "
          f"{record(facts.source_forbidden)} forbidden references. THE AST "
          f"SURFACE IS DISCLOSED AND IS NOT THE FULL TRANSITIVE CLOSURE")
    print(f"  SAMPLING: --deep {facts.deep}; at baseline every quotient-action "
          f"inverse is taken by ONE exact route and the vacuum factorization is "
          f"confirmed at {record(len(SPOT_NODES))} disjoint nodes, while --deep "
          f"recomputes every inverse by the landed DomainMatrix instrument and "
          f"adds two further disjoint vacuum nodes. DEEP INVERSE AGREEMENT "
          f"{tuple(ker[((n, d), 'deep_inverse_agrees')] for n, _, _ in COVER_EXTENTS for d in DIALS)}"
          f"; DEEP VACUUM NODES "
          f"{tuple(vac[(n, 'deep_spot')] for n in ('8x4', '12x4'))} -- None and "
          f"() mean the leg was NOT RUN at this invocation, which is DISCLOSED "
          f"rather than reported as agreement")
    print()

    checks = Checks()
    checks.check(
        "A-authority-and-THE-STALE-PIN-THAT-PREDATES-BOTH-ARTIFACTS",
        "main plus the TWO Block 176 artifacts content-bound -- its note and its runner, which are BOTH the stack parent this block's branch is cut from AND the content parent, since this runner IMPORTS the Block 176 runner and reaches the whole committed chain through Block 176's own import chain, which Block 176's gate A pins rather than this one duplicating it -- and the gate additionally requires that the Block 176 runner ACTUALLY IMPORTED, because every fixture below is built by the LANDED Block 170 Bench reached through it. PARENT_COMMIT IS REAL AND SO ARE BOTH ARTIFACT BLOBS: Block 176 HAS landed, so nothing needs sed at landing, and CURRENT_MAIN was re-resolved at draft time. THE FIVE-PIN AUTHORITY BLOCK binds origin/main's head, the axioms blob and the registry blob at origin/main, and the axioms and registry blobs in the worktree. THE STALE PIN IS THE BLOCK 175 TIP, a REAL ancestor of HEAD that PREDATES Block 176 and therefore carries NEITHER Block 176 artifact, which is exactly what makes the stale_parent_authority mutation bite -- under it the gate looks for the artifact blobs at a commit where they do not exist. THE HYGIENE RESIDUE BELOW THE AUDIT SURFACE IS COUNTED AND REPORTED AND NEVER CLAIMED REPAIRED, as (text mentions, LIVE CALL SITES) per module",
        gate_values["A"])
    checks.check(
        "B-the-two-banners-THE-NAMED-PREMISE-and-both-bench-anchors",
        "THE TWO BANNERS COME BEFORE ANY NUMERAL AND BOTH ARE MEASURED RATHER THAN ASSERTED. THE INERTIA CONVENTION: called on IDENTICAL matrices, b163/b164's congruence_inertia returns (n_+, n_0, n_-) and Block 165's real_symmetric_inertia returns (n_+, n_-, n_0), so the region normal form reads (4,4,0) there and (4,0,4) here; NEITHER HELPER IS WRONG and no landed verdict changes, but THE LITERAL STRING (4,4,0) MEANS PSD IN BLOCK 164'S LANDED FENCE AND FULLY HYPERBOLIC IN THIS NOTE -- which matters here more than anywhere, because this block reports (4,4,0) as a MIXED signature on both kernel candidates at 12x4. THE IMPOSED-OBJECT BANNER: six objects are imposed by this block or its parents -- the symmetric-power grading with its permanent Gram rule, the two one-particle kernel candidates, the two temporal dials, the three witness vectors, the vacuum factorization, and the inherited reflection, region pin, slice index set, menu, class map, slot order and record-slice scope -- and ZERO of them are registered and ZERO adopted. AND THE SHARPEST BANNER IS THE PREMISE ITSELF: THE QUASI-FREE SECTOR IDENTIFICATION IS A NAMED PREMISE AND NOT A CONSEQUENCE, exactly one such premise is declared, ONE decision is the OWNER'S, and TWO claims of the supervisor's own solve are carried here as WITHDRAWN OR CORRECTED by the cross-model check rather than quietly dropped. AND BOTH BENCH ANCHORS ARE MEASURED: at 8x4 the quotient action is 16x16 at T_phys = 4 and at 12x4 it is 24x24 at T_phys = 6, both read on the same eight-element slice index set so both reflected pairings are 8x8 and directly comparable, the substituted Bench.form agrees entry for entry with the pairing rebuilt from the substituted action, every pairing is Hermitian, and every quotient-action inverse has an exactly zero two-sided residual before any covariance kernel is formed. No float enters any measured object and the AST scan covers every file this runner reads code from in the runner chain",
        gate_values["B"])
    checks.check(
        "C-THE-SYM-N-LEMMA-by-DIRECT-SYMBOLIC-PERMANENT-CONSTRUCTION",
        "THE LEMMA IS BUILT, NOT CITED, AND THE COMPLEX CORRECTION IS THE POINT. For a Hermitian one-particle form with p = <u,u>, q = <v,v> and r = <u,v>, the n-particle Gram entries on the two symmetric monomials {u^n, u^(n-1) v} are computed by SUMMING OVER ALL PERMUTATIONS -- the permanent, every sign +1 -- at n = 2, 3 and 4, giving A = n! p^n, B = n! p^(n-1) r and D = (n-1)![p^(n-1) q + (n-1) p^(n-2) |r|^2], hence det = n!(n-1)! p^(2n-2) (pq - |r|^2) EXACTLY at every order tested. THE SOLVE'S r^2 IS CORRECTED TO |r|^2 AND THAT IS NOT A NOTATION VARIANT: the gate measures that |r|^2 = r conj(r) and that r^2 is a DIFFERENT symbolic object, and it is the modulus that the sesquilinear scope requires. THE COMPLEX SCOPE IS SETTLED THE OTHER WAY FROM THE SOLVE'S GUESS: the antilinear Wick contraction G2_(ij),(kl) = G_ik G_jl + G_il G_jk is rebuilt on a generic complex Hermitian kernel and is EXACTLY the permanent, with the resulting Sym^2 block Hermitian, because the conjugations sit in the LEFT SESQUILINEARITY and no extra entrywise conjugate occurs -- so the solve's real-symmetric example was inadequate evidence and it is superseded rather than repaired. THE SIGN CONCLUSION IS SYMBOLIC AND STRICT: with p a positive symbol and q strictly negative, pq < 0 and |r|^2 >= 0 force the determinant strictly negative at every order, so EVERY SYMMETRIC POWER OF A MIXED ONE-PARTICLE KERNEL IS INDEFINITE. AND THE NORMALIZATION LEG IS CLOSED: passing from raw monomials to divided or orthonormal symmetric tensors is a positive diagonal congruence, which multiplies the 2x2 determinant by (d1 d2)^2 > 0 and CANNOT CHANGE THE SIGN, measured symbolically on a generic Hermitian 2x2",
        gate_values["C"])
    checks.check(
        "D-THE-OBJECT-MISMATCH-and-THE-SECTOR-IDENTIFICATION-AS-A-NAMED-PREMISE",
        "THE TWO CANDIDATE KERNELS ARE DIFFERENT MATRICES AND THE DIFFERENCE IS EXACT. The solve graded the ACTION-side reflected pairing Bench.form = herm([r Q]_{S,S}), but the imported quotient-Gaussian machinery defines the covariance as Q^-1, so under its index order the Wick contractions see [r (Q^-1)^T]_{S,S} instead. BOTH ARE REBUILT HERE FROM THE LANDED MACHINERY AT BOTH EXTENTS AND BOTH DIALS. The raw covariance selection is MEASURED NOT EVEN HERMITIAN on any of the four fixtures, so it cannot be a reflected Gram as it stands; and Hermitianizing it does NOT recover the action form -- the (0,0) entry differs by EXACTLY -35233/38760 at 8x4 with s_t = 0, by the SAME exact rational at 12x4 with s_t = 0, and by exactly nonzero rationals at s_t = 1/4 at both extents, with the whole matrix difference nonzero at all four. THE CONSEQUENCE IS STATED AT ITS EXACT STRENGTH AND NOT ONE STEP FURTHER: the identification of the committed functional's Wick sectors with the direct sum of Sym^n of Bench.form -- or of any single displayed kernel -- IS AN ADDED PREMISE AND NOT A CONSEQUENCE OF THE STATED GAUSSIAN MEASURE. THIS BLOCK THEREFORE NAMES IT AS A PREMISE, declares it NOT DERIVED as a measured status flag rather than as prose, and names B2b -- derive the framework's own committed functional grading -- as the successor question. THAT MISMATCH IS THE INDEPENDENT CHECKER'S DISCOVERY, IT IS THE REASON THIS BLOCK'S THEOREM IS CONDITIONAL, AND IT IS CARRIED HERE AS THE SPINE RATHER THAN AS A FOOTNOTE",
        gate_values["D"])
    checks.check(
        "E-THE-FOUR-INERTIAS-BY-BOTH-ROUTES-the-TWO-MINOR-TRAINS-and-THE-CONSTRUCTED-NULL-SPACE",
        "EVERY ACTION-SIDE INERTIA IS TAKEN TWICE, BY TWO INSTRUMENTS THAT SHARE NO CODE PATH. The landed Block 165 route is Descartes-on-charpoly; the landed Block 170 route is exact Hermitian congruence with Schur complements and a hollow-remainder repair. They agree on all four: 8x4 with s_t = 1/4 at (5,3,0)(n+,n-,n0)[b165], 12x4 with s_t = 1/4 at (4,4,0)(n+,n-,n0)[b165], and both extents at s_t = 0 at (4,0,4)(n+,n-,n0)[b165]. AT THE REGION THE NULL SPACE IS CONSTRUCTED AND NOT INFERRED: the leading 4x4 block is exactly (57/40) I_4 with four positive pivots, the coupling block is exactly zero, the trailing block is exactly zero, so the Schur complement is IDENTICALLY 0_4 and the four standard directions e_4, e_5, e_6, e_7 are exhibited, verified annihilated by the pairing and verified independent. THE JACOBI MINOR-SIGN RULE IS APPLIED WHERE IT IS LEGAL: at 12x4 with s_t = 1/4 all eight leading minors are exactly nonzero -- 57/40, 3249/1600, 185193/64000, 10556001/2560000, -601692057/6553600000, 34296447249/16777216000000, -1954897493193/42949672960000000, 111429157112001/109951162777600000000 -- their signs are + + + + - + - +, and including the empty minor there are exactly FOUR changes, which is the negative index the charpoly route reports. At 8x4 the train is + + + + - - + - with THREE changes, again matching. THE EXTENT ASYMMETRY IS REAL ON THESE FIXTURES AND IT IS DISCLOSED AS A WRAP-CLASS OBSERVATION AT T_phys = 4 rather than explained: at the short extent the wrap fills structure the long extent leaves hollow, and this block measures that difference and does not resolve it",
        gate_values["E"])
    checks.check(
        "F-THE-WITNESSES-and-THE-DISPLAYED-PAIRING-with-THE-PROVENANCE-DEFECT-OWNED",
        "THE MIXED PAIR THE LEMMA NEEDS IS EXHIBITED AT BOTH EXTENTS BY NAMED VECTORS. At 12x4 with s_t = 1/4 the reflected pairing is EXACTLY [[57/40 I_4, (57/320) diag(1,-1,1,-1)], [same, 0_4]] -- checked entry for entry against a rebuilt literal, not eyeballed -- so u = e_0 gives u^dag G u = 57/40 > 0 and the checker's CLEAN witness v = e_0 - 5 e_4 gives v^dag G v = -57/160 < 0, which is THE MARGIN CONSTANT AGAIN. THE 57-FAMILY ECHO IS NOTED AND NOT OVER-READ: the same numeral recurring in the diagonal, the coupling and the witness is a structural remark about this pairing at this dial and is used as evidence for nothing. At 8x4 the recorded w = e_4 - e_5 gives -65/512 < 0, and the gate MEASURES that the very same vector gives EXACTLY ZERO at 12x4, because the reflected corner is hollow there -- so that witness is EXTENT-SPECIFIC and is reported as such rather than quoted as if it travelled. AND THE PROVENANCE DEFECT IS OWNED IN THE GATE ITSELF: the supervisor's solve quoted -24656243/1124404640 for a rationalized eigendirection and RECORDED NO COMPONENTS FOR THAT VECTOR, so the number is not reproducible as a claim about any named vector; the value is attainable, the checker exhibited a vector that attains it, but the solve's own record was defective and this block says so instead of letting the numeral stand",
        gate_values["F"])
    checks.check(
        "G-THE-COVARIANCE-KERNEL-ON-EITHER-DIAL-and-THE-VACUUM-SYMBOLIC-LEG",
        "THE ROBUSTNESS LEG IS WHAT MAKES A CONDITIONAL THEOREM WORTH STATING. The Hermitianized covariance kernel is not the action form, but it is ALSO MIXED: (6,2,0)(n+,n-,n0)[b165] at 8x4 and (4,4,0)(n+,n-,n0)[b165] at 12x4 with s_t = 1/4, by BOTH exact inertia routes. SO THE SYMMETRIC-POWER INDEFINITENESS FIRES ON EITHER KERNEL CANDIDATE and the theorem does not depend on which side the framework's own grading eventually picks. ON THE COVARIANCE SIDE THE MIXTURE PERSISTS EVEN AT s_t = 0: the gate MEASURES that its s_t = 0 inertias EQUAL its s_t = 1/4 inertias at both extents, and that is stated exactly as measured and NOT as the region result -- the (4,0,4) PSD region reading belongs to the ACTION side and this gate keeps the two apart. THE VACUUM LEG IS SYMBOLIC AND EXACT. Because Q is affine in s_t, det Q is a polynomial in s_t of degree at most N, so exact interpolation through N+1 integer nodes DETERMINES it rather than samples it; it is real, it factors as c P(s_t)^4 with a SINGLE base at exponent exactly 4, it reconstructs exactly, and the factorization is confirmed at three DISJOINT rational nodes that were never interpolation nodes. P(0) = 66447280221259 and P'(0) = -13079847592350 at 8x4; P(0) = 1993466346364384822133 and P'(0) = -744781636638830596050 at 12x4. THE DERIVATIVE IS EXACTLY NONZERO AT BOTH EXTENTS, so the vacuum readout -- PROPORTIONAL TO 1/|det Q|^2, the solve's naming slip CORRECTED -- is positive trivially, being a modulus of a nonzero complex number, and dial-sensitive exactly. AND THE DIAL'S SCOPE IS DECLARED HONESTLY: the Hodge operator and the region pin are s_t-free and only s_t moves between the two carriers, so s_t is a FAIR TEMPORAL TRANSPORT DIAL, but it is NOT a full connection-off dial because s_x = 3/5 remains; the cleaner global dial Q_tau = H + tau A with A = Q - H is NAMED for successors and is not run here",
        gate_values["G"])
    checks.check(
        "H-note-scope-THE-WITHDRAWALS-the-caution-and-the-N5-fence",
        "THE NOTE SITS AT ITS FINAL PATH AND SATISFIES EVERY REQUIRED SCOPE KEY, the required set is THE FULL KEY SET and not a subset -- which is what gives the two drop mutations their teeth once the note is landed -- the N5 fence is an N5-prefixed literal with nine labelled sections that appears BYTE-IDENTICALLY in the note, and the mutation battery is fifteen members mapped one-per-gate across A through H. THE THEOREM THIS GATE CERTIFIES IS THE CONDITIONAL ONE AND NOTHING WIDER: for any proper quasi-free reflected functional whose one-particle kernel is EITHER displayed candidate, every n >= 1 sector is indefinite at the tested dials at both extents while the vacuum sector is positive and dial-sensitive. THAT IS SECTOR-UNIQUENESS ONLY, INSIDE THE STIPULATED GRADED SUM. THE UNCONDITIONAL BORN-SELECTION CLAIM IS WITHDRAWN AND THE WITHDRAWAL IS GATED ON A MEASURED FLAG, NOT ON PROSE: positivity plus dial-sensitivity alone does not select Z Zbar among positive functions, and reasserting the unconditional claim fails this gate. TWO CLAIMS OF THE SUPERVISOR'S OWN SOLVE ARE CARRIED HERE AS WITHDRAWN OR CORRECTED -- the Born-selection wording and the real-only lemma form -- and THE CROSS-MODEL CHECKER IS CREDITED for both cuts, for discovering the object mismatch and for supplying the clean witness. The worker profile is disclosed in full: ALL SOLVE-SIDE SCIENCE by the supervising frontier model INLINE, per the owner's standing directive; the REFUTE-SPEC'D adversarial check by a codex 5.6-sol xhigh worker, cross-model, whose corrections OVERRIDE the solve everywhere they collide; OPUS MECHANICAL DRAFTING ONLY; and supervisor review and landing -- with common-mode risk reduced and NOT eliminated. The scope is TWO EXTENTS and no wider, and it is NOT a continuum statement, NOT an OS no-go, NOT a derivation of the Born rule and NOT a construction of a Fock space; and the disclosures are complete, THIS BLOCK'S OWN DEFECTS INCLUDED -- the sector identification is a premise, the solve's witness provenance was defective, s_t is a temporal dial only, the extent asymmetry is measured and unresolved -- alongside NO FLOAT anywhere, the not-re-verified list, N1 through N8, the W1 wall, the scope-key certificate, the LaTeX rho guard, the pool-2 leads, the three handoff items, zero axiom retirement, zero obligation retirement, no TOE percentage movement, a retained-positive end-to-end theory count that remains zero, and NO priority or originality wording anywhere in the note",
        gate_values["H"])
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
