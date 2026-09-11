#!/usr/bin/env python3
"""Corrected Block 219 finite three-direction bench calculation.

The runner retains the exact declared direct/Bloch comparisons, onsite
Bloch/principal-part similarity, named L+- seven-point ratios and quadratic
read-off, two named rescalings, and overlap-fold measurements on one (4,4,4)
bench. The W1 control compares complete normalized monic characteristic
polynomials across pure-t and pure-x. The pointwise ratio 32/33 at the triply
mixed point is explicitly not treated as a branch-constant counterexample.
Primitive integer factor shapes are kept distinct from monic polynomials.
No parent theorem, premise, assembly choice, physical metric, cone, action,
spacetime, continuum, dispersion law, dynamics, or gravity is supplied.
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
from sympy.polys.matrices import DomainMatrix

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

# THE MACHINERY IMPORTS, LANDED IN THIS BRANCH AND READ-ONLY: Block 218 (the
# two-direction bench over the algebraic fields, its helpers) and through it
# Blocks 217, 216, 215, 214, 213, 211, 209.
try:
    import admissibility_dirac_kahler_two_direction_bench_covariant_witness_2026_09_05 as b218
    B218_IMPORT_LANDED = True
except ModuleNotFoundError:                            # pragma: no cover
    b218 = None
    B218_IMPORT_LANDED = False
b217 = b218.b217 if b218 is not None else None
b216 = b218.b216 if b218 is not None else None
b214 = b218.b214 if b218 is not None else None
b213 = b218.b213 if b218 is not None else None
b211 = b218.b211 if b218 is not None else None
b209 = b218.b209 if b218 is not None else None
MACHINERY_IMPORT_LANDED = bool(B218_IMPORT_LANDED and b218 is not None and b218.MACHINERY_IMPORT_LANDED
                               and b217 is not None and b216 is not None and b214 is not None
                               and b213 is not None and b211 is not None and b209 is not None)
# Corrected finite suppliers. Every live implementation and citation input is
# bound below by SHA-256. Historical Git ancestry remains in recovery only.
B218_NOTE = "docs/ADMISSIBILITY_DIRAC_KAHLER_TWO_DIRECTION_BENCH_COVARIANT_WITNESS_BOUNDED_THEOREM_NOTE_2026-09-05.md"
B218_RUNNER = "scripts/admissibility_dirac_kahler_two_direction_bench_covariant_witness_2026_09_05.py"
B217_NOTE = "docs/ADMISSIBILITY_DIRAC_KAHLER_OVERLAP_ASSEMBLY_COVARIANT_CELLS_BOUNDED_THEOREM_NOTE_2026-09-05.md"
B217_RUNNER = "scripts/admissibility_dirac_kahler_overlap_assembly_covariant_cells_2026_09_05.py"
B216_NOTE = "docs/ADMISSIBILITY_DIRAC_KAHLER_COVARIANT_CURVED_CELL_CONE_BOUNDED_THEOREM_NOTE_2026-09-05.md"
B216_RUNNER = "scripts/admissibility_dirac_kahler_covariant_curved_cell_cone_2026_09_05.py"
B215_NOTE = "docs/ADMISSIBILITY_DIRAC_KAHLER_DUALITY_COVARIANCE_LOCUS_BOUNDED_THEOREM_NOTE_2026-09-05.md"
B215_RUNNER = "scripts/admissibility_dirac_kahler_duality_covariance_locus_2026_09_05.py"
B214_NOTE = "docs/ADMISSIBILITY_DIRAC_KAHLER_DUALITY_PARAMETERS_PRINCIPAL_PART_BOUNDED_THEOREM_NOTE_2026-09-05.md"
B214_RUNNER = "scripts/admissibility_dirac_kahler_duality_parameters_principal_part_2026_09_05.py"
B213_NOTE = "docs/ADMISSIBILITY_DIRAC_KAHLER_WEIGHTED_KERNEL_DISPERSION_BOUNDED_THEOREM_NOTE_2026-09-05.md"
B213_RUNNER = "scripts/admissibility_dirac_kahler_weighted_kernel_dispersion_2026_09_05.py"
B213_HELPER_PATH = "scripts/admissibility_dirac_kahler_weighted_kernel_released7981_7988_fixtures_2026_09_10.py"
B105_NOTE = "docs/ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md"
B105_RUNNER = "scripts/admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_2026_08_14.py"
GROUP_HELPER_PATH = "scripts/admissibility_dirac_kahler_released7992_7994_group_fixture_2026_09_10.py"
PARENT_NOTE = B218_NOTE
PARENT_RUNNER = B218_RUNNER
PARENT_ARTIFACTS = (PARENT_NOTE, PARENT_RUNNER)
FINAL_NOTE_NAME = "ADMISSIBILITY_DIRAC_KAHLER_THREE_DIRECTION_BENCH_COVARIANT_WITNESS_BOUNDED_THEOREM_NOTE_2026-09-05.md"
NOTE_PATH = ROOT / "docs" / FINAL_NOTE_NAME
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"

AUDIT_INPUT_PATHS = (
    'docs/ADMISSIBILITY_DIRAC_KAHLER_THREE_DIRECTION_BENCH_COVARIANT_WITNESS_BOUNDED_THEOREM_NOTE_2026-09-05.md',
    'docs/ADMISSIBILITY_DIRAC_KAHLER_TWO_DIRECTION_BENCH_COVARIANT_WITNESS_BOUNDED_THEOREM_NOTE_2026-09-05.md',
    'scripts/admissibility_dirac_kahler_two_direction_bench_covariant_witness_2026_09_05.py',
    'docs/ADMISSIBILITY_DIRAC_KAHLER_OVERLAP_ASSEMBLY_COVARIANT_CELLS_BOUNDED_THEOREM_NOTE_2026-09-05.md',
    'scripts/admissibility_dirac_kahler_overlap_assembly_covariant_cells_2026_09_05.py',
    'docs/ADMISSIBILITY_DIRAC_KAHLER_COVARIANT_CURVED_CELL_CONE_BOUNDED_THEOREM_NOTE_2026-09-05.md',
    'scripts/admissibility_dirac_kahler_covariant_curved_cell_cone_2026_09_05.py',
    'docs/ADMISSIBILITY_DIRAC_KAHLER_DUALITY_COVARIANCE_LOCUS_BOUNDED_THEOREM_NOTE_2026-09-05.md',
    'scripts/admissibility_dirac_kahler_duality_covariance_locus_2026_09_05.py',
    'docs/ADMISSIBILITY_DIRAC_KAHLER_DUALITY_PARAMETERS_PRINCIPAL_PART_BOUNDED_THEOREM_NOTE_2026-09-05.md',
    'scripts/admissibility_dirac_kahler_duality_parameters_principal_part_2026_09_05.py',
    'docs/ADMISSIBILITY_DIRAC_KAHLER_WEIGHTED_KERNEL_DISPERSION_BOUNDED_THEOREM_NOTE_2026-09-05.md',
    'scripts/admissibility_dirac_kahler_weighted_kernel_dispersion_2026_09_05.py',
    'scripts/admissibility_dirac_kahler_weighted_kernel_released7981_7988_fixtures_2026_09_10.py',
    'docs/ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md',
    'scripts/admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_2026_08_14.py',
    'scripts/admissibility_dirac_kahler_released7992_7994_group_fixture_2026_09_10.py',
    'docs/MINIMAL_AXIOMS_2026-06-29.md',
    'docs/audit/data/axiom_premise_nodes.json',
)
SELF_NOTE_INPUT = AUDIT_INPUT_PATHS[0]
INPUT_SHA256 = {
    SELF_NOTE_INPUT: "880d9378d7cb70fe010acef0a423e4a230d41760291e3e6eaf13c61d5137192d",
    B218_NOTE: "4dfebc34b34daedc6a52d3ab9dfb324428c812c5cf61e2c9babdb4c2565545e5",
    B218_RUNNER: "35229d5cacc72412992d13931e74a47f44faf62791c1399dfc00a592475d9e8c",
    B217_NOTE: "fe14239b8091cae1f0cce71a72c288cb6cbd49d0f1b381099348eb24824e405d",
    B217_RUNNER: "fe4f9300d69891d1bbb5f77db5c65982703f084be9ddaf144ef3a69ac60d62af",
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
AUDIT_TIMEOUT_SEC = 180
CORRECTION_SOURCE_BASE = "09dafe5bf6fb030249b368987fff091ef339c78a"
PARENT_SOURCE_SHA256 = INPUT_SHA256[B218_RUNNER]
CURRENT_MAIN = CORRECTION_SOURCE_BASE
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
    "claim_reading_selected",
    "claim_continuum_read",
    "break_bench_momenta",
    "break_witness_reproduction",
    "break_flat_control",
    "break_second_multiple_positivity",
    "break_bloch_equals_direct",
    "break_witness_multisets",
    "break_control_multisets",
    "break_raising_block_additivity",
    "break_onsite_similarity",
    "break_triply_mixed_identity",
    "break_cone_shape_visible",
    "break_g1_readoff",
    "break_triply_mixed_consistency",
    "break_line_rescaling",
    "break_d07_rescaling",
    "break_control_failure",
    "break_overlap_fold_dependence",
    "break_scout_grade_fence",
    "break_instance_scope",
    "drop_n5_fence",
    "break_float_absence",
)
MUTATION_GATE = {
    "stale_main_authority": "A", "stale_parent_authority": "A",
    "claim_objects_registered": "B", "claim_gravity_supplied": "B",
    "claim_covariance_inherited": "B", "claim_assembly_decided": "B",
    "claim_cell_selected": "B", "claim_reading_selected": "B", "claim_continuum_read": "B",
    "break_bench_momenta": "C", "break_witness_reproduction": "C", "break_flat_control": "C",
    "break_second_multiple_positivity": "C",
    "break_bloch_equals_direct": "D", "break_witness_multisets": "D", "break_control_multisets": "D",
    "break_raising_block_additivity": "E", "break_onsite_similarity": "E", "break_triply_mixed_identity": "E",
    "break_cone_shape_visible": "F", "break_g1_readoff": "F", "break_triply_mixed_consistency": "F",
    "break_line_rescaling": "G", "break_d07_rescaling": "G", "break_control_failure": "G",
    "break_overlap_fold_dependence": "G",
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
# A. source/input closure
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
    "Block 213's curve witnesses L+- and L-+ over QQ(sqrt 6), its bench_matrix and bench_momenta at any extent, and its Bloch reduction",
    "Block 214's principal part M = H0 D + D^T H0 under both assemblies and its first-order raising matrix D(kappa)",
    "Block 216's 8 rule-A covariant witnesses, their four pencil branch constants on the star line and its two rescalings LINE_RESCALE and D07_RESCALE",
    "Block 217's algebraic-field bench and Block 218's (4,4,2) bench with its Bloch-point lemma, onsite similarity and mixed-point identity",
    "Block 105's two assemblies (onsite at even anchors; overlap at every anchor with weight 2^-3)",
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
DISPERSION_LAW_CLAIMED = False
LORENTZIAN_CLAIMED = False
LIGHT_CONE_CLAIMED = False
CONE_IS_SPACETIME_CONE_CLAIMED = False
UNSUPPLIED_GRAVITY_STRUCTURES = (
    "lapse function", "shift vector", "ADM phase space", "Hamiltonian constraint",
    "momentum/diffeomorphism constraint", "first-class constraint algebra",
    "Dirac closure", "Dirac observable", "gauge orbit and its quotient",
)
SCOPED_HEADLINE_WORDS = ("COVARIANCE", "CONE", "CELL", "ASSEMBLY", "BENCH", "SHAPE")
AXIOM_COVARIANCE_CLAUSE = ("There is one fixed nearest-neighbor admissibility rule, covariant under lattice\n"
                           "translations and proper cubic rotations.")
READINGS = (
    "R1 the cell form inherits the Admissibility axiom's proper-cubic-rotation covariance (the antecedent; not established, not asserted)",
    "R2 the bench's seeing the cone's shape under the onsite pencil and under no other construction decides the assembly or the reading (not established: all four are measured, none is selected)",
    "R3 'one metric's cone', 'the cone's shape' or 'G1 read off the bench' is a metric, a cone or a shape of anything physical (not established: Block 213's polynomial statement and one 3 x 3 matrix of rationals)",
    "R4 the bench multisets are a dispersion law, a Lorentzian light cone or a continuum limit (not established: sixty-four exact eigenvalues of one finite matrix at eight Bloch points)",
    "R5 the Bloch-point identity with the principal part is a small-k limit (not established: an exact finite identity resting on d^2 = 0 and the onsite similarity, at fine momenta pi/2)",
    "R6 the covariant witness is a vacuum, a background or a spacetime (not established: a positive-definite point on one cell form)",
)
HISTORICAL_REVIEW_RECORD = "archived original checker record; superseded by the 2026-09-10 correction"

# the parameters, the moduli, the directions, the cells, the witnesses
PARAMETER_NAMES = ("D07", "D16", "D25", "D34")
PARAMETER_SYMBOLS = b217.PARAMETER_SYMBOLS
G0, G1, V0, V1 = b217.MODULI
MODULI = (G0, G1, V0, V1)
KT, KX, KY = b217.KAPPA
KAPPA = (KT, KX, KY)
LAM = b213.LAM
FACE_ORDER = b211.GAUGE_FACE_ORDER        # (tx0, ty0, xy0, tx1, ty1, xy1)
R = sp.Rational
QUARTER = R(1, 4)
HALF = R(1, 2)
BENCH_EXTENT = (4, 4, 4)                  # the three-direction bench: 64 sites, eight Bloch points
PARENT_EXTENT = (4, 4, 2)                 # Block 218's two-direction bench
GRANDPARENT_EXTENT = (4, 2, 2)            # Block 217's one-direction bench
LINE_POINT = b217.LINE_POINT              # (D07, D16, D25, D34) = (0, 1/4, -1/4, 1/4) on the star line
HALF_LINE_POINT = (sp.Integer(0), HALF, -HALF, HALF)        # the second line multiple, lambda = 1/2
D07_LINE_POINT = (QUARTER, QUARTER, -QUARTER, QUARTER)      # D07 = 1/4 on the line at lambda = 1/4
ZERO_POINT = (sp.Integer(0),) * 4
ALL_PLUS_CELL = b216.ALL_PLUS_CELL
W1_MODULI = b216.W1_MODULI                # (v0, g0, v1, g1) = (15/16, 1/4, 1, 1/4)
FLAT_MODULI = b216.FLAT_MODULI
REAL_FIELD = b218.REAL_FIELD              # QQ(sqrt 6)
COMPLEX_FIELD = b218.COMPLEX_FIELD        # QQ(sqrt 6, i)
UNIT_KAPPAS = b218.UNIT_KAPPAS
Z_SYMBOLS = b218.Z_SYMBOLS                # (z_t, z_x, z_y), all three live
LAM_LINE = sp.Symbol("lam_line")          # Block 216's symbolic line multiple

# the helpers of the parent, read-only
kappa_of = b218.kappa_of
momentum_literal = b218.momentum_literal
raising_operator = b218.raising_operator
phase_matrix = b218.phase_matrix
is_zero_matrix = b218.is_zero_matrix
residual_count = b218.residual_count
rational_roots = b218.rational_roots
normalized_monic_charpoly = b218.normalized_monic_charpoly
principal_square = b218.principal_square
principal_charpoly = b218.principal_charpoly
branch_constants = b218.branch_constants
generic_cell = b218.generic_cell
parity_block_literals = b218.parity_block_literals
raising_rules = b218.raising_rules

# ---------------------------------------------------------------------------
# exact helpers -- no float, no tolerance and NO nsimplify anywhere
# ---------------------------------------------------------------------------
NSIMPLIFY_TOKEN = "sp." + "nsimplify("


def nsimplify_occurrences() -> int:
    return Path(__file__).read_text(encoding="utf-8").count(NSIMPLIFY_TOKEN)


def float_literal_occurrences() -> int:
    tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    return sum(1 for node in ast.walk(tree)
               if isinstance(node, ast.Constant) and isinstance(node.value, float))


def float_call_sites() -> int:
    tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    return sum(1 for node in ast.walk(tree)
               if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == "float")


def bench_cells(census: dict) -> dict:
    """Block 218's bench cells (Block 217's five plus the flat cell at zero
    parameters) plus L+-'s cell at the second line multiple lambda = 1/2 and
    at D07 = 1/4 on the line -- Block 216's two rescalings, on the bench."""
    cells = dict(b218.bench_cells(census))
    witness = next(v for v in b217.rule_a_cells(census) if census["cells"][v]["mask"] == 2)
    cells["witness half"] = b217.formal(witness, b217.moduli_as_g(b217.curve_moduli(1)), HALF_LINE_POINT)
    cells["witness d07"] = b217.formal(witness, b217.moduli_as_g(b217.curve_moduli(1)), D07_LINE_POINT)
    return cells


def quadric_values(g1: sp.Matrix, points: tuple) -> dict:
    return {z: sp.radsimp(b213.quadratic_form(g1, kappa_of(tuple(sp.sympify(e) for e in z)))) for z in points}


# ---------------------------------------------------------------------------
# C/D. THE BENCH at extent (4,4,4) over QQ(sqrt 6) and QQ(sqrt 6, i): the
# eight 8 x 8 Bloch blocks always; the direct 64 x 64 charpoly where declared
# (the onsite pencil at every cell, the flat cell under every construction)
# ---------------------------------------------------------------------------
# (cell label, assembly, reading, direct 64 x 64 check?)
BENCH_PLAN = (
    ("witness line", "onsite", "pencil", True),
    ("witness line", "onsite", "form", True),
    ("witness line", "overlap", "form", False),
    ("witness line", "overlap", "pencil", False),
    ("witness half", "onsite", "pencil", True),
    ("witness d07", "onsite", "pencil", True),
    ("W1 line", "onsite", "pencil", True),
    ("flat line", "onsite", "pencil", False),
    ("witness zero", "overlap", "form", False),
    ("witness zero", "overlap", "pencil", False),
    ("flat zero", "onsite", "form", True),
    ("flat zero", "onsite", "pencil", True),
    ("flat zero", "overlap", "form", True),
    ("flat zero", "overlap", "pencil", True),
)


def bloch_blocks(cell: sp.Matrix, assembly: str, reading: str, extent: tuple) -> dict:
    """The 8 x 8 Bloch block charpoly per momentum over QQ(sqrt 6, i)."""
    rules = (b213.onsite_rules if assembly == "onsite" else b213.overlap_rules)(cell, b209.CORNERS, 3)
    raising = raising_rules()
    transposed = b213.transpose_rules(raising)
    blocks: dict = {}
    for z in b213.bench_momenta(extent):
        h_b = DomainMatrix.from_Matrix(b213.bloch_matrix(rules, z, 3)).convert_to(COMPLEX_FIELD)
        d_b = DomainMatrix.from_Matrix(b213.bloch_matrix(raising, z, 3)).convert_to(COMPLEX_FIELD)
        dt_b = DomainMatrix.from_Matrix(b213.bloch_matrix(transposed, z, 3)).convert_to(COMPLEX_FIELD)
        blocks[momentum_literal(z)] = b217.alg_charpoly(b217.symbol_matrix(h_b, d_b, dt_b, reading), COMPLEX_FIELD)
    return blocks


def direct_charpoly(cell: sp.Matrix, assembly: str, reading: str, extent: tuple):
    """The direct bench charpoly over QQ(sqrt 6) of the periodic bench matrix."""
    rules = (b213.onsite_rules if assembly == "onsite" else b213.overlap_rules)(cell, b209.CORNERS, 3)
    raising = raising_rules()
    hodge = DomainMatrix.from_Matrix(b213.bench_matrix(rules, extent)).convert_to(REAL_FIELD)
    lifted = DomainMatrix.from_Matrix(b213.bench_matrix(raising, extent)).convert_to(REAL_FIELD)
    return b217.alg_charpoly(b217.symbol_matrix(hodge, lifted, lifted.transpose(), reading), REAL_FIELD)


def measure_bench(cells: dict) -> dict:
    """D: every planned (cell, assembly, reading) on (4,4,4): the eight Bloch
    block charpolys, their multisets and factor shapes, and -- where planned --
    the direct degree-64 charpoly with Bloch union = direct."""
    facts: dict = {}
    table: dict = {}
    for label, assembly, reading, direct_planned in BENCH_PLAN:
        print(f"[bench] {label} {assembly} {reading}", file=sys.stderr)
        started = time.monotonic_ns()
        blocks = bloch_blocks(cells[label], assembly, reading, BENCH_EXTENT)
        union = sp.expand(sp.prod(list(blocks.values())))
        union_ms = (time.monotonic_ns() - started) // 1_000_000
        entry = {
            "direct_planned": direct_planned, "agree": None, "multiset": None, "degree": None, "direct_ms": None,
            "block_multisets": {z: b213.multiset_of(cp) for z, cp in blocks.items()},
            "block_shapes": {z: b217.charpoly_shape(cp) for z, cp in blocks.items()},
            "block_rational_roots": {z: rational_roots(cp) for z, cp in blocks.items()},
            "union_ms": union_ms, "blocks": blocks, "union_degree": sp.Poly(union, LAM).degree(),
        }
        if direct_planned:
            started = time.monotonic_ns()
            direct = direct_charpoly(cells[label], assembly, reading, BENCH_EXTENT)
            entry["direct_ms"] = (time.monotonic_ns() - started) // 1_000_000
            entry["agree"] = sp.expand(direct - union) == 0
            entry["multiset"] = b213.multiset_of(direct)
            entry["degree"] = sp.Poly(direct, LAM).degree()
        table[(label, assembly, reading)] = entry
    facts["table"] = table
    facts["charpoly_count"] = len(table)
    facts["direct_count"] = sum(1 for e in table.values() if e["direct_planned"])
    facts["all_direct_agree"] = all(e["agree"] for e in table.values() if e["direct_planned"])
    facts["all_direct_degree_64"] = all(e["degree"] == 64 for e in table.values() if e["direct_planned"])
    facts["all_union_degree_64"] = all(e["union_degree"] == 64 for e in table.values())
    facts["zero_point_is_eight_zeros"] = all(e["block_multisets"][("1", "1", "1")] == ((0, 8),) for e in table.values())
    facts["block_multisets"] = {key: e["block_multisets"] for key, e in table.items()}
    facts["block_shapes"] = {key: e["block_shapes"] for key, e in table.items()}
    facts["multisets"] = {key: e["multiset"] for key, e in table.items() if e["direct_planned"]}
    expected = b213.expected_flat_multiset(BENCH_EXTENT)
    facts["flat_expected"] = expected
    facts["flat_zero_is_r5"] = all(table[("flat zero", a, r)]["multiset"] == expected
                                   for a in ("onsite", "overlap") for r in ("form", "pencil"))
    facts["timings_ms"] = {key: (e["direct_ms"], e["union_ms"]) for key, e in table.items()}
    facts["max_direct_ms"] = max(e["direct_ms"] for e in table.values() if e["direct_planned"])
    return facts


# ---------------------------------------------------------------------------
# C. CONSTRUCTION FIDELITY: the bench is Block 213's at extent (4,4,4) with its
# eight momenta, the witness and the control are Blocks 216-218's, Block 218's
# (4,4,2) and Block 217's (4,2,2) identities reproduce, the second line
# multiple is positive definite by leading minors BEFORE it is used
# ---------------------------------------------------------------------------
def measure_construction(census: dict, cells: dict) -> dict:
    facts: dict = {}
    momenta = b213.bench_momenta(BENCH_EXTENT)
    facts["momenta"] = tuple(momentum_literal(z) for z in momenta)
    facts["kappas"] = tuple(kappa_of(z) for z in momenta)
    facts["triply_mixed_point_present"] = ("I", "I", "I") in facts["momenta"]
    facts["site_count"] = len(b213.bench_sites(BENCH_EXTENT))
    lifted = b213.bench_matrix(raising_rules(), BENCH_EXTENT)
    sites = b213.bench_sites(BENCH_EXTENT)
    facts["y_link_entries"] = sum(
        1 for a in sites for b in sites
        if a[:2] == b[:2] and a != b and lifted[b213.site_index(a, BENCH_EXTENT), b213.site_index(b, BENCH_EXTENT)] != 0)
    facts["raising_bench_nnz"] = residual_count(lifted)
    facts["parent_momenta"] = tuple(momentum_literal(z) for z in b213.bench_momenta(PARENT_EXTENT))
    facts["grandparent_momenta"] = tuple(momentum_literal(z) for z in b213.bench_momenta(GRANDPARENT_EXTENT))
    witness_values = tuple(v for v in census["cells"] if census["cells"][v]["mask"] == 2)
    facts["witness_values"] = witness_values
    facts["witness_is_rule_a"] = all(census["cells"][v]["rule_a"] for v in witness_values)
    facts["l_plus_minus_signs"] = tuple(b213.locus_witness_table()["L+-"][1][f] for f in b213.FACES)
    facts["face_orders_agree"] = tuple(FACE_ORDER) == tuple(b213.FACES)
    pairs = ((0, 7), (1, 6), (2, 5), (3, 4))
    facts["line_point_entries"] = tuple(cells["witness line"][i, j] for i, j in pairs)
    facts["half_point_entries"] = tuple(cells["witness half"][i, j] for i, j in pairs)
    facts["d07_point_entries"] = tuple(cells["witness d07"][i, j] for i, j in pairs)
    facts["witness_moduli"] = b217.curve_moduli(1)
    facts["w1_moduli_is_block211"] = tuple(W1_MODULI) == tuple(b211.W1_MODULI)
    # the two smaller extents as consistency gates: Block 218's (4,4,2), Block 217's (4,2,2)
    started = time.monotonic_ns()
    direct, union, blocks, _, _ = b218.bench_charpolys(cells["witness line"], "onsite", "pencil")
    facts["parent_bench_agrees"] = sp.expand(direct - union) == 0
    facts["parent_block_multisets"] = {z: b213.multiset_of(cp) for z, cp in blocks.items()}
    facts["parent_bench_ms"] = (time.monotonic_ns() - started) // 1_000_000
    started = time.monotonic_ns()
    direct, union, _, _ = b217.bench_charpolys(cells["witness line"], "onsite", "pencil")
    facts["grandparent_bench_multiset"] = b213.multiset_of(direct)
    facts["grandparent_bench_agrees"] = sp.expand(direct - union) == 0
    facts["grandparent_bench_ms"] = (time.monotonic_ns() - started) // 1_000_000
    g1 = b213.metric_candidates(cells["witness zero"])[0].applyfunc(sp.radsimp)
    facts["g1_tt_witness"] = g1[0, 0]
    # positivity of the second line multiple and of the D07 point, by leading minors, before use
    for label in ("witness half", "witness d07", "witness line"):
        minors = tuple(sp.radsimp(m) for m in b211.leading_minors(cells[label]))
        facts[f"leading_minors {label}"] = minors
        facts[f"positive_definite {label}"] = all(m.is_positive for m in minors)
    facts["half_multiple_below_volume_product"] = bool(HALF ** 2 < b216.VOLUME_PRODUCTS["L+-"])
    facts["volume_product"] = b216.VOLUME_PRODUCTS["L+-"]
    return facts


# ---------------------------------------------------------------------------
# E. THE BLOCH-POINT LEMMA IN THREE DIRECTIONS: the raising block is
# i D(kappa_z) at all eight points (measured first, at symbolic z with z_y
# live), the onsite Hodge block is Z^-1 H0 Z, d^2 = 0 for every kappa_z, and
# hence the onsite pencil block charpoly is the principal part's at every
# point -- the triply-mixed point included
# ---------------------------------------------------------------------------
IDENTITY_CELLS = ("witness line", "W1 line", "flat line", "witness half", "witness d07")


def measure_identities(cells: dict, bench: dict) -> dict:
    facts: dict = {}
    raising = raising_rules()
    momenta = b213.bench_momenta(BENCH_EXTENT)
    facts["raising_block_is_i_d"] = {
        momentum_literal(z): is_zero_matrix(b213.bloch_matrix(raising, z, 3) - sp.I * raising_operator(kappa_of(z)))
        for z in momenta}
    symbolic = b213.bloch_matrix(raising, Z_SYMBOLS, 3)
    predicted = sum((((zz - 1 / zz) / 2) * raising_operator(UNIT_KAPPAS[mu]) for mu, zz in enumerate(Z_SYMBOLS)),
                    sp.zeros(8, 8))
    facts["raising_block_additive_symbolic"] = residual_count((symbolic - predicted).applyfunc(sp.simplify)) == 0
    facts["z_y_live_in_symbolic_block"] = Z_SYMBOLS[2] in symbolic.free_symbols
    units = tuple(raising_operator(k) for k in UNIT_KAPPAS)
    facts["d_mu_squared_zero"] = all(is_zero_matrix(d * d) for d in units)
    facts["d_mu_anticommute"] = all(is_zero_matrix(units[a] * units[b] + units[b] * units[a])
                                    for a in range(3) for b in range(a + 1, 3))
    facts["d_kappa_squared_zero"] = {
        momentum_literal(z): is_zero_matrix(raising_operator(kappa_of(z)) * raising_operator(kappa_of(z))) for z in momenta}
    facts["onsite_similarity"] = {}
    for label in IDENTITY_CELLS:
        rules = b213.onsite_rules(cells[label], b209.CORNERS, 3)
        h0 = b213.folded_matrix(rules, 3)
        facts["onsite_similarity"][label] = all(
            is_zero_matrix(b213.bloch_matrix(rules, z, 3) - phase_matrix(z).inv() * h0 * phase_matrix(z)) for z in momenta)
    facts["onsite_similarity_everywhere"] = all(facts["onsite_similarity"].values())
    table: dict = {}
    for (label, assembly, reading), entry in bench["table"].items():
        if not label.endswith("line") and label not in ("witness half", "witness d07"):
            continue
        square = principal_square(cells[label], assembly, reading)
        table[(label, assembly, reading)] = {
            momentum_literal(z): sp.expand(entry["blocks"][momentum_literal(z)] - principal_charpoly(square, kappa_of(z))) == 0
            for z in momenta}
    facts["identity_table"] = table
    nonzero = tuple(momentum_literal(z) for z in momenta if kappa_of(z) != (0, 0, 0))
    facts["nonzero_points"] = nonzero
    facts["onsite_pencil_identity_everywhere"] = all(all(table[(label, "onsite", "pencil")].values()) for label in IDENTITY_CELLS)
    facts["triply_mixed_identity"] = {label: table[(label, "onsite", "pencil")][("I", "I", "I")] for label in IDENTITY_CELLS}
    facts["form_fails_at_every_nonzero_point"] = not any(table[("witness line", "onsite", "form")][z] for z in nonzero)
    facts["overlap_fails_at_every_nonzero_point"] = not any(
        table[("witness line", "overlap", reading)][z] for reading in ("form", "pencil") for z in nonzero)
    return facts


# ---------------------------------------------------------------------------
# F. THE SHAPE IN THREE DIRECTIONS and G1 READ OFF THE BENCH: at every one of
# the seven nonzero points every nonzero eigenvalue is a branch constant times
# Q(kappa_z); the six entries of G1 from the pure and doubly-mixed points; the
# triply-mixed point as the over-determined consistency check
# ---------------------------------------------------------------------------
PURE_T, PURE_X, PURE_Y = ("I", "1", "1"), ("1", "I", "1"), ("1", "1", "I")
MIXED_TX, MIXED_TY, MIXED_XY = ("I", "I", "1"), ("I", "1", "I"), ("1", "I", "I")
TRIPLY = ("I", "I", "I")
PURE_POINTS = (PURE_T, PURE_X, PURE_Y)
DOUBLY_MIXED_POINTS = (MIXED_TX, MIXED_TY, MIXED_XY)
NONZERO_POINTS = PURE_POINTS + DOUBLY_MIXED_POINTS + (TRIPLY,)
PAIR_OF = {MIXED_TX: (PURE_T, PURE_X), MIXED_TY: (PURE_T, PURE_Y), MIXED_XY: (PURE_X, PURE_Y)}
ENTRY_INDEX = {"tt": (0, 0), "xx": (1, 1), "yy": (2, 2), "tx": (0, 1), "ty": (0, 2), "xy": (1, 2)}


def smallest_nonzero(multisets: dict, points: tuple) -> dict:
    """The constant-1 branch at each point, read from the bench alone."""
    return {z: min(root for root, _ in multisets[z] if root != 0) for z in points}


def g1_from_bench(multisets: dict) -> dict:
    """The six entries of G1 from seven Bloch points: the diagonal from the pure
    points, the off-diagonal from (Q(e_mu + e_nu) - Q(e_mu) - Q(e_nu))/2."""
    small = smallest_nonzero(multisets, NONZERO_POINTS)
    return {"tt": small[PURE_T], "xx": small[PURE_X], "yy": small[PURE_Y],
            "tx": sp.radsimp((small[MIXED_TX] - small[PURE_T] - small[PURE_X]) / 2),
            "ty": sp.radsimp((small[MIXED_TY] - small[PURE_T] - small[PURE_Y]) / 2),
            "xy": sp.radsimp((small[MIXED_XY] - small[PURE_X] - small[PURE_Y]) / 2)}


def ratio_multisets(multisets: dict, quadrics: dict, points: tuple) -> dict:
    return {z: None if multisets[z] is None else tuple(sorted(
        ((sp.radsimp(root / quadrics[z]), mult) for root, mult in multisets[z] if root != 0), key=lambda t: t[0]))
        for z in points}


def measure_shape(cells: dict, bench: dict) -> dict:
    facts: dict = {}
    g1 = b213.metric_candidates(cells["witness zero"])[0].applyfunc(sp.radsimp)
    facts["g1_full"] = tuple(tuple(g1[i, j] for j in range(3)) for i in range(3))
    facts["g1_parameter_free"] = all(
        b213.metric_candidates(cells[label])[0].applyfunc(sp.radsimp) == g1 for label in ("witness line", "witness half", "witness d07"))
    facts["constants"] = branch_constants()
    facts["quadric_values"] = quadric_values(g1, NONZERO_POINTS)
    multisets = bench["block_multisets"][("witness line", "onsite", "pencil")]
    facts["multisets"] = {z: multisets[z] for z in NONZERO_POINTS}
    facts["ratios"] = ratio_multisets(multisets, facts["quadric_values"], NONZERO_POINTS)
    facts["shape_visible"] = all(facts["ratios"][z] == facts["constants"] for z in NONZERO_POINTS)
    facts["predicted_multisets"] = {z: tuple(sorted(((sp.radsimp(c * facts["quadric_values"][z]), m)
                                                     for c, m in facts["constants"]), key=lambda t: t[0])) for z in NONZERO_POINTS}
    facts["predicted_equal_measured"] = all(facts["predicted_multisets"][z] == multisets[z] for z in NONZERO_POINTS)
    facts["g1_bench"] = g1_from_bench(multisets)
    facts["g1_bench_equals_g1"] = all(facts["g1_bench"][k] == g1[i, j] for k, (i, j) in ENTRY_INDEX.items())
    gb = facts["g1_bench"]
    facts["triply_predicted"] = sp.radsimp(gb["tt"] + gb["xx"] + gb["yy"] + 2 * (gb["tx"] + gb["ty"] + gb["xy"]))
    facts["triply_measured"] = smallest_nonzero(multisets, (TRIPLY,))[TRIPLY]
    facts["triply_consistent"] = facts["triply_predicted"] == facts["triply_measured"]
    facts["pure_points_coincide"] = len({multisets[z] for z in PURE_POINTS}) == 1
    facts["doubly_mixed_points_coincide"] = len({multisets[z] for z in DOUBLY_MIXED_POINTS}) == 1
    facts["triply_equals_pure"] = multisets[TRIPLY] == multisets[PURE_T]
    h0, m, _ = b214.principal_part(cells["witness line"], "onsite")
    det = sp.radsimp(m.det(method="berkowitz"))
    constant, factors = sp.factor_list(det, *KAPPA, extension=sp.sqrt(6))
    facts["det_m_shape"] = tuple(sorted((sp.Poly(f, *KAPPA).total_degree(), p) for f, p in factors))
    facts["det_m_values"] = {z: det.subs(dict(zip(KAPPA, kappa_of(tuple(sp.sympify(e) for e in z))))) for z in NONZERO_POINTS}
    facts["det_m_is_quadric_fourth"] = all(
        sp.radsimp(facts["det_m_values"][z] - R(64, 81) * facts["quadric_values"][z] ** 4) == 0 for z in NONZERO_POINTS)
    return facts


# ---------------------------------------------------------------------------
# G (part 1). BLOCK 216's TWO RESCALINGS SEEN ON THE BENCH: at the second line
# multiple lambda = 1/2 and at D07 = 1/4 on the line, the block multisets
# against Block 216's rescaled constants times Q(kappa_z)
# ---------------------------------------------------------------------------
def symbolic_line_constants(value) -> tuple:
    """Block 216's BRANCH_TABLE[("L+-", "line symbolic")] evaluated exactly at lam_line = value."""
    table = b216.BRANCH_TABLE[("L+-", "line symbolic")][0]
    return tuple(sorted(((sp.sympify(expr).subs(LAM_LINE, value), power) for expr, power, _ in table), key=lambda t: t[0]))


def rescaled_constants(rescale) -> tuple:
    """{1 x2, (32/27) r x2, (4/3) r x4}: the top-form and transverse constants rescaled by r."""
    return tuple(sorted(((sp.Integer(1), 2), (R(32, 27) * rescale, 2), (R(4, 3) * rescale, 4)), key=lambda t: t[0]))


def measure_rescalings(cells: dict, bench: dict) -> dict:
    facts: dict = {}
    v0v1 = b216.VOLUME_PRODUCTS["L+-"]
    v1v0 = b216.VOLUME_RATIOS["L+-"]
    facts["line_rescale_quarter"] = 1 / (1 - QUARTER ** 2 / v0v1)
    facts["line_rescale_half"] = 1 / (1 - HALF ** 2 / v0v1)
    facts["line_rescale_quarter_is_block216"] = facts["line_rescale_quarter"] == b216.LINE_RESCALE["L+-"]
    facts["d07_rescale_quarter"] = 1 / (1 - QUARTER ** 2 * v1v0)
    facts["d07_rescale_quarter_is_block216"] = facts["d07_rescale_quarter"] == b216.D07_RESCALE["L+-"]
    facts["constants_quarter_symbolic"] = symbolic_line_constants(QUARTER)
    facts["constants_half_symbolic"] = symbolic_line_constants(HALF)
    facts["constants_quarter_is_table"] = facts["constants_quarter_symbolic"] == branch_constants()
    facts["constants_half_is_rescaled"] = facts["constants_half_symbolic"] == rescaled_constants(facts["line_rescale_half"])
    facts["constants_quarter_is_rescaled"] = facts["constants_quarter_symbolic"] == rescaled_constants(facts["line_rescale_quarter"])
    facts["constants_d07_table"] = tuple((sp.Rational(ratio), power) for ratio, power, _ in b216.BRANCH_TABLE[("L+-", "line 1/4 + D07 1/4")][0])
    facts["constants_d07_is_rescaled"] = facts["constants_d07_table"] == tuple(sorted(
        ((facts["d07_rescale_quarter"], 2), (R(128, 99), 2), (R(16, 11), 4)), key=lambda t: t[0]))
    g1 = b213.metric_candidates(cells["witness zero"])[0].applyfunc(sp.radsimp)
    quadrics = quadric_values(g1, NONZERO_POINTS)
    for label, constants in (("witness half", facts["constants_half_symbolic"]), ("witness d07", facts["constants_d07_table"])):
        multisets = bench["block_multisets"][(label, "onsite", "pencil")]
        facts[f"multisets {label}"] = {z: multisets[z] for z in NONZERO_POINTS}
        ratios = ratio_multisets(multisets, quadrics, NONZERO_POINTS)
        facts[f"ratios {label}"] = ratios
        facts[f"shape_visible {label}"] = all(ratios[z] == constants for z in NONZERO_POINTS)
        facts[f"pure_t_multiset {label}"] = multisets[PURE_T]
        facts[f"pure_t_predicted {label}"] = tuple(sorted(((sp.radsimp(c * quadrics[PURE_T]), m) for c, m in constants), key=lambda t: t[0]))
        facts[f"direct_agrees {label}"] = bench["table"][(label, "onsite", "pencil")]["agree"]
        facts[f"g1_bench {label}"] = g1_from_bench(multisets)
        facts[f"g1_bench_equals_g1 {label}"] = all(facts[f"g1_bench {label}"][k] == g1[i, j] for k, (i, j) in ENTRY_INDEX.items())
        facts[f"g1_bench_ratio {label}"] = frozenset(sp.radsimp(facts[f"g1_bench {label}"][k] / g1[i, j]) for k, (i, j) in ENTRY_INDEX.items())
    return facts


# ---------------------------------------------------------------------------
# G (part 2). THE CONTROL AND THE OVERLAP FOLD: the all-plus W1 at the eight
# points (the triply-mixed point in particular); the overlap Bloch fold's
# parameter dependence at the new points at symbolic signs, moduli and
# parameters; the overlap bench at the line point against zero parameters
# ---------------------------------------------------------------------------
def measure_control_overlap(cells: dict, bench: dict) -> dict:
    facts: dict = {}
    g1 = b213.metric_candidates(cells["W1 zero"])[0].applyfunc(sp.radsimp)
    facts["w1_g1_full"] = tuple(tuple(g1[i, j] for j in range(3)) for i in range(3))
    facts["w1_quadric_values"] = quadric_values(g1, NONZERO_POINTS)
    entry = bench["table"][("W1 line", "onsite", "pencil")]
    facts["w1_shapes"] = {z: entry["block_shapes"][z] for z in NONZERO_POINTS}
    facts["w1_rational_roots"] = {z: entry["block_rational_roots"][z] for z in NONZERO_POINTS}
    facts["w1_multisets_none"] = all(entry["block_multisets"][z] is None for z in NONZERO_POINTS)
    facts["w1_rational_branch_is_quadric"] = all((facts["w1_quadric_values"][z], 2) in facts["w1_rational_roots"][z] for z in NONZERO_POINTS)
    facts["w1_irreducible_degrees"] = {z: tuple(sorted(d for d, _, _ in entry["block_shapes"][z] if d > 1)) for z in NONZERO_POINTS}
    facts["w1_normalized_charpolys"] = {
        z: normalized_monic_charpoly(entry["blocks"][z], facts["w1_quadric_values"][z])
        for z in NONZERO_POINTS
    }
    facts["w1_normalized_t_x_differ"] = (
        sp.expand(facts["w1_normalized_charpolys"][PURE_T]
                  - facts["w1_normalized_charpolys"][PURE_X]) != 0
    )
    facts["w1_triply_shape"] = entry["block_shapes"][TRIPLY]
    facts["w1_triply_rational_roots"] = entry["block_rational_roots"][TRIPLY]
    facts["w1_direct_agrees"] = entry["agree"]
    small = facts["w1_quadric_values"]
    facts["w1_g1_bench"] = {"tt": small[PURE_T], "xx": small[PURE_X], "yy": small[PURE_Y],
                            "tx": (small[MIXED_TX] - small[PURE_T] - small[PURE_X]) / 2,
                            "ty": (small[MIXED_TY] - small[PURE_T] - small[PURE_Y]) / 2,
                            "xy": (small[MIXED_XY] - small[PURE_X] - small[PURE_Y]) / 2}
    facts["w1_g1_bench_equals_g1"] = all(facts["w1_g1_bench"][k] == g1[i, j] for k, (i, j) in ENTRY_INDEX.items())
    facts["w1_triply_extra_ratio"] = sp.radsimp(
        facts["w1_triply_rational_roots"][0][0] / small[TRIPLY])
    facts["w1_triply_shape_divisor"] = b217.primitive_shape_divisor(
        facts["w1_triply_shape"])
    h0, m, _ = b214.principal_part(cells["W1 line"], "onsite")
    det = sp.radsimp(m.det(method="berkowitz"))
    _, factors = sp.factor_list(det, *KAPPA, extension=sp.sqrt(6))
    facts["w1_det_m_shape"] = tuple(sorted((sp.Poly(f, *KAPPA).total_degree(), p) for f, p in factors))
    facts["w1_det_m_values"] = {z: det.subs(dict(zip(KAPPA, kappa_of(tuple(sp.sympify(e) for e in z))))) for z in NONZERO_POINTS}
    # the overlap Bloch fold at symbolic face signs, moduli and parameters, at every point
    rules = b213.overlap_rules(generic_cell(PARAMETER_SYMBOLS), b209.CORNERS, 3)
    fold: dict = {}
    for z in b213.bench_momenta(BENCH_EXTENT):
        matrix = b213.bloch_matrix(rules, z, 3)
        fold[momentum_literal(z)] = {
            "parameters_present": tuple(str(p) for p in PARAMETER_SYMBOLS if p in matrix.free_symbols),
            "parity_block": parity_block_literals(matrix),
        }
    facts["overlap_fold"] = fold
    facts["overlap_fold_parameter_free_points"] = tuple(z for z in fold if fold[z]["parameters_present"] == ())
    facts["overlap_fold_parity_blocks"] = {z: fold[z]["parity_block"] for z in fold if fold[z]["parity_block"] != ()}
    facts["overlap_fold_star_line_values"] = {
        z: tuple(sp.sympify(e).subs(dict(zip(PARAMETER_SYMBOLS, LINE_POINT))) for e in fold[z]["parity_block"])
        for z in DOUBLY_MIXED_POINTS}
    comparison: dict = {}
    for reading in ("form", "pencil"):
        line = bench["table"][("witness line", "overlap", reading)]["blocks"]
        zero = bench["table"][("witness zero", "overlap", reading)]["blocks"]
        comparison[reading] = {z: sp.expand(line[z] - zero[z]) == 0 for z in line}
    facts["overlap_line_vs_zero"] = comparison
    facts["overlap_line_equals_zero_points"] = tuple(z for z in comparison["form"] if comparison["form"][z] and comparison["pencil"][z])
    facts["overlap_line_differs_points"] = tuple(z for z in comparison["form"] if not comparison["form"][z] and not comparison["pencil"][z])
    ms = bench["block_multisets"]
    facts["overlap_witness_pure_multisets"] = {(r, z): ms[("witness line", "overlap", r)][z] for r in ("form", "pencil") for z in PURE_POINTS}
    facts["overlap_t_equals_y_not_x"] = all(
        ms[("witness line", "overlap", r)][PURE_T] == ms[("witness line", "overlap", r)][PURE_Y] != ms[("witness line", "overlap", r)][PURE_X]
        for r in ("form", "pencil"))
    facts["overlap_triply_pencil"] = ms[("witness line", "overlap", "pencil")][TRIPLY]
    facts["overlap_ty_pencil"] = ms[("witness line", "overlap", "pencil")][MIXED_TY]
    facts["onsite_pure_points_coincide"] = len({ms[("witness line", "onsite", "pencil")][z] for z in PURE_POINTS}) == 1
    return facts


@dataclass(frozen=True)
class Facts:
    authority: AuthorityCertificate
    construction: dict
    bench: dict
    identities: dict
    shape: dict
    rescalings: dict
    control: dict
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
    census = b216.measure_census()
    cells = bench_cells(census)
    lap("census")
    construction = measure_construction(census, cells)
    lap("construction")
    bench = measure_bench(cells)
    lap("bench")
    identities = measure_identities(cells, bench)
    lap("identities")
    shape = measure_shape(cells, bench)
    lap("shape")
    rescalings = measure_rescalings(cells, bench)
    lap("rescalings")
    control = measure_control_overlap(cells, bench)
    lap("control")
    axiom_text = (ROOT / AXIOM_PATH).read_text(encoding="utf-8") if (ROOT / AXIOM_PATH).is_file() else ""
    note_text = NOTE_PATH.read_text(encoding="utf-8") if NOTE_PATH.is_file() else ""
    return Facts(authority, construction, bench, identities, shape, rescalings, control, axiom_text, note_text, timings)


# ---------------------------------------------------------------------------
# THE DECLARED LITERALS -- every claim is a constant compared against a
# measurement; a mutation rewrites exactly one claim.
# ---------------------------------------------------------------------------
BENCH_MOMENTA = (("1", "1", "1"), ("1", "1", "I"), ("1", "I", "1"), ("1", "I", "I"),
                 ("I", "1", "1"), ("I", "1", "I"), ("I", "I", "1"), ("I", "I", "I"))   # Block 213's bench_momenta((4,4,4))
BENCH_KAPPAS = ((0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1), (1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1))
SITE_COUNT = 64
Y_LINK_ENTRIES = 64                                                                   # the y direction now carries its link
RAISING_BENCH_NNZ = 192
WITNESS_SIGNS = (1, 1, 1, 1, -1, 1)                                                   # Block 213's L+- cell = Block 216's mask 2
LINE_POINT_ENTRIES = (sp.Integer(0), R(1, 4), R(-1, 4), R(1, 4))
HALF_POINT_ENTRIES = (sp.Integer(0), R(1, 2), R(-1, 2), R(1, 2))
D07_POINT_ENTRIES = (R(1, 4), R(1, 4), R(-1, 4), R(1, 4))
G1_TT_WITNESS = R(9, 8)
FLAT_R5 = ((0, 8), (1, 24), (2, 24), (3, 8))                                          # Block 213's expected_flat_multiset((4,4,4))
SQRT6 = sp.sqrt(6)
HALF_LEADING_MINORS = (SQRT6 / 3, R(3, 4), SQRT6 / 4, R(3, 4), SQRT6 / 8, R(3, 16), SQRT6 / 24, R(1, 9))
VOLUME_PRODUCT = R(3, 4)                                                              # v0 v1 at L+-, Block 216's VOLUME_PRODUCTS
CHARPOLY_COUNT = 14
DIRECT_COUNT = 9
WITNESS_PURE_PENCIL = ((R(9, 8), 2), (R(16, 11), 2), (R(18, 11), 4))                  # Block 218's, now at three pure points AND the triply-mixed point
WITNESS_MIXED_PENCIL = ((R(3, 2), 2), (R(64, 33), 2), (R(24, 11), 4))                 # Block 218's, now at three doubly-mixed points
WITNESS_DIRECT_PENCIL = ((0, 8), (R(9, 8), 8), (R(16, 11), 8), (R(3, 2), 6), (R(18, 11), 16), (R(64, 33), 6), (R(24, 11), 12))
W1_TRIPLY_SHAPE = ((1, 2, (5, -8)), (1, 2, (165, -256)), (2, 2, (4157, -26952, 43008)))
W1_TRIPLY_RATIONAL_ROOTS = ((R(256, 165), 2), (R(8, 5), 2))
W1_TRIPLY_EXTRA_RATIO = R(32, 33)
W1_TRIPLY_MONIC_DIVISOR = sp.Integer(5 * 165 * 4157) ** 2
W1_IRREDUCIBLE_DEGREES = {PURE_T: (3,), PURE_X: (2,), PURE_Y: (3,), MIXED_TX: (3,), MIXED_TY: (2,), MIXED_XY: (3,), TRIPLY: (2,)}
W1_QUADRIC_VALUES = {PURE_T: R(16, 15), PURE_X: R(16, 15), PURE_Y: R(16, 15),
                     MIXED_TX: R(8, 5), MIXED_TY: R(8, 5), MIXED_XY: R(8, 5), TRIPLY: R(8, 5)}
W1_G1_FULL = ((R(16, 15), R(-4, 15), R(-4, 15)), (R(-4, 15), R(16, 15), R(-4, 15)), (R(-4, 15), R(-4, 15), R(16, 15)))
W1_DET_M_SHAPE = ((2, 2), (2, 2))
W1_DET_M_VALUES = {PURE_T: R(256, 225), PURE_X: R(256, 225), PURE_Y: R(256, 225),          # Block 218's 256/225 at e_t and 1024/225 at e_t + e_x
                   MIXED_TX: R(1024, 225), MIXED_TY: R(4096, 225), MIXED_XY: R(1024, 225), TRIPLY: R(3136, 225)}
BRANCH_CONSTANTS = ((1, 2), (R(128, 99), 2), (R(16, 11), 4))                          # Block 216's L+- line 1/4
QUADRIC_VALUES = {PURE_T: R(9, 8), PURE_X: R(9, 8), PURE_Y: R(9, 8),
                  MIXED_TX: R(3, 2), MIXED_TY: R(3, 2), MIXED_XY: R(3, 2), TRIPLY: R(9, 8)}
G1_FULL = ((R(9, 8), R(-3, 8), R(-3, 8)), (R(-3, 8), R(9, 8), R(-3, 8)), (R(-3, 8), R(-3, 8), R(9, 8)))
G1_BENCH = {"tt": R(9, 8), "xx": R(9, 8), "yy": R(9, 8), "tx": R(-3, 8), "ty": R(-3, 8), "xy": R(-3, 8)}
TRIPLY_Q = R(9, 8)
DET_M_SHAPE = ((2, 4),)
DET_M_VALUES = {PURE_T: R(81, 64), PURE_X: R(81, 64), PURE_Y: R(81, 64),
                MIXED_TX: sp.Integer(4), MIXED_TY: sp.Integer(4), MIXED_XY: sp.Integer(4), TRIPLY: R(81, 64)}
LINE_RESCALE_HALF = R(3, 2)                                                           # 1/(1 - (1/2)^2 / (3/4))
HALF_CONSTANTS = ((1, 2), (R(16, 9), 2), (2, 4))                                      # Block 216's symbolic constants at lam_line = 1/2
HALF_PURE_T = ((R(9, 8), 2), (2, 2), (R(9, 4), 4))
D07_CONSTANTS = ((R(128, 119), 2), (R(128, 99), 2), (R(16, 11), 4))                   # Block 216's line 1/4 + D07 1/4
D07_PURE_T = ((R(144, 119), 2), (R(16, 11), 2), (R(18, 11), 4))
OVERLAP_FOLD_ZERO_PARITY = ("D07/4 + D16/4 + D25/4 + D34/4",)                         # Block 217's (s/4) P111
OVERLAP_FOLD_PARITY = {MIXED_TX: ("-D07/4 - D16/4 + D25/4 + D34/4",),                 # Block 218's signed sum at (i,i,1)
                       MIXED_TY: ("-D07/4 + D16/4 - D25/4 + D34/4",),
                       MIXED_XY: ("-D07/4 + D16/4 + D25/4 - D34/4",)}
OVERLAP_FOLD_PARAMETER_FREE = (PURE_Y, PURE_X, PURE_T, TRIPLY)
OVERLAP_STAR_LINE = {MIXED_TX: (R(-1, 16),), MIXED_TY: (R(3, 16),), MIXED_XY: (R(-1, 16),)}
OVERLAP_LINE_EQUALS_ZERO = (("1", "1", "1"), PURE_Y, PURE_X, PURE_T, TRIPLY)
OVERLAP_LINE_DIFFERS = (MIXED_XY, MIXED_TY, MIXED_TX)
OVERLAP_TRIPLY_PENCIL = ((R(825, 371), 4), (R(537, 227), 4))
OVERLAP_TY_PENCIL = ((R(25774, 13445), 4), (R(22246, 9917), 4))
SCOUT_GRADE_FENCE = ("scout-grade finite exact linear algebra on one cell form, "
                     "not a spacetime and not a dynamics")
SCOUT_GRADE_ONLY = True
INSTANCE_SCOPE = (
    "one cell form: Block 211's family at L+-'s rule-A cell (mask 2) with Block 213's curve moduli, the all-plus W1 and the flat cell as controls; no other cell",
    "two assemblies, two readings, all four run at the witness; neither assembly decided, neither reading selected; the parameters at three numeric points on and beside the star line and at zero",
    "one bench, Block 213's bench_matrix at extent (4,4,4): all three directions sampled at the fine momentum pi/2 and at nothing else; no other extent",
    "the cone's shape in three directions: seven Bloch points fix the six entries of G1 with one consistency check; the direct degree-64 check certified for nine constructions, the overlap direct charpolys probed only",
    "the covariance notion: Block 215's (E_R R) H (E_R R)^T = H on the folded H0, measured at Block 216's named finite witnesses; the physical antecedent is not adopted",
    "no dispersion law, no Lorentzian or light-cone reading, no continuum limit, no metric of anything physical; the identity with the principal part is exact and finite, not a limit",
)
INSTANCE_SCOPE_COUNT = 6

N5_FENCE = "N5: The corrected Block 219 claim is finite. On one (4,4,4) bench at the named L+- witness, the seven sampled onsite-pencil blocks have the stated normalized branch multiset, the six quadratic entries and triply mixed consistency check, and the two named rescalings. At W1, pure-t and pure-x have different normalized monic characteristic polynomials even though Q is 16/15 at both; this cross-direction mismatch is the control result. The triply mixed ratio 32/33 is a constant and is not used as a pointwise counterexample. Primitive products are divided by their recorded leading-coefficient products before being called monic characteristic polynomials. No parent theorem, assembly choice, premise adoption, physical metric, cone, action, spacetime, continuum, dispersion law, or dynamics is claimed."


def scope_certificate(text: str) -> dict:
    return {"n5_verbatim": N5_FENCE in text}


def build_claims(mutation: str) -> dict:
    claims = {
        "current_main": CURRENT_MAIN, "parent_commit": PARENT_COMMIT,
        "registered": (), "gravity_supplied": False, "covariance_inherited": False,
        "assembly_decided": False, "cell_selected": False, "reading_selected": False, "continuum_read": False,
        "bench_momenta": BENCH_MOMENTA, "grandparent_multiset": b217.WITNESS_ONSITE_PENCIL, "flat_r5": FLAT_R5,
        "half_minors": HALF_LEADING_MINORS,
        "all_agree": True, "witness_mixed_pencil": WITNESS_MIXED_PENCIL, "w1_triply_shape": W1_TRIPLY_SHAPE,
        "raising_additive": True, "onsite_similarity": True, "triply_mixed_identity": True,
        "shape_visible": True, "g1_bench": G1_BENCH, "triply_q": TRIPLY_Q,
        "line_rescale_half": LINE_RESCALE_HALF, "d07_rescale": R(128, 119),
        "w1_irreducible_degrees": W1_IRREDUCIBLE_DEGREES, "w1_normalized_t_x_differ": True,
        "overlap_parity": OVERLAP_FOLD_PARITY,
        "scout_grade": SCOUT_GRADE_FENCE, "instance_scope_count": INSTANCE_SCOPE_COUNT,
        "n5_verbatim": True, "float_absent": True,
    }
    flips = {
        "stale_main_authority": ("current_main", STALE_MAIN),
        "stale_parent_authority": ("parent_commit", STALE_PARENT_COMMIT),
        "claim_objects_registered": ("registered", ("the cone's shape in three directions",)),
        "claim_gravity_supplied": ("gravity_supplied", True),
        "claim_covariance_inherited": ("covariance_inherited", True),
        "claim_assembly_decided": ("assembly_decided", True),
        "claim_cell_selected": ("cell_selected", True),
        "claim_reading_selected": ("reading_selected", True),
        "claim_continuum_read": ("continuum_read", True),
        "break_bench_momenta": ("bench_momenta", BENCH_MOMENTA[:7]),
        "break_witness_reproduction": ("grandparent_multiset", b217.R5_MULTISET),
        "break_flat_control": ("flat_r5", ((0, 8), (1, 24), (2, 24))),
        "break_second_multiple_positivity": ("half_minors", HALF_LEADING_MINORS[:7] + (-HALF_LEADING_MINORS[7],)),
        "break_bloch_equals_direct": ("all_agree", False),
        "break_witness_multisets": ("witness_mixed_pencil", WITNESS_PURE_PENCIL),
        "break_control_multisets": ("w1_triply_shape", b218.W1_PENCIL_SHAPES[b218.MIXED]),
        "break_raising_block_additivity": ("raising_additive", False),
        "break_onsite_similarity": ("onsite_similarity", False),
        "break_triply_mixed_identity": ("triply_mixed_identity", False),
        "break_cone_shape_visible": ("shape_visible", False),
        "break_g1_readoff": ("g1_bench", {**G1_BENCH, "ty": R(3, 8)}),
        "break_triply_mixed_consistency": ("triply_q", R(3, 2)),
        "break_line_rescaling": ("line_rescale_half", R(12, 11)),
        "break_d07_rescaling": ("d07_rescale", R(12, 11)),
        "break_control_failure": ("w1_normalized_t_x_differ", False),
        "break_overlap_fold_dependence": ("overlap_parity", {**OVERLAP_FOLD_PARITY, MIXED_TY: OVERLAP_FOLD_PARITY[MIXED_XY]}),
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
    checks.check("A-1", "EVERY DECLARED SOURCE, IMPLEMENTATION, AXIOM AND REGISTRY INPUT MATCHES ITS SHA-256 LITERAL",
                 au.all_inputs_content_bound and claims["current_main"] == CORRECTION_SOURCE_BASE)
    checks.check("A-2", "THE CORRECTED BLOCK 218 NOTE AND RUNNER ARE CONTENT-BOUND FINITE SUPPLIERS",
                 au.parent_inputs_content_bound and claims["parent_commit"] == PARENT_SOURCE_SHA256)
    checks.check("A-3", "THE CORRECTED SUPPLIER CLOSURE IMPORTS AND EVERY DECLARED INPUT IS READABLE",
                 au.machinery_import_landed and au.inputs_readable == len(AUDIT_INPUT_PATHS)
                 and not au.inputs_missing)

    checks.check("B-1", "NOTHING REGISTERED, NOTHING ADOPTED: seven imposed objects, zero registered, zero adopted",
                 len(IMPOSED_OBJECTS) == 7 and claims["registered"] == REGISTERED_OBJECTS == () and ADOPTED_OBJECTS == ())
    checks.check("B-2", "NO GRAVITY IS SUPPLIED: nine structures enumerated as not supplied",
                 not claims["gravity_supplied"] and not GRAVITY_SUPPLIED_CLAIMED and len(UNSUPPLIED_GRAVITY_STRUCTURES) == 9)
    checks.check("B-3", "THE AXIOM CLAUSE IS QUOTED VERBATIM AND GOVERNS THE RULE; that the cell form inherits it is a READING, asserted nowhere (the theorem is the conditional)",
                 AXIOM_COVARIANCE_CLAUSE in facts.axiom_text and not claims["covariance_inherited"] and not COVARIANCE_INHERITED_CLAIMED)
    checks.check("B-4", "NO CELL, NO SUBGROUP, NO ASSEMBLY, NO READING, NO PARAMETER VALUE IS SELECTED, AND NO METRIC IS SUPPLIED: that one assembly and one reading see the shape is measured, not a selector",
                 not claims["cell_selected"] and not CELL_SELECTED_CLAIMED and not claims["assembly_decided"] and not ASSEMBLY_DECIDED_CLAIMED
                 and not claims["reading_selected"] and not READING_SELECTED_CLAIMED and not METRIC_SUPPLIED_CLAIMED
                 and not SUBGROUP_SELECTED_CLAIMED and not PARAMETER_VALUE_SELECTED_CLAIMED)
    checks.check("B-5", "THE WORDS COVARIANCE, CONE, CELL, ASSEMBLY, BENCH AND SHAPE ARE SCOPED; six readings enumerated, none licensed; no dispersion law, no Lorentzian or light-cone reading, no continuum, no spacetime cone",
                 len(SCOPED_HEADLINE_WORDS) == 6 and len(READINGS) == 6 and not READINGS_LICENSED_CLAIMED
                 and not claims["continuum_read"] and not CONTINUUM_LIMIT_CLAIMED and not DISPERSION_LAW_CLAIMED
                 and not LORENTZIAN_CLAIMED and not LIGHT_CONE_CLAIMED and not CONE_IS_SPACETIME_CONE_CLAIMED)
    co, be, id_, sh, rs, ct = facts.construction, facts.bench, facts.identities, facts.shape, facts.rescalings, facts.control
    bm = be["block_multisets"]
    checks.check("C-1", "THE BENCH IS BLOCK 213's bench_matrix AT EXTENT (4,4,4): 64 sites, every direction carrying its link (64 y-link entries, 192 raising entries), the eight Bloch momenta {1, i}^3 with the triply-mixed point (i,i,i); Block 218's four and Block 217's two momenta are the smaller extents'",
                 co["momenta"] == claims["bench_momenta"] == BENCH_MOMENTA and co["kappas"] == BENCH_KAPPAS and co["triply_mixed_point_present"]
                 and co["site_count"] == SITE_COUNT and co["y_link_entries"] == Y_LINK_ENTRIES and co["raising_bench_nnz"] == RAISING_BENCH_NNZ
                 and co["parent_momenta"] == b218.BENCH_MOMENTA and co["grandparent_momenta"] == b217.BENCH_MOMENTA)
    checks.check("C-2", "THE WITNESS AND THE CONTROL ARE BLOCKS 216-218's: mask 2 = L+-'s signs (+,+,+,+,-,+); the three parameter points as declared; Block 218's (4,4,2) block multisets and Block 217's (4,2,2) multiset reproduce with Bloch = direct (the smaller-extent gates); G1_tt = 9/8; W1's moduli are Block 211's",
                 co["witness_values"] == (WITNESS_SIGNS,) and co["witness_is_rule_a"] and co["l_plus_minus_signs"] == WITNESS_SIGNS
                 and co["face_orders_agree"] and co["line_point_entries"] == LINE_POINT_ENTRIES == tuple(LINE_POINT)
                 and co["half_point_entries"] == HALF_POINT_ENTRIES and co["d07_point_entries"] == D07_POINT_ENTRIES
                 and co["parent_bench_agrees"] and co["parent_block_multisets"] == {("1", "1", "1"): ((0, 8),), b218.PURE_T: b218.WITNESS_PURE_PENCIL,
                                                                                    b218.PURE_X: b218.WITNESS_PURE_PENCIL, b218.MIXED: b218.WITNESS_MIXED_PENCIL}
                 and co["grandparent_bench_multiset"] == claims["grandparent_multiset"] == b217.WITNESS_ONSITE_PENCIL and co["grandparent_bench_agrees"]
                 and co["g1_tt_witness"] == G1_TT_WITNESS == b217.G1_TT_WITNESS and co["w1_moduli_is_block211"])
    checks.check("C-3", "THE FLAT CONTROL AT ZERO PARAMETERS GIVES R5's MULTISET {0 x8, 1 x24, 2 x24, 3 x8} = Block 213's expected_flat_multiset((4,4,4)) under both assemblies and both readings, direct",
                 be["flat_zero_is_r5"] and be["flat_expected"] == claims["flat_r5"] == FLAT_R5)
    checks.check("C-4", "THE SECOND LINE MULTIPLE IS POSITIVE DEFINITE BEFORE USE: the eight leading minors of the cell at (0, 1/2, -1/2, 1/2) are positive (sqrt6/3, 3/4, sqrt6/4, 3/4, sqrt6/8, 3/16, sqrt6/24, 1/9), lambda^2 = 1/4 < v0 v1 = 3/4; the D07 point and the line point are positive definite too",
                 co["positive_definite witness half"] and co["positive_definite witness d07"] and co["positive_definite witness line"]
                 and co["leading_minors witness half"] == claims["half_minors"] == HALF_LEADING_MINORS
                 and co["half_multiple_below_volume_product"] and co["volume_product"] == VOLUME_PRODUCT == b216.VOLUME_PRODUCTS["L+-"])
    checks.check("D-1", "BLOCH UNION = DIRECT BENCH at every one of the nine declared direct degree-64 charpolys over QQ(sqrt 6) and QQ(sqrt 6, i) (fourteen constructions, nine direct); every Bloch union has degree 64; the zero Bloch point contributes eight zeros everywhere",
                 claims["all_agree"] and be["all_direct_agree"] and be["all_direct_degree_64"] and be["all_union_degree_64"]
                 and be["charpoly_count"] == CHARPOLY_COUNT and be["direct_count"] == DIRECT_COUNT and be["zero_point_is_eight_zeros"])
    checks.check("D-2", "THE WITNESS BLOCKS: onsite pencil {9/8 x2, 16/11 x2, 18/11 x4} at the three pure points AND at the triply-mixed point, {3/2 x2, 64/33 x2, 24/11 x4} at the three doubly-mixed points; the direct degree-64 multiset {0 x8, 9/8 x8, 16/11 x8, 3/2 x6, 18/11 x16, 64/33 x6, 24/11 x12}",
                 all(bm[("witness line", "onsite", "pencil")][z] == WITNESS_PURE_PENCIL for z in PURE_POINTS + (TRIPLY,))
                 and all(bm[("witness line", "onsite", "pencil")][z] == claims["witness_mixed_pencil"] == WITNESS_MIXED_PENCIL for z in DOUBLY_MIXED_POINTS)
                 and be["multisets"][("witness line", "onsite", "pencil")] == WITNESS_DIRECT_PENCIL)
    checks.check("D-3", "THE CONTROL BLOCK AT THE TRIPLY-MIXED POINT at the all-plus W1: (5 lam - 8)^2 (165 lam - 256)^2 times an irreducible quadratic squared, the rational roots 8/5 and 256/165; no W1 block multiset is rational; the W1 direct degree-64 charpoly has Bloch union = direct",
                 ct["w1_triply_shape"] == claims["w1_triply_shape"] == W1_TRIPLY_SHAPE
                 and ct["w1_triply_rational_roots"] == W1_TRIPLY_RATIONAL_ROOTS
                 and ct["w1_triply_extra_ratio"] == W1_TRIPLY_EXTRA_RATIO
                 and ct["w1_triply_shape_divisor"] == W1_TRIPLY_MONIC_DIVISOR
                 and ct["w1_multisets_none"] and ct["w1_direct_agrees"])
    checks.check("E-1", "THE RAISING BLOCH BLOCK IS i D(kappa_z) AT ALL EIGHT POINTS, MEASURED FIRST: d_B(z) = sum_mu (z_mu - 1/z_mu)/2 D(e_mu) at symbolic z with z_y live; D(e_mu)^2 = 0, the D(e_mu) anticommute, D(kappa_z)^2 = 0 at every point incl. e_t + e_x + e_y",
                 all(id_["raising_block_is_i_d"].values()) and claims["raising_additive"] and id_["raising_block_additive_symbolic"]
                 and id_["z_y_live_in_symbolic_block"] and id_["d_mu_squared_zero"] and id_["d_mu_anticommute"] and all(id_["d_kappa_squared_zero"].values()))
    checks.check("E-2", "THE ONSITE HODGE BLOCH BLOCK IS Z^-1 H0 Z with Z = diag(z^c) at all eight points, at the witness, the control, the flat cell and the two rescaled points",
                 claims["onsite_similarity"] and id_["onsite_similarity_everywhere"])
    checks.check("E-3", "THE IDENTITY WITH THE PRINCIPAL PART AT ALL EIGHT POINTS: the onsite pencil block charpoly equals the charpoly of (H0^-1 M(kappa_z))^2 -- the TRIPLY-MIXED point with kappa = e_t + e_x + e_y included -- at the witness, the control, the flat cell and the two rescaled points; it fails for the form reading and for the overlap assembly at every nonzero point of the witness",
                 claims["triply_mixed_identity"] and id_["onsite_pencil_identity_everywhere"] and all(id_["triply_mixed_identity"].values())
                 and id_["form_fails_at_every_nonzero_point"] and id_["overlap_fails_at_every_nonzero_point"])
    checks.check("F-1", "THE SHAPE IN THREE DIRECTIONS: at each of the seven nonzero points every nonzero eigenvalue is a Block 216 branch constant {1, 128/99, 16/11 x2} times k^T G1 k at kappa_z, the quadric values 9/8 (pure), 3/2 (doubly-mixed), 9/8 (triply-mixed) computed from G1 = D1/D0 = (3/8)[[3,-1,-1],[-1,3,-1],[-1,-1,3]], parameter-free",
                 claims["shape_visible"] and sh["shape_visible"] and sh["predicted_equal_measured"] and sh["constants"] == BRANCH_CONSTANTS
                 and sh["quadric_values"] == QUADRIC_VALUES and sh["g1_full"] == G1_FULL and sh["g1_parameter_free"])
    checks.check("F-2", "G1 READ OFF THE BENCH: the six entries (9/8, 9/8, 9/8; -3/8, -3/8, -3/8) from the three pure and three doubly-mixed points equal the entries of D1/D0; the pure points coincide and the doubly-mixed points coincide",
                 sh["g1_bench"] == claims["g1_bench"] == G1_BENCH and sh["g1_bench_equals_g1"] and sh["pure_points_coincide"] and sh["doubly_mixed_points_coincide"])
    checks.check("F-3", "THE TRIPLY-MIXED CONSISTENCY CHECK: Q(e_t + e_x + e_y) predicted from the six entries, 3(9/8) + 6(-3/8) = 9/8, equals the measured constant-1 branch 9/8, so the triply-mixed multiset is the pure one; det M on the line is one quadric to the fourth, (64/81) Q^4 at all seven points (81/64, 81/64, 81/64, 4, 4, 4, 81/64)",
                 sh["triply_predicted"] == claims["triply_q"] == TRIPLY_Q == sh["triply_measured"] and sh["triply_consistent"] and sh["triply_equals_pure"]
                 and sh["det_m_shape"] == DET_M_SHAPE and sh["det_m_values"] == DET_M_VALUES and sh["det_m_is_quadric_fourth"])
    checks.check("G-1", "THE LINE RESCALING SEEN ON THE BENCH: at lambda = 1/2 the block multisets at all seven points are Block 216's symbolic constants at lam_line = 1/2, {1, 16/9, 2 x2} = {1, (32/27) r, (4/3) r x2} with r = 1/(1 - lambda^2/(v0 v1)) = 3/2 (12/11 = LINE_RESCALE at 1/4), times Q; the pure-t multiset {9/8 x2, 2 x2, 9/4 x4}; Bloch = direct; G1 read off unchanged",
                 rs["line_rescale_half"] == claims["line_rescale_half"] == LINE_RESCALE_HALF and rs["line_rescale_quarter_is_block216"]
                 and rs["constants_half_symbolic"] == HALF_CONSTANTS and rs["constants_half_is_rescaled"] and rs["constants_quarter_is_rescaled"]
                 and rs["constants_quarter_is_table"] and rs["shape_visible witness half"]
                 and rs["pure_t_multiset witness half"] == HALF_PURE_T == rs["pure_t_predicted witness half"]
                 and rs["direct_agrees witness half"] and rs["g1_bench_equals_g1 witness half"] and rs["g1_bench_ratio witness half"] == frozenset({sp.Integer(1)}))
    checks.check("G-2", "THE D07 RESCALING SEEN ON THE BENCH: at D07 = 1/4 the block multisets at all seven points are Block 216's {128/119, 128/99, 16/11 x2} times Q, the 0-form constant rescaled by 1/(1 - D07^2 v1/v0) = 128/119 = D07_RESCALE; the pure-t multiset {144/119 x2, 16/11 x2, 18/11 x4}; Bloch = direct; the bench read-off of G1 is (128/119) G1 exactly, the constant-1 branch carrying the rescaling",
                 rs["d07_rescale_quarter"] == claims["d07_rescale"] == R(128, 119) == b216.D07_RESCALE["L+-"] and rs["d07_rescale_quarter_is_block216"]
                 and rs["constants_d07_table"] == D07_CONSTANTS and rs["constants_d07_is_rescaled"] and rs["shape_visible witness d07"]
                 and rs["pure_t_multiset witness d07"] == D07_PURE_T == rs["pure_t_predicted witness d07"]
                 and rs["direct_agrees witness d07"] and rs["g1_bench_ratio witness d07"] == frozenset({R(128, 119)}))
    checks.check("G-3", "THE W1 CONTROL HAS NO COMMON NORMALIZED MONIC SPECTRUM ACROSS PURE t AND PURE x: Q=16/15 AT BOTH, BUT THE COMPLETE NORMALIZED POLYNOMIALS DIFFER; the triply mixed extra ratio is the pointwise constant 32/33 and is not used as a counterexample",
                 id_["triply_mixed_identity"]["W1 line"] and ct["w1_rational_branch_is_quadric"]
                 and ct["w1_irreducible_degrees"] == W1_IRREDUCIBLE_DEGREES
                 and ct["w1_quadric_values"] == W1_QUADRIC_VALUES
                 and ct["w1_g1_full"] == W1_G1_FULL and ct["w1_g1_bench_equals_g1"]
                 and claims["w1_normalized_t_x_differ"] and ct["w1_normalized_t_x_differ"]
                 and ct["w1_triply_extra_ratio"] == W1_TRIPLY_EXTRA_RATIO
                 and ct["w1_det_m_shape"] == W1_DET_M_SHAPE
                 and ct["w1_det_m_values"] == W1_DET_M_VALUES)

    checks.check("G-4", "THE OVERLAP FOLD AT THE NEW POINTS, at symbolic signs, moduli and parameters: parameter-free at the three pure points AND at the triply-mixed point; all four parameters at the three doubly-mixed points through the signed sums (-D07 - D16 + D25 + D34)/4, (-D07 + D16 - D25 + D34)/4, (-D07 + D16 + D25 - D34)/4 (-1/16, 3/16, -1/16 on the star line); the overlap bench at the line point equals the zero-parameter one at the four parameter-free points and at the zero point (d_B = 0 there) and differs at the three doubly-mixed points; the overlap bench identifies t with y and distinguishes x where the onsite bench identifies all three; the declared triply-mixed and (i,1,i) overlap pencil multisets",
                 ct["overlap_fold_parameter_free_points"] == OVERLAP_FOLD_PARAMETER_FREE
                 and ct["overlap_fold_parity_blocks"] == {("1", "1", "1"): OVERLAP_FOLD_ZERO_PARITY, **claims["overlap_parity"]}
                 and claims["overlap_parity"] == OVERLAP_FOLD_PARITY and ct["overlap_fold_star_line_values"] == OVERLAP_STAR_LINE
                 and ct["overlap_line_equals_zero_points"] == OVERLAP_LINE_EQUALS_ZERO and ct["overlap_line_differs_points"] == OVERLAP_LINE_DIFFERS
                 and ct["overlap_t_equals_y_not_x"] and ct["onsite_pure_points_coincide"]
                 and ct["overlap_triply_pencil"] == OVERLAP_TRIPLY_PENCIL and ct["overlap_ty_pencil"] == OVERLAP_TY_PENCIL)
    checks.check("H-1", "FINITE-SCOPE FENCE AGREES WITH THE CORRECTED SUPPLIERS",
                 claims["scout_grade"] == SCOUT_GRADE_FENCE == b218.SCOUT_GRADE_FENCE == b217.SCOUT_GRADE_FENCE and SCOUT_GRADE_ONLY)
    checks.check("H-2", "THE INSTANCE SCOPE IS ENUMERATED: six restrictions",
                 claims["instance_scope_count"] == len(INSTANCE_SCOPE) == 6)
    sc = scope_certificate(facts.note_text)
    checks.check("I-1", "THE NOTE IS PRESENT AND CARRIES THE N5 FENCE BYTE-IDENTICALLY",
                 bool(facts.note_text) and sc["n5_verbatim"] == claims["n5_verbatim"] and claims["n5_verbatim"])
    checks.check("I-2", "NO nsimplify, NO float literal, NO float call in this runner's source",
                 nsimplify_occurrences() == 0 and float_literal_occurrences() == 0 and float_call_sites() == 0 and claims["float_absent"])
    return checks


def report_measured(facts: Facts, elapsed_ns: int) -> None:
    print("== BLOCK 219: corrected finite three-direction bench -- measured facts ==")
    print(f"authority: {facts.authority}")
    for name in ("construction", "bench", "identities", "shape", "rescalings", "control"):
        section = getattr(facts, name)
        for key in sorted(section, key=str):
            value = section[key]
            if isinstance(value, dict):
                for inner in sorted(value, key=str):
                    item = value[inner]
                    if isinstance(item, dict):
                        item = {k: v for k, v in item.items() if k not in ("charpoly", "blocks")}
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
