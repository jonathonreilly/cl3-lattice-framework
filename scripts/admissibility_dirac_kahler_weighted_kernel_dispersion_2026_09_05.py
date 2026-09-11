#!/usr/bin/env python3
"""BLOCK 213 -- THE WEIGHTED-KERNEL DISPERSION: THE DIRAC-KAHLER LANE KERNEL
COMPLETED BY THE CURVED CELL FORM, ITS EXACT SQUARED SYMBOL ON THE PERIODIC
(4,4) AND (4,2,2) BENCHES, AND THE CONE = THE METRIC'S CONE HYPOTHESIS TESTED
EXACTLY -- UNDER THE GRADED ASSEMBLY THE CONE IS THE UNION OF THE TWO HODGE
READINGS OF THE CELL FORM, WHICH COINCIDE EXACTLY ON A CODIMENSION-ONE LOCUS
IN EIGHT OF THE SIXTY-FOUR SIGN CELLS (WHERE THE CONE IS ONE METRIC'S CONE
AND THE SYMBOL IS STILL NOT SCALAR) AND NOWHERE ELSE OFF FLAT; UNDER THE
OVERLAP ASSEMBLY IT IS A NON-HODGE PAIR OF CONES AT EVERY NAMED ORIGINAL
WITNESS MEASURED.

WHAT THIS BLOCK IS.  R5 named the weighted-kernel construction as the design
task: complete the lane kernel K = d - d^T by the curved cell form H in Block
the recovered Block 107 / Block 201 pattern Q = m H + H d - d^T H at m = 0 and periodic
closure, K_H = H d - d^T H, and ask whether the exact squared symbol's
characteristic cone is the null cone of the cell metric.  Two supplied
assemblies of ONE cell form into H exist (Block 105's onsite_hodge, anchored
at even sites, and its overlap_hodge, the recovered 2^-d-weighted all-anchor
average); two squared-symbol readings exist (the Euclidean form -K_H^2 and
the H-pencil -(H^-1 K_H)^2 = d delta + delta d).  All four reduce EXACTLY to
R5's flat kernel at the flat cell, and the flat symbol sum_d sin^2 k_d is
reproduced as the control on both benches.  Everything is exact: period-2
Bloch matrices over exact roots of unity, verified entry for entry against
the direct bench matrices.

  (i) THE PRINCIPAL PART, EXACTLY.  With K_H,B(z) = i eps M(kappa) + O(eps^2)
      and M = H0 D(kappa) + D(kappa)^T H0, both assemblies preserve grade
      parity, so M = [[0, B], [B^T, 0]] with B(kappa) = H_e D_eo + D_oe^T H_o
      a 2^(d-1) x 2^(d-1) matrix linear in kappa.  The characteristic cone
      {det B = 0} is reading-independent.  The principal symbols are
      M^2 (form) and (H0^-1 M)^2 (pencil), both block-diagonal in B B^T and
      H_e^-1 B H_o^-1 B^T.

 (ii) THE ONSITE CONE LEMMA (general, symbolic D).  For any block-diagonal
      cell form D = diag(D0, D1, D2, D3), det B = +D3 (k^T D1 k)(k^T E adj(D2) E k)
      in three directions and det B = -D2 (k^T D1 k) in two.  The pencil
      principal symbol is block-diagonal by form degree with the EXACT
      branches k^T G1 k (G1 = D1/D0) and k^T G2 k (G2 = D3 E D2^-1 E) --
      the two Hodge readings of the degree blocks -- plus, in three
      directions, two transverse 2-form branches that are algebraic in k.
      D0 never enters the cone; the volumes enter the branches only through
      D1/D0 and D3 D2^-1.

(iii) THE OVERLAP CONE (general, symbolic h).  The folded overlap H0 is
      h0 I + two-flip couplings 2 h_f, with h0 = (v0 + 3 v1 + 3/v0 + 1/v1)/8 and
      h_f = -(s_f0 v1 g0 + s_f1 g1 / v0)/8 on the Block 211 family; the cone is
      the union of the two quadratic cones Q+ and Q- displayed below, which
      differ by the sign of the t-y plane terms, and in two directions the
      single cone h0 (kt^2 + kx^2) + 4 h_tx kt kx with the effective shear
      c_K = 2 c v^2 / (3 v^2 + 1 - c^2 (v^2 + 1)) -- the same sign as, but a
      different magnitude from, the Hodge reading's shear c.

 (iv) THE HYPOTHESIS, ANSWERED -- AND THE FIRST DRAFT's ANSWER CORRECTED.
      On the four class representatives' (t, u) chart the proportionality
      ideal of (G1, G2) has lex Groebner basis {t (u^2 + 1), u (u^2 + 1)}, so
      there G1 ~ G2 only at flat.  But the weighted kernel is NOT invariant
      under Block 211's corner-sign gauge (E d E is not d), so the four
      representatives do not speak for the sixty-four sign cells.  The census
      over all sixty-four at symbolic (v0, g0, v1, g1) finds forty-eight cells
      coinciding only at flat and SIXTEEN carrying a coincidence CURVE, in
      closed form: with M1 = I - g0 S0, M2 = I - g1 S1 and E = diag(1,-1,1),
      G1 ~ G2 iff P = M1 E M2 E ~ I, and P = (1 - 2 g0 g1) I + (g1 - g0 -
      pi0 g0 g1) S0 when S1 = -E S0 E (rule A: curve g0 = g1/(1 + pi0 g1),
      positive and PD-solvable in all eight rule-A cells), P = (1 + 2 g0 g1) I
      - (g0 + g1 - pi0 g0 g1) S0 when S1 = +E S0 E (rule B: no positive
      point).  ON THE LOCUS THE GRADED det B IS PROPORTIONAL TO (k^T G1 k)^2,
      and every H-pencil branch is a constant multiple of k^T G1 k with the
      constants {1, mu, 1/(1 - g1^2) x2}, mu = (1 + 2 pi0 g1)/((1 - pi0 g1)
      (1 + pi0 g1)^3) never 1 off flat -- so the symbol is still not scalar.
      Off the locus the graded cone is the union of two DISTINCT quadrics and
      the exact discrepancy is the closed form above; under the overlap
      assembly the cone is a non-Hodge pair at every point measured, the
      locus included.  This finite scan is not a universal non-scalarity
      theorem: the exact positive-definite curved point with opposite offset
      signs, g0=3/8, g1=1/3, v0=sqrt(110)/12 and
      v1=16sqrt(110)/165 has scalar overlap H0 and pencil |k|^2 I.  Two
      witnesses over QQ(sqrt 6) realise the graded locus on the family with
      every cone, reading and branch constant RATIONAL; their det-B
      prefactors are respectively 8/9 and 3/4.

  (v) SHEAR REGISTRATION (the #7970 question).  The shears g0, g1 enter the
      cone in both assemblies (exact nonzero derivatives); the diagonal moduli
      enter only as branch scales (graded) or through h0 and the h_f sums
      (overlap), and at zero shear the overlap pencil symbol is R5's for EVERY
      volume pair.  Recorded as a named tension with the matter-side
      no-shear-response result; not resolved here.

THE WORDS ARE FENCED BEFORE THE FIRST NUMBER IS READ.  'SYMBOL' names the
exact 2^d x 2^d Bloch matrix of a finite antisymmetric kernel on a periodic
bench.  'CONE' names the zero set of det B(kappa), a homogeneous polynomial.
'METRIC' names one of two declared rational readings of the cell form's
degree blocks.  'DISPERSION' names the eigenvalue branches of a 4 x 4 or
8 x 8 exact matrix.  None names a spacetime, a light cone, a propagator, a
dynamics, a gravity or a continuum.

SCOUT-GRADE FINITE EXACT LINEAR ALGEBRA ON ONE CELL FORM, NOT A SPACETIME AND
NOT A DYNAMICS -- Block 211's fence, inherited verbatim.

GATES
  A  SOURCE-INPUT CLOSURE: the bounded recovery helper and current Block 105
     source import, every non-self runtime/citation input matches a fixed
     SHA-256 literal, and every declared input is readable.  Historical parent
     bodies are recovery evidence, not live authority.
  B  THE BANNER AND THE FENCE: six imposed objects, ZERO registered and ZERO
     adopted; gravity, dynamics, a spacetime cone, a decided assembly and
     licensed readings ALL declared NOT CLAIMED as measured constants.
  C  THE CONSTRUCTION'S FIDELITY TO THE CHAIN: the lane kernels are Block
     201's and Block 209's spin-diagonalised shadows; K = d - d^T with d^2 = 0
     in Block 201's grading; the assemblers reproduce Block 105's onsite and
     overlap Hodges and Block 201's fork Hodge digit for digit; the cell forms
     are Block 211's solved D with its block formulas; the flat cell gives
     H = I and K_H = K.
  D  THE R5 CONTROL: the flat symbol is sum_d sin^2 k_d times the identity as
     an exact polynomial identity, and the bench multisets on (4,4) and
     (4,2,2) are exactly {sum_d sin^2(2 pi m_d / N_d)}.
  E  THE EXACT SPECTRA AT THE WITNESSES: Bloch union = direct bench, all four
     constructions, both benches; translation covariance measured; the PD
     boundary edge case.
  F  THE PRINCIPAL PART AND THE CONE: the expansion and the onsite lemma and
     the overlap cone, symbolic; the two-direction branches, symbolic in
     (c, v); the three-direction branch identification at every witness;
     scalar-or-not at the listed witnesses plus the explicit overlap scalar
     counterexample; the coincidence theorem (chart
     fail-closed, sixty-four-cell census, closed form); the locus witnessed
     over QQ(sqrt 6) and proved along the curve.
  G  SHEAR REGISTRATION: exact, separately for shear and for the diagonal
     moduli, and the tension recorded.
  H  THE SCOPE FENCES, EACH A MEASURED CONSTANT.
  I  the note at its final path, the N5 fence byte-identical, nsimplify and
     float-literal and float-call counts all ZERO in this file's own source.

BASELINE EXPECTATION: A through I PASS, 36 checks, exit 0.

MUTATIONS
  THIRTY-SIX declared mutations, each rewriting ONE CLAIM and flipping EXACTLY
  ONE FAMILY; every measurement happens once, before any mutation flag is
  read.  Per-family census A 2, B 6, C 5, D 2, E 3, F 8, G 3, H 4, I 3, for
  both checks and mutations.

RUNNING
  python3 scripts/admissibility_dirac_kahler_weighted_kernel_dispersion_2026_09_05.py
  python3 ... --list-mutations
  python3 ... --mutation claim_cone_is_metric_cone
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import itertools
import sys
import time
from dataclasses import dataclass
from pathlib import Path

import sympy as sp
from sympy import QQ
from sympy.polys.domains import QQ_I
from sympy.polys.matrices import DomainMatrix

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

# The original runner imported historical Blocks 201, 209, and 211 through
# modules that are absent from the correction base.  The recovery helper below carries
# only the definitions this bounded computation actually calls.  The complete
# historical source bodies are preserved in the dedicated recovery packet.
try:
    import admissibility_dirac_kahler_weighted_kernel_released7981_7988_fixtures_2026_09_10 as fixtures
    FIXTURE_IMPORT_AVAILABLE = True
except ModuleNotFoundError:                            # pragma: no cover
    fixtures = None
    FIXTURE_IMPORT_AVAILABLE = False
try:
    import admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_2026_08_14 as b105
    B105_IMPORT_AVAILABLE = True
except ModuleNotFoundError:                            # pragma: no cover
    b105 = None
    B105_IMPORT_AVAILABLE = False
MACHINERY_IMPORT_AVAILABLE = bool(
    FIXTURE_IMPORT_AVAILABLE and B105_IMPORT_AVAILABLE and fixtures is not None)
b201 = fixtures.b201 if fixtures is not None else None
b209 = fixtures.b209 if fixtures is not None else None
b211 = fixtures.b211 if fixtures is not None else None

FINAL_NOTE_NAME = (
    "ADMISSIBILITY_DIRAC_KAHLER_WEIGHTED_KERNEL_DISPERSION_BOUNDED_THEOREM_"
    "NOTE_2026-09-05.md"
)
NOTE_PATH = ROOT / "docs" / FINAL_NOTE_NAME
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"

# A LITERAL TUPLE OF PLAIN STRING CONSTANTS.  The cache parser AST-reads this
# and rejects computed elements, so nothing here is built by concatenation.
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_WEIGHTED_KERNEL_DISPERSION_BOUNDED_THEOREM_NOTE_2026-09-05.md",
    "scripts/admissibility_dirac_kahler_weighted_kernel_released7981_7988_fixtures_2026_09_10.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "scripts/admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_2026_08_14.py",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
)
SELF_NOTE_INPUT = AUDIT_INPUT_PATHS[0]

AUDIT_TIMEOUT_SEC = 180
CORRECTION_SOURCE_BASE = "1157173587fde42555d36659954e71c544e23312"
EXPECTED_INPUT_SHA256 = (
    ("scripts/admissibility_dirac_kahler_weighted_kernel_released7981_7988_fixtures_2026_09_10.py", "082c88ae8d05df21874e90cef3a8a0784116a1eb6957d119709ef6838486a9ef"),
    ("docs/ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md", "9a615a79511ffc0dac0d1cf54388153604ce7c341496654fd709ed8873302a33"),
    ("scripts/admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_2026_08_14.py", "5499cc2c1a75f19e07b717aeb6c9ef7779c45e1c5757d84701c5d88ca92bf445"),
    ("docs/MINIMAL_AXIOMS_2026-06-29.md", "93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753"),
    ("docs/audit/data/axiom_premise_nodes.json", "615f13aaa70e82d50cdf1a8aa479eb40d6ce70a3bb7b152ac63fd88bee341f37"),
)

MUTATIONS = (
    "break_source_input_hash",
    "break_source_input_readability",
    "claim_objects_registered",
    "claim_gravity_supplied",
    "claim_symbol_is_dynamics",
    "claim_cone_is_spacetime_cone",
    "claim_assembly_selected",
    "claim_readings_licensed",
    "break_lane_kernel_fidelity",
    "break_three_direction_shadow",
    "break_assembler_fidelity",
    "break_cell_form_reconciliation",
    "break_flat_cell_identity",
    "break_flat_symbol_identity",
    "break_flat_bench_multiset",
    "break_bloch_bench_agreement",
    "break_witness_spectra",
    "break_boundary_edge_case",
    "break_onsite_cone_lemma",
    "break_overlap_cone_formula",
    "break_two_dim_branches",
    "break_three_dim_branch_identification",
    "claim_principal_part_scalar",
    "claim_cone_is_metric_cone",
    "break_coincidence_census",
    "break_coincidence_locus",
    "break_shear_registration",
    "claim_volume_registration",
    "drop_tension_record",
    "break_scout_grade_fence",
    "claim_assembly_decided",
    "claim_hodge_reading_selected",
    "break_instance_scope",
    "drop_n5_fence",
    "break_nsimplify_absence",
    "break_float_absence",
)

MUTATION_GATE = {
    "break_source_input_hash": "A",
    "break_source_input_readability": "A",
    "claim_objects_registered": "B",
    "claim_gravity_supplied": "B",
    "claim_symbol_is_dynamics": "B",
    "claim_cone_is_spacetime_cone": "B",
    "claim_assembly_selected": "B",
    "claim_readings_licensed": "B",
    "break_lane_kernel_fidelity": "C",
    "break_three_direction_shadow": "C",
    "break_assembler_fidelity": "C",
    "break_cell_form_reconciliation": "C",
    "break_flat_cell_identity": "C",
    "break_flat_symbol_identity": "D",
    "break_flat_bench_multiset": "D",
    "break_bloch_bench_agreement": "E",
    "break_witness_spectra": "E",
    "break_boundary_edge_case": "E",
    "break_onsite_cone_lemma": "F",
    "break_overlap_cone_formula": "F",
    "break_two_dim_branches": "F",
    "break_three_dim_branch_identification": "F",
    "claim_principal_part_scalar": "F",
    "claim_cone_is_metric_cone": "F",
    "break_coincidence_census": "F",
    "break_coincidence_locus": "F",
    "break_shear_registration": "G",
    "claim_volume_registration": "G",
    "drop_tension_record": "G",
    "break_scout_grade_fence": "H",
    "claim_assembly_decided": "H",
    "claim_hodge_reading_selected": "H",
    "break_instance_scope": "H",
    "drop_n5_fence": "I",
    "break_nsimplify_absence": "I",
    "break_float_absence": "I",
}
MUTATED_FAMILIES = "ABCDEFGHI"


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
# A. source-input closure
# ---------------------------------------------------------------------------
def sha256_path(path: str) -> str:
    target = ROOT / path
    return hashlib.sha256(target.read_bytes()).hexdigest() if target.is_file() else ""


def audit_inputs_readable() -> tuple:
    missing = tuple(
        path for path in AUDIT_INPUT_PATHS
        if path != SELF_NOTE_INPUT and not (ROOT / path).is_file())
    return len(AUDIT_INPUT_PATHS) - 1 - len(missing), missing


@dataclass(frozen=True)
class AuthorityCertificate:
    source_base: str
    fixed_source_inputs: bool
    machinery_import_available: bool
    inputs_readable: int
    inputs_missing: tuple
    input_hashes: tuple


def authority_certificate() -> AuthorityCertificate:
    readable, missing = audit_inputs_readable()
    hashes = tuple((path, sha256_path(path)) for path in AUDIT_INPUT_PATHS)
    actual_fixed = tuple((path, sha256_path(path)) for path, _ in EXPECTED_INPUT_SHA256)
    return AuthorityCertificate(
        CORRECTION_SOURCE_BASE,
        actual_fixed == EXPECTED_INPUT_SHA256,
        MACHINERY_IMPORT_AVAILABLE,
        readable,
        missing,
        hashes)


# ---------------------------------------------------------------------------
# B. the imposed objects and the NOT-CLAIMED keys, as measured literals
# ---------------------------------------------------------------------------
IMPOSED_OBJECTS = (
    "THE WEIGHTED KERNEL K_H = H d - d^T H, WHICH IS THIS BLOCK's FIRST NEW OBJECT: Block 107's / Block 201's completion Q = m H + H D_s - D_s^T H read at m = 0 and periodic closure, with d Block 201's graded raising part d_K = sum_g P_{g+1} K P_g of the eta-staggered lane kernel (eta_t = 1, eta_x = (-1)^t, and Block 209's eta_y = (-1)^(t+x) in three directions)",
    "THE TWO SUPPLIED ASSEMBLIES OF ONE CELL FORM INTO H: current Block 105's onsite_hodge (cells anchored at even sites, weight 1, the grade-diagonal assembly) and overlap_hodge (cells anchored at every site, weight 2^-d), extended from two to three directions by the same anchoring rule",
    "THE TWO SQUARED-SYMBOL READINGS: the Euclidean form -K_H^2 and the H-pencil -(H^-1 K_H)^2 = d delta + delta d with delta = H^-1 d^T H, which share the generalized eigenproblem K_H v = mu H v and therefore the characteristic cone",
    "THE PERIOD-2 BLOCH REDUCTION: the 2^d x 2^d Bloch matrix A_B(z)[c, c'] = sum_delta A[c, delta] z^delta of every period-2 operator, evaluated at exact roots of unity z_d = exp(2 pi i m_d / N_d), m_d < N_d / 2, whose union over supercell momenta is the bench spectrum; the first-order matrix D(kappa) and the bipartite block B(kappa) = H_e D_eo + D_oe^T H_o whose determinant's zero set is the cone",
    "THE TWO CANDIDATE CELL METRICS, READ OFF THE DEGREE BLOCKS BY BLOCK 209's HONEST-LIFT PATTERN D3(g, V) = diag(V, V g^-1, E g E / V, 1/V): G1 = D1 / D0 (the degree-0/1 reading) and G2 = D3 E D2^-1 E (the degree-2/3 reading), with E = diag(1, -1, 1) Block 209's wedge signature; equal at the flat point and, on the Block 211 family, on an explicit codimension-one locus of eight sign cells and nowhere else",
    "THE BOUNDED RECOVERED CONSTRUCTION DEFINITIONS: Block 211 face_system, solve_pinned, branch_moduli, diagonal_point, witnesses, chart and sixty-four sign cells; current Block 105 shear_hodge and two assemblies; Block 201 lane_kernel, covariant_kernel, site_sign_equivalent, raising_part and fork_hodge; and Block 209 omega, generators, corners and degree indices; their source paths and hashes are fixed inputs or recorded in the helper",
)
REGISTERED_OBJECTS = ()
ADOPTED_OBJECTS = ()
GRAVITY_SUPPLIED_CLAIMED = False
SYMBOL_IS_DYNAMICS_CLAIMED = False
CONE_IS_SPACETIME_CONE_CLAIMED = False
ASSEMBLY_SELECTED_CLAIMED = False
PROPAGATOR_CLAIMED = False
CONTINUUM_LIMIT_CLAIMED = False
GENERIC_PARAMETER_THEOREM_CLAIMED = False
READINGS_LICENSED_CLAIMED = False
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
SCOPED_HEADLINE_WORDS = ("SYMBOL", "CONE", "METRIC", "DISPERSION")
UNNAMED_PHYSICS_WORDS = ("SPACETIME", "LIGHT CONE", "PROPAGATOR", "EINSTEIN")
READINGS = (
    "R1: that the characteristic cone is a light cone or a causal structure.  Measured: the zero set of det B(kappa), a homogeneous polynomial in three formal variables attached to a finite antisymmetric matrix.  No time, no signal, no causality.  Reading.",
    "R2: that the H-pencil reading is the physical propagator.  Measured: one of two declared squared-symbol readings of the same antisymmetric form; neither reading is selected by any premise.  Reading.",
    "R3: that the assembly is decided.  Measured: the fixed Block 105 source defines BOTH onsite and overlap, the recovered completion uses overlap, and no premise here chooses; the two give different cones and both are reported.  Reading.",
    "R4: that kernel-side shear registration is a gravitational shear response.  Measured: exact nonzero derivatives of a polynomial with respect to two rational parameters of one cell form.  The matter-side result it stands in tension with is itself conditional (PR #7970).  Reading.",
    "R5: that the recovered Block 201 completion is physically selected.  Measured: its fork Hodge is reproduced exactly and its overlap assembly is one of the two supplied assemblies run here.  Reading.",
    "R6: that any of it generalises past this instance.  Measured: two periodic benches, one cell family, ten witnesses, two assemblies, two readings, one rule.  Reading.",
    "R7: that the coincidence locus is selected, preferred or physical.  Measured: a codimension-one algebraic locus in eight of sixty-four sign cells on which two DECLARED readings of one cell form agree; no premise here prefers it, the overlap assembly does not see it, and the symbol is not scalar on it.  Reading.",
)
HISTORICAL_CHECKER_RECORD = "RECOVERED-SUPPORT-NOT-CURRENT-AUTHORITY"

# ---------------------------------------------------------------------------
# THE EXPECTED VALUES, declared as literals so every claim below is auditable
# against the note without reading the code that measures it.
# ---------------------------------------------------------------------------
ZERO_RESIDUAL = 0
HALF = sp.Rational(1, 2)
BENCH_2D = (4, 4)
BENCH_3D = (4, 2, 2)
FORK_EXTENT = (8, 4)

# --- C: THE CONSTRUCTION'S FIDELITY -----------------------------------------
LANE_2D_NNZ = 64
LANE_3D_NNZ = 32                        # the extent-2 directions carry NO link
LANE_3D_LINKS_SCANNED = 48
LANE_3D_BAD_LINKS = 0
SPIN_NONSCALAR_2D = 0
FLAT_H_IS_IDENTITY = True
FLAT_KERNEL_IS_R5 = True
WITNESS_NAMES = ("flat", "W1", "W2", "W3", "mixed", "near_boundary",
                 "boundary", "honest_face")
WITNESS_COUNT = 10                      # eight rational + two QQ(sqrt 6) locus witnesses
PD_WITNESSES = ("flat", "W1", "W2", "W3", "mixed", "near_boundary",
                "honest_face", "L+-", "L-+")
COMPATIBLE_RANKS = (32, 32)

# --- D: THE R5 CONTROL --------------------------------------------------------
FLAT_SYMBOL_FORM = "sum_d sin^2 k_d = sum_d -(z_d - 1/z_d)^2 / 4"
FLAT_MULTISET_2D = ((0, 4), (1, 8), (2, 4))
FLAT_MULTISET_3D = ((0, 8), (1, 8))

# --- E: THE EXACT SPECTRA -----------------------------------------------------
ASSEMBLIES = ("onsite", "overlap")
READINGS_NAMES = ("form", "pencil")
# W1's own (4,4) spectra, the overlap assembly, declared exactly.
W1_OVERLAP_PENCIL_2D = ((0, 4), (1, 8), (sp.Rational(1922, 1081), 4))
# THE PD BOUNDARY IS A THREE-DIRECTION BOUNDARY: at g0 = g1 = 1/2 all-plus the
# triangle determinant (1 + g)^2 (1 - 2g) vanishes, so the onsite H on (4,2,2)
# is singular; the (4,4) bench carries the origin tx FACE, Block 105's
# shear_hodge at c = 1/2, whose 2 x 2 block has determinant v0^2/(1 - c^2) and
# is REGULAR (the two-direction PD condition is |c| < 1).  The first draft
# declared it singular on both benches, and its gate would have failed.
BOUNDARY_ONSITE_H_SINGULAR_3D = True
BOUNDARY_ONSITE_H_SINGULAR_2D = False

# --- F: THE PRINCIPAL PART AND THE CONE ---------------------------------------
# THE SIGN IS +D3 IN THREE DIRECTIONS AND -D2 IN TWO: the first draft declared
# -D3 and its gate would have failed had its baseline ever finished.
ONSITE_CONE_LEMMA_3D = "det B = +D3 * (k^T D1 k) * (k^T E adj(D2) E k)"
ONSITE_CONE_LEMMA_2D = "det B = -D2 * (k^T D1 k)"
ONSITE_PENCIL_BRANCHES_3D = ("k^T G1 k  (0-form sector, G1 = D1/D0)",
                             "k^T G2 k  (3-form sector, G2 = D3 E D2^-1 E)",
                             "two transverse 2-form branches: roots of a quadratic whose product is det(D2)/det(D1) (k^T D1 k)(k^T E D2^-1 E k)")
OVERLAP_H0_FORM = "h0 I + 2 h_f on the two-flip pairs, h0 = (v0 + 3 v1 + 3/v0 + 1/v1)/8, h_f = -(s_f0 v1 g0 + s_f1 g1 / v0)/8"
OVERLAP_CONE_PLUS = ("h0**2*kt**2 + h0**2*kx**2 + h0**2*ky**2 + 4*h0*htx*kt*kx + 4*h0*hty*kt*ky "
                     "+ 4*h0*hxy*kx*ky - 4*htx**2*ky**2 - 8*htx*hty*kx*ky - 8*htx*hxy*kt*ky "
                     "- 4*hty**2*kx**2 - 8*hty*hxy*kt*kx - 4*hxy**2*kt**2")
OVERLAP_CONE_MINUS = ("h0**2*kt**2 + h0**2*kx**2 + h0**2*ky**2 + 4*h0*htx*kt*kx - 4*h0*hty*kt*ky "
                      "+ 4*h0*hxy*kx*ky - 4*htx**2*ky**2 - 8*htx*hty*kx*ky + 8*htx*hxy*kt*ky "
                      "- 4*hty**2*kx**2 - 8*hty*hxy*kt*kx - 4*hxy**2*kt**2")
OVERLAP_CONE_2D = "h0*(kt**2 + kx**2) + 4*htx*kt*kx"
TWO_DIM_ONSITE_BRANCHES = ("(kt**2 - 2*c*kt*kx + kx**2)/(1 - c**2)",
                           "(kt**2 - 2*c*kt*kx + kx**2)/v**2")
TWO_DIM_OVERLAP_PENCIL = ("(c**2*(v**2 + 1) - 3*v**2 - 1)*((c**2*(v**2 + 1) - 3*v**2 - 1)*(kt**2 + kx**2) + 4*c*v**2*kt*kx)"
                          "/((c**2 - 1)*(c**2*(v**2 + 1)**2 - (3*v**2 + 1)**2))")
TWO_DIM_HODGE_CONE = "(kt**2 - 2*c*kt*kx + kx**2)/(1 - c**2)"
TWO_DIM_OVERLAP_EFFECTIVE_SHEAR = "2*c*v**2/(3*v**2 + 1 - c**2*(v**2 + 1))"
TWO_DIM_OVERLAP_SHEAR_DISCREPANCY = "-c*(1 - c**2)*(v**2 + 1)/(3*v**2 + 1 - c**2*(v**2 + 1))"
TWO_DIM_ONSITE_SCALAR_LOCUS = "v**2 = 1 - c**2"
W1_ONSITE_CONES = ("2*kt**2 - kt*kx - kt*ky + 2*kx**2 - kx*ky + 2*ky**2",
                   "3*kt**2 - 2*kt*kx + 2*kt*ky + 3*kx**2 - 2*kx*ky + 3*ky**2")
W1_OVERLAP_CONES = ("55*kt**2 - 16*kt*kx - 16*kt*ky + 55*kx**2 - 16*kx*ky + 55*ky**2",
                    "55*kt**2 - 16*kt*kx + 16*kt*ky + 55*kx**2 - 16*kx*ky + 55*ky**2")
PRINCIPAL_PART_SCALAR_AT_LISTED_CURVED_3D_WITNESSES = False
# THE COINCIDENCE THEOREM, IN THREE PARTS.  (1) On the four class
# representatives' (t, u) chart the ideal of the 2 x 2 minors of (vec G1,
# vec G2) has the lex Groebner basis below, whose only REAL zero is the flat
# point.  (2) BUT the weighted kernel is NOT invariant under Block 211's
# corner-sign gauge (E d E != d), so four representatives do not speak for the
# sixty-four sign cells: the census over all of them, at symbolic (v0, g0, v1,
# g1), finds forty-eight cells with coincidence only at flat and SIXTEEN cells
# carrying a coincidence CURVE.  (3) Closed form: with S0, S1 the two signed
# off-diagonal patterns (M1 = I - g0 S0, M2 = I - g1 S1) and E = diag(1, -1, 1),
# G1 ~ G2 iff P := M1(g0) E M2(g1) E ~ I, and
#     P = (1 - 2 g0 g1) I + (g1 - g0 - pi0 g0 g1) S0   when S1 = -E S0 E  (rule A),
#     P = (1 + 2 g0 g1) I - (g0 + g1 - pi0 g0 g1) S0   when S1 = +E S0 E  (rule B),
# so rule A gives the curve g0 = g1/(1 + pi0 g1), positive on the magnitude
# domain, and rule B the curve g0 = -g1/(1 - pi0 g1), with no positive point.
# Eight of the sixty-four cells therefore carry a positive-definite-solvable
# curve on which the graded cone IS one metric's cone.
COINCIDENCE_CHART_GROEBNER = ("t*(u**2 + 1)", "u*(u**2 + 1)")
COINCIDENCE_SOLUTIONS = ((0, 0),)
COINCIDENCE_CLASSES = 4
SIGN_CELLS = 64
COINCIDENCE_CENSUS = (                     # (lex Groebner basis in (g0, g1), cells, classes)
    ("(g0, g1)", 48, ((-1, -1), (-1, 1), (1, -1), (1, 1))),
    ("(g0*g1 + g0 - g1,)", 4, ((1, -1),)),
    ("(g0*g1 - g0 + g1,)", 4, ((-1, 1),)),
    ("(g0*g1 - g0 - g1,)", 4, ((1, 1),)),
    ("(g0*g1 + g0 + g1,)", 4, ((-1, -1),)),
)
COINCIDENCE_FLAT_ONLY_CELLS = 48
COINCIDENCE_CURVE_CELLS = 16
LOCUS_RULE_A = "S1 = -E S0 E (so pi1 = -pi0): g0 (1 + pi0 g1) = g1, i.e. g0 = g1/(1 + pi0 g1), positive on the magnitude domain"
LOCUS_RULE_B = "S1 = +E S0 E (so pi1 = pi0): g0 + g1 = pi0 g0 g1, i.e. g0 = -g1/(1 - pi0 g1) < 0 on the family's magnitude domain |g1| < 1: no positive point there"
LOCUS_RULE_A_CELLS = 8
LOCUS_RULE_B_CELLS = 8
LOCUS_POSITIVE_CELLS = 8
COINCIDENCE_ONLY_AT_FLAT_IN_EVERY_CELL = False
CONE_IS_ONE_METRIC_CONE_EVERYWHERE = False
CONE_IS_ONE_METRIC_CONE_ON_LOCUS = True
# THE TWO LOCUS WITNESSES, ONE PER POSITIVE RULE-A CLASS, over QQ(sqrt 6): no
# rational point with rational volumes exists on either curve below height
# 120, so the witnesses carry sqrt 6 in the volumes -- and every cone, every
# metric reading and every branch constant at them is RATIONAL.
LOCUS_WITNESS_NAMES = ("L+-", "L-+")
LOCUS_MU = (sp.Rational(32, 27), sp.Rational(27, 32))
LOCUS_DET_PREFACTORS = (sp.Rational(8, 9), sp.Rational(3, 4))
LOCUS_BRANCH_CONSTANTS = ((sp.Integer(1), sp.Rational(32, 27), sp.Rational(4, 3), sp.Rational(4, 3)),
                          (sp.Integer(1), sp.Rational(27, 32), sp.Rational(9, 8), sp.Rational(9, 8)))
LOCUS_BRANCH_CONSTANTS_SYMBOLIC = ("1", "(1 + 2 pi0 g1)/((1 - pi0 g1)(1 + pi0 g1)^3)",
                                   "1/(1 - g1^2)", "1/(1 - g1^2)")
LOCUS_MU_MINUS_ONE = "pi0 g1^3 (2 + pi0 g1)/((1 - pi0 g1)(1 + pi0 g1)^3)"
LOCUS_SYMBOL_SCALAR = False
# THE TRANSVERSE PAIR SPLITS INTO TWO QUADRATIC-FORM BRANCHES AT EXACTLY ONE
# CURVED RATIONAL WITNESS -- honest_face, where the offset-1 shear is zero and
# D2 is isotropic -- and stays an irreducible quadratic at the other five; the
# first draft declared it split nowhere, and its gate would have failed.
TRANSVERSE_SPLIT_RATIONAL_WITNESSES = ("honest_face",)
TRANSVERSE_SPLITS_ON_LOCUS = True

# --- G: SHEAR REGISTRATION ----------------------------------------------------
SHEAR_ENTERS_CONE_ONSITE = True
SHEAR_ENTERS_CONE_OVERLAP = True
VOLUME_ENTERS_CONE_ONSITE = False
OVERLAP_ZERO_SHEAR_PENCIL_IS_R5 = True
TENSION_RECORD = ("KERNEL-SIDE SHEAR REGISTRATION: YES in both assemblies (the cone moves with g0, g1 exactly); "
                  "DIAGONAL-METRIC REGISTRATION: branch scales only (graded) or through h0 and the h_f sums (overlap), "
                  "and invisible to the overlap pencil symbol at zero shear.  MATTER SIDE (PR #7970, conditional): "
                  "responds to the diagonal metric and to NO shear.  NAMED TENSION -- recorded, not resolved here.")
TENSION_RECORDED = True

# --- H: THE SCOPE FENCES ------------------------------------------------------
SCOUT_GRADE_FENCE = ("scout-grade finite exact linear algebra on one cell form, "
                     "not a spacetime and not a dynamics")
SCOUT_GRADE_ONLY = True
PHYSICAL_CONTENT_CLAIMED = False
ASSEMBLY_DECIDED = False
HODGE_READING_SELECTED = False
INSTANCE_SCOPE = (
    "two periodic benches, (4,4) with Block 105's 2D face form and (4,2,2) with Block 211's 3D cell form, and no other extent",
    "one cell family, Block 211's per-offset-isotropic variety at the degree-diagonal representative, eight rational witnesses and two QQ(sqrt 6) locus witnesses, with the sixty-four-cell census taken on the degree-block formulas at symbolic moduli",
    "two assemblies, Block 105's onsite and overlap, and two squared-symbol readings, the Euclidean form and the H-pencil",
    "one rule, Block 201's A = sx, B = -sz shadow and its Block 209 three-direction shadow, at the periodic closure and m = 0",
    "the principal part at k = 0 of the eight-fold degenerate zero; no continuum limit, no lattice-spacing statement",
    "the two Hodge readings G1 and G2 as declared candidates; which, if either, is 'the' metric is not decided here",
)
INSTANCE_SCOPE_COUNT = 6

SCOPE_KEYS = ("n5_verbatim",)


def scope_certificate(text: str) -> dict:
    return {"n5_verbatim": N5_FENCE in text}


# ---------------------------------------------------------------------------
# exact helpers -- no float, no tolerance and NO nsimplify anywhere
# ---------------------------------------------------------------------------
# THE nsimplify HAZARD, INHERITED FROM BLOCK 186 THROUGH BLOCK 211 AND HONOURED
# HERE BY ABSENCE.  This block's content is a set of exact polynomial
# identities and exact factorizations -- a cone factor that is or is not
# proportional to a declared quadratic form, a discrepancy polynomial that is
# or is not zero.  A tolerance-carrying call could turn the nonzero
# discrepancy 2 c (1 - c^2)(v^2 + 1) kt kx / |A| into a zero and manufacture
# the very identity this block refutes.  Gate I counts the occurrences in this
# file's own source and requires ZERO, ZERO float literals by AST, and ZERO
# float call sites, because every number here is an exact rational or symbol.
NSIMPLIFY_TOKEN = "sp." + "nsimplify("


def nsimplify_occurrences() -> int:
    try:
        return Path(__file__).read_text(encoding="utf-8").count(NSIMPLIFY_TOKEN)
    except OSError:                                    # pragma: no cover
        return -1


def float_literal_occurrences() -> int:
    try:
        tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    except (OSError, SyntaxError):                     # pragma: no cover
        return -1
    return sum(1 for node in ast.walk(tree)
               if isinstance(node, ast.Constant) and type(node.value) is float)


def float_call_sites() -> int:
    try:
        tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    except (OSError, SyntaxError):                     # pragma: no cover
        return -1
    return sum(1 for node in ast.walk(tree)
               if isinstance(node, ast.Call)
               and isinstance(node.func, ast.Name) and node.func.id == "float")


def residual_count(matrix) -> int:
    matrix = sp.Matrix(matrix)
    return sum(1 for i in range(matrix.rows) for j in range(matrix.cols)
               if sp.cancel(sp.together(matrix[i, j])) != 0)


def is_zero(expression) -> bool:
    return sp.cancel(sp.together(sp.expand(expression))) == 0


def proportional(first, second, variables) -> bool:
    """TWO POLYNOMIALS ARE PROPORTIONAL iff their ratio carries none of the
    listed variables.  Exact: the ratio is cancelled and its free symbols
    inspected; no coefficient is ever compared numerically."""
    first, second = sp.expand(first), sp.expand(second)
    if first == 0 or second == 0:
        return first == 0 and second == 0
    ratio = sp.cancel(sp.together(first / second))
    return not (ratio.free_symbols & set(variables))


def proportionality_minors(first: sp.Matrix, second: sp.Matrix) -> list:
    """The nonzero 2 x 2 minors of the two vectorised symmetric 3 x 3 matrices:
    their common zero set is EXACTLY the locus where the matrices are
    proportional.  Numerators only, so the ideal is polynomial."""
    vec1 = [first[i, j] for i in range(3) for j in range(i, 3)]
    vec2 = [second[i, j] for i in range(3) for j in range(i, 3)]
    minors = set()
    for i in range(6):
        for j in range(i + 1, 6):
            minor = sp.numer(sp.together(sp.cancel(vec1[i] * vec2[j] - vec1[j] * vec2[i])))
            if minor != 0:
                minors.add(sp.expand(minor))
    return sorted(minors, key=str)


def real_solutions_lex(basis: list, first, second) -> tuple:
    """THE REAL ZEROS OF A LEX GROEBNER BASIS IN (first, second), EXACTLY AND
    FAIL-CLOSED.  The basis contains a univariate element in `second`; its
    real roots are taken exactly; each is substituted and the real roots of
    the gcd of what remains in `first` are taken.  A substitution that kills
    every remaining element is a positive-dimensional real component and is
    returned as a marker rather than dropped -- sp.solve would drop it."""
    univariate = [g for g in basis if not g.has(first)]
    if not univariate:
        return ("NO-UNIVARIATE-ELEMENT",)
    solutions = set()
    for second_root in sp.Poly(univariate[-1], second).real_roots():
        rest = [sp.expand(g.subs(second, second_root)) for g in basis]
        rest = [g for g in rest if g != 0]
        if not rest:
            return ("POSITIVE-DIMENSIONAL", second_root)
        common = rest[0]
        for g in rest[1:]:
            common = sp.gcd(common, g)
        if common.has(first):
            for first_root in sp.Poly(common, first).real_roots():
                solutions.add((first_root, second_root))
    return tuple(sorted(solutions, key=lambda s: (str(s[0]), str(s[1]))))


def primitive_factors(expression, variables) -> tuple:
    """The irreducible factors over QQ that involve the listed variables, as
    expanded primitive polynomials with their multiplicities.  A rational
    function is reduced to its numerator; its denominator must be free of the
    listed variables (it is a moduli scale), else the call fails closed."""
    numerator, denominator = sp.fraction(sp.together(sp.expand(expression)))
    if denominator.free_symbols & set(variables):
        raise ValueError("cone denominator carries a formal variable")
    _, factors = sp.factor_list(sp.expand(numerator))
    out = []
    for base, power in factors:
        if base.free_symbols & set(variables):
            out.append((sp.expand(base), power))
    return tuple(out)


# ---------------------------------------------------------------------------
# THE PERIOD-2 OPERATOR MACHINERY.  An operator commuting with all even
# translations is a dictionary {(corner, delta): coefficient} meaning
# A[s, s + delta] = coefficient whenever s mod 2 = corner.  Composition,
# transposition, the Bloch matrix and the bench matrix are all exact.
# ---------------------------------------------------------------------------
KT, KX, KY = sp.symbols("kt kx ky", real=True)
LAM = sp.Symbol("lam")


def corners(dim: int) -> tuple:
    return tuple(itertools.product((0, 1), repeat=dim))


def cmod(corner: tuple) -> tuple:
    return tuple(x % 2 for x in corner)


def vadd(a: tuple, b: tuple) -> tuple:
    return tuple(x + y for x, y in zip(a, b))


def vneg(a: tuple) -> tuple:
    return tuple(-x for x in a)


def grade(corner: tuple) -> int:
    return sum(x % 2 for x in corner)


def eta(corner: tuple, direction: int) -> int:
    """Block 209's staggering phases eta = (1, (-1)^t, (-1)^(t+x)), Block
    201's (1, (-1)^t) in two directions: the product of the parities of all
    coordinates BEFORE the direction."""
    return (-1) ** sum(corner[:direction])


def lane_rules(dim: int) -> dict:
    """The eta-staggered lane kernel: +eta/2 forward, -eta/2 backward."""
    rules = {}
    for corner in corners(dim):
        for direction in range(dim):
            step = tuple(1 if k == direction else 0 for k in range(dim))
            rules[(corner, step)] = sp.Rational(eta(corner, direction), 2)
            rules[(corner, vneg(step))] = -sp.Rational(eta(corner, direction), 2)
    return rules


def raising_rules(kernel: dict) -> dict:
    """BLOCK 201's GRADING, d = sum_g P_{g+1} K P_g: the ROW grade is one
    higher than the COLUMN grade.  In dictionary form, the entries (c, delta)
    with grade(c) = grade(c + delta) + 1."""
    return {(c, d): v for (c, d), v in kernel.items()
            if grade(c) == grade(vadd(c, d)) + 1}


def transpose_rules(rules: dict) -> dict:
    return {(cmod(vadd(c, d)), vneg(d)): v for (c, d), v in rules.items()}


def compose_rules(first: dict, second: dict) -> dict:
    out: dict = {}
    for (c, d1), a in first.items():
        middle = cmod(vadd(c, d1))
        for (c2, d2), b in second.items():
            if c2 != middle:
                continue
            key = (c, vadd(d1, d2))
            out[key] = out.get(key, 0) + a * b
    return {k: sp.expand(v) for k, v in out.items() if sp.expand(v) != 0}


def combine_rules(first: dict, second: dict, sign_second=1) -> dict:
    out: dict = {}
    for k, v in first.items():
        out[k] = out.get(k, 0) + v
    for k, v in second.items():
        out[k] = out.get(k, 0) + sign_second * v
    return {k: sp.expand(v) for k, v in out.items() if sp.expand(v) != 0}


def onsite_rules(cell, cell_corners: tuple, dim: int) -> dict:
    """BLOCK 105's onsite_hodge: one cell per even anchor, weight 1, each site
    a fixed corner of exactly one cell -- the grade-diagonal assembly."""
    rules = {}
    for i, ci in enumerate(cell_corners):
        for j, cj in enumerate(cell_corners):
            if cell[i, j] == 0:
                continue
            rules[(tuple(ci), tuple(cj[k] - ci[k] for k in range(dim)))] = cell[i, j]
    return rules


def overlap_rules(cell, cell_corners: tuple, dim: int) -> dict:
    """BLOCK 105's overlap_hodge and BLOCK 191's rule as used by BLOCK 201's
    fork_hodge: one cell per anchor, weight 2^-d, every site a corner of 2^d
    cells -- the translation-invariant assembly."""
    rules: dict = {}
    weight = sp.Rational(1, 2 ** dim)
    for i, ci in enumerate(cell_corners):
        for j, cj in enumerate(cell_corners):
            if cell[i, j] == 0:
                continue
            delta = tuple(cj[k] - ci[k] for k in range(dim))
            for corner in corners(dim):
                rules[(corner, delta)] = rules.get((corner, delta), 0) + weight * cell[i, j]
    return {k: sp.expand(v) for k, v in rules.items() if sp.expand(v) != 0}


def bloch_matrix(rules: dict, z: tuple, dim: int) -> sp.Matrix:
    cs = corners(dim)
    matrix = sp.zeros(len(cs), len(cs))
    for (c, d), a in rules.items():
        phase = sp.Integer(1)
        for k in range(dim):
            phase *= z[k] ** d[k]
        matrix[cs.index(c), cs.index(cmod(vadd(c, d)))] += a * phase
    return matrix.applyfunc(sp.expand)


def folded_matrix(rules: dict, dim: int) -> sp.Matrix:
    """A_B(1): the Bloch matrix at zero momentum."""
    cs = corners(dim)
    matrix = sp.zeros(len(cs), len(cs))
    for (c, d), a in rules.items():
        matrix[cs.index(c), cs.index(cmod(vadd(c, d)))] += a
    return matrix.applyfunc(sp.expand)


def first_order_matrix(rules: dict, dim: int, kappa: tuple) -> sp.Matrix:
    """D(kappa)[c, c'] = sum_delta (delta . kappa) A[c, delta]: the exact
    first-order coefficient of A_B(exp(i eps kappa)) divided by i eps."""
    cs = corners(dim)
    matrix = sp.zeros(len(cs), len(cs))
    for (c, d), a in rules.items():
        matrix[cs.index(c), cs.index(cmod(vadd(c, d)))] += a * sum(
            d[k] * kappa[k] for k in range(dim))
    return matrix.applyfunc(sp.expand)


def site_index(site: tuple, extent: tuple) -> int:
    index = 0
    for coordinate, size in zip(site, extent):
        index = index * size + (coordinate % size)
    return index


def bench_sites(extent: tuple) -> tuple:
    return tuple(itertools.product(*(range(size) for size in extent)))


def bench_matrix(rules: dict, extent: tuple) -> sp.Matrix:
    """THE PERIODIC BENCH MATRIX OF A PERIOD-2 OPERATOR: aliases along an
    extent-2 direction ADD, which is exactly the projection of the infinite
    lattice operator onto periodic functions."""
    sites = bench_sites(extent)
    matrix = sp.zeros(len(sites), len(sites))
    for site in sites:
        corner = cmod(site)
        for (c, d), a in rules.items():
            if c != corner:
                continue
            matrix[site_index(site, extent), site_index(vadd(site, d), extent)] += a
    return matrix.applyfunc(sp.expand)


def bench_assembly(extent: tuple, cell_corners: tuple, block_of_anchor,
                   anchors: tuple, weight) -> sp.Matrix:
    """BLOCK 201's fork_hodge PATTERN, GENERALISED: embed block_of_anchor(a)
    at the corners a + c for every anchor a with the given weight."""
    sites = bench_sites(extent)
    matrix = sp.zeros(len(sites), len(sites))
    for anchor in anchors:
        block = block_of_anchor(anchor)
        indices = [site_index(vadd(anchor, tuple(c)), extent) for c in cell_corners]
        for i, ci in enumerate(indices):
            for j, cj in enumerate(indices):
                matrix[ci, cj] += weight * block[i, j]
    return matrix.applyfunc(sp.expand)


def bench_momenta(extent: tuple) -> tuple:
    """z_d = exp(2 pi i m_d / N_d) for m_d < N_d / 2, EXACT: for N_d = 4 the
    set {1, i}, for N_d = 2 the set {1}.  The folding over the 2^d corners
    supplies the other half."""
    axes = []
    for size in extent:
        values = []
        for m in range(size // 2):
            angle = 2 * sp.pi * m / size
            values.append(sp.expand(sp.cos(angle) + sp.I * sp.sin(angle)))
        axes.append(tuple(values))
    return tuple(itertools.product(*axes))


def charpoly_expr(matrix: sp.Matrix):
    poly = sp.Matrix(matrix).charpoly(LAM).as_expr()
    return sp.expand(poly)


# THE EXACT NUMERIC DOMAINS, AND THEY ARE NOT NUMERICAL METHODS.  Every Bloch
# matrix at a root of unity lies in QQ(i)^(n x n) and every bench matrix at a
# rational witness in QQ^(n x n); DomainMatrix carries out the products, the
# inverses and the characteristic polynomials by exact fraction-free
# arithmetic over those fields.  No float is created and no tolerance exists.
def domain_of(matrix: sp.Matrix, gaussian: bool) -> DomainMatrix:
    return DomainMatrix.from_Matrix(sp.Matrix(matrix)).convert_to(QQ_I if gaussian else QQ)


def domain_charpoly(matrix: DomainMatrix):
    coefficients = matrix.charpoly()
    domain = matrix.domain
    degree = len(coefficients) - 1
    return sp.expand(sum(domain.to_sympy(coefficient) * LAM ** (degree - k)
                         for k, coefficient in enumerate(coefficients)))


def domain_symbol(hodge: DomainMatrix, raising: DomainMatrix,
                  raising_transpose: DomainMatrix, reading: str) -> DomainMatrix:
    if reading == "form":
        kernel = hodge * raising - raising_transpose * hodge
        return -(kernel * kernel)
    operator = raising - hodge.inv() * raising_transpose * hodge
    return -(operator * operator)


def form_symbol(hodge_bloch, raising_bloch, raising_bloch_transpose):
    kernel = (hodge_bloch * raising_bloch
              - raising_bloch_transpose * hodge_bloch).applyfunc(sp.expand)
    return (-kernel * kernel).applyfunc(sp.expand), kernel


def pencil_symbol_with_inverse(hodge_bloch, hodge_inverse, raising_bloch,
                               raising_bloch_transpose):
    operator = (raising_bloch
                - hodge_inverse * raising_bloch_transpose * hodge_bloch).applyfunc(sp.cancel)
    return (-operator * operator).applyfunc(sp.cancel), operator


def onsite_pencil_symbol(cell, cell_corners: tuple, dim: int, z: tuple,
                         raising: dict):
    """THE GRADED H-PENCIL SYMBOL AT SYMBOLIC PHASES, CHEAPLY: the onsite
    Bloch matrix is Z^-1 D Z with Z = diag(z^c), so its inverse is the onsite
    Bloch matrix of D^-1 -- no symbolic inversion is ever performed."""
    h_b = bloch_matrix(onsite_rules(cell, cell_corners, dim), z, dim)
    h_inverse = bloch_matrix(onsite_rules(sp.Matrix(cell).inv(), cell_corners, dim), z, dim)
    d_b = bloch_matrix(raising, z, dim)
    dT_b = bloch_matrix(transpose_rules(raising), z, dim)
    return pencil_symbol_with_inverse(h_b, h_inverse, d_b, dT_b)


def bloch_spectrum_charpoly(rules_h: dict, rules_d: dict, extent: tuple,
                            dim: int, reading: str):
    """THE BENCH CHARPOLY FROM THE BLOCH SIDE: the product over the supercell
    momenta of the 2^d x 2^d charpolys, every root of unity exact, over QQ(i)."""
    rules_dT = transpose_rules(rules_d)
    product = sp.Integer(1)
    for z in bench_momenta(extent):
        h_b = domain_of(bloch_matrix(rules_h, z, dim), True)
        d_b = domain_of(bloch_matrix(rules_d, z, dim), True)
        dT_b = domain_of(bloch_matrix(rules_dT, z, dim), True)
        product *= domain_charpoly(domain_symbol(h_b, d_b, dT_b, reading))
    return sp.expand(product)


def direct_bench_charpoly(hodge: sp.Matrix, raising: sp.Matrix, reading: str):
    return domain_charpoly(domain_symbol(
        domain_of(hodge, False), domain_of(raising, False),
        domain_of(raising.T, False), reading))


def is_singular(matrix: sp.Matrix) -> bool:
    return domain_of(matrix, False).det() == 0


def multiset_of(charpoly_expression) -> tuple:
    """The root multiset of a charpoly whose roots are all rational, as a
    sorted tuple of (root, multiplicity); None if some root is not rational."""
    poly = sp.Poly(charpoly_expression, LAM)
    roots = sp.roots(poly)
    if sum(roots.values()) != poly.degree():
        return None
    if any(not root.is_rational for root in roots):
        return None
    return tuple(sorted(((root, mult) for root, mult in roots.items()), key=lambda t: t[0]))


def expected_flat_multiset(extent: tuple) -> tuple:
    values: dict = {}
    for m in itertools.product(*(range(size) for size in extent)):
        value = sp.expand(sum(sp.sin(2 * sp.pi * m[k] / extent[k]) ** 2
                              for k in range(len(extent))))
        values[value] = values.get(value, 0) + 1
    return tuple(sorted(values.items(), key=lambda t: t[0]))


def even_odd(dim: int) -> tuple:
    cs = corners(dim)
    even = [i for i, c in enumerate(cs) if grade(c) % 2 == 0]
    odd = [i for i, c in enumerate(cs) if grade(c) % 2 == 1]
    return even, odd


def bipartite_block(h0: sp.Matrix, dk: sp.Matrix, dim: int) -> tuple:
    """B(kappa) = H_e D_eo + D_oe^T H_o, together with H_e and H_o, once the
    folded H0 is verified to preserve grade parity."""
    even, odd = even_odd(dim)
    h_e = h0.extract(even, even)
    h_o = h0.extract(odd, odd)
    parity_preserving = (residual_count(h0.extract(even, odd)) == 0
                         and residual_count(h0.extract(odd, even)) == 0)
    d_eo = dk.extract(even, odd)
    d_oe = dk.extract(odd, even)
    block = (h_e * d_eo + d_oe.T * h_o).applyfunc(sp.cancel)
    return block, h_e, h_o, parity_preserving


def is_scalar_matrix(matrix: sp.Matrix) -> bool:
    n = matrix.rows
    return (all(is_zero(matrix[i, j]) for i in range(n) for j in range(n) if i != j)
            and all(is_zero(matrix[i, i] - matrix[0, 0]) for i in range(n)))


def metric_candidates(cell: sp.Matrix) -> tuple:
    """G1 = D1/D0 and G2 = D3 E D2^-1 E, both as 3 x 3 matrices over the
    directions (t, x, y): D1 is read on the unit corners e_mu and D2 on the
    complementary corners 1 - e_mu, which is Block 209's two_order."""
    unit = [b209.CORNERS.index(tuple(1 if k == mu else 0 for k in range(3))) for mu in range(3)]
    complement = [b209.CORNERS.index(tuple(0 if k == mu else 1 for k in range(3))) for mu in range(3)]
    d0, d3 = cell[0, 0], cell[7, 7]
    d1 = sp.Matrix(3, 3, lambda i, j: cell[unit[i], unit[j]])
    d2 = sp.Matrix(3, 3, lambda i, j: cell[complement[i], complement[j]])
    signature = sp.diag(1, -1, 1)
    g1 = (d1 / d0).applyfunc(sp.cancel)
    # AT THE PD BOUNDARY D2 IS SINGULAR AND THE DEGREE-2/3 READING HAS NO
    # INVERSE: G2 is then None, measured rather than assumed.
    g2 = None
    if sp.cancel(d2.det()) != 0:
        g2 = (d3 * signature * d2.inv() * signature).applyfunc(sp.cancel)
    return g1, g2, d0, d1, d2, d3


def quadratic_form(matrix: sp.Matrix, kappa: tuple):
    vector = sp.Matrix(kappa)
    return sp.expand((vector.T * matrix * vector)[0, 0])


# ---------------------------------------------------------------------------
# THE WITNESSES, READ THROUGH BLOCK 211's OWN OBJECTS
# ---------------------------------------------------------------------------
SQRT6 = sp.sqrt(6)
FACES = (("tx", 0), ("ty", 0), ("xy", 0), ("tx", 1), ("ty", 1), ("xy", 1))


def locus_witness_table() -> dict:
    """THE TWO COINCIDENCE-LOCUS WITNESSES, on the family (both ties exact),
    in rule-A cells: s1 = (s_tx0, -s_ty0, s_xy0) = -E s0 E."""
    return {
        # class (+1, -1): s0 = (+, +, +), s1 = (+, -, +); g1 = 1/2, g0 = g1/(1 + g1) = 1/3;
        # v0^2 = (1 - g0^2)(1 - g1^2) = 2/3, v1^2 = (1 - g1^2)/(1 - g0^2) = 27/32.
        "L+-": ((SQRT6 / 3, sp.Rational(1, 3), 3 * SQRT6 / 8, HALF),
                dict(zip(FACES, (1, 1, 1, 1, -1, 1)))),
        # class (-1, +1): s0 = (+, -, +), s1 = (+, +, +); g1 = 1/3, g0 = g1/(1 - g1) = 1/2;
        # v0^2 = 2/3, v1^2 = 32/27.
        "L-+": ((SQRT6 / 3, HALF, 4 * SQRT6 / 9, sp.Rational(1, 3)),
                dict(zip(FACES, (1, -1, 1, 1, 1, 1)))),
    }


def formal_family(class_signs: dict, g0, g1, v0, v1) -> sp.Matrix:
    """BLOCK 211's DEGREE-BLOCK FORMULAS AS A FORMAL 8 x 8 CELL FORM at the given
    (possibly symbolic, possibly untied) moduli: [v0], v1 M1(g0; signs),
    M2(g1; signs)/v0, [1/v1] on Block 209's degree indices."""
    family = sp.zeros(8, 8)
    family[0, 0], family[7, 7] = v0, 1 / v1
    first = v1 * first_block(g0, class_signs)
    second = second_block(g1, class_signs) / v0
    ones, twos = b209.DEGREE_INDICES[1], b209.DEGREE_INDICES[2]
    for i in range(3):
        for j in range(3):
            family[ones[i], ones[j]] = first[i, j]
            family[twos[i], twos[j]] = second[i, j]
    return family


def witness_table() -> dict:
    flipped_both = b211.flipped(("xy", 0), ("xy", 1))
    return {
        "flat": ((sp.Integer(1), sp.Integer(0), sp.Integer(1), sp.Integer(0)), b211.ALL_PLUS),
        "W1": (b211.W1_MODULI, b211.ALL_PLUS),
        "W2": (b211.W2_MODULI, flipped_both),
        "W3": (b211.W3_MODULI, flipped_both),
        "mixed": (b211.diagonal_point(sp.Rational(1, 4)), b211.REPRESENTATIVES[(1, -1)]),
        "near_boundary": (b211.diagonal_point(sp.Rational(49, 100)), b211.ALL_PLUS),
        "boundary": (b211.diagonal_point(HALF), b211.ALL_PLUS),
        # THE HONEST-FACE POINT: g1 = 0, v1 = 1/v0, v0^2 = 1 - g0^2, so the
        # offset-0 tx face has v^2 = det g2(c) exactly; class (-1, .) at g0 = 4/5.
        "honest_face": ((sp.Rational(3, 5), sp.Rational(4, 5), sp.Rational(5, 3), sp.Integer(0)),
                        b211.flipped(("xy", 0))),
    }


@dataclass(frozen=True)
class CellFacts:
    name: str
    moduli: tuple
    ranks: tuple
    free_names: tuple
    blocks_match_formulas: bool
    cross_degree_zero: bool
    face_restriction_is_shear_hodge: bool
    leading_minors: tuple
    positive_definite: bool
    face_moduli: tuple
    g1: tuple
    g2: tuple
    g1_proportional_to_g2: bool
    hodge_defect_scalar: object
    hodge_defect_matrix_nnz: int


def solve_witness(name: str, moduli: tuple, signs: dict) -> tuple:
    volume0, gamma0, volume1, gamma1 = moduli
    _, matrix, rhs = b211.face_system(b211.branch_moduli(volume0, gamma0, volume1, gamma1, signs))
    ranks = (matrix.rank(), matrix.row_join(rhs).rank())
    cell, free = b211.solve_pinned(matrix, rhs)
    # radsimp is the identity on rationals and puts the QQ(sqrt 6) locus
    # witnesses' entries into the canonical a + b sqrt(6) form so that every
    # exact sign test below is decidable.
    cell = cell.applyfunc(sp.radsimp)
    # THE DEGREE-BLOCK FORMULAS OF BLOCK 211, RE-VERIFIED AT THE POINT.
    first = volume1 * b211.signed_triangle((signs[("xy", 0)] * gamma0,
                                            signs[("ty", 0)] * gamma0,
                                            signs[("tx", 0)] * gamma0))
    second = b211.signed_triangle((signs[("tx", 1)] * gamma1,
                                   signs[("ty", 1)] * gamma1,
                                   signs[("xy", 1)] * gamma1)) / volume0
    blocks_ok = (residual_count(b211.degree_block(cell, 0) - sp.Matrix([[volume0]])) == 0
                 and residual_count(b211.degree_block(cell, 1) - first) == 0
                 and residual_count(b211.degree_block(cell, 2) - second) == 0
                 and residual_count(b211.degree_block(cell, 3) - sp.Matrix([[1 / volume1]])) == 0)
    cross_zero = all(cell[i, j] == 0 for i in range(8) for j in range(8)
                     if sum(b209.CORNERS[i]) != sum(b209.CORNERS[j]))
    # THE ORIGIN tx FACE IS BLOCK 105's shear_hodge AT (s_tx0 g0, v0), which
    # is what the (4,4) bench is built on.
    face_indices = [b209.CORNERS.index(c) for c in ((0, 0, 0), (0, 1, 0), (1, 0, 0), (1, 1, 0))]
    face = sp.Matrix(4, 4, lambda i, j: cell[face_indices[i], face_indices[j]])
    face_moduli = (signs[("tx", 0)] * gamma0, volume0)
    face_ok = residual_count(face - sp.Matrix(b211.LANDED_SHEAR_HODGE(*face_moduli))) == 0
    minors = tuple(sp.radsimp(m) for m in b211.leading_minors(cell))
    g1, g2, d0, d1, d2, d3 = metric_candidates(cell)
    if g2 is not None:
        g2 = g2.applyfunc(sp.radsimp)
    g1 = g1.applyfunc(sp.radsimp)
    prop = None
    if g2 is not None:
        vec1 = [g1[i, j] for i in range(3) for j in range(i, 3)]
        vec2 = [g2[i, j] for i in range(3) for j in range(i, 3)]
        prop = all(is_zero(vec1[a] * vec2[b] - vec1[b] * vec2[a])
                   for a in range(6) for b in range(a + 1, 6))
    signature = sp.diag(1, -1, 1)
    defect_matrix = (d1 * signature * d2 * signature - d0 * d3 * sp.eye(3)).applyfunc(sp.cancel)
    return CellFacts(
        name, tuple(moduli), ranks, tuple(str(s) for s in free), blocks_ok, cross_zero,
        face_ok, tuple(minors), all(m > 0 for m in minors), face_moduli,
        tuple(tuple(g1[i, j] for j in range(3)) for i in range(3)),
        (tuple(tuple(g2[i, j] for j in range(3)) for i in range(3))
         if g2 is not None else ("UNDEFINED: det D2 = 0",)),
        prop, sp.cancel(d0 * d3 - 1), residual_count(defect_matrix)), cell


# ---------------------------------------------------------------------------
# THE MEASURED FACTS
# ---------------------------------------------------------------------------
@dataclass(frozen=True)
class ConstructionFacts:
    lane_2d_matches_b201: bool
    lane_2d_nnz: int
    spin_nonscalar_2d: int
    lane_2d_site_sign_equivalent: bool
    raising_matches_b201_on_fork: bool
    k_is_d_minus_dT_2d: bool
    d_squared_zero_2d: bool
    lane_3d_links_scanned: int
    lane_3d_bad_links: int
    lane_3d_shadow_matches: bool
    lane_3d_nnz: int
    lane_3d_xy_links_absent: bool
    k_is_d_minus_dT_3d: bool
    d_squared_zero_3d: bool
    fork_hodge_reproduced: bool
    onsite_hodge_reproduced: bool
    overlap_hodge_reproduced: bool
    rules_match_bench_assembly: bool
    flat_h_identity: bool
    flat_kernel_is_r5: bool
    cells: tuple


@dataclass(frozen=True)
class ControlFacts:
    flat_symbol_identity_2d: bool
    flat_symbol_identity_3d: bool
    multiset_2d: tuple
    multiset_3d: tuple
    expected_2d: tuple
    expected_3d: tuple
    bloch_equals_direct_flat: bool


@dataclass(frozen=True)
class SpectrumFacts:
    entries: tuple                 # (witness, bench, assembly, reading, factored charpoly text, agreement, multiset)
    all_agree: bool
    w1_overlap_pencil_2d: tuple
    translation_commutators: tuple
    boundary_onsite_singular_2d: bool
    boundary_onsite_singular_3d: bool
    boundary_overlap_regular: bool


@dataclass(frozen=True)
class PrincipalFacts:
    lemma_3d_holds: bool
    lemma_2d_holds: bool
    lemma_3d_block_diagonal: bool
    lemma_3d_zero_form_branch: bool
    lemma_3d_top_form_branch: bool
    lemma_3d_transverse_product: bool
    lemma_d0_absent: bool
    expansion_exact: bool
    overlap_h0_form_holds: bool
    overlap_cone_3d_holds: bool
    overlap_cone_2d_holds: bool
    two_dim_onsite_branches: bool
    two_dim_onsite_form_scalar: bool
    two_dim_onsite_pencil_scalar_generic: bool
    two_dim_onsite_scalar_on_locus: bool
    two_dim_overlap_pencil_scalar: bool
    two_dim_overlap_pencil_matches: bool
    two_dim_overlap_cone_matches: bool
    two_dim_overlap_form_scalar: bool
    two_dim_effective_shear: bool
    two_dim_discrepancy: bool
    two_dim_onsite_zero_form_symbol: str
    two_dim_onsite_two_form_symbol: str
    two_dim_overlap_pencil_symbol: str
    witnesses: tuple               # per witness per assembly: cone factors etc
    w1_onsite_cones: bool
    w1_overlap_cones: bool
    onsite_cones_are_g1_g2_everywhere: bool
    onsite_branches_g1_g2_everywhere: bool
    overlap_cones_never_g1_g2: bool
    principal_scalar_at_listed_curved_3d_witnesses: bool
    overlap_scalar_counterexample: bool
    transverse_split_witnesses: tuple
    coincidence_chart_bases: tuple
    coincidence_chart_bases_equal: bool
    coincidence_solutions: tuple
    coincidence_classes: int
    census: tuple                  # ((groebner key, cells, classes), ...)
    census_cells: int
    rule_a_cells: int
    rule_b_cells: int
    rules_cover_curve_cells: bool
    closed_form_ok: bool
    curve_solutions_ok: bool
    locus_pd: bool
    locus_proportional: bool
    locus_mu: tuple
    locus_one_cone_squared: bool
    locus_det_prefactors: tuple
    locus_constants: tuple
    locus_transverse_split: bool
    locus_overlap_factor_counts: tuple
    locus_overlap_never_g1: bool
    locus_symbolic_one_cone: bool
    locus_symbolic_branches_k_free: bool
    locus_symbolic_constants: tuple
    locus_symbolic_constants_match: bool
    locus_mu_minus_one: tuple
    locus_mu_minus_one_matches: bool
    w1_zero_form_symbol: str


@dataclass(frozen=True)
class RegistrationFacts:
    onsite_cone_shear_derivative_nonzero: bool
    onsite_cone_volume_free: bool
    onsite_branch_scales: tuple
    overlap_symbol_depends_only_on_h: bool
    overlap_zero_shear_pencil_is_r5: bool
    overlap_zero_shear_form_scale: str
    overlap_cone_shear_derivative_nonzero: bool
    sign_class_moves_overlap_cone: bool


@dataclass(frozen=True)
class Facts:
    source_base: str
    authority: AuthorityCertificate
    imposed: int
    registered: int
    adopted: int
    unsupplied: int
    readings: int
    scoped_words: int
    construction: ConstructionFacts
    control: ControlFacts
    spectra: SpectrumFacts
    principal: PrincipalFacts
    registration: RegistrationFacts
    scope: dict
    nsimplify_calls: int
    float_literals: int
    float_calls: int


def measure_construction(witnesses: dict) -> tuple:
    """FAMILY C, MEASURED ONCE."""
    # (1) THE 2D LANE KERNEL IS BLOCK 201's, AND IT IS THE SHADOW.
    lane2 = lane_rules(2)
    bench2 = bench_matrix(lane2, BENCH_2D)
    b201_lane = b201.lane_kernel(BENCH_2D[0], BENCH_2D[1], "periodic")
    lane_matches = residual_count(bench2 - b201_lane) == 0
    scalar, nonscalar = b201.covariant_kernel(BENCH_2D[0], BENCH_2D[1], (1, 1))
    equivalent = b201.site_sign_equivalent(scalar, b201_lane, BENCH_2D[0] * BENCH_2D[1])
    d2 = raising_rules(lane2)
    fork_lane = b201.lane_kernel(FORK_EXTENT[0], FORK_EXTENT[1], "periodic")
    raising_matches = residual_count(bench_matrix(d2, FORK_EXTENT) - b201.raising_part(fork_lane)) == 0
    k_is_d_minus_dT_2d = combine_rules(lane2, combine_rules(d2, transpose_rules(d2), -1), -1) == {}
    d_squared_2d = compose_rules(d2, d2) == {}
    # (2) THE 3D LANE KERNEL IS BLOCK 209's SHADOW, LINK BY LINK.
    lane3 = lane_rules(3)
    scanned, bad, shadow_ok = 0, 0, True
    for site in bench_sites(BENCH_3D):
        for direction in range(3):
            stepped = list(site)
            stepped[direction] += 1
            neighbour = tuple(c % e for c, e in zip(stepped, BENCH_3D))
            block = sp.Matrix(sp.expand(
                b209.omega(site).T * (b209.GENERATORS[direction] / 2) * b209.omega(neighbour)))
            scanned += 1
            off_diagonal = any(block[i, j] != 0 for i in range(4) for j in range(4) if i != j)
            diagonal_equal = block[0, 0] == block[1, 1] == block[2, 2] == block[3, 3]
            if off_diagonal or not diagonal_equal:
                bad += 1
                continue
            step = tuple(1 if k == direction else 0 for k in range(3))
            if sp.expand(block[0, 0] - lane3[(cmod(site), step)]) != 0:
                shadow_ok = False
    bench3 = bench_matrix(lane3, BENCH_3D)
    xy_absent = all(
        bench3[site_index(s, BENCH_3D), site_index(vadd(s, step), BENCH_3D)] == 0
        for s in bench_sites(BENCH_3D) for step in ((0, 1, 0), (0, 0, 1)))
    d3 = raising_rules(lane3)
    k_is_d_minus_dT_3d = combine_rules(lane3, combine_rules(d3, transpose_rules(d3), -1), -1) == {}
    d_squared_3d = compose_rules(d3, d3) == {}
    # (3) THE ASSEMBLERS REPRODUCE THE FIXED-SOURCE HODGES DIGIT FOR DIGIT.
    fork_block = sp.expand(sp.Matrix(b211.LANDED_SHEAR_HODGE(b201.FORK_SHEAR, sp.Integer(1))))
    reflected = sp.expand(b201.OFFSET_PERMUTATION * fork_block * b201.OFFSET_PERMUTATION.T)
    fork = bench_assembly(
        FORK_EXTENT, b201.CELL_CORNERS,
        lambda anchor: fork_block if anchor[0] < FORK_EXTENT[0] // 2 else reflected,
        bench_sites(FORK_EXTENT), sp.Rational(1, 4))
    fork_ok = residual_count(fork - b201.fork_hodge(b201.FORK_SHEAR)) == 0
    length = b105.LENGTH
    onsite_anchors = tuple((2 * ct, 2 * cx) for ct in range(b105.COARSE_EXTENT)
                           for cx in range(b105.COARSE_EXTENT))
    onsite = bench_assembly(
        (length, length), b201.CELL_CORNERS,
        lambda anchor: sp.Matrix(b105.shear_hodge(*b105.BASE_SHEARS[2 * (anchor[0] // 2) + anchor[1] // 2])),
        onsite_anchors, sp.Integer(1))
    onsite_ok = residual_count(onsite - b105.onsite_hodge()) == 0
    field = b105.overlap_field()
    overlap = bench_assembly(
        (length, length), b201.CELL_CORNERS,
        lambda anchor: sp.Matrix(b105.shear_hodge(*field[anchor])),
        bench_sites((length, length)), sp.Rational(1, 4))
    overlap_ok = residual_count(overlap - b105.overlap_hodge(field)) == 0
    # (4) THE RULE-BASED ASSEMBLIES EQUAL THE BENCH ASSEMBLIES OF A UNIFORM CELL.
    w1_face = sp.expand(sp.Matrix(b211.LANDED_SHEAR_HODGE(sp.Rational(1, 4), sp.Rational(15, 16))))
    rules_ok = (
        residual_count(bench_matrix(onsite_rules(w1_face, b201.CELL_CORNERS, 2), BENCH_2D)
                       - bench_assembly(BENCH_2D, b201.CELL_CORNERS, lambda a: w1_face,
                                        tuple(s for s in bench_sites(BENCH_2D) if s[0] % 2 == 0 and s[1] % 2 == 0),
                                        sp.Integer(1))) == 0
        and residual_count(bench_matrix(overlap_rules(w1_face, b201.CELL_CORNERS, 2), BENCH_2D)
                           - bench_assembly(BENCH_2D, b201.CELL_CORNERS, lambda a: w1_face,
                                            bench_sites(BENCH_2D), sp.Rational(1, 4))) == 0)
    # (5) THE CELL FORMS, SOLVED THROUGH BLOCK 211: the eight rational witnesses
    # and the two QQ(sqrt 6) locus witnesses.
    cells, cell_matrices = [], {}
    for name in WITNESS_NAMES + LOCUS_WITNESS_NAMES:
        moduli, signs = witnesses[name]
        facts, cell = solve_witness(name, moduli, signs)
        cells.append(facts)
        cell_matrices[name] = cell
    flat_cell = cell_matrices["flat"]
    flat_face = sp.Matrix(4, 4, lambda i, j: flat_cell[[0, 2, 4, 6][i], [0, 2, 4, 6][j]])
    flat_identity, flat_r5 = True, True
    for dim, extent, cell, cell_corners, lane, raising in (
            (2, BENCH_2D, flat_face, b201.CELL_CORNERS, lane2, d2),
            (3, BENCH_3D, flat_cell, b209.CORNERS, lane3, d3)):
        for assembly in (onsite_rules, overlap_rules):
            hodge = bench_matrix(assembly(cell, cell_corners, dim), extent)
            if residual_count(hodge - sp.eye(hodge.rows)) != 0:
                flat_identity = False
            raise_bench = bench_matrix(raising, extent)
            kernel = hodge * raise_bench - raise_bench.T * hodge
            if residual_count(kernel - bench_matrix(lane, extent)) != 0:
                flat_r5 = False
    return ConstructionFacts(
        lane_matches, sum(1 for i in range(16) for j in range(16) if bench2[i, j] != 0),
        nonscalar, equivalent, raising_matches, k_is_d_minus_dT_2d, d_squared_2d,
        scanned, bad, shadow_ok,
        sum(1 for i in range(16) for j in range(16) if bench3[i, j] != 0), xy_absent,
        k_is_d_minus_dT_3d, d_squared_3d, fork_ok, onsite_ok, overlap_ok, rules_ok,
        flat_identity, flat_r5, tuple(cells)), cell_matrices


def measure_control() -> ControlFacts:
    """FAMILY D, MEASURED ONCE: R5's flat symbol, symbolically and on both
    benches, from the Bloch side and from the direct bench matrices."""
    identities, multisets, expected, agree = [], [], [], True
    for dim, extent in ((2, BENCH_2D), (3, BENCH_3D)):
        z = sp.symbols(f"z0:{dim}")
        lane = lane_rules(dim)
        kernel_bloch = bloch_matrix(lane, z, dim)
        symbol = (-kernel_bloch * kernel_bloch).applyfunc(sp.expand)
        target = sum(-(z[k] - 1 / z[k]) ** 2 / 4 for k in range(dim))
        identities.append(residual_count(symbol - sp.expand(target) * sp.eye(2 ** dim)) == 0)
        direct = bench_matrix(lane, extent)
        direct_poly = charpoly_expr((-direct * direct).applyfunc(sp.expand))
        raising = raising_rules(lane)
        identity_rules = {(c, tuple(0 for _ in range(dim))): sp.Integer(1) for c in corners(dim)}
        bloch_poly = bloch_spectrum_charpoly(identity_rules, raising, extent, dim, "form")
        if sp.expand(direct_poly - bloch_poly) != 0:
            agree = False
        multisets.append(multiset_of(direct_poly))
        expected.append(expected_flat_multiset(extent))
    return ControlFacts(identities[0], identities[1], multisets[0], multisets[1],
                        expected[0], expected[1], agree)


def measure_spectra(cell_matrices: dict) -> SpectrumFacts:
    """FAMILY E, MEASURED ONCE: the exact bench spectra of all four
    constructions at every witness, Bloch union against direct bench."""
    entries, all_agree = [], True
    commutators = []
    w1_pencil = None
    boundary_onsite_singular = {}
    boundary_overlap_regular = True
    for name in WITNESS_NAMES:
        cell3 = cell_matrices[name]
        face = sp.Matrix(4, 4, lambda i, j: cell3[[0, 2, 4, 6][i], [0, 2, 4, 6][j]])
        for dim, extent, cell, cell_corners in ((2, BENCH_2D, face, b201.CELL_CORNERS),
                                               (3, BENCH_3D, cell3, b209.CORNERS)):
            lane = lane_rules(dim)
            raising = raising_rules(lane)
            raise_bench = bench_matrix(raising, extent)
            for assembly in ASSEMBLIES:
                rules_h = (onsite_rules if assembly == "onsite" else overlap_rules)(cell, cell_corners, dim)
                hodge = bench_matrix(rules_h, extent)
                singular = is_singular(hodge)
                if name == "boundary":
                    if assembly == "onsite":
                        boundary_onsite_singular[dim] = singular
                    else:
                        boundary_overlap_regular = boundary_overlap_regular and not singular
                for reading in READINGS_NAMES:
                    if reading == "pencil" and singular:
                        entries.append((name, extent, assembly, reading, "UNDEFINED: det H = 0", True, None))
                        continue
                    direct_poly = direct_bench_charpoly(hodge, raise_bench, reading)
                    bloch_poly = bloch_spectrum_charpoly(rules_h, raising, extent, dim, reading)
                    agreement = sp.expand(direct_poly - bloch_poly) == 0
                    all_agree = all_agree and agreement
                    multiset = multiset_of(direct_poly)
                    entries.append((name, extent, assembly, reading,
                                    str(sp.factor(direct_poly)), agreement, multiset))
                    if name == "W1" and dim == 2 and assembly == "overlap" and reading == "pencil":
                        w1_pencil = multiset
                if name == "W1":
                    # TRANSLATION COVARIANCE, MEASURED: nnz([-K^2, T_mu]) per direction.
                    kernel = (hodge * raise_bench - raise_bench.T * hodge).applyfunc(sp.expand)
                    squared = (-kernel * kernel).applyfunc(sp.expand)
                    counts = []
                    for direction in range(dim):
                        shift = sp.zeros(hodge.rows, hodge.rows)
                        for site in bench_sites(extent):
                            stepped = list(site)
                            stepped[direction] += 1
                            shift[site_index(tuple(stepped), extent), site_index(site, extent)] = 1
                        counts.append(residual_count(squared * shift - shift * squared))
                    commutators.append((extent, assembly, tuple(counts)))
    return SpectrumFacts(tuple(entries), all_agree, w1_pencil, tuple(commutators),
                         boundary_onsite_singular.get(2, False), boundary_onsite_singular.get(3, False),
                         boundary_overlap_regular)


def principal_objects(rules_h: dict, raising: dict, dim: int, kappa: tuple,
                      with_pencil: bool = True, factor_det: bool = True) -> dict:
    """THE PRINCIPAL-PART OBJECTS OF ONE CONSTRUCTION: H0, D(kappa), B, det B,
    the form block B B^T and the pencil block H_e^-1 B H_o^-1 B^T.  At the
    fully symbolic cell form det B is left EXPANDED rather than factored
    (factor_det=False): the identity gates below compare expanded polynomials."""
    h0 = folded_matrix(rules_h, dim)
    dk = first_order_matrix(raising, dim, kappa)
    block, h_e, h_o, parity = bipartite_block(h0, dk, dim)
    raw_det = block.det(method="berkowitz")
    det_b = sp.factor(sp.cancel(raw_det)) if factor_det else sp.expand(raw_det)
    form_block = (block * block.T).applyfunc(sp.cancel)
    pencil_block = None
    if with_pencil and sp.cancel(h_e.det()) != 0 and sp.cancel(h_o.det()) != 0:
        pencil_block = (h_e.inv() * block * h_o.inv() * block.T).applyfunc(sp.cancel)
    return {"h0": h0, "dk": dk, "B": block, "H_e": h_e, "H_o": h_o, "parity": parity,
            "detB": det_b, "form": form_block, "pencil": pencil_block}


def linear_branches(charpoly, kappa: tuple) -> tuple:
    """The linear-in-lam factors of a charpoly in lam, i.e. the eigenvalue
    branches that ARE polynomials (quadratic forms) in kappa, and the
    remaining factor's degree structure."""
    _, factors = sp.factor_list(sp.expand(charpoly), LAM)
    branches, remainder = [], []
    for base, power in factors:
        poly = sp.Poly(base, LAM)
        if poly.degree() == 1:
            root = sp.cancel(-poly.coeff_monomial(1) / poly.coeff_monomial(LAM))
            branches.append((sp.expand(root), power))
        elif poly.degree() >= 2:
            remainder.append((poly.degree(), power))
    return tuple(branches), tuple(remainder)


def measure_principal(cell_matrices: dict) -> PrincipalFacts:
    """FAMILY F, MEASURED ONCE: the symbolic lemmas and the witnesses."""
    kappa3 = (KT, KX, KY)
    kappa2 = (KT, KX)
    signature = sp.diag(1, -1, 1)
    lane3, lane2 = lane_rules(3), lane_rules(2)
    d3, d2 = raising_rules(lane3), raising_rules(lane2)

    # --- THE ONSITE CONE LEMMA AT FULLY SYMBOLIC D --------------------------
    D0, D3 = sp.symbols("D0 D3", positive=True)
    a = sp.symbols("a11 a12 a13 a22 a23 a33", real=True)
    b = sp.symbols("b11 b12 b13 b22 b23 b33", real=True)
    D1 = sp.Matrix([[a[0], a[1], a[2]], [a[1], a[3], a[4]], [a[2], a[4], a[5]]])
    D2 = sp.Matrix([[b[0], b[1], b[2]], [b[1], b[3], b[4]], [b[2], b[4], b[5]]])
    cell = sp.zeros(8, 8)
    cell[0, 0], cell[7, 7] = D0, D3
    unit = [b209.CORNERS.index(tuple(1 if k == mu else 0 for k in range(3))) for mu in range(3)]
    complement = [b209.CORNERS.index(tuple(0 if k == mu else 1 for k in range(3))) for mu in range(3)]
    for i in range(3):
        for j in range(3):
            cell[unit[i], unit[j]] = D1[i, j]
            cell[complement[i], complement[j]] = D2[i, j]
    # FRACTION-FREE, BECAUSE THE FIRST DRAFT's GENERIC 4 x 4 PENCIL WITH
    # SYMBOLIC 3 x 3 INVERSES RAN THE BASELINE PAST THE CACHE TIMEOUT: every
    # identity below is an exact polynomial identity in the seventeen symbols,
    # with adjugates in place of inverses, and the transverse product is taken
    # on the symbolic Block 211 family, where the inverses are small.
    objects = principal_objects(onsite_rules(cell, b209.CORNERS, 3), d3, 3, kappa3,
                                with_pencil=False, factor_det=False)
    q1 = quadratic_form(D1, kappa3)
    q2_adj = quadratic_form(signature * D2.adjugate() * signature, kappa3)
    lemma_3d = sp.expand(objects["detB"] - D3 * q1 * q2_adj) == 0
    d0_absent = D0 not in objects["detB"].free_symbols
    # THE BLOCK STRUCTURE OF B: rows (0-form | three 2-forms), columns (three
    # 1-forms | 3-form).  B = [[k^T D1, 0], [D2 W, D3 E k]] with W the wedge
    # block of D(kappa) and, because d^2 = 0, W k = 0 and (E k)^T W = 0.  The
    # 1-form corners in odd-corner order are (y, x, t), so D1 and k are read
    # in that order there; the 2-form corners in even order are (t, x, y).
    block = objects["B"]
    even, odd = even_odd(3)
    cs = corners(3)
    zero_form_position = even.index(cs.index((0, 0, 0)))
    two_form_positions = [j for j in range(4) if j != zero_form_position]
    top_form_position = odd.index(cs.index((1, 1, 1)))
    one_form_positions = [j for j in range(4) if j != top_form_position]
    d1_odd = objects["H_o"].extract(one_form_positions, one_form_positions)
    d2_even = objects["H_e"].extract(two_form_positions, two_form_positions)
    k_odd = sp.Matrix([kappa3[[c for c in range(3) if cs[odd[p]][c] == 1][0]]
                       for p in one_form_positions])
    e_k = signature * sp.Matrix(kappa3)
    wedge = objects["dk"].extract([even[p] for p in two_form_positions],
                                  [odd[p] for p in one_form_positions])
    structure = (
        residual_count(block.extract([zero_form_position], one_form_positions) - k_odd.T * d1_odd) == 0
        and block[zero_form_position, top_form_position] == 0
        and residual_count(block.extract(two_form_positions, one_form_positions) - d2_even * wedge) == 0
        and residual_count(block.extract(two_form_positions, [top_form_position]) - D3 * e_k) == 0
        and residual_count(wedge * k_odd) == 0
        and residual_count(e_k.T * wedge) == 0)
    # THE PENCIL BLOCK BY BLOCK.  P = H_e^-1 B H_o^-1 B^T = diag(q1/D0, T) with
    # T = W D1^-1 W^T D2 + D3 D2^-1 (Ek)(Ek)^T.  Fraction-free:
    #   det(D1) . k^T D1 adj(D1) D1 k = det(D1)^2 q1      (the 0-form entry),
    #   the off-diagonal blocks carry (W k)^T and W k, hence vanish,
    #   T' = det(D1) det(D2) T = det(D2) W adj(D1) W^T D2 + D3 det(D1) adj(D2)(Ek)(Ek)^T,
    #   T' adj(D2) E k = D3 det(D1) (k^T E adj(D2) E k) adj(D2) E k     (the top form).
    det1, det2 = sp.expand(d1_odd.det()), sp.expand(d2_even.det())
    adj1, adj2 = d1_odd.adjugate(), d2_even.adjugate()
    zero_form_branch = sp.expand((k_odd.T * d1_odd * adj1 * d1_odd * k_odd)[0, 0] - det1 * q1) == 0
    block_diagonal = (structure
                      and residual_count((k_odd.T * d1_odd * adj1 * wedge.T * d2_even).applyfunc(sp.expand)) == 0
                      and residual_count((d2_even * wedge * k_odd).applyfunc(sp.expand)) == 0)
    t_prime = (det2 * wedge * adj1 * wedge.T * d2_even
               + D3 * det1 * adj2 * e_k * e_k.T).applyfunc(sp.expand)
    eigenvector = adj2 * e_k
    top_form_branch = residual_count(
        (t_prime * eigenvector - D3 * det1 * q2_adj * eigenvector).applyfunc(sp.expand)) == 0
    # THE TRANSVERSE PRODUCT, on the symbolic Block 211 family (all-plus class):
    # det(T)/q2 = det(D2)/det(D1) (k^T D1 k)(k^T E D2^-1 E k).
    g0f, g1f, v0f, v1f = sp.symbols("g0 g1 v0 v1", positive=True)
    family_plus = formal_family(b211.ALL_PLUS, g0f, g1f, v0f, v1f)
    objects_f = principal_objects(onsite_rules(family_plus, b209.CORNERS, 3), d3, 3, kappa3)
    pencil_f = objects_f["pencil"]
    _, d1_f, d2_f = objects_f["H_e"][zero_form_position, zero_form_position], \
        objects_f["H_o"].extract(one_form_positions, one_form_positions), \
        objects_f["H_e"].extract(two_form_positions, two_form_positions)
    q1_f = quadratic_form(d1_f, k_odd)
    q2_f = sp.cancel(objects_f["H_o"][top_form_position, top_form_position]
                     * quadratic_form(signature * d2_f.inv() * signature, kappa3))
    two_form_f = pencil_f.extract(two_form_positions, two_form_positions)
    transverse_product = (
        all(is_zero(pencil_f[zero_form_position, j]) and is_zero(pencil_f[j, zero_form_position])
            for j in two_form_positions)
        and is_zero(pencil_f[zero_form_position, zero_form_position]
                    - q1_f / objects_f["H_e"][zero_form_position, zero_form_position])
        and is_zero(sp.cancel(two_form_f.det() / q2_f)
                    - sp.cancel(d2_f.det() / d1_f.det() * q1_f
                                * quadratic_form(signature * d2_f.inv() * signature, kappa3))))
    # THE EXPANSION ITSELF, MEASURED AND NOT ASSUMED: K_H,B(z) = i eps M(kappa)
    # + O(eps^2) with M = H0 D + D^T H0 requires the folded raising part and
    # the folded K_H to vanish and the first-order coefficient of the COMPOSED
    # rules H d - d^T H to equal H0 D + D^T H0, which must be symmetric (K_H is
    # antisymmetric, so its Bloch matrix is anti-Hermitian and i eps M is).
    # Measured at the fully symbolic cell form under BOTH assemblies.
    expansion_exact = True
    dT3 = transpose_rules(d3)
    dk_symbolic = first_order_matrix(d3, 3, kappa3)
    for assembly_rules in (onsite_rules, overlap_rules):
        rules_h_cell = assembly_rules(cell, b209.CORNERS, 3)
        kh_rules = combine_rules(compose_rules(rules_h_cell, d3),
                                 compose_rules(dT3, rules_h_cell), -1)
        h0_cell = folded_matrix(rules_h_cell, 3)
        m_cell = (h0_cell * dk_symbolic + dk_symbolic.T * h0_cell).applyfunc(sp.expand)
        expansion_exact = (
            expansion_exact
            and residual_count(folded_matrix(d3, 3)) == 0
            and residual_count(folded_matrix(kh_rules, 3)) == 0
            and residual_count(first_order_matrix(kh_rules, 3, kappa3) - m_cell) == 0
            and residual_count(m_cell - m_cell.T) == 0
            and combine_rules(kh_rules, transpose_rules(kh_rules)) == {})
    # --- THE 2D LEMMA -------------------------------------------------------
    e0, e2 = sp.symbols("e0 e2", positive=True)
    p = sp.symbols("p11 p12 p22", real=True)
    P1 = sp.Matrix([[p[0], p[1]], [p[1], p[2]]])
    cell2 = sp.zeros(4, 4)
    cell2[0, 0], cell2[3, 3] = e0, e2
    for i, ci in enumerate((1, 2)):
        for j, cj in enumerate((1, 2)):
            cell2[ci, cj] = P1[i, j]
    objects2 = principal_objects(onsite_rules(cell2, b201.CELL_CORNERS, 2), d2, 2, kappa2)
    # corners 1 = (0,1) = the x step, 2 = (1,0) = the t step: k' = (kx, kt)
    q1_2d = quadratic_form(P1, (KX, KT))
    lemma_2d = is_zero(objects2["detB"] + e2 * q1_2d)

    # --- THE OVERLAP H0 FORM AND CONE, SYMBOLIC ------------------------------
    v0, v1, g0, g1 = sp.symbols("v0 v1 g0 g1", positive=True)
    s = sp.symbols("s_tx0 s_ty0 s_xy0 s_tx1 s_ty1 s_xy1")
    signs = {("tx", 0): s[0], ("ty", 0): s[1], ("xy", 0): s[2],
             ("tx", 1): s[3], ("ty", 1): s[4], ("xy", 1): s[5]}
    family = sp.zeros(8, 8)
    family[0, 0], family[7, 7] = v0, 1 / v1
    first = v1 * b211.signed_triangle((signs[("xy", 0)] * g0, signs[("ty", 0)] * g0, signs[("tx", 0)] * g0))
    second = b211.signed_triangle((signs[("tx", 1)] * g1, signs[("ty", 1)] * g1, signs[("xy", 1)] * g1)) / v0
    ones, twos = b209.DEGREE_INDICES[1], b209.DEGREE_INDICES[2]
    for i in range(3):
        for j in range(3):
            family[ones[i], ones[j]] = first[i, j]
            family[twos[i], twos[j]] = second[i, j]
    h_folded = folded_matrix(overlap_rules(family, b209.CORNERS, 3), 3)
    h0_expected = (v0 + 3 * v1 + 3 / v0 + 1 / v1) / 8
    h_expected = {"tx": -(signs[("tx", 0)] * v1 * g0 + signs[("tx", 1)] * g1 / v0) / 8,
                  "ty": -(signs[("ty", 0)] * v1 * g0 + signs[("ty", 1)] * g1 / v0) / 8,
                  "xy": -(signs[("xy", 0)] * v1 * g0 + signs[("xy", 1)] * g1 / v0) / 8}
    flips = {"tx": (1, 1, 0), "ty": (1, 0, 1), "xy": (0, 1, 1)}
    h0_form_ok = True
    cs = corners(3)
    for i, ci in enumerate(cs):
        for j, cj in enumerate(cs):
            difference = tuple((ci[k] + cj[k]) % 2 for k in range(3))
            if i == j:
                target = h0_expected
            elif difference in flips.values():
                plane = [name for name, flip in flips.items() if flip == difference][0]
                target = 2 * h_expected[plane]
            else:
                target = 0
            if not is_zero(h_folded[i, j] - target):
                h0_form_ok = False
    h0s, htx, hty, hxy = sp.symbols("h0 htx hty hxy", real=True)
    rules_h_symbolic = {}
    for corner in cs:
        rules_h_symbolic[(corner, (0, 0, 0))] = h0s
        for delta, h in (((1, -1, 0), htx), ((-1, 1, 0), htx), ((1, 0, -1), hty),
                         ((-1, 0, 1), hty), ((0, 1, -1), hxy), ((0, -1, 1), hxy)):
            rules_h_symbolic[(corner, delta)] = h
    overlap_objects = principal_objects(rules_h_symbolic, d3, 3, kappa3)
    local = {"h0": h0s, "htx": htx, "hty": hty, "hxy": hxy, "kt": KT, "kx": KX, "ky": KY}
    q_plus = sp.sympify(OVERLAP_CONE_PLUS, locals=local)
    q_minus = sp.sympify(OVERLAP_CONE_MINUS, locals=local)
    # THE SIGN IS PINNED, NOT LEFT AS +-: det B = +Q+ Q- exactly.
    overlap_cone_3d = is_zero(overlap_objects["detB"] - q_plus * q_minus)
    rules_h2 = {}
    for corner in corners(2):
        rules_h2[(corner, (0, 0))] = h0s
        rules_h2[(corner, (1, -1))] = htx
        rules_h2[(corner, (-1, 1))] = htx
    overlap_objects2 = principal_objects(rules_h2, d2, 2, kappa2)
    q_2d = sp.sympify(OVERLAP_CONE_2D, locals=local)
    overlap_cone_2d = is_zero(overlap_objects2["detB"] + h0s * q_2d)

    # --- TWO DIRECTIONS AT SYMBOLIC (c, v): BLOCK 105's OWN CELL FORM -------
    c, v = sp.symbols("c v", positive=True)
    face = sp.expand(sp.Matrix(b211.LANDED_SHEAR_HODGE(c, v)))
    local2 = {"c": c, "v": v, "kt": KT, "kx": KX}
    branch_targets = [sp.sympify(text, locals=local2) for text in TWO_DIM_ONSITE_BRANCHES]
    on2 = principal_objects(onsite_rules(face, b201.CELL_CORNERS, 2), d2, 2, kappa2)
    pencil2 = on2["pencil"]
    onsite_branches_ok = (
        is_zero(pencil2[0, 1]) and is_zero(pencil2[1, 0])
        and ((is_zero(pencil2[0, 0] - branch_targets[0]) and is_zero(pencil2[1, 1] - branch_targets[1]))
             or (is_zero(pencil2[0, 0] - branch_targets[1]) and is_zero(pencil2[1, 1] - branch_targets[0]))))
    onsite_form_scalar = is_scalar_matrix(on2["form"])
    onsite_pencil_scalar_generic = is_scalar_matrix(pencil2)
    # THE HONEST-VOLUME LOCUS v^2 = 1 - c^2, substituted exactly: the pencil
    # entries are even in v, so the substitution leaves rational functions of c.
    onsite_scalar_on_locus = is_scalar_matrix(
        pencil2.applyfunc(lambda entry: sp.radsimp(sp.cancel(entry.subs(v, sp.sqrt(1 - c ** 2))))))
    ov2 = principal_objects(overlap_rules(face, b201.CELL_CORNERS, 2), d2, 2, kappa2)
    pencil_ov2 = ov2["pencil"]
    overlap_pencil_scalar = is_scalar_matrix(pencil_ov2)
    overlap_target = sp.sympify(TWO_DIM_OVERLAP_PENCIL, locals=local2)
    overlap_pencil_matches = is_zero(pencil_ov2[0, 0] - overlap_target)
    hodge_cone = sp.sympify(TWO_DIM_HODGE_CONE, locals=local2)
    overlap_form_scalar = is_scalar_matrix(ov2["form"])
    abs_a = 3 * v ** 2 + 1 - c ** 2 * (v ** 2 + 1)
    overlap_cone_target = abs_a * (KT ** 2 + KX ** 2) - 4 * c * v ** 2 * KT * KX
    overlap_cone_matches = proportional(ov2["detB"], overlap_cone_target, (KT, KX))
    effective = sp.sympify(TWO_DIM_OVERLAP_EFFECTIVE_SHEAR, locals=local2)
    normalized = sp.expand(overlap_cone_target / abs_a)
    effective_ok = is_zero(-sp.Poly(normalized, KT, KX).coeff_monomial(KT * KX) / 2 - effective)
    discrepancy = sp.sympify(TWO_DIM_OVERLAP_SHEAR_DISCREPANCY, locals=local2)
    discrepancy_ok = is_zero(effective - c - discrepancy) and not is_zero(discrepancy)
    # THE EXACT TWO-DIRECTION SYMBOLS, DISPLAYED: the graded pencil symbol is
    # block-diagonal by degree at symbolic (c, v, z); its 0-form and 2-form
    # entries are scalars.  The overlap pencil symbol is translation-invariant
    # in two directions and is displayed at W1's own face (c, v) = (1/4, 15/16).
    z2 = sp.symbols("zt zx")
    pencil_sym, _ = onsite_pencil_symbol(face, b201.CELL_CORNERS, 2, z2, d2)
    zero_form_symbol = sp.cancel(pencil_sym[0, 0])
    two_form_symbol = sp.cancel(pencil_sym[3, 3])
    w1_face = sp.expand(sp.Matrix(b211.LANDED_SHEAR_HODGE(sp.Rational(1, 4), sp.Rational(15, 16))))
    h_bo = bloch_matrix(overlap_rules(w1_face, b201.CELL_CORNERS, 2), z2, 2)
    d_b = bloch_matrix(d2, z2, 2)
    dT_b = bloch_matrix(transpose_rules(d2), z2, 2)
    pencil_sym_o, _ = pencil_symbol_with_inverse(h_bo, h_bo.inv().applyfunc(sp.cancel), d_b, dT_b)
    row_sums = [sp.cancel(sum(pencil_sym_o[i, j] for j in range(4))) for i in range(4)]
    overlap_scalar_symbol = (sp.factor(row_sums[0]) if all(is_zero(r - row_sums[0]) for r in row_sums)
                             else "NOT-TRANSLATION-INVARIANT")

    # --- THREE DIRECTIONS AT THE WITNESSES ----------------------------------
    witness_records = []
    onsite_cones_ok, onsite_branches_ok3, overlap_never = True, True, True
    scalar_at_listed_witnesses, transverse_split_names = False, []
    w1_onsite_ok = w1_overlap_ok = False
    w1_zero_form = ""
    local3 = {"kt": KT, "kx": KX, "ky": KY}
    for name in WITNESS_NAMES:
        cell_w = cell_matrices[name]
        g1_m, g2_m, _, _, _, _ = metric_candidates(cell_w)
        cone1 = quadratic_form(g1_m, kappa3) if g1_m is not None else None
        cone2 = quadratic_form(g2_m, kappa3) if g2_m is not None else None
        for assembly in ASSEMBLIES:
            rules_h = (onsite_rules if assembly == "onsite" else overlap_rules)(cell_w, b209.CORNERS, 3)
            objects_w = principal_objects(rules_h, d3, 3, kappa3)
            factors = primitive_factors(objects_w["detB"], kappa3)
            # THE RANK OF EACH CONE FACTOR'S HESSIAN: 3 for a genuine cone, 2
            # when the cone has degenerated to a line (the PD boundary).
            factor_texts = tuple(
                f"({sp.expand(base)})^{power} [hessian rank {sp.hessian(base, kappa3).rank()}]"
                for base, power in factors)
            pencil_w = objects_w["pencil"]
            branches, remainder = (linear_branches(charpoly_expr(pencil_w), kappa3)
                                   if pencil_w is not None else ((), ()))
            form_branches, form_remainder = linear_branches(charpoly_expr(objects_w["form"]), kappa3)
            scalar_pencil = pencil_w is not None and is_scalar_matrix(pencil_w)
            scalar_form = is_scalar_matrix(objects_w["form"])
            cones_are_g1_g2 = None
            branches_are_g1_g2 = None
            if cone1 is not None and cone2 is not None and name != "flat":
                cone_bases = [base for base, _ in factors]
                cones_are_g1_g2 = (len(cone_bases) == 2
                                   and any(proportional(base, cone1, kappa3) for base in cone_bases)
                                   and any(proportional(base, cone2, kappa3) for base in cone_bases))
                if pencil_w is not None:
                    branch_values = [value for value, _ in branches]
                    branches_are_g1_g2 = (any(is_zero(value - cone1) for value in branch_values)
                                          and any(is_zero(value - cone2) for value in branch_values))
                if assembly == "onsite":
                    onsite_cones_ok = onsite_cones_ok and bool(cones_are_g1_g2)
                    if pencil_w is not None:
                        onsite_branches_ok3 = onsite_branches_ok3 and bool(branches_are_g1_g2)
                        # THE TRANSVERSE PAIR: it is a pair of quadratic-form
                        # branches only where the remaining quadratic factor
                        # SPLITS over QQ, which is recorded by witness name.
                        if len(branches) > 2:
                            transverse_split_names.append(name)
                else:
                    overlap_never = overlap_never and not any(
                        proportional(base, cone1, kappa3) or proportional(base, cone2, kappa3)
                        for base in cone_bases)
                if scalar_pencil or scalar_form:
                    scalar_at_listed_witnesses = True
            if name == "W1":
                bases = [sp.expand(base) for base, _ in factors]
                targets = [sp.sympify(text, locals=local3) for text in
                           (W1_ONSITE_CONES if assembly == "onsite" else W1_OVERLAP_CONES)]
                matched = all(any(proportional(base, target, kappa3) for base in bases) for target in targets)
                if assembly == "onsite":
                    w1_onsite_ok = matched and len(bases) == 2
                    z3 = sp.symbols("zt zx zy")
                    pencil_sym3, _ = onsite_pencil_symbol(cell_w, b209.CORNERS, 3, z3, d3)
                    w1_zero_form = str(sp.factor(pencil_sym3[0, 0]))
                else:
                    w1_overlap_ok = matched and len(bases) == 2
            witness_records.append((name, assembly, factor_texts,
                                    tuple((str(value), power) for value, power in branches), remainder,
                                    tuple((str(value), power) for value, power in form_branches), form_remainder,
                                    scalar_pencil, scalar_form, cones_are_g1_g2, branches_are_g1_g2,
                                    objects_w["parity"], str(cone1), str(cone2)))

    # A curved overlap point can nevertheless have scalar H0 and scalar
    # principal pencil.  Opposite offset signs cancel every two-flip
    # coefficient h_f when v1*g0 = g1/v0.  This exact positive-definite point
    # prevents the finite witness scan above from being promoted to a
    # universal non-scalarity theorem.
    counter_signs = dict(zip(FACES, (1, 1, 1, -1, -1, -1)))
    counter_cell = formal_family(
        counter_signs,
        sp.Rational(3, 8),
        sp.Rational(1, 3),
        sp.sqrt(110) / 12,
        16 * sp.sqrt(110) / 165,
    )
    counter_objects = principal_objects(
        overlap_rules(counter_cell, b209.CORNERS, 3), d3, 3, kappa3)
    overlap_scalar_counterexample = (
        all(sp.radsimp(value) > 0 for value in b211.leading_minors(counter_cell))
        and is_scalar_matrix(counter_objects["h0"])
        and residual_count(
            counter_objects["pencil"]
            - (KT ** 2 + KX ** 2 + KY ** 2) * sp.eye(4)) == 0)

    # --- COINCIDENCE OF THE TWO HODGE READINGS, (1) THE CHART, FAIL-CLOSED ----
    # The ideal of the proportionality minors on each class representative's
    # (t, u) chart is reduced to a lex Groebner basis and its REAL zeros are
    # taken exactly; a positive-dimensional real component would come back as
    # a marker and fail the gate, where sp.solve would have dropped it.
    t, u = b211.CHART_T, b211.CHART_U
    chart_bases, solutions, classes = [], set(), 0
    for orientation, class_signs in b211.REPRESENTATIVES.items():
        _, matrix, rhs = b211.face_system(b211.chart_moduli(class_signs))
        chart_cell, _ = b211.solve_pinned(matrix, rhs)
        g1_c, g2_c, _, _, _, _ = metric_candidates(chart_cell)
        basis = sp.groebner(proportionality_minors(g1_c, g2_c), t, u, order="lex")
        chart_bases.append(tuple(str(sp.factor(g)) for g in basis.exprs))
        for solution in real_solutions_lex(list(basis.exprs), t, u):
            solutions.add(solution)
        classes += 1
    chart_bases_equal = len(set(chart_bases)) == 1

    # --- (2) THE SIXTY-FOUR-CELL CENSUS AT SYMBOLIC MODULI, AND (3) THE CLOSED FORM
    # The weighted kernel is not invariant under Block 211's corner-sign gauge
    # (E d E is not d), so the four representatives do not speak for the
    # sixty-four sign cells.  Every cell is run at symbolic (v0, g0, v1, g1)
    # on Block 211's degree-block formulas, and the closed form of
    # P = M1(g0) E M2(g1) E is verified in the cells where S1 = -+ E S0 E.
    g0s, g1s, v0s, v1s = sp.symbols("g0 g1 v0 v1", positive=True)
    census: dict = {}
    rule_a_cells, rule_b_cells, curve_cells = [], [], []
    closed_form_ok, curve_solutions_ok = True, True
    for bits in itertools.product((1, -1), repeat=6):
        cell_signs = dict(zip(FACES, bits))
        pi0 = bits[0] * bits[1] * bits[2]
        pi1 = bits[3] * bits[4] * bits[5]
        fam = formal_family(cell_signs, g0s, g1s, v0s, v1s)
        g1_f, g2_f, _, d1_f, d2_f, _ = metric_candidates(fam)
        basis = sp.groebner(proportionality_minors(g1_f, g2_f), g0s, g1s, order="lex")
        elements = [str(sp.factor(g)) for g in basis.exprs]
        key = "(" + ", ".join(elements) + (",)" if len(elements) == 1 else ")")
        entry = census.setdefault(key, [0, set()])
        entry[0] += 1
        entry[1].add((pi0, pi1))
        if key != "(g0, g1)":
            curve_cells.append(bits)
        m1 = (d1_f / v1s).applyfunc(sp.cancel)
        m2 = (d2_f * v0s).applyfunc(sp.cancel)
        s0 = ((sp.eye(3) - m1) / g0s).applyfunc(sp.cancel)
        s1 = ((sp.eye(3) - m2) / g1s).applyfunc(sp.cancel)
        p = (m1 * signature * m2 * signature).applyfunc(sp.expand)
        if residual_count(s1 + signature * s0 * signature) == 0:
            rule_a_cells.append(bits)
            target = (1 - 2 * g0s * g1s) * sp.eye(3) + (g1s - g0s - pi0 * g0s * g1s) * s0
            closed_form_ok = closed_form_ok and residual_count(p - target) == 0
            # THE CURVE, SOLVED WITHOUT sp.solve: it is degree one in g0, so its
            # root is unique, and the root is verified by exact substitution
            # (sp.solve would silently drop a root that violates the symbols'
            # positivity assumptions -- which is exactly rule B's root).
            curve = g1s - g0s - pi0 * g0s * g1s
            curve_solutions_ok = (curve_solutions_ok and sp.Poly(curve, g0s).degree() == 1
                                  and is_zero(curve.subs(g0s, g1s / (1 + pi0 * g1s))))
        elif residual_count(s1 - signature * s0 * signature) == 0:
            rule_b_cells.append(bits)
            target = (1 + 2 * g0s * g1s) * sp.eye(3) - (g0s + g1s - pi0 * g0s * g1s) * s0
            closed_form_ok = closed_form_ok and residual_count(p - target) == 0
            curve = g0s + g1s - pi0 * g0s * g1s
            curve_solutions_ok = (curve_solutions_ok and sp.Poly(curve, g0s).degree() == 1
                                  and is_zero(curve.subs(g0s, -g1s / (1 - pi0 * g1s))))
    census_tuple = tuple(sorted(
        (key, count, tuple(sorted(cls))) for key, (count, cls) in census.items()))
    rules_cover_curves = set(curve_cells) == set(rule_a_cells) | set(rule_b_cells)

    # --- (4) THE LOCUS WITNESSES over QQ(sqrt 6), through Block 211's solve ---
    locus_pd, locus_prop, locus_one_cone, locus_split, locus_ov_never = True, True, True, True, True
    locus_mu, locus_prefactors, locus_constants, locus_ov_counts = [], [], [], []
    for name in LOCUS_WITNESS_NAMES:
        cell_l = cell_matrices[name]
        locus_pd = locus_pd and all(sp.radsimp(m) > 0 for m in b211.leading_minors(cell_l))
        g1_l, g2_l, _, _, _, _ = metric_candidates(cell_l)
        g1_l, g2_l = g1_l.applyfunc(sp.radsimp), g2_l.applyfunc(sp.radsimp)
        cone_l = quadratic_form(g1_l, kappa3)
        mu = sp.radsimp(g2_l[0, 0] / g1_l[0, 0])
        locus_mu.append(mu)
        locus_prop = locus_prop and residual_count((g2_l - mu * g1_l).applyfunc(sp.radsimp)) == 0
        on_l = principal_objects(onsite_rules(cell_l, b209.CORNERS, 3), d3, 3, kappa3)
        locus_prefactors.append(sp.radsimp(sp.cancel(on_l["detB"] / cone_l ** 2)))
        factors_l = primitive_factors(sp.radsimp(sp.expand(on_l["detB"])), kappa3)
        locus_one_cone = (locus_one_cone and len(factors_l) == 1 and factors_l[0][1] == 2
                          and proportional(factors_l[0][0], cone_l, kappa3))
        pencil_l = on_l["pencil"].applyfunc(sp.radsimp)
        branches_l, remainder_l = linear_branches(charpoly_expr(pencil_l), kappa3)
        constants = []
        for value, power in branches_l:
            constants.extend([sp.radsimp(sp.cancel(value / cone_l))] * power)
        # FAIL CLOSED BY FAMILY (checker finding CK-09): a k-dependent ratio means the
        # witness is off the locus; record a marker instead of sorting expressions
        # that cannot be ordered, so that gate F-8 fails rather than measure().
        k_free_l = all(not (sp.sympify(c).free_symbols & set(kappa3)) for c in constants)
        locus_constants.append(tuple(sorted(constants, key=sp.default_sort_key)) if k_free_l
                               else ("K-DEPENDENT-RATIO",))
        locus_split = locus_split and remainder_l == () and len(constants) == 4 and k_free_l
        ov_l = principal_objects(overlap_rules(cell_l, b209.CORNERS, 3), d3, 3, kappa3, False)
        ov_factors = primitive_factors(sp.radsimp(sp.expand(ov_l["detB"])), kappa3)
        locus_ov_counts.append(len(ov_factors))
        locus_ov_never = (locus_ov_never and len(ov_factors) == 2
                          and all(power == 1 for _, power in ov_factors)
                          and not any(proportional(base, cone_l, kappa3) for base, _ in ov_factors))

    # --- (5) THE LOCUS, SYMBOLICALLY ALONG THE CURVE, with free volumes then the ties
    symbolic_one_cone, symbolic_k_free, symbolic_match, mu_match = True, True, True, True
    symbolic_constants, mu_minus_one = [], []
    locus_signs = locus_witness_table()
    for name, pi0 in (("L+-", 1), ("L-+", -1)):
        _, signs_l = locus_signs[name]
        g0_curve = g1s / (1 + pi0 * g1s)
        fam = formal_family(signs_l, g0_curve, g1s, v0s, v1s)
        g1_f, _, _, _, _, _ = metric_candidates(fam)
        cone_f = quadratic_form(g1_f, kappa3)
        on_f = principal_objects(onsite_rules(fam, b209.CORNERS, 3), d3, 3, kappa3)
        fac_f = primitive_factors(on_f["detB"], kappa3)
        symbolic_one_cone = (symbolic_one_cone and len(fac_f) == 1 and fac_f[0][1] == 2
                             and proportional(fac_f[0][0], cone_f, kappa3))
        branches_f, remainder_f = linear_branches(charpoly_expr(on_f["pencil"]), kappa3)
        ties = {v0s: sp.sqrt((1 - g0_curve ** 2) * (1 - g1s ** 2)),
                v1s: sp.sqrt((1 - g1s ** 2) / (1 - g0_curve ** 2))}
        tied = []
        for value, power in branches_f:
            ratio = sp.cancel(value / cone_f)
            symbolic_k_free = symbolic_k_free and not (ratio.free_symbols & set(kappa3))
            tied.extend([sp.factor(sp.cancel(ratio.subs(ties)))] * power)
        symbolic_k_free = symbolic_k_free and remainder_f == () and len(tied) == 4
        expected = [sp.Integer(1),
                    (1 + 2 * pi0 * g1s) / ((1 - pi0 * g1s) * (1 + pi0 * g1s) ** 3),
                    1 / (1 - g1s ** 2), 1 / (1 - g1s ** 2)]
        remaining = list(tied)
        for target in expected:
            hit = next((c for c in remaining if is_zero(c - target)), None)
            if hit is None:
                symbolic_match = False
            else:
                remaining.remove(hit)
        symbolic_constants.append(tuple(str(c) for c in tied))
        mu_f = expected[1]
        difference = sp.factor(mu_f - 1)
        mu_minus_one.append(str(difference))
        mu_match = mu_match and is_zero(
            difference - pi0 * g1s ** 3 * (2 + pi0 * g1s) / ((1 - pi0 * g1s) * (1 + pi0 * g1s) ** 3)) \
            and not is_zero(difference)
    return PrincipalFacts(
        lemma_3d, lemma_2d, block_diagonal, zero_form_branch, top_form_branch, transverse_product,
        d0_absent, expansion_exact, h0_form_ok, overlap_cone_3d, overlap_cone_2d,
        onsite_branches_ok, onsite_form_scalar, onsite_pencil_scalar_generic, onsite_scalar_on_locus,
        overlap_pencil_scalar, overlap_pencil_matches, overlap_cone_matches, overlap_form_scalar,
        effective_ok, discrepancy_ok, str(zero_form_symbol), str(two_form_symbol), str(overlap_scalar_symbol),
        tuple(witness_records), w1_onsite_ok, w1_overlap_ok, onsite_cones_ok, onsite_branches_ok3,
        overlap_never, scalar_at_listed_witnesses, overlap_scalar_counterexample,
        tuple(transverse_split_names),
        tuple(chart_bases), chart_bases_equal,
        tuple(sorted(solutions, key=lambda s: (str(s[0]), str(s[1])))), classes,
        census_tuple, sum(count for _, count, _ in census_tuple),
        len(rule_a_cells), len(rule_b_cells), rules_cover_curves, closed_form_ok, curve_solutions_ok,
        locus_pd, locus_prop, tuple(locus_mu), locus_one_cone,
        tuple(locus_prefactors), tuple(locus_constants), locus_split,
        tuple(locus_ov_counts), locus_ov_never,
        symbolic_one_cone, symbolic_k_free, tuple(symbolic_constants), symbolic_match,
        tuple(mu_minus_one), mu_match,
        w1_zero_form)


def measure_registration() -> RegistrationFacts:
    """FAMILY G, MEASURED ONCE: does the shear enter, does the volume enter."""
    kappa3 = (KT, KX, KY)
    v0, v1, g0, g1 = sp.symbols("v0 v1 g0 g1", positive=True)
    lane3 = lane_rules(3)
    d3 = raising_rules(lane3)
    signature = sp.diag(1, -1, 1)
    results = {}
    for class_signs in (b211.ALL_PLUS, b211.flipped(("xy", 0), ("xy", 1))):
        family = sp.zeros(8, 8)
        family[0, 0], family[7, 7] = v0, 1 / v1
        first = v1 * b211.signed_triangle((class_signs[("xy", 0)] * g0, class_signs[("ty", 0)] * g0, class_signs[("tx", 0)] * g0))
        second = b211.signed_triangle((class_signs[("tx", 1)] * g1, class_signs[("ty", 1)] * g1, class_signs[("xy", 1)] * g1)) / v0
        ones, twos = b209.DEGREE_INDICES[1], b209.DEGREE_INDICES[2]
        for i in range(3):
            for j in range(3):
                family[ones[i], ones[j]] = first[i, j]
                family[twos[i], twos[j]] = second[i, j]
        g1_m, g2_m, _, _, _, _ = metric_candidates(family)
        cone1 = quadratic_form(g1_m, kappa3)
        cone2 = quadratic_form(g2_m, kappa3)
        results[str(class_signs[("xy", 0)])] = (cone1, cone2)
        onsite = principal_objects(onsite_rules(family, b209.CORNERS, 3), d3, 3, kappa3, False)
        overlap = principal_objects(overlap_rules(family, b209.CORNERS, 3), d3, 3, kappa3, False)
        results[("onsite", str(class_signs[("xy", 0)]))] = onsite["detB"]
        results[("overlap", str(class_signs[("xy", 0)]))] = overlap["detB"]
    cone1_plus, cone2_plus = results["1"]
    det_onsite = results[("onsite", "1")]
    det_overlap = results[("overlap", "1")]
    # SHEAR MOVES THE CONE, THE VOLUMES DO NOT: exact derivatives, and the
    # exact proportionality of det B to its own value at unit volumes.
    onsite_shear = (
        (not is_zero(sp.diff(cone1_plus, g0))) and (not is_zero(sp.diff(cone2_plus, g1)))
        and not proportional(det_onsite, det_onsite.subs({g0: 0, g1: 0}), kappa3))
    onsite_volume_free = proportional(det_onsite, det_onsite.subs({v0: 1, v1: 1}), kappa3)
    triangle_one = first_block(g0, b211.ALL_PLUS)
    triangle_two = second_block(g1, b211.ALL_PLUS)
    scales = (str(sp.cancel(cone1_plus / quadratic_form(triangle_one, kappa3))),
              str(sp.cancel(cone2_plus / quadratic_form(
                  signature * triangle_two.inv() * signature, kappa3))))
    # THE OVERLAP SYMBOL DEPENDS ON THE MODULI ONLY THROUGH (h0, h_f): the
    # zero-shear pencil symbol is R5's for every volume pair, the zero-shear
    # form symbol is h0^2 times R5's.
    z3 = sp.symbols("zt zx zy")
    family0 = sp.diag(v0, v1, v1, 1 / v0, v1, 1 / v0, 1 / v0, 1 / v1)
    rules0 = overlap_rules(family0, b209.CORNERS, 3)
    h_b = bloch_matrix(rules0, z3, 3)
    d_b = bloch_matrix(d3, z3, 3)
    dT_b = bloch_matrix(transpose_rules(d3), z3, 3)
    h0_value = sp.cancel((v0 + 3 * v1 + 3 / v0 + 1 / v1) / 8)
    depends_only_on_h = residual_count(h_b - h0_value * sp.eye(8)) == 0
    pencil0, _ = pencil_symbol_with_inverse(h_b, sp.eye(8) / h0_value, d_b, dT_b)
    form0, _ = form_symbol(h_b, d_b, dT_b)
    k_b = bloch_matrix(lane3, z3, 3)
    r5 = (-k_b * k_b).applyfunc(sp.expand)
    zero_shear_pencil_r5 = depends_only_on_h and residual_count(pencil0 - r5) == 0
    zero_shear_form_scale = "h0^2 times R5" if residual_count(form0 - h0_value ** 2 * r5) == 0 else "NOT h0^2 R5"
    overlap_shear = (
        (not is_zero(sp.diff(det_overlap, g0))) and (not is_zero(sp.diff(det_overlap, g1)))
        and not proportional(det_overlap, det_overlap.subs({g0: 0, g1: 0}), kappa3))
    sign_class_moves = not proportional(det_overlap, results[("overlap", "-1")], kappa3)
    return RegistrationFacts(onsite_shear, onsite_volume_free, scales, depends_only_on_h,
                             zero_shear_pencil_r5, zero_shear_form_scale, overlap_shear, sign_class_moves)


def first_block(g0, class_signs):
    return b211.signed_triangle((class_signs[("xy", 0)] * g0, class_signs[("ty", 0)] * g0, class_signs[("tx", 0)] * g0))


def second_block(g1, class_signs):
    return b211.signed_triangle((class_signs[("tx", 1)] * g1, class_signs[("ty", 1)] * g1, class_signs[("xy", 1)] * g1))


def measure() -> Facts:
    note_text = NOTE_PATH.read_text(encoding="utf-8") if NOTE_PATH.is_file() else ""
    witnesses = dict(witness_table())
    witnesses.update(locus_witness_table())
    construction, cell_matrices = measure_construction(witnesses)
    return Facts(
        CORRECTION_SOURCE_BASE,
        authority_certificate(),
        len(IMPOSED_OBJECTS),
        len(REGISTERED_OBJECTS),
        len(ADOPTED_OBJECTS),
        len(UNSUPPLIED_GRAVITY_STRUCTURES),
        len(READINGS),
        len(SCOPED_HEADLINE_WORDS),
        construction,
        measure_control(),
        measure_spectra(cell_matrices),
        measure_principal(cell_matrices),
        measure_registration(),
        scope_certificate(note_text),
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
        "source_base": CORRECTION_SOURCE_BASE,
        "source_inputs_match": True,
        "source_inputs_readable": True,
        # B
        "imposed": len(IMPOSED_OBJECTS),
        "registered": 0,
        "adopted": 0,
        "gravity_supplied": GRAVITY_SUPPLIED_CLAIMED,
        "unsupplied": len(UNSUPPLIED_GRAVITY_STRUCTURES),
        "symbol_is_dynamics": SYMBOL_IS_DYNAMICS_CLAIMED,
        "propagator": PROPAGATOR_CLAIMED,
        "cone_is_spacetime_cone": CONE_IS_SPACETIME_CONE_CLAIMED,
        "scoped_words": len(SCOPED_HEADLINE_WORDS),
        "assembly_selected": ASSEMBLY_SELECTED_CLAIMED,
        "generic_parameter_theorem": GENERIC_PARAMETER_THEOREM_CLAIMED,
        "continuum_limit": CONTINUUM_LIMIT_CLAIMED,
        "readings": len(READINGS),
        "readings_licensed": READINGS_LICENSED_CLAIMED,
        # C
        "lane_2d_nnz": LANE_2D_NNZ,
        "spin_nonscalar_2d": SPIN_NONSCALAR_2D,
        "lane_2d_fidelity": True,
        "lane_3d_links": LANE_3D_LINKS_SCANNED,
        "lane_3d_bad": LANE_3D_BAD_LINKS,
        "lane_3d_nnz": LANE_3D_NNZ,
        "lane_3d_shadow": True,
        "assemblers_reproduce_source": True,
        "cell_forms_reconciled": True,
        "witness_count": WITNESS_COUNT,
        "compatible_ranks": COMPATIBLE_RANKS,
        "flat_h_identity": FLAT_H_IS_IDENTITY,
        "flat_kernel_is_r5": FLAT_KERNEL_IS_R5,
        # D
        "flat_symbol_identity": True,
        "flat_multiset_2d": FLAT_MULTISET_2D,
        "flat_multiset_3d": FLAT_MULTISET_3D,
        # E
        "bloch_equals_bench": True,
        "w1_overlap_pencil_2d": W1_OVERLAP_PENCIL_2D,
        "boundary_onsite_singular_3d": BOUNDARY_ONSITE_H_SINGULAR_3D,
        "boundary_onsite_singular_2d": BOUNDARY_ONSITE_H_SINGULAR_2D,
        # F
        "onsite_lemma_3d": True,
        "onsite_lemma_2d": True,
        "onsite_lemma_structure": True,
        "overlap_h0_form": True,
        "overlap_cone_3d": True,
        "overlap_cone_2d": True,
        "two_dim_onsite_branches": True,
        "two_dim_onsite_scalar_generic": False,
        "two_dim_onsite_scalar_on_locus": True,
        "two_dim_overlap_pencil_scalar": True,
        "two_dim_overlap_matches": True,
        "two_dim_effective_shear": True,
        "three_dim_branches": True,
        "w1_cones": True,
        "principal_scalar_at_listed_curved_3d": PRINCIPAL_PART_SCALAR_AT_LISTED_CURVED_3D_WITNESSES,
        "overlap_scalar_counterexample": True,
        "locus_symbol_scalar": LOCUS_SYMBOL_SCALAR,
        "transverse_split_witnesses": TRANSVERSE_SPLIT_RATIONAL_WITNESSES,
        "transverse_splits_on_locus": TRANSVERSE_SPLITS_ON_LOCUS,
        "onsite_cones_g1_g2": True,
        "overlap_cones_never_g1_g2": True,
        "coincidence_chart_groebner": COINCIDENCE_CHART_GROEBNER,
        "coincidence_solutions": COINCIDENCE_SOLUTIONS,
        "coincidence_classes": COINCIDENCE_CLASSES,
        "sign_cells": SIGN_CELLS,
        "coincidence_census": COINCIDENCE_CENSUS,
        "locus_rule_a_cells": LOCUS_RULE_A_CELLS,
        "locus_rule_b_cells": LOCUS_RULE_B_CELLS,
        "locus_positive_cells": LOCUS_POSITIVE_CELLS,
        "coincidence_only_at_flat_everywhere": COINCIDENCE_ONLY_AT_FLAT_IN_EVERY_CELL,
        "cone_is_one_metric_cone_everywhere": CONE_IS_ONE_METRIC_CONE_EVERYWHERE,
        "cone_is_one_metric_cone_on_locus": CONE_IS_ONE_METRIC_CONE_ON_LOCUS,
        "locus_mu": LOCUS_MU,
        "locus_det_prefactors": LOCUS_DET_PREFACTORS,
        "locus_branch_constants": LOCUS_BRANCH_CONSTANTS,
        "locus_symbolic": True,
        # G
        "shear_enters_onsite": SHEAR_ENTERS_CONE_ONSITE,
        "shear_enters_overlap": SHEAR_ENTERS_CONE_OVERLAP,
        "volume_enters_onsite_cone": VOLUME_ENTERS_CONE_ONSITE,
        "overlap_zero_shear_pencil_r5": OVERLAP_ZERO_SHEAR_PENCIL_IS_R5,
        "tension_recorded": TENSION_RECORDED,
        # H
        "scout_grade_only": SCOUT_GRADE_ONLY,
        "physical_content": PHYSICAL_CONTENT_CLAIMED,
        "assembly_decided": ASSEMBLY_DECIDED,
        "hodge_reading_selected": HODGE_READING_SELECTED,
        "instance_scope": INSTANCE_SCOPE_COUNT,
        # I
        "note_present": True,
        "scope": {key: True for key in SCOPE_KEYS},
        "nsimplify_calls": 0,
        "float_literals": 0,
        "float_calls": 0,
    }

    # --- A ----------------------------------------------------------------
    if mutation == "break_source_input_hash":
        claims["source_inputs_match"] = False
    elif mutation == "break_source_input_readability":
        claims["source_inputs_readable"] = False
    # --- B ----------------------------------------------------------------
    elif mutation == "claim_objects_registered":
        claims["registered"] = 1
        claims["adopted"] = 1
    elif mutation == "claim_gravity_supplied":
        claims["gravity_supplied"] = True
        claims["unsupplied"] = 0
    elif mutation == "claim_symbol_is_dynamics":
        # THE FIRST MISREAD: the squared symbol of a finite antisymmetric
        # matrix is asserted to be a dynamics or a propagator.
        claims["symbol_is_dynamics"] = True
        claims["propagator"] = True
    elif mutation == "claim_cone_is_spacetime_cone":
        # THE SECOND MISREAD: the zero set of det B is asserted to be a
        # light cone.  It is a homogeneous polynomial's zero set.
        claims["cone_is_spacetime_cone"] = True
        claims["scoped_words"] = 0
    elif mutation == "claim_assembly_selected":
        claims["assembly_selected"] = True
    elif mutation == "claim_readings_licensed":
        claims["readings_licensed"] = True
        claims["generic_parameter_theorem"] = True
        claims["continuum_limit"] = True
    # --- C ----------------------------------------------------------------
    elif mutation == "break_lane_kernel_fidelity":
        # THE CHAIN DENIED: the lane kernel is asserted NOT to be Block 201's.
        claims["lane_2d_fidelity"] = False
        claims["lane_2d_nnz"] = 48
    elif mutation == "break_three_direction_shadow":
        claims["lane_3d_bad"] = 8
        claims["lane_3d_shadow"] = False
    elif mutation == "break_assembler_fidelity":
        claims["assemblers_reproduce_source"] = False
    elif mutation == "break_cell_form_reconciliation":
        claims["cell_forms_reconciled"] = False
        claims["compatible_ranks"] = (32, 33)
    elif mutation == "break_flat_cell_identity":
        # THE CONTROL DENIED: the flat cell is asserted to give a kernel
        # DIFFERENT from R5's.  It gives R5's exactly, in all four constructions.
        claims["flat_h_identity"] = False
        claims["flat_kernel_is_r5"] = False
    # --- D ----------------------------------------------------------------
    elif mutation == "break_flat_symbol_identity":
        claims["flat_symbol_identity"] = False
    elif mutation == "break_flat_bench_multiset":
        claims["flat_multiset_3d"] = ((0, 4), (1, 8), (2, 4))
    # --- E ----------------------------------------------------------------
    elif mutation == "break_bloch_bench_agreement":
        claims["bloch_equals_bench"] = False
    elif mutation == "break_witness_spectra":
        claims["w1_overlap_pencil_2d"] = ((0, 4), (1, 8), (2, 4))
    elif mutation == "break_boundary_edge_case":
        # THE FIRST DRAFT's CLAIM, ASSERTED: singular on BOTH benches.
        claims["boundary_onsite_singular_2d"] = True
    # --- F ----------------------------------------------------------------
    elif mutation == "break_onsite_cone_lemma":
        # THE LEMMA DENIED: det B is asserted to depend on D0 and not to
        # factor into the two Hodge readings.
        claims["onsite_lemma_3d"] = False
        claims["onsite_lemma_structure"] = False
    elif mutation == "break_overlap_cone_formula":
        claims["overlap_cone_3d"] = False
        claims["overlap_h0_form"] = False
    elif mutation == "break_two_dim_branches":
        claims["two_dim_onsite_branches"] = False
        claims["two_dim_overlap_matches"] = False
    elif mutation == "break_three_dim_branch_identification":
        claims["three_dim_branches"] = False
        claims["w1_cones"] = False
    elif mutation == "claim_principal_part_scalar":
        # Assert scalarity at the finite listed witness set, where the exact
        # matrices are non-scalar.  A separate exact point below shows why
        # this finite statement cannot be upgraded to all curved points.
        claims["principal_scalar_at_listed_curved_3d"] = True
        claims["two_dim_onsite_scalar_generic"] = True
        claims["locus_symbol_scalar"] = True
    elif mutation == "claim_cone_is_metric_cone":
        # R5's HYPOTHESIS AS STATED: the cone is asserted to be ONE metric's
        # cone at EVERY curved point.  It is that only on the locus; elsewhere
        # the union of two distinct cones, and under the overlap assembly a
        # non-Hodge pair everywhere measured.
        claims["cone_is_one_metric_cone_everywhere"] = True
        claims["overlap_cones_never_g1_g2"] = False
    elif mutation == "break_coincidence_census":
        # THE PREDECESSOR SEAT's OVERREACH, ASSERTED: coincidence only at flat
        # in EVERY sign cell.  The census finds sixteen curve cells, eight of
        # them positive.
        claims["coincidence_only_at_flat_everywhere"] = True
        claims["coincidence_census"] = (("(g0, g1)", 64, ((-1, -1), (-1, 1), (1, -1), (1, 1))),)
        claims["locus_positive_cells"] = 0
    elif mutation == "break_coincidence_locus":
        # THE LOCUS DENIED: the two locus witnesses are asserted to carry the
        # union of two distinct cones with equal readings (mu = 1).
        claims["cone_is_one_metric_cone_on_locus"] = False
        claims["locus_mu"] = (sp.Integer(1), sp.Integer(1))
        claims["locus_branch_constants"] = ((1, 1, 1, 1), (1, 1, 1, 1))
        claims["transverse_splits_on_locus"] = False
    # --- G ----------------------------------------------------------------
    elif mutation == "break_shear_registration":
        claims["shear_enters_onsite"] = False
        claims["shear_enters_overlap"] = False
    elif mutation == "claim_volume_registration":
        # THE #7970 MIRROR MISREAD: the volumes are asserted to move the
        # graded cone and the zero-shear overlap symbol.  They do neither.
        claims["volume_enters_onsite_cone"] = True
        claims["overlap_zero_shear_pencil_r5"] = False
    elif mutation == "drop_tension_record":
        claims["tension_recorded"] = False
    # --- H ----------------------------------------------------------------
    elif mutation == "break_scout_grade_fence":
        claims["scout_grade_only"] = False
        claims["physical_content"] = True
    elif mutation == "claim_assembly_decided":
        claims["assembly_decided"] = True
    elif mutation == "claim_hodge_reading_selected":
        claims["hodge_reading_selected"] = True
    elif mutation == "break_instance_scope":
        claims["instance_scope"] = 0
    # --- I ----------------------------------------------------------------
    elif mutation == "drop_n5_fence":
        claims["scope"] = {key: False for key in SCOPE_KEYS}
    elif mutation == "break_nsimplify_absence":
        claims["nsimplify_calls"] = 1
    elif mutation == "break_float_absence":
        claims["float_literals"] = 1
        claims["float_calls"] = 1
    return claims


def build_checks(facts: Facts, claims: dict) -> Checks:
    checks = Checks()
    authority = facts.authority
    build = facts.construction
    control = facts.control
    spectra = facts.spectra
    principal = facts.principal
    registration = facts.registration
    cells = {cell.name: cell for cell in build.cells}

    # --- A: SOURCE-INPUT CLOSURE --------------------------------------------
    checks.check(
        "A-1", f"the correction source base is {claims['source_base']}; all "
        f"non-self runtime and citation inputs match fixed SHA-256 literals; "
        f"the runner cap is {AUDIT_TIMEOUT_SEC}s",
        authority.source_base == claims["source_base"]
        and authority.fixed_source_inputs == claims["source_inputs_match"]
        and claims["source_inputs_match"])
    checks.check(
        "A-2", "the bounded recovery helper and current Block 105 import; "
        "the complete declared source/citation closure is readable; "
        f"{authority.inputs_readable} of {len(AUDIT_INPUT_PATHS) - 1} audit "
        "inputs other than the self note are readable",
        authority.machinery_import_available
        and authority.inputs_readable == len(AUDIT_INPUT_PATHS) - 1
        and not authority.inputs_missing
        and claims["source_inputs_readable"])

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
        "B-3", f"THE WORD *SYMBOL* IS SCOPED BEFORE THE FIRST NUMERAL: it names "
        f"the exact 2^d x 2^d Bloch matrix of a finite antisymmetric kernel on "
        f"a periodic bench and its eigenvalue branches; symbol_is_dynamics = "
        f"{claims['symbol_is_dynamics']}, propagator = {claims['propagator']}",
        claims["symbol_is_dynamics"] is False and claims["propagator"] is False)
    checks.check(
        "B-4", f"THE WORD *CONE* IS SCOPED: it names the zero set of det B(kappa), "
        f"a homogeneous polynomial in three formal variables, and NO light cone, "
        f"NO causal structure and NO spacetime; cone_is_spacetime_cone = "
        f"{claims['cone_is_spacetime_cone']}, and {claims['scoped_words']} "
        f"headline words {SCOPED_HEADLINE_WORDS} are scoped before any number, "
        f"the words {UNNAMED_PHYSICS_WORDS} naming NOTHING established here",
        claims["cone_is_spacetime_cone"] is False
        and facts.scoped_words == claims["scoped_words"])
    checks.check(
        "B-5", f"THE ASSEMBLY IS NOT SELECTED BY THIS BLOCK: the fixed Block 105 source defines BOTH "
        f"the onsite and the overlap assembly and the recovered completion uses "
        f"the overlap one; both are run and both are reported; "
        f"assembly_selected = {claims['assembly_selected']}",
        claims["assembly_selected"] is False)
    checks.check(
        "B-6", f"NO GENERIC-PARAMETER THEOREM AND NO CONTINUUM LIMIT, AND THE "
        f"READINGS ARE READINGS: {claims['readings']} of them are enumerated, "
        f"readings_licensed = {claims['readings_licensed']}, and EVERY NEGATIVE "
        f"HERE IS NON-SUPPLY WITHIN THIS FORMALISM AND NEVER METAPHYSICAL "
        f"NECESSITY -- the cycle-913 caution, carried verbatim, with nothing "
        f"registered and nothing adopted",
        claims["generic_parameter_theorem"] is False
        and claims["continuum_limit"] is False
        and facts.readings == claims["readings"]
        and claims["readings_licensed"] is False
        and not REGISTERED_OBJECTS and not ADOPTED_OBJECTS
        and claims["registered"] == 0 and claims["adopted"] == 0)

    # --- C: THE CONSTRUCTION'S FIDELITY TO THE CHAIN --------------------------
    checks.check(
        "C-1", f"THE 2D LANE KERNEL IS BLOCK 201's: on (4,4) the eta-staggered "
        f"rules give Block 201's lane_kernel exactly ({build.lane_2d_matches_b201}) "
        f"with {claims['lane_2d_nnz']} nonzero entries, it is site-sign-equivalent "
        f"to Block 201's spin-diagonalised covariant kernel "
        f"({build.lane_2d_site_sign_equivalent}) which has "
        f"{claims['spin_nonscalar_2d']} non-scalar blocks, the graded raising "
        f"part equals Block 201's raising_part on its (8,4) fork extent "
        f"({build.raising_matches_b201_on_fork}), and K = d - d^T with d^2 = 0 "
        f"({build.k_is_d_minus_dT_2d}, {build.d_squared_zero_2d})",
        build.lane_2d_matches_b201 is claims["lane_2d_fidelity"]
        and claims["lane_2d_fidelity"] is True
        and build.lane_2d_nnz == claims["lane_2d_nnz"]
        and build.spin_nonscalar_2d == claims["spin_nonscalar_2d"]
        and build.lane_2d_site_sign_equivalent
        and build.raising_matches_b201_on_fork
        and build.k_is_d_minus_dT_2d and build.d_squared_zero_2d)
    checks.check(
        "C-2", f"THE 3D LANE KERNEL IS BLOCK 209's SHADOW, LINK BY LINK: on "
        f"(4,2,2) all {claims['lane_3d_links']} directed links scalarise under "
        f"Omega = G1^t G2^x G3^y with {claims['lane_3d_bad']} bad links and every "
        f"scalar equal to the rule's eta_d / 2 ({build.lane_3d_shadow_matches}); "
        f"the bench kernel has {claims['lane_3d_nnz']} nonzero entries because "
        f"the extent-2 directions carry NO antisymmetric link "
        f"({build.lane_3d_xy_links_absent}) -- R5's (4,2,2) structure -- and "
        f"K = d - d^T, d^2 = 0 ({build.k_is_d_minus_dT_3d}, {build.d_squared_zero_3d})",
        build.lane_3d_links_scanned == claims["lane_3d_links"]
        and build.lane_3d_bad_links == claims["lane_3d_bad"]
        and build.lane_3d_shadow_matches is claims["lane_3d_shadow"]
        and claims["lane_3d_shadow"] is True
        and build.lane_3d_nnz == claims["lane_3d_nnz"]
        and build.lane_3d_xy_links_absent
        and build.k_is_d_minus_dT_3d and build.d_squared_zero_3d)
    checks.check(
        "C-3", f"THE ASSEMBLERS REPRODUCE THE FIXED SOURCE HODGES DIGIT FOR DIGIT: "
        f"Block 201's fork_hodge on (8,4) at c = {b201.FORK_SHEAR if b201 else '?'} "
        f"({build.fork_hodge_reproduced}), Block 105's onsite_hodge "
        f"({build.onsite_hodge_reproduced}) and overlap_hodge "
        f"({build.overlap_hodge_reproduced}), and the rule-based onsite and "
        f"overlap assemblies equal the bench assemblies of a uniform cell "
        f"({build.rules_match_bench_assembly})",
        (build.fork_hodge_reproduced and build.onsite_hodge_reproduced
         and build.overlap_hodge_reproduced and build.rules_match_bench_assembly)
        is claims["assemblers_reproduce_source"]
        and claims["assemblers_reproduce_source"] is True)
    checks.check(
        "C-4", f"THE CELL FORMS ARE BLOCK 211's, RECONCILED: all "
        f"{claims['witness_count']} witnesses solve at ranks "
        f"{claims['compatible_ranks']} with free names D07, D16, D25, D34, the "
        f"degree blocks equal Block 211's formulas [v0], v1 M1, M2/v0, [1/v1] "
        f"with zero cross-degree entries, the origin tx face equals Block 105's "
        f"shear_hodge(s_tx0 g0, v0), and PD holds exactly at "
        f"{PD_WITNESSES} -- the two QQ(sqrt 6) locus witnesses included -- and "
        f"fails at the boundary",
        len(build.cells) == claims["witness_count"]
        and all(cell.ranks == claims["compatible_ranks"] for cell in build.cells)
        and all(cell.free_names == ("D07", "D16", "D25", "D34") for cell in build.cells)
        and all(cell.blocks_match_formulas and cell.cross_degree_zero
                and cell.face_restriction_is_shear_hodge for cell in build.cells)
        is claims["cell_forms_reconciled"]
        and claims["cell_forms_reconciled"] is True
        and all(cells[name].positive_definite for name in PD_WITNESSES)
        and not cells["boundary"].positive_definite)
    checks.check(
        "C-5", f"THE FLAT CELL IS THE CONTROL'S CELL: at (c, v) = (0, 1) and at "
        f"Block 211's flat point both assemblies give H = I on both benches "
        f"({build.flat_h_identity}) and K_H = K exactly ({build.flat_kernel_is_r5})",
        build.flat_h_identity is claims["flat_h_identity"]
        and build.flat_kernel_is_r5 is claims["flat_kernel_is_r5"]
        and claims["flat_h_identity"] is True and claims["flat_kernel_is_r5"] is True)

    # --- D: THE R5 CONTROL ----------------------------------------------------
    checks.check(
        "D-1", f"R5's FLAT SYMBOL IS AN EXACT POLYNOMIAL IDENTITY: -K_B(z)^2 = "
        f"({FLAT_SYMBOL_FORM}) times the identity in two "
        f"({control.flat_symbol_identity_2d}) and three "
        f"({control.flat_symbol_identity_3d}) directions",
        (control.flat_symbol_identity_2d and control.flat_symbol_identity_3d)
        is claims["flat_symbol_identity"]
        and claims["flat_symbol_identity"] is True)
    checks.check(
        "D-2", f"AND THE BENCH MULTISETS ARE R5's, WITH MULTIPLICITIES: on (4,4) "
        f"{claims['flat_multiset_2d']} and on (4,2,2) {claims['flat_multiset_3d']}, "
        f"equal to {{sum_d sin^2(2 pi m_d / N_d)}} computed exactly, from the "
        f"direct bench charpoly and from the Bloch union alike "
        f"({control.bloch_equals_direct_flat})",
        control.multiset_2d == tuple((sp.Integer(a), b) for a, b in claims["flat_multiset_2d"])
        and control.multiset_3d == tuple((sp.Integer(a), b) for a, b in claims["flat_multiset_3d"])
        and control.expected_2d == control.multiset_2d
        and control.expected_3d == control.multiset_3d
        and control.bloch_equals_direct_flat)

    # --- E: THE EXACT SPECTRA AT THE WITNESSES ---------------------------------
    defined = [entry for entry in spectra.entries if entry[6] is not None or entry[4] != "UNDEFINED: det H = 0"]
    checks.check(
        "E-1", f"BLOCH UNION = DIRECT BENCH, EVERY TIME: {len(defined)} "
        f"(witness, bench, assembly, reading) charpolys of degree 16 agree "
        f"exactly between the product of 2^d x 2^d Bloch charpolys at exact "
        f"roots of unity and the direct 16 x 16 bench matrix "
        f"({spectra.all_agree}); translation covariance of -K_H^2 at W1, as "
        f"nnz([-K_H^2, T_mu]) per direction: {spectra.translation_commutators}",
        spectra.all_agree is claims["bloch_equals_bench"]
        and claims["bloch_equals_bench"] is True
        and all(entry[5] for entry in spectra.entries))
    checks.check(
        "E-2", f"W1's OWN (4,4) SPECTRUM, DECLARED: the overlap H-pencil "
        f"reading has the exact multiset {claims['w1_overlap_pencil_2d']} "
        f"against R5's {FLAT_MULTISET_2D} -- only the (pi/2, pi/2)-type momenta "
        f"move; every other witness spectrum is printed as its factored "
        f"charpoly above",
        spectra.w1_overlap_pencil_2d == tuple(
            (sp.sympify(a), b) for a, b in claims["w1_overlap_pencil_2d"]))
    checks.check(
        "E-3", f"THE PD BOUNDARY IS A THREE-DIRECTION EDGE CASE, MEASURED: at "
        f"gamma0 = gamma1 = 1/2 all-plus the onsite H is SINGULAR on (4,2,2) "
        f"({spectra.boundary_onsite_singular_3d}; the triangle determinant "
        f"(1 + g)^2 (1 - 2g) vanishes) so the H-pencil reading is undefined there "
        f"while the form reading stays defined, and REGULAR on (4,4) "
        f"({spectra.boundary_onsite_singular_2d} singular; the origin tx face is "
        f"Block 105's shear_hodge at c = 1/2 with 2 x 2 block determinant "
        f"v0^2/(1 - c^2), the two-direction PD condition being |c| < 1); the "
        f"overlap H stays regular on both ({spectra.boundary_overlap_regular})",
        spectra.boundary_onsite_singular_3d is claims["boundary_onsite_singular_3d"]
        and claims["boundary_onsite_singular_3d"] is True
        and spectra.boundary_onsite_singular_2d is claims["boundary_onsite_singular_2d"]
        and claims["boundary_onsite_singular_2d"] is False
        and spectra.boundary_overlap_regular)

    # --- F: THE PRINCIPAL PART AND THE CONE ------------------------------------
    checks.check(
        "F-1", f"THE ONSITE CONE LEMMA, AT FULLY SYMBOLIC D: {ONSITE_CONE_LEMMA_3D} "
        f"({principal.lemma_3d_holds}) and in two directions {ONSITE_CONE_LEMMA_2D} "
        f"({principal.lemma_2d_holds}); D0 is absent from det B "
        f"({principal.lemma_d0_absent}); B = [[k^T D1, 0], [D2 W, D3 E k]] with "
        f"W k = 0 and (E k)^T W = 0 so the pencil principal block is block-diagonal "
        f"by form degree ({principal.lemma_3d_block_diagonal}) with the 0-form "
        f"branch k^T D1 k / D0 ({principal.lemma_3d_zero_form_branch}) and the "
        f"eigenvector adj(D2) E k at eigenvalue D3 k^T E D2^-1 E k "
        f"({principal.lemma_3d_top_form_branch}), all as fraction-free polynomial "
        f"identities in the seventeen symbols; and on the symbolic Block 211 "
        f"family the transverse product is det(D2)/det(D1) (k^T D1 k)(k^T E D2^-1 E k) "
        f"({principal.lemma_3d_transverse_product}); "
        f"and the expansion K_H,B(z) = i eps M + O(eps^2), M = H0 D + D^T H0 "
        f"symmetric, is MEASURED from the composed rules at the symbolic cell "
        f"under both assemblies ({principal.expansion_exact})",
        (principal.lemma_3d_holds and principal.lemma_2d_holds) is claims["onsite_lemma_3d"]
        and claims["onsite_lemma_3d"] is True
        and (principal.lemma_d0_absent and principal.lemma_3d_block_diagonal
             and principal.lemma_3d_zero_form_branch and principal.lemma_3d_top_form_branch
             and principal.lemma_3d_transverse_product
             and principal.expansion_exact) is claims["onsite_lemma_structure"]
        and claims["onsite_lemma_structure"] is True)
    checks.check(
        "F-2", f"THE OVERLAP CONE, AT SYMBOLIC h: the folded overlap H0 is "
        f"{OVERLAP_H0_FORM} ({principal.overlap_h0_form_holds}); det B = +Q+ Q- "
        f"exactly, sign pinned, with Q+ = {OVERLAP_CONE_PLUS} and Q- = {OVERLAP_CONE_MINUS} "
        f"({principal.overlap_cone_3d_holds}), and in two directions det B = "
        f"-h0 ({OVERLAP_CONE_2D}) ({principal.overlap_cone_2d_holds})",
        principal.overlap_h0_form_holds is claims["overlap_h0_form"]
        and claims["overlap_h0_form"] is True
        and (principal.overlap_cone_3d_holds and principal.overlap_cone_2d_holds)
        is claims["overlap_cone_3d"]
        and claims["overlap_cone_3d"] is True)
    checks.check(
        "F-3", f"TWO DIRECTIONS AT SYMBOLIC (c, v), BLOCK 105's OWN CELL FORM: the "
        f"graded H-pencil principal symbol has EXACTLY the branches "
        f"{TWO_DIM_ONSITE_BRANCHES} ({principal.two_dim_onsite_branches}) -- the "
        f"Hodge reading's cone k^T (D1/D0) k and det(g)/v^2 times it -- so the "
        f"cone IS the cell metric's cone there; the overlap H-pencil principal "
        f"symbol is the scalar {TWO_DIM_OVERLAP_PENCIL} times the identity "
        f"({principal.two_dim_overlap_pencil_scalar}, {principal.two_dim_overlap_pencil_matches}) "
        f"with cone {principal.two_dim_overlap_cone_matches and 'h0(kt^2+kx^2)+4 htx kt kx'}",
        principal.two_dim_onsite_branches is claims["two_dim_onsite_branches"]
        and claims["two_dim_onsite_branches"] is True
        and (principal.two_dim_overlap_pencil_scalar and principal.two_dim_overlap_pencil_matches
             and principal.two_dim_overlap_cone_matches) is claims["two_dim_overlap_matches"]
        and claims["two_dim_overlap_matches"] is True
        and claims["two_dim_overlap_pencil_scalar"] is True)
    checks.check(
        "F-4", f"AND THE OVERLAP CONE DIFFERS FROM THE DECLARED HODGE READING AT POSITIVE NONZERO SHEAR: its effective shear is "
        f"{TWO_DIM_OVERLAP_EFFECTIVE_SHEAR} ({principal.two_dim_effective_shear}), "
        f"the same sign as the Hodge reading's c but never its magnitude, with "
        f"the exact discrepancy c_K - c = {TWO_DIM_OVERLAP_SHEAR_DISCREPANCY} "
        f"({principal.two_dim_discrepancy}), nonzero in the stated positive-definite c != 0 range",
        principal.two_dim_effective_shear is claims["two_dim_effective_shear"]
        and claims["two_dim_effective_shear"] is True
        and principal.two_dim_discrepancy)
    checks.check(
        "F-5", f"THREE DIRECTIONS AT EACH LISTED CURVED WITNESS: under the graded "
        f"assembly det B factors EXACTLY into the two Hodge readings' cones "
        f"k^T G1 k and k^T G2 k ({principal.onsite_cones_are_g1_g2_everywhere}) "
        f"and both are exact H-pencil branches ({principal.onsite_branches_g1_g2_everywhere}); "
        f"at W1 the cones are {W1_ONSITE_CONES} ({principal.w1_onsite_cones}) "
        f"and under the overlap assembly {W1_OVERLAP_CONES} ({principal.w1_overlap_cones}); "
        f"the overlap cones are proportional to NEITHER reading at any curved "
        f"rational witness ({principal.overlap_cones_never_g1_g2})",
        (principal.onsite_cones_are_g1_g2_everywhere and principal.onsite_branches_g1_g2_everywhere)
        is claims["three_dim_branches"]
        and claims["three_dim_branches"] is True
        and (principal.w1_onsite_cones and principal.w1_overlap_cones) is claims["w1_cones"]
        and claims["w1_cones"] is True
        and principal.overlap_cones_never_g1_g2 is claims["overlap_cones_never_g1_g2"]
        and claims["overlap_cones_never_g1_g2"] is True)
    checks.check(
        "F-6", f"SCALARITY IS RESOLVED ONLY ON THE DECLARED MATRICES: none of "
        f"the listed curved three-direction witness matrices is scalar "
        f"(principal_scalar_at_listed_curved_3d = "
        f"{claims['principal_scalar_at_listed_curved_3d']}), while the exact "
        f"opposite-offset-sign point g0=3/8, g1=1/3, v0=sqrt(110)/12, "
        f"v1=16 sqrt(110)/165 is positive definite and has overlap pencil "
        f"(kt^2+kx^2+ky^2) I ({principal.overlap_scalar_counterexample}); "
        f"the transverse 2-form pair "
        f"splits into two quadratic-form branches at exactly the curved rational "
        f"witnesses {claims['transverse_split_witnesses']} -- honest_face, offset-1 "
        f"shear zero, D2 isotropic -- and is an irreducible quadratic at the other "
        f"five (measured {principal.transverse_split_witnesses}); ON the "
        f"coincidence locus the cone is one quadric but the symbol is STILL not "
        f"scalar, because mu - 1 = {LOCUS_MU_MINUS_ONE} is a nonzero rational "
        f"function of g1 ({principal.locus_mu_minus_one_matches}; measured "
        f"{principal.locus_mu_minus_one}), locus_symbol_scalar = "
        f"{claims['locus_symbol_scalar']}; in two directions the graded symbol is scalar exactly on "
        f"{TWO_DIM_ONSITE_SCALAR_LOCUS} ({principal.two_dim_onsite_scalar_on_locus}) "
        f"and not as a generic symbolic identity ({principal.two_dim_onsite_pencil_scalar_generic}); "
        f"the two symbolic form matrices are likewise not scalar identities "
        f"({principal.two_dim_onsite_form_scalar}, {principal.two_dim_overlap_form_scalar}); "
        f"special parameter values are not excluded",
        principal.principal_scalar_at_listed_curved_3d_witnesses
        is claims["principal_scalar_at_listed_curved_3d"]
        and claims["principal_scalar_at_listed_curved_3d"] is False
        and principal.overlap_scalar_counterexample
        is claims["overlap_scalar_counterexample"]
        and principal.transverse_split_witnesses == tuple(claims["transverse_split_witnesses"])
        and principal.locus_mu_minus_one_matches
        and claims["locus_symbol_scalar"] is False
        and principal.two_dim_onsite_scalar_on_locus is claims["two_dim_onsite_scalar_on_locus"]
        and principal.two_dim_onsite_pencil_scalar_generic is claims["two_dim_onsite_scalar_generic"]
        and claims["two_dim_onsite_scalar_generic"] is False
        and not principal.two_dim_onsite_form_scalar
        and not principal.two_dim_overlap_form_scalar)
    checks.check(
        "F-7", f"THE COINCIDENCE THEOREM: on the four class representatives' (t, u) "
        f"chart the proportionality ideal of (G1, G2) has the lex Groebner basis "
        f"{claims['coincidence_chart_groebner']} in every class "
        f"({principal.coincidence_chart_bases_equal}) with real zeros EXACTLY "
        f"{claims['coincidence_solutions']} -- the flat point -- taken fail-closed over "
        f"{claims['coincidence_classes']} classes; BUT the weighted kernel is not "
        f"corner-sign-gauge invariant, and the census over all {claims['sign_cells']} "
        f"sign cells at symbolic moduli is {claims['coincidence_census']}: "
        f"{COINCIDENCE_FLAT_ONLY_CELLS} cells coincide only at flat and "
        f"{COINCIDENCE_CURVE_CELLS} carry a curve, exactly the {claims['locus_rule_a_cells']} "
        f"rule-A cells [{LOCUS_RULE_A}] and the {claims['locus_rule_b_cells']} rule-B cells "
        f"[{LOCUS_RULE_B}] ({principal.rules_cover_curve_cells}), with the closed form of "
        f"M1 E M2 E verified in each ({principal.closed_form_ok}) and both curves solved "
        f"exactly ({principal.curve_solutions_ok}); {claims['locus_positive_cells']} cells carry "
        f"a positive-definite-solvable coincidence curve; coincidence_only_at_flat_everywhere = "
        f"{claims['coincidence_only_at_flat_everywhere']}, cone_is_one_metric_cone_everywhere = "
        f"{claims['cone_is_one_metric_cone_everywhere']}",
        principal.coincidence_chart_bases_equal
        and principal.coincidence_chart_bases[0] == claims["coincidence_chart_groebner"]
        and principal.coincidence_solutions == tuple(
            (sp.sympify(a), sp.sympify(b)) for a, b in claims["coincidence_solutions"])
        and principal.coincidence_classes == claims["coincidence_classes"]
        and principal.census_cells == claims["sign_cells"]
        and principal.census == tuple(sorted(claims["coincidence_census"]))
        and principal.rule_a_cells == claims["locus_rule_a_cells"]
        and principal.rule_b_cells == claims["locus_rule_b_cells"]
        and principal.rules_cover_curve_cells
        and principal.closed_form_ok and principal.curve_solutions_ok
        and claims["locus_positive_cells"] == principal.rule_a_cells
        and claims["coincidence_only_at_flat_everywhere"] is False
        and claims["cone_is_one_metric_cone_everywhere"] is False
        and principal.onsite_cones_are_g1_g2_everywhere)
    checks.check(
        "F-8", f"THE LOCUS, WITNESSED AND THEN PROVED ALONG THE CURVE: the two "
        f"QQ(sqrt 6) witnesses {LOCUS_WITNESS_NAMES} are on the family and positive "
        f"definite ({principal.locus_pd}); G2 = mu G1 EXACTLY with mu = "
        f"{claims['locus_mu']} ({principal.locus_proportional}); the graded det B is "
        f"proportional to (k^T G1 k)^2 with respective prefactors "
        f"{claims['locus_det_prefactors']} ({principal.locus_det_prefactors}) and one "
        f"quadratic zero set ({principal.locus_one_cone_squared}) -- with all four H-pencil branches "
        f"constant multiples {claims['locus_branch_constants']} of k^T G1 k and the "
        f"transverse pair SPLIT ({principal.locus_transverse_split}), while the "
        f"overlap cone stays a non-Hodge pair with factor counts "
        f"{principal.locus_overlap_factor_counts} ({principal.locus_overlap_never_g1}); "
        f"symbolically along g0 = g1/(1 + pi0 g1) with free volumes det B is one "
        f"quadric squared ({principal.locus_symbolic_one_cone}), every branch is "
        f"k-free times k^T G1 k ({principal.locus_symbolic_branches_k_free}), and "
        f"with the ties the constants are {LOCUS_BRANCH_CONSTANTS_SYMBOLIC} "
        f"({principal.locus_symbolic_constants_match}); cone_is_one_metric_cone_on_locus = "
        f"{claims['cone_is_one_metric_cone_on_locus']}",
        principal.locus_pd and principal.locus_proportional
        and principal.locus_mu == tuple(sp.sympify(m) for m in claims["locus_mu"])
        and principal.locus_det_prefactors == tuple(
            sp.sympify(value) for value in claims["locus_det_prefactors"])
        and principal.locus_one_cone_squared is claims["cone_is_one_metric_cone_on_locus"]
        and claims["cone_is_one_metric_cone_on_locus"] is True
        and principal.locus_constants == tuple(
            tuple(sorted((sp.sympify(c) for c in row), key=sp.default_sort_key))
            for row in claims["locus_branch_constants"])
        and principal.locus_transverse_split is claims["transverse_splits_on_locus"]
        and claims["transverse_splits_on_locus"] is True
        and principal.locus_overlap_never_g1
        and (principal.locus_symbolic_one_cone and principal.locus_symbolic_branches_k_free
             and principal.locus_symbolic_constants_match) is claims["locus_symbolic"]
        and claims["locus_symbolic"] is True)

    # --- G: SHEAR REGISTRATION ------------------------------------------------
    checks.check(
        "G-1", f"THE SHEAR ENTERS THE CONE, EXACTLY: under the graded assembly "
        f"d(k^T G1 k)/dg0 and d(k^T G2 k)/dg1 are nonzero and det B is not "
        f"proportional to its zero-shear value ({registration.onsite_cone_shear_derivative_nonzero}); "
        f"under the overlap assembly likewise ({registration.overlap_cone_shear_derivative_nonzero}) "
        f"and the sign class moves the cone at fixed magnitudes "
        f"({registration.sign_class_moves_overlap_cone})",
        registration.onsite_cone_shear_derivative_nonzero is claims["shear_enters_onsite"]
        and registration.overlap_cone_shear_derivative_nonzero is claims["shear_enters_overlap"]
        and claims["shear_enters_onsite"] is True and claims["shear_enters_overlap"] is True
        and registration.sign_class_moves_overlap_cone)
    checks.check(
        "G-2", f"THE DIAGONAL METRIC DOES NOT: under the graded assembly det B is "
        f"proportional to its unit-volume value ({registration.onsite_cone_volume_free}) "
        f"and the volumes enter only the branch scales "
        f"{registration.onsite_branch_scales}; under the overlap assembly the "
        f"Bloch H at zero shear is h0 times the identity "
        f"({registration.overlap_symbol_depends_only_on_h}), the zero-shear "
        f"H-pencil symbol is R5's for EVERY volume pair "
        f"({registration.overlap_zero_shear_pencil_is_r5}) and the zero-shear "
        f"form symbol is {registration.overlap_zero_shear_form_scale}; "
        f"volume_enters_onsite_cone = {claims['volume_enters_onsite_cone']}",
        registration.onsite_cone_volume_free is (not claims["volume_enters_onsite_cone"])
        and claims["volume_enters_onsite_cone"] is False
        and registration.overlap_zero_shear_pencil_is_r5 is claims["overlap_zero_shear_pencil_r5"]
        and claims["overlap_zero_shear_pencil_r5"] is True
        and registration.overlap_symbol_depends_only_on_h)
    checks.check(
        "G-3", f"THE #7970 TENSION IS RECORDED AND NOT RESOLVED: {TENSION_RECORD} "
        f"(tension_recorded = {claims['tension_recorded']})",
        claims["tension_recorded"] is True and TENSION_RECORDED)

    # --- H: THE SCOPE FENCES ----------------------------------------------------
    checks.check(
        "H-1", f"FENCE ONE -- '{SCOUT_GRADE_FENCE}', BLOCK 211's FENCE INHERITED "
        f"VERBATIM: scout_grade_only = {claims['scout_grade_only']}, "
        f"physical_content = {claims['physical_content']}",
        claims["scout_grade_only"] is True and claims["physical_content"] is False)
    checks.check(
        "H-2", f"FENCE TWO -- THE ASSEMBLY IS A SUPPLIED FORK, NOT A RESULT: "
        f"Block 105's onsite and overlap assemblies give DIFFERENT cones and "
        f"this block decides between them nowhere; assembly_decided = "
        f"{claims['assembly_decided']}",
        claims["assembly_decided"] is False)
    checks.check(
        "H-3", f"FENCE THREE -- NO HODGE READING IS SELECTED: G1 = D1/D0 and "
        f"G2 = D3 E D2^-1 E are both realised as exact branches and neither is "
        f"named 'the' metric; hodge_reading_selected = {claims['hodge_reading_selected']}",
        claims["hodge_reading_selected"] is False)
    checks.check(
        "H-4", f"FENCE FOUR -- THE INSTANCE SCOPE, ENUMERATED: "
        f"{claims['instance_scope']} restrictions ({INSTANCE_SCOPE})",
        claims["instance_scope"] == len(INSTANCE_SCOPE)
        and claims["instance_scope"] == INSTANCE_SCOPE_COUNT
        and claims["instance_scope"] > 0)

    # --- I: THE NOTE, THE FENCE AND THE EXACTNESS HYGIENE ----------------------
    checks.check(
        "I-1", f"the note is present at {NOTE_PATH.name} and the N5 fence "
        f"appears in it VERBATIM as a single line",
        NOTE_PATH.is_file() is claims["note_present"]
        and facts.scope == claims["scope"])
    checks.check(
        "I-2", f"sp.nsimplify appears {claims['nsimplify_calls']} times in this "
        f"runner's own source -- MEASURED, not promised -- so no rational "
        f"tolerance can turn the nonzero discrepancy polynomial into a zero and "
        f"manufacture the identity this block refutes",
        facts.nsimplify_calls == claims["nsimplify_calls"])
    checks.check(
        "I-3", f"and {claims['float_literals']} float literals appear in that "
        f"same source with EXACTLY {claims['float_calls']} float call sites, "
        f"both MEASURED by an AST walk -- Block 211's strict form",
        facts.float_literals == claims["float_literals"]
        and facts.float_calls == claims["float_calls"])
    return checks


# ---------------------------------------------------------------------------
# THE MEASURED REPORT
# ---------------------------------------------------------------------------
def report_measured(facts: Facts, elapsed_ns: int) -> None:
    print("MEASURED")
    print(f"  elapsed: {elapsed_ns // 1000000000}s")
    print(f"  correction source base {facts.source_base}")
    print(f"  authority {facts.authority}")
    print(f"  imposed {facts.imposed}, registered {facts.registered}, "
          f"adopted {facts.adopted}, gravity structures NOT SUPPLIED "
          f"{facts.unsupplied}, readings {facts.readings}, scoped headline "
          f"words {facts.scoped_words}")
    print(f"  historical checker record: {HISTORICAL_CHECKER_RECORD}")
    build = facts.construction
    print("  THE CONSTRUCTION")
    print(f"    2D lane kernel = Block 201's {build.lane_2d_matches_b201}, nnz "
          f"{build.lane_2d_nnz}, spin-nonscalar {build.spin_nonscalar_2d}, "
          f"site-sign-equivalent {build.lane_2d_site_sign_equivalent}, raising "
          f"part = Block 201's on (8,4) {build.raising_matches_b201_on_fork}, "
          f"K = d - d^T {build.k_is_d_minus_dT_2d}, d^2 = 0 {build.d_squared_zero_2d}")
    print(f"    3D lane kernel: {build.lane_3d_links_scanned} links scanned, "
          f"{build.lane_3d_bad_links} bad, shadow = eta/2 {build.lane_3d_shadow_matches}, "
          f"nnz {build.lane_3d_nnz}, x/y links absent on extent 2 "
          f"{build.lane_3d_xy_links_absent}, K = d - d^T {build.k_is_d_minus_dT_3d}, "
          f"d^2 = 0 {build.d_squared_zero_3d}")
    print(f"    assemblers: fork_hodge {build.fork_hodge_reproduced}, onsite_hodge "
          f"{build.onsite_hodge_reproduced}, overlap_hodge {build.overlap_hodge_reproduced}, "
          f"rules = bench assembly {build.rules_match_bench_assembly}")
    print(f"    flat: H = I {build.flat_h_identity}, K_H = K {build.flat_kernel_is_r5}")
    for cell in build.cells:
        print(f"    witness {cell.name}: moduli (v0, g0, v1, g1) = {cell.moduli}, ranks "
              f"{cell.ranks}, free {cell.free_names}, blocks = formulas "
              f"{cell.blocks_match_formulas}, cross-degree zero {cell.cross_degree_zero}, "
              f"origin tx face = shear_hodge{cell.face_moduli} {cell.face_restriction_is_shear_hodge}")
        print(f"      leading minors {cell.leading_minors}, PD {cell.positive_definite}")
        print(f"      G1 = D1/D0 = {cell.g1}")
        print(f"      G2 = D3 E D2^-1 E = {cell.g2}")
        print(f"      G1 ~ G2 {cell.g1_proportional_to_g2}; Hodge-consistency defects: "
              f"D0 D3 - 1 = {cell.hodge_defect_scalar}, nnz(D1 E D2 E - D0 D3 I) = "
              f"{cell.hodge_defect_matrix_nnz}")
    control = facts.control
    print("  THE R5 CONTROL")
    print(f"    flat symbol identity 2D {control.flat_symbol_identity_2d}, 3D "
          f"{control.flat_symbol_identity_3d}; (4,4) multiset {control.multiset_2d} "
          f"expected {control.expected_2d}; (4,2,2) multiset {control.multiset_3d} "
          f"expected {control.expected_3d}; Bloch = direct {control.bloch_equals_direct_flat}")
    spectra = facts.spectra
    print("  THE EXACT SPECTRA (factored charpoly of the 16 x 16 bench -K^2; "
          "'agree' = Bloch union equals direct bench)")
    for name, extent, assembly, reading, text, agreement, multiset in spectra.entries:
        print(f"    [{name} {extent} {assembly} {reading}] agree {agreement}"
              f"{' multiset ' + str(multiset) if multiset is not None else ''}")
        print(f"      {text}")
    print(f"    translation covariance at W1, nnz([-K_H^2, T_mu]): {spectra.translation_commutators}")
    print(f"    boundary: onsite H singular on (4,4) {spectra.boundary_onsite_singular_2d}, "
          f"on (4,2,2) {spectra.boundary_onsite_singular_3d}; overlap H regular "
          f"{spectra.boundary_overlap_regular}")
    principal = facts.principal
    print("  THE PRINCIPAL PART AND THE CONE")
    print(f"    onsite lemma 3D {principal.lemma_3d_holds}, 2D {principal.lemma_2d_holds}, "
          f"D0 absent {principal.lemma_d0_absent}, block-diagonal {principal.lemma_3d_block_diagonal}, "
          f"0-form branch {principal.lemma_3d_zero_form_branch}, top-form branch "
          f"{principal.lemma_3d_top_form_branch}, transverse product {principal.lemma_3d_transverse_product}, "
          f"expansion K_H,B = i eps (H0 D + D^T H0) + O(eps^2) measured {principal.expansion_exact}")
    print(f"    overlap H0 form {principal.overlap_h0_form_holds}, overlap cone 3D "
          f"{principal.overlap_cone_3d_holds}, 2D {principal.overlap_cone_2d_holds}")
    print(f"    2D (c, v): onsite branches {principal.two_dim_onsite_branches}, onsite pencil "
          f"scalar generically {principal.two_dim_onsite_pencil_scalar_generic}, on the locus "
          f"v^2 = 1 - c^2 {principal.two_dim_onsite_scalar_on_locus}, onsite form scalar "
          f"{principal.two_dim_onsite_form_scalar}; overlap pencil scalar "
          f"{principal.two_dim_overlap_pencil_scalar}, matches {principal.two_dim_overlap_pencil_matches}, "
          f"cone matches {principal.two_dim_overlap_cone_matches}, form scalar "
          f"{principal.two_dim_overlap_form_scalar}, effective shear {principal.two_dim_effective_shear}, "
          f"discrepancy {principal.two_dim_discrepancy}")
    print(f"    2D onsite exact 0-form H-pencil symbol: {principal.two_dim_onsite_zero_form_symbol}")
    print(f"    2D onsite exact 2-form H-pencil symbol: {principal.two_dim_onsite_two_form_symbol}")
    print(f"    2D overlap exact H-pencil scalar symbol: {principal.two_dim_overlap_pencil_symbol}")
    for record in principal.witnesses:
        (name, assembly, factor_texts, branches, remainder, form_branches, form_remainder,
         scalar_pencil, scalar_form, cones_ok, branches_ok, parity, cone1, cone2) = record
        print(f"    [{name} {assembly}] parity-preserving H0 {parity}; det B factors {factor_texts}")
        print(f"      pencil branches (quadratic-form eigenvalues, multiplicity) {branches}; "
              f"remaining factor degrees {remainder}; scalar {scalar_pencil}")
        print(f"      form branches {form_branches}; remaining {form_remainder}; scalar {scalar_form}")
        print(f"      k^T G1 k = {cone1}; k^T G2 k = {cone2}; cones are G1, G2 {cones_ok}; "
              f"branches include G1, G2 {branches_ok}")
    print(f"    W1 graded exact 0-form H-pencil symbol: {principal.w1_zero_form_symbol}")
    print(f"    W1 cones onsite {principal.w1_onsite_cones}, overlap {principal.w1_overlap_cones}; "
          f"onsite cones = G1, G2 everywhere {principal.onsite_cones_are_g1_g2_everywhere}; "
          f"branches everywhere {principal.onsite_branches_g1_g2_everywhere}; overlap cones "
          f"never G1, G2 at the listed witnesses {principal.overlap_cones_never_g1_g2}; "
          f"scalar at a listed curved 3D witness "
          f"{principal.principal_scalar_at_listed_curved_3d_witnesses}; explicit curved "
          f"overlap scalar counterexample {principal.overlap_scalar_counterexample}; transverse pair splits at "
          f"{principal.transverse_split_witnesses}")
    print(f"    G1 ~ G2 on the chart: Groebner bases {principal.coincidence_chart_bases} "
          f"(all equal {principal.coincidence_chart_bases_equal}), real solutions "
          f"{principal.coincidence_solutions} over {principal.coincidence_classes} classes")
    print(f"    THE SIXTY-FOUR-CELL CENSUS ({principal.census_cells} cells): {principal.census}")
    print(f"      rule-A cells (S1 = -E S0 E) {principal.rule_a_cells}, rule-B cells (S1 = +E S0 E) "
          f"{principal.rule_b_cells}, rules cover the curve cells {principal.rules_cover_curve_cells}, "
          f"closed form of M1 E M2 E verified {principal.closed_form_ok}, curves solved "
          f"{principal.curve_solutions_ok}")
    print(f"    THE LOCUS WITNESSES {LOCUS_WITNESS_NAMES}: PD {principal.locus_pd}, G2 = mu G1 "
          f"{principal.locus_proportional} with mu {principal.locus_mu}, graded det B is proportional "
          f"to (k^T G1 k)^2 {principal.locus_one_cone_squared} with prefactors "
          f"{principal.locus_det_prefactors}, branch constants {principal.locus_constants}, "
          f"transverse split {principal.locus_transverse_split}, overlap factor counts "
          f"{principal.locus_overlap_factor_counts}, overlap never G1 {principal.locus_overlap_never_g1}")
    print(f"    THE LOCUS SYMBOLICALLY: one quadric squared {principal.locus_symbolic_one_cone}, "
          f"branches k-free {principal.locus_symbolic_branches_k_free}, tied constants "
          f"{principal.locus_symbolic_constants} match {principal.locus_symbolic_constants_match}, "
          f"mu - 1 = {principal.locus_mu_minus_one} matches {principal.locus_mu_minus_one_matches}")
    registration = facts.registration
    print("  SHEAR REGISTRATION")
    print(f"    onsite: shear moves the cone {registration.onsite_cone_shear_derivative_nonzero}, "
          f"volumes do not {registration.onsite_cone_volume_free}, branch scales "
          f"{registration.onsite_branch_scales}")
    print(f"    overlap: Bloch H at zero shear = h0 I {registration.overlap_symbol_depends_only_on_h}, "
          f"zero-shear pencil = R5 {registration.overlap_zero_shear_pencil_is_r5}, zero-shear form = "
          f"{registration.overlap_zero_shear_form_scale}, shear moves the cone "
          f"{registration.overlap_cone_shear_derivative_nonzero}, sign class moves the cone "
          f"{registration.sign_class_moves_overlap_cone}")
    print(f"    {TENSION_RECORD}")
    print("  READINGS, AND EACH IS A READING")
    for reading in READINGS:
        print(f"    {reading}")
    print(f"  nsimplify calls in this source: {facts.nsimplify_calls}; float literals: "
          f"{facts.float_literals}; float call sites: {facts.float_calls}")
    print("  NOT CLAIMED: NO GRAVITY. NO DYNAMICS. NO SPACETIME CONE. NO PROPAGATOR. "
          "NO ASSEMBLY DECIDED. NO HODGE READING SELECTED. NO CONTINUUM. THE "
          "READINGS ARE READINGS.")
    print()


N5_FENCE = 'N5: NOTHING HERE IS REGISTERED OR ADOPTED. SYMBOL means an exact finite Bloch matrix; CONE means the zero set of a homogeneous determinant; METRIC means one of two declared degree-block readings; DISPERSION means exact matrix branches. The live runtime inputs are the bounded recovered 201/209/211 construction helper, the current Block 105 assembly helper, the paired note, axioms, and registry; historical parent bodies and caches are preserved only as recovery evidence. At the degree-diagonal representative, the graded onsite determinant factorizes into the two reading quadrics. On the coincidence curve it is proportional to (k^T G1 k)^2, with factors 8/9 at L+- and 3/4 at L-+. None of the listed curved witness matrices is scalar, but this finite fact is not universal: the positive-definite opposite-sign point g0=3/8, g1=1/3, v0=sqrt(110)/12, v1=16sqrt(110)/165 has overlap pencil (kt^2+kx^2+ky^2) I. In two dimensions the overlap pencil is generically scalar, while the graded pencil is scalar on v^2=1-c^2; the form matrices are not scalar as symbolic identities but may be scalar at special values such as zero shear. No assembly, metric reading, action, propagator, continuum, spacetime cone, dynamics, or gravity is selected or supplied. Every negative is confined to the displayed formal family, exact identities, and named finite witnesses.'


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
