#!/usr/bin/env python3
"""Corrected Block 217 finite overlap-cell and bench calculation.

At eight transported curve witnesses plus W1 and flat controls, this runner
certifies the overlap union locus with the gcd and square-free part of the
univariate coefficient polynomials in s.  It separately measures the s=0
quadric pair, the generic joint factorization in (s, kappa), finite
stabilizers, and sixteen exact (4,2,2) bench characteristic polynomials with
explicit monic normalization.  It does not infer irreducibility at every
nonzero-s specialization or supply a physical cone, assembly choice, premise,
action, continuum, spacetime, or dynamics.
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
from sympy.polys.matrices import DomainMatrix

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

# THE MACHINERY IMPORTS, LANDED IN THIS BRANCH AND READ-ONLY: Block 216 (the
# census, the witnesses, the strict stabiliser) and through it Blocks 215,
# 214, 213, 211, 209.
try:
    import admissibility_dirac_kahler_covariant_curved_cell_cone_2026_09_05 as b216
    B216_IMPORT_LANDED = True
except ModuleNotFoundError:                            # pragma: no cover
    b216 = None
    B216_IMPORT_LANDED = False
b215 = b216.b215 if b216 is not None else None
b214 = b216.b214 if b216 is not None else None
b213 = b216.b213 if b216 is not None else None
b211 = b216.b211 if b216 is not None else None
b209 = b216.b209 if b216 is not None else None
MACHINERY_IMPORT_LANDED = bool(B216_IMPORT_LANDED and b216 is not None and b216.MACHINERY_IMPORT_LANDED
                               and b215 is not None and b214 is not None and b213 is not None
                               and b211 is not None and b209 is not None)
FINAL_NOTE_NAME = "ADMISSIBILITY_DIRAC_KAHLER_OVERLAP_ASSEMBLY_COVARIANT_CELLS_BOUNDED_THEOREM_NOTE_2026-09-05.md"
NOTE_PATH = ROOT / "docs" / FINAL_NOTE_NAME
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"
B216_NOTE = "docs/ADMISSIBILITY_DIRAC_KAHLER_COVARIANT_CURVED_CELL_CONE_BOUNDED_THEOREM_NOTE_2026-09-05.md"
B216_RUNNER = "scripts/admissibility_dirac_kahler_covariant_curved_cell_cone_2026_09_05.py"
B215_NOTE = "docs/ADMISSIBILITY_DIRAC_KAHLER_DUALITY_COVARIANCE_LOCUS_BOUNDED_THEOREM_NOTE_2026-09-05.md"
B215_RUNNER = "scripts/admissibility_dirac_kahler_duality_covariance_locus_2026_09_05.py"
B214_NOTE = "docs/ADMISSIBILITY_DIRAC_KAHLER_DUALITY_PARAMETERS_PRINCIPAL_PART_BOUNDED_THEOREM_NOTE_2026-09-05.md"
B214_RUNNER = "scripts/admissibility_dirac_kahler_duality_parameters_principal_part_2026_09_05.py"
B213_NOTE = "docs/ADMISSIBILITY_DIRAC_KAHLER_WEIGHTED_KERNEL_DISPERSION_BOUNDED_THEOREM_NOTE_2026-09-05.md"
B213_RUNNER = "scripts/admissibility_dirac_kahler_weighted_kernel_dispersion_2026_09_05.py"
PARENT_NOTE = B216_NOTE
PARENT_RUNNER = B216_RUNNER
PARENT_ARTIFACTS = (PARENT_NOTE, PARENT_RUNNER)
GROUP_HELPER_PATH = "scripts/admissibility_dirac_kahler_released7992_7994_group_fixture_2026_09_10.py"
B213_HELPER_PATH = "scripts/admissibility_dirac_kahler_weighted_kernel_released7981_7988_fixtures_2026_09_10.py"
B105_NOTE = "docs/ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md"
B105_RUNNER = "scripts/admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_2026_08_14.py"

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_OVERLAP_ASSEMBLY_COVARIANT_CELLS_BOUNDED_THEOREM_NOTE_2026-09-05.md",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_COVARIANT_CURVED_CELL_CONE_BOUNDED_THEOREM_NOTE_2026-09-05.md",
    "scripts/admissibility_dirac_kahler_covariant_curved_cell_cone_2026_09_05.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_DUALITY_COVARIANCE_LOCUS_BOUNDED_THEOREM_NOTE_2026-09-05.md",
    "scripts/admissibility_dirac_kahler_duality_covariance_locus_2026_09_05.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_DUALITY_PARAMETERS_PRINCIPAL_PART_BOUNDED_THEOREM_NOTE_2026-09-05.md",
    "scripts/admissibility_dirac_kahler_duality_parameters_principal_part_2026_09_05.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_WEIGHTED_KERNEL_DISPERSION_BOUNDED_THEOREM_NOTE_2026-09-05.md",
    "scripts/admissibility_dirac_kahler_weighted_kernel_dispersion_2026_09_05.py",
    "scripts/admissibility_dirac_kahler_weighted_kernel_released7981_7988_fixtures_2026_09_10.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "scripts/admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_2026_08_14.py",
    "scripts/admissibility_dirac_kahler_released7992_7994_group_fixture_2026_09_10.py",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
)
SELF_NOTE_INPUT = AUDIT_INPUT_PATHS[0]
INPUT_SHA256 = {
    AUDIT_INPUT_PATHS[0]: "fe14239b8091cae1f0cce71a72c288cb6cbd49d0f1b381099348eb24824e405d",
    B216_NOTE: "8f5d4ee30482c6d945359e91edbb6339d49e5906685f32b01441662322485765",
    B216_RUNNER: "383835cb0c24e6c818a2fe4de90ae354f3872dbb689e9739eba519c84c13a233",
    B215_NOTE: "bf50cb757c46f79fbd612d9f3d2a0edbb68f238092595fb86f21feead673ffbf",
    B215_RUNNER: "88b641afcad684de468f8692d9ee66fc1892f9eedd69881534285c22b38fbb81",
    B214_NOTE: "fe5e7a659bf56af3d0a002ec56ecfc9ab52a1fc8a20a87174f33db8ce9fac745",
    B214_RUNNER: "f0d70c67c5a13a53995698752276a10183dc77e46e7446617e10817603a74b91",
    B213_NOTE: "6eb45758067a92f7bc44f2ffbc5fec9999c2930e2b2c924dfa6dfa67ca5db5ae",
    B213_RUNNER: "d80ce0e3168968fcc1a887e6737681e4cdfc31c82813813415f008a68507088d",
    B213_HELPER_PATH: "082c88ae8d05df21874e90cef3a8a0784116a1eb6957d119709ef6838486a9ef",
    B105_NOTE: "9a615a79511ffc0dac0d1cf54388153604ce7c341496654fd709ed8873302a33",
    B105_RUNNER: "5499cc2c1a75f19e07b717aeb6c9ef7779c45e1c5757d84701c5d88ca92bf445",
    GROUP_HELPER_PATH: "bf048dead3a18c1b389522e24e7a12008a313b5382d7ed23df5e1f6bc7005b7f",
    AXIOM_PATH: "93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753",
    REGISTRY_PATH: "615f13aaa70e82d50cdf1a8aa479eb40d6ce70a3bb7b152ac63fd88bee341f37",
}
AUDIT_TIMEOUT_SEC = 240
SOURCE_BASE_COMMIT = "eb0fe5cae19cb8cf813182e8ccaddc4a0408faf3"
PARENT_SOURCE_SHA256 = "383835cb0c24e6c818a2fe4de90ae354f3872dbb689e9739eba519c84c13a233"
CURRENT_MAIN = SOURCE_BASE_COMMIT
PARENT_COMMIT = PARENT_SOURCE_SHA256
STALE_MAIN = "historical-moving-main-guard"
STALE_PARENT_COMMIT = "historical-parent-guard"

MUTATIONS = (
    "stale_main_authority",
    "stale_parent_authority",
    "claim_objects_registered",
    "claim_gravity_supplied",
    "claim_covariance_inherited",
    "claim_assembly_decided",
    "claim_cell_selected",
    "claim_metric_supplied",
    "break_cell_census",
    "break_witness_reproduction",
    "break_fold_sees_sum",
    "break_flat_control",
    "break_union_locus_s",
    "break_strict_stabiliser",
    "break_twisted_stabiliser",
    "break_shear_relation",
    "claim_curve_satisfies_shear_relation",
    "break_overlap_cone_pair",
    "claim_overlap_cone_is_onsite_cone",
    "break_overlap_cone_symbolic_s",
    "break_bench_multisets",
    "break_bloch_equals_direct",
    "break_bench_control",
    "break_bench_reads_principal_part",
    "break_bloch_fold_sees_parameters",
    "break_scout_grade_fence",
    "break_instance_scope",
    "drop_n5_fence",
    "break_float_absence",
)
MUTATION_GATE = {
    "stale_main_authority": "A", "stale_parent_authority": "A",
    "claim_objects_registered": "B", "claim_gravity_supplied": "B",
    "claim_covariance_inherited": "B", "claim_assembly_decided": "B",
    "claim_cell_selected": "B", "claim_metric_supplied": "B",
    "break_cell_census": "C", "break_witness_reproduction": "C",
    "break_fold_sees_sum": "C", "break_flat_control": "C",
    "break_union_locus_s": "D", "break_strict_stabiliser": "D", "break_twisted_stabiliser": "D",
    "break_shear_relation": "D", "claim_curve_satisfies_shear_relation": "D",
    "break_overlap_cone_pair": "E", "claim_overlap_cone_is_onsite_cone": "E", "break_overlap_cone_symbolic_s": "E",
    "break_bench_multisets": "F", "break_bloch_equals_direct": "F", "break_bench_control": "F",
    "break_bench_reads_principal_part": "G", "break_bloch_fold_sees_parameters": "G",
    "break_scout_grade_fence": "H", "break_instance_scope": "H",
    "drop_n5_fence": "I", "break_float_absence": "I",
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
# A. authority
# ---------------------------------------------------------------------------
def sha256_path(path: str) -> str:
    target = ROOT / path
    return hashlib.sha256(target.read_bytes()).hexdigest() if target.is_file() else ""


@dataclass(frozen=True)
class AuthorityCertificate:
    all_inputs_content_bound: bool
    parent_inputs_content_bound: bool
    machinery_import_landed: bool
    inputs_readable: int
    inputs_missing: tuple
    input_hashes: tuple


def authority_certificate() -> AuthorityCertificate:
    missing = tuple(path for path in AUDIT_INPUT_PATHS if not (ROOT / path).is_file())
    hashes = tuple((path, sha256_path(path)) for path in AUDIT_INPUT_PATHS)
    actual = dict(hashes)
    return AuthorityCertificate(
        actual == INPUT_SHA256,
        all(actual.get(path, "") == INPUT_SHA256[path] for path in PARENT_ARTIFACTS),
        MACHINERY_IMPORT_LANDED,
        len(AUDIT_INPUT_PATHS) - len(missing),
        missing,
        hashes,
    )


# ---------------------------------------------------------------------------
# B. the imposed objects and the NOT-CLAIMED keys, as measured literals
# ---------------------------------------------------------------------------
IMPOSED_OBJECTS = (
    "the cube complex, corners, degree indices and wedge signature (Block 209; Block 213's eta/lane_rules/raising_rules)",
    "Block 211's six-face-compatible cell-form family with its ties, 64 face-sign cells, four gauge classes and four free duality parameters",
    "Block 213's coincidence census, its curve witnesses L+- and L-+ over QQ(sqrt 6), its (4,2,2) bench and its Bloch reduction",
    "Block 214's principal part M = H0 D + D^T H0 under both assemblies, its plane and its union-locus statement in s at all-plus witnesses",
    "Block 215's corner action of the 24 proper rotations, its sign vectors and its overlap statements at the four class representatives",
    "Block 216's 16 star-pattern cells, its 8 rule-A covariant witnesses and their strict S3_body stabilisers under the onsite assembly",
)
REGISTERED_OBJECTS = ()
ADOPTED_OBJECTS = ()
GRAVITY_SUPPLIED_CLAIMED = False
COVARIANCE_INHERITED_CLAIMED = False
CELL_SELECTED_CLAIMED = False
SUBGROUP_SELECTED_CLAIMED = False
ASSEMBLY_DECIDED_CLAIMED = False
METRIC_SUPPLIED_CLAIMED = False
PARAMETER_VALUE_SELECTED_CLAIMED = False
READING_SELECTED_CLAIMED = False
READINGS_LICENSED_CLAIMED = False
CONTINUUM_LIMIT_CLAIMED = False
LIGHT_CONE_CLAIMED = False
CONE_IS_SPACETIME_CONE_CLAIMED = False
UNSUPPLIED_GRAVITY_STRUCTURES = (
    "lapse function", "shift vector", "ADM phase space", "Hamiltonian constraint",
    "momentum/diffeomorphism constraint", "first-class constraint algebra",
    "Dirac closure", "Dirac observable", "gauge orbit and its quotient",
)
SCOPED_HEADLINE_WORDS = ("COVARIANCE", "CONE", "CELL", "ASSEMBLY", "BENCH")
AXIOM_COVARIANCE_CLAUSE = ("There is one fixed nearest-neighbor admissibility rule, covariant under lattice\n"
                           "translations and proper cubic rotations.")
READINGS = (
    "R1 the cell form inherits the Admissibility axiom's proper-cubic-rotation covariance (the antecedent; not established, not asserted)",
    "R2 the difference in covariance between the two assemblies at the covariant cells decides the assembly (not established: both are measured, neither is selected)",
    "R3 'one metric's cone' or 'a non-Hodge pair of cones' is a metric or a cone of anything physical (not established: Block 213's polynomial statements)",
    "R4 the (4,2,2) bench multisets are a dispersion law, a light cone or a continuum limit (not established: sixteen exact eigenvalues of one finite matrix at two Bloch points)",
    "R5 the overlap fold's twisted D4_face stabiliser is a symmetry of anything physical (not established: a matrix identity on one folded 8 x 8 matrix)",
    "R6 the covariant witness is a vacuum, a background or a spacetime (not established: a positive-definite point on one cell form)",
)
HISTORICAL_REVIEW_RECORD = "PRESERVED-NOT-CURRENT-EVIDENCE"

# the parameters, the moduli, the directions, the cells, the witnesses
PARAMETER_NAMES = ("D07", "D16", "D25", "D34")
PARAMETER_SYMBOLS = b216.PARAMETER_SYMBOLS
A07, B16, C25, D34 = PARAMETER_SYMBOLS
G0, G1, V0, V1 = b216.MODULI
MODULI = (G0, G1, V0, V1)
KT, KX, KY = b216.KAPPA
KAPPA = (KT, KX, KY)
SUM = sp.Symbol("s")                      # Block 215's overlap sum s = D07 + D16 + D25 + D34
LAM = b213.LAM
FACE_ORDER = b211.GAUGE_FACE_ORDER        # (tx0, ty0, xy0, tx1, ty1, xy1)
FACE_NAMES = ("tx", "ty", "xy")
SIGNATURE = sp.diag(1, -1, 1)             # Block 213's E on (t, x, y)
QUARTER = sp.Rational(1, 4)
BENCH_EXTENT = (4, 2, 2)                  # Block 213's three-direction bench
LINE_POINT = (sp.Integer(0), QUARTER, -QUARTER, QUARTER)   # (D07, D16, D25, D34) on the star line at 1/4
ALL_PLUS_CELL = b216.ALL_PLUS_CELL
W1_MODULI = b216.W1_MODULI                # (v0, g0, v1, g1) = (15/16, 1/4, 1, 1/4)
FLAT_MODULI = b216.FLAT_MODULI
GAUGE_CLASSES = b216.GAUGE_CLASSES

# ---------------------------------------------------------------------------
# exact helpers -- no float, no tolerance and NO nsimplify anywhere
# ---------------------------------------------------------------------------
NSIMPLIFY_TOKEN = "sp." + "nsimplify("


def nsimplify_occurrences() -> int:
    return Path(__file__).read_text(encoding="utf-8").count(NSIMPLIFY_TOKEN)


def float_literal_occurrences() -> int:
    tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    return sum(1 for node in ast.walk(tree)
               if isinstance(node, ast.Constant) and type(node.value) is float)


def float_call_sites() -> int:
    tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    return sum(1 for node in ast.walk(tree)
               if isinstance(node, ast.Call)
               and isinstance(node.func, ast.Name) and node.func.id == "float")


def residual_count(matrix) -> int:
    return b213.residual_count(matrix)


def is_zero_alg(expression) -> bool:
    return sp.expand(sp.radsimp(expression)) == 0


def sign_dict(values: tuple) -> dict:
    return b216.sign_dict(values)


def formal(values: tuple, moduli: tuple, params: tuple) -> sp.Matrix:
    """Block 214's formal_cell at a face-sign cell (moduli as (g0, g1, v0, v1))."""
    return b216.formal(values, moduli, params)


def curve_moduli(pi0: int) -> tuple:
    """Block 213's curve point (v0, g0, v1, g1): L+-'s for pi0 = +1, L-+'s for pi0 = -1."""
    return b216.curve_moduli(pi0)


def moduli_as_g(moduli: tuple) -> tuple:
    return b216.moduli_as_g(moduli)


def rule_a_cells(census: dict) -> tuple:
    return tuple(v for v in b216.star_cells(census) if census["cells"][v]["rule_a"])


def overlap_fold(cell_s: sp.Matrix) -> tuple:
    """(H0(s), M(s)) of the overlap assembly for a cell carrying (s, 0, 0, 0)."""
    h0, m, _ = b214.principal_part(cell_s, "overlap")
    return h0, m


# ---------------------------------------------------------------------------
# C. THE FOLD AT SYMBOLIC FACE SIGNS AND SYMBOLIC MODULI (a lemma at every cell)
# ---------------------------------------------------------------------------
SIGN_SYMBOLS = sp.symbols("s_tx0 s_ty0 s_xy0 s_tx1 s_ty1 s_xy1")


def generic_cell(params: tuple) -> sp.Matrix:
    return b214.formal_cell(dict(zip(FACE_ORDER, SIGN_SYMBOLS)), G0, G1, V0, V1, params)


def measure_fold() -> dict:
    """The overlap fold H0 at symbolic face signs, moduli and parameters: it
    depends on the parameters only through s (Block 215's F-1, now a lemma at
    every cell), its parity block is (s/4) P111, and at s = 0 it is h0 I plus
    the two-flip couplings; the flat cell gives H = I at zero parameters under
    both assemblies; the overlap Bloch fold at z = (i, 1, 1) is parameter-free."""
    facts: dict = {}
    h_full, _ = overlap_fold(generic_cell(PARAMETER_SYMBOLS))
    h_s, _ = overlap_fold(generic_cell((SUM, 0, 0, 0)))
    facts["fold_sees_sum_only_symbolic_signs"] = residual_count(
        (h_full - h_s.subs(SUM, sum(PARAMETER_SYMBOLS))).applyfunc(sp.expand)) == 0
    even, odd = b213.even_odd(3)
    p111 = b214.hodge_complement_permutation()
    facts["parity_block_is_sum_over_four_p111"] = residual_count(
        (h_s.extract(even, odd) - SUM / 4 * p111.extract(even, odd)).applyfunc(sp.expand)) == 0
    facts["fold_linear_in_s"] = all(sp.Poly(sp.expand(x), SUM).degree() <= 1 for x in h_s if x != 0)
    h_zero = h_s.subs(SUM, 0)
    facts["fold_zero_free_symbols"] = tuple(sorted(str(x) for x in h_zero.free_symbols))
    facts["fold_diagonal"] = str(sp.factor(h_zero[0, 0]))
    facts["fold_diagonal_scalar"] = all(sp.cancel(h_zero[i, i] - h_zero[0, 0]) == 0 for i in range(8))
    couplings: dict = {}
    for i in range(8):
        for j in range(i + 1, 8):
            if h_zero[i, j] != 0:
                couplings[(i, j)] = str(sp.factor(h_zero[i, j]))
    facts["couplings"] = couplings
    facts["coupling_count"] = len(couplings)
    facts["coupling_literals"] = tuple(sorted(set(couplings.values())))
    # every coupling joins a two-flip pair (corners differing in exactly two coordinates)
    facts["couplings_are_two_flip_pairs"] = all(
        sum(1 for a, b in zip(b209.CORNERS[i], b209.CORNERS[j]) if a != b) == 2 for (i, j) in couplings)
    # the flat control: both assemblies give the identity at zero parameters; the flat fold is I + (s/4) P111
    flat = formal(ALL_PLUS_CELL, moduli_as_g(FLAT_MODULI), (0, 0, 0, 0))
    h_on, _, _ = b214.principal_part(flat, "onsite")
    h_ov, _, _ = b214.principal_part(flat, "overlap")
    facts["flat_both_assemblies_identity"] = residual_count(h_on - sp.eye(8)) == 0 and residual_count(h_ov - sp.eye(8)) == 0
    flat_s, _ = overlap_fold(formal(ALL_PLUS_CELL, moduli_as_g(FLAT_MODULI), (SUM, 0, 0, 0)))
    facts["flat_fold_is_identity_plus_sum_p111"] = residual_count((flat_s - sp.eye(8) - SUM / 4 * p111).applyfunc(sp.expand)) == 0
    # the overlap Bloch fold at the bench's nonzero point z = (i, 1, 1), symbolic everything: parameter-free
    rules = b213.overlap_rules(generic_cell(PARAMETER_SYMBOLS), b209.CORNERS, 3)
    bloch_i = b213.bloch_matrix(rules, (sp.I, 1, 1), 3)
    facts["bloch_fold_at_i_parameter_free"] = not (bloch_i.free_symbols & set(PARAMETER_SYMBOLS))
    facts["bloch_momenta"] = tuple(tuple(str(x) for x in z) for z in b213.bench_momenta(BENCH_EXTENT))
    return facts


# ---------------------------------------------------------------------------
# D. THE LOCI: stabilisers of the fold at s = 0 and at symbolic s, the shear
# relation at symbolic signs, the union locus in s
# ---------------------------------------------------------------------------
def s_locus(h_sym: sp.Matrix, lift: sp.Matrix, e: tuple) -> tuple:
    """(feasible, forced) for T = E L on a fold linear in s: infeasible when an
    entry of T H T^T - H is a nonzero constant, else the forced locus in s."""
    t = sp.diag(*e) * lift
    residual = (t * h_sym * t.T - h_sym).applyfunc(sp.radsimp)
    forced = set()
    for i in range(8):
        for j in range(i, 8):
            x = sp.expand(residual[i, j])
            if x == 0:
                continue
            if sp.Poly(x, SUM).degree() == 0:
                return (False, None)
            forced.add("s")
    return (True, tuple(sorted(forced)))


def stabilisers_in_s(h_sym: sp.Matrix, lifts: tuple) -> tuple:
    """(strict, twisted): rotation -> forced loci in s, over E = 1 and over all 64 sign vectors."""
    strict, twisted = {}, {}
    for g in range(24):
        ok, forced = s_locus(h_sym, lifts[g], (1,) * 8)
        if ok:
            strict[g] = forced
        loci = set()
        for e in b215.sign_vectors():
            ok, forced = s_locus(h_sym, lifts[g], e)
            if ok:
                loci.add(forced)
        if loci:
            twisted[g] = tuple(sorted(loci))
    return strict, twisted


def forced_conditions(h: sp.Matrix, lift: sp.Matrix) -> tuple:
    """The moduli conditions forced by L H L^T = H at symbolic moduli: the
    non-volume factors of every nonzero entry's numerator (the volumes are
    nonzero on Block 211's domain)."""
    out = set()
    residual = (lift * h * lift.T - h).applyfunc(sp.cancel)
    for i in range(8):
        for j in range(i, 8):
            entry = residual[i, j]
            if entry == 0:
                continue
            numerator, _ = sp.fraction(sp.factor(entry))
            _, factors = sp.factor_list(numerator)
            out.add(tuple(sorted(str(base) for base, _ in factors if base.free_symbols and base not in (V0, V1))))
    return tuple(sorted(out))


def union_locus_s(m_s: sp.Matrix, gaussian: bool) -> tuple:
    """Univariate coefficient-gcd certificate in s at one fixed witness.

    The nonzero kappa coefficients of det M - det(B)^2 lie in QQ[s] or
    QQ(sqrt(6))[s].  Their gcd generates their ideal because that ring is a
    PID; its square-free part therefore defines the finite union locus.
    """
    even, odd = b213.even_odd(3)
    det_m = sp.expand(b214.ff_det(m_s, (SUM,) + KAPPA, algebraic=gaussian))
    det_b = sp.expand(sp.radsimp(m_s.extract(even, odd).det(method="berkowitz")))
    difference = sp.expand(sp.radsimp(det_m - det_b ** 2))
    raw_coefficients = tuple(
        sp.expand(sp.radsimp(value))
        for value in sp.Poly(difference, *KAPPA).coeffs()
        if not is_zero_alg(value)
    )
    if gaussian:
        polynomials = tuple(sp.Poly(value, SUM, extension=sp.sqrt(6))
                            for value in raw_coefficients)
    else:
        polynomials = tuple(sp.Poly(value, SUM, domain=QQ)
                            for value in raw_coefficients)
    if not polynomials:
        raise AssertionError("empty coefficient ideal")
    coefficient_gcd = polynomials[0]
    for polynomial in polynomials[1:]:
        coefficient_gcd = sp.gcd(coefficient_gcd, polynomial)
    coefficient_gcd = coefficient_gcd.monic()
    square_free = coefficient_gcd.sqf_part().monic()
    generators = (str(sp.expand(square_free.as_expr())),)
    gcd_literal = str(sp.expand(coefficient_gcd.as_expr()))
    return (generators, gcd_literal, len(polynomials),
            sp.Poly(det_m, SUM).degree(), sp.Poly(det_b, SUM).degree(),
            det_m, det_b)


def class_name_of(group: dict, members: tuple) -> str:
    target = frozenset(members)
    for name, cls in group["classes"].items():
        if any(frozenset(member) == target for member in cls):
            return name
    return "NONE"


def rotation_axis(rotation: sp.Matrix) -> tuple:
    space = (rotation - sp.eye(3)).nullspace()
    if len(space) != 1:
        return ()
    axis = space[0] / sp.gcd(list(space[0]))
    return tuple(axis)


def measure_loci(group: dict, census: dict) -> dict:
    """D: at each rule-A cell with Block 216's curve witness, and at the all-plus
    W1 and flat controls: the onsite strict stabiliser (Block 216's S3_body),
    the overlap fold's strict and twisted stabilisers at symbolic s (feasible
    rotations and the locus in s each forces), the shear relation at symbolic
    moduli under the cell's own S3_body, its value on the curve, the union
    locus in s and the degrees of det M and det B in s."""
    lifts, rots, orders = group["lifts"], group["rotations"], group["orders"]
    fold_generic_zero, _ = overlap_fold(generic_cell((0, 0, 0, 0)))
    table: dict = {}
    witnesses = [(census["cells"][v]["mask"], v, curve_moduli(census["cells"][v]["class"][0]), True)
                 for v in rule_a_cells(census)]
    witnesses += [("W1", ALL_PLUS_CELL, W1_MODULI, False), ("flat", ALL_PLUS_CELL, FLAT_MODULI, False)]
    for key, values, moduli, gaussian in witnesses:
        print(f"[loci] witness {key}", file=sys.stderr)
        v0, g0, v1, g1 = moduli
        entry: dict = {"class": census["cells"][values]["class"], "moduli": moduli}
        onsite_zero = formal(values, moduli_as_g(moduli), (0, 0, 0, 0))
        onsite_stab = b216.strict_stabiliser(onsite_zero, lifts)
        entry["onsite_stabiliser"] = onsite_stab
        entry["onsite_stabiliser_class"] = class_name_of(group, onsite_stab)
        h_s, m_s = overlap_fold(formal(values, moduli_as_g(moduli), (SUM, 0, 0, 0)))
        entry["fold_linear_in_s"] = all(sp.Poly(sp.expand(x), SUM).degree() <= 1 for x in h_s if x != 0)
        strict, twisted = stabilisers_in_s(h_s, lifts)
        entry["strict_feasible"] = tuple(sorted(strict))
        entry["strict_all_s"] = tuple(sorted(g for g, f in strict.items() if f == ()))
        entry["strict_only_at_zero"] = tuple(sorted(g for g, f in strict.items() if f == ("s",)))
        entry["twisted_feasible"] = tuple(sorted(twisted))
        entry["twisted_all_s"] = tuple(sorted(g for g, loci in twisted.items() if () in loci))
        entry["twisted_class"] = class_name_of(group, entry["twisted_all_s"])
        entry["twisted_axes"] = tuple(sorted(set(rotation_axis(rots[g]) for g in entry["twisted_all_s"] if orders[g] == 4)))
        common = tuple(sorted(set(onsite_stab) & set(entry["twisted_all_s"])))
        entry["common_with_onsite"] = common
        entry["common_class"] = class_name_of(group, common)
        entry["s3_in_twisted"] = set(onsite_stab) <= set(entry["twisted_all_s"])
        # the shear relation at SYMBOLIC moduli at this cell's signs, under the onsite stabiliser
        fold_cell = fold_generic_zero.subs(dict(zip(SIGN_SYMBOLS, values)))
        forced = {g: forced_conditions(fold_cell, lifts[g]) for g in onsite_stab if orders[g] > 1}
        entry["forced_by_order"] = tuple(sorted(set((orders[g], f) for g, f in forced.items())))
        entry["forced_union"] = tuple(sorted(set(itertools.chain.from_iterable(
            itertools.chain.from_iterable(f) for f in forced.values()))))
        entry["shear_relation_plus"] = sp.radsimp(g0 * v0 * v1 + g1)
        entry["shear_relation_minus"] = sp.radsimp(g0 * v0 * v1 - g1)
        entry["volume_product"] = sp.radsimp(v0 * v1)
        entry["shears_nonzero"] = g0 != 0 and g1 != 0
        generators, coefficient_gcd, coefficient_count, deg_m, deg_b, _, _ = union_locus_s(m_s, gaussian)
        entry["union_locus"] = generators
        entry["coefficient_gcd"] = coefficient_gcd
        entry["coefficient_count"] = coefficient_count
        entry["det_m_degree_s"], entry["det_b_degree_s"] = deg_m, deg_b
        table[key] = entry
    facts: dict = {"table": table}
    rule_keys = [k for k in table if isinstance(k, int)]
    facts["rule_a_count"] = len(rule_keys)
    facts["onsite_stabiliser_is_s3_everywhere"] = all(table[k]["onsite_stabiliser_class"] == "S3_body" for k in rule_keys)
    facts["overlap_strict_trivial_everywhere"] = all(table[k]["strict_feasible"] == (0,) for k in rule_keys)
    facts["overlap_twisted_classes"] = tuple(sorted(set(table[k]["twisted_class"] for k in rule_keys)))
    facts["overlap_twisted_is_all_s"] = all(table[k]["twisted_feasible"] == table[k]["twisted_all_s"] for k in rule_keys)
    facts["overlap_twisted_orders"] = tuple(sorted(set(len(table[k]["twisted_all_s"]) for k in rule_keys)))
    facts["overlap_twisted_axes"] = tuple(sorted(set(table[k]["twisted_axes"] for k in rule_keys)))
    facts["common_classes"] = tuple(sorted(set(table[k]["common_class"] for k in rule_keys)))
    facts["s3_in_twisted_anywhere"] = any(table[k]["s3_in_twisted"] for k in rule_keys)
    facts["forced_by_order"] = tuple(sorted(set(table[k]["forced_by_order"] for k in rule_keys)))
    facts["forced_union"] = tuple(sorted(set(table[k]["forced_union"] for k in rule_keys)))
    facts["shear_relations_on_curve"] = {key: tuple(sorted(set((table[k]["shear_relation_plus"], table[k]["shear_relation_minus"])
                                                              for k in rule_keys if table[k]["class"] == key)))
                                         for key in ((1, -1), (-1, 1))}
    facts["curve_violates_every_relation"] = all(table[k]["shear_relation_plus"] != 0 and table[k]["shear_relation_minus"] != 0
                                                 and table[k]["shears_nonzero"] for k in rule_keys)
    facts["union_locus_everywhere"] = tuple(sorted(set(table[k]["union_locus"] for k in table)))
    facts["coefficient_gcd_everywhere"] = tuple(sorted(set(table[k]["coefficient_gcd"] for k in table)))
    facts["coefficient_counts_positive"] = all(table[k]["coefficient_count"] > 0 for k in table)
    facts["det_degrees_s"] = tuple(sorted(set((table[k]["det_m_degree_s"], table[k]["det_b_degree_s"]) for k in table)))
    facts["witness_count"] = len(table)
    facts["w1_twisted_class"] = table["W1"]["twisted_class"]
    facts["w1_strict_feasible"] = table["W1"]["strict_feasible"]
    facts["flat_strict_all_s_class"] = class_name_of(group, table["flat"]["strict_all_s"])
    facts["flat_strict_only_at_zero_count"] = len(table["flat"]["strict_only_at_zero"])
    facts["flat_twisted_class"] = table["flat"]["twisted_class"]
    return facts


# ---------------------------------------------------------------------------
# E. THE OVERLAP CONE at the witnesses: s = 0 and symbolic s, against the onsite cone
# ---------------------------------------------------------------------------
def quadric_coefficients(quadric) -> tuple:
    """(c_xx, |c_tx|, |c_ty|, |c_xy|) of a quadric normalised to kt^2 + ... + ky^2."""
    poly = sp.Poly(sp.expand(quadric), *KAPPA)
    lead = poly.coeff_monomial(KT ** 2)
    norm = lambda m: sp.radsimp(poly.coeff_monomial(m) / lead)
    return (norm(KX ** 2), sp.Abs(norm(KT * KX)), sp.Abs(norm(KT * KY)), sp.Abs(norm(KX * KY)), norm(KY ** 2))


def measure_cone(census: dict) -> dict:
    facts: dict = {}
    table: dict = {}
    even, odd = b213.even_odd(3)
    witnesses = [(census["cells"][v]["mask"], v, curve_moduli(census["cells"][v]["class"][0]), True)
                 for v in rule_a_cells(census)]
    witnesses += [("W1", ALL_PLUS_CELL, W1_MODULI, False), ("flat", ALL_PLUS_CELL, FLAT_MODULI, False)]
    for key, values, moduli, gaussian in witnesses:
        print(f"[cone] witness {key}", file=sys.stderr)
        entry: dict = {"class": census["cells"][values]["class"]}
        _, m_s = overlap_fold(formal(values, moduli_as_g(moduli), (SUM, 0, 0, 0)))
        det_m = sp.expand(b214.ff_det(m_s, (SUM,) + KAPPA, algebraic=gaussian))
        det_b0 = sp.expand(sp.radsimp(m_s.extract(even, odd).det(method="berkowitz")))
        entry["det_m_zero_is_det_b_squared"] = is_zero_alg(det_m.subs(SUM, 0) - det_b0 ** 2)
        extension = {"extension": sp.sqrt(6)} if gaussian else {}
        _, factors = sp.factor_list(det_m, SUM, *KAPPA, **extension)
        entry["det_m_shape"] = tuple(sorted((sp.Poly(b, SUM, *KAPPA).degree_list(), p) for b, p in factors
                                            if b.free_symbols & set(KAPPA)))
        _, factors0 = sp.factor_list(det_b0, *KAPPA, **extension)
        quadrics = [sp.expand(b) for b, p in factors0 if b.free_symbols & set(KAPPA)]
        entry["det_b_zero_shape"] = tuple(sorted((sp.Poly(b, *KAPPA).total_degree(), p) for b, p in factors0
                                                 if b.free_symbols & set(KAPPA)))
        onsite_zero = formal(values, moduli_as_g(moduli), (0, 0, 0, 0))
        g1_m = b213.metric_candidates(onsite_zero)[0].applyfunc(sp.radsimp)
        form = b213.quadratic_form(g1_m, KAPPA)
        entry["det_b_zero_is_onsite_cone"] = b213.proportional(det_b0, form ** 2, KAPPA)
        entry["quadrics_proportional_to_onsite"] = tuple(b213.proportional(q, form, KAPPA) for q in quadrics)
        entry["quadrics_rational"] = all(not q.has(sp.sqrt(6)) for q in quadrics)
        if len(quadrics) == 2:
            entry["pair_proportional"] = b213.proportional(quadrics[0], quadrics[1], KAPPA)
            difference = sp.Poly(sp.expand(sp.radsimp(quadrics[0] - quadrics[1])), *KAPPA)
            entry["pair_differs_in_kt_ky_only"] = difference.monoms() == [(1, 0, 1)]
            entry["coefficients"] = quadric_coefficients(quadrics[0])
        table[key] = entry
    facts["table"] = table
    rule_keys = [k for k in table if isinstance(k, int)]
    facts["det_m_zero_is_det_b_squared_everywhere"] = all(e["det_m_zero_is_det_b_squared"] for e in table.values())
    facts["det_m_shapes"] = tuple(sorted(set(e["det_m_shape"] for e in table.values())))
    facts["det_m_factorization_scope"] = "generic_joint_polynomial_in_s_and_kappa"
    facts["det_b_zero_shapes_rule_a"] = tuple(sorted(set(table[k]["det_b_zero_shape"] for k in rule_keys)))
    facts["det_b_zero_shape_w1"] = table["W1"]["det_b_zero_shape"]
    facts["det_b_zero_shape_flat"] = table["flat"]["det_b_zero_shape"]
    facts["overlap_cone_is_onsite_cone_anywhere"] = any(table[k]["det_b_zero_is_onsite_cone"] for k in rule_keys)
    facts["quadric_proportional_to_onsite_anywhere"] = any(any(table[k]["quadrics_proportional_to_onsite"]) for k in rule_keys)
    facts["pair_distinct_everywhere"] = all(not table[k]["pair_proportional"] for k in rule_keys)
    facts["pair_kt_ky_everywhere"] = all(table[k]["pair_differs_in_kt_ky_only"] for k in rule_keys)
    facts["quadrics_rational_everywhere"] = all(table[k]["quadrics_rational"] for k in rule_keys)
    facts["coefficients_per_class"] = {key: tuple(sorted(set(table[k]["coefficients"] for k in rule_keys if table[k]["class"] == key)))
                                       for key in ((1, -1), (-1, 1))}
    return facts


# ---------------------------------------------------------------------------
# F/G. THE BENCH over QQ(sqrt 6) and QQ(sqrt 6, i): Block 213's (4,2,2), both
# assemblies, both readings, Bloch union = direct, and the principal part at e_t
# ---------------------------------------------------------------------------
def alg_charpoly(matrix: DomainMatrix, domain):
    coefficients = matrix.charpoly()
    return sp.expand(sum(domain.to_sympy(c) * LAM ** (len(coefficients) - 1 - k) for k, c in enumerate(coefficients)))


def symbol_matrix(hodge: DomainMatrix, raising: DomainMatrix, raising_t: DomainMatrix, reading: str) -> DomainMatrix:
    """Block 213's domain_symbol: -K^2 (form) or -(d - H^-1 d^T H)^2 (pencil)."""
    if reading == "form":
        kernel = hodge * raising - raising_t * hodge
        return -(kernel * kernel)
    operator = raising - hodge.inv() * raising_t * hodge
    return -(operator * operator)


def bench_charpolys(cell: sp.Matrix, assembly: str, reading: str) -> tuple:
    """(direct 16 x 16 bench charpoly over QQ(sqrt 6), Bloch union over
    QQ(sqrt 6, i) at Block 213's bench momenta, seconds direct, seconds union)."""
    rules = (b213.onsite_rules if assembly == "onsite" else b213.overlap_rules)(cell, b209.CORNERS, 3)
    raising = b213.raising_rules(b213.lane_rules(3))
    real_field = QQ.algebraic_field(sp.sqrt(6))
    complex_field = QQ.algebraic_field(sp.sqrt(6), sp.I)
    started = time.monotonic_ns()
    hodge = DomainMatrix.from_Matrix(b213.bench_matrix(rules, BENCH_EXTENT)).convert_to(real_field)
    lifted = DomainMatrix.from_Matrix(b213.bench_matrix(raising, BENCH_EXTENT)).convert_to(real_field)
    direct = alg_charpoly(symbol_matrix(hodge, lifted, lifted.transpose(), reading), real_field)
    direct_ms = (time.monotonic_ns() - started) // 1_000_000
    started = time.monotonic_ns()
    product = sp.Integer(1)
    transposed = b213.transpose_rules(raising)
    for z in b213.bench_momenta(BENCH_EXTENT):
        h_b = DomainMatrix.from_Matrix(b213.bloch_matrix(rules, z, 3)).convert_to(complex_field)
        d_b = DomainMatrix.from_Matrix(b213.bloch_matrix(raising, z, 3)).convert_to(complex_field)
        dt_b = DomainMatrix.from_Matrix(b213.bloch_matrix(transposed, z, 3)).convert_to(complex_field)
        product *= alg_charpoly(symbol_matrix(h_b, d_b, dt_b, reading), complex_field)
    union = sp.expand(product)
    return direct, union, direct_ms, (time.monotonic_ns() - started) // 1_000_000


def charpoly_shape(charpoly) -> tuple:
    """Every irreducible factor over QQ as (degree, multiplicity, primitive integer coefficients)."""
    _, factors = sp.factor_list(sp.expand(charpoly), LAM)
    out = []
    for base, power in factors:
        poly = sp.Poly(base, LAM)
        coefficients = tuple(poly.all_coeffs())
        if coefficients[0] < 0:
            coefficients = tuple(-c for c in coefficients)
        out.append((poly.degree(), power, coefficients))
    return tuple(sorted(out))


def primitive_shape_divisor(shape: tuple):
    """Leading-coefficient product needed to recover a monic charpoly."""
    return sp.prod(sp.Integer(coefficients[0]) ** power
                   for _, power, coefficients in shape)


def bench_cells(census: dict) -> dict:
    """The bench cells: L+-'s own cell (mask 2) at the curve moduli, the all-plus
    W1 control and the flat cell, each with the parameters at the line point;
    the first two also at zero parameters (for the overlap comparison)."""
    witness = next(v for v in rule_a_cells(census) if census["cells"][v]["mask"] == 2)
    return {
        "witness line": formal(witness, moduli_as_g(curve_moduli(1)), LINE_POINT),
        "W1 line": formal(ALL_PLUS_CELL, moduli_as_g(W1_MODULI), LINE_POINT),
        "flat line": formal(ALL_PLUS_CELL, moduli_as_g(FLAT_MODULI), LINE_POINT),
        "witness zero": formal(witness, moduli_as_g(curve_moduli(1)), (0, 0, 0, 0)),
        "W1 zero": formal(ALL_PLUS_CELL, moduli_as_g(W1_MODULI), (0, 0, 0, 0)),
    }


def measure_bench(cells: dict) -> dict:
    """F: every (cell, assembly, reading) charpoly of degree 16 on (4,2,2):
    Bloch union = direct bench, the multiset (or the factor shape when a root
    is irrational), the two timings."""
    facts: dict = {}
    table: dict = {}
    for label, cell in cells.items():
        assemblies = ("onsite", "overlap") if label.endswith("line") else ("overlap",)
        for assembly in assemblies:
            for reading in ("form", "pencil"):
                print(f"[bench] {label} {assembly} {reading}", file=sys.stderr)
                direct, union, direct_ms, union_ms = bench_charpolys(cell, assembly, reading)
                table[(label, assembly, reading)] = {
                    "agree": sp.expand(direct - union) == 0, "multiset": b213.multiset_of(direct),
                    "shape": charpoly_shape(direct), "degree": sp.Poly(direct, LAM).degree(),
                    "direct_ms": direct_ms, "union_ms": union_ms, "charpoly": direct,
                }
    facts["table"] = table
    facts["charpoly_count"] = len(table)
    facts["all_agree"] = all(e["agree"] for e in table.values())
    facts["all_degree_16"] = all(e["degree"] == 16 for e in table.values())
    facts["multisets"] = {key: e["multiset"] for key, e in table.items()}
    facts["shapes"] = {key: e["shape"] for key, e in table.items()}
    normalization_keys = {
        "L+- onsite form": ("witness line", "onsite", "form"),
        "W1 onsite form": ("W1 line", "onsite", "form"),
        "W1 onsite pencil": ("W1 line", "onsite", "pencil"),
        "flat onsite form": ("flat line", "onsite", "form"),
    }
    facts["monic_normalization_divisors"] = {
        label: primitive_shape_divisor(table[key]["shape"])
        for label, key in normalization_keys.items()
    }
    facts["overlap_line_equals_zero"] = all(
        table[(f"{c} line", "overlap", r)]["charpoly"] == table[(f"{c} zero", "overlap", r)]["charpoly"]
        for c in ("witness", "W1") for r in ("form", "pencil"))
    facts["overlap_pencil_is_r5_everywhere"] = all(
        e["multiset"] == ((0, 8), (1, 8)) for key, e in table.items() if key[1] == "overlap" and key[2] == "pencil")
    facts["timings_ms"] = {key: (e["direct_ms"], e["union_ms"]) for key, e in table.items()}
    return facts


def principal_charpoly_at_et(cell: sp.Matrix, assembly: str, reading: str):
    """The charpoly of the principal symbol at kappa = e_t: (H0^-1 M)^2 (pencil) or M^2 (form)."""
    h0, m, _ = b214.principal_part(cell, assembly)
    if reading == "pencil":
        operator = (h0.inv() * m).applyfunc(sp.radsimp)
        squared = (operator * operator).applyfunc(sp.radsimp)
    else:
        squared = (m * m).applyfunc(sp.expand)
    at_et = squared.subs({KT: 1, KX: 0, KY: 0})
    field = QQ.algebraic_field(sp.sqrt(6))
    return alg_charpoly(DomainMatrix.from_Matrix(at_et).convert_to(field), field)


def measure_smallk(cells: dict, bench: dict) -> dict:
    """G: the bench against the principal part at kappa = e_t -- the pencil
    bench charpoly equals lam^8 times the charpoly of (H0^-1 M(e_t))^2 under
    the onsite assembly (an exact identity, not a limit), the witness reading
    G1_tt times Block 216's four branch constants on the line; the identity
    fails for the form reading and for the overlap assembly, whose Bloch fold
    at z = (i, 1, 1) is parameter-free and differs from H0."""
    facts: dict = {}
    table: dict = {}
    for label in ("witness line", "W1 line", "flat line"):
        for assembly in ("onsite", "overlap"):
            for reading in ("form", "pencil"):
                principal = principal_charpoly_at_et(cells[label], assembly, reading)
                table[(label, assembly, reading)] = sp.expand(bench["table"][(label, assembly, reading)]["charpoly"] - LAM ** 8 * principal) == 0
    facts["identity_table"] = table
    facts["onsite_pencil_identity_everywhere"] = all(table[(l, "onsite", "pencil")] for l in ("witness line", "W1 line", "flat line"))
    facts["identity_fails_form_and_overlap"] = not any(v for key, v in table.items() if key[1] == "overlap" or key[2] == "form")
    # the witness reads G1_tt times the four branch constants of Block 216's line-1/4 table
    g1_m = b213.metric_candidates(cells["witness zero"])[0].applyfunc(sp.radsimp)
    g1_tt = sp.radsimp(g1_m[0, 0])
    facts["g1_tt_witness"] = g1_tt
    predicted = tuple(sorted(((sp.radsimp(g1_tt * sp.Rational(ratio)), power)
                              for ratio, power, _ in b216.BRANCH_TABLE[("L+-", "line 1/4")][0]), key=lambda t: t[0]))
    bench_multiset = bench["table"][("witness line", "onsite", "pencil")]["multiset"]
    facts["witness_multiset_is_g1tt_times_constants"] = bench_multiset is not None and bench_multiset == ((0, 8),) + predicted
    facts["predicted_nonzero"] = predicted
    # the overlap Bloch fold at the bench's nonzero point versus the fold at s = 0, at the witness
    rules = b213.overlap_rules(cells["witness line"], b209.CORNERS, 3)
    bloch_i = b213.bloch_matrix(rules, (sp.I, 1, 1), 3)
    h_zero, _, _ = b214.principal_part(cells["witness zero"], "overlap")
    facts["bloch_fold_differs_from_h0_entries"] = residual_count((bloch_i - h_zero).applyfunc(sp.expand))
    facts["bloch_fold_parameter_free_at_witness"] = residual_count((bloch_i - b213.bloch_matrix(
        b213.overlap_rules(cells["witness zero"], b209.CORNERS, 3), (sp.I, 1, 1), 3)).applyfunc(sp.expand)) == 0
    # the onsite cone at kappa = e_t is a number: det M(e_t) = c G1_tt^4 (Block 216's constant), no zero
    h0, m, _ = b214.principal_part(cells["witness line"], "onsite")
    det_et = sp.radsimp(m.subs({KT: 1, KX: 0, KY: 0}).det(method="berkowitz"))
    facts["onsite_cone_at_et"] = sp.radsimp(det_et / g1_tt ** 4)
    return facts


@dataclass(frozen=True)
class Facts:
    authority: AuthorityCertificate
    group: dict
    census: dict
    fold: dict
    loci: dict
    cone: dict
    bench: dict
    smallk: dict
    axiom_text: str
    note_text: str
    timings: dict


def measure() -> Facts:
    timings: dict = {}
    started = time.monotonic_ns()

    def lap(label: str) -> None:
        nonlocal started
        now = time.monotonic_ns()
        timings[label] = (now - started) // 1_000_000
        started = now
        print(f"[phase] {label}: {timings[label]} ms", file=sys.stderr)

    authority = authority_certificate()
    lap("authority")
    group = b215.measure_group()
    lap("group")
    census = b216.measure_census()
    lap("census")
    fold = measure_fold()
    lap("fold")
    loci = measure_loci(group, census)
    lap("loci")
    cone = measure_cone(census)
    lap("cone")
    cells = bench_cells(census)
    bench = measure_bench(cells)
    lap("bench")
    smallk = measure_smallk(cells, bench)
    lap("smallk")
    axiom_text = (ROOT / AXIOM_PATH).read_text(encoding="utf-8") if (ROOT / AXIOM_PATH).is_file() else ""
    note_text = NOTE_PATH.read_text(encoding="utf-8") if NOTE_PATH.is_file() else ""
    return Facts(authority, group, census, fold, loci, cone, bench, smallk, axiom_text, note_text, timings)


# ---------------------------------------------------------------------------
# THE DECLARED LITERALS -- every claim is a constant compared against a
# measurement; a mutation rewrites exactly one claim.
# ---------------------------------------------------------------------------
RULE_A_MASKS = (2, 11, 16, 25, 38, 47, 52, 61)                  # = Block 216's RULE_A_MASKS
FOLD_DIAGONAL = "(v0 + 3*v1)*(v0*v1 + 1)/(8*v0*v1)"               # h0 = (v0 + 3 v1 + 3/v0 + 1/v1)/8, Block 213's
FOLD_COUPLING_LITERALS = ("-(g0*s_tx0*v0*v1 + g1*s_tx1)/(4*v0)",  # 2 h_f, h_f = -(s_f0 v1 g0 + s_f1 g1/v0)/8
                          "-(g0*s_ty0*v0*v1 + g1*s_ty1)/(4*v0)",
                          "-(g0*s_xy0*v0*v1 + g1*s_xy1)/(4*v0)")
FOLD_COUPLING_COUNT = 12                                          # four two-flip pairs per face
FOLD_ZERO_FREE_SYMBOLS = ("g0", "g1", "s_tx0", "s_tx1", "s_ty0", "s_ty1", "s_xy0", "s_xy1", "v0", "v1")
BENCH_MOMENTA = (("1", "1", "1"), ("I", "1", "1"))                 # Block 213's bench_momenta((4,2,2))
ONSITE_STABILISER_CLASS = "S3_body"
OVERLAP_STRICT_FEASIBLE = (0,)                                    # the identity alone, at every s
OVERLAP_TWISTED_CLASSES = ("D4_face",)
OVERLAP_TWISTED_ORDERS = (8,)
OVERLAP_TWISTED_AXES = (((0, 1, 0),),)                            # the x axis in (t, x, y): the face with the odd sign product is ty
COMMON_CLASSES = ("C2_edge",)
FORCED_BY_ORDER = ((2, (("g0",), ("g0*v0*v1 + g1",), ("g1",))),
                   (2, (("g0*v0*v1 + g1",), ("g0*v0*v1 - g1",))),
                   (3, (("g0",), ("g1",))))
FORCED_UNION = ("g0", "g0*v0*v1 + g1", "g0*v0*v1 - g1", "g1")
SHEAR_RELATIONS_ON_CURVE = {(1, -1): ((sp.Rational(3, 4), sp.Rational(-1, 4)),),
                            (-1, 1): ((sp.Rational(7, 9), sp.Rational(1, 9)),)}
UNION_LOCUS = (("s",),)
DET_DEGREES_S = ((4, 0),)
LOCI_WITNESS_COUNT = 10
W1_TWISTED_CLASS = "O"
W1_STRICT_FEASIBLE = (0,)
FLAT_STRICT_ALL_S_CLASS = "D4_face"
FLAT_STRICT_ONLY_AT_ZERO_COUNT = 16
FLAT_TWISTED_CLASS = "O"
DET_M_SHAPES = ((((2, 4, 4, 4), 2),),)                            # one irreducible factor, degree 2 in s and 4 in kappa, squared
DET_B_ZERO_SHAPES_RULE_A = (((2, 1), (2, 1)),)
DET_B_ZERO_SHAPE_W1 = ((2, 1), (2, 1))
DET_B_ZERO_SHAPE_FLAT = ((2, 2),)
OVERLAP_CONE_COEFFICIENTS = {                                     # (c_xx, |c_tx|, |c_ty|, |c_xy|, c_yy), kt^2 monic
    (1, -1): ((sp.Rational(59701, 57109), sp.Rational(24516, 57109), sp.Rational(2988, 57109), sp.Rational(24516, 57109), sp.Integer(1)),),
    (-1, 1): ((sp.Rational(64961, 61889), sp.Rational(27664, 61889), sp.Rational(2192, 61889), sp.Rational(27664, 61889), sp.Integer(1)),),
}
R5_MULTISET = ((0, 8), (1, 8))
WITNESS_ONSITE_PENCIL = ((0, 8), (sp.Rational(9, 8), 2), (sp.Rational(16, 11), 2), (sp.Rational(18, 11), 4))
WITNESS_OVERLAP_FORM = ((0, 8), (sp.Rational(36481, 55296), 4), (sp.Rational(89401, 55296), 4))
W1_OVERLAP_FORM = ((0, 8), (sp.Rational(116281, 147456), 4), (sp.Rational(4844401, 3686400), 4))   # = Block 214's OVERLAP_FORM_W1
FLAT_ONSITE_PENCIL = ((0, 8), (1, 2), (sp.Rational(16, 15), 6))
WITNESS_ONSITE_FORM_SHAPE = ((1, 8, (1, 0)), (4, 2, (55296, -388672, 698656, -422145, 69984)))
W1_ONSITE_PENCIL_SHAPE = ((1, 2, (15, -16)), (1, 8, (1, 0)), (3, 2, (4801335, -18293776, 22913024, -9437184)))
W1_ONSITE_FORM_SHAPE = ((1, 8, (1, 0)), (4, 2, (129600, -647676, 1086353, -711440, 147456)))
BENCH_CHARPOLY_COUNT = 16
GENERIC_FACTORIZATION_SCOPE = "generic_joint_polynomial_in_s_and_kappa"
COEFFICIENT_GCD = ("s**2",)
MONIC_NORMALIZATION_DIVISORS = {
    "L+- onsite form": sp.Integer(55296) ** 2,
    "W1 onsite form": sp.Integer(129600) ** 2,
    "W1 onsite pencil": sp.Integer(15 * 4801335) ** 2,
    "flat onsite form": sp.Integer(4 * 16) ** 2,
}
G1_TT_WITNESS = sp.Rational(9, 8)
PREDICTED_NONZERO = ((sp.Rational(9, 8), 2), (sp.Rational(16, 11), 2), (sp.Rational(18, 11), 4))
BLOCH_FOLD_DIFFERS_ENTRIES = 16
ONSITE_CONE_AT_ET = sp.Rational(64, 81)                            # Block 216's c at pi0 = +1
SCOUT_GRADE_FENCE = ("scout-grade finite exact linear algebra on one cell form, "
                     "not a spacetime and not a dynamics")
SCOUT_GRADE_ONLY = True
INSTANCE_SCOPE = (
    "one cell form: Block 211's family at the 8 rule-A star-pattern cells with Block 216's curve witnesses, the all-plus W1 and flat cells as controls",
    "two assemblies measured (onsite through Block 216's facts, overlap here); neither decided; two readings on the bench, neither selected",
    "the overlap parameter s symbolic for the loci and the cone; the bench at the numeric line point (1/4, -1/4, 1/4), D07 = 0, and at zero parameters",
    "one bench, (4,2,2), at one covariant witness (L+-'s cell, mask 2), one all-plus control and the flat cell; no other extent, witness or point",
    "the covariance notion: Block 215's (E_R R) H (E_R R)^T = H on the folded H0, twisted over its 64 sign vectors or strict; no other twist",
    "no continuum, no light cone, no dispersion law, no metric of anything physical; 'one metric's cone' and 'non-Hodge pair' name Block 213's statements only",
)
INSTANCE_SCOPE_COUNT = 6

N5_FENCE = "N5: The corrected Block 217 claim is finite. At eight curve witnesses plus W1 and flat controls, the univariate coefficient gcd is s^2 and its square-free part is s, certifying the locus s = 0 only at those ten witnesses. The joint factorization in (s,kappa) is generic and does not imply irreducibility at every nonzero-s specialization. Primitive bench factor shapes are divided by their stated leading-coefficient squares to obtain monic characteristic polynomials. No assembly selection, premise adoption, physical cone, action, spacetime, continuum, dispersion law, or dynamics is claimed."


def scope_certificate(text: str) -> dict:
    return {"n5_verbatim": N5_FENCE in text}


def build_claims(mutation: str) -> dict:
    claims = {
        "current_main": CURRENT_MAIN, "parent_commit": PARENT_COMMIT,
        "registered": (), "gravity_supplied": False, "covariance_inherited": False,
        "assembly_decided": False, "cell_selected": False, "metric_supplied": False,
        "rule_a_masks": RULE_A_MASKS, "onsite_stabiliser_class": ONSITE_STABILISER_CLASS,
        "fold_coupling_literals": FOLD_COUPLING_LITERALS, "flat_control": True,
        "union_locus": UNION_LOCUS, "overlap_strict_feasible": OVERLAP_STRICT_FEASIBLE,
        "overlap_twisted_classes": OVERLAP_TWISTED_CLASSES, "forced_by_order": FORCED_BY_ORDER,
        "curve_violates_relations": True,
        "det_b_zero_shapes_rule_a": DET_B_ZERO_SHAPES_RULE_A, "overlap_cone_is_onsite_cone": False,
        "det_m_shapes": DET_M_SHAPES,
        "witness_onsite_pencil": WITNESS_ONSITE_PENCIL, "all_agree": True, "w1_overlap_form": W1_OVERLAP_FORM,
        "onsite_pencil_identity": True, "bloch_fold_parameter_free": True,
        "scout_grade": SCOUT_GRADE_FENCE, "instance_scope_count": INSTANCE_SCOPE_COUNT,
        "n5_verbatim": True, "float_absent": True,
    }
    flips = {
        "stale_main_authority": ("current_main", STALE_MAIN),
        "stale_parent_authority": ("parent_commit", STALE_PARENT_COMMIT),
        "claim_objects_registered": ("registered", ("the overlap fold's D4",)),
        "claim_gravity_supplied": ("gravity_supplied", True),
        "claim_covariance_inherited": ("covariance_inherited", True),
        "claim_assembly_decided": ("assembly_decided", True),
        "claim_cell_selected": ("cell_selected", True),
        "claim_metric_supplied": ("metric_supplied", True),
        "break_cell_census": ("rule_a_masks", RULE_A_MASKS[:4]),
        "break_witness_reproduction": ("onsite_stabiliser_class", "C3_body"),
        "break_fold_sees_sum": ("fold_coupling_literals", FOLD_COUPLING_LITERALS[:2]),
        "break_flat_control": ("flat_control", False),
        "break_union_locus_s": ("union_locus", ((),)),
        "break_strict_stabiliser": ("overlap_strict_feasible", (0, 23)),
        "break_twisted_stabiliser": ("overlap_twisted_classes", ("S3_body",)),
        "break_shear_relation": ("forced_by_order", FORCED_BY_ORDER[:2]),
        "claim_curve_satisfies_shear_relation": ("curve_violates_relations", False),
        "break_overlap_cone_pair": ("det_b_zero_shapes_rule_a", (((2, 2),),)),
        "claim_overlap_cone_is_onsite_cone": ("overlap_cone_is_onsite_cone", True),
        "break_overlap_cone_symbolic_s": ("det_m_shapes", ((((2, 2, 2, 2), 4),),)),
        "break_bench_multisets": ("witness_onsite_pencil", R5_MULTISET),
        "break_bloch_equals_direct": ("all_agree", False),
        "break_bench_control": ("w1_overlap_form", R5_MULTISET),
        "break_bench_reads_principal_part": ("onsite_pencil_identity", False),
        "break_bloch_fold_sees_parameters": ("bloch_fold_parameter_free", False),
        "break_scout_grade_fence": ("scout_grade", "a spacetime and a dynamics"),
        "break_instance_scope": ("instance_scope_count", 2),
        "drop_n5_fence": ("n5_verbatim", False),
        "break_float_absence": ("float_absent", False),
    }
    if mutation:
        key, value = flips[mutation]
        claims[key] = value
    return claims


def build_checks(facts: Facts, claims: dict) -> Checks:
    checks = Checks()
    au = facts.authority
    checks.check("A-1", "THE COMPLETE RUNTIME AND CITATION INPUT CLOSURE matches fixed SHA-256 literals; no moving ref is consulted",
                 au.all_inputs_content_bound and claims["current_main"] == SOURCE_BASE_COMMIT)
    checks.check("A-2", "THE CORRECTED BLOCK 216 NOTE AND RUNNER are content-bound finite suppliers; ancestry is provenance only",
                 au.parent_inputs_content_bound and claims["parent_commit"] == PARENT_SOURCE_SHA256)
    checks.check("A-3", "THE CORRECTED 213--216 IMPORT CLOSURE is present and every declared input is readable",
                 au.machinery_import_landed and au.inputs_readable == len(AUDIT_INPUT_PATHS)
                 and not au.inputs_missing)
    checks.check("B-1", "NOTHING REGISTERED, NOTHING ADOPTED: six imposed objects, zero registered, zero adopted",
                 len(IMPOSED_OBJECTS) == 6 and claims["registered"] == REGISTERED_OBJECTS == () and ADOPTED_OBJECTS == ())
    checks.check("B-2", "NO GRAVITY IS SUPPLIED: nine structures enumerated as not supplied",
                 not claims["gravity_supplied"] and not GRAVITY_SUPPLIED_CLAIMED and len(UNSUPPLIED_GRAVITY_STRUCTURES) == 9)
    checks.check("B-3", "THE AXIOM CLAUSE IS QUOTED VERBATIM AND GOVERNS THE RULE; that the cell form inherits it is a READING, asserted nowhere (the theorem is the conditional)",
                 AXIOM_COVARIANCE_CLAUSE in facts.axiom_text and not claims["covariance_inherited"] and not COVARIANCE_INHERITED_CLAIMED)
    checks.check("B-4", "NO CELL, NO SUBGROUP, NO ASSEMBLY, NO READING, NO PARAMETER VALUE IS SELECTED, AND NO METRIC IS SUPPLIED: the difference between the assemblies is measured, not a selector",
                 not claims["cell_selected"] and not CELL_SELECTED_CLAIMED and not claims["assembly_decided"] and not ASSEMBLY_DECIDED_CLAIMED
                 and not claims["metric_supplied"] and not METRIC_SUPPLIED_CLAIMED and not SUBGROUP_SELECTED_CLAIMED
                 and not PARAMETER_VALUE_SELECTED_CLAIMED and not READING_SELECTED_CLAIMED)
    checks.check("B-5", "THE WORDS COVARIANCE, CONE, CELL, ASSEMBLY AND BENCH ARE SCOPED; six readings enumerated, none licensed; no continuum, no light cone, no spacetime cone",
                 len(SCOPED_HEADLINE_WORDS) == 5 and len(READINGS) == 6 and not READINGS_LICENSED_CLAIMED
                 and not CONTINUUM_LIMIT_CLAIMED and not LIGHT_CONE_CLAIMED and not CONE_IS_SPACETIME_CONE_CLAIMED)
    ce, fo, lo, co, be, sk = facts.census, facts.fold, facts.loci, facts.cone, facts.bench, facts.smallk
    checks.check("C-1", "THE CELLS ARE BLOCK 216's: the census reproduces its 8 rule-A masks (2, 11, 16, 25, 38, 47, 52, 61) among its 16 star-pattern cells, indexings agreeing",
                 ce["indexing_agrees"] and ce["rule_a_masks"] == claims["rule_a_masks"] == RULE_A_MASKS == b216.RULE_A_MASKS
                 and ce["star_masks"] == b216.STAR_MASKS and lo["rule_a_count"] == 8)
    checks.check("C-2", "THE WITNESSES ARE BLOCK 216's: at every rule-A cell the transported curve point has the S3_body as onsite strict stabiliser, both shears nonzero, v0 v1 = 3/4 or 8/9",
                 claims["onsite_stabiliser_class"] == ONSITE_STABILISER_CLASS and lo["onsite_stabiliser_is_s3_everywhere"]
                 and all(lo["table"][k]["shears_nonzero"] and lo["table"][k]["volume_product"] in (sp.Rational(3, 4), sp.Rational(8, 9))
                         for k in lo["table"] if isinstance(k, int)))
    checks.check("C-3", "THE FOLD LEMMA AT SYMBOLIC FACE SIGNS AND MODULI: the overlap H0 sees the parameters only through s at every cell, its parity block is (s/4) P111, it is linear in s, and at s = 0 it is h0 I plus twelve two-flip couplings -(s_f0 g0 v0 v1 + s_f1 g1)/(4 v0), one magnitude per face",
                 fo["fold_sees_sum_only_symbolic_signs"] and fo["parity_block_is_sum_over_four_p111"] and fo["fold_linear_in_s"]
                 and fo["fold_diagonal"] == FOLD_DIAGONAL and fo["fold_diagonal_scalar"] and fo["coupling_count"] == FOLD_COUPLING_COUNT
                 and fo["coupling_literals"] == claims["fold_coupling_literals"] == FOLD_COUPLING_LITERALS
                 and fo["couplings_are_two_flip_pairs"] and fo["fold_zero_free_symbols"] == FOLD_ZERO_FREE_SYMBOLS)
    checks.check("C-4", "THE FLAT CONTROL: both assemblies give H = I at zero parameters (Block 213's D-1) and the flat fold is I + (s/4) P111",
                 claims["flat_control"] and fo["flat_both_assemblies_identity"] and fo["flat_fold_is_identity_plus_sum_p111"])
    checks.check("D-1", "THE FINITE UNION LOCUS IN s IS s = 0 at all 10 named witnesses: the coefficient gcd in QQ[s] or QQ(sqrt(6))[s] is s^2, its square-free part is s, det M has degree 4 in s, and det B is s-free",
                 lo["union_locus_everywhere"] == claims["union_locus"] == UNION_LOCUS
                 and lo["coefficient_gcd_everywhere"] == COEFFICIENT_GCD
                 and lo["coefficient_counts_positive"] and lo["det_degrees_s"] == DET_DEGREES_S
                 and lo["witness_count"] == LOCI_WITNESS_COUNT)
    checks.check("D-2", "THE STRICT STABILISER OF THE OVERLAP FOLD IS TRIVIAL at every rule-A witness for every s (the identity is the only feasible rotation); at the all-plus W1 control it is trivial too",
                 lo["overlap_strict_trivial_everywhere"] and claims["overlap_strict_feasible"] == OVERLAP_STRICT_FEASIBLE
                 and all(lo["table"][k]["strict_feasible"] == OVERLAP_STRICT_FEASIBLE for k in lo["table"] if isinstance(k, int))
                 and lo["w1_strict_feasible"] == W1_STRICT_FEASIBLE)
    checks.check("D-3", "THE TWISTED STABILISER OF THE OVERLAP FOLD IS A D4_face OF ORDER 8 ABOUT THE x AXIS FOR EVERY s at every rule-A witness, the S3_body is not inside it, the two assemblies share exactly one twisted C2_edge; the all-plus W1 fold is twisted-O for every s; the flat fold is strictly D4_face for every s and strictly covariant under the other 16 only at s = 0, twisted-O for every s",
                 lo["overlap_twisted_classes"] == claims["overlap_twisted_classes"] == OVERLAP_TWISTED_CLASSES
                 and lo["overlap_twisted_is_all_s"] and lo["overlap_twisted_orders"] == OVERLAP_TWISTED_ORDERS
                 and lo["overlap_twisted_axes"] == OVERLAP_TWISTED_AXES and not lo["s3_in_twisted_anywhere"]
                 and lo["common_classes"] == COMMON_CLASSES and lo["w1_twisted_class"] == W1_TWISTED_CLASS
                 and lo["flat_strict_all_s_class"] == FLAT_STRICT_ALL_S_CLASS
                 and lo["flat_strict_only_at_zero_count"] == FLAT_STRICT_ONLY_AT_ZERO_COUNT and lo["flat_twisted_class"] == FLAT_TWISTED_CLASS)
    checks.check("D-4", "THE SHEAR RELATION AT SYMBOLIC MODULI under each cell's own S3_body: the order-3 elements force g0 = g1 = 0, the order-2 elements force g0 v0 v1 + g1 = 0 with g0 = g1 = 0 or with g0 v0 v1 - g1 = 0 -- the same at all 8 cells; no shear-alive strict locus exists",
                 lo["forced_by_order"] == (claims["forced_by_order"],) and claims["forced_by_order"] == FORCED_BY_ORDER
                 and lo["forced_union"] == (FORCED_UNION,))
    checks.check("D-5", "THE CURVE VIOLATES EVERY VARIANT: g0 v0 v1 + g1 = 3/4 and g0 v0 v1 - g1 = -1/4 where pi0 = +1, 7/9 and 1/9 where pi0 = -1, both shears nonzero -- the overlap fold at a rule-A witness is NOT strictly S3-covariant, and the two assemblies differ in covariance at the covariant cells",
                 claims["curve_violates_relations"] and lo["curve_violates_every_relation"]
                 and lo["shear_relations_on_curve"] == SHEAR_RELATIONS_ON_CURVE)
    checks.check("E-1", "THE OVERLAP CONE AT s = 0 IS A NON-HODGE PAIR at every rule-A witness: det M(0) = det B(0)^2, det B(0) = Q+ Q- with two DISTINCT rational quadrics differing in the sign of the kt ky term alone, the declared coefficient magnitudes per class; the same shape at the all-plus W1, one quadric squared at the flat cell",
                 co["det_m_zero_is_det_b_squared_everywhere"] and co["det_b_zero_shapes_rule_a"] == claims["det_b_zero_shapes_rule_a"] == DET_B_ZERO_SHAPES_RULE_A
                 and co["pair_distinct_everywhere"] and co["pair_kt_ky_everywhere"] and co["quadrics_rational_everywhere"]
                 and co["coefficients_per_class"] == OVERLAP_CONE_COEFFICIENTS and co["det_b_zero_shape_w1"] == DET_B_ZERO_SHAPE_W1
                 and co["det_b_zero_shape_flat"] == DET_B_ZERO_SHAPE_FLAT)
    checks.check("E-2", "THE OVERLAP CONE IS NOT THE ONSITE CONE: at no rule-A witness is det B(0) proportional to (k^T G1 k)^2, and neither quadric is proportional to k^T G1 k -- not one metric's cone",
                 not claims["overlap_cone_is_onsite_cone"] and not co["overlap_cone_is_onsite_cone_anywhere"]
                 and not co["quadric_proportional_to_onsite_anywhere"])
    checks.check("E-3", "THE GENERIC JOINT POLYNOMIAL IN (s,kappa) is one irreducible factor squared, of degree 2 in s and 4 in kappa, at all 10 witnesses; exceptional fixed nonzero-s specializations are not classified",
                 co["det_m_shapes"] == claims["det_m_shapes"] == DET_M_SHAPES
                 and co["det_m_factorization_scope"] == GENERIC_FACTORIZATION_SCOPE)
    checks.check("F-1", "THE BENCH AT THE COVARIANT WITNESS (L+-'s cell, line point 1/4): onsite pencil {0 x8, 9/8 x2, 16/11 x2, 18/11 x4}, onsite form has the declared primitive quartic factor shape, with its monic divisor applied, overlap form {0 x8, 36481/55296 x4, 89401/55296 x4}, overlap pencil R5's",
                 be["multisets"][("witness line", "onsite", "pencil")] == claims["witness_onsite_pencil"] == WITNESS_ONSITE_PENCIL
                 and be["shapes"][("witness line", "onsite", "form")] == WITNESS_ONSITE_FORM_SHAPE
                 and be["multisets"][("witness line", "overlap", "form")] == WITNESS_OVERLAP_FORM
                 and be["multisets"][("witness line", "overlap", "pencil")] == R5_MULTISET)
    checks.check("F-2", "BLOCH UNION = DIRECT BENCH at every one of the 16 degree-16 charpolys (Block 213's E-gate over QQ(sqrt 6) and QQ(sqrt 6, i))",
                 claims["all_agree"] and be["all_agree"] and be["all_degree_16"] and be["charpoly_count"] == BENCH_CHARPOLY_COUNT)
    checks.check("F-3", "THE CONTROLS ON THE BENCH: at the all-plus W1 the onsite pencil has primitive shape lam^8 (15 lam - 16)^2 times an irreducible cubic squared, the onsite form has the declared primitive quartic factor shape; their monic divisors are applied, the overlap form Block 214's OVERLAP_FORM_W1; at the flat cell the onsite pencil is {0 x8, 1 x2, 16/15 x6}; the overlap pencil is R5's everywhere",
                 be["shapes"][("W1 line", "onsite", "pencil")] == W1_ONSITE_PENCIL_SHAPE and be["shapes"][("W1 line", "onsite", "form")] == W1_ONSITE_FORM_SHAPE
                 and be["multisets"][("W1 line", "overlap", "form")] == claims["w1_overlap_form"] == W1_OVERLAP_FORM == b214.OVERLAP_FORM_W1
                 and be["multisets"][("flat line", "onsite", "pencil")] == FLAT_ONSITE_PENCIL and be["overlap_pencil_is_r5_everywhere"])
    checks.check("F-4", "PRIMITIVE FACTOR SHAPES ARE NORMALIZED TO MONIC CHARACTERISTIC POLYNOMIALS by the four declared leading-coefficient products",
                 be["monic_normalization_divisors"] == MONIC_NORMALIZATION_DIVISORS)
    checks.check("G-1", "THE BENCH READS THE PRINCIPAL PART AT ONE DIRECTION, EXACTLY: the bench momenta are z = (1,1,1) and (i,1,1); the onsite pencil bench charpoly equals lam^8 times the charpoly of (H0^-1 M(e_t))^2 at the witness, the control and the flat cell; at the witness that is G1_tt = 9/8 times Block 216's four branch constants; the onsite cone at e_t is the number 64/81 G1_tt^4; the identity fails for the form reading and for the overlap assembly -- no continuum reading",
                 fo["bloch_momenta"] == BENCH_MOMENTA and claims["onsite_pencil_identity"] and sk["onsite_pencil_identity_everywhere"]
                 and sk["identity_fails_form_and_overlap"] and sk["g1_tt_witness"] == G1_TT_WITNESS
                 and sk["witness_multiset_is_g1tt_times_constants"] and sk["predicted_nonzero"] == PREDICTED_NONZERO
                 and sk["onsite_cone_at_et"] == ONSITE_CONE_AT_ET)
    checks.check("G-2", "THE BENCH DOES NOT SEE THE OVERLAP SUM: the overlap Bloch fold at z = (i,1,1) is parameter-free at symbolic signs, moduli and parameters, differs from H0 in 16 entries at the witness, and the overlap bench charpolys at the line point equal those at zero parameters",
                 claims["bloch_fold_parameter_free"] and fo["bloch_fold_at_i_parameter_free"] and sk["bloch_fold_parameter_free_at_witness"]
                 and sk["bloch_fold_differs_from_h0_entries"] == BLOCH_FOLD_DIFFERS_ENTRIES and be["overlap_line_equals_zero"])
    checks.check("H-1", "SCOUT-GRADE FENCE, inherited verbatim from Blocks 211, 213, 214, 215 and 216",
                 claims["scout_grade"] == SCOUT_GRADE_FENCE == b216.SCOUT_GRADE_FENCE and SCOUT_GRADE_ONLY)
    checks.check("H-2", "THE INSTANCE SCOPE IS ENUMERATED: six restrictions",
                 claims["instance_scope_count"] == len(INSTANCE_SCOPE) == 6)
    sc = scope_certificate(facts.note_text)
    checks.check("I-1", "THE NOTE IS PRESENT AND CARRIES THE N5 FENCE BYTE-IDENTICALLY",
                 bool(facts.note_text) and sc["n5_verbatim"] == claims["n5_verbatim"] and claims["n5_verbatim"])
    checks.check("I-2", "NO nsimplify, NO float literal, NO float call in this runner's source",
                 nsimplify_occurrences() == 0 and float_literal_occurrences() == 0 and float_call_sites() == 0 and claims["float_absent"])
    return checks


def report_measured(facts: Facts, elapsed_ns: int) -> None:
    print("== BLOCK 217: the other assembly at the covariant cells, and the bench -- measured facts ==")
    print(f"authority: {facts.authority}")
    for name in ("fold", "loci", "cone", "bench", "smallk"):
        section = getattr(facts, name)
        for key in sorted(section, key=str):
            value = section[key]
            if isinstance(value, dict):
                for inner in sorted(value, key=str):
                    item = value[inner]
                    if isinstance(item, dict):
                        item = {k: v for k, v in item.items() if k != "charpoly"}
                    print(f"{name} {key} {inner}: {item}")
            else:
                print(f"{name} {key}: {value}")
    print(f"timings_ms: {facts.timings}  elapsed_ms: {elapsed_ns // 1_000_000}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS, default="")
    parser.add_argument("--list-mutations", action="store_true")
    arguments = parser.parse_args()
    if arguments.list_mutations:
        for name in MUTATIONS:
            print(name)
        return 0
    mutation = arguments.mutation
    started_ns = time.monotonic_ns()
    # Every measurement happens once, before any mutation flag is consulted.
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
