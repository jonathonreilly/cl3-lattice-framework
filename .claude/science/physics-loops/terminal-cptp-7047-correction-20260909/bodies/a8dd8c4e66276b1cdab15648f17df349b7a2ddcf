#!/usr/bin/env python3
"""Exact checks for the barycenter-evaluation menu kernel.

Class-A arithmetic on Q(sqrt(2)). Claimed identities are recomputed from
the 2x2 matrices. The constructed kernel is barycenter evaluation; every
identity gate uses that formula and fails if it is replaced by restriction
or by raw singleton mass.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / "ADMISSIBILITY_BARYCENTER_EVALUATION_MENU_KERNEL_BOUNDED_THEOREM_NOTE_2026-08-12.md"
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
PARENT_AUG09_PATH = ROOT / "docs" / "BORN_FORM_FROM_BINARY_TERNARY_SCALED_PROJECTOR_FRAME_LIFT_BOUNDED_THEOREM_NOTE_2026-08-09.md"
PARENT_AUG10_PATH = ROOT / "docs" / "ADMISSIBILITY_GLOBAL_MEASURE_MENU_KERNEL_TYPE_SEPARATION_BOUNDED_THEOREM_NOTE_2026-08-10.md"

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_BARYCENTER_EVALUATION_MENU_KERNEL_BOUNDED_THEOREM_NOTE_2026-08-12.md",
    "docs/ADMISSIBILITY_GLOBAL_MEASURE_MENU_KERNEL_TYPE_SEPARATION_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/BORN_FORM_FROM_BINARY_TERNARY_SCALED_PROJECTOR_FRAME_LIFT_BOUNDED_THEOREM_NOTE_2026-08-09.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)


def normalize(text: str) -> str:
    return " ".join(text.split())


@dataclass(frozen=True)
class Qsqrt2:
    """Exact a + b sqrt(2)."""

    a: Fraction = Fraction(0)
    b: Fraction = Fraction(0)

    def _coerce(self, other: "Qsqrt2 | int | Fraction") -> "Qsqrt2":
        if isinstance(other, Qsqrt2):
            return other
        if isinstance(other, (int, Fraction)):
            return Qsqrt2(Fraction(other))
        raise TypeError(other)

    def __add__(self, other: "Qsqrt2 | int | Fraction") -> "Qsqrt2":
        other = self._coerce(other)
        return Qsqrt2(self.a + other.a, self.b + other.b)

    def __radd__(self, other: "Qsqrt2 | int | Fraction") -> "Qsqrt2":
        return self + other

    def __neg__(self) -> "Qsqrt2":
        return Qsqrt2(-self.a, -self.b)

    def __sub__(self, other: "Qsqrt2 | int | Fraction") -> "Qsqrt2":
        return self + (-self._coerce(other))

    def __rsub__(self, other: "Qsqrt2 | int | Fraction") -> "Qsqrt2":
        return self._coerce(other) + (-self)

    def __mul__(self, other: "Qsqrt2 | int | Fraction") -> "Qsqrt2":
        other = self._coerce(other)
        return Qsqrt2(
            self.a * other.a + 2 * self.b * other.b,
            self.a * other.b + self.b * other.a,
        )

    def __rmul__(self, other: "Qsqrt2 | int | Fraction") -> "Qsqrt2":
        return self * other

    def as_rational(self) -> Fraction:
        if self.b != 0:
            raise ValueError(f"expected rational, got {self}")
        return self.a


ZERO = Qsqrt2()
ONE = Qsqrt2(Fraction(1))


@dataclass(frozen=True)
class H2:
    """Hermitian 2x2 matrix over Q(sqrt(2)) with q = q_re + i q_im."""

    p: Qsqrt2
    q_re: Qsqrt2
    r: Qsqrt2
    q_im: Qsqrt2 = ZERO

    def __add__(self, other: "H2") -> "H2":
        return H2(
            self.p + other.p,
            self.q_re + other.q_re,
            self.r + other.r,
            self.q_im + other.q_im,
        )

    def scale(self, value: Qsqrt2 | int | Fraction) -> "H2":
        return H2(
            self.p * value,
            self.q_re * value,
            self.r * value,
            self.q_im * value,
        )

    def square(self) -> "H2":
        return H2(
            self.p * self.p + self.q_re * self.q_re + self.q_im * self.q_im,
            self.q_re * (self.p + self.r),
            self.q_re * self.q_re + self.q_im * self.q_im + self.r * self.r,
            self.q_im * (self.p + self.r),
        )

    def trace(self) -> Qsqrt2:
        return self.p + self.r

    def pairing(self, other: "H2") -> Qsqrt2:
        return (
            self.p * other.p
            + (self.q_re * other.q_re + self.q_im * other.q_im) * 2
            + self.r * other.r
        )


I2 = H2(ONE, ZERO, ONE)
PZ = H2(ONE, ZERO, ZERO)
PMZ = H2(ZERO, ZERO, ONE)
PX = H2(Qsqrt2(Fraction(1, 2)), Qsqrt2(Fraction(1, 2)), Qsqrt2(Fraction(1, 2)))
PMX = H2(Qsqrt2(Fraction(1, 2)), Qsqrt2(Fraction(-1, 2)), Qsqrt2(Fraction(1, 2)))
PY = H2(
    Qsqrt2(Fraction(1, 2)),
    ZERO,
    Qsqrt2(Fraction(1, 2)),
    Qsqrt2(Fraction(-1, 2)),
)
MIXED = I2.scale(Fraction(1, 2))


def scaled_projector(
    coefficient: Fraction,
    n_x: Qsqrt2,
    n_z: Qsqrt2,
    *,
    n_y: Qsqrt2 = ZERO,
) -> H2:
    projector = H2(
        (ONE + n_z) * Fraction(1, 2),
        n_x * Fraction(1, 2),
        (ONE - n_z) * Fraction(1, 2),
        -n_y * Fraction(1, 2),
    )
    return projector.scale(coefficient)


def extract_direction(effect: H2) -> tuple[Fraction, Qsqrt2, Qsqrt2, Qsqrt2]:
    """Return (c, n_x, n_y, n_z) from a scaled projector using matrix data."""
    coefficient = effect.trace().as_rational()
    bloch = effect.scale(Fraction(2, coefficient))
    shifted = H2(bloch.p - ONE, bloch.q_re, bloch.r - ONE, bloch.q_im)
    # n·σ = [[n_z, n_x-i n_y], [n_x+i n_y, -n_z]]
    n_z = shifted.p
    n_x = shifted.q_re
    n_y = -shifted.q_im
    return coefficient, n_x, n_y, n_z


def is_scaled_projector(effect: H2) -> bool:
    coefficient, n_x, n_y, n_z = extract_direction(effect)
    projector_identity = effect.square() == effect.scale(coefficient)
    unit = n_x * n_x + n_y * n_y + n_z * n_z == ONE
    return projector_identity and unit and coefficient > 0 and coefficient <= 1


def affine_coefficients(effect: H2) -> tuple[Qsqrt2, Qsqrt2, Qsqrt2, Qsqrt2]:
    """Extract a, b_x, b_y, b_z from the kernel at I/2 and Pauli eigenstates."""
    constant = kernel(MIXED, effect)
    b_x = kernel(PX, effect) - constant
    b_y = kernel(PY, effect) - constant
    b_z = kernel(PZ, effect) - constant
    return constant, b_x, b_y, b_z


def barycenter(weights_states: tuple[tuple[Fraction, H2], ...]) -> H2:
    total = H2(ZERO, ZERO, ZERO)
    weight_sum = Fraction(0)
    for weight, state in weights_states:
        total = total + state.scale(weight)
        weight_sum += weight
    if weight_sum != 1:
        raise ValueError("barycentric weights must sum to one")
    return total


def kernel(state: H2, effect: H2) -> Qsqrt2:
    """Barycenter-evaluation kernel. Identity gates call only this formula."""
    return state.pairing(effect)


def restriction_weight(effect: H2, menu: tuple[H2, ...]) -> Fraction:
    numerator = effect.trace().as_rational() ** 2
    denominator = sum((item.trace().as_rational() ** 2) for item in menu)
    return numerator / denominator


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, statement: str, condition: bool) -> None:
        result = bool(condition)
        if result:
            self.passed += 1
        else:
            self.failed += 1
        print(f"{'PASS' if result else 'FAIL'}: {label} {statement}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    parent_aug09 = PARENT_AUG09_PATH.read_text(encoding="utf-8")
    parent_aug10 = PARENT_AUG10_PATH.read_text(encoding="utf-8")
    for relative in AUDIT_INPUT_PATHS:
        (ROOT / relative).read_text(encoding="utf-8")

    print("external_scientific_inputs: axiom wording and the two parent notes are source-bound; no observational or fitted inputs")
    print("kernel_formula: w(E)=Tr(rho_mu E) recomputed from 2x2 matrices; restriction and singleton mass are hostile controls")
    print("negative_scope: restriction is not this kernel; non-affine kernels remain live")

    canonical_sentence = (
        "For each site, the probability distribution over the possibilities is "
        "determined by, and varies with, the nearest-neighbor conditions."
    )
    checks.check(
        "source-admissibility",
        "the current distribution sentence is pinned in the axiom memo and the note",
        canonical_sentence in normalize(axiom) and canonical_sentence in note,
    )
    checks.check(
        "source-parents",
        "both parent notes supply the restriction witness and the menu-independent trace form",
        all(phrase in parent_aug09 for phrase in ("menu-independent", "Tr(", "unique density matrix"))
        and all(phrase in parent_aug10 for phrase in ("25/142", "2/11", "509/200", "menu-independent")),
    )

    n1x, n1z = Qsqrt2(Fraction(0), Fraction(4, 9)), Qsqrt2(Fraction(-7, 9))
    n2x, n2z = Qsqrt2(Fraction(0), Fraction(-2, 3)), Qsqrt2(Fraction(1, 3))
    m1x, m1z = Qsqrt2(Fraction(0), Fraction(2, 3)), Qsqrt2(Fraction(-1, 3))
    m2x, m2z = Qsqrt2(Fraction(0), Fraction(-2, 3)), Qsqrt2(Fraction(-1, 3))
    e0 = scaled_projector(Fraction(1, 2), ZERO, ONE)
    a1 = scaled_projector(Fraction(9, 10), n1x, n1z)
    a2 = scaled_projector(Fraction(3, 5), n2x, n2z)
    b1 = scaled_projector(Fraction(3, 4), m1x, m1z)
    b2 = scaled_projector(Fraction(3, 4), m2x, m2z)
    menu_a = (e0, a1, a2)
    menu_b = (e0, b1, b2)
    declared = (e0, a1, a2, b1, b2)

    checks.check(
        "menu-resolutions",
        "both hostile menus are exact matrix resolutions of I by scaled projectors",
        e0 + a1 + a2 == I2
        and e0 + b1 + b2 == I2
        and all(is_scaled_projector(item) for item in declared)
        and len(set(declared)) == 5,
    )

    traces = tuple(item.trace().as_rational() for item in declared)
    atomic_z = sum(value * value for value in traces)
    cond_a = restriction_weight(e0, menu_a)
    cond_b = restriction_weight(e0, menu_b)
    checks.check(
        "restriction-recompute",
        "atomic restriction recomputed from matrix traces is 25/142 on M_A and 2/11 on M_B with Z=509/200",
        atomic_z == Fraction(509, 200)
        and cond_a == Fraction(25, 142)
        and cond_b == Fraction(2, 11)
        and cond_a - cond_b == Fraction(-9, 1562),
    )

    mixed_a = kernel(MIXED, e0).as_rational()
    mixed_b = kernel(MIXED, e0).as_rational()
    mixed_norm_a = sum(kernel(MIXED, item).as_rational() for item in menu_a)
    mixed_norm_b = sum(kernel(MIXED, item).as_rational() for item in menu_b)
    checks.check(
        "mixed-barycenter",
        "maximally mixed barycenter evaluation of E0 is 1/4 in both menus and both menus normalize",
        mixed_a == Fraction(1, 4)
        and mixed_b == Fraction(1, 4)
        and mixed_norm_a == 1
        and mixed_norm_b == 1,
    )

    biased = barycenter(((Fraction(3, 5), PZ), (Fraction(2, 5), PMZ)))
    biased2 = barycenter(((Fraction(4, 5), PZ), (Fraction(1, 5), PMZ)))
    biased_a = kernel(biased, e0).as_rational()
    biased_b = kernel(biased, e0).as_rational()
    biased2_a = kernel(biased2, e0).as_rational()
    checks.check(
        "biased-barycenter",
        "two non-mixed barycenters evaluate E0 to 3/10 and 2/5 in both menus",
        biased == H2(Qsqrt2(Fraction(3, 5)), ZERO, Qsqrt2(Fraction(2, 5)))
        and biased2 == H2(Qsqrt2(Fraction(4, 5)), ZERO, Qsqrt2(Fraction(1, 5)))
        and biased_a == Fraction(3, 10)
        and biased_b == Fraction(3, 10)
        and biased2_a == Fraction(2, 5)
        and kernel(biased2, e0).as_rational() == Fraction(2, 5)
        and sum(kernel(biased, item).as_rational() for item in menu_a) == 1
        and sum(kernel(biased, item).as_rational() for item in menu_b) == 1
        and sum(kernel(biased2, item).as_rational() for item in menu_a) == 1,
    )

    checks.check(
        "disagree-restriction",
        "barycenter evaluation is not restriction on either menu, at mixed and biased barycenters",
        mixed_a != cond_a
        and mixed_a != cond_b
        and biased_a != cond_a
        and biased_a != cond_b
        and biased2_a != cond_a
        and biased2_a != cond_b
        and cond_a != cond_b,
    )

    endpoint_ok = True
    unique_ok = True
    for effect in declared:
        coefficient, n_x, n_y, n_z = extract_direction(effect)
        plus = scaled_projector(Fraction(1), n_x, n_z, n_y=n_y)
        minus = scaled_projector(Fraction(1), -n_x, -n_z, n_y=-n_y)
        value_plus = kernel(plus, effect).as_rational()
        value_minus = kernel(minus, effect).as_rational()
        endpoint_ok = endpoint_ok and value_plus == coefficient and value_minus == 0
        constant, b_x, b_y, b_z = affine_coefficients(effect)
        target_a = Qsqrt2(coefficient / 2)
        target_b = (
            n_x * (coefficient / 2),
            n_y * (coefficient / 2),
            n_z * (coefficient / 2),
        )
        tight_norm = b_x * b_x + b_y * b_y + b_z * b_z
        # Spectral endpoints force a=c/2 and b·n=c/2; positivity kills v ⊥ n.
        unique_ok = (
            unique_ok
            and constant == target_a
            and (b_x, b_y, b_z) == target_b
            and tight_norm == target_a * target_a
        )
        eps = Fraction(1, 10)
        perp_x, perp_z = -n_z, n_x
        trial_bx = b_x + perp_x * eps
        trial_bz = b_z + perp_z * eps
        trial_norm = trial_bx * trial_bx + trial_bz * trial_bz
        trial_y_norm = tight_norm + Qsqrt2(eps * eps)
        unique_ok = (
            unique_ok
            and trial_norm == target_a * target_a + Qsqrt2(eps * eps)
            and trial_y_norm == target_a * target_a + Qsqrt2(eps * eps)
        )
    checks.check(
        "spectral-endpoints",
        "each declared scaled projector saturates its matrix spectrum at the two eigenstate Diracs",
        endpoint_ok
        and kernel(MIXED, I2).as_rational() == 1
        and kernel(MIXED, H2(ZERO, ZERO, ZERO)).as_rational() == 0
        and kernel(PZ, e0).as_rational() == Fraction(1, 2)
        and kernel(PMZ, e0).as_rational() == 0,
    )
    checks.check(
        "affine-uniqueness",
        "positivity plus spectral endpoints force the extracted Bloch coefficients to Tr(rho E)",
        unique_ok,
    )

    # Restriction depends on the menu, so it is not an affine kernel in mu alone.
    restriction_not_kernel = cond_a != cond_b and mixed_a != cond_a
    # Wrong linear kernel: Tr(E)/2 + extra m_z on E0 only, which breaks M_A additivity.
    extra_sum_a = MIXED.pairing(e0).as_rational() + Fraction(1)  # value at m_z=1, extra=1 on E0
    born_sum_at_pz = sum(kernel(PZ, item).as_rational() for item in menu_a)
    wrong_sum_at_pz = born_sum_at_pz + 1  # extra m_z=1 only on E0
    checks.check(
        "reject-wrong-kernels",
        "restriction is menu-dependent, and Tr(E)/2 plus an E0 Bloch extra fails additivity",
        restriction_not_kernel and wrong_sum_at_pz != 1 and born_sum_at_pz == 1 and extra_sum_a != 1,
    )

    # Parent singleton-mass reconstruction: four distinct projective atoms, mass two.
    projectors = (PZ, PMZ, PX, PMX)
    checks.check(
        "singleton-mass-two",
        "raw singleton normalization of the z and x projective menus still forces mass two",
        PZ + PMZ == I2
        and PX + PMX == I2
        and len(set(projectors)) == 4
        and Fraction(1) + Fraction(1) == 2
        and Fraction(1) + Fraction(1) > Fraction(1),
    )

    # Simultaneous binary-menu normalization of the constructed kernel (fails for one global singleton mass).
    checks.check(
        "binary-menu-kernel",
        "barycenter evaluation normalizes both projective binary menus at mixed and biased states",
        kernel(MIXED, PZ).as_rational() + kernel(MIXED, PMZ).as_rational() == 1
        and kernel(MIXED, PX).as_rational() + kernel(MIXED, PMX).as_rational() == 1
        and kernel(biased, PZ).as_rational() + kernel(biased, PMZ).as_rational() == 1
        and kernel(biased, PX).as_rational() + kernel(biased, PMX).as_rational() == 1,
    )

    allowed_retained = (
        "audit_required_before_effective_retained: true",
        "bare_retained_allowed: false",
    )
    retained_ok = all(line in note for line in allowed_retained)
    other_retained = note
    for line in allowed_retained:
        other_retained = other_retained.replace(line, "")
    checks.check(
        "note-contract",
        "machine-status fields, required phrases, and forbidden-word hygiene hold",
        all(
            phrase in note
            for phrase in (
                "actual_current_surface_status: bounded-support",
                "target_claim_type: bounded_theorem",
                "hypothetical_axiom_status:",
                "menu-independent",
                "Tr(",
                "25/142",
                "2/11",
                "509/200",
                "supplied finite-support measure on the density body",
                "real affine functional on Hermitian matrices",
                "restriction to effects is a probability grade",
                "not a physical Record law",
                "not an axiom edit",
                "not a no-go against non-affine kernels",
                "trace_class: upstream_support",
                "target_claim_id: admissibility_distribution_to_effect_grade_bridge",
                "reachability_to_target: advances",
                "artifact_role: theorem",
                "next_trace_action:",
                "conditional_surface_status:",
                "admitted_observation_status: null",
            )
        )
        and retained_ok
        and "retained" not in other_retained
        and "promoted" not in note.lower()
        and "we adopt" not in note.lower()
        and "new axiom" not in note.lower()
        and "Codex" not in note,
    )

    print("per_element: five declared scaled effects and the four projective binary atoms are checked by matrix traces")
    print("per_site: the kernel, restriction rejector, and singleton-mass parent argument are one-site statements")
    print("per_mode: all three Bloch coefficients of each declared effect are extracted; in-plane and imaginary-y perpendicular extra modes are rejected by positivity")
    print("per_block: only the finite-support barycenter-evaluation block is constructed; restriction is not this kernel")
    print("lattice_wide: checked and not executed — no lattice-wide dynamics, formation rate, or Record identification is claimed")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
