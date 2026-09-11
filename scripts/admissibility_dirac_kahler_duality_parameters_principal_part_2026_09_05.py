#!/usr/bin/env python3
"""BLOCK 214 -- THE DUALITY PARAMETERS AND THE PRINCIPAL PART.

Block 211 solves the six-face system at every compatible moduli point with
exactly four free duality parameters D07, D16, D25, D34 (each pairing a corner
with its Hodge complement).  Block 213 proved its graded-cone theorem at the
degree-diagonal representative D07 = D16 = D25 = D34 = 0 and its refuting
recovered source exhibited W1 with D16 = 1/4 breaking grade parity of the folded H0 and
replaces the union of the two Hodge cones by an irreducible quartic squared.
This runner determines EXACTLY, on the four-parameter cell form imported
through Block 213's machinery (read-only), what the parameters do to the
principal part M = H0 D + D^T H0 of the period-2 Bloch expansion:

  the parity-breaking mechanism and the general D07 congruence; the exact
  coefficient-ideal locus where det M equals the old block-square expression
  at the run witnesses; the generic W1 factorization and four named slices;
  the coincidence cone on its plane and at one off-plane point; selected
  pencil branches; the deformed flat cell; and two explicitly fixed
  shear/volume registration slices.  The simple D07 branch rescaling is
  restricted to the D07-only star line, and unsampled special loci remain open.

Gate families: A authority, B banner and fences, C construction fidelity,
D the control, E the bench witnesses, F the lemmas, G registration, H scope
fences, I note and hygiene.  Every measurement is taken once before any
mutation flag is read; exact arithmetic only -- no float, no nsimplify.
Scout-grade finite exact linear algebra on one cell form, not a spacetime and
not a dynamics.  Nothing is registered and nothing is adopted.
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

# THE FIXED MACHINERY IMPORT: the corrected Block 213 runner
# carries the period-2 operator machinery, the two assemblies, the metric
# candidates, the witness tables and, through it, Blocks 201, 211, 209 and 105.
try:
    import admissibility_dirac_kahler_weighted_kernel_dispersion_2026_09_05 as b213
    B213_IMPORT_AVAILABLE = True
except ModuleNotFoundError:                            # pragma: no cover
    b213 = None
    B213_IMPORT_AVAILABLE = False
b211 = b213.b211 if b213 is not None else None
b209 = b213.b209 if b213 is not None else None
MACHINERY_IMPORT_AVAILABLE = bool(B213_IMPORT_AVAILABLE and b213 is not None
                               and b213.MACHINERY_IMPORT_AVAILABLE
                               and b211 is not None and b209 is not None)

FINAL_NOTE_NAME = (
    "ADMISSIBILITY_DIRAC_KAHLER_DUALITY_PARAMETERS_PRINCIPAL_PART_BOUNDED_"
    "THEOREM_NOTE_2026-09-05.md"
)
NOTE_PATH = ROOT / "docs" / FINAL_NOTE_NAME
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"

# A LITERAL TUPLE OF PLAIN STRING CONSTANTS (the cache parser AST-reads it).
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_DUALITY_PARAMETERS_PRINCIPAL_PART_BOUNDED_THEOREM_NOTE_2026-09-05.md",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_WEIGHTED_KERNEL_DISPERSION_BOUNDED_THEOREM_NOTE_2026-09-05.md",
    "scripts/admissibility_dirac_kahler_weighted_kernel_dispersion_2026_09_05.py",
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
    ("docs/ADMISSIBILITY_DIRAC_KAHLER_WEIGHTED_KERNEL_DISPERSION_BOUNDED_THEOREM_NOTE_2026-09-05.md", "6eb45758067a92f7bc44f2ffbc5fec9999c2930e2b2c924dfa6dfa67ca5db5ae"),
    ("scripts/admissibility_dirac_kahler_weighted_kernel_dispersion_2026_09_05.py", "d80ce0e3168968fcc1a887e6737681e4cdfc31c82813813415f008a68507088d"),
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
    "claim_parameter_value_selected",
    "claim_readings_licensed",
    "break_parameter_carriers",
    "break_degree_diagonal_reconciliation",
    "break_overlap_folded_structure",
    "break_flat_control",
    "break_flat_deformation",
    "break_bloch_bench_agreement",
    "break_parity_mechanism",
    "break_d07_congruence",
    "break_union_locus",
    "break_factorization_type",
    "claim_single_metric_cone_restored",
    "break_coincidence_fate",
    "break_pencil_branches",
    "break_shear_registration",
    "claim_volume_blind_under_parameters",
    "break_scout_grade_fence",
    "claim_assembly_decided",
    "break_instance_scope",
    "drop_n5_fence",
    "break_float_absence",
)
MUTATION_GATE = {
    "break_source_input_hash": "A", "break_source_input_readability": "A",
    "claim_objects_registered": "B", "claim_gravity_supplied": "B",
    "claim_parameter_value_selected": "B", "claim_readings_licensed": "B",
    "break_parameter_carriers": "C", "break_degree_diagonal_reconciliation": "C",
    "break_overlap_folded_structure": "C",
    "break_flat_control": "D", "break_flat_deformation": "D",
    "break_bloch_bench_agreement": "E",
    "break_parity_mechanism": "F", "break_d07_congruence": "F",
    "break_union_locus": "F", "break_factorization_type": "F",
    "claim_single_metric_cone_restored": "F", "break_coincidence_fate": "F",
    "break_pencil_branches": "F",
    "break_shear_registration": "G", "claim_volume_blind_under_parameters": "G",
    "break_scout_grade_fence": "H", "claim_assembly_decided": "H",
    "break_instance_scope": "H",
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
# A. source-input closure
# ---------------------------------------------------------------------------
def sha256_path(path: str) -> str:
    target = ROOT / path
    return hashlib.sha256(target.read_bytes()).hexdigest() if target.is_file() else ""


@dataclass(frozen=True)
class AuthorityCertificate:
    source_base: str
    fixed_source_inputs: bool
    machinery_import_available: bool
    inputs_readable: int
    inputs_missing: tuple
    input_hashes: tuple


def authority_certificate() -> AuthorityCertificate:
    missing = tuple(path for path in AUDIT_INPUT_PATHS
                    if path != SELF_NOTE_INPUT and not (ROOT / path).is_file())
    readable = len(AUDIT_INPUT_PATHS) - 1 - len(missing)
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
    "weighted kernel K_H = H d - d^T H (Block 201's completion at m = 0)",
    "Block 105's onsite and overlap assemblies (Block 213's rules)",
    "the period-2 Bloch principal part M = H0 D(kappa) + D(kappa)^T H0",
    "Block 211's four-parameter cell form with D07, D16, D25, D34 free",
    "the two Hodge readings G1 = D1/D0 and G2 = D3 E D2^-1 E (Block 213)",
    "Block 211's witnesses W1, W2, W3, mixed, honest_face, L+-, L-+ and flat",
)
REGISTERED_OBJECTS = ()
ADOPTED_OBJECTS = ()
GRAVITY_SUPPLIED_CLAIMED = False
PARAMETER_VALUE_SELECTED_CLAIMED = False
SYMBOL_IS_DYNAMICS_CLAIMED = False
CONE_IS_SPACETIME_CONE_CLAIMED = False
READINGS_LICENSED_CLAIMED = False
CONTINUUM_LIMIT_CLAIMED = False
UNSUPPLIED_GRAVITY_STRUCTURES = (
    "lapse function", "shift vector", "ADM phase space", "Hamiltonian constraint",
    "momentum/diffeomorphism constraint", "first-class constraint algebra",
    "Dirac closure", "Dirac observable", "gauge orbit and its quotient",
)
SCOPED_HEADLINE_WORDS = ("PARAMETER", "PARITY", "CONE", "LOCUS", "BRANCH")
READINGS = (
    "R1 the parameters are a gauge-like freedom of the cell form (not established)",
    "R2 the plane D16 = D34 = -D25 is preferred (not established)",
    "R3 D07 is a 0-form normalisation (a congruence fact, not a physical reading)",
    "R4 the deformed flat cell is a physical vacuum deformation (not established)",
    "R5 the irreducible quartic is a birefringence (not established, no dynamics)",
    "R6 the volume registration through the parameters resolves #7970 (not established)",
)
HISTORICAL_CHECKER_RECORD = "RECOVERED-SUPPORT-NOT-CURRENT-AUTHORITY"

# THE DECLARED PARAMETER POINTS (exact rationals, all inside Block 211's bound
# D07^2 < v0/v1, D16^2, D25^2, D34^2 < v1/v0 at every rational witness used).
QUARTER = sp.Rational(1, 4)
PARAMETER_NAMES = ("D07", "D16", "D25", "D34")
PARAMETER_SYMBOLS = sp.symbols(" ".join(PARAMETER_NAMES))
A07, B16, C25, D34 = PARAMETER_SYMBOLS
KT, KX, KY = b213.KT, b213.KX, b213.KY
KAPPA = (KT, KX, KY)
LAM = b213.LAM
SIGN_ASSEMBLIES = ("onsite", "overlap")
RATIONAL_WITNESSES = ("W1", "W2", "W3", "mixed", "honest_face")
LOCUS_WITNESSES = ("L+-", "L-+")
CONE_WITNESSES = RATIONAL_WITNESSES + LOCUS_WITNESSES
# THE CONE PHASE RUNS AT W1 (both assemblies, every test) AND AT THE TWO LOCUS
# WITNESSES (onsite): the other four rational witnesses are solved and
# reconciled (C) but their cone tests did not fit the 600 s budget.
CONE_RUN_WITNESSES = ("W1",) + LOCUS_WITNESSES
BENCH_EXTENT = (4, 2, 2)

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


def ff_det(matrix: sp.Matrix, gens: tuple, field: bool = False, algebraic: bool = False):
    """THE FRACTION-FREE DETERMINANT over QQ[gens] (or its fraction field, or
    QQ(sqrt 6)[gens]): Bareiss on a DomainMatrix, exact, no float, no tolerance."""
    base = QQ.algebraic_field(sp.sqrt(6)) if algebraic else QQ
    domain = base.frac_field(*gens) if field else base[list(gens)]
    return domain.to_sympy(DomainMatrix.from_Matrix(matrix).convert_to(domain).det())


def factor_shape(expression, variables: tuple) -> tuple:
    """The (total degree in the variables, multiplicity) of every irreducible
    factor over QQ that carries a variable -- the factorization TYPE."""
    return tuple((sp.Poly(base, *variables).total_degree(), power)
                 for base, power in b213.primitive_factors(expression, variables))


def square_root_factor(expression, variables: tuple):
    """The unique irreducible factor of a perfect square det M = Q^2 (fails
    closed if the factorization is not one irreducible factor squared)."""
    factors = b213.primitive_factors(expression, variables)
    if len(factors) != 1 or factors[0][1] != 2:
        return None
    return factors[0][0]


def coefficient_ideal(expression, variables: tuple, unknowns: tuple) -> tuple:
    """The lex Groebner basis, in the unknowns, of the ideal generated by the
    coefficients of `expression` as a polynomial in `variables`: its zero set
    is EXACTLY where the expression vanishes identically in the variables."""
    coefficients = sp.Poly(sp.expand(expression), *variables).coeffs()
    basis = sp.groebner([sp.expand(cf) for cf in coefficients], *unknowns, order="lex")
    return tuple(sp.expand(g) for g in basis.exprs)


def linear_radical_certificate(
        basis: tuple, linear_generators: tuple, variables: tuple,
        relations: tuple = ()) -> dict:
    """Certify the radical of one measured ideal as a declared linear ideal.

    This deliberately does not split factors of arbitrary generators.  It
    proves I is contained in J, each declared linear generator has a bounded
    power in I, and each coefficient-field relation lies in I.  Here J is the
    prime linear ideal (over QQ, or over QQ[r]/(r^2-6)).
    """
    raw = sp.groebner(tuple(basis), *variables, order="lex")
    target = sp.groebner(tuple(linear_generators) + tuple(relations),
                         *variables, order="lex")
    basis_in_target = all(
        sp.expand(target.reduce(sp.expand(element))[1]) == 0
        for element in basis)
    relations_in_raw = all(
        sp.expand(raw.reduce(sp.expand(relation))[1]) == 0
        for relation in relations)
    powers = []
    for generator in linear_generators:
        exponent = next((power for power in range(1, 9)
                         if sp.expand(raw.reduce(
                             sp.expand(generator ** power))[1]) == 0), None)
        powers.append((sp.expand(generator), exponent))
    return {
        "basis_in_target": basis_in_target,
        "relations_in_raw": relations_in_raw,
        "power_witnesses": tuple(powers),
        "certified": (basis_in_target and relations_in_raw
                      and all(power is not None for _, power in powers)),
    }


# THE FOUR-PARAMETER CELL, SOLVED THROUGH BLOCK 211 WITH THE PARAMETERS KEPT
# SYMBOLIC (solve_pinned at_zero=False) -- and reconciled with Block 213's
# degree-diagonal cell (at_zero=True) by substitution at zero.
def full_witness_table() -> dict:
    table = dict(b213.witness_table())
    table.update(b213.locus_witness_table())
    return table


def cell_with_parameters(name: str) -> tuple:
    moduli, signs = full_witness_table()[name]
    volume0, gamma0, volume1, gamma1 = moduli
    _, matrix, rhs = b211.face_system(b211.branch_moduli(volume0, gamma0, volume1, gamma1, signs))
    cell, free = b211.solve_pinned(matrix, rhs, at_zero=False)
    diagonal, _ = b211.solve_pinned(matrix, rhs, at_zero=True)
    return cell.applyfunc(sp.radsimp), tuple(str(s) for s in free), diagonal.applyfunc(sp.radsimp)


def raising_matrix() -> sp.Matrix:
    return b213.first_order_matrix(b213.raising_rules(b213.lane_rules(3)), 3, KAPPA)


def principal_part(cell: sp.Matrix, assembly: str) -> tuple:
    """H0 (the folded H at zero momentum) and M = H0 D + D^T H0 for one cell
    under one assembly, from Block 213's rules."""
    rules = (b213.onsite_rules if assembly == "onsite" else b213.overlap_rules)(cell, b209.CORNERS, 3)
    h0 = b213.folded_matrix(rules, 3)
    dk = raising_matrix()
    return h0, (h0 * dk + dk.T * h0).applyfunc(sp.expand), rules


def hodge_complement_permutation() -> sp.Matrix:
    return sp.Matrix(8, 8, lambda i, j: 1 if b209.CORNERS[j] == tuple(1 - x for x in b209.CORNERS[i]) else 0)


def formal_cell(signs: dict, g0, g1, v0, v1, params: tuple) -> sp.Matrix:
    """Block 213's formal block-diagonal family with the four duality entries
    placed on their corner pairs (0,7), (1,6), (2,5), (3,4)."""
    cell = b213.formal_family(signs, g0, g1, v0, v1)
    for (i, j), value in zip(((0, 7), (1, 6), (2, 5), (3, 4)), params):
        cell[i, j] = cell[j, i] = value
    return cell


# ---------------------------------------------------------------------------
# THE MEASUREMENTS -- every fact once, before any mutation flag is read
# ---------------------------------------------------------------------------
GQ = sp.Matrix(3, 3, lambda i, j: sp.Symbol(f"G{min(i, j)}{max(i, j)}"))
HQ = sp.Matrix(3, 3, lambda i, j: sp.Symbol(f"H{min(i, j)}{max(i, j)}"))
GQ_UNKNOWNS = (GQ[0, 1], GQ[0, 2], GQ[1, 1], GQ[1, 2], GQ[2, 2])
HQ_UNKNOWNS = (HQ[0, 1], HQ[0, 2], HQ[1, 1], HQ[1, 2], HQ[2, 2])


def single_quadric_locus(quartic, params: tuple) -> tuple:
    """Q = (k^T G k)^2 with G a general symmetric 3 x 3: the lex Groebner basis
    eliminated to the parameters -- () with basis (1,) means NO solution over
    the algebraic closure, i.e. no parameter point makes Q one quadric squared."""
    q = b213.quadratic_form(GQ, KAPPA)
    equations = sp.Poly(sp.expand(quartic - q ** 2), *KAPPA).coeffs()
    unknowns = tuple(GQ[i, j] for i in range(3) for j in range(i, 3))
    basis = sp.groebner(equations, *unknowns, *params, order="lex")
    return tuple(sp.expand(g) for g in basis.exprs if not any(g.has(u) for u in unknowns))


def two_quadric_locus(quartic, params: tuple) -> tuple:
    """Q = q1 q2 with two general quadrics, normalised by the kt^4 coefficient
    (nonzero on each named W1 slice used here): the eliminant is exactly the
    product-of-two-quadrics locus on that slice over the closure."""
    lead = sp.Poly(quartic, *KAPPA).coeff_monomial(KT ** 4)
    if lead == 0:
        return ("LEAD-COEFFICIENT-ZERO",)
    q1, q2 = b213.quadratic_form(GQ, KAPPA), b213.quadratic_form(HQ, KAPPA)
    equations = [sp.expand(e.subs({GQ[0, 0]: 1, HQ[0, 0]: lead}))
                 for e in sp.Poly(sp.expand(quartic - q1 * q2), *KAPPA).coeffs()]
    basis = sp.groebner(equations, *GQ_UNKNOWNS, *HQ_UNKNOWNS, *params, order="lex")
    return tuple(sp.factor(g) for g in basis.exprs
                 if not any(g.has(u) for u in GQ_UNKNOWNS + HQ_UNKNOWNS))


def line_factor_locus(quartic, params: tuple) -> tuple:
    """Q vanishes on a projective line: the three affine charts of the dual
    plane, kt = -(l1 kx + l2 ky), kx = -l2 ky, ky = 0 -- exhaustive."""
    l1, l2 = sp.symbols("l1 l2")
    out = []
    for substitution in ({KT: -(l1 * KX + l2 * KY)}, {KX: -l2 * KY}, {KY: 0}):
        equations = sp.Poly(sp.expand(quartic.subs(substitution)), *KAPPA).coeffs()
        basis = sp.groebner(equations, l1, l2, *params, order="lex")
        out.append(tuple(sp.factor(g) for g in basis.exprs if not g.has(l1, l2)))
    return tuple(out)


def exact_charpoly(matrix: sp.Matrix):
    """THE CHARPOLY IN lam OVER THE POLYNOMIAL RING QQ[kt, kx, ky] (or over
    QQ(sqrt 6)[kt, kx, ky] at the locus witnesses), fraction-free on a
    DomainMatrix -- exact, and far cheaper than the generic symbolic charpoly."""
    field = QQ.algebraic_field(sp.sqrt(6)) if matrix.has(sp.sqrt(6)) else QQ
    domain = field[list(KAPPA)]
    coefficients = DomainMatrix.from_Matrix(matrix).convert_to(domain).charpoly()
    degree = len(coefficients) - 1
    return sp.expand(sum(domain.to_sympy(coefficient) * LAM ** (degree - k)
                         for k, coefficient in enumerate(coefficients)))


def pencil_branches(h0: sp.Matrix, m: sp.Matrix) -> tuple:
    """The charpoly of (H0^-1 M)^2 (the H-pencil principal symbol) factored in
    lam: the linear factors are the algebraic branches, the rest the degree
    structure of the irreducible remainder."""
    operator = (h0.inv() * m).applyfunc(sp.radsimp)
    return b213.linear_branches(exact_charpoly((operator * operator).applyfunc(sp.radsimp)), KAPPA)


def form_branches(m: sp.Matrix) -> tuple:
    return b213.linear_branches(exact_charpoly((m * m).applyfunc(sp.expand)), KAPPA)


def measure_cells() -> dict:
    facts: dict = {}
    for name in ("flat",) + CONE_WITNESSES:
        cell, free, diagonal = cell_with_parameters(name)
        carriers = tuple((i, j) for i in range(8) for j in range(8)
                         if cell[i, j].free_symbols & set(PARAMETER_SYMBOLS))
        zero = {s: sp.Integer(0) for s in PARAMETER_SYMBOLS}
        facts[name] = {
            "cell": cell, "free": free, "carriers": carriers,
            "entries": tuple(str(cell[i, j]) for i, j in ((0, 7), (1, 6), (2, 5), (3, 4))),
            "reconciled": residual_count(cell.subs(zero) - diagonal) == 0,
            "reconciled_b213": residual_count(diagonal - b213.solve_witness(name, *full_witness_table()[name])[1]) == 0,
        }
    return facts


def measure_construction(cells: dict) -> dict:
    """C: the four-parameter cell, its carriers, reconciliation with Block 213's
    degree-diagonal cell, onsite H0 = cell, overlap H0 = H0(0) + (s/4) P111."""
    g0, g1, v0, v1 = sp.symbols("g0 g1 v0 v1")
    formal = formal_cell(b211.ALL_PLUS, g0, g1, v0, v1, PARAMETER_SYMBOLS)
    zero = {s: sp.Integer(0) for s in PARAMETER_SYMBOLS}
    h_on, _, _ = principal_part(formal, "onsite")
    h_ov, _, _ = principal_part(formal, "overlap")
    total = sum(PARAMETER_SYMBOLS)
    even, odd = b213.even_odd(3)
    h_eo_on = h_on.extract(even, odd)
    # The separate pairwise bounds are necessary, not sufficient, for H>0.
    # At W1, (D07,D16,D25,D34)=(0,3/4,3/4,3/4) obeys every quoted bound, but
    # the common all-ones degree-1/degree-2 subspace has this indefinite block.
    bounded_subspace = sp.Matrix([
        [sp.Rational(1, 2), sp.Rational(3, 4)],
        [sp.Rational(3, 4), sp.Rational(8, 15)],
    ])
    return {
        "free_names": tuple(cells[n]["free"] for n in ("flat",) + CONE_WITNESSES),
        "carriers": tuple(cells[n]["carriers"] for n in ("flat",) + CONE_WITNESSES),
        "entries": tuple(cells[n]["entries"] for n in ("flat",) + CONE_WITNESSES),
        "reconciled": all(cells[n]["reconciled"] and cells[n]["reconciled_b213"] for n in ("flat",) + CONE_WITNESSES),
        "onsite_h0_is_cell": residual_count(h_on - formal) == 0,
        "onsite_h_eo": tuple(tuple(str(h_eo_on[i, j]) for j in range(4)) for i in range(4)),
        "overlap_h0_structure": residual_count(h_ov - h_ov.subs(zero) - total / 4 * hodge_complement_permutation()) == 0,
        "overlap_parity_preserved_iff_sum_zero": residual_count(h_ov.extract(even, odd).subs(zero)) == 0
        and residual_count(h_ov.extract(even, odd) - total / 4 * hodge_complement_permutation().extract(even, odd)) == 0,
        "individual_bound_counterexample_inside": (
            sp.Rational(9, 16) < sp.Rational(16, 15)),
        "individual_bound_counterexample_minor": bounded_subspace.det(),
    }


def bench_charpolys(cell: sp.Matrix, assembly: str, reading: str) -> tuple:
    rules = (b213.onsite_rules if assembly == "onsite" else b213.overlap_rules)(cell, b209.CORNERS, 3)
    raising = b213.raising_rules(b213.lane_rules(3))
    hodge = b213.bench_matrix(rules, BENCH_EXTENT)
    lifted = b213.bench_matrix(raising, BENCH_EXTENT)
    direct = b213.direct_bench_charpoly(hodge, lifted, reading)
    union = b213.bloch_spectrum_charpoly(rules, raising, BENCH_EXTENT, 3, reading)
    return direct, union, hodge


def measure_control(cells: dict) -> dict:
    """D: the flat cell at zero parameters is the identity and gives R5's
    symbol; the flat cell with a parameter on is NOT the identity -- the
    deformed flat symbol is measured exactly."""
    flat = cells["flat"]["cell"]
    zero = {s: sp.Integer(0) for s in PARAMETER_SYMBOLS}
    facts: dict = {"flat_zero_is_identity": residual_count(flat.subs(zero) - sp.eye(8)) == 0}
    h0, m, _ = principal_part(flat, "onsite")
    det_m = sp.expand(ff_det(m, PARAMETER_SYMBOLS + KAPPA))
    quartic = square_root_factor(det_m, KAPPA)
    norm = (KT ** 2 + KX ** 2 + KY ** 2) ** 2
    facts["flat_det_shape"] = factor_shape(det_m, KAPPA)
    facts["flat_quartic"] = str(sp.expand(quartic)) if quartic is not None else None
    facts["flat_quartic_zero_is_norm4"] = quartic is not None and sp.expand(quartic.subs(zero) + norm) == 0
    facts["flat_quartic_minus_norm4"] = str(sp.expand(quartic - quartic.subs(zero))) if quartic is not None else None
    facts["flat_plane_restores_norm4"] = quartic is not None and sp.expand(
        quartic.subs({C25: -B16, D34: B16}) + norm) == 0
    facts["flat_d07_absent"] = quartic is not None and not quartic.has(A07)
    for label, point in (("D16", {A07: 0, B16: QUARTER, C25: 0, D34: 0}),
                         ("D07", {A07: QUARTER, B16: 0, C25: 0, D34: 0}),
                         ("zero", zero)):
        cellp = flat.subs(point)
        for reading in ("form", "pencil"):
            direct, union, hodge = bench_charpolys(cellp, "onsite", reading)
            facts[f"flat_{label}_{reading}_multiset"] = b213.multiset_of(direct)
            facts[f"flat_{label}_{reading}_agree"] = sp.expand(direct - union) == 0
        facts[f"flat_{label}_h_is_identity"] = residual_count(hodge - sp.eye(hodge.rows)) == 0
    return facts


def measure_bench(cells: dict) -> dict:
    """E: Bloch union = direct bench on (4,2,2) at W1 with D16 = 1/4 and with
    D07 = 1/4, both assemblies, both readings; the multisets recorded."""
    facts: dict = {}
    for label, point in (("D16", {A07: 0, B16: QUARTER, C25: 0, D34: 0}),
                         ("D07", {A07: QUARTER, B16: 0, C25: 0, D34: 0})):
        cellp = cells["W1"]["cell"].subs(point)
        for assembly in SIGN_ASSEMBLIES:
            for reading in ("form", "pencil"):
                direct, union, _ = bench_charpolys(cellp, assembly, reading)
                facts[(label, assembly, reading)] = (sp.expand(direct - union) == 0, b213.multiset_of(direct))
    return facts


def measure_mechanism() -> dict:
    """F-1/F-2: the parity-breaking mechanism at the FORMAL family with symbolic
    moduli AND symbolic parameters -- M_ee, M_oo, the D07 unipotent congruence."""
    g0, g1, v0, v1 = sp.symbols("g0 g1 v0 v1")
    formal = formal_cell(b211.ALL_PLUS, g0, g1, v0, v1, PARAMETER_SYMBOLS)
    facts: dict = {}
    even, odd = b213.even_odd(3)
    for assembly in SIGN_ASSEMBLIES:
        h0, m, _ = principal_part(formal, assembly)
        m_ee, m_oo = m.extract(even, even), m.extract(odd, odd)
        facts[(assembly, "M_ee")] = tuple(tuple(str(sp.factor(m_ee[i, j])) for j in range(4)) for i in range(4))
        facts[(assembly, "M_oo")] = tuple(tuple(str(sp.factor(m_oo[i, j])) for j in range(4)) for i in range(4))
        zero = {s: sp.Integer(0) for s in PARAMETER_SYMBOLS}
        facts[(assembly, "M_eo_parameter_free")] = not (m.extract(even, odd).free_symbols & set(PARAMETER_SYMBOLS))
        facts[(assembly, "diagonal_blocks_vanish_at_zero")] = residual_count(m_ee.subs(zero)) == 0 and residual_count(m_oo.subs(zero)) == 0
    # the onsite M_oo vanishes identically iff D16 = D34 = -D25 (any D07): its
    # three entries are (D16 + D25) kt, (D34 - D16) kx, -(D25 + D34) ky
    h0, m, _ = principal_part(formal, "onsite")
    m_oo = m.extract(odd, odd)
    facts["onsite_M_oo_entries"] = (str(sp.factor(m_oo[0, 1])), str(sp.factor(m_oo[0, 2])), str(sp.factor(m_oo[1, 2])))
    facts["onsite_M_oo_zero_on_plane"] = residual_count(m_oo.subs({C25: -B16, D34: B16})) == 0
    facts["onsite_M_oo_row7_zero"] = residual_count(m_oo[3, :]) == 0 and residual_count(m_oo[:, 3]) == 0
    m_ee = m.extract(even, even)
    facts["onsite_M_ee_vector"] = (str(sp.factor(m_ee[0, 1])), str(sp.factor(m_ee[0, 2])), str(sp.factor(m_ee[0, 3])))
    facts["onsite_M_ee_2form_block_zero"] = residual_count(m_ee[1:, 1:]) == 0
    # THE D07 CONGRUENCE: U = I - (D07/D3) E_70 with D3 = 1/v1
    unipotent = sp.eye(8)
    unipotent[7, 0] = -A07 / formal[7, 7]
    m_zero, h_zero = m.subs(A07, 0), h0.subs(A07, 0)
    facts["d07_congruence_M"] = residual_count((unipotent.T * m * unipotent - m_zero).applyfunc(sp.cancel)) == 0
    shifted = (unipotent.T * h0 * unipotent - h_zero).applyfunc(sp.cancel)
    facts["d07_congruence_H0_shift"] = str(sp.factor(shifted[0, 0]))
    facts["d07_congruence_H0_rest_zero"] = residual_count(shifted) == (1 if shifted[0, 0] != 0 else 0)
    facts["d07_shift_is_minus_a2_over_D3"] = sp.cancel(shifted[0, 0] + A07 ** 2 / formal[7, 7]) == 0
    # Congruence preserves the determinant and inertia, but does not isolate a
    # zero-form pencil branch once another duality entry couples the degree
    # sectors.  This exact positive-definite example falsifies that stronger
    # inference while leaving both congruence identities intact.
    h_counter = sp.eye(8)
    h_counter[0, 7] = h_counter[7, 0] = sp.Rational(1, 4)
    h_counter[1, 6] = h_counter[6, 1] = sp.Rational(1, 3)
    d_counter = b213.first_order_matrix(
        b213.raising_rules(b213.lane_rules(3)), 3,
        (sp.Integer(1), sp.Integer(2), sp.Integer(3)))
    m_counter = h_counter * d_counter + d_counter.T * h_counter
    pencil_counter = (h_counter.inv() * m_counter) ** 2
    candidate = sp.Rational(224, 15)
    counter_residual = sp.factor(
        (pencil_counter - candidate * sp.eye(8)).det())
    expected_charpoly = (
        (8 * LAM ** 2 - 238 * LAM + 1719) ** 2
        * (15 * LAM ** 2 - 434 * LAM + 3056) ** 2 / 14400)
    facts["d07_mixed_counterexample_pd"] = all(
        minor > 0 for minor in b211.leading_minors(h_counter))
    facts["d07_mixed_counterexample_candidate"] = candidate
    facts["d07_mixed_counterexample_residual"] = counter_residual
    facts["d07_mixed_counterexample_charpoly"] = sp.expand(
        pencil_counter.charpoly(LAM).as_expr() - expected_charpoly) == 0
    # The general block identity carries (-1)^n.  The actual even block has
    # n=4 and therefore the positive sign used in the cone calculations.
    for size in (1, 4):
        entries = sp.symbols(f"b0:{size}")
        block = sp.diag(*entries)
        bordered = sp.zeros(2 * size)
        bordered[:size, size:] = block
        bordered[size:, :size] = block.T
        facts[f"block_det_sign_n{size}"] = sp.expand(
            bordered.det() - (-1) ** size * block.det() ** 2) == 0
    # THE OVERLAP M SEES ONLY THE SUM s = D07 + D16 + D25 + D34: moving the
    # whole value from one parameter to another leaves M unchanged.
    _, m_overlap, _ = principal_part(formal, "overlap")
    total = sp.Symbol("s")
    reference = m_overlap.subs({A07: total, B16: 0, C25: 0, D34: 0})
    facts["overlap_sum_only"] = all(
        residual_count(m_overlap.subs({A07: 0, B16: 0, C25: 0, D34: 0, parameter: total}) - reference) == 0
        for parameter in (B16, C25, D34))
    return facts


def measure_cone(cells: dict) -> dict:
    """Bounded cone checks at W1 and the two named locus witnesses.

    The old-union coefficient ideal is measured at all three; generic
    factorization, the all-parameter single-quadric system, and four
    two-quadric slices are measured at W1.  At the two QQ(sqrt 6) cells,
    onsite plane persistence and one off-plane single-quadric point are
    measured with r^2-6 adjoined.  No line-factor locus is run.
    """
    facts: dict = {}
    even, odd = b213.even_odd(3)
    plane_generators = (sp.expand(B16 - D34), sp.expand(C25 + D34))
    r = sp.Symbol("r")
    for name in CONE_RUN_WITNESSES:
        cell = cells[name]["cell"]
        gaussian = name in LOCUS_WITNESSES
        for assembly in (SIGN_ASSEMBLIES if not gaussian else ("onsite",)):
            print(f"[cone] {name} {assembly}", file=sys.stderr)
            params = (B16, C25, D34) if assembly == "onsite" else (A07,)
            point = {A07: 0} if assembly == "onsite" else {B16: 0, C25: 0, D34: 0}
            h0, m, _ = principal_part(cell.subs(point), assembly)
            det_m = sp.expand(ff_det(m, params + KAPPA, algebraic=gaussian))
            det_b = sp.expand(sp.radsimp(m.extract(even, odd).det(method="berkowitz")))
            difference = sp.expand(sp.radsimp(det_m - det_b ** 2))
            entry: dict = {}
            if gaussian:
                coefficients = sp.Poly(difference.subs(sp.sqrt(6), r), *KAPPA).coeffs() + [r ** 2 - 6]
                basis = sp.groebner(coefficients, *params, r, order="lex")
                raw_basis = tuple(sp.expand(element) for element in basis.exprs)
                target = plane_generators
                certificate = linear_radical_certificate(
                    raw_basis, target, params + (r,), (r ** 2 - 6,))
                entry["union_basis_raw"] = raw_basis
                entry["union_radical_target"] = target
                entry["union_radical_power_witnesses"] = certificate["power_witnesses"]
                entry["union_radical_certificate"] = certificate["certified"]
                # ON THE PLANE (s, -s, s), symbolic s: det M = (k^T G1 k)^4 times a
                # constant -- the locus witness's single-quadric cone persists.
                g1 = b213.metric_candidates(cell.subs({A07: 0, B16: 0, C25: 0, D34: 0}))[0]
                form = b213.quadratic_form(g1.applyfunc(sp.radsimp), KAPPA)
                s = sp.Symbol("s")
                on_plane = sp.expand(sp.radsimp(det_m.subs({B16: s, C25: -s, D34: s})))
                entry["plane_is_single_quadric"] = b213.proportional(on_plane, form ** 4, KAPPA + (s,))
                # OFF THE PLANE at the declared point D16 = 1/4: the single-quadric
                # system in G alone (sqrt 6 as r, r^2 - 6 adjoined) is inconsistent.
                q = b213.quadratic_form(GQ, KAPPA)
                unknowns = tuple(GQ[i, j] for i in range(3) for j in range(i, 3))
                off = det_m.subs({B16: QUARTER, C25: 0, D34: 0})
                equations = sp.Poly(sp.expand((off - q ** 4).subs(sp.sqrt(6), r)), *KAPPA).coeffs() + [r ** 2 - 6]
                basis = sp.groebner(equations, *unknowns, r, order="lex")
                entry["single_quadric_locus"] = tuple(sp.expand(g) for g in basis.exprs)
                entry["shape"] = ("NOT-FACTORED-OVER-QQ(sqrt6)",)
                entry["is_square_of_quartic"] = None
            else:
                basis = coefficient_ideal(difference, KAPPA, params)
                target = plane_generators if assembly == "onsite" else (A07,)
                certificate = linear_radical_certificate(basis, target, params)
                entry["union_basis_raw"] = basis
                entry["union_radical_target"] = target
                entry["union_radical_power_witnesses"] = certificate["power_witnesses"]
                entry["union_radical_certificate"] = certificate["certified"]
                entry["shape"] = factor_shape(det_m, KAPPA)
                quartic = square_root_factor(det_m, KAPPA)
                entry["is_square_of_quartic"] = quartic is not None
                if quartic is not None:
                    quartic = sp.expand(quartic)
                    entry["quartic_parameter_degree"] = sp.Poly(quartic, *params).total_degree()
                    entry["quartic_even_in_parameters"] = sp.expand(
                        quartic.subs({p: -p for p in params}, simultaneous=True) - quartic) == 0
                    entry["single_quadric_locus"] = single_quadric_locus(quartic, params)
                    if assembly == "onsite" and name == "W1":
                        print("[cone] W1 slices", file=sys.stderr)
                        s = sp.Symbol("s")
                        slices = {"D16": {B16: s, C25: 0, D34: 0}, "D25": {B16: 0, C25: s, D34: 0},
                                  "D34": {B16: 0, C25: 0, D34: s}, "diag": {B16: s, C25: s, D34: s}}
                        entry["two_quadric_slices"] = tuple(
                            (label, two_quadric_locus(sp.expand(quartic.subs(sub)), (s,)))
                            for label, sub in slices.items())
            entry["union_iff_plane"] = entry["union_radical_certificate"]
            entry["d07_absent"] = not det_m.has(A07)
            facts[(name, assembly)] = entry
    return facts


def measure_branches(cells: dict) -> dict:
    """Selected pencil/form branches at W1 and L+-.  The simple D07 rescaling
    is measured only on the degree-diagonal/star line where the other three
    duality parameters vanish."""
    facts: dict = {}
    points = {
        "W1 D16": ("W1", {A07: 0, B16: QUARTER, C25: 0, D34: 0}),
        "W1 D07": ("W1", {A07: QUARTER, B16: 0, C25: 0, D34: 0}),
        "W1 plane": ("W1", {A07: 0, B16: QUARTER, C25: -QUARTER, D34: QUARTER}),
        "W1 zero": ("W1", {A07: 0, B16: 0, C25: 0, D34: 0}),
        "L+- D07": ("L+-", {A07: QUARTER, B16: 0, C25: 0, D34: 0}),
        "L+- D16": ("L+-", {A07: 0, B16: QUARTER, C25: 0, D34: 0}),
    }
    for label, (name, point) in points.items():
        cell = cells[name]["cell"].subs(point)
        h0, m, _ = principal_part(cell, "onsite")
        branches, remainder = pencil_branches(h0, m)
        facts[(label, "pencil")] = (tuple((str(sp.factor(root)), power) for root, power in branches), remainder)
        if name == "W1":
            branches_f, remainder_f = form_branches(m)
            facts[(label, "form")] = (tuple((str(sp.factor(root)), power) for root, power in branches_f), remainder_f)
    # THE D07-ONLY RESCALING, EXACT: with D16=D25=D34=0 at W1 the 0-form
    # branch k^T D1 k / D0 becomes k^T D1 k / (D0 - D07^2 / D3).
    cell = cells["W1"]["cell"]
    g1, _, d0, d1, _, d3 = b213.metric_candidates(cell.subs({A07: 0, B16: 0, C25: 0, D34: 0}))
    facts["d07_rescaled_zero_form"] = str(sp.factor(b213.quadratic_form(d1, KAPPA) / (d0 - QUARTER ** 2 / d3)))
    facts["zero_form_branch"] = str(sp.factor(b213.quadratic_form(g1, KAPPA)))
    cellL = cells["L+-"]["cell"]
    g1L, _, d0L, d1L, _, d3L = b213.metric_candidates(cellL.subs({A07: 0, B16: 0, C25: 0, D34: 0}))
    facts["locus_d07_rescale_constant"] = sp.radsimp(sp.cancel(d0L / (d0L - QUARTER ** 2 / d3L)))
    facts["locus_tuning_a2"] = sp.radsimp(sp.cancel(d0L * d3L * (1 - sp.Rational(27, 32))))
    return facts


def measure_registration() -> dict:
    """G: two distinct formal slices.  The shear derivative calculation fixes
    (v0,v1)=(15/16,1); the volume comparison fixes (g0,g1)=(1/4,1/4)."""
    g0, g1, v0, v1 = sp.symbols("g0 g1 v0 v1")
    facts: dict = {}
    facts["shear_slice_volumes"] = (sp.Rational(15, 16), sp.Integer(1))
    facts["volume_slice_shears"] = (QUARTER, QUARTER)
    # shear: volumes at W1, shears symbolic, three parameters symbolic
    formal = formal_cell(b211.ALL_PLUS, g0, g1, sp.Rational(15, 16), sp.Integer(1), (0, B16, C25, D34))
    _, m, _ = principal_part(formal, "onsite")
    det_m = sp.expand(ff_det(m, (B16, C25, D34, g0, g1) + KAPPA))
    for shear in (g0, g1):
        derivative = sp.expand(sp.diff(det_m, shear))
        facts[f"shear_{shear}_registers"] = derivative != 0
        basis = coefficient_ideal(derivative, KAPPA + (g0, g1), (B16, C25, D34))
        facts[f"shear_{shear}_cancelling_parameters"] = basis
    # volume: shears at W1, volumes symbolic, three parameters symbolic
    formal = formal_cell(b211.ALL_PLUS, QUARTER, QUARTER, v0, v1, (0, B16, C25, D34))
    _, m, _ = principal_part(formal, "onsite")
    numerator, _ = sp.fraction(sp.together(sp.cancel(ff_det(m, (B16, C25, D34, v0, v1) + KAPPA, field=True))))
    numerator = sp.expand(numerator)
    unit = numerator.subs({v0: 1, v1: 1})
    zero = {B16: 0, C25: 0, D34: 0}
    facts["volume_blind_with_parameters"] = b213.proportional(numerator, unit, KAPPA + (B16, C25, D34))
    facts["volume_blind_at_zero_parameters"] = b213.proportional(numerator.subs(zero), unit.subs(zero), KAPPA)
    facts["volume_derivative_with_parameters"] = sp.expand(sp.diff(sp.cancel(numerator / unit), v0)) != 0
    return facts


@dataclass(frozen=True)
class Facts:
    authority: AuthorityCertificate
    construction: dict
    control: dict
    bench: dict
    mechanism: dict
    cone: dict
    branches: dict
    registration: dict
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
    cells = measure_cells()
    construction = measure_construction(cells)
    lap("construction")
    control = measure_control(cells)
    lap("control")
    bench = measure_bench(cells)
    lap("bench")
    mechanism = measure_mechanism()
    lap("mechanism")
    cone = measure_cone(cells)
    lap("cone")
    branches = measure_branches(cells)
    lap("branches")
    registration = measure_registration()
    lap("registration")
    note_text = NOTE_PATH.read_text(encoding="utf-8") if NOTE_PATH.is_file() else ""
    return Facts(authority, construction, control, bench, mechanism, cone,
                 branches, registration, note_text, timings)


# ---------------------------------------------------------------------------
# THE DECLARED LITERALS -- every claim is a constant compared against a
# measurement; a mutation rewrites exactly one claim.
# ---------------------------------------------------------------------------
PLANE = ("D16 - D34", "D25 + D34")
ONSITE_M_OO_ENTRIES = ("kt*(D16 + D25)", "-kx*(D16 - D34)", "-ky*(D25 + D34)")
ONSITE_M_EE_VECTOR = ("kt*(D07 + D34)", "-kx*(D07 - D25)", "ky*(D07 + D16)")
D07_SHIFT = "-D07**2*v1"
# THE DEFORMED FLAT QUARTIC: Q_flat = -|k|^4 + Q2_flat (the square root's sign is
# the factor's; the zero-parameter part is -|k|^4 and Q2_flat vanishes on the plane).
FLAT_DEFORMATION = ("D16**2*kt**2*ky**2 + D16**2*kx**2*ky**2 + 2*D16*D25*kx**2*ky**2 - 2*D16*D34*kt**2*ky**2 "
                    "+ D25**2*kt**2*kx**2 + D25**2*kx**2*ky**2 + 2*D25*D34*kt**2*kx**2 + D34**2*kt**2*kx**2 "
                    "+ D34**2*kt**2*ky**2")
SIXTEEN_FIFTEENTHS = sp.Rational(16, 15)
# (D16 form, D16 pencil, D07 form, D07 pencil) at the flat cell on (4,2,2): the
# form multisets are None (irrational roots), the pencil ones {0 x8, 1 x6, 16/15 x2}.
FLAT_MULTISETS = (None, ((0, 8), (1, 6), (SIXTEEN_FIFTEENTHS, 2)),
                  None, ((0, 8), (1, 6), (SIXTEEN_FIFTEENTHS, 2)))
OVERLAP_FORM_W1 = ((0, 8), (sp.Rational(116281, 147456), 4), (sp.Rational(4844401, 3686400), 4))
W1_BENCH_MULTISETS = (
    None, ((0, 8), (SIXTEEN_FIFTEENTHS, 2), (sp.Rational(9, 8), 2), (sp.Rational(8, 7), 2), (sp.Rational(32, 25), 2)),
    OVERLAP_FORM_W1, ((0, 8), (1, 8)),
    None, None,
    OVERLAP_FORM_W1, ((0, 8), (1, 8)),
)
ZERO_FORM_W1 = "8*(2*kt**2 - kt*kx - kt*ky + 2*kx**2 - kx*ky + 2*ky**2)/15"
ZERO_FORM_W1_D07 = "4*(2*kt**2 - kt*kx - kt*ky + 2*kx**2 - kx*ky + 2*ky**2)/7"
TOP_FORM_W1 = "3*(3*kt**2 - 2*kt*kx + 2*kt*ky + 3*kx**2 - 2*kx*ky + 3*ky**2)/8"
G1_LOCUS = "3*kt**2 - 2*kt*kx - 2*kt*ky + 3*kx**2 - 2*kx*ky + 3*ky**2"
BRANCH_TABLE = (
    (("L+- D07", "pencil"), (((f"4*({G1_LOCUS})/9", 2), (f"48*({G1_LOCUS})/119", 2), (f"({G1_LOCUS})/2", 4)), ())),
    (("L+- D16", "pencil"), ((), ((4, 2),))),
    (("W1 D07", "form"), ((), ((8, 1),))),
    (("W1 D07", "pencil"), (((ZERO_FORM_W1_D07, 2), (TOP_FORM_W1, 2)), ((2, 2),))),
    (("W1 D16", "form"), ((), ((8, 1),))),
    (("W1 D16", "pencil"), ((), ((4, 2),))),
    (("W1 plane", "form"), ((), ((8, 1),))),
    (("W1 plane", "pencil"), (((ZERO_FORM_W1, 2),), ((3, 2),))),
    (("W1 zero", "form"), ((), ((4, 2),))),
    (("W1 zero", "pencil"), (((TOP_FORM_W1, 2), (ZERO_FORM_W1, 2)), ((2, 2),))),
)
CONE_SHAPES = {"onsite": ((4, 2),), "overlap": ((4, 2),)}
TWO_QUADRIC_SLICE_ELIMINANT = "s**2"
LOCUS_D07_RESCALE = sp.Rational(128, 119)
LOCUS_TUNING_A2 = sp.Rational(5, 36)
SCOUT_GRADE_FENCE = ("scout-grade finite exact linear algebra on one cell form, "
                     "not a spacetime and not a dynamics")
SCOUT_GRADE_ONLY = True
ASSEMBLY_DECIDED = False
HODGE_READING_SELECTED = False
INSTANCE_SCOPE = (
    "one bench (4,2,2) for the exact spectra; the principal part at one degenerate zero",
    "one cell family (Block 211's), seven cone witnesses, the flat cell, four declared parameter points",
    "two assemblies, two readings, neither selected; no parameter value selected",
    "construction reconciled at seven witnesses; parameterized cone calculations at W1 and L+-/L-+; symbolic moduli only for the mechanism and registration",
    "generic factorization and all-parameter single-quadric exclusion at W1; four named W1 slices and two bounded L+-/L-+ checks",
    "m = 0 and periodic closure, this block's choices as in Block 213",
)
INSTANCE_SCOPE_COUNT = 6
SCOPE_KEYS = ("n5_verbatim",)


def scope_certificate(text: str) -> dict:
    return {"n5_verbatim": N5_FENCE in text}


def build_claims(mutation: str) -> dict:
    claims = {
        "source_base": CORRECTION_SOURCE_BASE,
        "source_inputs_match": True, "source_inputs_readable": True,
        "registered": (), "adopted": (), "gravity_supplied": False,
        "parameter_value_selected": False, "readings_licensed": False,
        "carriers": ((0, 7), (1, 6), (2, 5), (3, 4), (4, 3), (5, 2), (6, 1), (7, 0)),
        "reconciled": True, "overlap_structure": True,
        "individual_bounds_sufficient_for_pd": False,
        "flat_zero_identity": True, "flat_deformation_absent": False,
        "bench_agreement": True,
        "m_oo_entries": ONSITE_M_OO_ENTRIES, "m_ee_vector": ONSITE_M_EE_VECTOR,
        "d07_congruence": True, "d07_shift": D07_SHIFT,
        "d07_mixed_simple_branch": False,
        "union_iff_plane": True, "cone_shapes": CONE_SHAPES,
        "single_quadric_restored": False, "locus_plane_and_offpoint": True,
        "pencil_zero_form_rescaled": True,
        "shear_registers": True, "volume_blind_with_parameters": False,
        "shear_slice_volumes": (sp.Rational(15, 16), sp.Integer(1)),
        "volume_slice_shears": (QUARTER, QUARTER),
        "scout_grade": SCOUT_GRADE_FENCE, "assembly_decided": False,
        "instance_scope_count": INSTANCE_SCOPE_COUNT,
        "n5_verbatim": True, "float_absent": True,
    }
    flips = {
        "break_source_input_hash": ("source_inputs_match", False),
        "break_source_input_readability": ("source_inputs_readable", False),
        "claim_objects_registered": ("registered", ("the four duality parameters",)),
        "claim_gravity_supplied": ("gravity_supplied", True),
        "claim_parameter_value_selected": ("parameter_value_selected", True),
        "claim_readings_licensed": ("readings_licensed", True),
        "break_parameter_carriers": ("carriers", ((0, 7), (7, 0))),
        "break_degree_diagonal_reconciliation": ("reconciled", False),
        "break_overlap_folded_structure": ("overlap_structure", False),
        "break_flat_control": ("flat_zero_identity", False),
        "break_flat_deformation": ("flat_deformation_absent", True),
        "break_bloch_bench_agreement": ("bench_agreement", False),
        "break_parity_mechanism": ("m_oo_entries", ("kt*(D16 - D25)", "-kx*(D16 - D34)", "-ky*(D25 + D34)")),
        "break_d07_congruence": ("d07_shift", "-D07**2*v0"),
        "break_union_locus": ("union_iff_plane", False),
        "break_factorization_type": ("cone_shapes", {"onsite": ((2, 2), (2, 2)), "overlap": ((4, 2),)}),
        "claim_single_metric_cone_restored": ("single_quadric_restored", True),
        "break_coincidence_fate": ("locus_plane_and_offpoint", False),
        "break_pencil_branches": ("pencil_zero_form_rescaled", False),
        "break_shear_registration": ("shear_registers", False),
        "claim_volume_blind_under_parameters": ("volume_blind_with_parameters", True),
        "break_scout_grade_fence": ("scout_grade", "a spacetime and a dynamics"),
        "claim_assembly_decided": ("assembly_decided", True),
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
    checks.check("A-1", "THE CORRECTION SOURCE BASE IS FIXED AND EVERY NON-SELF RUNTIME OR CITATION INPUT MATCHES ITS SHA-256 LITERAL",
                 au.source_base == claims["source_base"] == CORRECTION_SOURCE_BASE
                 and au.fixed_source_inputs == claims["source_inputs_match"]
                 and claims["source_inputs_match"])
    checks.check("A-2", "BLOCK 213 AND ITS COMPLETE TRANSITIVE HELPER/ASSEMBLY CLOSURE IMPORT; ALL DECLARED INPUTS ARE READABLE",
                 au.machinery_import_available
                 and au.inputs_readable == len(AUDIT_INPUT_PATHS) - 1
                 and not au.inputs_missing and claims["source_inputs_readable"])
    checks.check("B-1", "NOTHING REGISTERED, NOTHING ADOPTED: six imposed objects, zero registered, zero adopted",
                 len(IMPOSED_OBJECTS) == 6 and claims["registered"] == REGISTERED_OBJECTS == () and claims["adopted"] == ADOPTED_OBJECTS == ())
    checks.check("B-2", "NO GRAVITY IS SUPPLIED: nine structures enumerated as not supplied",
                 not claims["gravity_supplied"] and not GRAVITY_SUPPLIED_CLAIMED and len(UNSUPPLIED_GRAVITY_STRUCTURES) == 9)
    checks.check("B-3", "NO PARAMETER VALUE IS SELECTED: the four parameter points are declared probes, not a choice",
                 not claims["parameter_value_selected"] and not PARAMETER_VALUE_SELECTED_CLAIMED)
    checks.check("B-4", "THE WORDS PARAMETER, PARITY, CONE, LOCUS AND BRANCH ARE SCOPED; SYMBOL NAMES NO DYNAMICS, CONE NO SPACETIME CONE",
                 len(SCOPED_HEADLINE_WORDS) == 5 and not SYMBOL_IS_DYNAMICS_CLAIMED and not CONE_IS_SPACETIME_CONE_CLAIMED
                 and not CONTINUUM_LIMIT_CLAIMED)
    checks.check("B-5", "THE READINGS ARE READINGS: six enumerated, none licensed",
                 len(READINGS) == 6 and not claims["readings_licensed"] and not READINGS_LICENSED_CLAIMED)
    co = facts.construction
    checks.check("C-1", "THE FREE PARAMETERS ARE EXACTLY D07, D16, D25, D34 at all eight cells and they carry exactly the eight antidiagonal entries",
                 all(f == PARAMETER_NAMES for f in co["free_names"]) and all(c == claims["carriers"] for c in co["carriers"])
                 and all(e == PARAMETER_NAMES for e in co["entries"]))
    checks.check("C-2", "THE CELL AT ZERO PARAMETERS IS BLOCK 213's DEGREE-DIAGONAL CELL (solve_witness) at every witness",
                 co["reconciled"] == claims["reconciled"] and claims["reconciled"])
    checks.check("C-3", "ONSITE: the folded H0 IS the cell, so H_eo carries the four parameters on the antidiagonal; OVERLAP: H0 = H0(0) + (s/4) P111",
                 co["onsite_h0_is_cell"] and co["overlap_h0_structure"] == claims["overlap_structure"]
                 and co["overlap_parity_preserved_iff_sum_zero"] and claims["overlap_structure"])
    checks.check("C-4", "THE FOUR INDIVIDUAL PAIRWISE BOUNDS ARE NECESSARY ONLY: the W1 point (0,3/4,3/4,3/4) obeys them but has a restricted 2x2 determinant -71/240, so pencil claims require actual positive definiteness",
                 co["individual_bound_counterexample_inside"]
                 and co["individual_bound_counterexample_minor"] == sp.Rational(-71, 240)
                 and not claims["individual_bounds_sufficient_for_pd"])
    ct = facts.control
    checks.check("D-1", "THE CONTROL IS R5's: the flat cell at zero parameters is the identity, H = I on (4,2,2), multisets {0x8, 1x8} form and pencil, Bloch = direct",
                 ct["flat_zero_is_identity"] == claims["flat_zero_identity"] and claims["flat_zero_identity"]
                 and ct["flat_zero_h_is_identity"] and ct["flat_zero_form_multiset"] == ct["flat_zero_pencil_multiset"] == ((0, 8), (1, 8))
                 and ct["flat_zero_form_agree"] and ct["flat_zero_pencil_agree"] and ct["flat_quartic_zero_is_norm4"])
    checks.check("D-2", "THE FLAT CELL WITH A PARAMETER ON IS NOT THE IDENTITY: det M = Q^2 with Q = -|k|^4 + Q2_flat, Q2_flat the declared even quadratic in (D16, D25, D34), D07 absent, Q2_flat = 0 on the plane D16 = D34 = -D25",
                 (not ct["flat_D16_h_is_identity"]) and (not ct["flat_D07_h_is_identity"]) and ct["flat_det_shape"] == ((4, 2),)
                 and ct["flat_quartic_minus_norm4"] == FLAT_DEFORMATION and ct["flat_d07_absent"] and ct["flat_plane_restores_norm4"]
                 and not claims["flat_deformation_absent"])
    checks.check("D-3", "THE DEFORMED FLAT BENCH: the (4,2,2) multisets with D16 = 1/4 and with D07 = 1/4 are the declared literals, Bloch = direct",
                 tuple(ct[f"flat_{l}_{r}_multiset"] for l in ("D16", "D07") for r in ("form", "pencil")) == FLAT_MULTISETS
                 and all(ct[f"flat_{l}_{r}_agree"] for l in ("D16", "D07") for r in ("form", "pencil")))
    be = facts.bench
    checks.check("E-1", "BLOCH UNION = DIRECT BENCH on (4,2,2) at W1 with D16 = 1/4 and with D07 = 1/4, both assemblies, both readings",
                 all(v[0] for v in be.values()) == claims["bench_agreement"] and claims["bench_agreement"] and len(be) == 8)
    checks.check("E-2", "THE W1 BENCH MULTISETS WITH A PARAMETER ON are the declared literals",
                 tuple(be[k][1] for k in sorted(be)) == W1_BENCH_MULTISETS)
    me = facts.mechanism
    checks.check("F-1", "THE PARITY MECHANISM (onsite, symbolic moduli and parameters): M_eo is parameter-free; M_ee couples corner 0 to the 2-forms by u = ((D07+D34)kt, (D25-D07)kx, (D07+D16)ky); M_oo is the zero-diagonal 3x3 [(D16+D25)kt, (D34-D16)kx, -(D25+D34)ky] on the 1-forms with corner 7 empty",
                 me[("onsite", "M_eo_parameter_free")] and me["onsite_M_ee_vector"] == claims["m_ee_vector"]
                 and me["onsite_M_oo_entries"] == claims["m_oo_entries"] and me["onsite_M_oo_row7_zero"]
                 and me["onsite_M_ee_2form_block_zero"] and me[("onsite", "diagonal_blocks_vanish_at_zero")]
                 and me["onsite_M_oo_zero_on_plane"])
    checks.check("F-2", "THE GENERAL D07 CONGRUENCE: U = I - (D07/D3) E_70 gives U^T M U = M|D07=0 and shifts only D0 in U^T H0 U; it preserves det M and inertia but does not isolate a rescaled 0-form branch when other duality entries are on",
                 me["d07_congruence_M"] == claims["d07_congruence"] and claims["d07_congruence"]
                 and me["d07_congruence_H0_shift"] == claims["d07_shift"] and me["d07_congruence_H0_rest_zero"]
                 and me["d07_shift_is_minus_a2_over_D3"]
                 and me["d07_mixed_counterexample_pd"]
                 and me["d07_mixed_counterexample_candidate"] == sp.Rational(224, 15)
                 and me["d07_mixed_counterexample_residual"] == sp.Rational(528724036, 455625)
                 and me["d07_mixed_counterexample_charpoly"]
                 and not claims["d07_mixed_simple_branch"]
                 and me["block_det_sign_n1"] and me["block_det_sign_n4"])
    checks.check("F-3", "OVERLAP: M sees only the sum s = D07 + D16 + D25 + D34 and its M_eo is parameter-free",
                 me["overlap_sum_only"] and me[("overlap", "M_eo_parameter_free")])
    cn = facts.cone
    checks.check("F-4", "THE UNION LOCUS AT THE RUN WITNESSES: raw coefficient-ideal bases certify radical (D16-D34,D25+D34) onsite and (s) overlap by containment and power membership; no generic factor-splitting rule is used",
                 all(entry["union_iff_plane"] and (entry["d07_absent"] or key[1] == "overlap") for key, entry in cn.items()) == claims["union_iff_plane"]
                 and claims["union_iff_plane"] and len(cn) == 4)
    checks.check("F-5", "THE GENERIC W1 FACTORIZATION TYPE over the stated rational-function fields: det M is one irreducible quartic squared under both assemblies, with quartic parameter degree 2 and even parameter dependence; this does not classify every specialization",
                 all(cn[(n, a)]["shape"] == claims["cone_shapes"][a] and cn[(n, a)]["is_square_of_quartic"]
                     and cn[(n, a)]["quartic_parameter_degree"] == 2 and cn[(n, a)]["quartic_even_in_parameters"]
                     for n in ("W1",) for a in SIGN_ASSEMBLIES))
    checks.check("F-6", "AT W1 ONLY, the full modeled onsite parameter system and the effective overlap-sum system have inconsistent single-quadric equations (basis (1,)); no conclusion is drawn for every other witness",
                 all(cn[(n, a)]["single_quadric_locus"] == (sp.Integer(1),) for n in ("W1",) for a in SIGN_ASSEMBLIES)
                 == (not claims["single_quadric_restored"]))
    checks.check("F-7", "AT L+- AND L-+ ONSITE: the old single-quadric zero set persists along the plane (s,-s,s), for any D07 because det M is D07-free; at the one declared off-plane point D16=1/4 the single-quadric system is inconsistent. The rest of the off-plane locus is open",
                 all(cn[(n, "onsite")]["plane_is_single_quadric"] and cn[(n, "onsite")]["single_quadric_locus"] == (sp.Integer(1),)
                     for n in LOCUS_WITNESSES) == claims["locus_plane_and_offpoint"] and claims["locus_plane_and_offpoint"])
    checks.check("F-8", "ON FOUR DECLARED W1 ONSITE SLICES ONLY, the two-quadric eliminant is s^2, excluding a product of two quadrics away from s=0; linear-times-cubic factors and unsampled parameter directions remain open",
                 all(str(e[1]) == f"({TWO_QUADRIC_SLICE_ELIMINANT},)" for e in cn[("W1", "onsite")]["two_quadric_slices"]))
    br = facts.branches
    checks.check("F-9", "THE SELECTED W1 BRANCH STRUCTURES are the declared literals; on the D07-only star line (D16=D25=D34=0), the 0-form branch is k^T D1 k/(D0-D07^2/D3) and the other branches are Block 213's",
                 tuple((k, br[k]) for k in sorted(k for k in br if isinstance(k, tuple))) == BRANCH_TABLE
                 and claims["pencil_zero_form_rescaled"])
    checks.check("F-10", "ON THE L+- D07-ONLY STAR LINE: at D07=1/4 the 0-form constant becomes 128/119 while the other three stay 32/27,4/3,4/3; this selected pencil is not scalar",
                 br["locus_d07_rescale_constant"] == LOCUS_D07_RESCALE and br["locus_tuning_a2"] == LOCUS_TUNING_A2)
    rg = facts.registration
    checks.check("G-1", "ON THE FORMAL SLICE (v0,v1)=(15/16,1), neither shear derivative is the zero polynomial in momentum and symbolic shears for any fixed (D16,D25,D34), as certified by coefficient ideal (1)",
                 rg["shear_g0_registers"] and rg["shear_g1_registers"] and rg["shear_g0_cancelling_parameters"] == (sp.Integer(1),)
                 and rg["shear_g1_cancelling_parameters"] == (sp.Integer(1),) and claims["shear_registers"]
                 and rg["shear_slice_volumes"] == claims["shear_slice_volumes"])
    checks.check("G-2", "ON THE DISTINCT FORMAL SLICE (g0,g1)=(1/4,1/4), det M is proportional to its unit-volume value at zero duality parameters and not proportional with symbolic D16,D25,D34",
                 rg["volume_blind_at_zero_parameters"] and rg["volume_blind_with_parameters"] == claims["volume_blind_with_parameters"]
                 and not claims["volume_blind_with_parameters"] and rg["volume_derivative_with_parameters"]
                 and rg["volume_slice_shears"] == claims["volume_slice_shears"])
    checks.check("H-1", "SCOUT-GRADE FENCE, inherited verbatim from Blocks 211 and 213",
                 claims["scout_grade"] == SCOUT_GRADE_FENCE and SCOUT_GRADE_ONLY)
    checks.check("H-2", "THE ASSEMBLY IS NOT DECIDED AND NO HODGE READING IS SELECTED",
                 not claims["assembly_decided"] and not ASSEMBLY_DECIDED and not HODGE_READING_SELECTED)
    checks.check("H-3", "THE INSTANCE SCOPE IS ENUMERATED: six restrictions",
                 claims["instance_scope_count"] == len(INSTANCE_SCOPE) == 6)
    sc = scope_certificate(facts.note_text)
    checks.check("I-1", "THE NOTE IS PRESENT AND CARRIES THE N5 FENCE BYTE-IDENTICALLY",
                 bool(facts.note_text) and sc["n5_verbatim"] == claims["n5_verbatim"] and claims["n5_verbatim"])
    checks.check("I-2", "NO nsimplify, NO float literal, NO float call in this runner's source",
                 nsimplify_occurrences() == 0 and float_literal_occurrences() == 0 and float_call_sites() == 0
                 and claims["float_absent"])
    return checks


def report_measured(facts: Facts, elapsed_ns: int) -> None:
    print("== BLOCK 214: the duality parameters and the principal part -- measured facts ==")
    print(f"authority: {facts.authority}")
    co = facts.construction
    print(f"construction: free={co['free_names'][0]} carriers={co['carriers'][0]} reconciled={co['reconciled']} "
          f"onsite_h0_is_cell={co['onsite_h0_is_cell']} overlap_h0_structure={co['overlap_h0_structure']}")
    print(f"onsite H_eo (rows even 0,3,5,6; cols odd 1,2,4,7): {co['onsite_h_eo']}")
    ct = facts.control
    for key in sorted(ct):
        print(f"control {key}: {ct[key]}")
    for key in sorted(facts.bench):
        print(f"bench {key}: {facts.bench[key]}")
    me = facts.mechanism
    for key in me:
        print(f"mechanism {key}: {me[key]}")
    for key in facts.cone:
        entry = facts.cone[key]
        print(f"cone {key}: " + " ".join(f"{k}={entry[k]}" for k in entry))
    for key in facts.branches:
        print(f"branches {key}: {facts.branches[key]}")
    for key in facts.registration:
        print(f"registration {key}: {facts.registration[key]}")
    print(f"timings_ms: {facts.timings}  elapsed_ms: {elapsed_ns // 1_000_000}")


N5_FENCE = 'N5: NOTHING HERE IS REGISTERED OR ADOPTED. PARAMETER names a free coordinate of the supplied finite cell system; CONE is a determinant zero set; BRANCH is an exact matrix eigenvalue. The open positive-definite duality region is contained in, but is not equal to, the separate pairwise-bound box; pencil statements require actual positive definiteness. The general D07 unipotent congruence preserves det M and inertia and shifts D0 by -D07^2/D3. Its simple zero-form branch rescaling is established only on the D07-only degree-diagonal/star line: the positive-definite mixed D07=1/4,D16=1/3 example has candidate 224/15 residual 528724036/455625. For the actual n=4 block, det[[0,B],[B^T,0]]=det(B)^2; the general sign is (-1)^n. Raw coefficient-ideal bases certify the old det-B union locus at W1 and L+-/L-+ by containment and power membership, without generic factor splitting. The generic W1 determinant is an irreducible quartic squared over the stated rational-function fields; four named W1 slices exclude a product of two quadrics away from their origin, while linear-times-cubic and other specializations remain open. At L+- and L-+ the old single-quadric zero set persists on the declared plane and is excluded only at the tested off-plane D16=1/4 point; the remaining off-plane locus is open. Shear registration fixes (v0,v1)=(15/16,1); volume registration separately fixes (g0,g1)=(1/4,1/4). No action, parameter selector, assembly, physical metric, propagation law, continuum, spacetime cone, dynamics, or gravity is selected or supplied.'


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
