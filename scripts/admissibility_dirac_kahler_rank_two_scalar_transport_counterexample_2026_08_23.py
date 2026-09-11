#!/usr/bin/env python3
"""Exact finite rank-two scalar transport counterexample.

The runner reconstructs two disclosed finite reflection forms through the
reviewed released7332--7334 fixture helper.  It proves one rank-two isometric
compression identity and a carefully quantified affine-admixture lemma.  It
does not select a physical readout or import any historical parent theorem.
"""

from __future__ import annotations

import ast
import hashlib
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
TRANSPORT = sp.symbols("s_t", real=True)
EXPECTED_ROWS = (4, 5, 6, 7, 8, 9, 10, 11)
EXPECTED_SCALAR = R(114, 125) + R(171, 250) * TRANSPORT
EXPECTED_GAP = R(513, 2000)
EXPECTED_DETERMINANT = R(3249, 62500) * (3 * TRANSPORT + 4) ** 2

CHECKS: list[tuple[str, bool, str]] = []


def check(name: str, condition: bool, detail: str) -> None:
    CHECKS.append((name, bool(condition), detail))


def sha256_path(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def is_zero(matrix: sp.MatrixBase) -> bool:
    return all(sp.expand(entry) == 0 for entry in matrix)


def isometry() -> sp.Matrix:
    """Expose the pair's exact two-column witness."""
    return fixture.witness_isometry()


def committed_form(tag: str, cover_t: int) -> tuple[fixture.Bench, sp.Matrix]:
    """Return the supplied finite F_T(s_t)=Herm(Sel^T r Q Sel)."""
    bench = fixture.Bench(tag, cover_t, 4)
    return bench, sp.expand(bench.form.subs(bench.carrier(st=TRANSPORT)))


def exact_fixture_checks() -> dict[str, dict]:
    x = isometry()
    expected = EXPECTED_SCALAR * sp.eye(2)
    results: dict[str, dict] = {}
    for tag, cover_t, _ in fixture.PRIMARY:
        bench, form = committed_form(tag, cover_t)
        compression = sp.expand(x.H * form * x)
        determinant = sp.factor(compression.det())
        at_small = sp.expand(compression.subs(TRANSPORT, R(1, 8)))
        at_large = sp.expand(compression.subs(TRANSPORT, R(1, 2)))
        derivative = sp.diff(sp.trace(compression) / 2, TRANSPORT)
        gap = sp.expand(sp.trace(at_large - at_small) / 2)
        results[tag] = {
            "compression": compression,
            "determinant": determinant,
        }
        check(
            f"{tag} committed row map",
            tuple(bench.rows) == EXPECTED_ROWS and form.shape == (8, 8),
            f"rows={tuple(bench.rows)}, form_shape={form.shape}",
        )
        check(
            f"{tag} exact rank-two scalar compression",
            is_zero(compression - expected),
            f"X^H F X={compression}",
        )
        check(
            f"{tag} positive and transport-sensitive",
            (
                compression.rank() == 2
                and at_small == R(399, 400) * sp.eye(2)
                and at_large == R(627, 500) * sp.eye(2)
                and derivative == R(171, 250)
                and gap == EXPECTED_GAP
                and determinant == EXPECTED_DETERMINANT
            ),
            (
                f"slope={derivative}, gap={gap}, det={determinant}, "
                f"endpoints=({at_small[0, 0]},{at_large[0, 0]})"
            ),
        )
    check(
        "rank-two isometry",
        x.H * x == sp.eye(2) and x.rank() == 2,
        f"X^H X={x.H * x}, rank={x.rank()}",
    )
    check(
        "extent-independent compressed law",
        results["8x4"]["compression"] == results["12x4"]["compression"],
        "the exact 2x2 law agrees at the two disclosed cover extents",
    )
    return results


def affine_closure_checks() -> None:
    """Check the bounded affine lemma with its necessary hypotheses.

    Let P be a sensitive positive rank-one effect.  For a nonzero PSD Q whose
    support is orthogonal to P, rank(P+epsilon Q)=rank(P)+rank(Q) for epsilon
    positive.  The affine response d+epsilon*q has at most one tuned root.  If
    effects obey 0<=E<=I, epsilon must also be small enough to preserve that
    upper bound; the displayed example checks it directly.
    """
    epsilon, d, q = sp.symbols("epsilon d q", real=True)
    response = d + epsilon * q
    polynomial = sp.Poly(response, epsilon)
    check(
        "quantified affine admixture response",
        polynomial.degree() <= 1 and polynomial.eval(0) == d,
        "for d!=0, d+epsilon*q has at most one tuned root",
    )

    p = sp.diag(1, 0)
    q_effect = sp.diag(0, 1)
    difference = sp.diag(1, -2)
    eps = R(1, 4)
    mixed = p + eps * q_effect
    raw = sp.trace(mixed * difference)
    normalized = sp.cancel(raw / sp.trace(mixed))
    check(
        "normalized nonzero-orthogonal rank-two witness",
        (
            q_effect != sp.zeros(2)
            and p * q_effect == sp.zeros(2)
            and mixed.rank() == p.rank() + q_effect.rank() == 2
            and mixed.is_positive_semidefinite is True
            and (sp.eye(2) - mixed).is_positive_semidefinite is True
            and raw == R(1, 2)
            and normalized == R(2, 5)
        ),
        f"rank={mixed.rank()}, raw={raw}, normalized={normalized}, epsilon={eps}",
    )


def native_effect_check() -> None:
    """Check one finite rank-two union effect without adopting its reading."""
    density = sp.diag(
        *(R(n, fixture.DENSITY_DENOMINATOR) for n in fixture.DENSITY_NUMERATORS)
    )
    effect = fixture.effect_for((fixture.MENU[1], fixture.MENU[2]))
    reading = fixture.trace_reading(density, effect)
    expected = R(
        fixture.DENSITY_NUMERATORS[1] + fixture.DENSITY_NUMERATORS[2],
        fixture.DENSITY_DENOMINATOR,
    )
    check(
        "finite rank-two union effect",
        (
            effect.rank() == 2
            and effect == sp.diag(0, 1, 1, 0)
            and reading == expected
            and reading > 0
        ),
        f"rank={effect.rank()}, Tr(C E_12)={reading}",
    )


def source_hygiene_check() -> None:
    tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    floats = [
        node
        for node in ast.walk(tree)
        if isinstance(node, ast.Constant) and isinstance(node.value, float)
    ]
    note = NOTE.read_text(encoding="utf-8") if NOTE.exists() else ""
    required = tuple(f"## N{i}" for i in range(1, 9))
    actual_hashes = {
        path: sha256_path(ROOT / path) for path in AUDIT_INPUT_PATHS
    }
    check(
        "source/input binding and bounded-note surface",
        (
            not floats
            and all(section in note for section in required)
            and actual_hashes == INPUT_SHA256
            and fixture.supplier_certificate()
        ),
        (
            f"float_literals={len(floats)}, "
            f"N_sections={sum(section in note for section in required)}/8, "
            f"inputs_bound={actual_hashes == INPUT_SHA256}"
        ),
    )


def main() -> int:
    exact_fixture_checks()
    affine_closure_checks()
    native_effect_check()
    source_hygiene_check()

    for name, passed, detail in CHECKS:
        print(f"{'PASS' if passed else 'FAIL'}: {name} :: {detail}")

    print("per_element: the displayed compression and the quantified affine-response lemma are exact; nonlinear readout categories remain open")
    print("per_site: the selected eight-row finite reflection form is reconstructed at the disclosed 8x4 and 12x4 covers")
    print("per_mode: the displayed rank-two scalar compression changes with the supplied s_t dial; no physical carrier identification follows")
    print("per_block: the finite rank-one-only successor fails for standard isometric compression on these two fixtures")
    print("lattice_wide: no all-lattice, continuum, physical-selector, probability-law, axiom, obligation, or TOE conclusion is licensed")

    passed = sum(ok for _, ok, _ in CHECKS)
    total = len(CHECKS)
    print(f"TOTAL: {passed}/{total} {'PASS' if passed == total else 'FAIL'}")
    return 0 if passed == total else 1


if __name__ == "__main__":
    raise SystemExit(main())
