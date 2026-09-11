#!/usr/bin/env python3
"""Corrected Block 212 finite joint-pin and alphabet diagnostics.

This runner evaluates one fixed exact-rational 12 x 4 cover through the
reviewed released7753 helper.  It retains finite profile, residual, rank, and
fixed-coordinate projection facts.  It does not adopt the historical parent
theorems, a probability or measurement interpretation, a universal
dependency-order theorem, a classical no-go, dynamics, continuum physics, or
gravity.

The four corrections are explicit in the checks and note: (1) the 5 x 16
system is consistent because rank(A) equals rank([A|b]), not because it is
underdetermined; (2) ratio comparisons use exact l1 norms, with component
magnitude counts reported separately; (3) A.T A is invertible at the 25 x 4
rung, while the pivot-basis Gram C.T C is invertible at every rung; and (4)
two proposed factorization orders differing on this fixture does not imply a
universal dependency-order result.

The historical cache reported about 51.83 seconds for the 45-environment exact
calculation.  Run this source only through the established bounded cache
wrapper after the literal input hashes are verified.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import sys
import time
from dataclasses import dataclass
from pathlib import Path

import sympy as sp
from sympy.polys.domains import QQ_I
from sympy.polys.matrices import DomainMatrix

# THE EXACT INTEGERS IN THIS BLOCK ARE LARGE: the two-pin residual components
# carry numerators above fourteen hundred digits and the refutation minors are
# larger still.  CPython's default decimal-conversion limit is 4300 digits and
# SymPy reaches for str() on its internal error paths, so the limit is raised
# once, here, deterministically.  This is an INTEGER setting; it converts
# nothing, rounds nothing and is not a float call site.
sys.set_int_max_str_digits(200000)

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

# The sole local machinery import is the reviewed, bounded fixture extraction.
# Alias it as b171 only to preserve the historical measurement function names;
# the old 42-module closure is neither imported nor treated as authority.
try:
    import admissibility_dirac_kahler_released7753_fixture_2026_09_10 as b171
    FIXTURE_IMPORT_READY = True
except ModuleNotFoundError:  # pragma: no cover
    b171 = None
    FIXTURE_IMPORT_READY = False

FINAL_NOTE_NAME = (
    "ADMISSIBILITY_DIRAC_KAHLER_JOINT_PIN_ORDER_EXTENDED_ALPHABET_"
    "BOUNDED_THEOREM_NOTE_2026-08-27.md"
)
NOTE_PATH = ROOT / "docs" / FINAL_NOTE_NAME
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"
HELPER_PATH = (
    "scripts/admissibility_dirac_kahler_released7753_fixture_2026_09_10.py"
)
BLOCK105_PATH = (
    "scripts/admissibility_dirac_kahler_shifted_origin_frame_gauge_"
    "nonuniform_hodge_overlap_2026_08_14.py"
)
LEDGER_PATH = (
    ".claude/science/physics-loops/toe-axiom-closure-block212-"
    "joint-pin-order-extended-alphabet-20260827/NO_GO_LEDGER.md"
)

# Complete literal runtime/citation read surface.  The note is read for the N5
# fence; the helper and current Block 105 supply the finite construction; the
# axiom and registry files are context boundaries only and supply no premise.
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_JOINT_PIN_ORDER_EXTENDED_ALPHABET_BOUNDED_THEOREM_NOTE_2026-08-27.md",
    "scripts/admissibility_dirac_kahler_released7753_fixture_2026_09_10.py",
    "scripts/admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_2026_08_14.py",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
)
SELF_NOTE_INPUT = AUDIT_INPUT_PATHS[0]

# Actual reviewed bytes.  Commit ancestry is historical provenance only.
INPUT_SHA256 = {
    "docs/ADMISSIBILITY_DIRAC_KAHLER_JOINT_PIN_ORDER_EXTENDED_ALPHABET_BOUNDED_THEOREM_NOTE_2026-08-27.md": "e92a3ebb5ab90db11add8087193f142544f8b04e096705432f61c38ea64d0d04",
    "scripts/admissibility_dirac_kahler_released7753_fixture_2026_09_10.py": "91f85c476739e95e4b982861285872b467597592f88838f21b5f990a0c2c1c6b",
    "scripts/admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_2026_08_14.py": "5499cc2c1a75f19e07b717aeb6c9ef7779c45e1c5757d84701c5d88ca92bf445",
    "docs/MINIMAL_AXIOMS_2026-06-29.md": "93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753",
    "docs/audit/data/axiom_premise_nodes.json": "615f13aaa70e82d50cdf1a8aa479eb40d6ce70a3bb7b152ac63fd88bee341f37",
}
SOURCE_BASE_COMMIT = "1157173587fde42555d36659954e71c544e23312"
AUDIT_TIMEOUT_SEC = 120
NOTE_SOURCE_REQUIRED = "final"

# The first two names are preserved legacy wiring-control IDs.  They mutate
# expected hash claims after measurement; they are not evidence that a live
# file was tampered with or that a moving branch ref was consulted.
MUTATIONS = (
    "stale_main_authority",
    "stale_parent_authority",
    "claim_objects_registered",
    "claim_gravity_supplied",
    "claim_joint_is_measurement",
    "claim_order_is_quantum_signature",
    "claim_extended_alphabet_complete",
    "claim_classical_no_go",
    "claim_readings_licensed",
    "break_joint_instrument",
    "break_joint_normalisation",
    "break_joint_nonnegativity",
    "break_two_pin_identity",
    "break_compounding",
    "break_order_dependence",
    "break_structural_commutation",
    "break_order_residual_split",
    "break_single_readout_solvability",
    "break_extended_alphabet",
    "break_extended_stack_inconsistency",
    "break_exclusion_series",
    "break_conjecture_refutation",
    "claim_reading_identified",
    "claim_noncommutativity_is_nonclassical",
    "claim_order_axis_is_new",
    "claim_alphabet_exhaustive",
    "claim_rank_law",
    "claim_bound_violated",
    "break_instance_scope",
    "drop_n5_fence",
    "break_nsimplify_absence",
    "break_float_absence",
)

MUTATION_GATE = {
    "stale_main_authority": "A",
    "stale_parent_authority": "A",
    "claim_objects_registered": "B",
    "claim_gravity_supplied": "B",
    "claim_joint_is_measurement": "B",
    "claim_order_is_quantum_signature": "B",
    "claim_extended_alphabet_complete": "B",
    "claim_classical_no_go": "B",
    "claim_readings_licensed": "B",
    "break_joint_instrument": "C",
    "break_joint_normalisation": "C",
    "break_joint_nonnegativity": "C",
    "break_two_pin_identity": "C",
    "break_compounding": "C",
    "break_order_dependence": "D",
    "break_structural_commutation": "D",
    "break_order_residual_split": "D",
    "break_single_readout_solvability": "D",
    "break_extended_alphabet": "E",
    "break_extended_stack_inconsistency": "E",
    "break_exclusion_series": "E",
    "break_conjecture_refutation": "E",
    "claim_reading_identified": "F",
    "claim_noncommutativity_is_nonclassical": "F",
    "claim_order_axis_is_new": "F",
    "claim_alphabet_exhaustive": "F",
    "claim_rank_law": "F",
    "claim_bound_violated": "F",
    "break_instance_scope": "F",
    "drop_n5_fence": "G",
    "break_nsimplify_absence": "G",
    "break_float_absence": "G",
}
MUTATED_FAMILIES = "ABCDEFG"


class Checks:
    def __init__(self) -> None:
        self.results: list = []

    def check(self, key: str, statement: str, condition: object) -> None:
        self.results.append((key, statement, bool(condition)))

    def families(self) -> dict:
        summary: dict = {}
        for key, _, value in self.results:
            family = key.split("-", 1)[0]
            summary[family] = summary.get(family, True) and value
        return summary

    def report(self) -> None:
        for key, statement, value in self.results:
            print(f"[{'PASS' if value else 'FAIL'}] {key}: {statement}")
        print("GATES " + " ".join(
            f"{family}={'PASS' if value else 'FAIL'}"
            for family, value in self.families().items()))

    def finish(self) -> int:
        passed = sum(value for _, _, value in self.results)
        failed = len(self.results) - passed
        print(f"TOTAL: PASS={passed} FAIL={failed}")
        return failed


# ---------------------------------------------------------------------------
# A. immutable input-byte closure (no moving-ref or ancestry gate)
# ---------------------------------------------------------------------------
def sha256_path(path: Path) -> str:
    try:
        return hashlib.sha256(path.read_bytes()).hexdigest()
    except OSError:
        return ""


def audit_inputs_readable() -> tuple:
    missing = tuple(path for path in AUDIT_INPUT_PATHS if not (ROOT / path).is_file())
    return len(AUDIT_INPUT_PATHS) - len(missing), missing


def note_text() -> tuple:
    if NOTE_PATH.is_file():
        return NOTE_PATH.read_text(encoding="utf-8"), "final"
    return "", "absent"


@dataclass(frozen=True)
class AuthorityCertificate:
    all_inputs_content_bound: bool
    note_content_bound: bool
    helper_content_bound: bool
    supplier_content_bound: bool
    context_inputs_content_bound: bool
    fixture_import_ready: bool
    helper_supplier_certificate: bool
    inputs_readable: int
    inputs_missing: tuple


def authority_certificate() -> AuthorityCertificate:
    actual = {path: sha256_path(ROOT / path) for path in AUDIT_INPUT_PATHS}
    readable, missing = audit_inputs_readable()
    return AuthorityCertificate(
        actual == INPUT_SHA256,
        actual.get(SELF_NOTE_INPUT, "") == INPUT_SHA256[SELF_NOTE_INPUT],
        actual.get(HELPER_PATH, "") == INPUT_SHA256[HELPER_PATH],
        actual.get(BLOCK105_PATH, "") == INPUT_SHA256[BLOCK105_PATH],
        actual.get(AXIOM_PATH, "") == INPUT_SHA256[AXIOM_PATH]
        and actual.get(REGISTRY_PATH, "") == INPUT_SHA256[REGISTRY_PATH],
        FIXTURE_IMPORT_READY,
        bool(FIXTURE_IMPORT_READY and b171.supplier_certificate()),
        readable,
        missing,
    )


# ---------------------------------------------------------------------------
# B. the imposed objects and the NOT-CLAIMED keys, as measured literals
# ---------------------------------------------------------------------------
IMPOSED_OBJECTS = (
    "THE JOINT-PIN FINITE INSTRUMENT, HISTORICALLY PROPOSED IN BLOCK 210 AND REBUILT HERE: IT IS A DOUBLE SUBSTITUTION AND NOT A JOINT MEASUREMENT: the sixteen doubly-pinned environments carrying records at BOTH (2, x) and (4, y) at class value 0, written into the extracted finite carrier field by the bounded helper's record substitution and read out through the bounded helper's Env.profile at level 5, together with the eight single class-0 pins at slots 2 and 4 and the record-free base",
    "THE TWO PROPOSED JOINT-WEIGHT FACTORIZATIONS AND THE TWO-PIN MIXTURE IDENTITY: w_fwd(x, y) = w_2(x) * P(y at 4 | pin x at 2) and w_rev(x, y) = w_4(y) * P(x at 2 | pin y at 4), each an exact nonnegative sixteen-entry array summing to exactly one; reversing structural dictionary insertion changes zero actions; and the residual P0 - sum_{x,y} w(x, y) P_{x,y} is taken at read level 5 under the PROPOSED W9 formation-weight reading",
    "THE SINGLE-PIN COMPARISON CENSUS, RE-MEASURED FROM THE SAME CACHE AND NOT CITED: the three single-pin mixture residuals at slots 2, 3 and 4, of which the mid-slot 3 one is the historical cache's four-outcome residual, together with the exact componentwise and l1-norm comparisons against both two-pin residuals",
    "THE TWENTY-OUTCOME EXTENDED ALPHABET AND ITS SIX-CONTEXT STACK: the twenty outcomes (x, k) for x = 0..3 and k in {0, 1/5, -1/5, 2/5, -2/5} at the mid slot 3, one column per outcome and one row per readout component per (family, level) context over (W9, W2) x (5, 4, 2) plus one affine normalisation row, read as the 25 x 20 stack and as the three-rung exclusion series at 4, 12 and 20 outcomes from the SAME twenty environments",
    "THE REFUTATION WITNESS FOR THE DECLARED REPRESENTATIVE-LEVEL CONTRADICTION CONJECTURE: the fixed-row-coordinate Euclidean/Riesz residual r_n = b - proj_col(A_n)(b) at each rung -- exact but not invariant under arbitrary row reparameterization -- together with the three left-cokernel dimensions and exact pairwise non-proportionality certificates",
    "THE REVIEWED EXTRACTED 12x4 BENCH READ THROUGH THE BOUNDED HELPER'S Site AND Env CLASSES: Site('12x4', 12, 4) with N = 24, T = 6, c = 1, tstar = 5 and lx = 4, the xgraded carrier substitution, the record dictionary and the W2/W9 profile constructions",
)
REGISTERED_OBJECTS = ()
ADOPTED_OBJECTS = ()
# THE BANNER'S SECOND HALF, AS DECLARED MEASURED CONSTANTS.  ALL OF THEM ARE
# FALSE AND STAY FALSE.
GRAVITY_SUPPLIED_CLAIMED = False
JOINT_IS_MEASUREMENT_CLAIMED = False
ORDER_IS_QUANTUM_SIGNATURE_CLAIMED = False
EXTENDED_ALPHABET_COMPLETE_CLAIMED = False
CLASSICAL_NO_GO_CLAIMED = False
GENERIC_PARAMETER_THEOREM_CLAIMED = False
CONTINUUM_LIMIT_CLAIMED = False
READINGS_LICENSED_CLAIMED = False
READING_IDENTIFIED_CLAIMED = False
NONCOMMUTATIVITY_IS_NONCLASSICAL_CLAIMED = False
ORDER_AXIS_PRIORITY_CLAIMED = False
ALPHABET_EXHAUSTIVE_CLAIMED = False
RANK_GROWTH_LAW_CLAIMED = False
BOUND_VIOLATED_CLAIMED = False
SCOPE_GENERALISATION_CLAIMED = False
UNSUPPLIED_GRAVITY_STRUCTURES = (
    "lapse function",
    "shift vector",
    "ADM phase space",
    "Hamiltonian constraint",
    "momentum/diffeomorphism constraint",
    "first-class constraint algebra",
    "Dirac closure",
    "Dirac observable",
    "gauge orbit and its quotient",
)
# Three historical labels are retained for scope checking.  The old block
# 210 formulated a Leggett-Garg-type bound and found it satisfied everywhere.
# This block formulates NO bound and violates NONE.
NAMED_PHYSICS_WORDS = ("QUANTUM", "BELL", "LEGGETT-GARG")
BOUND_FORMULATED_HERE = False
BOUNDS_VIOLATED = 0
# THE ONE PHRASE THE PACKAGE LICENSES, VERBATIM AND UNCHANGED FROM BLOCKS 202
# AND 210.
LICENSED_PHRASE = "contextuality/interference-LIKE diagnostics"
# THE THREE SCOPED HEADLINE WORDS.
SCOPED_HEADLINE_WORDS = ("ORDER", "JOINT", "EXTENDED")
READINGS = (
    "R1: that a failing two-pin mixture identity is a nonclassicality result.  Measured: one identity, on one bench, under ONE PROPOSED reading of the pinned profiles as conditionals and the record-free profile as formation weights.  The calculation does not identify either half of that proposed reading; nothing here decides which assumption fails.  Reading.",
    "R2: that the record action itself is noncommutative.  Measured: the two proposed chain-rule FACTORIZATIONS give different sixteen-entry arrays, while reversing insertion order in the bounded helper's simultaneous record dictionary leaves the structural action identical at all sixteen outcomes.  The diagnostic order dependence belongs to the proposed conditioning rule, not to the record substitution.  Reading.",
    "R3: that the order axis is NEW.  Measured: this block runs it on this bench.  No priority survey of any literature was performed by any line here, and calling the axis new would be an unsupported priority claim.  Reading.",
    "R4: that the twenty-outcome inconsistency excludes a classical hidden-outcome model.  Measured: no TWENTY-COMPONENT weight over the SIX TESTED contexts, at ranks (12, 13).  Six exact normalization-row relations cap coefficient rank at 19, so no outcome-count threshold is inferred; richer alphabets, other class values, other families and other levels are NOT excluded.  Reading.",
    "R5: that the rank-growth pattern (4, 5), (8, 9), (12, 13) is a law.  Measured: THREE points, displayed.  No fourth rung is run and no extrapolation to any rung is claimed by any gate here.  Reading.",
    "R6: that any of it generalises past this instance.  Measured: one bench, one carrier, one pin class value, two pin slots for the joint instrument, one mid slot for the alphabet, one readout level for the order test and six contexts for the alphabet.  Reading.",
)
HISTORICAL_CONTEXT_LABEL = "B210-R3-C3-CONFIRM-R4-RANKS-CONFIRM-CONJECTURE-REFUTE"
CORRECTION_NUMBER = 112

# ---------------------------------------------------------------------------
# THE EXPECTED VALUES, declared as literals so every claim below is auditable
# against the note without reading the code that measures it.
# ---------------------------------------------------------------------------
ZERO_RESIDUAL = 0

# --- the fixed finite bench ------------------------------------------------------
BENCH_TAG = "12x4"
BENCH_COVER = 12
BENCH_LX = 4
BENCH_N = 24
BENCH_T = 6
BENCH_CORE = 1
BENCH_TSTAR = 5
FREE_LEVELS = (2, 3, 4, 5)
SLOT_A = 2
SLOT_B = 4
MID_SLOT = 3
READ_LEVEL = 5
GRAM_PRIMARY = "W9"
GRAM_SECOND = "W2"
PIN_CLASS_VALUE = 0

# --- C: THE JOINT-PIN INSTRUMENT ---------------------------------------------
JOINT_SLOTS = (2, 4)
JOINT_OUTCOMES = 16
JOINT_SINGLE_PINS = 8
JOINT_ENVIRONMENTS = 25
CACHE_ENVIRONMENTS = 45
JOINT_SUPPORT_COMPLETE = True
# Both ordered factorization arrays are exact normalized nonnegative arrays.
# Calling them physical probabilities would additionally require the proposed
# reading, which this runner does not identify.
JOINT_SUM_FORWARD = sp.Integer(1)
JOINT_SUM_REVERSED = sp.Integer(1)
JOINT_NONNEGATIVE_FORWARD = True
JOINT_NONNEGATIVE_REVERSED = True
# THE TWO-PIN MIXTURE IDENTITY FAILS IN BOTH ORDERS.  The residual components
# run to fourteen hundred digits each and are therefore fingerprinted by their
# exact sign pattern, their exact zero sum, their exact nonzeroness and their
# numerator/denominator digit counts, with the decimals below produced by the
# single display helper and never consumed by a verdict.
TWO_PIN_IDENTITY_HOLDS = False
TWO_PIN_NONZERO_FORWARD = 4
TWO_PIN_NONZERO_REVERSED = 4
TWO_PIN_SIGNS_FORWARD = ("+", "-", "+", "-")
TWO_PIN_SIGNS_REVERSED = ("+", "-", "+", "-")
TWO_PIN_SUM_FORWARD = sp.Integer(0)
TWO_PIN_SUM_REVERSED = sp.Integer(0)
TWO_PIN_DISPLAY_FORWARD = ("+4.969e-04", "-1.279e-03",
                           "+2.016e-03", "-1.233e-03")
TWO_PIN_DISPLAY_REVERSED = ("+5.010e-04", "-1.282e-03",
                            "+2.017e-03", "-1.236e-03")
# THE HISTORICAL CACHE'S PRINTED FINGERPRINTS, CARRIED SEPARATELY SO THE
# REPRODUCTION IS A COMPARISON AND NOT AN ASSERTION.  They are identical to the
# two tuples above, character for character, and gate C-3 says so.
HISTORICAL_CACHE_TWO_PIN_FORWARD = ("+4.969e-04", "-1.279e-03",
                                 "+2.016e-03", "-1.233e-03")
HISTORICAL_CACHE_TWO_PIN_REVERSED = ("+5.010e-04", "-1.282e-03",
                                  "+2.017e-03", "-1.236e-03")
TWO_PIN_NUMERATOR_DIGITS_FORWARD = (1403, 1403, 1401, 1403)
TWO_PIN_NUMERATOR_DIGITS_REVERSED = (1381, 1382, 1380, 1382)
# THE SINGLE-PIN COMPARISON CENSUS, RE-MEASURED HERE FROM THE SAME CACHE.  The
# mid-slot entry is THE HISTORICAL CACHE'S MID-SLOT RESIDUAL and it reproduces digit for
# digit at the displayed precision.
SINGLE_PIN_SLOTS = (2, 3, 4)
SINGLE_PIN_DISPLAY = {
    2: ("+6.972e-06", "-1.088e-05", "+8.217e-06", "-4.311e-06"),
    3: ("+9.178e-05", "-2.297e-04", "+1.328e-04", "+5.072e-06"),
    4: ("+4.964e-04", "-1.274e-03", "+2.012e-03", "-1.234e-03"),
}
# Historical cache display string, retained only as a fingerprint.  The live
# run recomputes the mid-slot row and does not import the old note or runner.
HISTORICAL_MID_SLOT_DISPLAY = ("+9.178e-05", "-2.297e-04",
                                    "+1.328e-04", "+5.072e-06")
HISTORICAL_MID_SLOT_MATCHED = True
# THE COMPOUNDING, AND IT IS MEASURED IN BOTH DIRECTIONS.  Componentwise counts
# out of four, per (order, single-pin slot).
COMPOUND_COMPONENTWISE = {
    ("fwd", 2): 4, ("fwd", 3): 4, ("fwd", 4): 3,
    ("rev", 2): 4, ("rev", 3): 4, ("rev", 4): 4,
}
# TEN TIMES the l1 norm of the single-pin residual is still below the two-pin
# one at slots 2 and 3 -- an order of magnitude, exactly and as a rational
# predicate -- AND IT IS NOT at slot 4.
COMPOUND_L1_TENFOLD = {
    ("fwd", 2): True, ("fwd", 3): True, ("fwd", 4): False,
    ("rev", 2): True, ("rev", 3): True, ("rev", 4): False,
}
COMPOUND_L1_STRICT = {
    ("fwd", 2): True, ("fwd", 3): True, ("fwd", 4): True,
    ("rev", 2): True, ("rev", 3): True, ("rev", 4): True,
}
# At slot 2 the l1 comparison is also hundredfold.  Every ratio word in the
# note has a predicate here; none is prose.
COMPOUND_L1_HUNDREDFOLD = {
    ("fwd", 2): True, ("fwd", 3): False, ("fwd", 4): False,
    ("rev", 2): True, ("rev", 3): False, ("rev", 4): False,
}
# THE HONEST HALF OF THE COMPOUNDING, AND IT IS MEASURED RATHER THAN ASSERTED:
# the LATER pin already carries essentially the whole two-pin residual.  The
# predicate is exact -- TWO HUNDRED times the l1 EXCESS of the two-pin residual
# over the single-pin one is still below that single-pin norm -- and it is TRUE
# at slot 4 in both orders and FALSE at slots 2 and 3, which is precisely the
# asymmetry the word 'dominates' names.
COMPOUND_L1_EXCESS_NARROW = {
    ("fwd", 2): False, ("fwd", 3): False, ("fwd", 4): True,
    ("rev", 2): False, ("rev", 3): False, ("rev", 4): True,
}
LATER_PIN_DOMINATES = True
COMPOUND_TENFOLD_OVER_MID_SLOT = True

# --- D: THE PROPOSED FACTORIZATION ORDER -------------------------------------
ORDER_ENTRIES = 16
ORDER_ENTRIES_DIFFERING = 16
ORDER_DEPENDENT = True
STRUCTURAL_ACTION_ENTRIES_DIFFERING = 0
STRUCTURAL_ACTION_COMMUTES = True
ORDER_MAX_DIFF_OUTCOME = (1, 0)
ORDER_MAX_DIFF_DISPLAY = "+2.180e-04"
ORDER_MAX_DIFF_NUMERATOR_DIGITS = 292
ORDER_MAX_DIFF_DENOMINATOR_DIGITS = 295
# THE EXACT MAXIMUM ABSOLUTE PIN-ORDER DIFFERENCE, CARRIED IN FULL RATHER THAN
# BY A HASH, so the note and the runner can be compared digit for digit.  Its
# display-only value is +2.1801e-04.
ORDER_MAX_DIFF = sp.Rational(
    1565710736248937471499916530502589575836696751368152580871498630060704757035961462688350022240775047246547494788318797706435864142630834492933612531076492084126845308134490722427335332880539475722846668849343250837202859477236495364458047997486566112399600227411525347989595791624636196906250,
    7181982954771103878426315968327978694686094989256572078303343259921606966348545103224746231948836245188087985091137926511162395361618070313446724229579120980375021889512805907765622479593505668520629567006725788814595350188787850785099114965558628307101320853888144884084076777019083512600995739)
# THE SECOND, INDEPENDENT CONSEQUENCE OF THE ORDER: the two orders push the
# READOUT residual apart in every component.
ORDER_SPLIT_NONZERO = 4
ORDER_SPLIT_SUM = sp.Integer(0)
ORDER_SPLIT_DISPLAY = ("-4.133e-06", "+3.120e-06",
                       "-1.775e-06", "+2.788e-06")
# THIS SINGLE-READOUT INSTANCE IS REAL-AFFINE CONSISTENT: the measured equality
# rank(A) = rank([A|b]) proves that statement for this system.  The 16-versus-5
# equation count alone proves nothing about consistency, and nonnegative
# restoring weights are untested.
RESTORE16_SHAPE = (5, 16)
RESTORE16_RANKS = (4, 4)
RESTORE16_SOLVABLE = True
SIMPLEX_MEMBERSHIP_TESTED = False
MULTI_CONTEXT_JOINT_INSTRUMENT_TESTED = False

# --- E: THE EXTENDED ALPHABET -------------------------------------------------
EXTENDED_CLASS_VALUES = (sp.Integer(0), sp.Rational(1, 5), sp.Rational(-1, 5),
                         sp.Rational(2, 5), sp.Rational(-2, 5))
EXTENDED_CELLS = 4
EXTENDED_OUTCOMES = 20
EXTENDED_SUPPORT_COMPLETE = True
CONTEXT_FAMILIES = ("W9", "W2")
CONTEXT_LEVELS = (5, 4, 2)
CONTEXT_COUNT = 6
EXTENDED_STACK_SHAPE = (25, 20)
EXTENDED_STACK_RANKS = (12, 13)
EXTENDED_COMMON_EXISTS = False
# THE THREE-RUNG EXCLUSION SERIES, ALL FROM ONE CACHE.  The four- and
# twelve-outcome stacks are literal sub-column-sets of the twenty-outcome one,
# so the series is ONE measurement and not three blocks' numbers.
SERIES_RUNGS = (4, 12, 20)
SERIES_SHAPES = ((25, 4), (25, 12), (25, 20))
SERIES_RANKS = ((4, 5), (8, 9), (12, 13))
SERIES_ALL_INCONSISTENT = True
SERIES_FROM_ONE_CACHE = True
# The old cache printed the first two pairs; the repaired run recomputes all
# three from one live environment cache instead of treating the old rows as
# authority.
HISTORICAL_RUNGS_MATCHED = True
RAW_GRAM_INVERTIBLE = (True, False, False)
PIVOT_BASIS_GRAM_INVERTIBLE = (True, True, True)
# --- THE REFUTATION -----------------------------------------------------------
# THE CONJECTURE, STATED SO THAT ITS REFUTATION IS UNAMBIGUOUS: that the
# contradiction functional of the six-context stack is CLASS-REFINEMENT-
# INVARIANT -- that one canonical contradiction direction is shared by every
# rung of the series.  IT IS EXACTLY FALSE.
COKERNEL_DIMENSIONS = (21, 17, 13)
COKERNEL_IS_ONE_DIMENSIONAL = False
RIESZ_ORTHOGONAL = True
RIESZ_PAIRS_WITH_RHS = True
RIESZ_REPRESENTATION_INVARIANT_CLAIMED = False
RIESZ_COLUMN_BASIS_SIZES = (4, 8, 12)
PROPORTIONALITY_PAIRS = ((4, 12), (12, 20), (4, 20))
PAIRWISE_NOT_PROPORTIONAL = (True, True, True)
# EVERY ONE OF THE 2 x 2 MINORS OF EACH PAIR IS NONZERO -- 300 of 300 in each
# of the three pairs -- so the non-proportionality is not a lucky coordinate.
PAIRWISE_NONZERO_MINORS = (300, 300, 300)
PAIRWISE_TOTAL_MINORS = 300
# THE HISTORICAL CACHE'S COMPACT FINGERPRINT, REPRODUCED EXACTLY: the
# 4-vs-12 cross-product on context rows 0 and 1 has a rational numerator
# congruent to 7 mod 101 and is therefore nonzero.  The other two pairs are
# certified the same way here.
CERTIFICATE_MODULUS = 101
CERTIFICATE_ROWS = (0, 1)
CERTIFICATE_RESIDUES = (7, 72, 71)
CONJECTURE_REFUTED = True
# THE WEAKER TRUE STATEMENT THE CHECK LEFT STANDING, CARRIED SO THE REFUTATION
# IS NOT READ AS MORE THAN IT IS.
WEAKER_STATEMENT_SURVIVING = (
    "because the outcome columns are NESTED, the twenty-outcome residual "
    "annihilates all three stacks and pairs nontrivially with their common "
    "right-hand side, so a COMMON contradiction certificate may be CHOSEN -- "
    "that is existence, and never uniqueness or invariance of 'the' "
    "contradiction direction",
    "quotienting each cokernel by the kernel of pairing with b produces a "
    "one-dimensional quotient AUTOMATICALLY from the rank-one augmented jump, "
    "and calling that a discovered common geometric direction would be "
    "overreach",
)

# --- F: THE SIX SCOPE FENCES --------------------------------------------------
PROPOSED_READING = ("p(x at slot i, y at slot j) = w_i(x) * "
                    "P(y at j | pin x at i)")
JOINT_IDENTIFICATION_HALVES = (
    "the pinned profiles read as CONDITIONALS of one common joint law",
    "the native record-free profile('W9', i) read as FORMATION WEIGHTS",
)
WHICH_HALF_FAILS_IS_OPEN = True
# THE ORDER AXIS IS CLASSICALLY AVAILABLE, AND THESE ARE THE MECHANISMS THAT
# MAKE IT SO.  Naming them is what converts the fence from prose into a count.
CLASSICAL_ORDER_MECHANISMS = (
    "classical model misspecification -- the pinned profiles need not be "
    "conditionals of one common joint law",
    "classical marginal mismatch -- the two native record-free profiles need "
    "not be marginals of the same joint distribution",
    "classical order-dependent response kernels -- an explicitly sequential "
    "instrument may change the kernel used at its second step; this is a null "
    "model, not a claim about the simultaneous action implemented here",
)
LICENSED_PHRASE_UNCHANGED_FROM_PARENT = True
ALPHABET_OUTCOMES_TESTED = 20
UNTESTED_ALPHABET_REFINEMENTS = (
    "class values outside the tested quintuple {0, 1/5, -1/5, 2/5, -2/5}",
    "any alphabet with additional or different class values; no outcome-count threshold is established",
    "more than one class value per cell, or alphabet pins at more than one slot",
    "any readout family outside the tested pair (W9, W2)",
    "any level outside the tested triple (5, 4, 2)",
)
# The 25 displayed rows are not independent: summing the four component rows
# in each of six normalized contexts reproduces the common affine row.  These
# six exact relations give a coefficient-rank ceiling of 19.  Outcome count
# alone therefore supplies no triviality threshold.
NORMALIZATION_ROW_RELATIONS = 6
COEFFICIENT_RANK_CEILING = 19
OUTCOME_COUNT_THRESHOLD_CLAIMED = False
RICHER_ALPHABETS_REMAIN_OPEN = True
# THE SERIES IS A DISPLAYED SEQUENCE AND NOT A LAW.
SERIES_POINTS_DISPLAYED = 3
EXTRAPOLATION_CLAIMED = False
INSTANCE_SCOPE = (
    "one bench, the extracted Site('12x4', 12, 4)",
    "one carrier, the extracted xgraded substitution",
    "one pin class value, 0, throughout the joint instrument",
    "two pin slots for the joint instrument, 2 and 4, and one readout level, 5",
    "one mid slot for the extended alphabet, mid = 3",
    "six readout contexts for the alphabet, (W9, W2) x (5, 4, 2)",
)
INSTANCE_SCOPE_COUNT = 6
NOT_TESTED_HERE = (
    "the MULTI-CONTEXT joint instrument -- the sixteen-outcome stack over more "
    "than one readout context, which is the named next step",
    "simplex membership for any of the solvable systems -- nonnegativity is "
    "never asked for anywhere in this block",
    "any joint pin at a slot pair other than (2, 4)",
)

# THE ONE-FAMILY CONTRACT IS ENFORCED BY DISJOINT CLAIM KEYS AND NOT ONLY BY THE
# ASSERTION IN main().  Every claim key below is read by EXACTLY ONE FAMILY.  The
# F fences therefore carry their own constants -- READING_IDENTIFIED_CLAIMED,
# NONCOMMUTATIVITY_IS_NONCLASSICAL_CLAIMED, ORDER_AXIS_PRIORITY_CLAIMED,
# ALPHABET_EXHAUSTIVE_CLAIMED, RANK_GROWTH_LAW_CLAIMED, BOUND_VIOLATED_CLAIMED
# and SCOPE_GENERALISATION_CLAIMED -- rather than re-reading the B, C, D and E
# keys that state the same thing from the other side.  Where an F gate depends on
# a fact measured elsewhere, the gate NAMES the family that measures it in its
# statement and does not consume that family's claim, so neither leans on the
# other and no mutation can flip two families at once.

SCOPE_KEYS = ("n5_verbatim",)


def scope_certificate(text: str) -> dict:
    return {"n5_verbatim": N5_FENCE in text}


# ---------------------------------------------------------------------------
# exact helpers -- no float, no tolerance and NO nsimplify anywhere
# ---------------------------------------------------------------------------
# THE nsimplify HAZARD, INHERITED FROM BLOCK 186 AND HONOURED HERE BY ABSENCE.
# That call carries a rational TOLERANCE and maps a small nonzero rational to
# EXACTLY ZERO.  This block's whole content is a set of exact NONZERONESS
# statements about numbers whose decimals sit between 1e-6 and 1e-3, a set of
# exact ORDER statements between two such numbers, and a set of exact rank
# statements.  A tolerance-carrying call would zero the two-pin residual, zero
# the pin-order difference, collapse the compounding comparison and turn the
# refutation's minors into false proportionality.  Gate G counts the occurrences
# in this file's own source and requires ZERO, requires ZERO float literals by
# an AST scan of the same source, and requires that decimal conversion happen at
# EXACTLY ONE call site, inside the display helper, so no verdict predicate can
# ever consume a float.
NSIMPLIFY_TOKEN = "sp." + "nsimplify("


def nsimplify_occurrences() -> int:
    """MEASURED, NOT PROMISED: how many times this runner calls that function."""
    try:
        return Path(__file__).read_text(encoding="utf-8").count(NSIMPLIFY_TOKEN)
    except OSError:                                    # pragma: no cover
        return -1


def float_literal_occurrences() -> int:
    """MEASURED, NOT PROMISED: how many float literals this runner's own source
    contains, by an AST walk rather than by a text search."""
    try:
        tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    except (OSError, SyntaxError):                     # pragma: no cover
        return -1
    return sum(1 for node in ast.walk(tree)
               if isinstance(node, ast.Constant) and type(node.value) is float)


def float_call_sites() -> int:
    """THE SECOND HALF OF THE SAME HYGIENE, AND IT IS THE HALF THIS BLOCK
    ACTUALLY NEEDS.  The note carries decimal DISPLAYS for residual components
    whose exact numerators run past fourteen hundred digits, so a float
    conversion must exist somewhere; what must NOT exist is a second one.  Gate
    G-3 requires EXACTLY ONE -- the display helper below.  Every verdict
    predicate in this file therefore consumes exact rationals only, by
    measurement."""
    try:
        tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    except (OSError, SyntaxError):                     # pragma: no cover
        return -1
    return sum(1 for node in ast.walk(tree)
               if isinstance(node, ast.Call)
               and isinstance(node.func, ast.Name) and node.func.id == "float")


def display(value) -> str:
    """THE ONE AND ONLY DECIMAL CONVERSION IN THIS FILE, AND IT IS DISPLAY-ONLY.
    Nothing this function returns is ever ranked, summed or fed to a verdict;
    it is compared only against declared STRING literals, and those literals
    are the strings the historical cache printed.
    THE PRECISION IS FOUR SIGNIFICANT DIGITS ON PURPOSE: it is the precision
    the historical cache printed the two-pin residuals at and the precision
    the historical cache printed the mid-slot residual at, so the comparison
    at C-3 and C-4 is character for character rather than approximate.  Gate G-3 measures
    that this is the sole float call site."""
    return f"{float(value):+.3e}"


def exact_rank(matrix: sp.MatrixBase) -> int:
    """The rank over QQ_I, exactly.  Every consistency verdict in families D and
    E is one of these numbers against another, never a residual norm."""
    return DomainMatrix.from_Matrix(sp.Matrix(matrix)).convert_to(QQ_I).rank()


def sign_word(value) -> str:
    """The exact sign of an exact rational.  Ternary and never thresholded."""
    return "+" if value > 0 else "-" if value < 0 else "0"


def l1_norm(vector) -> object:
    """The exact l1 norm of an exact rational vector.  Used only inside ORDER
    predicates that compare two of them, never converted."""
    return sp.cancel(sum((abs(v) for v in vector), sp.Integer(0)))


def digits(value) -> int:
    """The decimal digit count of an exact integer.  An INTEGER measurement of
    an INTEGER; nothing here rounds."""
    return len(str(abs(sp.Integer(value))))


# ---------------------------------------------------------------------------
# THE MEASURED FACTS
# ---------------------------------------------------------------------------
@dataclass(frozen=True)
class BenchFacts:
    tag: str
    size: int
    width: int
    core: int
    tstar: int
    extent: int
    free_levels: tuple
    slot_a_rows: tuple
    slot_b_rows: tuple
    read_rows: tuple


@dataclass(frozen=True)
class JointFacts:
    environments: int
    cache_environments: int
    outcomes: int
    single_pins: int
    support_complete: bool
    sum_forward: object
    sum_reversed: object
    nonnegative_forward: bool
    nonnegative_reversed: bool
    nonzero_forward: int
    nonzero_reversed: int
    signs_forward: tuple
    signs_reversed: tuple
    sum_residual_forward: object
    sum_residual_reversed: object
    display_forward: tuple
    display_reversed: tuple
    numerator_digits_forward: tuple
    numerator_digits_reversed: tuple
    identity_holds: bool
    single_display: dict
    compound_componentwise: dict
    compound_l1_tenfold: dict
    compound_l1_hundredfold: dict
    compound_l1_strict: dict
    compound_l1_narrow: dict


@dataclass(frozen=True)
class OrderFacts:
    entries: int
    differing: int
    dependent: bool
    structural_differing: int
    structural_commutes: bool
    max_outcome: tuple
    max_value: object
    max_display: str
    max_numerator_digits: int
    max_denominator_digits: int
    split_nonzero: int
    split_sum: object
    split_display: tuple
    restore_shape: tuple
    restore_ranks: tuple
    restore_solvable: bool


@dataclass(frozen=True)
class AlphabetFacts:
    class_values: tuple
    outcomes: int
    support_complete: bool
    stack_shape: tuple
    stack_ranks: tuple
    common_exists: bool
    series_shapes: tuple
    series_ranks: tuple
    series_all_inconsistent: bool
    normalization_relations: int
    normalization_relations_exact: bool
    coefficient_rank_ceiling: int
    cokernel_dimensions: tuple
    column_basis_sizes: tuple
    raw_gram_invertible: tuple
    pivot_basis_gram_invertible: tuple
    riesz_orthogonal: bool
    riesz_pairs_with_rhs: bool
    pairwise_not_proportional: tuple
    pairwise_nonzero_minors: tuple
    pairwise_total_minors: int
    certificate_residues: tuple


@dataclass(frozen=True)
class Facts:
    source_base: str
    authority: AuthorityCertificate
    note_source: str
    imposed: int
    registered: int
    adopted: int
    unsupplied: int
    readings: int
    named_words: int
    scoped_words: int
    bench: BenchFacts
    joint: JointFacts
    order: OrderFacts
    alphabet: AlphabetFacts
    scope: dict
    nsimplify_calls: int
    float_literals: int
    float_calls: int


def residual(base_profile, weights, pinned_profiles, extent):
    """THE MIXTURE RESIDUAL, IN ONE PLACE FOR BOTH THE SINGLE-PIN AND THE
    TWO-PIN INSTRUMENTS.  P0 - sum_o w(o) P_o, componentwise and exact.  The
    weight keys and the pinned-profile keys are the SAME outcome keys, so the
    single-pin census and the joint instrument are literally the same
    arithmetic at two different alphabets."""
    return tuple(
        sp.cancel(base_profile[component]
                  - sum((weights[o] * pinned_profiles[o][component]
                         for o in weights), sp.Integer(0)))
        for component in range(extent))


def measure_joint(site, base_env, single_pins, joint_pins,
                  cache_size) -> JointFacts:
    """THE JOINT-PIN INSTRUMENT.  Two records are written at once and the
    mixture identity is asked in BOTH sequential orders.  Everything here is an
    exact rational; the only decimals are produced by `display` and are never
    compared against a measurement.

    `single_pins` carries TWELVE entries and the instrument uses EIGHT of them:
    the four at the mid slot are the class-0 column of family E's twenty
    environments, aliased in so that the historical cache's single-pin residual is
    RE-MEASURED from this cache rather than cited.  `cache_size` is the true
    count of distinct environments built in `measure`, which is why it is
    passed rather than inferred from these two dictionaries."""
    extent = site.lx
    base_read = base_env.profile(GRAM_PRIMARY, READ_LEVEL)
    w_a = base_env.profile(GRAM_PRIMARY, SLOT_A)
    w_b = base_env.profile(GRAM_PRIMARY, SLOT_B)
    support = base_read is not None and w_a is not None and w_b is not None

    forward, reversed_ = {}, {}
    for x in range(extent):
        conditional = single_pins[(SLOT_A, x)].profile(GRAM_PRIMARY, SLOT_B)
        support = support and conditional is not None
        for y in range(extent):
            forward[(x, y)] = sp.cancel(w_a[x] * conditional[y])
    for y in range(extent):
        conditional = single_pins[(SLOT_B, y)].profile(GRAM_PRIMARY, SLOT_A)
        support = support and conditional is not None
        for x in range(extent):
            reversed_[(x, y)] = sp.cancel(w_b[y] * conditional[x])

    joint_read = {}
    for key, environment in joint_pins.items():
        joint_read[key] = environment.profile(GRAM_PRIMARY, READ_LEVEL)
        support = support and joint_read[key] is not None

    residuals = {"fwd": residual(base_read, forward, joint_read, extent),
                 "rev": residual(base_read, reversed_, joint_read, extent)}

    singles = {}
    for slot in SINGLE_PIN_SLOTS:
        weights = base_env.profile(GRAM_PRIMARY, slot)
        pinned = {x: single_pins[(slot, x)].profile(GRAM_PRIMARY, READ_LEVEL)
                  for x in range(extent)}
        support = support and weights is not None \
            and all(p is not None for p in pinned.values())
        singles[slot] = residual(base_read, {x: weights[x] for x in
                                             range(extent)}, pinned, extent)

    componentwise, tenfold, hundredfold, strict, narrow = {}, {}, {}, {}, {}
    for order in ("fwd", "rev"):
        for slot in SINGLE_PIN_SLOTS:
            single_norm = l1_norm(singles[slot])
            joint_norm = l1_norm(residuals[order])
            componentwise[(order, slot)] = sum(
                1 for c in range(extent)
                if abs(residuals[order][c]) > abs(singles[slot][c]))
            tenfold[(order, slot)] = bool(
                sp.Integer(10) * single_norm < joint_norm)
            hundredfold[(order, slot)] = bool(
                sp.Integer(100) * single_norm < joint_norm)
            strict[(order, slot)] = bool(single_norm < joint_norm)
            # THE DOMINANCE PREDICATE, EXACT: two hundred times the EXCESS is
            # still below the single-pin norm, so the two-pin residual adds
            # under one part in two hundred to what that one pin already
            # produces.  True only where the single pin already carries the
            # whole thing.
            narrow[(order, slot)] = bool(
                sp.Integer(200) * sp.cancel(joint_norm - single_norm)
                < single_norm)

    return JointFacts(
        1 + 2 * extent + len(joint_pins),
        cache_size,
        len(joint_pins),
        2 * extent,
        bool(support),
        sp.cancel(sum(forward.values())),
        sp.cancel(sum(reversed_.values())),
        bool(all(value >= 0 for value in forward.values())),
        bool(all(value >= 0 for value in reversed_.values())),
        sum(1 for v in residuals["fwd"] if v != 0),
        sum(1 for v in residuals["rev"] if v != 0),
        tuple(sign_word(v) for v in residuals["fwd"]),
        tuple(sign_word(v) for v in residuals["rev"]),
        sp.cancel(sum(residuals["fwd"])),
        sp.cancel(sum(residuals["rev"])),
        tuple(display(v) for v in residuals["fwd"]),
        tuple(display(v) for v in residuals["rev"]),
        tuple(digits(sp.fraction(v)[0]) for v in residuals["fwd"]),
        tuple(digits(sp.fraction(v)[0]) for v in residuals["rev"]),
        bool(all(v == 0 for v in residuals["fwd"])
             and all(v == 0 for v in residuals["rev"])),
        {slot: tuple(display(v) for v in singles[slot])
         for slot in SINGLE_PIN_SLOTS},
        componentwise, tenfold, hundredfold, strict, narrow)


def measure_order(site, base_env, single_pins, joint_pins) -> OrderFacts:
    """THE PROPOSED FACTORIZATION ORDER, plus a direct check of the
    actual simultaneous structural action.  The two chain-rule arrays are
    compared entrywise.  Separately, reversing insertion order in the record
    dictionary must leave the bounded helper's substituted Q unchanged."""
    extent = site.lx
    w_a = base_env.profile(GRAM_PRIMARY, SLOT_A)
    w_b = base_env.profile(GRAM_PRIMARY, SLOT_B)
    forward, reversed_ = {}, {}
    for x in range(extent):
        conditional = single_pins[(SLOT_A, x)].profile(GRAM_PRIMARY, SLOT_B)
        for y in range(extent):
            forward[(x, y)] = sp.cancel(w_a[x] * conditional[y])
    for y in range(extent):
        conditional = single_pins[(SLOT_B, y)].profile(GRAM_PRIMARY, SLOT_A)
        for x in range(extent):
            reversed_[(x, y)] = sp.cancel(w_b[y] * conditional[x])
    deltas = {key: sp.cancel(forward[key] - reversed_[key]) for key in forward}
    differing = sum(1 for v in deltas.values() if v != 0)
    peak_key = max(deltas, key=lambda key: abs(deltas[key]))
    peak = abs(deltas[peak_key])

    structural_differing = 0
    for x in range(extent):
        for y in range(extent):
            forward_records = {
                (SLOT_A, x): sp.Integer(PIN_CLASS_VALUE),
                (SLOT_B, y): sp.Integer(PIN_CLASS_VALUE),
            }
            reverse_records = {
                (SLOT_B, y): sp.Integer(PIN_CLASS_VALUE),
                (SLOT_A, x): sp.Integer(PIN_CLASS_VALUE),
            }
            q_forward = sp.Matrix(site.bench.Q.subs(
                site.sub(records=forward_records)))
            q_reverse = sp.Matrix(site.bench.Q.subs(
                site.sub(records=reverse_records)))
            structural_differing += int(q_forward != q_reverse)

    base_read = base_env.profile(GRAM_PRIMARY, READ_LEVEL)
    joint_read = {key: joint_pins[key].profile(GRAM_PRIMARY, READ_LEVEL)
                  for key in joint_pins}
    split = tuple(sp.cancel(a - b) for a, b in zip(
        residual(base_read, forward, joint_read, extent),
        residual(base_read, reversed_, joint_read, extent)))

    columns = [[joint_read[(x, y)][component] for x in range(extent)
                for y in range(extent)] for component in range(extent)]
    system = sp.Matrix(columns).col_join(sp.ones(1, len(joint_read)))
    rhs = sp.Matrix([base_read[c] for c in range(extent)] + [sp.Integer(1)])
    ranks = (exact_rank(system), exact_rank(system.row_join(rhs)))
    return OrderFacts(
        len(deltas), differing, bool(differing == len(deltas)),
        structural_differing, bool(structural_differing == 0),
        peak_key, peak, display(peak),
        digits(sp.fraction(peak)[0]), digits(sp.fraction(peak)[1]),
        sum(1 for v in split if v != 0), sp.cancel(sum(split)),
        tuple(display(v) for v in split),
        system.shape, ranks, ranks[0] == ranks[1])


def outcome_system(base_env, envs, outcomes, extent):
    """THE OUTCOME SYSTEM, AND ITS SHAPE IS ITS CONTENT.  One column per
    outcome, one row per readout component per context, plus one affine
    normalisation row sum(w) = 1.  `outcomes` selects a SUB-TUPLE of the same
    twenty environments at every rung, so the whole series is one cache."""
    rows, rhs, support = [], [], True
    for family in CONTEXT_FAMILIES:
        for level in CONTEXT_LEVELS:
            base = base_env.profile(family, level)
            pinned = [envs[o].profile(family, level) for o in outcomes]
            if base is None or any(p is None for p in pinned):
                support = False
                continue
            for component in range(extent):
                rows.append([p[component] for p in pinned])
                rhs.append(base[component])
    rows.append([sp.Integer(1)] * len(outcomes))
    rhs.append(sp.Integer(1))
    return sp.Matrix(rows), sp.Matrix(rhs), support


def riesz_residual(matrix, rhs):
    """THE FIXED-EUCLIDEAN-ROW-COORDINATE CONTRADICTION REPRESENTATIVE.
    r = b - proj_col(A)b is unique after the displayed row coordinates and
    their Euclidean inner product are fixed.  It is independent of which
    column basis spans col(A), but it is not invariant under arbitrary
    non-orthogonal changes of row coordinates.  The raw A.T A is invertible at
    the 25 x 4 rung and singular at the 12- and 20-column rungs.  The projector
    uniformly uses the RREF pivot basis C; C has full column rank, so C.T C is
    positive definite and invertible at every rung.  Everything is exact
    rational; no pseudo-inverse and no tolerance is used."""
    pivots = sp.Matrix(matrix).rref(simplify=False)[1]
    basis = matrix[:, list(pivots)]
    normal = basis.T * basis
    coefficients = normal.LUsolve(basis.T * rhs)
    return (sp.Matrix([sp.cancel(v) for v in (rhs - basis * coefficients)]),
            tuple(pivots))


def measure_alphabet(site, base_env, envs) -> AlphabetFacts:
    """THE EXTENDED ALPHABET AND THE REFUTATION.  'Does ANY twenty-weight
    reproduce the six tested marginals' is rank A against rank [A|b], exactly
    over QQ_I.  'Is the contradiction direction class-refinement-invariant' is
    three exact non-proportionality certificates."""
    extent = site.lx
    rungs = {4: EXTENDED_CLASS_VALUES[:1],
             12: EXTENDED_CLASS_VALUES[:3],
             20: EXTENDED_CLASS_VALUES}
    shapes, ranks, systems, support = [], [], {}, True
    for size in SERIES_RUNGS:
        outcomes = tuple((x, k) for x in range(extent) for k in rungs[size])
        matrix, rhs, rung_support = outcome_system(
            base_env, envs, outcomes, extent)
        support = support and rung_support
        shapes.append(matrix.shape)
        ranks.append((exact_rank(matrix), exact_rank(matrix.row_join(rhs))))
        systems[size] = (matrix, rhs)

    extended_matrix, extended_rhs = systems[EXTENDED_OUTCOMES]
    relation_rows = []
    for context in range(CONTEXT_COUNT):
        row = [sp.Integer(0)] * extended_matrix.rows
        for component in range(extent):
            row[context * extent + component] = sp.Integer(1)
        row[-1] = sp.Integer(-1)
        relation_rows.append(row)
    relation_matrix = sp.Matrix(relation_rows)
    relation_count = exact_rank(relation_matrix)
    relations_exact = bool(
        relation_matrix * extended_matrix == sp.zeros(CONTEXT_COUNT,
                                                       extended_matrix.cols)
        and relation_matrix * extended_rhs == sp.zeros(CONTEXT_COUNT, 1)
    )
    rank_ceiling = extended_matrix.rows - relation_count

    residuals, bases, basis_gram_invertible, orthogonal, pairs_with_rhs, \
        cokernels = {}, [], [], True, True, []
    for rung_index, size in enumerate(SERIES_RUNGS):
        matrix, rhs = systems[size]
        vector, pivots = riesz_residual(matrix, rhs)
        residuals[size] = vector
        bases.append(len(pivots))
        # Over the real rationals, a full-column-rank C makes C.T C positive
        # definite.  RREF supplies exactly rank(A) pivot columns; LUsolve above
        # also fails rather than silently pseudo-inverting a singular normal.
        basis_gram_invertible.append(
            len(pivots) == ranks[rung_index][0]
        )
        orthogonal = orthogonal and all(
            sp.cancel(v) == 0 for v in (matrix.T * vector))
        pairs_with_rhs = pairs_with_rhs and sp.cancel(
            (vector.T * rhs)[0, 0]) != 0
        cokernels.append(matrix.rows - ranks[rung_index][0])

    not_proportional, nonzero_minors, residues = [], [], []
    total_minors = 0
    for left, right in PROPORTIONALITY_PAIRS:
        first, second = residuals[left], residuals[right]
        minors = [sp.cancel(first[a] * second[b] - first[b] * second[a])
                  for a in range(first.rows)
                  for b in range(a + 1, first.rows)]
        total_minors = len(minors)
        nonzero = sum(1 for m in minors if m != 0)
        not_proportional.append(nonzero > 0)
        nonzero_minors.append(nonzero)
        anchor = sp.cancel(first[CERTIFICATE_ROWS[0]] * second[CERTIFICATE_ROWS[1]]
                           - first[CERTIFICATE_ROWS[1]] * second[CERTIFICATE_ROWS[0]])
        residues.append(int(sp.Integer(sp.fraction(anchor)[0])
                            % CERTIFICATE_MODULUS) if anchor != 0 else -1)

    index = SERIES_RUNGS.index(EXTENDED_OUTCOMES)
    return AlphabetFacts(
        EXTENDED_CLASS_VALUES, extent * len(EXTENDED_CLASS_VALUES),
        bool(support), shapes[index], ranks[index],
        ranks[index][0] == ranks[index][1],
        tuple(shapes), tuple(ranks),
        bool(all(a != b for a, b in ranks)),
        relation_count, relations_exact, rank_ceiling,
        tuple(cokernels), tuple(bases),
        tuple(rank[0] == shape[1] for rank, shape in zip(ranks, shapes)),
        tuple(basis_gram_invertible), bool(orthogonal), bool(pairs_with_rhs),
        tuple(not_proportional), tuple(nonzero_minors),
        total_minors, tuple(residues))


def measure() -> Facts:
    source_base = SOURCE_BASE_COMMIT
    text, source = note_text()
    site = b171.Site(BENCH_TAG, BENCH_COVER, BENCH_LX)

    def action(records):
        return sp.Matrix(site.bench.Q.subs(site.sub(records=dict(records))))

    # THE ONE MEASUREMENT PASS, AND THE CACHE IS THE COST CONTROL.  Forty-five
    # exact environments are built here and shared by every family: the
    # record-free base, the EIGHT single class-0 pins at slots 2 and 4, the
    # SIXTEEN doubly-pinned environments, and the TWENTY extended-alphabet
    # environments at the mid slot 3.  The base is ONE object serving all
    # three; and the four class-0 environments at the mid slot inside family
    # E's twenty are the SAME objects that supply the historical cache's single-pin
    # residual in family C, so that comparison is a re-measurement and not a
    # citation.
    base_env = b171.Env(site, action({}), "b")
    alphabet_envs = {
        (x, k): b171.Env(site, action({(MID_SLOT, x): k}), f"m{x}k{k}")
        for x in range(site.lx) for k in EXTENDED_CLASS_VALUES}
    single_pins = {}
    for slot in (SLOT_A, SLOT_B):
        for x in range(site.lx):
            single_pins[(slot, x)] = b171.Env(
                site, action({(slot, x): sp.Integer(PIN_CLASS_VALUE)}),
                f"p{slot}x{x}")
    for x in range(site.lx):
        single_pins[(MID_SLOT, x)] = alphabet_envs[
            (x, EXTENDED_CLASS_VALUES[0])]
    joint_pins = {
        (x, y): b171.Env(
            site,
            action({(SLOT_A, x): sp.Integer(PIN_CLASS_VALUE),
                    (SLOT_B, y): sp.Integer(PIN_CLASS_VALUE)}),
            f"j{x}{y}")
        for x in range(site.lx) for y in range(site.lx)}

    bench = BenchFacts(
        site.tag, site.N, site.T, site.c, site.tstar, site.lx,
        tuple(site.free_levels), tuple(site.rows(SLOT_A)),
        tuple(site.rows(SLOT_B)), tuple(site.rows(READ_LEVEL)))
    return Facts(
        source_base,
        authority_certificate(),
        source,
        len(IMPOSED_OBJECTS),
        len(REGISTERED_OBJECTS),
        len(ADOPTED_OBJECTS),
        len(UNSUPPLIED_GRAVITY_STRUCTURES),
        len(READINGS),
        len(NAMED_PHYSICS_WORDS),
        len(SCOPED_HEADLINE_WORDS),
        bench,
        measure_joint(site, base_env, single_pins, joint_pins,
                      1 + 2 * site.lx + len(joint_pins) + len(alphabet_envs)),
        measure_order(site, base_env, single_pins, joint_pins),
        measure_alphabet(site, base_env, alphabet_envs),
        scope_certificate(text),
        nsimplify_occurrences(),
        float_literal_occurrences(),
        float_call_sites())


# ---------------------------------------------------------------------------
# THE CLAIMS.  Every one of them is a literal, and a mutation rewrites exactly
# one of them.  No measurement is taken here.
# ---------------------------------------------------------------------------
def build_claims(mutation: str) -> dict:
    claims = {
        # A
        "source_base": SOURCE_BASE_COMMIT,
        "note_sha256": INPUT_SHA256[SELF_NOTE_INPUT],
        "helper_sha256": INPUT_SHA256[HELPER_PATH],
        # B
        "imposed": len(IMPOSED_OBJECTS),
        "registered": 0,
        "adopted": 0,
        "gravity_supplied": GRAVITY_SUPPLIED_CLAIMED,
        "unsupplied": len(UNSUPPLIED_GRAVITY_STRUCTURES),
        "joint_is_measurement": JOINT_IS_MEASUREMENT_CLAIMED,
        "order_is_quantum_signature": ORDER_IS_QUANTUM_SIGNATURE_CLAIMED,
        "extended_alphabet_complete": EXTENDED_ALPHABET_COMPLETE_CLAIMED,
        "classical_no_go": CLASSICAL_NO_GO_CLAIMED,
        "generic_parameter_theorem": GENERIC_PARAMETER_THEOREM_CLAIMED,
        "continuum_limit": CONTINUUM_LIMIT_CLAIMED,
        "readings": len(READINGS),
        "readings_licensed": READINGS_LICENSED_CLAIMED,
        # C
        "bench_metadata": (BENCH_TAG, BENCH_N, BENCH_T, BENCH_CORE,
                           BENCH_TSTAR, BENCH_LX),
        "free_levels": FREE_LEVELS,
        "slot_a_rows": (8, 9, 10, 11),
        "slot_b_rows": (16, 17, 18, 19),
        "read_rows": (20, 21, 22, 23),
        "joint_outcomes": JOINT_OUTCOMES,
        "joint_single_pins": JOINT_SINGLE_PINS,
        "joint_environments": JOINT_ENVIRONMENTS,
        "cache_environments": CACHE_ENVIRONMENTS,
        "joint_support": JOINT_SUPPORT_COMPLETE,
        "joint_sum_forward": JOINT_SUM_FORWARD,
        "joint_sum_reversed": JOINT_SUM_REVERSED,
        "joint_nonnegative": (JOINT_NONNEGATIVE_FORWARD,
                              JOINT_NONNEGATIVE_REVERSED),
        "two_pin_identity_holds": TWO_PIN_IDENTITY_HOLDS,
        "two_pin_nonzero": (TWO_PIN_NONZERO_FORWARD, TWO_PIN_NONZERO_REVERSED),
        "two_pin_signs": (TWO_PIN_SIGNS_FORWARD, TWO_PIN_SIGNS_REVERSED),
        "two_pin_sums": (TWO_PIN_SUM_FORWARD, TWO_PIN_SUM_REVERSED),
        "two_pin_display": (TWO_PIN_DISPLAY_FORWARD, TWO_PIN_DISPLAY_REVERSED),
        "two_pin_digits": (TWO_PIN_NUMERATOR_DIGITS_FORWARD,
                           TWO_PIN_NUMERATOR_DIGITS_REVERSED),
        "single_display": SINGLE_PIN_DISPLAY,
        "historical_mid_slot_matched": HISTORICAL_MID_SLOT_MATCHED,
        "compound_componentwise": COMPOUND_COMPONENTWISE,
        "compound_tenfold": COMPOUND_L1_TENFOLD,
        "compound_hundredfold": COMPOUND_L1_HUNDREDFOLD,
        "compound_strict": COMPOUND_L1_STRICT,
        "compound_narrow": COMPOUND_L1_EXCESS_NARROW,
        "later_pin_dominates": LATER_PIN_DOMINATES,
        "compound_over_mid_slot": COMPOUND_TENFOLD_OVER_MID_SLOT,
        # D
        "order_entries": ORDER_ENTRIES,
        "order_differing": ORDER_ENTRIES_DIFFERING,
        "order_dependent": ORDER_DEPENDENT,
        "structural_differing": STRUCTURAL_ACTION_ENTRIES_DIFFERING,
        "structural_commutes": STRUCTURAL_ACTION_COMMUTES,
        "order_max_outcome": ORDER_MAX_DIFF_OUTCOME,
        "order_max": ORDER_MAX_DIFF,
        "order_max_display": ORDER_MAX_DIFF_DISPLAY,
        "order_max_digits": (ORDER_MAX_DIFF_NUMERATOR_DIGITS,
                             ORDER_MAX_DIFF_DENOMINATOR_DIGITS),
        "order_split_nonzero": ORDER_SPLIT_NONZERO,
        "order_split_sum": ORDER_SPLIT_SUM,
        "order_split_display": ORDER_SPLIT_DISPLAY,
        "restore_shape": RESTORE16_SHAPE,
        "restore_ranks": RESTORE16_RANKS,
        "restore_solvable": RESTORE16_SOLVABLE,
        "simplex_tested": SIMPLEX_MEMBERSHIP_TESTED,
        "multi_context_tested": MULTI_CONTEXT_JOINT_INSTRUMENT_TESTED,
        # E
        "extended_class_values": EXTENDED_CLASS_VALUES,
        "extended_outcomes": EXTENDED_OUTCOMES,
        "extended_support": EXTENDED_SUPPORT_COMPLETE,
        "extended_stack_shape": EXTENDED_STACK_SHAPE,
        "extended_stack_ranks": EXTENDED_STACK_RANKS,
        "extended_common_exists": EXTENDED_COMMON_EXISTS,
        "series_shapes": SERIES_SHAPES,
        "series_ranks": SERIES_RANKS,
        "series_inconsistent": SERIES_ALL_INCONSISTENT,
        "normalization_relations": NORMALIZATION_ROW_RELATIONS,
        "normalization_relations_exact": True,
        "coefficient_rank_ceiling": COEFFICIENT_RANK_CEILING,
        "series_one_cache": SERIES_FROM_ONE_CACHE,
        "historical_rungs_matched": HISTORICAL_RUNGS_MATCHED,
        "cokernel_dimensions": COKERNEL_DIMENSIONS,
        "cokernel_one_dimensional": COKERNEL_IS_ONE_DIMENSIONAL,
        "riesz_orthogonal": RIESZ_ORTHOGONAL,
        "riesz_pairs": RIESZ_PAIRS_WITH_RHS,
        "riesz_representation_invariant":
            RIESZ_REPRESENTATION_INVARIANT_CLAIMED,
        "riesz_bases": RIESZ_COLUMN_BASIS_SIZES,
        "raw_gram_invertible": RAW_GRAM_INVERTIBLE,
        "pivot_basis_gram_invertible": PIVOT_BASIS_GRAM_INVERTIBLE,
        "not_proportional": PAIRWISE_NOT_PROPORTIONAL,
        "nonzero_minors": PAIRWISE_NONZERO_MINORS,
        "total_minors": PAIRWISE_TOTAL_MINORS,
        "certificate_residues": CERTIFICATE_RESIDUES,
        "conjecture_refuted": CONJECTURE_REFUTED,
        "correction_number": CORRECTION_NUMBER,
        "weaker_statements": len(WEAKER_STATEMENT_SURVIVING),
        # F
        "joint_halves": len(JOINT_IDENTIFICATION_HALVES),
        "which_half_open": WHICH_HALF_FAILS_IS_OPEN,
        "reading_identified": READING_IDENTIFIED_CLAIMED,
        "noncommutativity_nonclassical":
            NONCOMMUTATIVITY_IS_NONCLASSICAL_CLAIMED,
        "order_axis_priority": ORDER_AXIS_PRIORITY_CLAIMED,
        "classical_mechanisms": len(CLASSICAL_ORDER_MECHANISMS),
        "phrase_unchanged": LICENSED_PHRASE_UNCHANGED_FROM_PARENT,
        "alphabet_tested": ALPHABET_OUTCOMES_TESTED,
        "alphabet_exhaustive": ALPHABET_EXHAUSTIVE_CLAIMED,
        "untested_refinements": len(UNTESTED_ALPHABET_REFINEMENTS),
        "outcome_threshold_claimed": OUTCOME_COUNT_THRESHOLD_CLAIMED,
        "richer_alphabets_open": RICHER_ALPHABETS_REMAIN_OPEN,
        "rank_growth_law": RANK_GROWTH_LAW_CLAIMED,
        "series_points": SERIES_POINTS_DISPLAYED,
        "extrapolation": EXTRAPOLATION_CLAIMED,
        "bound_formulated_here": BOUND_FORMULATED_HERE,
        "bounds_violated": BOUNDS_VIOLATED,
        "bound_violated_claimed": BOUND_VIOLATED_CLAIMED,
        "named_words": len(NAMED_PHYSICS_WORDS),
        "instance_scope": INSTANCE_SCOPE_COUNT,
        "scope_generalisation": SCOPE_GENERALISATION_CLAIMED,
        "not_tested_here": len(NOT_TESTED_HERE),
        "scoped_words": len(SCOPED_HEADLINE_WORDS),
        # G
        "note_present": True,
        "scope": {key: True for key in SCOPE_KEYS},
        "nsimplify_calls": 0,
        "float_literals": 0,
        "float_calls": 1,
    }

    # --- A ----------------------------------------------------------------
    if mutation == "stale_main_authority":
        claims["note_sha256"] = "0" * 64
    elif mutation == "stale_parent_authority":
        claims["helper_sha256"] = "0" * 64
    # --- B ----------------------------------------------------------------
    elif mutation == "claim_objects_registered":
        claims["registered"] = 1
        claims["adopted"] = 1
    elif mutation == "claim_gravity_supplied":
        claims["gravity_supplied"] = True
        claims["unsupplied"] = 0
    elif mutation == "claim_joint_is_measurement":
        # THE FIRST MISREAD: writing TWO records at once is asserted to be a
        # JOINT MEASUREMENT.  Two class values written into two cells of a
        # rational matrix are still two substitutions.
        claims["joint_is_measurement"] = True
    elif mutation == "claim_order_is_quantum_signature":
        # THE SECOND MISREAD, AND IT IS THE ONE THIS BLOCK MUST GET RIGHT:
        # order-dependence of two proposed chain-rule factorizations is asserted
        # to be a quantum signature.  Classical order-dependent response rules
        # can produce the same distinction, while the tested structural action
        # itself commutes.
        claims["order_is_quantum_signature"] = True
    elif mutation == "claim_extended_alphabet_complete":
        # THE THIRD MISREAD: twenty outcomes are asserted to be the complete
        # alphabet.  They are one finite tested alphabet inside an unbounded
        # family; no outcome-count threshold is established.
        claims["extended_alphabet_complete"] = True
    elif mutation == "claim_classical_no_go":
        # THE OVERREACH IN ITS STRONGEST FORM: a general classical no-go is
        # asserted from six tested contexts and one readout on one bench.
        claims["classical_no_go"] = True
        claims["generic_parameter_theorem"] = True
        claims["continuum_limit"] = True
    elif mutation == "claim_readings_licensed":
        claims["readings_licensed"] = True
    # --- C ----------------------------------------------------------------
    elif mutation == "break_joint_instrument":
        claims["joint_outcomes"] = 4
        claims["joint_environments"] = 5
    elif mutation == "break_joint_normalisation":
        # THE INSTRUMENT UNCALIBRATED: the sequential joint weights are
        # asserted NOT to sum to one, which would make every residual below a
        # weighted sum over something that is not a probability array.
        claims["joint_sum_forward"] = sp.Rational(1, 2)
    elif mutation == "break_joint_nonnegativity":
        claims["joint_nonnegative"] = (False, True)
    elif mutation == "break_two_pin_identity":
        # THE HEADLINE DENIED: the two-pin mixture identity is asserted to
        # HOLD, which is exactly the outcome that would have made the joint
        # instrument uninformative.
        claims["two_pin_identity_holds"] = True
        claims["two_pin_nonzero"] = (0, 0)
    elif mutation == "break_compounding":
        # THE HONEST HALF DELETED: the two-pin residual is asserted to exceed
        # EVERY single-pin residual by an order of magnitude.  It does not --
        # at slot 4 it exceeds it by under one part in two hundred.
        claims["compound_tenfold"] = {key: True
                                      for key in COMPOUND_L1_TENFOLD}
        claims["compound_hundredfold"] = {key: True
                                          for key in COMPOUND_L1_HUNDREDFOLD}
        claims["compound_narrow"] = {key: False
                                     for key in COMPOUND_L1_EXCESS_NARROW}
        claims["later_pin_dominates"] = False
    # --- D ----------------------------------------------------------------
    elif mutation == "break_order_dependence":
        # The two proposed factorization arrays are falsely asserted equal;
        # this mutation says nothing about the simultaneous record action,
        # whose commutativity is measured separately.
        claims["order_differing"] = 0
        claims["order_dependent"] = False
    elif mutation == "break_structural_commutation":
        claims["structural_differing"] = ORDER_ENTRIES
        claims["structural_commutes"] = False
    elif mutation == "break_order_residual_split":
        claims["order_split_nonzero"] = 0
    elif mutation == "break_single_readout_solvability":
        # THE MEASURED RANK EQUALITY REWRITTEN: the actual (4, 4) pair is
        # changed to (4, 5), fabricating an affine exclusion.  The shape alone
        # supplies neither the baseline consistency nor the mutated result.
        claims["restore_ranks"] = (4, 5)
        claims["restore_solvable"] = False
    # --- E ----------------------------------------------------------------
    elif mutation == "break_extended_alphabet":
        claims["extended_outcomes"] = 12
        claims["extended_class_values"] = EXTENDED_CLASS_VALUES[:3]
    elif mutation == "break_extended_stack_inconsistency":
        # THE ESCAPE RE-OPENED: the twenty-outcome stack is asserted
        # CONSISTENT, which is the outcome that would have converted the whole
        # package into a statement about an under-specified alphabet.
        claims["extended_stack_ranks"] = (12, 12)
        claims["extended_common_exists"] = True
    elif mutation == "break_exclusion_series":
        # THE COMPARISON BROKEN: the historical cache's twelve-outcome rung is
        # asserted CONSISTENT here, which would make this block's (12, 13) an
        # unrelated fact rather than the third rung of one series.
        claims["series_ranks"] = ((4, 5), (8, 8), (12, 13))
        claims["historical_rungs_matched"] = False
    elif mutation == "break_conjecture_refutation":
        # THE REFUTATION DENIED: the canonical contradiction directions are
        # asserted PROPORTIONAL across refinements, which is the conjecture the
        # finite calculation refutes.
        claims["not_proportional"] = (False, False, False)
        claims["conjecture_refuted"] = False
    # --- F ----------------------------------------------------------------
    elif mutation == "claim_reading_identified":
        # THE PROPOSED-READING FENCE DELETED: the W9 formation-weight reading is
        # asserted identified rather than proposed, which would turn every
        # residual in this block from a conditional number into an established
        # one.
        claims["reading_identified"] = True
        claims["which_half_open"] = False
    elif mutation == "claim_noncommutativity_is_nonclassical":
        # The proposed-factorization difference is promoted to a
        # nonclassicality result despite the explicit classical nulls above.
        claims["noncommutativity_nonclassical"] = True
        claims["classical_mechanisms"] = 0
    elif mutation == "claim_order_axis_is_new":
        # THE PRIORITY CLAIM THE BLOCK DOES NOT EARN: the order axis is
        # asserted NEW.  No priority survey was performed by any line here.
        claims["order_axis_priority"] = True
    elif mutation == "claim_alphabet_exhaustive":
        # THE EXCLUSION ASSERTED FULLY CLOSED: twenty outcomes are asserted to
        # exhaust the classical outcome space, so that 'no common w' would
        # become 'no classical model'.  Twenty-one alone refutes it.
        claims["alphabet_exhaustive"] = True
        claims["untested_refinements"] = 0
    elif mutation == "claim_rank_law":
        # THREE POINTS PROMOTED TO A LAW: the rank-growth pattern is asserted
        # to be a rule rather than a displayed sequence.
        claims["rank_growth_law"] = True
        claims["extrapolation"] = True
    elif mutation == "claim_bound_violated":
        # THE WORD THE PACKAGE DOES NOT EARN: a violated bound is asserted.
        # This block formulates NO bound and violates NONE; the historical bound is
        # satisfied everywhere it was measured and is not re-fired here.
        claims["bound_violated_claimed"] = True
        claims["bounds_violated"] = 1
    elif mutation == "break_instance_scope":
        claims["instance_scope"] = 0
    # --- G ----------------------------------------------------------------
    elif mutation == "drop_n5_fence":
        claims["scope"] = {key: False for key in SCOPE_KEYS}
    elif mutation == "break_nsimplify_absence":
        claims["nsimplify_calls"] = 1
    elif mutation == "break_float_absence":
        claims["float_literals"] = 1
        claims["float_calls"] = 2
    return claims


def build_checks(facts: Facts, claims: dict) -> Checks:
    checks = Checks()
    authority = facts.authority
    bench = facts.bench
    joint = facts.joint
    order = facts.order
    alphabet = facts.alphabet

    # --- A: IMMUTABLE INPUT-BYTE CLOSURE -----------------------------------
    checks.check(
        "A-1", f"all {len(AUDIT_INPUT_PATHS)} literal input paths are readable "
        f"and match their declared SHA-256 bytes; the repair source context is "
        f"{claims['source_base'][:12]} and the declared producer timeout is "
        f"{AUDIT_TIMEOUT_SEC}s",
        authority.all_inputs_content_bound
        and authority.inputs_readable == len(AUDIT_INPUT_PATHS)
        and not authority.inputs_missing
        and facts.source_base == claims["source_base"])
    checks.check(
        "A-2", f"the note hash {claims['note_sha256'][:12]} and helper hash "
        f"{claims['helper_sha256'][:12]} equal the reviewed bytes; current "
        f"Block 105 and both context-boundary files are pinned, the bounded "
        f"fixture imports, and its supplier certificate passes",
        authority.note_content_bound
        and claims["note_sha256"] == INPUT_SHA256[SELF_NOTE_INPUT]
        and authority.helper_content_bound
        and claims["helper_sha256"] == INPUT_SHA256[HELPER_PATH]
        and authority.supplier_content_bound
        and authority.context_inputs_content_bound
        and authority.fixture_import_ready
        and authority.helper_supplier_certificate)

    # --- B: THE BANNER AND THE FENCE ---------------------------------------
    checks.check(
        "B-1", f"{facts.imposed} imposed objects, {claims['registered']} "
        f"registered, {claims['adopted']} adopted",
        facts.imposed == claims["imposed"]
        and facts.registered == claims["registered"]
        and facts.adopted == claims["adopted"])
    checks.check(
        "B-2", f"NO GRAVITY IS SUPPLIED: gravity_supplied = "
        f"{claims['gravity_supplied']} and {claims['unsupplied']} gravity "
        f"structures are enumerated as NOT SUPPLIED",
        claims["gravity_supplied"] is False
        and facts.unsupplied == claims["unsupplied"])
    checks.check(
        "B-3", f"THE WORD *JOINT* IS SCOPED BEFORE THE FIRST NUMERAL: it names "
        f"TWO class-{PIN_CLASS_VALUE} records written at once into two cells "
        f"of a rational matrix by the bounded helper's record substitution, at slots "
        f"{JOINT_SLOTS} -- a DOUBLE SUBSTITUTION -- and it names NO joint "
        f"measurement, NO collapse, NO state update and NO physical "
        f"intervention",
        claims["joint_is_measurement"] is False)
    checks.check(
        "B-4", f"THE WORD *ORDER* IS SCOPED: it names the order of the two "
        f"PROPOSED chain-rule factorizations, not the insertion order of the "
        f"simultaneous record dictionary. Family D measures the former as "
        f"different and the latter as identical; neither is a quantum "
        f"signature -- order_is_quantum_signature = "
        f"{claims['order_is_quantum_signature']}",
        claims["order_is_quantum_signature"] is False)
    checks.check(
        "B-5", f"THE WORD *EXTENDED* IS SCOPED: it names "
        f"{EXTENDED_CELLS} cells x {len(EXTENDED_CLASS_VALUES)} class values = "
        f"{EXTENDED_OUTCOMES} outcomes at the mid slot {MID_SLOT}; F-3 proves "
        f"six row relations and explicitly claims NO outcome threshold. It names NO "
        f"complete alphabet and NO exhausted outcome space -- so "
        f"extended_alphabet_complete = {claims['extended_alphabet_complete']}",
        claims["extended_alphabet_complete"] is False)
    checks.check(
        "B-6", "NO GENERAL CLASSICAL NO-GO, NO GENERIC-PARAMETER THEOREM AND "
        "NO CONTINUUM LIMIT: what is established is a set of exact "
        "finite-instance predicates on ONE bench, and six tested contexts with "
        "one readout level are not a parameter space and not a limit",
        claims["classical_no_go"] is False
        and claims["generic_parameter_theorem"] is False
        and claims["continuum_limit"] is False)
    checks.check(
        "B-7", f"THE READINGS ARE READINGS: {claims['readings']} of them are "
        f"enumerated as readings, readings_licensed = "
        f"{claims['readings_licensed']}, and EVERY NEGATIVE HERE IS NON-SUPPLY "
        f"WITHIN THIS FORMALISM AND NEVER METAPHYSICAL NECESSITY -- the "
        f"cycle-913 caution, carried verbatim, with nothing registered and "
        f"nothing adopted",
        facts.readings == claims["readings"]
        and claims["readings_licensed"] is False
        and not REGISTERED_OBJECTS and not ADOPTED_OBJECTS
        and claims["registered"] == 0 and claims["adopted"] == 0)

    # --- C: THE JOINT-PIN INSTRUMENT ---------------------------------------
    checks.check(
        "C-1", f"THE JOINT-PIN FINITE INSTRUMENT IS BUILT: the bounded helper's fixed bench {claims['bench_metadata']} for "
        f"(tag, N, T, c, tstar, lx) with free levels {claims['free_levels']}, "
        f"pin rows {claims['slot_a_rows']} at slot {SLOT_A} and "
        f"{claims['slot_b_rows']} at slot {SLOT_B}, readout rows "
        f"{claims['read_rows']} at level {READ_LEVEL}; "
        f"{claims['joint_outcomes']} DOUBLY-pinned environments plus "
        f"{claims['joint_single_pins']} single pins plus the base = "
        f"{claims['joint_environments']} environments for this instrument, "
        f"inside ONE shared cache of {claims['cache_environments']}, every "
        f"profile with support ({claims['joint_support']})",
        (bench.tag, bench.size, bench.width, bench.core, bench.tstar,
         bench.extent) == claims["bench_metadata"]
        and bench.free_levels == claims["free_levels"]
        and bench.slot_a_rows == claims["slot_a_rows"]
        and bench.slot_b_rows == claims["slot_b_rows"]
        and bench.read_rows == claims["read_rows"]
        and joint.outcomes == claims["joint_outcomes"]
        and claims["joint_outcomes"] == BENCH_LX * BENCH_LX
        and joint.single_pins == claims["joint_single_pins"]
        and joint.environments == claims["joint_environments"]
        and joint.cache_environments == claims["cache_environments"]
        and joint.support_complete is claims["joint_support"]
        and claims["joint_support"] is True)
    checks.check(
        "C-2", f"BOTH SEQUENTIAL JOINT-WEIGHT ARRAYS NORMALISE TO *EXACTLY* "
        f"ONE, AND THAT IS AN EXACT SUM AND NOT A TOLERANCE: "
        f"w_fwd(x, y) = w_2(x) * P(y at 4 | pin x at 2) sums to "
        f"{claims['joint_sum_forward']} and w_rev(x, y) = w_4(y) * "
        f"P(x at 2 | pin y at 4) sums to {claims['joint_sum_reversed']} over "
        f"all {JOINT_OUTCOMES} outcomes; every component is also exactly "
        f"nonnegative {claims['joint_nonnegative']}, so both are exact "
        f"probability arrays and every residual at C-3 is a weighted sum over one",
        sp.cancel(joint.sum_forward - claims["joint_sum_forward"]) == 0
        and sp.cancel(joint.sum_reversed - claims["joint_sum_reversed"]) == 0
        and claims["joint_sum_forward"] == sp.Integer(1)
        and claims["joint_sum_reversed"] == sp.Integer(1)
        and (joint.nonnegative_forward, joint.nonnegative_reversed)
        == claims["joint_nonnegative"]
        and all(claims["joint_nonnegative"]))
    checks.check(
        "C-3", f"THE TWO-PIN MIXTURE IDENTITY *FAILS IN BOTH ORDERS*, EXACTLY "
        f"AND IN EVERY COMPONENT: identity_holds = "
        f"{claims['two_pin_identity_holds']}, the residuals are exactly "
        f"nonzero in {claims['two_pin_nonzero'][0]} of {BENCH_LX} forward and "
        f"{claims['two_pin_nonzero'][1]} of {BENCH_LX} reversed, with exact "
        f"sign patterns {claims['two_pin_signs']}, each summing to EXACTLY "
        f"{claims['two_pin_sums'][0]} as normalisation requires; their exact "
        f"numerators run to {claims['two_pin_digits'][0]} and "
        f"{claims['two_pin_digits'][1]} digits so they are fingerprinted "
        f"rather than printed, and their display-only decimals are "
        f"{claims['two_pin_display'][0]} forward and "
        f"{claims['two_pin_display'][1]} reversed -- REPRODUCING the "
        f"historical cache fingerprints "
        f"{HISTORICAL_CACHE_TWO_PIN_FORWARD} and "
        f"{HISTORICAL_CACHE_TWO_PIN_REVERSED} character for character",
        joint.identity_holds is claims["two_pin_identity_holds"]
        and claims["two_pin_identity_holds"] is False
        and (joint.nonzero_forward, joint.nonzero_reversed)
        == claims["two_pin_nonzero"]
        and claims["two_pin_nonzero"] == (BENCH_LX, BENCH_LX)
        and (joint.signs_forward, joint.signs_reversed)
        == claims["two_pin_signs"]
        and sp.cancel(joint.sum_residual_forward
                      - claims["two_pin_sums"][0]) == 0
        and sp.cancel(joint.sum_residual_reversed
                      - claims["two_pin_sums"][1]) == 0
        and (joint.display_forward, joint.display_reversed)
        == claims["two_pin_display"]
        and joint.display_forward == HISTORICAL_CACHE_TWO_PIN_FORWARD
        and joint.display_reversed == HISTORICAL_CACHE_TWO_PIN_REVERSED
        and (joint.numerator_digits_forward, joint.numerator_digits_reversed)
        == claims["two_pin_digits"])
    checks.check(
        "C-4", f"AND THE COMPOUNDING IS MEASURED IN BOTH DIRECTIONS, WITH THE "
        f"HONEST HALF CARRIED AS A CONSTANT: the three single-pin residuals at "
        f"slots {SINGLE_PIN_SLOTS} are re-measured from the SAME cache and "
        f"display as {claims['single_display']}, of which the mid-slot one "
        f"reproduces the historical cache's "
        f"{HISTORICAL_MID_SLOT_DISPLAY} ({claims['historical_mid_slot_matched']}); "
        f"the two-pin residual has strictly larger component magnitudes in "
        f"{claims['compound_componentwise']} of four; TEN times the l1 norm of "
        f"the single-pin residual is still below the two-pin one at slots 2 "
        f"and 3 ({claims['compound_over_mid_slot']}) -- a HUNDRED times at slot 2 "
        f"({claims['compound_hundredfold']}) -- but NOT at slot 4 "
        f"({claims['compound_tenfold']}), where it is exceeded only strictly "
        f"({claims['compound_strict']}) -- TWO HUNDRED times the l1 EXCESS "
        f"over the slot-{SLOT_B} residual is still below that residual's own "
        f"norm ({claims['compound_narrow']}), so THE LATER PIN DOMINATES "
        f"({claims['later_pin_dominates']})",
        joint.single_display == claims["single_display"]
        and claims["historical_mid_slot_matched"] is True
        and joint.single_display[MID_SLOT]
        == HISTORICAL_MID_SLOT_DISPLAY
        and joint.compound_componentwise == claims["compound_componentwise"]
        and joint.compound_l1_tenfold == claims["compound_tenfold"]
        and joint.compound_l1_hundredfold == claims["compound_hundredfold"]
        and claims["compound_hundredfold"][("fwd", SLOT_A)] is True
        and claims["compound_hundredfold"][("rev", SLOT_A)] is True
        and claims["compound_hundredfold"][("fwd", MID_SLOT)] is False
        and joint.compound_l1_strict == claims["compound_strict"]
        and joint.compound_l1_narrow == claims["compound_narrow"]
        and all(claims["compound_strict"].values())
        and claims["compound_tenfold"][("fwd", MID_SLOT)] is True
        and claims["compound_tenfold"][("rev", MID_SLOT)] is True
        and claims["compound_tenfold"][("fwd", SLOT_B)] is False
        and claims["compound_tenfold"][("rev", SLOT_B)] is False
        and claims["compound_narrow"][("fwd", SLOT_B)] is True
        and claims["compound_narrow"][("rev", SLOT_B)] is True
        and claims["compound_narrow"][("fwd", MID_SLOT)] is False
        and claims["compound_over_mid_slot"] is True
        and claims["later_pin_dominates"] is True)

    # --- D: THE PIN ORDER ---------------------------------------------------
    checks.check(
        "D-1", f"THE PROPOSED FACTORIZATION ORDER MATTERS, EXACTLY AND "
        f"ENTRYWISE: w_fwd and w_rev differ in "
        f"{claims['order_differing']} of {claims['order_entries']} entries, "
        f"so factorization_order_dependent = {claims['order_dependent']}. "
        f"By contrast, reversing insertion order in the simultaneous record "
        f"dictionary changes {claims['structural_differing']} of "
        f"{claims['order_entries']} actions, so structural_action_commutes = "
        f"{claims['structural_commutes']}; the largest absolute factorization "
        f"difference sits at outcome {claims['order_max_outcome']} and is "
        f"carried as ONE exact rational with a "
        f"{claims['order_max_digits'][0]}-digit numerator and a "
        f"{claims['order_max_digits'][1]}-digit denominator, display-only "
        f"{claims['order_max_display']}",
        order.entries == claims["order_entries"]
        and order.differing == claims["order_differing"]
        and claims["order_differing"] == claims["order_entries"]
        and order.dependent is claims["order_dependent"]
        and claims["order_dependent"] is True
        and order.structural_differing == claims["structural_differing"]
        and claims["structural_differing"] == 0
        and order.structural_commutes is claims["structural_commutes"]
        and claims["structural_commutes"] is True
        and order.max_outcome == claims["order_max_outcome"]
        and sp.cancel(order.max_value - claims["order_max"]) == 0
        and order.max_display == claims["order_max_display"]
        and (order.max_numerator_digits, order.max_denominator_digits)
        == claims["order_max_digits"])
    checks.check(
        "D-2", f"AND THE FACTORIZATION CHOICE REACHES THE WEIGHTED RESIDUAL: "
        f"the two ordered residuals "
        f"of C-3 differ in {claims['order_split_nonzero']} of {BENCH_LX} "
        f"components, exactly, with the difference summing to EXACTLY "
        f"{claims['order_split_sum']} and displaying as "
        f"{claims['order_split_display']}. This is a difference between two "
        f"proposed conditioning rules on one fixed simultaneous-action family, "
        f"not structural-action noncommutativity",
        order.split_nonzero == claims["order_split_nonzero"]
        and claims["order_split_nonzero"] == BENCH_LX
        and sp.cancel(order.split_sum - claims["order_split_sum"]) == 0
        and order.split_display == claims["order_split_display"])
    checks.check(
        "D-3", f"THIS SINGLE-READOUT INSTANCE IS REAL-AFFINE CONSISTENT: the "
        f"sixteen-weight restoring system "
        f"is {claims['restore_shape']} -- {JOINT_OUTCOMES} unknowns against "
        f"{BENCH_LX} profile equations plus one normalisation row -- with "
        f"ranks {claims['restore_ranks']}, so it is real-affine SOLVABLE by "
        f"rank(A) = rank([A|b]) "
        f"({claims['restore_solvable']}); no affine inconsistency is detected "
        f"here. Simplex "
        f"membership is NOT tested ({claims['simplex_tested']}) and the "
        f"MULTI-CONTEXT joint instrument is NOT run here "
        f"({claims['multi_context_tested']}), which is the named next step",
        order.restore_shape == claims["restore_shape"]
        and order.restore_ranks == claims["restore_ranks"]
        and claims["restore_ranks"][0] == claims["restore_ranks"][1]
        and order.restore_solvable is claims["restore_solvable"]
        and claims["restore_solvable"] is True
        and claims["simplex_tested"] is False
        and claims["multi_context_tested"] is False)

    # --- E: THE EXTENDED ALPHABET -------------------------------------------
    checks.check(
        "E-1", f"THE EXTENDED ALPHABET IS BUILT AND EVERY OUTCOME HAS SUPPORT: "
        f"{EXTENDED_CELLS} cells x {len(claims['extended_class_values'])} "
        f"class values "
        f"{tuple(str(v) for v in claims['extended_class_values'])} = "
        f"{claims['extended_outcomes']} outcomes at the mid slot {MID_SLOT}, "
        f"each written into the extracted finite carrier field by the bounded "
        f"helper's record substitution, with no profile in the stack a 0/0 "
        f"({claims['extended_support']})",
        alphabet.class_values == claims["extended_class_values"]
        and alphabet.outcomes == claims["extended_outcomes"]
        and claims["extended_outcomes"]
        == EXTENDED_CELLS * len(claims["extended_class_values"])
        and alphabet.support_complete is claims["extended_support"]
        and claims["extended_support"] is True)
    checks.check(
        "E-2", f"THE SIX-CONTEXT TWENTY-OUTCOME STACK IS *STILL INCONSISTENT*: "
        f"{claims['extended_stack_shape']} -- {len(CONTEXT_FAMILIES)} families "
        f"x {len(CONTEXT_LEVELS)} levels x {BENCH_LX} components plus one "
        f"affine normalisation row -- with rank A = "
        f"{claims['extended_stack_ranks'][0]} and rank [A|b] = "
        f"{claims['extended_stack_ranks'][1]}, so common_exists = "
        f"{claims['extended_common_exists']} and NO twenty-component weight "
        f"reproduces the six tested marginals; consistency is a LINEAR "
        f"question and it fails before nonnegativity is asked for",
        alphabet.stack_shape == claims["extended_stack_shape"]
        and alphabet.stack_ranks == claims["extended_stack_ranks"]
        and claims["extended_stack_ranks"][0]
        != claims["extended_stack_ranks"][1]
        and alphabet.common_exists is claims["extended_common_exists"]
        and claims["extended_common_exists"] is False)
    checks.check(
        "E-3", f"AND THE EXCLUSION SERIES GAINS ITS THIRD RUNG, ALL FROM ONE "
        f"CACHE: shapes {claims['series_shapes']} at ranks "
        f"{claims['series_ranks']} for {SERIES_RUNGS} outcomes, every rung "
        f"INCONSISTENT ({claims['series_inconsistent']}); the four- and "
        f"twelve-outcome stacks are literal sub-column-sets of the "
        f"twenty-outcome one ({claims['series_one_cache']}); the live values "
        f"match the historical cache's first two rank pairs "
        f"({claims['historical_rungs_matched']}). Raw A.T A invertibility is "
        f"{claims['raw_gram_invertible']} across the three rungs, while the "
        f"pivot-basis C.T C is invertible at every rung "
        f"{claims['pivot_basis_gram_invertible']}",
        alphabet.series_shapes == claims["series_shapes"]
        and alphabet.series_ranks == claims["series_ranks"]
        and alphabet.series_all_inconsistent is claims["series_inconsistent"]
        and claims["series_inconsistent"] is True
        and alphabet.normalization_relations
        == claims["normalization_relations"]
        and claims["normalization_relations"] == NORMALIZATION_ROW_RELATIONS
        and alphabet.normalization_relations_exact
        is claims["normalization_relations_exact"]
        and claims["normalization_relations_exact"] is True
        and alphabet.coefficient_rank_ceiling
        == claims["coefficient_rank_ceiling"]
        and alphabet.raw_gram_invertible
        == claims["raw_gram_invertible"]
        and claims["raw_gram_invertible"] == (True, False, False)
        and alphabet.pivot_basis_gram_invertible
        == claims["pivot_basis_gram_invertible"]
        and all(claims["pivot_basis_gram_invertible"])
        and claims["series_one_cache"] is True
        and claims["historical_rungs_matched"] is True
        and claims["series_ranks"][0] == (4, 5)
        and claims["series_ranks"][1] == (8, 9))
    checks.check(
        "E-4", f"AND THE CLASS-REFINEMENT-INVARIANT CONTRADICTION CONJECTURE "
        f"IS *EXACTLY REFUTED* -- correction {claims['correction_number']}: "
        f"the left-cokernels have dimensions {claims['cokernel_dimensions']}, "
        f"so one-dimensional = {claims['cokernel_one_dimensional']} and a "
        f"a REPRESENTATIVE is required; the fixed-row-coordinate Euclidean/Riesz residual "
        f"r_n = b - proj_col(A_n)(b), built on column bases of sizes "
        f"{claims['riesz_bases']}, satisfies A^T r = 0 exactly "
        f"({claims['riesz_orthogonal']}) and pairs nontrivially with b "
        f"({claims['riesz_pairs']}); and all three pairs "
        f"{PROPORTIONALITY_PAIRS} are NON-proportional "
        f"({claims['not_proportional']}) with "
        f"{claims['nonzero_minors']} of {claims['total_minors']} exact 2 x 2 "
        f"minors nonzero in each and the check's own row-{CERTIFICATE_ROWS} "
        f"numerators congruent to {claims['certificate_residues']} mod "
        f"{CERTIFICATE_MODULUS} -- conjecture_refuted = "
        f"{claims['conjecture_refuted']}. It is column-basis independent but "
        f"not invariant under arbitrary row reparameterization "
        f"({claims['riesz_representation_invariant']}), with "
        f"{claims['weaker_statements']} weaker statements left standing",
        alphabet.cokernel_dimensions == claims["cokernel_dimensions"]
        and claims["cokernel_one_dimensional"] is False
        and all(d > 1 for d in claims["cokernel_dimensions"])
        and alphabet.column_basis_sizes == claims["riesz_bases"]
        and alphabet.riesz_orthogonal is claims["riesz_orthogonal"]
        and claims["riesz_orthogonal"] is True
        and alphabet.riesz_pairs_with_rhs is claims["riesz_pairs"]
        and claims["riesz_pairs"] is True
        and claims["riesz_representation_invariant"] is False
        and alphabet.pairwise_not_proportional == claims["not_proportional"]
        and all(claims["not_proportional"])
        and alphabet.pairwise_nonzero_minors == claims["nonzero_minors"]
        and alphabet.pairwise_total_minors == claims["total_minors"]
        and alphabet.certificate_residues == claims["certificate_residues"]
        and claims["conjecture_refuted"] is True
        and claims["weaker_statements"] == len(WEAKER_STATEMENT_SURVIVING))

    # --- F: THE SIX SCOPE FENCES -------------------------------------------
    checks.check(
        "F-1", f"FENCE ONE -- EVERY RESIDUAL IN FAMILIES C AND D IS TAKEN "
        f"UNDER A *PROPOSED* READING, AND THE TWO-PART IDENTIFICATION FENCE STANDS: the reading is {PROPOSED_READING}, its "
        f"{claims['joint_halves']} halves are {JOINT_IDENTIFICATION_HALVES}, "
        f"which of them fails is OPEN ({claims['which_half_open']}), and "
        f"reading_identified = {claims['reading_identified']} -- an identity "
        f"that FAILS under a proposed reading indicts the reading or the "
        f"framework and does not say which",
        claims["reading_identified"] is False
        and claims["joint_halves"] == len(JOINT_IDENTIFICATION_HALVES)
        and claims["joint_halves"] == 2
        and claims["which_half_open"] is True)
    checks.check(
        "F-2", f"FENCE TWO -- THE MEASURED ORDER DEPENDENCE BELONGS TO TWO "
        f"PROPOSED CLASSICAL FACTORIZATIONS, WHILE THE SIMULTANEOUS STRUCTURAL "
        f"ACTION COMMUTES: noncommutativity_nonclassical = "
        f"{claims['noncommutativity_nonclassical']}, "
        f"{claims['classical_mechanisms']} classical mechanisms that produce "
        f"the same order-dependence are named ({CLASSICAL_ORDER_MECHANISMS}), "
        f"order_axis_priority = {claims['order_axis_priority']} because no "
        f"priority survey was run, and the licensed phrase is UNCHANGED from "
        f"Blocks 202 and 210 ({claims['phrase_unchanged']}) and remains "
        f"'{LICENSED_PHRASE}'; the measured order-dependence itself is gated "
        f"separately at D-1 and D-2, so neither leans on the other",
        claims["noncommutativity_nonclassical"] is False
        and claims["order_axis_priority"] is False
        and claims["classical_mechanisms"] == len(CLASSICAL_ORDER_MECHANISMS)
        and claims["classical_mechanisms"] > 0
        and claims["phrase_unchanged"] is True)
    checks.check(
        "F-3", f"FENCE THREE -- THE ALPHABET EXCLUSION IS "
        f"{claims['alphabet_tested']}-OUTCOME AND {CONTEXT_COUNT}-CONTEXT, AND "
        f"NO OUTCOME-COUNT TRIVIALITY THRESHOLD IS CLAIMED: alphabet_exhaustive = "
        f"{claims['alphabet_exhaustive']}, {claims['untested_refinements']} "
        f"richer refinements are named as NOT tested. The 25 displayed rows "
        f"have {claims['normalization_relations']} exact normalization "
        f"relations and coefficient-rank ceiling "
        f"{claims['coefficient_rank_ceiling']}; outcome_threshold_claimed = "
        f"{claims['outcome_threshold_claimed']} and richer_alphabets_open = "
        f"{claims['richer_alphabets_open']}",
        claims["alphabet_exhaustive"] is False
        and claims["alphabet_tested"] == EXTENDED_OUTCOMES
        and claims["untested_refinements"]
        == len(UNTESTED_ALPHABET_REFINEMENTS)
        and claims["untested_refinements"] > 0
        and claims["normalization_relations"] == 6
        and claims["coefficient_rank_ceiling"] == 19
        and claims["outcome_threshold_claimed"] is False
        and claims["richer_alphabets_open"] is True)
    checks.check(
        "F-4", f"FENCE FOUR -- THE RANK-GROWTH PATTERN IS A *DISPLAYED "
        f"SEQUENCE* AND NOT A LAW: {claims['series_points']} points are "
        f"displayed, rank_growth_law = {claims['rank_growth_law']} and "
        f"extrapolation = {claims['extrapolation']}; no fourth rung is run "
        f"anywhere in this block, nothing is fitted, and no statement about "
        f"any untested alphabet size follows from the three measured ones -- "
        f"the ranks themselves are gated separately at E-3, so neither leans "
        f"on the other",
        claims["rank_growth_law"] is False
        and claims["extrapolation"] is False
        and claims["series_points"] == len(SERIES_RUNGS)
        and claims["series_points"] > 0)
    checks.check(
        "F-5", f"FENCE FIVE -- NO BOUND IS FORMULATED HERE AND NONE IS "
        f"VIOLATED: bound_formulated_here = {claims['bound_formulated_here']}, "
        f"{claims['bounds_violated']} bounds are violated by any line of this "
        f"block and bound_violated_claimed = "
        f"{claims['bound_violated_claimed']}; the {claims['named_words']} "
        f"words {NAMED_PHYSICS_WORDS} are historical labels for a bound, which is not "
        f"re-fired here, and NOTHING in this block approaches it; the general "
        f"classical no-go, the gravity banner and the registered/adopted "
        f"counts are gated separately at B-6, B-2 and B-1, so neither leans on "
        f"the other",
        claims["bound_formulated_here"] is False
        and claims["bounds_violated"] == 0
        and claims["bound_violated_claimed"] is False
        and facts.named_words == claims["named_words"])
    checks.check(
        "F-6", f"FENCE SIX -- THE INSTANCE SCOPE, ENUMERATED RATHER THAN "
        f"GESTURED AT: {claims['instance_scope']} restrictions "
        f"({INSTANCE_SCOPE}), scope_generalisation = "
        f"{claims['scope_generalisation']}, and {claims['not_tested_here']} "
        f"instruments are named as NOT run here ({NOT_TESTED_HERE}); the "
        f"{claims['scoped_words']} scoped headline words "
        f"{SCOPED_HEADLINE_WORDS} each name something narrower than they "
        f"suggest",
        claims["instance_scope"] == len(INSTANCE_SCOPE)
        and claims["instance_scope"] == INSTANCE_SCOPE_COUNT
        and claims["instance_scope"] > 0
        and claims["scope_generalisation"] is False
        and claims["not_tested_here"] == len(NOT_TESTED_HERE)
        and claims["not_tested_here"] > 0
        and facts.scoped_words == claims["scoped_words"])

    # --- G: THE NOTE, THE FENCE AND THE EXACTNESS HYGIENE -------------------
    checks.check(
        "G-1", f"the note is readable at {NOTE_PATH.name} (source: "
        f"{facts.note_source}; NOTE_SOURCE_REQUIRED = {NOTE_SOURCE_REQUIRED}) "
        f"and the N5 fence appears in it VERBATIM as a single line",
        (facts.note_source == "final"
         or (NOTE_SOURCE_REQUIRED == "any" and facts.note_source == "draft"))
        is claims["note_present"]
        and facts.scope == claims["scope"])
    checks.check(
        "G-2", f"sp.nsimplify appears {claims['nsimplify_calls']} times in "
        f"this runner's own source -- MEASURED, not promised -- so no rational "
        f"tolerance can zero the two-pin residual, zero the pin-order "
        f"difference, collapse the compounding comparison or turn the "
        f"refutation's exact minors into false proportionality",
        facts.nsimplify_calls == claims["nsimplify_calls"])
    checks.check(
        "G-3", f"and {claims['float_literals']} float literals appear in that "
        f"same source with EXACTLY {claims['float_calls']} float call site, "
        f"both MEASURED by an AST walk rather than by a text search -- so "
        f"every decimal in this note is display-only and no verdict predicate "
        f"anywhere in this file consumes anything but an exact rational",
        facts.float_literals == claims["float_literals"]
        and facts.float_calls == claims["float_calls"])
    return checks


# ---------------------------------------------------------------------------
# THE MEASURED REPORT
# ---------------------------------------------------------------------------
def report_measured(facts: Facts, elapsed_ns: int) -> None:
    print("MEASURED")
    print(f"  elapsed: {elapsed_ns // 1000000000}s")
    print(f"  repair source context {facts.source_base}")
    print(f"  authority {facts.authority}")
    print(f"  note source: {facts.note_source} "
          f"(NOTE_SOURCE_REQUIRED = {NOTE_SOURCE_REQUIRED}; exact final note "
          f"bytes are required)")
    print(f"  imposed {facts.imposed}, registered {facts.registered}, "
          f"adopted {facts.adopted}, gravity structures NOT SUPPLIED "
          f"{facts.unsupplied}, readings {facts.readings}")
    print(f"  historical context label (not an input): {HISTORICAL_CONTEXT_LABEL}")
    bench = facts.bench
    print("  THE BENCH, READ THROUGH THE REVIEWED EXTRACTED HELPER")
    print(f"    {bench.tag}: N {bench.size}, T {bench.width}, c {bench.core}, "
          f"tstar {bench.tstar}, lx {bench.extent}, free levels "
          f"{bench.free_levels}")
    print(f"    pin rows {bench.slot_a_rows} at slot {SLOT_A}, "
          f"{bench.slot_b_rows} at slot {SLOT_B}, readout rows "
          f"{bench.read_rows} at level {READ_LEVEL}")
    joint = facts.joint
    print("  THE JOINT-PIN INSTRUMENT")
    print(f"    proposed reading: {PROPOSED_READING}")
    print(f"    {joint.outcomes} doubly-pinned + {joint.single_pins} single "
          f"pins + base = {joint.environments} environments; shared cache "
          f"{joint.cache_environments}; support complete "
          f"{joint.support_complete}")
    print(f"    joint-weight normalisations: forward {joint.sum_forward}, "
          f"reversed {joint.sum_reversed} (EXACT)")
    print(f"    two-pin residual FORWARD : nonzero {joint.nonzero_forward}/"
          f"{bench.extent}, signs {joint.signs_forward}, sum "
          f"{joint.sum_residual_forward}, numerator digits "
          f"{joint.numerator_digits_forward}")
    print(f"      {joint.display_forward} (DISPLAY ONLY)")
    print(f"    two-pin residual REVERSED: nonzero {joint.nonzero_reversed}/"
          f"{bench.extent}, signs {joint.signs_reversed}, sum "
          f"{joint.sum_residual_reversed}, numerator digits "
          f"{joint.numerator_digits_reversed}")
    print(f"      {joint.display_reversed} (DISPLAY ONLY)")
    print(f"    two-pin mixture identity holds: {joint.identity_holds}")
    print("    THE SINGLE-PIN COMPARISON CENSUS, RE-MEASURED FROM THIS CACHE")
    for slot in SINGLE_PIN_SLOTS:
        tag = " <- HISTORICAL CACHE FINGERPRINT" if slot == MID_SLOT else ""
        print(f"      slot {slot}: {joint.single_display[slot]} "
              f"(DISPLAY ONLY){tag}")
    print(f"      Historical cache mid-slot display {HISTORICAL_MID_SLOT_DISPLAY}")
    print("    THE COMPOUNDING, AND THE HONEST HALF OF IT")
    for key in sorted(joint.compound_componentwise, key=lambda k: (k[1], k[0])):
        print(f"      {key[0]} vs single slot {key[1]}: component magnitudes "
              f"strictly larger in {joint.compound_componentwise[key]}/"
              f"{bench.extent}; 10x l1 {joint.compound_l1_tenfold[key]}; 100x l1 "
              f"{joint.compound_l1_hundredfold[key]}; 1x l1 "
              f"{joint.compound_l1_strict[key]}; 200x excess narrow "
              f"{joint.compound_l1_narrow[key]}")
    print(f"      LATER PIN DOMINATES: {LATER_PIN_DOMINATES} -- the slot-"
          f"{SLOT_B} single pin already carries essentially the whole two-pin "
          f"residual")
    order = facts.order
    print("  THE PROPOSED FACTORIZATION ORDER")
    print(f"    {order.differing}/{order.entries} entries differ; "
          f"factorization_order_dependent {order.dependent}; structural "
          f"actions differing {order.structural_differing}/{order.entries}; "
          f"structural action commutes {order.structural_commutes}; max at outcome "
          f"{order.max_outcome}, display {order.max_display} (DISPLAY ONLY), "
          f"digits ({order.max_numerator_digits}, "
          f"{order.max_denominator_digits})")
    print(f"    max |w_fwd - w_rev| exact: {order.max_value}")
    print(f"    ordered residuals differ in {order.split_nonzero}/"
          f"{bench.extent} components, sum {order.split_sum}, displays "
          f"{order.split_display} (DISPLAY ONLY)")
    print(f"    single-readout 16-weight system: shape {order.restore_shape}, "
          f"ranks {order.restore_ranks}, solvable {order.restore_solvable} -- "
          f"no affine inconsistency detected here")
    alphabet = facts.alphabet
    print("  THE EXTENDED ALPHABET")
    print(f"    class values {tuple(str(v) for v in alphabet.class_values)}, "
          f"outcomes {alphabet.outcomes}, support complete "
          f"{alphabet.support_complete}")
    print(f"    six-context stack: shape {alphabet.stack_shape}, ranks "
          f"{alphabet.stack_ranks}, common twenty-weight exists "
          f"{alphabet.common_exists}")
    print(f"    normalization-row relations {alphabet.normalization_relations}, "
          f"exact {alphabet.normalization_relations_exact}, coefficient-rank "
          f"ceiling {alphabet.coefficient_rank_ceiling}; no outcome threshold")
    print(f"    raw A.T A invertible by rung "
          f"{alphabet.raw_gram_invertible}; pivot-basis C.T C invertible "
          f"{alphabet.pivot_basis_gram_invertible}")
    for size, shape, ranks in zip(SERIES_RUNGS, alphabet.series_shapes,
                                  alphabet.series_ranks):
        print(f"    series rung {size:>2} outcomes: shape {shape}, ranks "
              f"{ranks} -> "
              f"{'CONSISTENT' if ranks[0] == ranks[1] else 'INCONSISTENT'}")
    print("  THE REFUTATION OF THE CLASS-INVARIANT CONTRADICTION CONJECTURE")
    print(f"    left-cokernel dimensions {alphabet.cokernel_dimensions} -- NOT "
          f"one-dimensional, so a representative is required")
    print(f"    Riesz column-basis sizes {alphabet.column_basis_sizes}; "
          f"A^T r == 0 exactly {alphabet.riesz_orthogonal}; r.b nonzero "
          f"{alphabet.riesz_pairs_with_rhs}")
    for pair, flag, nonzero, residue in zip(
            PROPORTIONALITY_PAIRS, alphabet.pairwise_not_proportional,
            alphabet.pairwise_nonzero_minors, alphabet.certificate_residues):
        print(f"    r_{pair[0]} vs r_{pair[1]}: NOT proportional {flag}; "
              f"{nonzero}/{alphabet.pairwise_total_minors} exact 2 x 2 minors "
              f"nonzero; row-{CERTIFICATE_ROWS} numerator = {residue} mod "
              f"{CERTIFICATE_MODULUS}")
    print(f"    CONJECTURE REFUTED: {CONJECTURE_REFUTED} -- correction "
          f"{CORRECTION_NUMBER}")
    for statement in WEAKER_STATEMENT_SURVIVING:
        print(f"    weaker statement left standing: {statement}")
    print("  THE SIX FENCES, AND EACH IS A MEASURED CONSTANT")
    print(f"    F1 the reading is PROPOSED: {PROPOSED_READING}; halves "
          f"{JOINT_IDENTIFICATION_HALVES}; which half fails is OPEN "
          f"{WHICH_HALF_FAILS_IS_OPEN}")
    print(f"    F2 proposed-factorization order-dependence is CLASSICALLY POSSIBLE; mechanisms "
          f"{CLASSICAL_ORDER_MECHANISMS}; priority claimed "
          f"{ORDER_AXIS_PRIORITY_CLAIMED}; licensed phrase "
          f"'{LICENSED_PHRASE}' unchanged {LICENSED_PHRASE_UNCHANGED_FROM_PARENT}")
    print(f"    F3 alphabet tested at {ALPHABET_OUTCOMES_TESTED} outcomes; NOT "
          f"tested: {UNTESTED_ALPHABET_REFINEMENTS}; exact normalization "
          f"relations {NORMALIZATION_ROW_RELATIONS}, coefficient-rank ceiling "
          f"{COEFFICIENT_RANK_CEILING}, outcome threshold claimed "
          f"{OUTCOME_COUNT_THRESHOLD_CLAIMED}")
    print(f"    F4 the series is {SERIES_POINTS_DISPLAYED} DISPLAYED points; "
          f"rank-growth law claimed {RANK_GROWTH_LAW_CLAIMED}; extrapolation "
          f"{EXTRAPOLATION_CLAIMED}")
    print(f"    F5 bound formulated here {BOUND_FORMULATED_HERE}; bounds "
          f"violated {BOUNDS_VIOLATED}; words {NAMED_PHYSICS_WORDS}")
    print(f"    F6 instance scope {INSTANCE_SCOPE}; NOT tested here "
          f"{NOT_TESTED_HERE}")
    print("  READINGS, AND EACH IS A READING")
    for reading in READINGS:
        print(f"    {reading}")
    print(f"  nsimplify calls in this source: {facts.nsimplify_calls}; float "
          f"literals: {facts.float_literals}; float call sites: "
          f"{facts.float_calls} -- the single display helper")
    print("  NOT CLAIMED: NO GRAVITY. WRITING TWO RECORDS AT ONCE IS A DOUBLE "
          "SUBSTITUTION AND NOT A JOINT MEASUREMENT. THE STRUCTURAL ACTION "
          "COMMUTES; ONLY THE PROPOSED FACTORIZATIONS ARE ORDER-DEPENDENT. THE ORDER AXIS "
          "IS NOT CLAIMED NEW. TWENTY OUTCOMES DO NOT EXHAUST THE CLASSICAL "
          "OUTCOME SPACE. THE RANK-GROWTH PATTERN IS THREE DISPLAYED POINTS "
          "AND NOT A LAW. THE W9 FORMATION-WEIGHT READING IS PROPOSED AND NOT "
          "IDENTIFIED. NO BOUND IS FORMULATED HERE AND NONE IS VIOLATED. NO "
          "CLASSICAL NO-GO. NO GENERIC-PARAMETER THEOREM. NO CONTINUUM. THE "
          "READINGS ARE READINGS.")
    print()


N5_FENCE = """N5: per_element: THE STRUCTURAL DOUBLE-RECORD ACTION IS ONE SIMULTANEOUS DICTIONARY SUBSTITUTION; REVERSING INSERTION ORDER CHANGES ZERO OF SIXTEEN SUBSTITUTED MATRICES.
per_site: THE TWO PROPOSED CHAIN-RULE FACTORIZATION ARRAYS ARE COMPONENTWISE NONNEGATIVE, EACH SUMS EXACTLY TO ONE, AND THEY DIFFER IN SIXTEEN OF SIXTEEN WEIGHTS; THEIR MIXTURE RESIDUALS ARE NONZERO IN FOUR OF FOUR COMPONENTS.
per_mode: IN THE STATED l1 COMPARISON, THE SLOT-4 SINGLE PIN ALREADY CARRIES ALL BUT A SUB-PERCENT EXCESS OF THE TWO-PIN RESIDUAL; THE SINGLE-READOUT SIXTEEN-WEIGHT RESTORING SYSTEM IS REAL-AFFINE SOLVABLE BECAUSE rank(A) = rank([A|b]) = 4, AND NONNEGATIVITY AND MULTI-CONTEXT EXCLUSION REMAIN OPEN.
per_block: THE SIX-CONTEXT TWENTY-OUTCOME STACK IS INCONSISTENT AT RANKS (12, 13), REPRODUCING THE FINITE SERIES (4, 5), (8, 9), (12, 13); SIX EXACT NORMALIZATION-ROW RELATIONS CAP COEFFICIENT RANK AT 19, SO NO OUTCOME-COUNT THRESHOLD IS CLAIMED.
lattice_wide: THE THREE FIXED-ROW-COORDINATE EUCLIDEAN RESIDUALS ARE PAIRWISE NONPROPORTIONAL, REFUTING ONLY THE DECLARED REPRESENTATIVE-LEVEL INVARIANCE CONJECTURE; THIS IS NOT A REPRESENTATION-INVARIANT OBSTRUCTION, UNIVERSAL DEPENDENCY-ORDER THEOREM, CLASSICAL NO-GO, CONTINUUM RESULT, DYNAMICS, OR GRAVITY."""


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS, default="")
    parser.add_argument(
        "--list-mutations", action="store_true",
        help="print the declared mutation names, one per line, and exit")
    arguments = parser.parse_args()
    if arguments.list_mutations:
        for name in MUTATIONS:
            print(name)
        return 0
    mutation = arguments.mutation
    started_ns = time.monotonic_ns()

    # Every measurement happens once, before any mutation flag is consulted, so
    # a mutation can only rewrite a CLAIM.  No family can cascade into another
    # because no gate feeds a measurement.
    facts = measure()
    elapsed_ns = time.monotonic_ns() - started_ns

    checks = build_checks(facts, build_claims(""))
    if mutation:
        raw = checks.families()
        checks = build_checks(facts, build_claims(mutation))
        mutated = checks.families()
        target = MUTATION_GATE[mutation]
        changed = {family for family in raw if raw[family] != mutated[family]}
        if changed - {target} or mutated[target]:
            raise AssertionError("mutation did not fail exactly its own gate")

    report_measured(facts, elapsed_ns)
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
