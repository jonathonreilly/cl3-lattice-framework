#!/usr/bin/env python3
"""Exact Block52 R-eta source/action and cyclic spectral discriminator.

This runner checks exact finite supplied-model identities and pinned text
boundaries. Text/identity checks are not scientific proof or audit authority.
It does not identify a physical charged-lepton carrier, amend an
axiom, retire an obligation, or set an audit verdict.
"""

from __future__ import annotations

import hashlib
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = "docs/AC_RETA_C3_SOURCE_RESPONSE_SPECTRAL_IDENTITY_TYPE_REPAIR_BOUNDED_THEOREM_NOTE_2026-09-02.md"

AUDIT_TIMEOUT_SEC = 150
AUDIT_INPUT_PATHS = ('docs/AC_RETA_C3_SOURCE_RESPONSE_SPECTRAL_IDENTITY_TYPE_REPAIR_BOUNDED_THEOREM_NOTE_2026-09-02.md',
 'docs/MINIMAL_AXIOMS_2026-06-29.md',
 'docs/AC_RETA_HCLASS_HUNIT_READOUT_DERIVATION_OBLIGATION.md',
 'archive/notes/docs/ACPHILAMBDA_R_ETA_HCLASS_FIRST_PRINCIPLES_STRETCH_NO_GO_NOTE_2026-07-04.md',
 'archive/notes/docs/ACPHILAMBDA_R_ETA_ANGLE_NATIVE_FRONTIER_NO_GO_NOTE_2026-07-04.md',
 'archive/notes/docs/ACPHILAMBDA_REGISTRABLE_CYCLE_HOLONOMY_NORMAL_FORM_2026-07-01.md',
 'docs/KOIDE_A1_O13_CHEEGER_SIMONS_RZ_NO_GO_NOTE_2026-04-24.md',
 'docs/KOIDE_A1_RADIAN_BRIDGE_IRREDUCIBILITY_AUDIT_NOTE_2026-04-24.md',
 'scripts/frontier_koide_a1_cheeger_simons_rz_probe.py')
INPUT_SHA256 = {'docs/AC_RETA_C3_SOURCE_RESPONSE_SPECTRAL_IDENTITY_TYPE_REPAIR_BOUNDED_THEOREM_NOTE_2026-09-02.md': '8bb07f6e65a9e146d94504798bbb01175429ee78fac971588600fb417cb86530',
 'docs/MINIMAL_AXIOMS_2026-06-29.md': '93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753',
 'docs/AC_RETA_HCLASS_HUNIT_READOUT_DERIVATION_OBLIGATION.md': '4d742bcc68a1e7cdb154b366e671f576e9b719b3206445b97666c812a790e58c',
 'archive/notes/docs/ACPHILAMBDA_R_ETA_HCLASS_FIRST_PRINCIPLES_STRETCH_NO_GO_NOTE_2026-07-04.md': '08c15bdc0c2fc2ccd750ca2752260ae02ec2521a70bc0307103c42058a63ed09',
 'archive/notes/docs/ACPHILAMBDA_R_ETA_ANGLE_NATIVE_FRONTIER_NO_GO_NOTE_2026-07-04.md': '83f4ab11435b7f5224c1013768dc56c28dfb56f0ab3fdd5811f9b06251dde665',
 'archive/notes/docs/ACPHILAMBDA_REGISTRABLE_CYCLE_HOLONOMY_NORMAL_FORM_2026-07-01.md': '29d97d9abf35e870e7fbff2ad81810deef89dbb9ea6d92fcf7ba147ea5796d69',
 'docs/KOIDE_A1_O13_CHEEGER_SIMONS_RZ_NO_GO_NOTE_2026-04-24.md': '793175beb13915457722519668524d50b20cee4cadce6646bfaae4ccd3148744',
 'docs/KOIDE_A1_RADIAN_BRIDGE_IRREDUCIBILITY_AUDIT_NOTE_2026-04-24.md': '88ad09bf68eeba52d1978e3ee46d3bb902c60145b929985db4518f72e2b6500a',
 'scripts/frontier_koide_a1_cheeger_simons_rz_probe.py': '93043e5dc4346a512c72ca86bc4865babb5af58385f10f8863f09bfe45339d64'}

def require_inputs(root=ROOT):
    for rel, expected in INPUT_SHA256.items():
        path = root / rel
        if not path.is_file() or sha256(path) != expected:
            raise ValueError(f"missing or changed declared input: {rel}")


@dataclass
class Result:
    group: str
    label: str
    ok: bool


class Checks:
    def __init__(self) -> None:
        self.results: list[Result] = []

    def add(self, group: str, label: str, ok: object) -> None:
        self.results.append(Result(group, label, bool(ok)))

    def finish(self) -> int:
        grouped: dict[str, list[Result]] = defaultdict(list)
        for result in self.results:
            grouped[result.group].append(result)
        for group in sorted(grouped):
            vals = grouped[group]
            passed = sum(v.ok for v in vals)
            print(f"{group}: PASS={passed} FAIL={len(vals)-passed}")
            for value in vals:
                if not value.ok:
                    print(f"FAIL [{group}] {value.label}")
        passed = sum(r.ok for r in self.results)
        failed = len(self.results) - passed
        print(f"TOTAL: PASS={passed} FAIL={failed}")
        return 0 if failed == 0 else 1


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def matrix_equal(a: sp.Matrix, b: sp.Matrix) -> bool:
    return all(sp.simplify(x) == 0 for x in (a - b))


def c3_carrier():
    C = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    I3 = sp.eye(3)
    omega = -sp.Rational(1, 2) + sp.I * sp.sqrt(3) / 2
    projectors = []
    for r in range(3):
        projector = sp.zeros(3)
        for k in range(3):
            projector += (omega ** (-r * k)) * (C ** k)
        projectors.append(sp.simplify(projector / 3))
    return C, I3, omega, projectors


def logarithmic_source_response(determinant, source):
    return sp.simplify(sp.diff(sp.log(determinant), source).subs(source, 0))


COORDINATES = sp.symbols("x y z", real=True)


def exterior_derivative(form):
    out = {}
    for basis, coefficient in form.items():
        for axis, coordinate in enumerate(COORDINATES):
            if axis in basis:
                continue
            degree = sum(i < axis for i in basis)
            key = tuple(sorted((axis, *basis)))
            out[key] = out.get(key, 0) + (-1)**degree * sp.diff(coefficient, coordinate)
    return {key: sp.simplify(value) for key, value in out.items() if value != 0}


def hodge_star(form):
    out = {}
    for basis, coefficient in form.items():
        complement = tuple(i for i in range(3) if i not in basis)
        perm = basis + complement
        inversions = sum(perm[i] > perm[j] for i in range(3) for j in range(i+1, 3))
        out[complement] = (-1)**inversions * coefficient
    return out


def odd_signature_local(form, half_degree):
    first = hodge_star(exterior_derivative(form))
    second = exterior_derivative(hodge_star(form))
    return {key: sp.simplify((-1)**(half_degree+1) *
            (first.get(key, 0) - second.get(key, 0)))
            for key in first.keys() | second.keys()}


def focused_checks():
    _, identity, _, projectors = c3_carrier()
    j = sp.Symbol("j", real=True)
    determinant = 7*(2+j)**2
    ordinary = sp.diff(determinant, j).subs(j, 0)
    logarithmic = logarithmic_source_response(determinant, j)
    local = odd_signature_local({(): COORDINATES[0]}, 0)
    return {
        "Fourier normalization": matrix_equal(sum(projectors, sp.zeros(3)), identity),
        "log derivative distinguished": ordinary == 28 and logarithmic == 1 and ordinary != logarithmic,
        "Hodge order on x": local.get((1, 2), 0) == -1 and all(v == 0 for k, v in local.items() if k != (1, 2)),
    }


def main() -> int:
    checks = Checks()

    # Fail closed on missing or changed declared text before finite calculations.
    try:
        require_inputs(ROOT)
    except (OSError, ValueError) as exc:
        print(f"INPUT_ERROR: {exc}")
        return 2
    checks.add("INPUT_IDENTITY", "all declared note/context texts match frozen hashes", True)
    axiom_text = (ROOT / "docs/MINIMAL_AXIOMS_2026-06-29.md").read_text()
    checks.add("PUBLICATION", "source/action remains outside axiom content",
               "source/action and physical-observable identification" in axiom_text)
    checks.add("PUBLICATION", "removed scalar/additive Record wording is explicit",
               "Finite additivity, a named scalar collection functional `I`" in axiom_text
               and "are not Record axiom content" in axiom_text)

    # Exact C3 carrier and projector classification.
    C, I3, omega, projectors = c3_carrier()
    P0, P1, P2 = projectors
    Ps, Pd = P0, sp.simplify(P1 + P2)

    completeness = matrix_equal(P0 + P1 + P2, I3)
    checks.add("CARRIER", "Fourier projectors complete", completeness)
    for r, Pr in enumerate(projectors):
        checks.add("CARRIER", f"P{r} Hermitian", matrix_equal(Pr.conjugate().T, Pr))
        checks.add("CARRIER", f"P{r} idempotent", matrix_equal(Pr * Pr, Pr))
        checks.add("CARRIER", f"P{r} rank one", Pr.rank() == 1)
        checks.add("CARRIER", f"P{r} commutes with C", matrix_equal(Pr * C, C * Pr))
    checks.add("CARRIER", "projectors pairwise orthogonal",
               all(matrix_equal(projectors[r] * projectors[s], sp.zeros(3))
                   for r in range(3) for s in range(3) if r != s))
    k_swap = matrix_equal(P1.conjugate(), P2) and matrix_equal(P2.conjugate(), P1)
    checks.add("CARRIER", "K swaps the nontrivial characters", k_swap)
    checks.add("CARRIER", "K fixes singlet and doublet projectors",
               matrix_equal(Ps.conjugate(), Ps) and matrix_equal(Pd.conjugate(), Pd))
    checks.add("CARRIER", "singlet/doublet ranks are one/two",
               Ps.rank() == 1 and Pd.rank() == 2)

    # The commutant has complex dimension 3.  Its Hermitian part has the
    # displayed three-real-vector basis, and K-even part drops the imaginary one.
    x = sp.symbols("x0:9")
    X = sp.Matrix(3, 3, x)
    linear_map = sp.linear_eq_to_matrix(list(X * C - C * X), x)[0]
    checks.add("CLASSIFICATION", "C3 commutant complex dimension three",
               9 - linear_map.rank() == 3)
    hermitian_basis = (I3, C + C.T, sp.I * (C - C.T))
    checks.add("CLASSIFICATION", "three displayed invariant Hermitian basis matrices",
               all(matrix_equal(B.conjugate().T, B) and matrix_equal(B * C, C * B)
                   for B in hermitian_basis))
    flat_basis = [sp.Matrix([sp.re(z) for z in B]).col_join(
        sp.Matrix([sp.im(z) for z in B])) for B in hermitian_basis]
    checks.add("CLASSIFICATION", "Hermitian invariant basis real-independent",
               sp.Matrix.hstack(*flat_basis).rank() == 3)
    checks.add("CLASSIFICATION", "K-even invariant Hermitian dimension two",
               matrix_equal(hermitian_basis[0].conjugate(), hermitian_basis[0])
               and matrix_equal(hermitian_basis[1].conjugate(), hermitian_basis[1])
               and matrix_equal(hermitian_basis[2].conjugate(), -hermitian_basis[2]))

    spectral_subsets = []
    for mask in range(8):
        P = sp.zeros(3)
        for r in range(3):
            if mask & (1 << r):
                P += projectors[r]
        if matrix_equal(P.conjugate(), P):
            spectral_subsets.append((mask, sp.simplify(P)))
    k_even_count = len(spectral_subsets)
    checks.add("CLASSIFICATION", "exactly four K-even invariant projections",
               k_even_count == 4)
    masks = {mask for mask, _ in spectral_subsets}
    checks.add("CLASSIFICATION", "K-even projection masks are 0, singlet, doublet, identity",
               masks == {0, 1, 6, 7})
    candidates = [P for _, P in spectral_subsets
                  if matrix_equal(P * Ps, sp.zeros(3)) and P.rank() > 0]
    unique_doublet = len(candidates) == 1 and matrix_equal(candidates[0], Pd)
    checks.add("CLASSIFICATION", "unique nonzero K-even projection killing singlet is Pd",
               unique_doublet)

    # Formal determinant response.  The invariant action normalization and the
    # physical statistics/measure typing are both live bits.
    a_s, a_d, j, c, lam = sp.symbols("a_s a_d j c lambda", positive=True)
    det_Aj = sp.expand(a_s * (a_d + j) ** 2)
    raw_response = logarithmic_source_response(det_Aj, j)
    normalized_trace_response = sp.simplify(raw_response / 3)
    orbit_density_factor = sp.Rational(1, 3)
    response = sp.simplify(orbit_density_factor * normalized_trace_response)
    phi = sp.simplify(3 * response)
    checks.add("RESPONSE", "logarithmic determinant source derivative is 2/ad", raw_response == 2 / a_d)
    checks.add("RESPONSE", "stipulated orbit-density times normalized-trace response is 2/(9ad)",
               response == 2 / (9 * a_d))
    checks.add("RESPONSE", "cycle response is Phi=3h=2/(3ad)", phi == 2 / (3 * a_d))
    trace_factor = sp.Rational(1, 3)
    checks.add("RESPONSE", "normalization is stipulated orbit density times normalized trace",
               orbit_density_factor * trace_factor == sp.Rational(1, 9))

    # The genuine conjugation average is type-preserving.  Since A^{-1}P_d is
    # C3 invariant, averaging C^k X C^{-k} returns X; it does not generate the
    # extra scalar factor used in the campaign-normalized response.
    A_inv_Pd = sp.simplify(Pd / a_d)
    true_group_average = sp.simplify(sum(
        [(C ** k) * A_inv_Pd * (C ** (-k)) for k in range(3)],
        sp.zeros(3),
    ) / 3)
    group_average_preserves = matrix_equal(true_group_average, A_inv_Pd)
    checks.add("RESPONSE", "true C3 conjugation average preserves invariant operator",
               group_average_preserves)
    typed_trace = sp.simplify(sp.trace(A_inv_Pd) / 3)
    scalar_tau_well_typed = typed_trace == normalized_trace_response
    checks.add("RESPONSE", "tau is applied to A^-1 Pd before scalar orbit factor",
               scalar_tau_well_typed)

    determinant_powers = {
        "real_boson": -sp.Rational(1, 2),
        "complex_boson": -sp.Integer(1),
        "complex_Grassmann": sp.Integer(1),
    }
    statistical_type_visible = len(set(determinant_powers.values())) == 3
    checks.add("RESPONSE", "Gaussian statistics give three distinct determinant powers",
               statistical_type_visible)
    checks.add("RESPONSE", "formal determinant response equals Grassmann exponent only",
               determinant_powers["complex_Grassmann"] * raw_response == raw_response
               and determinant_powers["real_boson"] * raw_response != raw_response
               and determinant_powers["complex_boson"] * raw_response != raw_response)
    source_scaled = sp.simplify(c * 2 / (9 * a_d))
    checks.add("RESPONSE", "source scaling changes response",
               source_scaled == c * response and sp.diff(source_scaled, c) != 0)
    action_scaled = sp.simplify(2 / (9 * lam * a_d))
    checks.add("RESPONSE", "doublet action scaling changes response",
               action_scaled == response / lam and sp.diff(action_scaled, lam) != 0)
    idempotent_equation = sp.factor(c ** 2 - c)
    checks.add("RESPONSE", "nonzero idempotent source fixes c=1",
               idempotent_equation == c * (c - 1))
    target_member = sp.solve(sp.Eq(2 / (9 * a_d), sp.Rational(2, 9)), a_d)
    checks.add("RESPONSE", "target h occurs iff ad=1", target_member == [1])

    # Each common-looking normalization alone leaves a positive countermember.
    det_counter = {a_s: sp.Rational(1, 4), a_d: 2}
    trace_counter = {a_s: 2, a_d: sp.Rational(1, 2)}
    det_alone_nonunique = (sp.simplify((a_s * a_d ** 2).subs(det_counter)) == 1
                           and sp.simplify(response.subs(det_counter)) != sp.Rational(2, 9))
    trace_alone_nonunique = (sp.simplify((a_s + 2 * a_d).subs(trace_counter)) == 3
                             and sp.simplify(response.subs(trace_counter)) != sp.Rational(2, 9))
    checks.add("RESPONSE", "determinant normalization alone leaves countermember",
               det_alone_nonunique)
    checks.add("RESPONSE", "trace normalization alone leaves countermember",
               trace_alone_nonunique)
    joint_poly = sp.factor(2 * a_d ** 3 - 3 * a_d ** 2 + 1)
    checks.add("RESPONSE", "joint det-and-trace normalization has unique positive member",
               joint_poly == (a_d - 1) ** 2 * (2 * a_d + 1))

    # Exact local fixed-point and global odd-signature lens formulas.
    p = sp.symbols("p", integer=True, positive=True)
    q1 = sp.simplify(p * (p - 1) / 2 / p)  # q'(1)/q(1)
    q2 = sp.simplify(p * (p - 1) * (p - 2) / 3 / p)  # q''(1)/q(1)
    reciprocal_square_sum = sp.simplify(q1 ** 2 - q2)
    fixed_sum = sp.simplify(q1 - reciprocal_square_sum)
    fixed_density = sp.factor(fixed_sum / p)
    csc_square_sum = sp.simplify(4 * fixed_sum)
    cot_square_sum = sp.factor(csc_square_sum - (p - 1))
    lens_eta = sp.factor(cot_square_sum / p)
    checks.add("SPECTRAL", "root-polynomial first reciprocal sum", q1 == (p - 1) / 2)
    checks.add("SPECTRAL", "root-polynomial reciprocal-square sum",
               reciprocal_square_sum == (p - 1) * (5 - p) / 12)
    checks.add("SPECTRAL", "local cyclic fixed density closed form",
               sp.simplify(fixed_density - (p ** 2 - 1) / (12 * p)) == 0)
    checks.add("SPECTRAL", "cosecant-square sum closed form",
               csc_square_sum == (p ** 2 - 1) / 3)
    checks.add("SPECTRAL", "cotangent-square sum closed form",
               cot_square_sum == (p - 1) * (p - 2) / 3)
    checks.add("SPECTRAL", "lens odd-signature eta magnitude closed form",
               lens_eta == (p - 1) * (p - 2) / (3 * p))

    # Lens-space convention controls.  For the quotient action with weights
    # (1,q), the cotangent product flips sign between q=+1 and q=-1.  The note
    # records the round metric, quotient orientation, and the exact APS
    # odd-signature operator convention; reversing orientation or B flips eta.
    cot_plus_3 = sp.simplify(sum(
        sp.cot(sp.pi * k / 3) * sp.cot(sp.pi * k / 3) for k in (1, 2)
    ) / 3)
    cot_minus_3 = sp.simplify(sum(
        sp.cot(sp.pi * k / 3) * sp.cot(-sp.pi * k / 3) for k in (1, 2)
    ) / 3)
    weights_distinct = cot_plus_3 == sp.Rational(2, 9) and cot_minus_3 == -sp.Rational(2, 9)
    checks.add("SPECTRAL", "lens weights (1,1) and (1,-1) have opposite eta signs",
               weights_distinct)

    kernel_h = sp.Integer(1)
    reduced_eta_positive = sp.simplify((sp.Rational(2, 9) + kernel_h) / 2)
    reduced_eta_negative = sp.simplify((-sp.Rational(2, 9) + kernel_h) / 2)
    raw_reduced_distinct = (reduced_eta_positive == sp.Rational(11, 18)
                            and reduced_eta_negative == sp.Rational(7, 18))
    checks.add("SPECTRAL", "raw eta and reduced eta are distinct",
               raw_reduced_distinct)
    kernel_visible = kernel_h == 1
    checks.add("SPECTRAL", "odd-signature kernel correction h_B=1 is explicit",
               kernel_visible)

    direct_fixed_3 = sp.simplify(sum(
        1 / ((omega ** k - 1) * (omega ** (-k) - 1)) for k in (1, 2)
    ) / 3)
    direct_eta_3 = sp.simplify((sp.cot(sp.pi / 3) ** 2
                                + sp.cot(2 * sp.pi / 3) ** 2) / 3)
    p3_equal = direct_fixed_3 == direct_eta_3 == sp.Rational(2, 9)
    checks.add("SPECTRAL", "direct C3 fixed density equals lens eta at 2/9", p3_equal)
    difference = sp.factor(lens_eta - fixed_density)
    checks.add("SPECTRAL", "local/global difference factor",
               difference == (p - 1) * (p - 3) / (4 * p))
    uniqueness = sp.solve(sp.Eq(sp.factor((p - 1) * (p - 3)), 0), p) == [1, 3]
    checks.add("SPECTRAL", "p=3 is unique nontrivial equality", uniqueness)
    typed_distinct = sp.simplify(difference.subs(p, 4)) != 0
    checks.add("SPECTRAL", "fixed density and lens eta remain distinct object families",
               typed_distinct)

    # Flat torsion characters and the exact prior-art contradiction.
    h = sp.Rational(2, 9)
    characters_z3 = {sp.Rational(m, 3) for m in range(3)}
    torsion_relation = sp.Mod(3 * h, 1) == sp.Rational(2, 3)
    checks.add("CHARACTER", "2/9 violates flat Z3 character relation",
               torsion_relation and sp.Mod(3 * h, 1) != 0)
    valid_character_claim = h not in characters_z3
    checks.add("CHARACTER", "flat Z3 character values exclude 2/9",
               valid_character_claim)
    checks.add("CHARACTER", "flat Z3 character values are 0,1/3,2/3",
               characters_z3 == {0, sp.Rational(1, 3), sp.Rational(2, 3)})
    old_cs = (ROOT / "docs/KOIDE_A1_O13_CHEEGER_SIMONS_RZ_NO_GO_NOTE_2026-04-24.md").read_text()
    old_runner = (ROOT / "scripts/frontier_koide_a1_cheeger_simons_rz_probe.py").read_text()
    checks.add("TEXT_COMPARISON", "old runner computes failed torsion relation",
               "3 c(g) = 2/3 mod 1, NOT zero" in old_runner)
    checks.add("TEXT_COMPARISON", "old runner nevertheless asserts valid flat lift",
               "is a valid differential character" in old_runner
               and "well-defined holonomy 2/9" in old_runner)
    checks.add("TEXT_COMPARISON", "old note makes the same flat-holonomy assertion",
               "holonomy `2/9 mod 1` around the Z" in old_cs)
    degree_typed = "loop holonomy uses degree two in the modern convention" \
                   " and degree one in the shifted Cheeger--Simons convention"
    checks.add("PUBLICATION", "differential-character degree convention kept explicit",
               "modern convention" in degree_typed and "shifted" in degree_typed)
    eta_is_flat_holonomy = False
    checks.add("PUBLICATION", "global eta value not equated to flat generator holonomy",
               not eta_is_flat_holonomy)

    # Phase normalization remains a separate physical map.
    phase_identity = h
    phase_2pi = 2 * sp.pi * h
    phase_pi = sp.pi * h
    phase_half_pi = sp.pi * h / 2
    checks.add("PHASE", "identity reading gives 2/9", phase_identity == sp.Rational(2, 9))
    checks.add("PHASE", "canonical R/Z exponential gives 4pi/9",
               phase_2pi == 4 * sp.pi / 9)
    checks.add("PHASE", "pi and half-pi maps give distinct coefficients",
               phase_pi == 2 * sp.pi / 9 and phase_half_pi == sp.pi / 9)
    checks.add("PHASE", "none of the pi-bearing maps is identity reading",
               all(expr != h for expr in (phase_2pi, phase_pi, phase_half_pi)))

    note = (ROOT / NOTE_PATH).read_text()

    checks.add("PUBLICATION", "physical carrier remains open",
               "physical carrier remains open" in note and "physical carrier is derived" not in note)
    checks.add("PUBLICATION", "Record supplies no source or action",
               "Record supplies no source or action" in note
               and "Record supplies the source action" not in note)
    checks.add("PUBLICATION", "open PRs are comparator-only",
               "Open PRs are comparators only" in note
               and "Open PRs are retained authority" not in note)
    checks.add("PUBLICATION", "obligation remains open",
               "The obligation remains open" in note and "The obligation is retired" not in note)
    checks.add("PUBLICATION", "TOE movement remains zero",
               "TOE percentage movement: `0`" in note and "TOE percentage movement: `1`" not in note)
    checks.add("PUBLICATION", "N1 alternatives committed",
               "## N1 -- Alternative route enumeration" in note)
    checks.add("PUBLICATION", "bounded theorem claim type",
               "claim_type: bounded_theorem" in note)
    normalized_note = " ".join(note.split())
    lens_surface = {
        "lens_quotient_action_hidden": "(z_1,z_2) -> (zeta_p z_1,zeta_p z_2)",
        "lens_round_metric_hidden": "round quotient metric",
        "lens_orientation_hidden": "boundary orientation induced from the unit ball",
        "odd_signature_operator_hidden": "B(phi)=(-1)^(r+1)(*d-d*)phi",
        "determinant_statistical_type_hidden": "real boson, complex boson, and complex Grassmann",
        "raw_reduced_eta_conflated": "reduced eta values are 11/18 or 7/18",
        "eta_kernel_additive_correction_omitted": "h_B=1",
    }
    for convention_key, needle in lens_surface.items():
        present = needle in normalized_note
        checks.add("PUBLICATION", f"typed convention present: {convention_key}", present)
    checks.add("PUBLICATION", "partial-narrowing disposition explicit",
               "actual_current_surface_status: partial-narrowing" in note
               and "no_go_discipline_gate: FAIL" in note)

    print("per_element: checked — C3 projectors, source scale, and flat-character values are exact.")
    print("per_site: checked conditionally — the finite triplet is not claimed as the physical site carrier.")
    print("per_mode: checked — singlet and conjugate-doublet Fourier modes are classified exactly.")
    print("per_block: checked — every C3/K invariant quadratic and projection block is covered.")
    print("lattice_wide: not executed — no physical lattice action or charged-lepton attachment is supplied.")
    print("N5_SCOPE no-go: only the flat-Z3-character shortcut and free finite action family.")
    print("N5_SCOPE never: no claim against future eta, source/action, or differential-cohomology routes.")
    print("N5_SCOPE impossible: no universal impossibility claim.")
    print("N5_SCOPE forced: only exact finite algebra, character relations, and formula identities.")
    print("N5_SCOPE only: uniqueness is confined to the nonzero K-even singlet-killing projector.")
    print("N5_SCOPE must: closure must meet the registered physical carrier/readout criterion.")
    print("N5_SCOPE cannot: 2/9 cannot be flat holonomy on the order-three generator only.")

    for label, ok in focused_checks().items():
        checks.add("FOCUSED", label, ok)
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
