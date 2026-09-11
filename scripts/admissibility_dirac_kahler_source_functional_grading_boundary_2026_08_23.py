#!/usr/bin/env python3
"""Exact finite Gaussian source-functional and reflection-boundary checks.

Formal differentiation fixes the covariance and Wick tower for any supplied
matrix.  The ordinary complex Gaussian interpretation is invoked only after a
separate positive-Hermitian-part certificate on each disclosed finite fixture.
The historical Block107 row/column comparison is dated provenance, not a claim
about a current canonical implementation.
"""

from __future__ import annotations

import ast
import hashlib
from pathlib import Path

import sympy as sp

import admissibility_dirac_kahler_released7332_7334_fixtures_2026_09_10 as fixture


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SOURCE_FUNCTIONAL_GRADING_BOUNDARY_"
    "BOUNDED_THEOREM_NOTE_2026-08-23.md"
)
AXIOMS = ROOT / "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY = ROOT / "docs/audit/data/axiom_premise_nodes.json"

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SOURCE_FUNCTIONAL_GRADING_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-23.md",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_RANK_TWO_SCALAR_TRANSPORT_COUNTEREXAMPLE_BOUNDED_THEOREM_NOTE_2026-08-23.md",
    "scripts/admissibility_dirac_kahler_released7332_7334_fixtures_2026_09_10.py",
    "scripts/admissibility_dirac_kahler_strict_neighbor_m2_gaussian_compiler_released7333_fixture_2026_09_10.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "scripts/admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_2026_08_14.py",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
)
INPUT_SHA256 = {
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SOURCE_FUNCTIONAL_GRADING_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-23.md": "8d96ae29c1e3f31d39eb55189488a2253a19391fe1e0f7d6ccb678f86a73a5b4",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_RANK_TWO_SCALAR_TRANSPORT_COUNTEREXAMPLE_BOUNDED_THEOREM_NOTE_2026-08-23.md": "79237becf28b2855ce021b554cde830b03edd2e9713d06efe7ffdc90302784aa",
    "scripts/admissibility_dirac_kahler_released7332_7334_fixtures_2026_09_10.py": "594e7032f453fec4c6791067a147d1544636ddce9567a87a3449352b5546d5f5",
    "scripts/admissibility_dirac_kahler_strict_neighbor_m2_gaussian_compiler_released7333_fixture_2026_09_10.py": "8d2e071da05f0e540c8ec061b5dbea6cb996040a33b90efcd2f6e11b73d52cd2",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md": "9a615a79511ffc0dac0d1cf54388153604ce7c341496654fd709ed8873302a33",
    "scripts/admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_2026_08_14.py": "5499cc2c1a75f19e07b717aeb6c9ef7779c45e1c5757d84701c5d88ca92bf445",
    "docs/MINIMAL_AXIOMS_2026-06-29.md": "93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753",
    "docs/audit/data/axiom_premise_nodes.json": "615f13aaa70e82d50cdf1a8aa479eb40d6ce70a3bb7b152ac63fd88bee341f37",
}
AUDIT_TIMEOUT_SEC = 60

R = sp.Rational
ZERO = sp.Integer(0)
DIALS = (ZERO, R(1, 4))
EXPECTED_INERTIA = {
    ("8x4", ZERO): (6, 2, 0),
    ("8x4", R(1, 4)): (6, 2, 0),
    ("12x4", ZERO): (4, 4, 0),
    ("12x4", R(1, 4)): (4, 4, 0),
}
EXPECTED_ACTION_REFLECTION_DEFECT_00 = {
    "8x4": R(-997, 27456),
    "12x4": R(3167, 10560),
}
EXPECTED_HALF_TRACE_GAP = {
    "8x4": R(73977924244224, 1492124486100431),
    "12x4": R(
        150346029799280479942166602650413136160,
        2455275247171512614379752553769527826469,
    ),
}


class Reporter:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, name: str, condition: bool, detail: str) -> None:
        ok = bool(condition)
        self.passed += int(ok)
        self.failed += int(not ok)
        print(f"{'PASS' if ok else 'FAIL'} {name}: {detail}")

    def total(self) -> None:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")


def sha256_path(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def matrix_equal(left: sp.MatrixBase, right: sp.MatrixBase) -> bool:
    return left.shape == right.shape and all(
        sp.expand(a - b) == 0 for a, b in zip(left, right)
    )


def source_functional_checks(report: Reporter) -> None:
    """Differentiate a formal normalized two-source generating series."""
    bj0, bj1, j0, j1 = sp.symbols("bar_j0 bar_j1 j0 j1")
    g00, g01, g10, g11 = sp.symbols("g00 g01 g10 g11")
    bar_j = sp.Matrix((bj0, bj1))
    source_j = sp.Matrix((j0, j1))
    covariance = sp.Matrix(((g00, g01), (g10, g11)))
    exponent = (bar_j.T * covariance * source_j)[0]
    normalized = sp.exp(exponent)
    at_zero = {bj0: 0, bj1: 0, j0: 0, j1: 0}

    two_point = sp.Matrix(
        2,
        2,
        lambda i, j: sp.diff(normalized, bar_j[i], source_j[j]).subs(at_zero),
    )
    four_point = sp.diff(normalized, bj0, bj1, j0, j1).subs(at_zero)
    same_type = sp.diff(normalized, bj0, bj1).subs(at_zero)
    report.check(
        "FORMAL_SOURCE_TWO_POINT",
        matrix_equal(two_point, covariance),
        "formal d_barJ d_J exp(barJ G J)|0 = G exactly",
    )
    report.check(
        "FORMAL_SOURCE_WICK_PERMANENT",
        sp.expand(four_point - (g00 * g11 + g01 * g10)) == 0
        and same_type == 0,
        "formal degree two is the permanent; same-polarity contractions vanish",
    )
    report.check(
        "FORMAL_NORMALIZED_VACUUM",
        normalized.subs(at_zero) == 1,
        "the formal normalized degree-zero coefficient is 1",
    )

    zq, zq_bar = sp.symbols("Z_Q Z_Qbar", nonzero=True)
    unnormalized = zq * normalized
    doubled = zq * zq_bar
    scaled_two_point = sp.Matrix(
        2,
        2,
        lambda i, j: sp.diff(
            doubled * normalized, bar_j[i], source_j[j]
        ).subs(at_zero),
    )
    report.check(
        "VACUUM_CATEGORY_SPLIT",
        unnormalized.subs(at_zero) == zq
        and doubled != zq
        and matrix_equal(scaled_two_point, doubled * covariance),
        "one-copy Z_Q, doubled Z_Q Z_Qbar, and normalized coefficient 1 are distinct",
    )


def historical_orientation_check(report: Reporter) -> None:
    """Compare the two exact conventions in the archived original107 body."""
    symbols = sp.symbols("g0:16")
    generic = sp.Matrix(4, 4, symbols)

    def site_index(time: int, space: int) -> int:
        assert space == 0
        return time % 4

    code = fixture.historical107_history_gram(generic, site_index)
    displayed = fixture.historical107_displayed_gram(generic, site_index)
    report.check(
        "HISTORICAL107_ORIENTATION_COMPARISON",
        matrix_equal(code, displayed.T) and not matrix_equal(code, displayed),
        "the archived original107 code is the transpose of its displayed equation on generic G",
    )


def selection(matrix: sp.MatrixBase, rows: tuple[int, ...]) -> sp.Matrix:
    return sp.Matrix(
        len(rows),
        len(rows),
        lambda a, b: sp.expand(matrix[rows[a], rows[b]]),
    )


def exact_fixture_checks(report: Reporter) -> None:
    """Measure four supplied finite cells and certify Gaussian convergence."""
    isometry = fixture.witness_isometry()
    projector = sp.expand(isometry * isometry.H)
    swap = sp.Matrix(((0, 1), (1, 0)))
    u, v = sp.symbols("u v", real=True)
    weight_family = sp.zeros(8, 2)
    weight_family[0, 0], weight_family[4, 0] = u, v
    weight_family[2, 1], weight_family[6, 1] = u, v
    local_shift_two = sp.zeros(8, 8)
    for time_block in range(2):
        for space in range(4):
            local_shift_two[
                4 * time_block + (space + 2) % 4,
                4 * time_block + space,
            ] = 1
    report.check(
        "RANK_TWO_ISOMETRY",
        matrix_equal(isometry.H * isometry, sp.eye(2)),
        "X=[(4e0+3e4)/5,(4e2+3e6)/5] has X^dag X=I_2",
    )
    report.check(
        "PERIOD_TWO_DOES_NOT_SELECT_WEIGHTS",
        matrix_equal(local_shift_two * weight_family, weight_family * swap),
        "every weight pair (u,v), not only (4/5,3/5), intertwines shift by two",
    )

    for name, cover_t, width in fixture.PRIMARY:
        bench = fixture.Bench(f"source-{name}", cover_t, width)
        field = fixture.graded_carrier(
            bench.fx,
            bench.c,
            fixture.CARRIER_SIGMA,
        )
        hodge = sp.expand(bench.Hq.subs(bench.carrier(st=ZERO)))
        report.check(
            f"{name}_HODGE_POSITIVE_RESTRICTION_CERTIFICATE",
            fixture.hodge_restriction_certificate(bench, field),
            "positive local Hodge blocks and full-rank antiperiodic restriction give H_q>0",
        )

        injection = sp.zeros(bench.N, len(bench.rows))
        for column, row in enumerate(bench.rows):
            injection[row, column] = 1
        ambient_shift_two = sp.zeros(bench.N, bench.N)
        for time in range(bench.T):
            for space in range(bench.lx):
                ambient_shift_two[
                    bench.lx * time + (space + 2) % bench.lx,
                    bench.lx * time + space,
                ] = 1

        compressed: dict[sp.Expr, sp.Matrix] = {}
        determinants: dict[sp.Expr, sp.Expr] = {}
        convergent: dict[sp.Expr, bool] = {}
        for dial in DIALS:
            substitutions = bench.carrier(st=dial)
            q_matrix = sp.expand(bench.Q.subs(substitutions))
            connection = sp.expand(bench.Kq.subs(substitutions))
            hermitian_part_q = sp.expand((q_matrix + q_matrix.H) / 2)
            convergent[dial] = bool(
                matrix_equal(connection.H, -connection)
                and matrix_equal(hermitian_part_q, hodge)
            )
            report.check(
                f"{name}_{dial}_GAUSSIAN_CONVERGENCE_PREMISES",
                convergent[dial],
                "K_q is anti-Hermitian and Herm(Q)=H_q; the positive H_q certificate applies",
            )

            determinants[dial] = sp.factor(q_matrix.det(method="domain-ge"))
            covariance = sp.expand(q_matrix.inv(method="LU"))
            displayed_kernel = selection(bench.r * covariance.T, bench.rows)
            code_order_kernel = selection(covariance * bench.r, bench.rows)
            anti = sp.expand(displayed_kernel - displayed_kernel.H)
            hermitian_kernel = sp.expand(
                (displayed_kernel + displayed_kernel.H) / 2
            )
            action_defect = sp.expand(bench.r * q_matrix.H * bench.r - q_matrix)
            restricted = sp.expand(isometry.H * displayed_kernel * isometry)
            restricted_code = sp.expand(
                isometry.H * code_order_kernel * isometry
            )
            compressed[dial] = restricted

            local_q = selection(q_matrix, bench.rows)
            action_form = sp.expand(bench.form.subs(substitutions))
            residual_r = sp.expand(
                (sp.eye(8) - projector)
                * selection(bench.r, bench.rows)
                * isometry
            )
            residual_q = sp.expand((sp.eye(8) - projector) * local_q * isometry)
            residual_form = sp.expand(
                (sp.eye(8) - projector) * action_form * isometry
            )

            report.check(
                f"{name}_{dial}_FULL_SOURCE_BOUNDARY",
                all(sp.im(value) == 0 for value in q_matrix)
                and all(sp.im(value) == 0 for value in covariance)
                and matrix_equal(code_order_kernel, displayed_kernel.H)
                and not matrix_equal(displayed_kernel, displayed_kernel.H)
                and anti.rank() == 8
                and fixture.real_symmetric_inertia(hermitian_kernel)
                == EXPECTED_INERTIA[(name, dial)],
                (
                    "real fixture; the two historical orders are adjoints; "
                    f"raw anti-Hermitian rank=8; inertia={EXPECTED_INERTIA[(name, dial)]}"
                ),
            )
            report.check(
                f"{name}_{dial}_REFLECTION_COVARIANCE_DEFECT",
                action_defect[0, 0]
                == EXPECTED_ACTION_REFLECTION_DEFECT_00[name],
                f"(r Q^dag r-Q)[0,0]={EXPECTED_ACTION_REFLECTION_DEFECT_00[name]} != 0",
            )
            report.check(
                f"{name}_{dial}_POSITIVE_RESTRICTION",
                matrix_equal(restricted, restricted.H)
                and matrix_equal(restricted, restricted_code)
                and restricted[0, 0] > 0
                and restricted.det() > 0,
                "X^dag K X is convention-independent here and positive by exact Sylvester minors",
            )
            report.check(
                f"{name}_{dial}_X_NOT_SELECTED_BY_INVARIANCE",
                matrix_equal(ambient_shift_two * q_matrix, q_matrix * ambient_shift_two)
                and matrix_equal(ambient_shift_two * bench.r, bench.r * ambient_shift_two)
                and matrix_equal(
                    ambient_shift_two * injection * isometry,
                    injection * isometry * swap,
                )
                and residual_r.rank() == 2
                and residual_q.rank() == 2
                and residual_form.rank() == 2,
                "shift-two covariance explains the shape but does not select X by invariance",
            )

        gap = sp.expand(sp.trace(compressed[R(1, 4)] - compressed[ZERO]) / 2)
        report.check(
            f"{name}_RESTRICTION_TRANSPORT_RESPONSE",
            gap == EXPECTED_HALF_TRACE_GAP[name] and gap > 0,
            f"exact half-trace gap from s_t=0 to 1/4 is {gap}",
        )
        report.check(
            f"{name}_CONVERGENT_ONE_COPY_VACUUM_RESPONSE",
            all(convergent.values())
            and determinants[ZERO] > 0
            and determinants[R(1, 4)] > 0
            and determinants[ZERO] != determinants[R(1, 4)],
            "Herm(Q)>0 licenses the ordinary Gaussian; det(Q)>0 changes with the dial",
        )


def authority_and_scope_checks(report: Reporter) -> None:
    axioms = AXIOMS.read_text(encoding="utf-8")
    registry = REGISTRY.read_text(encoding="utf-8")
    note = NOTE.read_text(encoding="utf-8") if NOTE.exists() else ""
    source_tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    floats = [
        node
        for node in ast.walk(source_tree)
        if isinstance(node, ast.Constant) and isinstance(node.value, float)
    ]
    actual_hashes = {
        path: sha256_path(ROOT / path) for path in AUDIT_INPUT_PATHS
    }
    report.check(
        "FOUNDATION_AUTHORITY_BOUNDARY",
        "source/action and physical-observable identification" in axioms
        and "Born weight values" in axioms
        and '"minimal_axioms"' in registry,
        "current foundation leaves source/observable and Born/readout selection open",
    )
    report.check(
        "SOURCE_INPUT_BINDING",
        actual_hashes == INPUT_SHA256 and fixture.supplier_certificate(),
        f"inputs_bound={actual_hashes == INPUT_SHA256}; finite_supplier_bound={fixture.supplier_certificate()}",
    )
    report.check(
        "EXACT_AST_SURFACE",
        not floats,
        f"float_literals={len(floats)} on the primary runner AST",
    )
    report.check(
        "BOUNDED_NO_GO_SURFACE",
        all(f"## N{i}" in note for i in range(1, 9))
        and "Claim type:** `bounded_theorem`" in note,
        "N1-N8 and bounded theorem metadata are present; this is not an audit verdict",
    )


def main() -> int:
    report = Reporter()
    try:
        source_functional_checks(report)
        historical_orientation_check(report)
        exact_fixture_checks(report)
        authority_and_scope_checks(report)
    except Exception as exc:
        report.check("UNCAUGHT_EXCEPTION", False, f"{type(exc).__name__}: {exc}")

    print("per_element: formal differentiation fixes G and Wick permanents; ordinary Gaussian language is used only where Herm(Q)>0 is certified")
    print("per_site: four supplied finite cells have non-Hermitian full selected kernels and one positive imposed rank-two restriction")
    print("per_mode: the positive restriction and convergent one-copy vacuum change at two supplied dial values; the dial is not physically identified")
    print("per_block: the algebraic Wick identities, finite raw-kernel boundary, positive route, and dated original107 convention comparison are preserved")
    print("lattice_wide: no universal OS, physical event/source, probability, continuum, axiom, obligation, or TOE conclusion is claimed")
    report.total()
    return 1 if report.failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
