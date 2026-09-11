#!/usr/bin/env python3
"""Alternative exact check of the finite rank-two scalar witness.

This checker shares the reviewed finite construction helper with the primary
runner, but rebuilds the compression and affine-admixture calculations through
a separate check implementation.  It is therefore corroborating evidence, not
an independent reconstruction of the fixture closure.
"""

from __future__ import annotations

import ast
import hashlib
from dataclasses import dataclass
from pathlib import Path

import sympy as sp

import admissibility_dirac_kahler_released7332_7334_fixtures_2026_09_10 as fixture


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_RANK_TWO_SCALAR_TRANSPORT_"
    "COUNTEREXAMPLE_BOUNDED_THEOREM_NOTE_2026-08-23.md"
)
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_RANK_TWO_SCALAR_TRANSPORT_COUNTEREXAMPLE_BOUNDED_THEOREM_NOTE_2026-08-23.md",
    "scripts/admissibility_dirac_kahler_released7332_7334_fixtures_2026_09_10.py",
    "scripts/admissibility_dirac_kahler_strict_neighbor_m2_gaussian_compiler_released7333_fixture_2026_09_10.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "scripts/admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_2026_08_14.py",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
)
INPUT_SHA256 = {
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
I = sp.I


@dataclass
class Reporter:
    passed: int = 0
    failed: int = 0

    def check(self, name: str, condition: bool, detail: str) -> None:
        if bool(condition):
            self.passed += 1
            status = "PASS"
        else:
            self.failed += 1
            status = "FAIL"
        print(f"{status} {name}: {detail}")

    def total(self) -> None:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")


def sha256_path(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def matrix_equal(left: sp.MatrixBase, right: sp.MatrixBase) -> bool:
    if left.shape != right.shape:
        return False
    return all(sp.simplify(a - b) == 0 for a, b in zip(left, right))


def is_exact_pd_2x2(matrix: sp.MatrixBase) -> bool:
    return bool(
        matrix.shape == (2, 2)
        and matrix_equal(matrix, matrix.H)
        and sp.simplify(matrix[0, 0]).is_positive is True
        and sp.simplify(matrix.det()).is_positive is True
    )


def reconstruct_fixture(specification: tuple[str, int, int]) -> dict:
    tag, cover_t, width = specification
    bench = fixture.Bench(tag, cover_t, width)
    form = sp.expand(bench.form.subs(bench.carrier(st=None)))
    witness = fixture.witness_isometry()
    compression = sp.expand(witness.H * form * witness)
    return {
        "tag": tag,
        "form": form,
        "witness": witness,
        "compression": compression,
    }


def check_fixture(reconstruction: dict, reporter: Reporter) -> None:
    tag = reconstruction["tag"]
    form = reconstruction["form"]
    witness = reconstruction["witness"]
    compression = reconstruction["compression"]
    identity_two = sp.eye(2)
    expected_scalar = R(114, 125) + R(171, 250) * fixture.ST
    expected_compression = expected_scalar * identity_two

    reporter.check(
        f"{tag}_FORM",
        form.shape == (8, 8)
        and form.free_symbols == {fixture.ST}
        and matrix_equal(form, form.H),
        f"shape={form.shape}, free_symbols={sorted(map(str, form.free_symbols))}",
    )
    reporter.check(
        f"{tag}_ISOMETRY",
        matrix_equal(witness.H * witness, identity_two),
        "X^dagger X=I_2",
    )
    reporter.check(
        f"{tag}_COMPRESSION",
        matrix_equal(compression, expected_compression),
        f"X^dagger F_T X=({expected_scalar}) I_2",
    )

    points = (sp.Integer(0), R(1, 8), R(1, 2), sp.Integer(1))
    point_results = []
    point_ok = True
    for point in points:
        evaluated = sp.simplify(compression.subs(fixture.ST, point))
        scalar = sp.simplify(expected_scalar.subs(fixture.ST, point))
        determinant = sp.simplify(evaluated.det())
        point_ok = bool(
            point_ok
            and determinant == scalar ** 2
            and is_exact_pd_2x2(evaluated)
        )
        point_results.append(f"{point}:{determinant}")
    reporter.check(
        f"{tag}_RATIONAL_PD",
        point_ok,
        "det(s_t)=" + ",".join(point_results) + "; all PD",
    )

    slope = compression.applyfunc(lambda entry: sp.diff(entry, fixture.ST))
    gap = sp.expand(
        compression.subs(fixture.ST, R(1, 2))
        - compression.subs(fixture.ST, R(1, 8))
    )
    reporter.check(
        f"{tag}_TRANSPORT_RESPONSE",
        matrix_equal(slope, R(171, 250) * identity_two)
        and matrix_equal(gap, R(513, 2000) * identity_two)
        and not matrix_equal(gap, sp.zeros(2)),
        "slope=(171/250)I_2; gap[1/8->1/2]=(513/2000)I_2",
    )


def check_affine_admixture_lemma(reporter: Reporter) -> None:
    """Give an explicit effect-bounded admixture for arbitrary d nonzero."""
    d = sp.Symbol("d", real=True, nonzero=True)
    q, x, y = sp.symbols("q x y", real=True)
    epsilon = sp.Symbol("epsilon", real=True, positive=True)

    delta = sp.Matrix([[d, x + I * y], [x - I * y, q]])
    rank_one = sp.diag(1, 0)
    added_ray = sp.diag(0, 1)
    rank_two = rank_one + epsilon * added_ray
    response = sp.expand(sp.trace(rank_two * delta))

    reporter.check(
        "AFFINE_RESPONSE_IDENTITY",
        matrix_equal(delta, delta.H)
        and sp.simplify(sp.trace(rank_one * delta) - d) == 0
        and sp.simplify(response - (d + epsilon * q)) == 0,
        "Tr[(P+epsilon Q)Delta]=d+epsilon q with Tr[P Delta]=d!=0",
    )
    reporter.check(
        "NONZERO_ORTHOGONAL_PSD_SUPPORT",
        added_ray != sp.zeros(2)
        and rank_one * added_ray == sp.zeros(2)
        and added_ray.is_positive_semidefinite is True
        and rank_one.rank() + added_ray.rank() == 2,
        "Q is nonzero PSD, has support orthogonal to P, and ambient dimension is two",
    )

    sum_squares = d ** 2 + q ** 2
    epsilon_star = sp.factor(d ** 2 / (2 * sum_squares))
    persisted = sp.factor(response.subs(epsilon, epsilon_star))
    positive_numerator = sp.expand(2 * sum_squares + d * q)
    positive_certificate = (
        R(3, 2) * sum_squares + R(1, 2) * (d + q) ** 2
    )
    expected_persisted = d * positive_numerator / (2 * sum_squares)
    rank_two_star = rank_two.subs(epsilon, epsilon_star)

    reporter.check(
        "AFFINE_ADMIXTURE_EFFECT",
        epsilon_star.is_positive is True
        and sp.factor(1 - epsilon_star).is_positive is True
        and rank_two_star.rank() == 2
        and rank_two_star.is_positive_semidefinite is True
        and (sp.eye(2) - rank_two_star).is_positive_semidefinite is True,
        "epsilon*=d^2/[2(d^2+q^2)] is in (0,1) and gives a rank-2 effect",
    )
    reporter.check(
        "AFFINE_SENSITIVITY_PERSISTS",
        sp.simplify(positive_numerator - positive_certificate) == 0
        and positive_certificate.is_positive is True
        and sp.simplify(persisted - expected_persisted) == 0,
        "response=d[2(d^2+q^2)+dq]/[2(d^2+q^2)] is nonzero",
    )


def source_binding_check(reporter: Reporter) -> None:
    tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    floats = [
        node
        for node in ast.walk(tree)
        if isinstance(node, ast.Constant) and isinstance(node.value, float)
    ]
    actual = {path: sha256_path(ROOT / path) for path in AUDIT_INPUT_PATHS}
    reporter.check(
        "SOURCE_INPUT_BINDING",
        (
            not floats
            and actual == INPUT_SHA256
            and fixture.supplier_certificate()
            and all(f"## N{i}" in NOTE.read_text(encoding="utf-8") for i in range(1, 9))
        ),
        f"float_literals={len(floats)}, inputs_bound={actual == INPUT_SHA256}",
    )


def main() -> int:
    reporter = Reporter()
    try:
        reporter.check(
            "FINITE_SUPPLIER",
            fixture.supplier_certificate(),
            "reviewed finite helper and current Block105 bytes are bound",
        )
        reconstructions = [
            reconstruct_fixture(specification) for specification in fixture.PRIMARY
        ]
        for reconstruction in reconstructions:
            check_fixture(reconstruction, reporter)
        reporter.check(
            "CROSS_EXTENT_COMPRESSION",
            matrix_equal(
                reconstructions[0]["compression"],
                reconstructions[1]["compression"],
            ),
            "8x4 and 12x4 give the same exact rank-2 affine compression",
        )
        check_affine_admixture_lemma(reporter)
        source_binding_check(reporter)
    except Exception as exc:
        reporter.check("UNCAUGHT_EXCEPTION", False, f"{type(exc).__name__}: {exc}")

    reporter.total()
    return 1 if reporter.failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
