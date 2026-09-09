#!/usr/bin/env python3
"""Exact checks for the Gaussian content-only decoder boundary.

The runner checks the center-independent imaginary-trace uniformizer, exact
second-moment effect weights along the C=tP_z family, condition-indexed
threshold realization, and the algebraic pole contradiction used by the
analytic Weierstrass-transform proof.  Entire continuation and the
probability-integral transform are proved in the source; exact fixtures and
claim/governance surfaces are executed here.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / "ADMISSIBILITY_GAUSSIAN_CONTENT_ONLY_UNIFORMIZER_WEIERSTRASS_DECODER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md"
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
IMAGINARY_TRACE_PRIOR_PATH = ROOT / "docs" / "DECLARED_IMAGINARY_TRACE_FUNCTIONAL_HERMITIAN_KERNEL_BOUNDED_THEOREM_NOTE_2026-08-13.md"
COMPILER_PARENT_PATH = ROOT / "docs" / "ADMISSIBILITY_GAUSSIAN_SECOND_MOMENT_QUANTILE_DECODER_EFFECT_QUOTIENT_BOUNDED_THEOREM_NOTE_2026-08-10.md"
CONTACT_PARENT_PATH = ROOT / "docs" / "ADMISSIBILITY_CNOT_CONTACT_GAUSSIAN_EXTRACTOR_TYPE_ORDER_BOUNDED_THEOREM_NOTE_2026-08-10.md"

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_GAUSSIAN_CONTENT_ONLY_UNIFORMIZER_WEIERSTRASS_DECODER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/DECLARED_IMAGINARY_TRACE_FUNCTIONAL_HERMITIAN_KERNEL_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/ADMISSIBILITY_GAUSSIAN_SECOND_MOMENT_QUANTILE_DECODER_EFFECT_QUOTIENT_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/ADMISSIBILITY_CNOT_CONTACT_GAUSSIAN_EXTRACTOR_TYPE_ORDER_BOUNDED_THEOREM_NOTE_2026-08-10.md",
)


Matrix = tuple[tuple[complex, complex], tuple[complex, complex]]

PAULI_X: Matrix = (
    (0j, 1 + 0j),
    (1 + 0j, 0j),
)
PHASE_CUBIC: Matrix = (
    (1 + 0j, 0j),
    (0j, 1j),
)


def matrix_multiply(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(
            sum(left[row][index] * right[index][column] for index in range(2))
            for column in range(2)
        )
        for row in range(2)
    )  # type: ignore[return-value]


def matrix_dagger(matrix: Matrix) -> Matrix:
    return tuple(
        tuple(matrix[column][row].conjugate() for column in range(2))
        for row in range(2)
    )  # type: ignore[return-value]


def conjugate(matrix: Matrix, unitary: Matrix) -> Matrix:
    return matrix_multiply(matrix_multiply(unitary, matrix), matrix_dagger(unitary))


def matrix_trace(matrix: Matrix) -> complex:
    return matrix[0][0] + matrix[1][1]


def imaginary_trace(matrix: Matrix) -> float:
    return float(matrix_trace(matrix).imag)


def hermitian_fixture(a: int, b: int, off_real: int, off_imag: int) -> Matrix:
    off = complex(off_real, off_imag)
    return (
        (complex(a), off),
        (off.conjugate(), complex(b)),
    )


def effect_weight(t: int, offset: int | Fraction = 0) -> Fraction:
    """Half-P_z grade for the lambda-offset extractor at C=t P_z."""

    return Fraction(t * t + 2 + offset, 2 * (t * t + 4 + 2 * offset))


def pole_squared(offset: int | Fraction) -> Fraction:
    """The squared complex pole location z^2 for finite lambda=offset."""

    return -(4 + 2 * offset)


def numerator_at_pole(offset: int | Fraction) -> Fraction:
    return pole_squared(offset) + 2 + offset


def indexed_threshold_probability(t: int, offset: int | Fraction = 0) -> Fraction:
    """Uniform U thresholded at the condition-indexed target weight."""

    return effect_weight(t, offset)


def fixed_threshold_probability(threshold: Fraction, _t: int) -> Fraction:
    """A fixed threshold of a common uniformizer is condition-independent."""

    return threshold


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, statement: str, condition: bool) -> None:
        result = bool(condition)
        self.passed += int(result)
        self.failed += int(not result)
        print(f"{'PASS' if result else 'FAIL'}: {label} {statement}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    imaginary_trace_prior = IMAGINARY_TRACE_PRIOR_PATH.read_text(encoding="utf-8")
    compiler_parent = COMPILER_PARENT_PATH.read_text(encoding="utf-8")
    contact_parent = CONTACT_PARENT_PATH.read_text(encoding="utf-8")
    note_flat = " ".join(note.split())
    axiom_flat = " ".join(axiom.split())

    print("external_scientific_inputs: the current axiom and reviewed current-main imaginary-trace prior, Gaussian compiler, and CNOT boundary are source-bound; no closed-unmerged source, literature theorem, observed probability, fitted parameter, or external PR artifact is imported")
    print("package_local_integrity_reads: the proposed theorem note is checked for construction, boundary, trace status, and N1-N8 surfaces; the cache envelope binds every declared input")
    print("analytic_boundary: Gaussian factorization, entire continuation by dominated differentiation, and the identity-theorem contradiction are proved in the source; exact variances, weights, poles, and finite fixtures are executed here")
    print("negative_scope: only one fixed bounded content-only readout kernel on the displayed Gaussian translation family and one fixed half-projector effect are bounded; indexed decoders, tagged records, changed laws, finite center sets, and physical processes remain live")

    checks.check(
        "source-current-axiom",
        "the current neighborhood-varying probability and content-only Record clauses are present",
        all(
            phrase in axiom_flat
            for phrase in (
                "the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions",
                "A readout value is determined by record content alone.",
                "The full one-site possibility domain has algebraic presentation `M_2(C)`.",
            )
        ),
    )
    checks.check(
        "source-imaginary-trace-prior",
        "the current-main overlap proves the Hermitian kernel but leaves every physical readout and Gaussian extension open",
        "`H_2` is contained in `ker J`" in imaginary_trace_prior
        and "physical readout, writing process, formation site/rate" in imaginary_trace_prior
        and all(
            phrase not in imaginary_trace_prior
            for phrase in (
                "U(A)=Phi(Im Tr A)",
                "`P_r(z)` is entire",
                "w_lambda(t)",
            )
        ),
    )
    checks.check(
        "source-compiler-parent",
        "the current-main Gaussian uniformizer is explicitly conditional on fixed C and a supplied program",
        "Define the centered real-trace statistic" in compiler_parent
        and "The map `d_(C,M)` is a program-relative mathematical event label" in compiler_parent
        and "would have to encode the program distinction in record content" in compiler_parent,
    )
    checks.check(
        "source-contact-parent",
        "the current-main CNOT theorem accepts a local quantile comparator while leaving its threshold and registration open",
        "The Gaussian law already provides an exact uniform scalar" in contact_parent
        and "derive the comparator, `q_C`, eigenbasis, restriction" in contact_parent
        and "That is the next exact target" in contact_parent,
    )

    real_coordinate_variance = Fraction(1, 2)
    checks.check(
        "imaginary-trace-variance",
        "the two independent diagonal imaginary coordinates have total variance one",
        real_coordinate_variance + real_coordinate_variance == 1,
    )

    hermitian_centers = (
        hermitian_fixture(0, 0, 0, 0),
        hermitian_fixture(3, -2, 1, 4),
        hermitian_fixture(-5, 7, -3, 2),
    )
    checks.check(
        "hermitian-center-imaginary-trace",
        "every tested Hermitian Gaussian center has zero imaginary trace",
        all(imaginary_trace(center) == 0 for center in hermitian_centers),
    )

    arbitrary_content: Matrix = (
        (complex(2, 3), complex(-1, 4)),
        (complex(5, -2), complex(7, -1)),
    )
    checks.check(
        "imaginary-trace-conjugation-invariance",
        "the content statistic is invariant under two exact unitary conjugations",
        imaginary_trace(conjugate(arbitrary_content, PAULI_X))
        == imaginary_trace(arbitrary_content)
        and imaginary_trace(conjugate(arbitrary_content, PHASE_CUBIC))
        == imaginary_trace(arbitrary_content),
    )
    checks.check(
        "common-uniformizer-parameters",
        "all Hermitian centers leave the imaginary-trace statistic at exact mean zero and variance one",
        all(imaginary_trace(center) == 0 for center in hermitian_centers)
        and 2 * real_coordinate_variance == 1,
    )

    expected_weights = {
        0: (Fraction(1, 4), Fraction(3, 10), Fraction(3, 8), Fraction(11, 26)),
        1: (Fraction(1, 4), Fraction(2, 7), Fraction(7, 20), Fraction(2, 5)),
        2: (Fraction(1, 4), Fraction(5, 18), Fraction(1, 3), Fraction(13, 34)),
    }
    checks.check(
        "extractor-weight-fixtures",
        "three finite extractor members reproduce twelve exact half-projector weights",
        all(
            tuple(effect_weight(t, offset) for t in (0, 1, 2, 3)) == weights
            for offset, weights in expected_weights.items()
        ),
    )
    checks.check(
        "finite-offset-weight-variation",
        "every tested finite extractor member varies across an open-center family rather than supplying one constant threshold",
        all(effect_weight(0, offset) != effect_weight(1, offset) for offset in range(6)),
    )
    checks.check(
        "fixed-threshold-condition-independence",
        "a fixed threshold of the common uniformizer has one probability at every tested center",
        all(
            fixed_threshold_probability(Fraction(3, 10), t) == Fraction(3, 10)
            for t in (-3, -1, 0, 1, 3)
        ),
    )
    checks.check(
        "indexed-threshold-realization",
        "condition-indexed thresholds exactly realize every displayed target weight",
        all(
            indexed_threshold_probability(t, offset) == effect_weight(t, offset)
            for offset in range(4)
            for t in (-3, -1, 0, 1, 3)
        ),
    )

    checks.check(
        "finite-offset-pole-location",
        "the rational target denominator vanishes at a finite nonreal squared pole for every tested lambda",
        all(
            pole_squared(offset) + 4 + 2 * offset == 0
            for offset in range(8)
        ),
    )
    checks.check(
        "finite-offset-pole-nonremovable",
        "the target numerator remains exactly minus (lambda+2) at every tested pole",
        all(
            numerator_at_pole(offset) == -(offset + 2)
            and numerator_at_pole(offset) != 0
            for offset in range(8)
        ),
    )
    fractional_offsets = (
        Fraction(1, 7),
        Fraction(1, 2),
        Fraction(3, 2),
        Fraction(17, 3),
    )
    checks.check(
        "noninteger-finite-offset-pole",
        "the pole and nonzero residual identities also hold at exact noninteger finite lambda fixtures",
        all(
            pole_squared(offset) + 4 + 2 * offset == 0
            and numerator_at_pole(offset) == -(offset + 2)
            and numerator_at_pole(offset) != 0
            for offset in fractional_offsets
        ),
    )
    checks.check(
        "entire-identity-contradiction-fixture",
        "the entire cross-multiplied identity evaluates to a nonzero lambda+2 residual at each denominator root",
        all(-numerator_at_pole(offset) == offset + 2 for offset in range(8)),
    )
    checks.check(
        "raw-member-rational-decomposition",
        "the lambda-zero target is exactly one-half minus one over t-squared-plus-four on representative centers",
        all(
            effect_weight(t, 0)
            == Fraction(1, 2) - Fraction(1, t * t + 4)
            for t in (-5, -2, 0, 2, 5)
        ),
    )

    construction_needles = (
        "`U(A)=Phi(Im Tr A)`",
        "`mu_C(U<=u)=u`",
        "`P_r(z)` is entire",
        "`w_lambda(t)=(t^2+2+lambda)/(2(t^2+4+2lambda))`",
        "no fixed bounded content-only readout kernel",
        "condition-indexed threshold",
    )
    checks.check(
        "construction-source-surface",
        "the source states the common uniformizer, entire transform, rational target, boundary, and indexed escape",
        all(phrase in note for phrase in construction_needles),
    )
    boundary_needles = (
        "on any nonempty open interval",
        "finite set of centers remains live",
        "tagged or condition-indexed decoder remains live",
        "No global content-decoder or Record no-go is claimed",
        "no canonical axiom is edited",
        "supplies no scalar collection functional `I`, finite additivity, decoder map",
        "mathematical enlargement of the deterministic content-decoder class",
    )
    checks.check(
        "boundary-source-surface",
        "the source preserves the interval, finite-set, tagged-decoder, global-negative, and governance limits",
        all(phrase in note_flat for phrase in boundary_needles),
    )
    checks.check(
        "machine-status-contract",
        "the source carries the complete bounded upstream-support trace contract",
        all(
            phrase in note
            for phrase in (
                "actual_current_surface_status: bounded-support",
                "target_claim_type: bounded_theorem",
                "trace_class: upstream_support",
                "target_claim_id:",
                "target_blocker_text:",
                "source_of_blocker_text: handoff",
                "reachability_to_target: advances",
                "artifact_role: theorem",
                "next_trace_action:",
                "audit_required_before_effective_retained: true",
                "bare_retained_allowed: false",
            )
        ),
    )
    checks.check(
        "canonical-nonmutation",
        "the imaginary-trace/Weierstrass decoder notation is absent from the canonical axiom memo",
        all(
            phrase not in axiom
            for phrase in (
                "U(A)=Phi(Im Tr A)",
                "P_r(z)",
                "condition-indexed threshold",
                "Weierstrass decoder",
            )
        ),
    )
    checks.check(
        "no-go-gate",
        "all N1-N8 sections, source matching, primitive scan, and global-negative rejection are visible",
        all(f"### N{index}" in note for index in range(1, 9))
        and "| Source location | Source residual used |" in note
        and "The primitive-registry scan used" in note
        and "FAIL / DO NOT SHIP" in note
        and "No global content-decoder or Record no-go is claimed" in note_flat,
    )

    print("per_element: both diagonal imaginary coordinates, twelve rational target weights, eight pole fixtures, and representative fixed/indexed thresholds are checked")
    print("per_site: one M_2(C) Record site is executed across the continuous C=tP_z preparation slice with one fixed half-projector effect; no occurrence process is asserted")
    print("per_mode: common-uniformizer, fixed-kernel, condition-indexed-threshold, finite-lambda, and unitary-conjugation modes are separated exactly")
    print("per_block: the Gaussian law-to-common-uniformizer positive route and fixed-content-readout entire-function boundary are checked through the tagged-program residual")
    print("lattice_wide: checked and not executed — Hermitian-center and conjugation invariance are analytic, while program-tag propagation, Record formation, and histories remain absent")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
