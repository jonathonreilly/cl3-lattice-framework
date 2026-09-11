#!/usr/bin/env python3
"""Corrected Block 215 finite proper-cubic covariance calculation.

The runner builds the 24 proper signed rotations and their exterior lifts,
measures exact strict and corner-sign-twisted covariance loci of one supplied
eight-corner cell family, verifies the exterior-star line, and scans the
finite sign-cell controls.  Covariance means only the displayed matrix
identity.  No inherited physical symmetry, premise, subgroup, assembly,
metric, action, continuum, spacetime, or dynamics is supplied or selected.

The historical Block 201 dependency is replaced by a bounded helper containing
only the determinant-one signed-permutation construction.  Corrected Blocks
213 and 214 supply the finite matrices and are byte-bound below; their broader
claims are not adopted.
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
from types import SimpleNamespace

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

# Reviewed finite suppliers.  The group helper replaces the one function used
# from historical Block 201; no historical theorem is imported.
try:
    import admissibility_dirac_kahler_duality_parameters_principal_part_2026_09_05 as b214
    B214_IMPORT_AVAILABLE = True
except ModuleNotFoundError:                            # pragma: no cover
    b214 = None
    B214_IMPORT_AVAILABLE = False
try:
    import admissibility_dirac_kahler_released7992_7994_group_fixture_2026_09_10 as b201
    GROUP_HELPER_IMPORT_AVAILABLE = True
except ModuleNotFoundError:                            # pragma: no cover
    b201 = None
    GROUP_HELPER_IMPORT_AVAILABLE = False
b213 = b214.b213 if b214 is not None else None
b211 = (SimpleNamespace(**vars(b214.b211), GAUGE_FACE_ORDER=b201.GAUGE_FACE_ORDER)
        if b214 is not None and b201 is not None else None)
b209 = (SimpleNamespace(**vars(b214.b209), CORNER_DEGREE=b201.CORNER_DEGREE)
        if b214 is not None and b201 is not None else None)
MACHINERY_IMPORT_LANDED = bool(
    B214_IMPORT_AVAILABLE and GROUP_HELPER_IMPORT_AVAILABLE
    and b214 is not None and b214.MACHINERY_IMPORT_AVAILABLE
    and b201 is not None and b201.supplier_certificate()
    and b213 is not None and b211 is not None and b209 is not None
)

FINAL_NOTE_NAME = (
    "ADMISSIBILITY_DIRAC_KAHLER_DUALITY_COVARIANCE_LOCUS_BOUNDED_THEOREM_"
    "NOTE_2026-09-05.md"
)
NOTE_PATH = ROOT / "docs" / FINAL_NOTE_NAME
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"

B214_NOTE = "docs/ADMISSIBILITY_DIRAC_KAHLER_DUALITY_PARAMETERS_PRINCIPAL_PART_BOUNDED_THEOREM_NOTE_2026-09-05.md"
B214_RUNNER = "scripts/admissibility_dirac_kahler_duality_parameters_principal_part_2026_09_05.py"
B213_NOTE = "docs/ADMISSIBILITY_DIRAC_KAHLER_WEIGHTED_KERNEL_DISPERSION_BOUNDED_THEOREM_NOTE_2026-09-05.md"
B213_RUNNER = "scripts/admissibility_dirac_kahler_weighted_kernel_dispersion_2026_09_05.py"
PARENT_NOTE = B214_NOTE
PARENT_RUNNER = B214_RUNNER
PARENT_ARTIFACTS = (PARENT_NOTE, PARENT_RUNNER)
GROUP_HELPER_PATH = "scripts/admissibility_dirac_kahler_released7992_7994_group_fixture_2026_09_10.py"
B213_HELPER_PATH = "scripts/admissibility_dirac_kahler_weighted_kernel_released7981_7988_fixtures_2026_09_10.py"
B105_NOTE = "docs/ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md"
B105_RUNNER = "scripts/admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_2026_08_14.py"

# Complete literal runtime and citation closure.  The notes identify fixed
# finite formulas; they do not promote parent theorem conclusions to premises.
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_DUALITY_COVARIANCE_LOCUS_BOUNDED_THEOREM_NOTE_2026-09-05.md",
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
    AUDIT_INPUT_PATHS[0]: "bf50cb757c46f79fbd612d9f3d2a0edbb68f238092595fb86f21feead673ffbf",
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
SUPPLIER_FREEZE_COMMIT = "2e60673f8d1668fd229f02096b79c78eda65de5f"
CURRENT_MAIN = SOURCE_BASE_COMMIT
PARENT_COMMIT = SUPPLIER_FREEZE_COMMIT
STALE_MAIN = "historical-moving-main-guard"
STALE_PARENT_COMMIT = "historical-parent-guard"

MUTATIONS = (
    "stale_main_authority",
    "stale_parent_authority",
    "claim_objects_registered",
    "claim_gravity_supplied",
    "claim_covariance_inherited",
    "claim_subgroup_selected",
    "claim_assembly_decided",
    "break_representation_orders",
    "break_intertwining",
    "break_subgroup_class_count",
    "break_gauge_congruence",
    "break_star_signs",
    "break_star_line",
    "break_twisted_census",
    "break_strict_census",
    "claim_shears_killed_by_twisted_covariance",
    "break_p111_commutation",
    "break_overlap_locus",
    "claim_positivity_selects_plane",
    "claim_parity_selects_plane",
    "break_flat_cell_loci",
    "break_strict_s3_cells",
    "break_star_pattern_cells",
    "break_scout_grade_fence",
    "break_instance_scope",
    "drop_n5_fence",
    "break_float_absence",
)
MUTATION_GATE = {
    "stale_main_authority": "A", "stale_parent_authority": "A",
    "claim_objects_registered": "B", "claim_gravity_supplied": "B",
    "claim_covariance_inherited": "B", "claim_subgroup_selected": "B",
    "claim_assembly_decided": "B",
    "break_representation_orders": "C", "break_intertwining": "C",
    "break_subgroup_class_count": "C", "break_gauge_congruence": "C",
    "break_star_signs": "D", "break_star_line": "D",
    "break_twisted_census": "E", "break_strict_census": "E",
    "claim_shears_killed_by_twisted_covariance": "E",
    "break_p111_commutation": "F", "break_overlap_locus": "F",
    "claim_positivity_selects_plane": "G", "claim_parity_selects_plane": "G",
    "break_flat_cell_loci": "G", "break_strict_s3_cells": "G", "break_star_pattern_cells": "G",
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
    helper_content_bound: bool
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
        actual.get(GROUP_HELPER_PATH, "") == INPUT_SHA256[GROUP_HELPER_PATH],
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
    "Block 211's six-face-compatible cell-form family with its ties, four gauge classes and four free duality parameters",
    "Block 211's corner-sign gauge D -> E D E (64 sign vectors, four classes)",
    "the 24 proper cubic rotations (Block 201's signed permutations, det = +1) and the corner action BUILT HERE",
    "Block 105's two assemblies (onsite, overlap) through Block 213/214's rules",
    "Block 214's plane D16 = D34 = -D25 and its facts F-1..F-4 (the loci whose name is sought)",
)
REGISTERED_OBJECTS = ()
ADOPTED_OBJECTS = ()
GRAVITY_SUPPLIED_CLAIMED = False
COVARIANCE_INHERITED_CLAIMED = False
SUBGROUP_SELECTED_CLAIMED = False
ASSEMBLY_DECIDED_CLAIMED = False
PARAMETER_VALUE_SELECTED_CLAIMED = False
READINGS_LICENSED_CLAIMED = False
CONTINUUM_LIMIT_CLAIMED = False
CONE_IS_SPACETIME_CONE_CLAIMED = False
UNSUPPLIED_GRAVITY_STRUCTURES = (
    "lapse function", "shift vector", "ADM phase space", "Hamiltonian constraint",
    "momentum/diffeomorphism constraint", "first-class constraint algebra",
    "Dirac closure", "Dirac observable", "gauge orbit and its quotient",
)
SCOPED_HEADLINE_WORDS = ("COVARIANCE", "LOCUS", "STAR", "GAUGE", "PLANE")
AXIOM_COVARIANCE_CLAUSE = ("There is one fixed nearest-neighbor admissibility rule, covariant under lattice\n"
                           "translations and proper cubic rotations.")
READINGS = (
    "R1 the cell form inherits the Admissibility axiom's proper-cubic-rotation covariance (the antecedent; not established, not asserted)",
    "R2 the plane D16 = D34 = -D25 is preferred because it is the star line (not established: only the conditional is claimed)",
    "R3 the full group O is 'the' symmetry of the cell form (not established: no subgroup is selected)",
    "R4 the sign gauge is a physical gauge symmetry (not established: it is Block 211's congruence of one solved system)",
    "R5 the star line is a light-cone or a metric statement (not established: the cone is a polynomial identity)",
    "R6 strict covariance killing the shears means the curved family is unphysical (not established: no dynamics, no selection)",
)
HISTORICAL_REVIEW_RECORD = "PRESERVED-NOT-CURRENT-EVIDENCE"

# the parameters, the corners and the moduli
PARAMETER_NAMES = ("D07", "D16", "D25", "D34")
PARAMETER_SYMBOLS = sp.symbols(" ".join(PARAMETER_NAMES))
A07, B16, C25, D34 = PARAMETER_SYMBOLS
G0, G1, V0, V1 = sp.symbols("g0 g1 v0 v1")
MODULI = (G0, G1, V0, V1)
SUM = sp.Symbol("s")
KT, KX, KY = b213.KT, b213.KX, b213.KY
KAPPA = (KT, KX, KY)
CORNERS = b209.CORNERS
DEGREE_INDICES = b209.DEGREE_INDICES
PAIRS = ((0, 7), (1, 6), (2, 5), (4, 3))
DIRECTION_NAMES = ("t", "x", "y")
GAUGE_CLASSES = ((1, 1), (1, -1), (-1, 1), (-1, -1))
QUARTER = sp.Rational(1, 4)

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


def corner_index(corner: tuple) -> int:
    return CORNERS.index(tuple(corner))


# ---------------------------------------------------------------------------
# C. THE ROTATIONS, THE WEDGE, THE CORNER ACTION -- built here, then verified
# ---------------------------------------------------------------------------
def rotations() -> tuple:
    """Block 201's signed 3 x 3 permutation matrices with det = +1: the
    proper cubic rotations of the direction space (t, x, y)."""
    return tuple(sp.ImmutableMatrix(m) for m in b201.signed_permutations())


def raising_matrix() -> sp.Matrix:
    return b214.raising_matrix()


def unit_raising(direction: int) -> sp.Matrix:
    """D(e_mu): the raising part at the unit vector kappa = e_mu -- left
    multiplication by the basis 1-form of that direction, read off the lane's
    own D(kappa) and nothing else."""
    point = {k: (1 if i == direction else 0) for i, k in enumerate(KAPPA)}
    return raising_matrix().subs(point)


def wedge_rule() -> dict:
    """THE LANE'S WEDGE SIGNATURE, MEASURED FROM D: for each direction mu and
    each corner c without mu, the sign of D(e_mu)[c + e_mu, c]."""
    rule = {}
    for mu in range(3):
        d = unit_raising(mu)
        for c in CORNERS:
            if c[mu] == 1:
                continue
            target = tuple(c[k] + (1 if k == mu else 0) for k in range(3))
            rule[(mu, c)] = d[corner_index(target), corner_index(c)]
    return rule


def ordered_monomial_sign(mu: int, c: tuple) -> int:
    """The sign of e_mu ^ e_c in the ORDERED monomial basis t < x < y: minus
    one for every occupied direction of c before mu."""
    return (-1) ** sum(c[:mu])


def corner_action(rotation: sp.Matrix) -> sp.Matrix:
    """L(R) e_c = (R e_mu1) ^ (R e_mu2) ^ ... for c = {mu1 < mu2 < ...}: the
    multiplicative extension of the direction action THROUGH THE LANE'S WEDGE
    (products of D(e_mu) applied to the empty corner), so every sign is the
    lane's own."""
    unit = [unit_raising(mu) for mu in range(3)]
    images = [sum((rotation[nu, mu] * unit[nu] for nu in range(3)), sp.zeros(8, 8)) for mu in range(3)]
    lifted = sp.zeros(8, 8)
    vacuum = sp.zeros(8, 1)
    vacuum[0, 0] = 1
    for c in CORNERS:
        vector = vacuum
        for mu in reversed([mu for mu in range(3) if c[mu] == 1]):
            vector = images[mu] * vector
        lifted[:, corner_index(c)] = vector
    return sp.ImmutableMatrix(lifted)


def direction_map(rotation: sp.Matrix) -> tuple:
    """(pi, s): column mu of R has its nonzero at row pi(mu) with sign s_mu."""
    pi, signs = [], []
    for mu in range(3):
        nu = [n for n in range(3) if rotation[n, mu] != 0][0]
        pi.append(nu)
        signs.append(int(rotation[nu, mu]))
    return tuple(pi), tuple(signs)


def orientation_lift(rotation: sp.Matrix) -> sp.Matrix:
    """THE SIGN RULE, STATED: L(R) e_c = (prod of the direction signs on c) x
    (sign of the permutation sorting the image directions) e_{R c}.  Compared
    against the wedge construction at gate C-2."""
    pi, signs = direction_map(rotation)
    lifted = sp.zeros(8, 8)
    for c in CORNERS:
        occupied = [mu for mu in range(3) if c[mu] == 1]
        image = [pi[mu] for mu in occupied]
        sign = 1
        for mu in occupied:
            sign *= signs[mu]
        for i in range(len(image)):
            for j in range(i + 1, len(image)):
                if image[i] > image[j]:
                    sign = -sign
        target = tuple(1 if nu in image else 0 for nu in range(3))
        lifted[corner_index(target), corner_index(c)] = sign
    return sp.ImmutableMatrix(lifted)


def monomial_intertwiners(rotation: sp.Matrix) -> tuple:
    """MEASURE the sign rule instead of guessing it: among the 256 signed
    versions of the corner permutation of R, exactly those satisfying
    T D(kappa) T^-1 = D(R kappa) -- expected to be +-L(R) and nothing else."""
    lifted = corner_action(rotation)
    permutation = lifted.applyfunc(abs)
    dk = raising_matrix()
    rotated = dk.subs({k: sum(rotation[i, j] * KAPPA[j] for j in range(3)) for i, k in enumerate(KAPPA)},
                      simultaneous=True)
    found = []
    for signs in itertools.product((1, -1), repeat=8):
        t = sp.diag(*signs) * permutation
        if residual_count((t * dk * t.T - rotated).applyfunc(sp.expand)) == 0:
            found.append(sp.ImmutableMatrix(t))
    return tuple(found)


def matrix_order(matrix: sp.Matrix) -> int:
    power = matrix
    for n in range(1, 25):
        if power == sp.eye(8):
            return n
        power = power * matrix
    return 0


def axis_type(rotation: sp.Matrix) -> str:
    """The rotation axis from the +1 eigenspace: face (a coordinate axis),
    edge (two nonzero coordinates) or body (the diagonal)."""
    space = (rotation - sp.eye(3)).nullspace()
    if len(space) == 3:
        return "identity"
    vector = space[0]
    return {1: "face", 2: "edge", 3: "body"}[sum(1 for x in vector if x != 0)]


# ---------------------------------------------------------------------------
# the group: multiplication table, subgroups, conjugacy classes -- COMPUTED
# ---------------------------------------------------------------------------
def group_table(lifts: tuple) -> tuple:
    """The 24 x 24 multiplication table of the lifted matrices (closure and
    the identity are measured, not assumed)."""
    index = {m: i for i, m in enumerate(lifts)}
    table = []
    for a in lifts:
        row = []
        for b in lifts:
            product = sp.ImmutableMatrix(a * b)
            row.append(index.get(product, -1))
        table.append(tuple(row))
    return tuple(table)


def closure(table: tuple, generators: frozenset, identity: int) -> frozenset:
    elements = {identity} | set(generators)
    frontier = list(elements)
    while frontier:
        g = frontier.pop()
        for h in list(elements):
            for product in (table[g][h], table[h][g]):
                if product not in elements:
                    elements.add(product)
                    frontier.append(product)
    return frozenset(elements)


def all_subgroups(table: tuple, identity: int) -> tuple:
    """Closures of every pair of elements, deduplicated; then the completeness
    certificate: adjoining any element to any listed subgroup and closing gives
    a listed subgroup (so every subgroup, generated element by element, is
    listed)."""
    n = len(table)
    found = set()
    for i in range(n):
        for j in range(n):
            found.add(closure(table, frozenset((i, j)), identity))
    complete = all(closure(table, s | {g}, identity) in found for s in found for g in range(n))
    return tuple(sorted(found, key=lambda s: (len(s), sorted(s)))), complete


def inverse_of(table: tuple, g: int, identity: int) -> int:
    return [h for h in range(len(table)) if table[g][h] == identity][0]


def conjugacy_classes(table: tuple, subgroups: tuple, identity: int) -> tuple:
    n = len(table)
    classes, seen = [], set()
    for s in subgroups:
        if s in seen:
            continue
        orbit = set()
        for g in range(n):
            ginv = inverse_of(table, g, identity)
            orbit.add(frozenset(table[table[g][h]][ginv] for h in s))
        seen |= orbit
        classes.append(tuple(sorted(orbit, key=sorted)))
    return tuple(classes)


def class_signature(subgroup: frozenset, orders: tuple, axes: tuple) -> tuple:
    """The multiset of (element order, axis type) -- the geometric label of a
    subgroup class, computed from its elements."""
    return tuple(sorted((orders[g], axes[g]) for g in subgroup))


SIGNATURE_NAMES = {
    ((1, "identity"),): "1",
    ((1, "identity"), (2, "face")): "C2_face",
    ((1, "identity"), (2, "edge")): "C2_edge",
    ((1, "identity"), (3, "body"), (3, "body")): "C3_body",
    ((1, "identity"), (2, "face"), (4, "face"), (4, "face")): "C4_face",
    ((1, "identity"), (2, "face"), (2, "face"), (2, "face")): "V4_faces",
    ((1, "identity"), (2, "edge"), (2, "edge"), (2, "face")): "V4_face_edges",
    ((1, "identity"), (2, "edge"), (2, "edge"), (2, "edge"), (3, "body"), (3, "body")): "S3_body",
    ((1, "identity"), (2, "edge"), (2, "edge"), (2, "face"), (2, "face"), (2, "face"), (4, "face"), (4, "face")): "D4_face",
    tuple(sorted([(1, "identity")] + [(2, "face")] * 3 + [(3, "body")] * 8)): "T",
    tuple(sorted([(1, "identity")] + [(2, "face")] * 3 + [(3, "body")] * 8 + [(2, "edge")] * 6 + [(4, "face")] * 6)): "O",
}


# ---------------------------------------------------------------------------
# D. THE STAR, derived from the lane's wedge
# ---------------------------------------------------------------------------
def hodge_star() -> sp.Matrix:
    """* e_c = sign e_{c-bar} with the sign fixed by e_c ^ (* e_c) = e_{txy}
    (the volume form = the full corner with coefficient +1), the wedge being
    the products of the lane's D(e_mu) -- no sign is assumed."""
    unit = [unit_raising(mu) for mu in range(3)]
    star = sp.zeros(8, 8)
    for c in CORNERS:
        complement = tuple(1 - x for x in c)
        vector = sp.zeros(8, 1)
        vector[corner_index(complement), 0] = 1
        for mu in reversed([mu for mu in range(3) if c[mu] == 1]):
            vector = unit[mu] * vector
        star[corner_index(complement), corner_index(c)] = vector[7, 0]
    return sp.ImmutableMatrix(star)


def degree_projector(degree: int) -> sp.Matrix:
    p = sp.zeros(8, 8)
    for i in DEGREE_INDICES[degree]:
        p[i, i] = 1
    return p


def star_facts(lifts: tuple) -> dict:
    star = hodge_star()
    dk = raising_matrix()
    facts: dict = {"star_signs": tuple(int(star[corner_index(tuple(1 - x for x in c)), corner_index(c)]) for c in CORNERS)}
    facts["star_squares"] = tuple(int((star * star * degree_projector(k))[DEGREE_INDICES[k][0], DEGREE_INDICES[k][0]]) for k in range(4))
    facts["star_square_is_scalar"] = residual_count(star * star - sp.diag(*[facts["star_squares"][b209.CORNER_DEGREE[i]] for i in range(8)])) == 0
    # * D(kappa) = eps_k D(kappa)^T * on k-forms, the sign measured per degree
    adjoint_signs = []
    for k in range(3):
        left = (star * dk * degree_projector(k)).applyfunc(sp.expand)
        right = (dk.T * star * degree_projector(k)).applyfunc(sp.expand)
        sign = [e for e in (1, -1) if residual_count((left - e * right).applyfunc(sp.expand)) == 0]
        adjoint_signs.append(sign[0] if sign else 0)
    facts["star_adjoint_signs"] = tuple(adjoint_signs)
    facts["star_commutes_with_every_lift"] = all(residual_count(L * star - star * L) == 0 for L in lifts)
    p111 = b214.hodge_complement_permutation()
    facts["p111_is_unsigned_star"] = residual_count(p111 - star.applyfunc(abs)) == 0
    twists = []
    for L in lifts:
        twist = L * p111 * L.T
        diagonal = (twist * p111).applyfunc(sp.expand)
        twists.append(tuple(int(diagonal[i, i]) for i in range(8)) if residual_count(twist.applyfunc(abs) - p111) == 0 else None)
    facts["p111_twists"] = tuple(twists)
    facts["p111_commutes_with_lift_count"] = sum(1 for t in twists if t == (1,) * 8)
    facts["p111_commutes_with_unsigned_permutation"] = all(
        residual_count(P * p111 - p111 * P) == 0 for P in (L.applyfunc(abs) for L in lifts))
    # the 1 <-> 2 block of the star on the duality pairs (1,6), (2,5), (4,3)
    facts["star_pair_signs"] = tuple(int(star[j, i]) for i, j in PAIRS)
    return facts


# ---------------------------------------------------------------------------
# the family, the gauge, the locus machinery
# ---------------------------------------------------------------------------
def family(class_key: tuple, params: tuple, moduli: tuple = MODULI) -> sp.Matrix:
    g0, g1, v0, v1 = moduli
    return b214.formal_cell(b211.REPRESENTATIVES[class_key], g0, g1, v0, v1, params)


def sign_vectors() -> tuple:
    """Block 211's 64 corner-sign vectors: the six middle corners free, the
    empty and the full corner fixed at +1."""
    out = []
    for signs in itertools.product((1, -1), repeat=6):
        e = [1] * 8
        for k, i in enumerate((1, 2, 4, 3, 5, 6)):
            e[i] = signs[k]
        out.append(tuple(e))
    return tuple(out)


def canonical_subspace(rows: list, unknowns: tuple):
    """The linear ideal generated by the rows, as the RREF of the coefficient
    matrix -- a canonical form, so equal subspaces compare equal."""
    if not rows:
        return ()
    matrix = sp.Matrix(rows)
    reduced, pivots = matrix.rref()
    return tuple(tuple(reduced[i, j] for j in range(len(unknowns))) for i in range(len(pivots)))


def subspace_contains(inner, outer) -> bool:
    """V(inner) is a subset of V(outer): every generator of `outer` lies in the
    row space of `inner`."""
    if not outer:
        return True
    if not inner:
        return False
    a = sp.Matrix(list(inner))
    b = sp.Matrix(list(inner) + list(outer))
    return a.rank() == b.rank()


def constraints(h: sp.Matrix, lift: sp.Matrix, e: tuple, unknowns: tuple) -> tuple:
    """(forced moduli conditions, parameter subspace) for T = E L: the entries
    of T H T^T - H, each either a parameter-linear form (collected) or a
    moduli-only expression (which forces a condition on the moduli)."""
    # T = E L is a signed permutation: T e_i = eps_i e_{p(i)} with eps_i the
    # lift's sign at column i times e at the target, so (T H T^T)[p(i), p(j)]
    # = eps_i eps_j H[i, j] -- the congruence entry by entry, no products.
    p = [next(r for r in range(8) if lift[r, i] != 0) for i in range(8)]
    eps = [int(lift[p[i], i]) * e[p[i]] for i in range(8)]
    rows, forced = [], set()
    for i in range(8):
        for j in range(i, 8):
            if h[i, j] == 0 and h[p[i], p[j]] == 0:
                continue
            entry = sp.expand(eps[i] * eps[j] * h[i, j] - h[p[i], p[j]])
            if entry == 0:
                continue
            if not (entry.free_symbols & set(unknowns)):
                # a moduli-only entry forces its numerator's non-numeric
                # factors to vanish (the denominators are volumes, nonzero)
                # and the volumes are nonzero on Block 211's domain, so they drop
                numerator, _ = sp.fraction(sp.factor(entry))
                _, factors = sp.factor_list(numerator)
                forced.add("*".join(sorted(str(base) for base, _ in factors if base not in (V0, V1))))
                continue
            poly = sp.Poly(entry, *unknowns)
            if poly.total_degree() != 1 or (poly.free_symbols - set(unknowns)):
                forced.add("NONLINEAR:" + str(entry))
                continue
            rows.append([poly.coeff_monomial(u) for u in unknowns])
    return frozenset(forced), canonical_subspace(rows, unknowns)


def irredundant(components: list) -> tuple:
    """Drop every component contained in another: (F, V) is inside (F', V')
    when F' is a subset of F and V is a subset of V'."""
    kept = []
    for f, v in components:
        dominated = any((f2 <= f and subspace_contains(v, v2)) and (f2, v2) != (f, v)
                        for f2, v2 in components)
        if not dominated and (f, v) not in kept:
            kept.append((f, v))
    return tuple(sorted(kept, key=lambda fv: (sorted(fv[0]), fv[1])))


def intersect(left: tuple, right: tuple, unknowns: tuple) -> tuple:
    out = []
    for f1, v1 in left:
        for f2, v2 in right:
            out.append((f1 | f2, canonical_subspace([list(r) for r in v1 + v2], unknowns)))
    return irredundant(out)


def per_rotation_loci(h: sp.Matrix, lifts: tuple, unknowns: tuple, twisted: bool) -> tuple:
    """For every rotation, the union of components over the admissible sign
    vectors (twisted) or over E = 1 alone (strict)."""
    vectors = sign_vectors() if twisted else ((1,) * 8,)
    return tuple(irredundant([constraints(h, L, e, unknowns) for e in vectors]) for L in lifts)


def subgroup_locus(per_rotation: tuple, subgroup: frozenset, unknowns: tuple) -> tuple:
    result = ((frozenset(), ()),)
    for g in sorted(subgroup):
        result = intersect(result, per_rotation[g], unknowns)
    return result


def describe(components: tuple, unknowns: tuple) -> tuple:
    """A printable literal: each component as (forced conditions, generators)."""
    out = []
    for f, v in components:
        generators = tuple(str(sp.expand(sum(coefficient * u for coefficient, u in zip(row, unknowns)))) for row in v)
        out.append((tuple(sorted(f)), generators))
    return tuple(out)


# ---------------------------------------------------------------------------
# THE MEASUREMENTS -- every fact once, before any mutation flag is read
# ---------------------------------------------------------------------------
def measure_group() -> dict:
    """C: the 24 rotations, the corner action as a representation, the sign
    rule measured, the intertwining, the subgroup classes computed."""
    rots = rotations()
    lifts = tuple(corner_action(R) for R in rots)
    facts: dict = {"rotation_count": len(rots), "all_det_one": all(R.det() == 1 for R in rots)}
    facts["distinct_lifts"] = len(set(lifts))
    table = group_table(lifts)
    facts["closed"] = all(x >= 0 for row in table for x in row)
    identity = lifts.index(sp.ImmutableMatrix(sp.eye(8)))
    facts["identity_index"] = identity
    orders = tuple(matrix_order(L) for L in lifts)
    facts["order_counts"] = tuple((n, orders.count(n)) for n in (1, 2, 3, 4))
    facts["homomorphism"] = all(
        table[i][j] == lifts.index(sp.ImmutableMatrix(corner_action(rots[i] * rots[j])))
        for i in range(24) for j in range(24))
    facts["sign_rule_matches_wedge"] = all(orientation_lift(R) == L for R, L in zip(rots, lifts))
    facts["lift_on_empty_and_full_corner"] = tuple(sorted(set((int(L[0, 0]), int(L[7, 7])) for L in lifts)))
    dk = raising_matrix()
    facts["intertwines"] = all(
        residual_count((L * dk * L.T - dk.subs(
            {k: sum(R[i, j] * KAPPA[j] for j in range(3)) for i, k in enumerate(KAPPA)}, simultaneous=True)
        ).applyfunc(sp.expand)) == 0 for R, L in zip(rots, lifts))
    facts["lift_orthogonal"] = all(residual_count(L * L.T - sp.eye(8)) == 0 for L in lifts)
    # the sign rule MEASURED: the intertwining monomial lifts are exactly +-L(R)
    measured = tuple(monomial_intertwiners(R) for R in rots)
    facts["monomial_intertwiner_count"] = tuple(sorted(set(len(m) for m in measured)))
    facts["monomial_intertwiners_are_plus_minus_lift"] = all(
        set(m) == {L, sp.ImmutableMatrix(-L)} for m, L in zip(measured, lifts))
    # the wedge rule read off D versus the ordered-monomial sign
    rule = wedge_rule()
    facts["wedge_is_ordered_monomial"] = all(v == ordered_monomial_sign(mu, c) for (mu, c), v in rule.items())
    facts["wedge_rule_count"] = len(rule)
    # subgroups and their conjugacy classes, from the table
    subgroups, complete = all_subgroups(table, identity)
    classes = conjugacy_classes(table, subgroups, identity)
    axes = tuple(axis_type(R) for R in rots)
    labelled = []
    for cls in classes:
        signature = class_signature(cls[0], orders, axes)
        labelled.append((SIGNATURE_NAMES.get(signature, "UNNAMED:" + str(signature)), len(cls[0]), len(cls), cls[0]))
    labelled.sort(key=lambda x: (x[1], x[0]))
    facts["subgroup_count"] = len(subgroups)
    facts["subgroups_complete"] = complete
    facts["class_table"] = tuple((name, order, size) for name, order, size, _ in labelled)
    facts["representatives"] = {name: rep for name, _, _, rep in labelled}
    facts["classes"] = {SIGNATURE_NAMES.get(class_signature(cls[0], orders, axes), "UNNAMED"): cls for cls in classes}
    facts["lifts"] = lifts
    facts["rotations"] = rots
    facts["table"] = table
    facts["axes"] = axes
    facts["orders"] = orders
    return facts


def measure_star(group: dict) -> dict:
    facts = star_facts(group["lifts"])
    # THE STAR LINE: the 1 <-> 2 cross block of the family is proportional to
    # the star exactly when (D16, D25, D34) is proportional to the star's pair
    # signs; the linear ideal of that line, canonical.
    sy, sx, st = facts["star_pair_signs"][1:]
    lam = sp.Symbol("lam")
    line = canonical_subspace([[0, 1, 0, -sy * st], [0, 0, 1, -sx * st]], PARAMETER_SYMBOLS)
    facts["star_line_generators"] = describe(((frozenset(), line),), PARAMETER_SYMBOLS)[0][1]
    facts["star_line_is_block214_plane"] = tuple(sorted(facts["star_line_generators"])) == tuple(sorted(b214.PLANE))
    # the cross block on the line IS lam * star (1 -> 2) with D07 the free 0 <-> 3 multiple
    star = hodge_star()
    h = family((1, 1), (A07, lam * sy, lam * sx, lam * st))
    even, odd = b213.even_odd(3)
    ones, twos = DEGREE_INDICES[1], DEGREE_INDICES[2]
    cross = h.extract(list(twos), list(ones))
    facts["cross_block_is_lam_star_on_line"] = residual_count(cross - lam * star.extract(list(twos), list(ones))) == 0
    facts["d07_is_zero_three_star_multiple"] = h[7, 0] == A07 * star[7, 0]
    # the mechanism: the onsite M_oo vanishes on the star line and not off it
    hs = family((1, 1), PARAMETER_SYMBOLS)
    _, m, _ = b214.principal_part(hs, "onsite")
    m_oo = m.extract(odd, odd)
    on_line = m_oo.subs({B16: lam * sy, C25: lam * sx, D34: lam * st})
    facts["m_oo_zero_on_star_line"] = residual_count(on_line.applyfunc(sp.expand)) == 0
    facts["m_oo_nonzero_off_line"] = residual_count(m_oo.subs({B16: lam, C25: lam, D34: lam}).applyfunc(sp.expand)) > 0
    # the star-line ideal equals the coefficient ideal of M_oo in the parameters
    entries = [sp.expand(m_oo[i, j]) for i in range(4) for j in range(4) if sp.expand(m_oo[i, j]) != 0]
    rows = []
    for entry in entries:
        for coefficient in sp.Poly(entry, *KAPPA).coeffs():
            rows.append([sp.Poly(coefficient, *PARAMETER_SYMBOLS).coeff_monomial(u) for u in PARAMETER_SYMBOLS])
    facts["m_oo_ideal_is_star_line"] = canonical_subspace(rows, PARAMETER_SYMBOLS) == line
    return facts


def measure_census(group: dict) -> dict:
    """E: per gauge class, per subgroup class: the twisted and the strict
    loci with the fate of the shears, from the per-rotation data."""
    lifts = group["lifts"]
    facts: dict = {"twisted": {}, "strict": {}, "per_rotation_twisted_shears_survive": {},
                   "per_rotation_strict_shears_survive": {}}
    for key in GAUGE_CLASSES:
        h = family(key, PARAMETER_SYMBOLS)
        print(f"[census] gauge class {key}", file=sys.stderr)
        twisted = per_rotation_loci(h, lifts, PARAMETER_SYMBOLS, True)
        strict = per_rotation_loci(h, lifts, PARAMETER_SYMBOLS, False)
        facts["per_rotation_twisted_shears_survive"][key] = tuple(any(not f for f, _ in comps) for comps in twisted)
        facts["per_rotation_strict_shears_survive"][key] = tuple(any(not f for f, _ in comps) for comps in strict)
        for name, rep in group["representatives"].items():
            locus = subgroup_locus(twisted, rep, PARAMETER_SYMBOLS)
            facts["twisted"][(key, name)] = describe(locus, PARAMETER_SYMBOLS)
            facts["strict"][(key, name)] = describe(subgroup_locus(strict, rep, PARAMETER_SYMBOLS), PARAMETER_SYMBOLS)
            if name == "O":
                # the shear-alive twisted line meets the star line only at the
                # origin D16 = D25 = D34 = 0 (D07 free) -- measured per class
                star = [[0, 1, 0, -1], [0, 0, 1, 1]]
                origin = canonical_subspace([[0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]], PARAMETER_SYMBOLS)
                facts.setdefault("twisted_o_line_meets_star_line_at_origin", {})[key] = all(
                    canonical_subspace(star + [list(r) for r in v], PARAMETER_SYMBOLS) == origin for f, v in locus if not f)
        # EVERY member of every class (30 subgroups): the loci at a FIXED cell are
        # not conjugation-invariant, so the number of distinct loci per class is
        # measured (1 for the normal subgroups; sign images otherwise).
        for kind, per in (("twisted", twisted), ("strict", strict)):
            for name, cls in group["classes"].items():
                distinct = {describe(subgroup_locus(per, member, PARAMETER_SYMBOLS), PARAMETER_SYMBOLS) for member in cls}
                facts.setdefault(f"{kind}_distinct_per_class", {})[(key, name)] = len(distinct)
                if name == "O" or name == "T" or name == "V4_faces":
                    facts.setdefault(f"{kind}_normal_single", {})[(key, name)] = len(distinct) == 1
    return facts


def measure_overlap(group: dict) -> dict:
    """F: the overlap fold sees the sum only; its parity; its loci in s."""
    lifts = group["lifts"]
    h_full, _, _ = b214.principal_part(family((1, 1), PARAMETER_SYMBOLS), "overlap")
    h_sum, _, _ = b214.principal_part(family((1, 1), (SUM, 0, 0, 0)), "overlap")
    facts: dict = {"overlap_sees_sum_only": residual_count(
        (h_full - h_sum.subs(SUM, sum(PARAMETER_SYMBOLS))).applyfunc(sp.expand)) == 0}
    even, odd = b213.even_odd(3)
    p111 = b214.hodge_complement_permutation()
    facts["overlap_parity_block_is_sum_over_four_p111"] = residual_count(
        (h_sum.extract(even, odd) - SUM / 4 * p111.extract(even, odd)).applyfunc(sp.expand)) == 0
    facts["twisted"], facts["strict"] = {}, {}
    for key in GAUGE_CLASSES:
        h, _, _ = b214.principal_part(family(key, (SUM, 0, 0, 0)), "overlap")
        print(f"[overlap] gauge class {key}", file=sys.stderr)
        twisted = per_rotation_loci(h, lifts, (SUM,), True)
        strict = per_rotation_loci(h, lifts, (SUM,), False)
        for name, rep in group["representatives"].items():
            facts["twisted"][(key, name)] = describe(subgroup_locus(twisted, rep, (SUM,)), (SUM,))
            facts["strict"][(key, name)] = describe(subgroup_locus(strict, rep, (SUM,)), (SUM,))
    return facts


def measure_controls(group: dict) -> dict:
    """G: positivity off the plane, onsite parity, the flat cell, the gauge
    congruence in the field, the reconciliation with Block 214's cell."""
    lifts = group["lifts"]
    facts: dict = {}
    w1 = (sp.Rational(1, 4), sp.Rational(1, 4), sp.Rational(15, 16), sp.Integer(1))   # (g0, g1, v0, v1) at W1
    witness = family((1, 1), (0, QUARTER, 0, 0), w1)
    minors = tuple(witness[:k, :k].det() for k in range(1, 9))
    facts["positivity_witness_minors"] = minors
    facts["positivity_witness_is_pd"] = all(m > 0 for m in minors)
    plane = [sp.sympify(g) for g in b214.PLANE]
    facts["positivity_witness_off_plane"] = any(
        g.subs({B16: QUARTER, C25: 0, D34: 0}) != 0 for g in plane)
    h = family((1, 1), PARAMETER_SYMBOLS)
    even, odd = b213.even_odd(3)
    h_eo = h.extract(even, odd)
    facts["onsite_parity_block_entries"] = tuple(sorted(str(x) for x in h_eo if x != 0))
    facts["onsite_parity_preserved_iff_all_zero"] = set(h_eo.free_symbols) == set(PARAMETER_SYMBOLS) and all(
        residual_count(h_eo.subs({p: 0 for p in PARAMETER_SYMBOLS if p != q})) == 1 for q in PARAMETER_SYMBOLS)
    flat = family((1, 1), PARAMETER_SYMBOLS, (sp.Integer(0), sp.Integer(0), sp.Integer(1), sp.Integer(1)))
    facts["flat_zero_is_identity"] = residual_count(flat.subs({p: 0 for p in PARAMETER_SYMBOLS}) - sp.eye(8)) == 0
    twisted = per_rotation_loci(flat, lifts, PARAMETER_SYMBOLS, True)
    strict = per_rotation_loci(flat, lifts, PARAMETER_SYMBOLS, False)
    facts["flat_twisted"] = {name: describe(subgroup_locus(twisted, rep, PARAMETER_SYMBOLS), PARAMETER_SYMBOLS)
                             for name, rep in group["representatives"].items()}
    facts["flat_strict"] = {name: describe(subgroup_locus(strict, rep, PARAMETER_SYMBOLS), PARAMETER_SYMBOLS)
                            for name, rep in group["representatives"].items()}
    # THE GAUGE CONGRUENCE IN THE FIELD: a two-face flip at one offset (same
    # class) IS E D E for one of the 64 sign vectors at symbolic moduli; a
    # one-face flip (the other class) is NOT -- the per-offset product is the
    # invariant.
    # (the parameters are set to zero for this check: the gauge also flips
    # D16, D25, D34 by e_i e_j, which is the twist the census uses).
    zeros = (sp.Integer(0),) * 4
    base = family((1, 1), zeros)

    def reachable(signs: dict) -> bool:
        target = b214.formal_cell(signs, G0, G1, V0, V1, zeros)
        return any(residual_count((sp.diag(*e) * base * sp.diag(*e) - target).applyfunc(sp.expand)) == 0
                   for e in sign_vectors())
    facts["gauge_congruence_in_field"] = (
        reachable(b211.flipped(("tx", 0), ("ty", 0))) and reachable(b211.flipped(("tx", 1), ("xy", 1)))
        and not reachable(b211.flipped(("xy", 0))) and not reachable(b211.flipped(("xy", 1))))
    # THE 64 SIGN CELLS UNDER THE FULL GROUP (two generators suffice: the signed
    # lifts fixing H form a group): at which cells is the shear-alive twisted
    # locus the star line?
    table, orders = group["table"], group["orders"]
    g3 = orders.index(3)
    g4 = next(i for i in range(24) if orders[i] == 4 and len(closure(table, frozenset((g3, i)), group["identity_index"])) == 24)
    facts["generators_generate_o"] = len(closure(table, frozenset((g3, g4)), group["identity_index"])) == 24
    star_line = canonical_subspace([[0, 1, 0, -1], [0, 0, 1, 1]], PARAMETER_SYMBOLS)
    scan, strict_scan = {}, {}
    for values in itertools.product((1, -1), repeat=6):
        signs = dict(zip(b211.GAUGE_FACE_ORDER, (sp.Integer(v) for v in values)))
        cell = b214.formal_cell(signs, G0, G1, V0, V1, PARAMETER_SYMBOLS)
        per = tuple(irredundant([constraints(cell, lifts[g], e, PARAMETER_SYMBOLS) for e in sign_vectors()]) for g in (g3, g4))
        locus = intersect(per[0], per[1], PARAMETER_SYMBOLS)
        alive = tuple(v for f, v in locus if not f)
        scan[values] = (len(alive), alive == (star_line,), describe(tuple((frozenset(), v) for v in alive), PARAMETER_SYMBOLS))
        # STRICT (E = 1) covariance at this cell under every S3_body and under T: the
        # shear-alive components, if any (the sealed blind seat predicted that a curved
        # cell is strictly S3-covariant at exactly the 16 star-line cells; measured here)
        strict_per = tuple(irredundant([constraints(cell, lifts[g], (1,) * 8, PARAMETER_SYMBOLS)]) for g in range(24))
        s3_alive = tuple(tuple(v for f, v in subgroup_locus(strict_per, member, PARAMETER_SYMBOLS) if not f)
                         for member in group["classes"]["S3_body"])
        t_alive = tuple(v for f, v in subgroup_locus(strict_per, group["representatives"]["T"], PARAMETER_SYMBOLS) if not f)
        strict_scan[values] = (any(s3_alive), all(a in ((), (star_line,)) for a in s3_alive), bool(t_alive))
    facts["cell_scan_alive_component_counts"] = tuple(sorted(set(v[0] for v in scan.values())))
    facts["cell_scan_star_line_cells"] = sum(1 for v in scan.values() if v[1])
    facts["cell_scan_distinct_alive_loci"] = tuple(sorted(set(v[2] for v in scan.values())))
    facts["cell_scan_all_plus"] = scan[(1,) * 6][2]
    facts["cell_scan_strict_s3_alive_cells"] = sum(1 for v in strict_scan.values() if v[0])
    facts["cell_scan_strict_s3_alive_is_star_line"] = all(v[1] for v in strict_scan.values())
    facts["cell_scan_strict_s3_cells_are_star_line_cells"] = all(strict_scan[k][0] == scan[k][1] for k in scan)
    facts["cell_scan_strict_t_alive_cells"] = sum(1 for v in strict_scan.values() if v[2])
    # THE FACE-SIGN RULE (the refuting checker's CK-11, then measured here): a cell is a
    # star-line cell iff its two-offset face-sign products (P_tx, P_ty, P_xy), in Block
    # 211's GAUGE_FACE_ORDER (tx0, ty0, xy0, tx1, ty1, xy1), follow the star's pair signs
    # (+, -, +) on (tx, ty, xy) up to a global sign.
    star_pattern = ((1, -1, 1), (-1, 1, -1))
    facts["cell_scan_star_pattern_cells"] = sum(1 for k in scan if (k[0] * k[3], k[1] * k[4], k[2] * k[5]) in star_pattern)
    facts["cell_scan_star_line_cells_are_star_pattern_cells"] = all(
        scan[k][1] == ((k[0] * k[3], k[1] * k[4], k[2] * k[5]) in star_pattern) for k in scan)
    cell, free, _ = b214.cell_with_parameters("W1")
    renamed = cell.subs({s: dict(zip(PARAMETER_NAMES, PARAMETER_SYMBOLS))[str(s)] for s in cell.free_symbols
                         if str(s) in PARAMETER_NAMES})
    facts["family_is_block214_cell_at_w1"] = residual_count((renamed - family((1, 1), PARAMETER_SYMBOLS, w1)).applyfunc(sp.cancel)) == 0 \
        and free == PARAMETER_NAMES
    return facts


@dataclass(frozen=True)
class Facts:
    authority: AuthorityCertificate
    group: dict
    star: dict
    census: dict
    overlap: dict
    controls: dict
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
    group = measure_group()
    lap("group")
    star = measure_star(group)
    lap("star")
    census = measure_census(group)
    lap("census")
    overlap = measure_overlap(group)
    lap("overlap")
    controls = measure_controls(group)
    lap("controls")
    axiom_text = (ROOT / AXIOM_PATH).read_text(encoding="utf-8") if (ROOT / AXIOM_PATH).is_file() else ""
    note_text = NOTE_PATH.read_text(encoding="utf-8") if NOTE_PATH.is_file() else ""
    return Facts(authority, group, star, census, overlap, controls, axiom_text, note_text, timings)


# ---------------------------------------------------------------------------
# THE DECLARED LITERALS -- every claim is a constant compared against a
# measurement; a mutation rewrites exactly one claim.
# ---------------------------------------------------------------------------
ORDER_COUNTS = ((1, 1), (2, 9), (3, 8), (4, 6))
CLASS_TABLE = (("1", 1, 1), ("C2_edge", 2, 6), ("C2_face", 2, 3), ("C3_body", 3, 4), ("C4_face", 4, 3),
               ("V4_face_edges", 4, 3), ("V4_faces", 4, 1), ("S3_body", 6, 4), ("D4_face", 8, 3), ("T", 12, 1), ("O", 24, 1))
SUBGROUP_COUNT = 30
# * e_c = STAR_SIGNS[c] e_{c-bar} in Block 209's corner order; on the duality
# pairs (0,7), (1,6), (2,5), (4,3) the signs are (+, +, -, +): t -> +xy, x -> -ty, y -> +tx.
STAR_SIGNS = (1, 1, -1, 1, 1, -1, 1, 1)
STAR_PAIR_SIGNS = (1, 1, -1, 1)
STAR_ADJOINT_SIGNS = (1, -1, 1)          # * D(kappa) = eps_k D(kappa)^T * on k-forms
STAR_LINE = ("D16 - D34", "D25 + D34")   # = Block 214's PLANE literal
DIAGONAL_LINE = ("D16 - D34", "D25 - D34")
P111_COMMUTING_LIFTS = 8
STRICT_SHEAR_SURVIVING_ROTATIONS = {(1, 1): 2, (1, -1): 2, (-1, 1): 2, (-1, -1): 2}
CELL_SCAN_STAR_LINE_CELLS = 16
CELL_SCAN_ALIVE_COUNTS = (1,)
STRICT_S3_ALIVE_CELLS = 16
STRICT_T_ALIVE_CELLS = 0
STAR_PATTERN_CELLS = 16
POSITIVITY_WITNESS_MINORS = (sp.Rational(15, 16), sp.Rational(15, 16), sp.Rational(225, 256), sp.Rational(15, 16),
                             sp.Rational(25, 32), sp.Rational(25, 32), sp.Rational(1465, 2304), sp.Rational(1465, 2304))
SCOUT_GRADE_FENCE = ("scout-grade finite exact linear algebra on one cell form, "
                     "not a spacetime and not a dynamics")
SCOUT_GRADE_ONLY = True
INSTANCE_SCOPE = (
    "one cell form: Block 211's six-face-compatible family at symbolic moduli on its ties, the four class representatives and the 64 sign cells (full group only)",
    "the covariance notion: (E_R R) H (E_R R)^T = H with E_R among Block 211's 64 sign vectors (twisted) or E_R = 1 (strict); no other twist",
    "the group: the 24 proper cubic rotations lifted through the lane's wedge; no improper element, no translation, no continuum rotation",
    "the loci are linear varieties at symbolic moduli; no cone, no dispersion and no bench is computed here (Block 214's loci are imported as literals)",
    "both assemblies run; neither decided; no Hodge reading, no subgroup, no parameter value selected",
    "the union-locus statement on the twisted lines at sign cells other than Block 214's witnesses is NOT computed",
)
INSTANCE_SCOPE_COUNT = 6


def scope_certificate(text: str) -> dict:
    return {"n5_verbatim": N5_FENCE in text}


def alive(components: tuple) -> tuple:
    """The shear-surviving components of a described locus."""
    return tuple(generators for forced, generators in components if not forced)


def star_line_only_with_shear_killed(table: dict) -> bool:
    return all(forced for entry in table.values() for forced, generators in entry
               if tuple(sorted(generators)) == tuple(sorted(STAR_LINE)))


def build_claims(mutation: str) -> dict:
    wrong_twisted = dict(TWISTED_LOCI)
    wrong_twisted[((1, 1), "O")] = (((), STAR_LINE),)
    wrong_strict = dict(STRICT_LOCI)
    wrong_strict[((1, 1), "O")] = (((), STAR_LINE),)
    wrong_overlap = dict(OVERLAP_TWISTED_LOCI)
    wrong_overlap[((1, 1), "O")] = (((), ("s",)),)
    wrong_flat = dict(FLAT_STRICT_LOCI)
    wrong_flat["O"] = (((), DIAGONAL_LINE),)
    claims = {
        "current_main": CURRENT_MAIN, "parent_commit": PARENT_COMMIT,
        "registered": (), "gravity_supplied": False, "covariance_inherited": False,
        "subgroup_selected": False, "assembly_decided": False,
        "order_counts": ORDER_COUNTS, "intertwines": True, "class_table": CLASS_TABLE,
        "gauge_congruence": True,
        "star_adjoint_signs": STAR_ADJOINT_SIGNS, "star_line": STAR_LINE,
        "twisted_loci": TWISTED_LOCI, "strict_loci": STRICT_LOCI, "twisted_shears_survive": True,
        "p111_commuting_lifts": P111_COMMUTING_LIFTS, "overlap_twisted_loci": OVERLAP_TWISTED_LOCI,
        "positivity_selects_plane": False, "parity_selects_plane": False, "flat_strict_loci": FLAT_STRICT_LOCI,
        "strict_s3_alive_cells": STRICT_S3_ALIVE_CELLS, "star_pattern_cells": STAR_PATTERN_CELLS,
        "scout_grade": SCOUT_GRADE_FENCE, "instance_scope_count": INSTANCE_SCOPE_COUNT,
        "n5_verbatim": True, "float_absent": True,
    }
    flips = {
        "stale_main_authority": ("current_main", STALE_MAIN),
        "stale_parent_authority": ("parent_commit", STALE_PARENT_COMMIT),
        "claim_objects_registered": ("registered", ("the corner action",)),
        "claim_gravity_supplied": ("gravity_supplied", True),
        "claim_covariance_inherited": ("covariance_inherited", True),
        "claim_subgroup_selected": ("subgroup_selected", True),
        "claim_assembly_decided": ("assembly_decided", True),
        "break_representation_orders": ("order_counts", ((1, 1), (2, 7), (3, 8), (4, 8))),
        "break_intertwining": ("intertwines", False),
        "break_subgroup_class_count": ("class_table", CLASS_TABLE[:-1]),
        "break_gauge_congruence": ("gauge_congruence", False),
        "break_star_signs": ("star_adjoint_signs", (1, 1, 1)),
        "break_star_line": ("star_line", DIAGONAL_LINE),
        "break_twisted_census": ("twisted_loci", wrong_twisted),
        "break_strict_census": ("strict_loci", wrong_strict),
        "claim_shears_killed_by_twisted_covariance": ("twisted_shears_survive", False),
        "break_p111_commutation": ("p111_commuting_lifts", 24),
        "break_overlap_locus": ("overlap_twisted_loci", wrong_overlap),
        "claim_positivity_selects_plane": ("positivity_selects_plane", True),
        "claim_parity_selects_plane": ("parity_selects_plane", True),
        "break_flat_cell_loci": ("flat_strict_loci", wrong_flat),
        "break_strict_s3_cells": ("strict_s3_alive_cells", 0),
        "break_star_pattern_cells": ("star_pattern_cells", 8),
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
    checks.check("A-2", "THE CORRECTED BLOCK 214 NOTE AND RUNNER are content-bound finite suppliers; ancestry is provenance only",
                 au.parent_inputs_content_bound and claims["parent_commit"] == SUPPLIER_FREEZE_COMMIT)
    checks.check("A-3", "THE MINIMAL GROUP HELPER AND CORRECTED 213/214 IMPORT CLOSURE are present and every declared input is readable",
                 au.helper_content_bound and au.machinery_import_landed
                 and au.inputs_readable == len(AUDIT_INPUT_PATHS) and not au.inputs_missing)
    checks.check("B-1", "NOTHING REGISTERED, NOTHING ADOPTED: six imposed objects, zero registered, zero adopted",
                 len(IMPOSED_OBJECTS) == 6 and claims["registered"] == REGISTERED_OBJECTS == () and ADOPTED_OBJECTS == ())
    checks.check("B-2", "NO GRAVITY IS SUPPLIED: nine structures enumerated as not supplied",
                 not claims["gravity_supplied"] and not GRAVITY_SUPPLIED_CLAIMED and len(UNSUPPLIED_GRAVITY_STRUCTURES) == 9)
    checks.check("B-3", "THE AXIOM CLAUSE IS QUOTED VERBATIM AND GOVERNS THE RULE; that the cell form inherits it is a READING, asserted nowhere (the theorem is the conditional)",
                 AXIOM_COVARIANCE_CLAUSE in facts.axiom_text and not claims["covariance_inherited"] and not COVARIANCE_INHERITED_CLAIMED)
    checks.check("B-4", "NO SUBGROUP IS SELECTED AS 'THE' SYMMETRY, NO ASSEMBLY DECIDED, NO PARAMETER VALUE SELECTED",
                 not claims["subgroup_selected"] and not SUBGROUP_SELECTED_CLAIMED and not claims["assembly_decided"]
                 and not ASSEMBLY_DECIDED_CLAIMED and not PARAMETER_VALUE_SELECTED_CLAIMED)
    checks.check("B-5", "THE WORDS COVARIANCE, LOCUS, STAR, GAUGE AND PLANE ARE SCOPED; six readings enumerated, none licensed; no continuum, no spacetime cone",
                 len(SCOPED_HEADLINE_WORDS) == 5 and len(READINGS) == 6 and not READINGS_LICENSED_CLAIMED
                 and not CONTINUUM_LIMIT_CLAIMED and not CONE_IS_SPACETIME_CONE_CLAIMED)
    gr = facts.group
    checks.check("C-1", "THE CORNER ACTION IS A REPRESENTATION OF THE 24 PROPER ROTATIONS: Block 201's det = +1 signed permutations are 24; the lifts are 24 distinct orthogonal matrices, closed, containing the identity, L(R1 R2) = L(R1) L(R2), element orders 1/2/3/4 in counts 1/9/8/6",
                 gr["rotation_count"] == 24 and gr["all_det_one"] and gr["distinct_lifts"] == 24 and gr["closed"]
                 and gr["homomorphism"] and gr["lift_orthogonal"] and gr["order_counts"] == claims["order_counts"])
    checks.check("C-2", "THE SIGN RULE IS DERIVED, NOT GUESSED: the lane's D(kappa) is the ordered-monomial wedge (12 signs); the lift built through that wedge equals the orientation-sign rule; the only monomial intertwiners are +-L(R); every lift is +1 on the empty and on the full corner (det R = +1)",
                 gr["wedge_is_ordered_monomial"] and gr["wedge_rule_count"] == 12 and gr["sign_rule_matches_wedge"]
                 and gr["monomial_intertwiner_count"] == (2,) and gr["monomial_intertwiners_are_plus_minus_lift"]
                 and gr["lift_on_empty_and_full_corner"] == ((1, 1),))
    checks.check("C-3", "THE LIFT INTERTWINES THE RAISING PART: L(R) D(kappa) L(R)^-1 = D(R kappa) for every R",
                 gr["intertwines"] == claims["intertwines"] and claims["intertwines"])
    checks.check("C-4", "THE SUBGROUP CLASSES ARE COMPUTED FROM THE GROUP: 30 subgroups with a completeness certificate, 11 conjugacy classes with the declared (name, order, size) table",
                 gr["subgroup_count"] == SUBGROUP_COUNT and gr["subgroups_complete"] and gr["class_table"] == claims["class_table"]
                 and len(claims["class_table"]) == 11)
    ct = facts.controls
    checks.check("C-5", "THE FAMILY IS BLOCK 214's CELL: at W1 it equals cell_with_parameters with the four free names; the gauge congruence E D E holds in the field for same-class two-face flips and fails for one-face flips",
                 ct["family_is_block214_cell_at_w1"] and ct["gauge_congruence_in_field"] == claims["gauge_congruence"] and claims["gauge_congruence"])
    st = facts.star
    checks.check("D-1", "THE STAR FROM THE WEDGE: * e_c = sign e_{c-bar} with the declared signs, ** = +1 on every degree, * D(kappa) = eps_k D(kappa)^T * with eps = (+1, -1, +1) on 0-, 1-, 2-forms, and * commutes with every lift",
                 st["star_signs"] == STAR_SIGNS and st["star_squares"] == (1, 1, 1, 1) and st["star_square_is_scalar"]
                 and st["star_adjoint_signs"] == claims["star_adjoint_signs"] and st["star_commutes_with_every_lift"])
    checks.check("D-2", "THE STAR LEMMA: the 1 <-> 2 cross block is lam * exactly on the line D16 = D34 = -D25 (the star's pair signs (+, -, +) on (y, x, t)), which IS Block 214's plane; D07 is the free 0 <-> 3 star multiple; the onsite M_oo vanishes exactly there (its coefficient ideal is the line)",
                 st["star_pair_signs"] == STAR_PAIR_SIGNS and tuple(sorted(st["star_line_generators"])) == tuple(sorted(claims["star_line"]))
                 and st["star_line_is_block214_plane"] and st["cross_block_is_lam_star_on_line"] and st["d07_is_zero_three_star_multiple"]
                 and st["m_oo_zero_on_star_line"] and st["m_oo_nonzero_off_line"] and st["m_oo_ideal_is_star_line"])
    ce = facts.census
    checks.check("E-1", "THE SHEARS SURVIVE TWISTED COVARIANCE UNDER EVERY ROTATION in all four gauge classes; strictly they survive only the identity and one edge rotation per class",
                 all(all(v) for v in ce["per_rotation_twisted_shears_survive"].values()) == claims["twisted_shears_survive"]
                 and claims["twisted_shears_survive"]
                 and {k: sum(v) for k, v in ce["per_rotation_strict_shears_survive"].items()} == STRICT_SHEAR_SURVIVING_ROTATIONS)
    checks.check("E-2", "THE TWISTED CENSUS at the four class representatives is the declared table: O, T, S3, C3 force ONE shear-alive line (the diagonal D16 = D25 = D34 at all-plus and at (-1,-1); D16 = D25 = -D34 at the two mixed classes), never the star line; the star line appears only with a shear killed",
                 ce["twisted"] == claims["twisted_loci"] and star_line_only_with_shear_killed(claims["twisted_loci"])
                 and alive(claims["twisted_loci"][((1, 1), "O")]) == (DIAGONAL_LINE,)
                 and all(ce["twisted_o_line_meets_star_line_at_origin"].values()))
    checks.check("E-3", "THE STRICT CENSUS is the declared table: O and T force the star line WITH g0 = g1 = 0 (the flat cell); C3 (S3) force the star line with one shear killed; the minimal strict class forcing the star line is C3",
                 ce["strict"] == claims["strict_loci"]
                 and all(claims["strict_loci"][(key, "O")] == ((("g0", "g1"), STAR_LINE),) for key in GAUGE_CLASSES)
                 and claims["strict_loci"][((1, 1), "C3_body")] == ((("g1",), STAR_LINE),))
    checks.check("E-4", "EVERY MEMBER OF EVERY CLASS (30 subgroups): the loci at a fixed cell are not conjugation-invariant except for the normal subgroups; the distinct-locus counts per class are the declared literals",
                 ce["twisted_distinct_per_class"] == TWISTED_DISTINCT_PER_CLASS and ce["strict_distinct_per_class"] == STRICT_DISTINCT_PER_CLASS
                 and all(ce["twisted_normal_single"].values()) and all(ce["strict_normal_single"].values()))
    checks.check("E-5", "D07 IS FREE UNDER EVERY SUBGROUP, twisted and strict: no locus generator carries D07",
                 not any("D07" in g for table in (ce["twisted"], ce["strict"]) for entry in table.values() for _, gens in entry for g in gens))
    ov = facts.overlap
    checks.check("F-1", "P111 IS THE UNSIGNED STAR: it commutes with the unsigned corner permutation of every rotation but with only 8 of the 24 signed lifts (the twist is diag(s_c s_{R^-1 c})); the STAR commutes with all 24",
                 st["p111_is_unsigned_star"] and st["p111_commutes_with_unsigned_permutation"]
                 and st["p111_commutes_with_lift_count"] == claims["p111_commuting_lifts"] and st["star_commutes_with_every_lift"])
    checks.check("F-2", "THE OVERLAP FOLD sees only s = D07 + D16 + D25 + D34, its parity block is (s/4) P111, and NO subgroup's TWISTED covariance forces s = 0 in any class (declared table); strict covariance forces s = 0 together with a shear relation (declared table)",
                 ov["overlap_sees_sum_only"] and ov["overlap_parity_block_is_sum_over_four_p111"]
                 and ov["twisted"] == claims["overlap_twisted_loci"] and ov["strict"] == OVERLAP_STRICT_LOCI
                 and not any("s" in gens for entry in claims["overlap_twisted_loci"].values() for _, gens in entry))
    checks.check("G-1", "POSITIVITY DOES NOT SELECT THE PLANE: Block 214's witness W1 + D16 = 1/4 is off the plane and positive definite by exact leading minors",
                 ct["positivity_witness_is_pd"] and ct["positivity_witness_off_plane"] and ct["positivity_witness_minors"] == POSITIVITY_WITNESS_MINORS
                 and not claims["positivity_selects_plane"])
    checks.check("G-2", "ONSITE PARITY DOES NOT SELECT THE PLANE: the folded onsite parity block carries exactly the four parameters and vanishes iff all four vanish (the origin)",
                 ct["onsite_parity_block_entries"] == PARAMETER_NAMES and ct["onsite_parity_preserved_iff_all_zero"] and not claims["parity_selects_plane"])
    checks.check("G-3", "THE FLAT CELL: strict O-covariance of the flat cell forces exactly the star line; twisted, the four sign lines (declared tables); the 64-cell scan under two generators of O finds ONE shear-alive line at every cell, the star line at exactly 16 cells and the diagonal at all-plus",
                 ct["flat_zero_is_identity"] and ct["flat_strict"] == claims["flat_strict_loci"] and ct["flat_twisted"] == FLAT_TWISTED_LOCI
                 and ct["generators_generate_o"] and ct["cell_scan_alive_component_counts"] == CELL_SCAN_ALIVE_COUNTS
                 and ct["cell_scan_star_line_cells"] == CELL_SCAN_STAR_LINE_CELLS and ct["cell_scan_all_plus"] == (((), DIAGONAL_LINE),))
    checks.check("G-4", "STRICT S3-COVARIANT CURVED CELLS: at exactly 16 of the 64 sign cells some S3_body keeps both shears alive under strict (E = 1) covariance, the shear-alive strict-S3 locus there is the star line, those 16 cells are exactly the cells whose twisted-O line is the star line, and strict T keeps the shears alive at no cell",
                 ct["cell_scan_strict_s3_alive_cells"] == claims["strict_s3_alive_cells"] == STRICT_S3_ALIVE_CELLS
                 and ct["cell_scan_strict_s3_alive_is_star_line"] and ct["cell_scan_strict_s3_cells_are_star_line_cells"]
                 and ct["cell_scan_strict_t_alive_cells"] == STRICT_T_ALIVE_CELLS)
    checks.check("G-5", "THE FACE-SIGN RULE FOR THE 16 CELLS: a sign cell is a star-line cell (twisted-O line = the star line) IFF its two-offset face-sign products (P_tx, P_ty, P_xy) follow the star's pair signs (+, -, +) on (tx, ty, xy) up to a global sign; exactly 16 cells do",
                 ct["cell_scan_star_line_cells_are_star_pattern_cells"]
                 and ct["cell_scan_star_pattern_cells"] == claims["star_pattern_cells"] == STAR_PATTERN_CELLS)
    checks.check("H-1", "SCOUT-GRADE FENCE, inherited verbatim from Blocks 211, 213 and 214",
                 claims["scout_grade"] == SCOUT_GRADE_FENCE and SCOUT_GRADE_ONLY)
    checks.check("H-2", "THE INSTANCE SCOPE IS ENUMERATED: six restrictions",
                 claims["instance_scope_count"] == len(INSTANCE_SCOPE) == 6)
    sc = scope_certificate(facts.note_text)
    checks.check("I-1", "THE NOTE IS PRESENT AND CARRIES THE N5 FENCE BYTE-IDENTICALLY",
                 bool(facts.note_text) and sc["n5_verbatim"] == claims["n5_verbatim"] and claims["n5_verbatim"])
    checks.check("I-2", "NO nsimplify, NO float literal, NO float call in this runner's source",
                 nsimplify_occurrences() == 0 and float_literal_occurrences() == 0 and float_call_sites() == 0
                 and claims["float_absent"])
    return checks


def report_measured(facts: Facts, elapsed_ns: int) -> None:
    print("== BLOCK 215: the covariance locus of the four duality parameters -- measured facts ==")
    print(f"authority: {facts.authority}")
    gr = facts.group
    for key in ("rotation_count", "distinct_lifts", "closed", "homomorphism", "order_counts", "sign_rule_matches_wedge",
                "monomial_intertwiner_count", "intertwines", "wedge_is_ordered_monomial", "subgroup_count", "subgroups_complete", "class_table"):
        print(f"group {key}: {gr[key]}")
    for key, value in facts.star.items():
        print(f"star {key}: {value}")
    ce = facts.census
    for key in ("per_rotation_twisted_shears_survive", "per_rotation_strict_shears_survive"):
        print(f"census {key}: {ce[key]}")
    for kind in ("twisted", "strict"):
        for key in sorted(ce[kind], key=str):
            print(f"census {kind} {key}: {ce[kind][key]}")
        print(f"census {kind}_distinct_per_class: {ce[f'{kind}_distinct_per_class']}")
    ov = facts.overlap
    print(f"overlap sees_sum_only={ov['overlap_sees_sum_only']} parity_block={ov['overlap_parity_block_is_sum_over_four_p111']}")
    for kind in ("twisted", "strict"):
        for key in sorted(ov[kind], key=str):
            print(f"overlap {kind} {key}: {ov[kind][key]}")
    for key, value in facts.controls.items():
        print(f"controls {key}: {value}")
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


N5_FENCE = "N5: The corrected Block 215 claim is finite exact covariance algebra on one supplied cell family: 24 proper signed rotations, 30 subgroups in 11 conjugacy classes, the exterior-star line D16 = D34 = -D25, strict and sign-twisted linear loci, and a 16-cell star-pattern census. Covariance means only (E_R L) H (E_R L)^T = H. No inheritance from the Admissibility axiom, premise adoption, subgroup selection, assembly choice, physical metric, action, spacetime, continuum, or dynamics is claimed; superseded parent assurances are historical only."


# ---------------------------------------------------------------------------
# THE DECLARED CENSUS TABLES (compact): one 4-character pattern per subgroup
# class in CLASS_TABLE order, one character per gauge class in GAUGE_CLASSES
# order, indexing the value tuple (1-based: 1..9, A..).
# ---------------------------------------------------------------------------
def expand_table(patterns: str, values: tuple) -> dict:
    digits = "123456789ABCDEFGHIJ"
    out = {}
    for (name, _, _), pattern in zip(CLASS_TABLE, patterns.split()):
        for key, ch in zip(GAUGE_CLASSES, pattern):
            out[(key, name)] = values[digits.index(ch)]
    return out


def expand_flat(patterns: str, values: tuple) -> dict:
    digits = "123456789ABCDEFGHIJ"
    return {name: values[digits.index(ch)] for (name, _, _), ch in zip(CLASS_TABLE, patterns.split())}


TW1 = (((), ()),)
TW2 = (((), ('D16 - D25',)), ((), ('D16 + D25', 'D34')), (('g0',), ('D16 + D25',)), (('g1',), ('D16 + D25',)))
TW3 = (((), ('D16 - D34', 'D25 - D34')), (('g0',), ('D16 - D34', 'D25 + D34')), (('g0',), ('D16 + D34', 'D25 - D34')), (('g0',), ('D16 + D34', 'D25 + D34')), (('g1',), ('D16 - D34', 'D25 + D34')), (('g1',), ('D16 + D34', 'D25 - D34')), (('g1',), ('D16 + D34', 'D25 + D34')))
TW4 = (((), ('D16 + D34', 'D25 + D34')), (('g0',), ('D16 - D34', 'D25 - D34')), (('g0',), ('D16 - D34', 'D25 + D34')), (('g0',), ('D16 + D34', 'D25 - D34')), (('g1',), ('D16 - D34', 'D25 - D34')), (('g1',), ('D16 - D34', 'D25 + D34')), (('g1',), ('D16 + D34', 'D25 - D34')))
TWISTED_LOCI = expand_table("1111 2222 1111 3443 2222 2222 1111 3443 2222 3443 3443", (TW1, TW2, TW3, TW4))
ST1 = (((), ()),)
ST2 = ((('g0',), ('D16 + D25',)),)
ST3 = ((('g0', 'g1'), ()),)
ST4 = ((('g0', 'g1'), ('D16 - D34', 'D25 + D34')),)
ST5 = ((('g0', 'g1'), ('D16 + D25',)),)
ST6 = ((('g0',), ('D16 - D34', 'D25 + D34')),)
ST7 = ((('g1',), ('D16 - D34', 'D25 + D34')),)
STRICT_LOCI = expand_table("1111 2222 3333 7744 5555 5555 3333 6464 5555 4444 4444", (ST1, ST2, ST3, ST4, ST5, ST6, ST7))
OT1 = (((), ()),)
OT2 = ((('g0',), ()), (('g1',), ()))
OVERLAP_TWISTED_LOCI = expand_table("1111 1111 1111 1221 1111 1111 1111 1221 1111 1221 1221", (OT1, OT2))
OS1 = (((), ()),)
OS2 = ((('g0*v0*v1 + g1',), ('s',)),)
OS3 = ((('g0*v0*v1 + g1',), ()),)
OS4 = ((('g0*v0*v1 + g1', 'g0*v0*v1 - g1'), ('s',)),)
OS5 = ((('g0', 'g0*v0*v1 + g1', 'g1'), ('s',)),)
OS6 = ((('g0', 'g0*v0*v1 + g1', 'g0*v0*v1 - g1', 'g1'), ('s',)),)
OS7 = ((('g0*v0*v1 + g1', 'g0*v0*v1 - g1'), ()),)
OVERLAP_STRICT_LOCI = expand_table("1111 2442 3333 2552 2442 2442 3773 2662 2442 2662 2662", (OS1, OS2, OS3, OS4, OS5, OS6, OS7))
FT1 = (((), ()),)
FT2 = (((), ('D16 - D25',)), ((), ('D16 + D25',)))
FT3 = (((), ('D16 - D34', 'D25 - D34')), ((), ('D16 - D34', 'D25 + D34')), ((), ('D16 + D34', 'D25 - D34')), ((), ('D16 + D34', 'D25 + D34')))
FLAT_TWISTED_LOCI = expand_flat("1 2 1 3 2 2 1 3 2 3 3", (FT1, FT2, FT3))
FS1 = (((), ()),)
FS2 = (((), ('D16 + D25',)),)
FS3 = (((), ('D16 - D34', 'D25 + D34')),)
FLAT_STRICT_LOCI = expand_flat("1 2 1 3 2 2 1 3 2 3 3", (FS1, FS2, FS3))
TWISTED_DISTINCT_PER_CLASS = expand_table("1111 3333 1111 1111 3333 3333 1111 1111 3333 1111 1111", (1, 2, 3, 4, 5, 6, 7, 8, 9))
STRICT_DISTINCT_PER_CLASS = expand_table("1111 6666 1111 3333 3333 3333 1111 3333 3333 1111 1111", (1, 2, 3, 4, 5, 6, 7, 8, 9))


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except SystemExit:
        raise
    except Exception as error:
        print(f"[FAIL] INTERNAL-EXCEPTION: {type(error).__name__}: {error}")
        print("TOTAL: PASS=0 FAIL=1")
        raise
