#!/usr/bin/env python3
"""Corrected Block 218 finite two-direction bench calculation.

The runner retains exact direct/Bloch characteristic-polynomial comparisons,
the onsite Bloch/principal-part similarity, the named L+- branch ratios and
cross term, and the overlap-fold measurements on one (4,4,2) bench. The W1
control compares complete normalized monic characteristic polynomials across
the pure-t and pure-x directions. A value at one point is never used to infer
or refute a direction-independent branch constant. Primitive integer factor
shapes are kept distinct from monic polynomials. No parent theorem, premise,
assembly choice, physical metric, cone, action, spacetime, continuum,
dispersion law, dynamics, or gravity is supplied.
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
from sympy import QQ
from sympy.polys.matrices import DomainMatrix

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

# THE MACHINERY IMPORTS, LANDED IN THIS BRANCH AND READ-ONLY: Block 217 (the
# bench over algebraic number fields, its cells) and through it Blocks 216,
# 215, 214, 213, 211, 209.
try:
    import admissibility_dirac_kahler_overlap_assembly_covariant_cells_2026_09_05 as b217
    B217_IMPORT_LANDED = True
except ModuleNotFoundError:                            # pragma: no cover
    b217 = None
    B217_IMPORT_LANDED = False
b216 = b217.b216 if b217 is not None else None
b215 = b217.b215 if b217 is not None else None
b214 = b217.b214 if b217 is not None else None
b213 = b217.b213 if b217 is not None else None
b211 = b217.b211 if b217 is not None else None
b209 = b217.b209 if b217 is not None else None
MACHINERY_IMPORT_LANDED = bool(B217_IMPORT_LANDED and b217 is not None and b217.MACHINERY_IMPORT_LANDED
                               and b216 is not None and b214 is not None and b213 is not None
                               and b211 is not None and b209 is not None)
# Corrected finite suppliers. Every live implementation and citation input is
# bound below by SHA-256. Historical Git ancestry remains in recovery only.
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
PARENT_NOTE = B217_NOTE
PARENT_RUNNER = B217_RUNNER
PARENT_ARTIFACTS = (PARENT_NOTE, PARENT_RUNNER)
FINAL_NOTE_NAME = "ADMISSIBILITY_DIRAC_KAHLER_TWO_DIRECTION_BENCH_COVARIANT_WITNESS_BOUNDED_THEOREM_NOTE_2026-09-05.md"
NOTE_PATH = ROOT / "docs" / FINAL_NOTE_NAME
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"

AUDIT_INPUT_PATHS = (
    'docs/ADMISSIBILITY_DIRAC_KAHLER_TWO_DIRECTION_BENCH_COVARIANT_WITNESS_BOUNDED_THEOREM_NOTE_2026-09-05.md',
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
    SELF_NOTE_INPUT: "4dfebc34b34daedc6a52d3ab9dfb324428c812c5cf61e2c9babdb4c2565545e5",
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
AUDIT_TIMEOUT_SEC = 120
CORRECTION_SOURCE_BASE = "09dafe5bf6fb030249b368987fff091ef339c78a"
PARENT_SOURCE_SHA256 = INPUT_SHA256[B217_RUNNER]
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
    "break_bloch_equals_direct",
    "break_witness_multisets",
    "break_control_multisets",
    "break_raising_block_additivity",
    "break_onsite_similarity",
    "break_mixed_point_identity",
    "break_cone_shape_visible",
    "break_cross_term",
    "break_control_failure",
    "break_overlap_fold_dependence",
    "break_direction_distinction",
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
    "break_bloch_equals_direct": "D", "break_witness_multisets": "D", "break_control_multisets": "D",
    "break_raising_block_additivity": "E", "break_onsite_similarity": "E", "break_mixed_point_identity": "E",
    "break_cone_shape_visible": "F", "break_cross_term": "F",
    "break_control_failure": "G", "break_overlap_fold_dependence": "G", "break_direction_distinction": "G",
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
    "Block 216's 8 rule-A covariant witnesses, their strict S3_body stabilisers under the onsite assembly and their four pencil branch constants on the star line",
    "Block 217's algebraic-field bench (Bloch union = direct over QQ(sqrt 6) and QQ(sqrt 6, i)), its cells and its (4,2,2) identity at kappa = e_t",
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
    "R2 the bench's seeing the cone's shape under the onsite assembly and not under the overlap assembly decides the assembly (not established: both are measured, neither is selected)",
    "R3 'one metric's cone' or 'the cone's shape' is a metric, a cone or a shape of anything physical (not established: Block 213's polynomial statement, restricted here to the (t, x) plane)",
    "R4 the bench multisets are a dispersion law, a Lorentzian light cone or a continuum limit (not established: thirty-two exact eigenvalues of one finite matrix at four Bloch points, the y direction unsampled)",
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
QUARTER = sp.Rational(1, 4)
BENCH_EXTENT = (4, 4, 2)                  # the two-direction bench of the three-direction chain: 32 sites
PARENT_EXTENT = (4, 2, 2)                 # Block 213's three-direction bench, Block 217's (one direction sampled)
LINE_POINT = b217.LINE_POINT              # (D07, D16, D25, D34) = (0, 1/4, -1/4, 1/4) on the star line
ZERO_POINT = (sp.Integer(0),) * 4
ALL_PLUS_CELL = b216.ALL_PLUS_CELL
W1_MODULI = b216.W1_MODULI                # (v0, g0, v1, g1) = (15/16, 1/4, 1, 1/4)
FLAT_MODULI = b216.FLAT_MODULI
REAL_FIELD = QQ.algebraic_field(sp.sqrt(6))
COMPLEX_FIELD = QQ.algebraic_field(sp.sqrt(6), sp.I)
UNIT_KAPPAS = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
Z_SYMBOLS = sp.symbols("z_t z_x z_y")
SIGN_SYMBOLS = sp.symbols("s_tx0 s_ty0 s_xy0 s_tx1 s_ty1 s_xy1")

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


def residual_count(matrix) -> int:
    return sum(1 for entry in matrix if entry != 0)


def is_zero_matrix(matrix) -> bool:
    return residual_count(matrix.applyfunc(sp.expand)) == 0


def kappa_of(z: tuple) -> tuple:
    """kappa_z = e_t [z_t = i] + e_x [z_x = i] + e_y [z_y = i]: the direction the fine momentum pi/2 samples."""
    return tuple(1 if entry == sp.I else 0 for entry in z)


def momentum_literal(z: tuple) -> tuple:
    return tuple(str(entry) for entry in z)


def raising_operator(kappa: tuple) -> sp.Matrix:
    """Block 214's first-order raising matrix D(kappa) at a numeric kappa."""
    return b214.raising_matrix().subs(dict(zip(KAPPA, kappa)))


def phase_matrix(z: tuple) -> sp.Matrix:
    """Z = diag(z^c) over Block 209's corners: the onsite similarity H_B(z) = Z^-1 H0 Z."""
    return sp.diag(*[sp.prod([z[k] ** c[k] for k in range(3)]) for c in b209.CORNERS])


def bench_cells(census: dict) -> dict:
    """Block 217's bench cells (the same function: L+-'s own cell at mask 2 with
    the curve moduli, the all-plus W1 control and the flat cell at the line
    point; the first two at zero parameters) plus the flat cell at zero
    parameters, the R5 control of the bench construction."""
    cells = dict(b217.bench_cells(census))
    cells["flat zero"] = b217.formal(ALL_PLUS_CELL, b217.moduli_as_g(FLAT_MODULI), ZERO_POINT)
    return cells


# ---------------------------------------------------------------------------
# C/D. THE BENCH at extent (4,4,2) over QQ(sqrt 6) and QQ(sqrt 6, i): both
# assemblies, both readings, the direct 32 x 32 charpoly and the four 8 x 8
# Bloch blocks, Bloch union = direct
# ---------------------------------------------------------------------------
def raising_rules() -> dict:
    return b213.raising_rules(b213.lane_rules(3))


def bench_charpolys(cell: sp.Matrix, assembly: str, reading: str) -> tuple:
    """(direct 32 x 32 charpoly over QQ(sqrt 6), Bloch union over QQ(sqrt 6, i),
    the 8 x 8 block charpoly per momentum, seconds direct, seconds union)."""
    rules = (b213.onsite_rules if assembly == "onsite" else b213.overlap_rules)(cell, b209.CORNERS, 3)
    raising = raising_rules()
    started = time.monotonic_ns()
    hodge = DomainMatrix.from_Matrix(b213.bench_matrix(rules, BENCH_EXTENT)).convert_to(REAL_FIELD)
    lifted = DomainMatrix.from_Matrix(b213.bench_matrix(raising, BENCH_EXTENT)).convert_to(REAL_FIELD)
    direct = b217.alg_charpoly(b217.symbol_matrix(hodge, lifted, lifted.transpose(), reading), REAL_FIELD)
    direct_ms = (time.monotonic_ns() - started) // 1_000_000
    started = time.monotonic_ns()
    blocks: dict = {}
    transposed = b213.transpose_rules(raising)
    for z in b213.bench_momenta(BENCH_EXTENT):
        h_b = DomainMatrix.from_Matrix(b213.bloch_matrix(rules, z, 3)).convert_to(COMPLEX_FIELD)
        d_b = DomainMatrix.from_Matrix(b213.bloch_matrix(raising, z, 3)).convert_to(COMPLEX_FIELD)
        dt_b = DomainMatrix.from_Matrix(b213.bloch_matrix(transposed, z, 3)).convert_to(COMPLEX_FIELD)
        blocks[momentum_literal(z)] = b217.alg_charpoly(b217.symbol_matrix(h_b, d_b, dt_b, reading), COMPLEX_FIELD)
    union = sp.expand(sp.prod(list(blocks.values())))
    return direct, union, blocks, direct_ms, (time.monotonic_ns() - started) // 1_000_000


def rational_roots(charpoly) -> tuple:
    return tuple(sorted(((root, mult) for root, mult in sp.roots(sp.Poly(charpoly, LAM)).items() if root.is_rational),
                        key=lambda t: t[0]))


def normalized_monic_charpoly(charpoly, quadric_value):
    """Monic spectrum after dividing all roots by a nonzero Q value."""
    poly = sp.Poly(charpoly, LAM)
    normalized = sp.cancel(poly.as_expr().subs(LAM, quadric_value * LAM)
                           / quadric_value ** poly.degree())
    return sp.Poly(normalized, LAM).monic().as_expr()


def measure_bench(cells: dict) -> dict:
    """D: every (cell, assembly, reading) charpoly of degree 32 on (4,4,2):
    Bloch union = direct bench, the multiset or the factor shape, the same per
    8 x 8 Bloch block, the two timings."""
    facts: dict = {}
    table: dict = {}
    for label, cell in cells.items():
        assemblies = ("onsite", "overlap") if label.endswith("line") or label == "flat zero" else ("overlap",)
        for assembly in assemblies:
            for reading in ("form", "pencil"):
                print(f"[bench] {label} {assembly} {reading}", file=sys.stderr)
                direct, union, blocks, direct_ms, union_ms = bench_charpolys(cell, assembly, reading)
                table[(label, assembly, reading)] = {
                    "agree": sp.expand(direct - union) == 0, "multiset": b213.multiset_of(direct),
                    "shape": b217.charpoly_shape(direct), "degree": sp.Poly(direct, LAM).degree(),
                    "block_multisets": {z: b213.multiset_of(cp) for z, cp in blocks.items()},
                    "block_shapes": {z: b217.charpoly_shape(cp) for z, cp in blocks.items()},
                    "block_rational_roots": {z: rational_roots(cp) for z, cp in blocks.items()},
                    "direct_ms": direct_ms, "union_ms": union_ms, "charpoly": direct, "blocks": blocks,
                }
    facts["table"] = table
    facts["charpoly_count"] = len(table)
    facts["all_agree"] = all(e["agree"] for e in table.values())
    facts["all_degree_32"] = all(e["degree"] == 32 for e in table.values())
    facts["zero_point_is_eight_zeros"] = all(e["block_multisets"][("1", "1", "1")] == ((0, 8),) for e in table.values())
    facts["block_multisets"] = {key: e["block_multisets"] for key, e in table.items()}
    facts["block_shapes"] = {key: e["block_shapes"] for key, e in table.items()}
    facts["multisets"] = {key: e["multiset"] for key, e in table.items()}
    facts["shapes"] = {key: e["shape"] for key, e in table.items()}
    expected = b213.expected_flat_multiset(BENCH_EXTENT)
    facts["flat_expected"] = expected
    facts["flat_zero_is_r5"] = all(table[("flat zero", a, r)]["multiset"] == expected
                                   for a in ("onsite", "overlap") for r in ("form", "pencil"))
    facts["timings_ms"] = {key: (e["direct_ms"], e["union_ms"]) for key, e in table.items()}
    facts["max_direct_ms"] = max(e["direct_ms"] for e in table.values())
    return facts


# ---------------------------------------------------------------------------
# C. CONSTRUCTION FIDELITY: the bench is Block 213's at extent (4,4,2), the
# witness and the control are Blocks 216/217's, the mixed point exists
# ---------------------------------------------------------------------------
def measure_construction(census: dict, cells: dict) -> dict:
    facts: dict = {}
    momenta = b213.bench_momenta(BENCH_EXTENT)
    facts["momenta"] = tuple(momentum_literal(z) for z in momenta)
    facts["kappas"] = tuple(kappa_of(z) for z in momenta)
    facts["mixed_point_present"] = ("I", "I", "1") in facts["momenta"]
    facts["site_count"] = len(b213.bench_sites(BENCH_EXTENT))
    lifted = b213.bench_matrix(raising_rules(), BENCH_EXTENT)
    sites = b213.bench_sites(BENCH_EXTENT)
    facts["y_link_entries"] = sum(
        1 for a in sites for b in sites
        if a[:2] == b[:2] and a != b and lifted[b213.site_index(a, BENCH_EXTENT), b213.site_index(b, BENCH_EXTENT)] != 0)
    facts["raising_bench_nnz"] = residual_count(lifted)
    facts["parent_momenta"] = tuple(momentum_literal(z) for z in b213.bench_momenta(PARENT_EXTENT))
    # the witness: Block 216's mask-2 rule-A cell carries Block 213's L+- face signs
    witness_values = tuple(v for v in census["cells"] if census["cells"][v]["mask"] == 2)
    facts["witness_values"] = witness_values
    facts["witness_is_rule_a"] = all(census["cells"][v]["rule_a"] for v in witness_values)
    facts["l_plus_minus_signs"] = tuple(b213.locus_witness_table()["L+-"][1][f] for f in b213.FACES)
    facts["face_orders_agree"] = tuple(FACE_ORDER) == tuple(b213.FACES)
    cell = cells["witness line"]
    facts["line_point_entries"] = tuple(cell[i, j] for i, j in ((0, 7), (1, 6), (2, 5), (3, 4)))
    facts["witness_moduli"] = b217.curve_moduli(1)
    facts["w1_moduli_is_block211"] = tuple(W1_MODULI) == tuple(b211.W1_MODULI)
    # Block 213's smaller-extent check as the consistency gate: Block 217's (4,2,2) identity at the witness
    started = time.monotonic_ns()
    direct, union, _, _ = b217.bench_charpolys(cell, "onsite", "pencil")
    facts["parent_bench_multiset"] = b213.multiset_of(direct)
    facts["parent_bench_agrees"] = sp.expand(direct - union) == 0
    facts["parent_bench_ms"] = (time.monotonic_ns() - started) // 1_000_000
    g1 = b213.metric_candidates(cells["witness zero"])[0].applyfunc(sp.radsimp)
    facts["g1_tt_witness"] = g1[0, 0]
    return facts


# ---------------------------------------------------------------------------
# E. THE BLOCH-POINT IDENTITIES: the raising block is i D(kappa_z) (measured
# first, at symbolic z), the onsite Hodge block is Z^-1 H0 Z, d^2 = 0, and
# hence the onsite pencil block charpoly is the principal part's at every
# point -- the mixed point included
# ---------------------------------------------------------------------------
def principal_square(cell: sp.Matrix, assembly: str, reading: str) -> sp.Matrix:
    """(H0^-1 M(kappa))^2 (pencil) or M(kappa)^2 (form), symbolic in kappa."""
    h0, m, _ = b214.principal_part(cell, assembly)
    if reading == "pencil":
        operator = (h0.inv() * m).applyfunc(sp.radsimp)
        return (operator * operator).applyfunc(sp.radsimp)
    return (m * m).applyfunc(sp.expand)


def principal_charpoly(square: sp.Matrix, kappa: tuple):
    at = square.subs(dict(zip(KAPPA, kappa)))
    return b217.alg_charpoly(DomainMatrix.from_Matrix(at).convert_to(REAL_FIELD), REAL_FIELD)


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
    units = tuple(raising_operator(k) for k in UNIT_KAPPAS)
    facts["d_mu_squared_zero"] = all(is_zero_matrix(d * d) for d in units)
    facts["d_mu_anticommute"] = all(is_zero_matrix(units[a] * units[b] + units[b] * units[a])
                                    for a in range(3) for b in range(a + 1, 3))
    facts["d_mixed_squared_zero"] = is_zero_matrix((units[0] + units[1]) * (units[0] + units[1]))
    facts["onsite_similarity"] = {}
    for label in ("witness line", "W1 line", "flat line"):
        rules = b213.onsite_rules(cells[label], b209.CORNERS, 3)
        h0 = b213.folded_matrix(rules, 3)
        facts["onsite_similarity"][label] = all(
            is_zero_matrix(b213.bloch_matrix(rules, z, 3) - phase_matrix(z).inv() * h0 * phase_matrix(z)) for z in momenta)
    facts["onsite_similarity_everywhere"] = all(facts["onsite_similarity"].values())
    table: dict = {}
    for label in ("witness line", "W1 line", "flat line"):
        for assembly in ("onsite", "overlap"):
            for reading in ("form", "pencil"):
                square = principal_square(cells[label], assembly, reading)
                blocks = bench["table"][(label, assembly, reading)]["blocks"]
                table[(label, assembly, reading)] = {
                    momentum_literal(z): sp.expand(blocks[momentum_literal(z)] - principal_charpoly(square, kappa_of(z))) == 0
                    for z in momenta}
    facts["identity_table"] = table
    nonzero = tuple(momentum_literal(z) for z in momenta if kappa_of(z) != (0, 0, 0))
    facts["nonzero_points"] = nonzero
    facts["onsite_pencil_identity_everywhere"] = all(
        all(table[(label, "onsite", "pencil")].values()) for label in ("witness line", "W1 line", "flat line"))
    facts["mixed_point_identity"] = {label: table[(label, "onsite", "pencil")][("I", "I", "1")]
                                     for label in ("witness line", "W1 line", "flat line")}
    facts["form_fails_at_every_nonzero_point"] = not any(
        table[(label, assembly, "form")][z] for label in ("witness line", "W1 line")
        for assembly in ("onsite", "overlap") for z in nonzero)
    facts["overlap_fails_at_every_nonzero_point"] = not any(
        table[(label, "overlap", reading)][z] for label in ("witness line", "W1 line")
        for reading in ("form", "pencil") for z in nonzero)
    facts["flat_overlap_table"] = {reading: table[("flat line", "overlap", reading)] for reading in ("form", "pencil")}
    return facts


# ---------------------------------------------------------------------------
# F. THE CONE'S SHAPE FROM THE BENCH at the witness: every nonzero eigenvalue
# at the three nonzero points is a branch constant times k^T G1 k at kappa_z,
# and the cross term G1_tx is isolated from the three points
# ---------------------------------------------------------------------------
def branch_constants() -> tuple:
    return tuple((sp.Rational(ratio), power) for ratio, power, _ in b216.BRANCH_TABLE[("L+-", "line 1/4")][0])


def quadric_values(g1: sp.Matrix, points: tuple) -> dict:
    return {z: sp.radsimp(b213.quadratic_form(g1, kappa_of(tuple(sp.sympify(e) for e in z)))) for z in points}


def cross_term_from_bench(multisets: dict, points: tuple):
    """G1_tx read from the bench alone: the smallest nonzero eigenvalue at each
    point is the constant-1 branch, Q(kappa_z); then (Q_mixed - Q_t - Q_x)/2."""
    smallest = {z: min(root for root, _ in multisets[z] if root != 0) for z in points}
    return sp.radsimp((smallest[("I", "I", "1")] - smallest[("I", "1", "1")] - smallest[("1", "I", "1")]) / 2), smallest


def measure_shape(cells: dict, bench: dict) -> dict:
    facts: dict = {}
    g1 = b213.metric_candidates(cells["witness zero"])[0].applyfunc(sp.radsimp)
    facts["g1_plane"] = (g1[0, 0], g1[0, 1], g1[1, 1])
    facts["g1_full"] = tuple(tuple(g1[i, j] for j in range(3)) for i in range(3))
    points = (("I", "1", "1"), ("1", "I", "1"), ("I", "I", "1"))
    facts["points"] = points
    facts["constants"] = branch_constants()
    facts["quadric_values"] = quadric_values(g1, points)
    multisets = bench["block_multisets"][("witness line", "onsite", "pencil")]
    facts["multisets"] = {z: multisets[z] for z in points}
    facts["ratios"] = {z: None if multisets[z] is None else tuple(sorted(
        ((sp.radsimp(root / facts["quadric_values"][z]), mult) for root, mult in multisets[z] if root != 0),
        key=lambda t: t[0])) for z in points}
    facts["shape_visible"] = all(facts["ratios"][z] == facts["constants"] for z in points)
    facts["predicted_multisets"] = {z: tuple(sorted(((sp.radsimp(c * facts["quadric_values"][z]), m)
                                                     for c, m in facts["constants"]), key=lambda t: t[0])) for z in points}
    facts["predicted_equal_measured"] = all(facts["predicted_multisets"][z] == multisets[z] for z in points)
    facts["cross_term_bench"], facts["smallest_eigenvalues"] = cross_term_from_bench(multisets, points)
    facts["cross_term_equals_g1"] = facts["cross_term_bench"] == g1[0, 1]
    facts["pure_points_coincide"] = multisets[("I", "1", "1")] == multisets[("1", "I", "1")]
    h0, m, _ = b214.principal_part(cells["witness line"], "onsite")
    det = sp.radsimp(m.det(method="berkowitz"))
    constant, factors = sp.factor_list(det, *KAPPA, extension=sp.sqrt(6))
    facts["det_m_shape"] = tuple(sorted((sp.Poly(f, *KAPPA).total_degree(), p) for f, p in factors))
    facts["det_m_values"] = (det.subs({KT: 1, KX: 0, KY: 0}), det.subs({KT: 0, KX: 1, KY: 0}), det.subs({KT: 1, KX: 1, KY: 0}))
    facts["det_m_ratio_is_quadric_ratio_fourth"] = sp.radsimp(
        facts["det_m_values"][2] / facts["det_m_values"][0]
        - (facts["quadric_values"][("I", "I", "1")] / facts["quadric_values"][("I", "1", "1")]) ** 4) == 0
    return facts


# ---------------------------------------------------------------------------
# G. THE CONTROL AND THE OVERLAP ASSEMBLY: where the shape statement fails and
# exactly how; the overlap Bloch fold's parameter dependence at every point;
# the x-axis distinction seen by the bench
# ---------------------------------------------------------------------------
def generic_cell(params: tuple) -> sp.Matrix:
    """Block 214's formal cell at symbolic face signs, moduli and parameters."""
    return b214.formal_cell(dict(zip(FACE_ORDER, SIGN_SYMBOLS)), G0, G1, V0, V1, params)


def parity_block_literals(matrix: sp.Matrix) -> tuple:
    even, odd = b213.even_odd(3)
    entries = matrix.extract(even, odd).applyfunc(sp.expand)
    return tuple(sorted(str(e) for e in set(entries) if e != 0))


def measure_control_overlap(cells: dict, bench: dict) -> dict:
    facts: dict = {}
    points = (("I", "1", "1"), ("1", "I", "1"), ("I", "I", "1"))
    # the all-plus W1 control under the onsite pencil: the rational branch and the irreducible rest
    g1 = b213.metric_candidates(cells["W1 zero"])[0].applyfunc(sp.radsimp)
    facts["w1_g1_plane"] = (g1[0, 0], g1[0, 1], g1[1, 1])
    facts["w1_quadric_values"] = quadric_values(g1, points)
    entry = bench["table"][("W1 line", "onsite", "pencil")]
    facts["w1_shapes"] = {z: entry["block_shapes"][z] for z in points}
    facts["w1_rational_roots"] = {z: entry["block_rational_roots"][z] for z in points}
    facts["w1_multisets_none"] = all(entry["block_multisets"][z] is None for z in points)
    facts["w1_rational_branch_is_quadric"] = all((facts["w1_quadric_values"][z], 2) in facts["w1_rational_roots"][z] for z in points)
    facts["w1_irreducible_degrees"] = {z: tuple(sorted(d for d, _, _ in entry["block_shapes"][z] if d > 1)) for z in points}
    facts["w1_normalized_charpolys"] = {
        z: normalized_monic_charpoly(entry["blocks"][z], facts["w1_quadric_values"][z])
        for z in points
    }
    facts["w1_normalized_t_x_differ"] = (
        sp.expand(facts["w1_normalized_charpolys"][("I", "1", "1")]
                  - facts["w1_normalized_charpolys"][("1", "I", "1")]) != 0
    )
    facts["w1_primitive_shape_divisors"] = {
        z: b217.primitive_shape_divisor(entry["block_shapes"][z]) for z in points
    }
    smallest = {z: min(root for root, _ in facts["w1_rational_roots"][z]) for z in points}
    facts["w1_cross_term_from_rational_branch"] = sp.radsimp(
        (facts["w1_quadric_values"][("I", "I", "1")] - facts["w1_quadric_values"][("I", "1", "1")]
         - facts["w1_quadric_values"][("1", "I", "1")]) / 2)
    facts["w1_rational_branch_reads_g1_tx"] = facts["w1_cross_term_from_rational_branch"] == g1[0, 1]
    facts["w1_pure_points_differ"] = entry["block_shapes"][("I", "1", "1")] != entry["block_shapes"][("1", "I", "1")]
    h0, m, _ = b214.principal_part(cells["W1 line"], "onsite")
    det = sp.radsimp(m.det(method="berkowitz"))
    _, factors = sp.factor_list(det, *KAPPA, extension=sp.sqrt(6))
    facts["w1_det_m_shape"] = tuple(sorted((sp.Poly(f, *KAPPA).total_degree(), p) for f, p in factors))
    facts["w1_det_m_values"] = (det.subs({KT: 1, KX: 0, KY: 0}), det.subs({KT: 1, KX: 1, KY: 0}))
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
    facts["overlap_fold_parameter_free_at_pure_points"] = all(
        fold[z]["parameters_present"] == () for z in (("I", "1", "1"), ("1", "I", "1")))
    facts["overlap_fold_mixed_parameters"] = fold[("I", "I", "1")]["parameters_present"]
    facts["overlap_fold_mixed_parity_block"] = fold[("I", "I", "1")]["parity_block"]
    facts["overlap_fold_zero_parity_block"] = fold[("1", "1", "1")]["parity_block"]
    # the overlap bench at the line point against zero parameters, point by point
    comparison: dict = {}
    for label in ("witness", "W1"):
        for reading in ("form", "pencil"):
            line = bench["table"][(f"{label} line", "overlap", reading)]["blocks"]
            zero = bench["table"][(f"{label} zero", "overlap", reading)]["blocks"]
            comparison[(label, reading)] = {z: sp.expand(line[z] - zero[z]) == 0 for z in line}
    facts["overlap_line_vs_zero"] = comparison
    facts["overlap_line_equals_zero_at_pure_points"] = all(
        comparison[key][z] for key in comparison for z in (("1", "1", "1"), ("I", "1", "1"), ("1", "I", "1")))
    facts["overlap_line_differs_at_mixed_point"] = not any(comparison[key][("I", "I", "1")] for key in comparison)
    # the x-axis distinction: the two pure points against each other
    ms = bench["block_multisets"]
    facts["onsite_witness_pure_points_coincide"] = all(
        ms[("witness line", "onsite", r)][("I", "1", "1")] == ms[("witness line", "onsite", r)][("1", "I", "1")]
        and bench["block_shapes"][("witness line", "onsite", r)][("I", "1", "1")]
        == bench["block_shapes"][("witness line", "onsite", r)][("1", "I", "1")] for r in ("form", "pencil"))
    facts["overlap_witness_pure_points_differ"] = all(
        ms[("witness line", "overlap", r)][("I", "1", "1")] != ms[("witness line", "overlap", r)][("1", "I", "1")]
        for r in ("form", "pencil"))
    facts["overlap_witness_pure_multisets"] = {
        (r, z): ms[("witness line", "overlap", r)][z] for r in ("form", "pencil") for z in (("I", "1", "1"), ("1", "I", "1"))}
    facts["overlap_w1_form_pure_points_coincide"] = (
        ms[("W1 line", "overlap", "form")][("I", "1", "1")] == ms[("W1 line", "overlap", "form")][("1", "I", "1")])
    facts["overlap_w1_pencil_pure_points_differ"] = (
        ms[("W1 line", "overlap", "pencil")][("I", "1", "1")] != ms[("W1 line", "overlap", "pencil")][("1", "I", "1")])
    facts["overlap_w1_pencil_pure_multisets"] = {
        z: ms[("W1 line", "overlap", "pencil")][z] for z in (("I", "1", "1"), ("1", "I", "1"))}
    facts["overlap_witness_mixed_shapes"] = {
        (r, p): bench["block_shapes"][(f"witness {p}", "overlap", r)][("I", "I", "1")]
        for r in ("form", "pencil") for p in ("line", "zero")}
    facts["overlap_witness_mixed_zero_pencil"] = ms[("witness zero", "overlap", "pencil")][("I", "I", "1")]
    return facts


@dataclass(frozen=True)
class Facts:
    authority: AuthorityCertificate
    construction: dict
    bench: dict
    identities: dict
    shape: dict
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
    control = measure_control_overlap(cells, bench)
    lap("control")
    axiom_text = (ROOT / AXIOM_PATH).read_text(encoding="utf-8") if (ROOT / AXIOM_PATH).is_file() else ""
    note_text = NOTE_PATH.read_text(encoding="utf-8") if NOTE_PATH.is_file() else ""
    return Facts(authority, construction, bench, identities, shape, control, axiom_text, note_text, timings)


# ---------------------------------------------------------------------------
# THE DECLARED LITERALS -- every claim is a constant compared against a
# measurement; a mutation rewrites exactly one claim.
# ---------------------------------------------------------------------------
R = sp.Rational
BENCH_MOMENTA = (("1", "1", "1"), ("1", "I", "1"), ("I", "1", "1"), ("I", "I", "1"))   # Block 213's bench_momenta((4,4,2))
BENCH_KAPPAS = ((0, 0, 0), (0, 1, 0), (1, 0, 0), (1, 1, 0))
PARENT_MOMENTA = (("1", "1", "1"), ("I", "1", "1"))                                  # Block 217's BENCH_MOMENTA on (4,2,2)
SITE_COUNT = 32
Y_LINK_ENTRIES = 0                                                                    # the extent-2 direction carries no link
RAISING_BENCH_NNZ = 64
WITNESS_SIGNS = (1, 1, 1, 1, -1, 1)                                                   # Block 213's L+- cell = Block 216's mask 2
LINE_POINT_ENTRIES = (sp.Integer(0), R(1, 4), R(-1, 4), R(1, 4))
G1_TT_WITNESS = R(9, 8)
FLAT_R5 = ((0, 8), (1, 16), (2, 8))                                                   # Block 213's expected_flat_multiset((4,4,2))
CHARPOLY_COUNT = 20
PURE_T, PURE_X, MIXED = ("I", "1", "1"), ("1", "I", "1"), ("I", "I", "1")
NONZERO_POINTS = (PURE_T, PURE_X, MIXED)
WITNESS_PURE_PENCIL = ((R(9, 8), 2), (R(16, 11), 2), (R(18, 11), 4))
WITNESS_MIXED_PENCIL = ((R(3, 2), 2), (R(64, 33), 2), (R(24, 11), 4))
WITNESS_FORM_PURE_SHAPE = ((4, 2, (55296, -388672, 698656, -422145, 69984)),)       # Block 217's quartic, per pure point
WITNESS_FORM_MIXED_SHAPE = ((4, 2, (864, -8096, 19891, -15870, 3456)),)
WITNESS_OVERLAP_FORM_PURE = {PURE_T: ((R(36481, 55296), 4), (R(89401, 55296), 4)),
                             PURE_X: ((R(51529, 55296), 4), (R(69169, 55296), 4))}
WITNESS_OVERLAP_PENCIL_PURE = {PURE_T: ((1, 8),), PURE_X: ((R(227, 263), 4), (R(263, 227), 4))}
WITNESS_OVERLAP_MIXED_SHAPES = {("form", "line"): ((4, 2),), ("form", "zero"): ((2, 4),),
                                ("pencil", "line"): ((2, 4),), ("pencil", "zero"): ((1, 8),)}
WITNESS_OVERLAP_MIXED_PENCIL_LINE = ((2, 4, (17837, -58604, 48020)),)
WITNESS_OVERLAP_MIXED_ZERO_PENCIL = ((R(490, 299), 8),)
W1_PENCIL_SHAPES = {
    PURE_T: ((1, 2, (15, -16)), (3, 2, (4801335, -18293776, 22913024, -9437184))),  # Block 217's cubic
    PURE_X: ((1, 2, (15, -16)), (1, 2, (385, -256)), (2, 2, (12471, -45584, 36864))),
    MIXED: ((1, 2, (5, -8)), (3, 2, (4801335, -27171928, 46940160, -25165824))),
}
W1_IRREDUCIBLE_DEGREES = {PURE_T: (3,), PURE_X: (2,), MIXED: (3,)}
W1_QUADRIC_VALUES = {PURE_T: R(16, 15), PURE_X: R(16, 15), MIXED: R(8, 5)}
W1_G1_PLANE = (R(16, 15), R(-4, 15), R(16, 15))
W1_DET_M_SHAPE = ((2, 2), (2, 2))
W1_DET_M_VALUES = (R(256, 225), R(1024, 225))
W1_OVERLAP_FORM_PURE = ((R(116281, 147456), 4), (R(4844401, 3686400), 4))            # = Block 214's OVERLAP_FORM_W1, both pure points
W1_OVERLAP_PENCIL_PURE = {PURE_T: ((1, 8),), PURE_X: ((R(55, 71), 4), (R(71, 55), 4))}
MONIC_NORMALIZATION_DIVISORS = {
    "witness form pure": sp.Integer(55296) ** 2,
    "witness form mixed": sp.Integer(864) ** 2,
    "witness overlap pencil mixed": sp.Integer(17837) ** 4,
    "W1 pencil pure t": sp.Integer(15 * 4801335) ** 2,
    "W1 pencil pure x": sp.Integer(15 * 385 * 12471) ** 2,
    "W1 pencil mixed": sp.Integer(5 * 4801335) ** 2,
}
BRANCH_CONSTANTS = ((1, 2), (R(128, 99), 2), (R(16, 11), 4))                          # Block 216's L+- line 1/4
QUADRIC_VALUES = {PURE_T: R(9, 8), PURE_X: R(9, 8), MIXED: R(3, 2)}
G1_PLANE = (R(9, 8), R(-3, 8), R(9, 8))
CROSS_TERM = R(-3, 8)
DET_M_SHAPE = ((2, 4),)
DET_M_VALUES = (R(81, 64), R(81, 64), sp.Integer(4))
OVERLAP_FOLD_ZERO_PARITY = ("D07/4 + D16/4 + D25/4 + D34/4",)                         # Block 217's (s/4) P111
OVERLAP_FOLD_MIXED_PARITY = ("-D07/4 - D16/4 + D25/4 + D34/4",)                       # the signed sum at (i, i, 1)
OVERLAP_FOLD_MIXED_PARAMETERS = ("D07", "D16", "D25", "D34")
SCOUT_GRADE_FENCE = ("scout-grade finite exact linear algebra on one cell form, "
                     "not a spacetime and not a dynamics")
SCOUT_GRADE_ONLY = True
INSTANCE_SCOPE = (
    "one cell form: Block 211's family at L+-'s rule-A cell (mask 2) with Block 213's curve moduli, the all-plus W1 and the flat cell as controls; no other cell",
    "two assemblies, two readings, all four run; neither assembly decided, neither reading selected; the parameters at the numeric line point (0, 1/4, -1/4, 1/4) and at zero",
    "one bench, Block 213's bench_matrix at extent (4,4,2): the (t, x) plane sampled at the fine momentum pi/2, the y direction at extent 2 unsampled; no other extent",
    "the cone's shape restricted to the (t, x) plane: three Bloch points fix (G1_tt, G1_tx, G1_xx); G1_ty, G1_xy, G1_yy are not read",
    "the covariance notion: Block 215's (E_R R) H (E_R R)^T = H on the folded H0, measured at Block 216's named finite witnesses; the physical antecedent is not adopted",
    "no dispersion law, no Lorentzian or light-cone reading, no continuum limit, no metric of anything physical; the identity with the principal part is exact and finite, not a limit",
)
INSTANCE_SCOPE_COUNT = 6

N5_FENCE = "N5: The corrected Block 218 claim is finite. On one (4,4,2) bench at the named L+- witness, the onsite pencil block has the stated three normalized branch constants across the sampled t-x points and the mixed-point identity holds. At W1, the normalized monic characteristic polynomials at the pure-t and pure-x points differ even though Q is 16/15 at both; this cross-direction mismatch, rather than any single irrational or rational eigenvalue, is the control result. Primitive factor products are divided by their recorded leading-coefficient products before being called monic characteristic polynomials. No parent theorem, assembly choice, premise adoption, physical metric, cone, action, spacetime, continuum, dispersion law, or dynamics is claimed."


def scope_certificate(text: str) -> dict:
    return {"n5_verbatim": N5_FENCE in text}


def build_claims(mutation: str) -> dict:
    claims = {
        "current_main": CURRENT_MAIN, "parent_commit": PARENT_COMMIT,
        "registered": (), "gravity_supplied": False, "covariance_inherited": False,
        "assembly_decided": False, "cell_selected": False, "reading_selected": False, "continuum_read": False,
        "bench_momenta": BENCH_MOMENTA, "parent_witness_pencil": b217.WITNESS_ONSITE_PENCIL, "flat_r5": FLAT_R5,
        "all_agree": True, "witness_mixed_pencil": WITNESS_MIXED_PENCIL, "w1_pencil_shapes": W1_PENCIL_SHAPES,
        "raising_additive": True, "onsite_similarity": True, "mixed_point_identity": True,
        "shape_visible": True, "cross_term": CROSS_TERM,
        "w1_irreducible_degrees": W1_IRREDUCIBLE_DEGREES, "w1_normalized_t_x_differ": True,
        "overlap_mixed_parity": OVERLAP_FOLD_MIXED_PARITY,
        "overlap_witness_pure_points_differ": True,
        "scout_grade": SCOUT_GRADE_FENCE, "instance_scope_count": INSTANCE_SCOPE_COUNT,
        "n5_verbatim": True, "float_absent": True,
    }
    flips = {
        "stale_main_authority": ("current_main", STALE_MAIN),
        "stale_parent_authority": ("parent_commit", STALE_PARENT_COMMIT),
        "claim_objects_registered": ("registered", ("the cone's shape",)),
        "claim_gravity_supplied": ("gravity_supplied", True),
        "claim_covariance_inherited": ("covariance_inherited", True),
        "claim_assembly_decided": ("assembly_decided", True),
        "claim_cell_selected": ("cell_selected", True),
        "claim_reading_selected": ("reading_selected", True),
        "claim_continuum_read": ("continuum_read", True),
        "break_bench_momenta": ("bench_momenta", BENCH_MOMENTA[:3]),
        "break_witness_reproduction": ("parent_witness_pencil", b217.R5_MULTISET),
        "break_flat_control": ("flat_r5", ((0, 8), (1, 8))),
        "break_bloch_equals_direct": ("all_agree", False),
        "break_witness_multisets": ("witness_mixed_pencil", WITNESS_PURE_PENCIL),
        "break_control_multisets": ("w1_pencil_shapes", {**W1_PENCIL_SHAPES, MIXED: W1_PENCIL_SHAPES[PURE_T]}),
        "break_raising_block_additivity": ("raising_additive", False),
        "break_onsite_similarity": ("onsite_similarity", False),
        "break_mixed_point_identity": ("mixed_point_identity", False),
        "break_cone_shape_visible": ("shape_visible", False),
        "break_cross_term": ("cross_term", -CROSS_TERM),
        "break_control_failure": ("w1_normalized_t_x_differ", False),
        "break_overlap_fold_dependence": ("overlap_mixed_parity", OVERLAP_FOLD_ZERO_PARITY),
        "break_direction_distinction": ("overlap_witness_pure_points_differ", False),
        "break_scout_grade_fence": ("scout_grade", "a spacetime and a dynamics"),
        "break_instance_scope": ("instance_scope_count", 2),
        "drop_n5_fence": ("n5_verbatim", False),
        "break_float_absence": ("float_absent", False),
    }
    if mutation:
        key, value = flips[mutation]
        claims[key] = value
    return claims


def degree_shape(shape: tuple) -> tuple:
    return tuple((degree, power) for degree, power, _ in shape)


def build_checks(facts: Facts, claims: dict) -> Checks:
    checks = Checks()
    au = facts.authority
    checks.check("A-1", "EVERY DECLARED SOURCE, IMPLEMENTATION, AXIOM AND REGISTRY INPUT MATCHES ITS SHA-256 LITERAL",
                 au.all_inputs_content_bound and claims["current_main"] == CORRECTION_SOURCE_BASE)
    checks.check("A-2", "THE CORRECTED BLOCK 217 NOTE AND RUNNER ARE CONTENT-BOUND FINITE SUPPLIERS",
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
    co, be, id_, sh, ct = facts.construction, facts.bench, facts.identities, facts.shape, facts.control
    bm, bs = be["block_multisets"], be["block_shapes"]
    checks.check("C-1", "THE BENCH IS BLOCK 213's bench_matrix AT EXTENT (4,4,2): 32 sites, the y direction carrying no link (0 y-link entries, 64 raising entries), Bloch momenta (1,1,1), (1,i,1), (i,1,1), (i,i,1) -- the MIXED fine point exists; Block 217's (4,2,2) momenta are (1,1,1), (i,1,1)",
                 co["momenta"] == claims["bench_momenta"] == BENCH_MOMENTA and co["kappas"] == BENCH_KAPPAS and co["mixed_point_present"]
                 and co["site_count"] == SITE_COUNT and co["y_link_entries"] == Y_LINK_ENTRIES and co["raising_bench_nnz"] == RAISING_BENCH_NNZ
                 and co["parent_momenta"] == PARENT_MOMENTA == b217.BENCH_MOMENTA)
    checks.check("C-2", "THE WITNESS AND THE CONTROL ARE BLOCKS 216/217's: Block 216's mask-2 rule-A cell carries Block 213's L+- signs (+,+,+,+,-,+), the parameters sit at (0, 1/4, -1/4, 1/4), Block 217's (4,2,2) onsite pencil multiset reproduces with Bloch = direct (the smaller-extent consistency gate), G1_tt = 9/8, W1's moduli are Block 211's",
                 co["witness_values"] == (WITNESS_SIGNS,) and co["witness_is_rule_a"] and co["l_plus_minus_signs"] == WITNESS_SIGNS
                 and co["face_orders_agree"] and co["line_point_entries"] == LINE_POINT_ENTRIES == tuple(LINE_POINT)
                 and co["parent_bench_multiset"] == claims["parent_witness_pencil"] == b217.WITNESS_ONSITE_PENCIL and co["parent_bench_agrees"]
                 and co["g1_tt_witness"] == G1_TT_WITNESS == b217.G1_TT_WITNESS and co["w1_moduli_is_block211"])
    checks.check("C-3", "THE FLAT CONTROL AT ZERO PARAMETERS GIVES R5's MULTISET {0 x8, 1 x16, 2 x8} = Block 213's expected_flat_multiset((4,4,2)) under both assemblies and both readings",
                 be["flat_zero_is_r5"] and be["flat_expected"] == claims["flat_r5"] == FLAT_R5)
    checks.check("D-1", "BLOCH UNION = DIRECT BENCH at every one of the 20 degree-32 charpolys over QQ(sqrt 6) and QQ(sqrt 6, i); the zero Bloch point contributes eight zeros everywhere",
                 claims["all_agree"] and be["all_agree"] and be["all_degree_32"] and be["charpoly_count"] == CHARPOLY_COUNT and be["zero_point_is_eight_zeros"])
    checks.check("D-2", "THE WITNESS BLOCKS: onsite pencil {9/8 x2, 16/11 x2, 18/11 x4} at both pure points and {3/2 x2, 64/33 x2, 24/11 x4} at the mixed point; onsite form Block 217's irreducible quartic squared at the pure points and another at the mixed point; the overlap form and pencil at the pure points as declared; the overlap mixed-point shapes as declared",
                 bm[("witness line", "onsite", "pencil")][PURE_T] == bm[("witness line", "onsite", "pencil")][PURE_X] == WITNESS_PURE_PENCIL
                 and bm[("witness line", "onsite", "pencil")][MIXED] == claims["witness_mixed_pencil"] == WITNESS_MIXED_PENCIL
                 and bs[("witness line", "onsite", "form")][PURE_T] == bs[("witness line", "onsite", "form")][PURE_X] == WITNESS_FORM_PURE_SHAPE
                 and bs[("witness line", "onsite", "form")][MIXED] == WITNESS_FORM_MIXED_SHAPE
                 and {z: bm[("witness line", "overlap", "form")][z] for z in (PURE_T, PURE_X)} == WITNESS_OVERLAP_FORM_PURE
                 and {z: bm[("witness line", "overlap", "pencil")][z] for z in (PURE_T, PURE_X)} == WITNESS_OVERLAP_PENCIL_PURE
                 and {k: degree_shape(v) for k, v in ct["overlap_witness_mixed_shapes"].items()} == WITNESS_OVERLAP_MIXED_SHAPES
                 and bs[("witness line", "overlap", "pencil")][MIXED] == WITNESS_OVERLAP_MIXED_PENCIL_LINE
                 and ct["overlap_witness_mixed_zero_pencil"] == WITNESS_OVERLAP_MIXED_ZERO_PENCIL
                 and b217.primitive_shape_divisor(bs[("witness line", "onsite", "form")][PURE_T])
                 == MONIC_NORMALIZATION_DIVISORS["witness form pure"]
                 and b217.primitive_shape_divisor(bs[("witness line", "onsite", "form")][MIXED])
                 == MONIC_NORMALIZATION_DIVISORS["witness form mixed"]
                 and b217.primitive_shape_divisor(bs[("witness line", "overlap", "pencil")][MIXED])
                 == MONIC_NORMALIZATION_DIVISORS["witness overlap pencil mixed"])
    checks.check("D-3", "THE CONTROL BLOCKS at the all-plus W1: onsite pencil (15 lam - 16)^2 times Block 217's irreducible cubic squared at (i,1,1), (15 lam - 16)^2 (385 lam - 256)^2 times an irreducible quadratic squared at (1,i,1), (5 lam - 8)^2 times an irreducible cubic squared at (i,i,1); overlap form Block 214's OVERLAP_FORM_W1 at both pure points; overlap pencil R5's at (i,1,1) and {55/71 x4, 71/55 x4} at (1,i,1)",
                 ct["w1_shapes"] == claims["w1_pencil_shapes"] == W1_PENCIL_SHAPES
                 and ct["w1_primitive_shape_divisors"] == {
                     PURE_T: MONIC_NORMALIZATION_DIVISORS["W1 pencil pure t"],
                     PURE_X: MONIC_NORMALIZATION_DIVISORS["W1 pencil pure x"],
                     MIXED: MONIC_NORMALIZATION_DIVISORS["W1 pencil mixed"],
                 }
                 and bm[("W1 line", "overlap", "form")][PURE_T] == bm[("W1 line", "overlap", "form")][PURE_X] == W1_OVERLAP_FORM_PURE == b214.OVERLAP_FORM_W1[1:]
                 and ct["overlap_w1_pencil_pure_multisets"] == W1_OVERLAP_PENCIL_PURE)
    checks.check("E-1", "THE RAISING BLOCH BLOCK IS i D(kappa_z) AT EVERY POINT, MEASURED FIRST: d_B(z) = sum_mu (z_mu - 1/z_mu)/2 D(e_mu) at symbolic z (the fine momenta enter additively; at the mixed point i D(e_t + e_x)); D(e_mu)^2 = 0, the D(e_mu) anticommute, D(e_t + e_x)^2 = 0",
                 all(id_["raising_block_is_i_d"].values()) and claims["raising_additive"] and id_["raising_block_additive_symbolic"]
                 and id_["d_mu_squared_zero"] and id_["d_mu_anticommute"] and id_["d_mixed_squared_zero"])
    checks.check("E-2", "THE ONSITE HODGE BLOCH BLOCK IS Z^-1 H0 Z with Z = diag(z^c) at every point, at the witness, the control and the flat cell",
                 claims["onsite_similarity"] and id_["onsite_similarity_everywhere"])
    checks.check("E-3", "THE IDENTITY WITH THE PRINCIPAL PART: the onsite pencil block charpoly equals the charpoly of (H0^-1 M(kappa_z))^2 at EVERY point -- the MIXED point with kappa = e_t + e_x included -- at the witness, the control and the flat cell; it fails for the form reading and for the overlap assembly at every nonzero point of the witness and the control",
                 claims["mixed_point_identity"] and id_["onsite_pencil_identity_everywhere"] and all(id_["mixed_point_identity"].values())
                 and id_["form_fails_at_every_nonzero_point"] and id_["overlap_fails_at_every_nonzero_point"])
    checks.check("F-1", "THE CONE'S SHAPE IS VISIBLE at the witness: at each of the three nonzero points every nonzero eigenvalue is a Block 216 branch constant {1, 128/99, 16/11 x2} times k^T G1 k at kappa_z, the quadric values 9/8, 9/8, 3/2; G1's (t, x)-plane restriction is (9/8, -3/8, 9/8)",
                 claims["shape_visible"] and sh["shape_visible"] and sh["predicted_equal_measured"] and sh["constants"] == BRANCH_CONSTANTS
                 and sh["quadric_values"] == QUADRIC_VALUES and sh["g1_plane"] == G1_PLANE)
    checks.check("F-2", "THE CROSS TERM IS ISOLATED FROM THE THREE POINTS: (Q_mixed - Q_t - Q_x)/2 = -3/8 = G1_tx read from the bench alone; the pure points coincide; det M on the line is one quadric to the fourth power with 81/64, 81/64, 4 at e_t, e_x, e_t + e_x, the ratio (Q_mixed/Q_t)^4",
                 sh["cross_term_bench"] == claims["cross_term"] == CROSS_TERM and sh["cross_term_equals_g1"] and sh["pure_points_coincide"]
                 and sh["det_m_shape"] == DET_M_SHAPE and sh["det_m_values"] == DET_M_VALUES and sh["det_m_ratio_is_quadric_ratio_fourth"])
    checks.check("G-1", "THE W1 CONTROL HAS NO COMMON NORMALIZED MONIC SPECTRUM ACROSS PURE t AND PURE x: Q=16/15 AT BOTH, BUT THE COMPLETE NORMALIZED POLYNOMIALS DIFFER; the rational Q branch and recorded primitive factor shapes are retained",
                 id_["mixed_point_identity"]["W1 line"] and ct["w1_multisets_none"]
                 and ct["w1_rational_branch_is_quadric"]
                 and ct["w1_irreducible_degrees"] == W1_IRREDUCIBLE_DEGREES
                 and ct["w1_quadric_values"] == W1_QUADRIC_VALUES
                 and ct["w1_g1_plane"] == W1_G1_PLANE and ct["w1_rational_branch_reads_g1_tx"]
                 and claims["w1_normalized_t_x_differ"] and ct["w1_normalized_t_x_differ"]
                 and ct["w1_pure_points_differ"] and ct["w1_det_m_shape"] == W1_DET_M_SHAPE
                 and ct["w1_det_m_values"] == W1_DET_M_VALUES)

    checks.check("G-2", "THE OVERLAP FOLD'S PARAMETER DEPENDENCE, POINT BY POINT, at symbolic signs, moduli and parameters: parameter-free at both pure points; at the mixed point all four parameters through the signed sum (-D07 - D16 + D25 + D34)/4 on the parity block (Block 217's (D07 + D16 + D25 + D34)/4 at the zero point); the overlap bench at the line point equals the zero-parameter one at the pure points and differs at the mixed point, form and pencil, witness and control",
                 ct["overlap_fold_parameter_free_at_pure_points"] and ct["overlap_fold_mixed_parameters"] == OVERLAP_FOLD_MIXED_PARAMETERS
                 and ct["overlap_fold_mixed_parity_block"] == claims["overlap_mixed_parity"] == OVERLAP_FOLD_MIXED_PARITY
                 and ct["overlap_fold_zero_parity_block"] == OVERLAP_FOLD_ZERO_PARITY
                 and ct["overlap_line_equals_zero_at_pure_points"] and ct["overlap_line_differs_at_mixed_point"])
    checks.check("G-3", "THE SECOND DIRECTION SEES THE x-AXIS DISTINCTION: at the witness the onsite blocks at (i,1,1) and (1,i,1) coincide while the overlap blocks differ (form {36481/55296, 89401/55296} against {51529/55296, 69169/55296}; pencil R5's against {227/263, 263/227}); at W1 the overlap form coincides and the overlap pencil differs",
                 ct["onsite_witness_pure_points_coincide"] and claims["overlap_witness_pure_points_differ"] and ct["overlap_witness_pure_points_differ"]
                 and ct["overlap_witness_pure_multisets"] == {("form", PURE_T): WITNESS_OVERLAP_FORM_PURE[PURE_T], ("form", PURE_X): WITNESS_OVERLAP_FORM_PURE[PURE_X],
                                                              ("pencil", PURE_T): WITNESS_OVERLAP_PENCIL_PURE[PURE_T], ("pencil", PURE_X): WITNESS_OVERLAP_PENCIL_PURE[PURE_X]}
                 and ct["overlap_w1_form_pure_points_coincide"] and ct["overlap_w1_pencil_pure_points_differ"])
    checks.check("H-1", "FINITE-SCOPE FENCE AGREES WITH THE CORRECTED SUPPLIERS",
                 claims["scout_grade"] == SCOUT_GRADE_FENCE == b217.SCOUT_GRADE_FENCE and SCOUT_GRADE_ONLY)
    checks.check("H-2", "THE INSTANCE SCOPE IS ENUMERATED: six restrictions",
                 claims["instance_scope_count"] == len(INSTANCE_SCOPE) == 6)
    sc = scope_certificate(facts.note_text)
    checks.check("I-1", "THE NOTE IS PRESENT AND CARRIES THE N5 FENCE BYTE-IDENTICALLY",
                 bool(facts.note_text) and sc["n5_verbatim"] == claims["n5_verbatim"] and claims["n5_verbatim"])
    checks.check("I-2", "NO nsimplify, NO float literal, NO float call in this runner's source",
                 nsimplify_occurrences() == 0 and float_literal_occurrences() == 0 and float_call_sites() == 0 and claims["float_absent"])
    return checks


def report_measured(facts: Facts, elapsed_ns: int) -> None:
    print("== BLOCK 218: corrected finite two-direction bench -- measured facts ==")
    print(f"authority: {facts.authority}")
    for name in ("construction", "bench", "identities", "shape", "control"):
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
