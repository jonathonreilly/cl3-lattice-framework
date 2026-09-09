#!/usr/bin/env python3
"""Companion finite checks for the Regge lift/refinement theorem.

The checker uses a genuinely separate dense Schur example.  Its metric/gauge
and Fourier calculations reimplement the primary formulas while sharing the
declared finite fixture and Regge definitions.  Importing this module does not
read the primary cache; that binding is checked only when the checker is
executed as an entry point.
"""
from __future__ import annotations

import json
from pathlib import Path
import re

import numpy as np
from scipy.linalg import eigvalsh, null_space

import regge_tt_observable_refinement_finite_fixture_2026_09_09 as fixture


AUDIT_TIMEOUT_SEC = 30
ROOT = Path(__file__).resolve().parents[1]
NOTE = "docs/ADMISSIBILITY_REGGE_TT_RECORD_OBSERVABLE_INVERSE_AMPLIFICATION_REFINEMENT_GATE_BOUNDED_THEOREM_NOTE_2026-08-23.md"
PRIMARY = "scripts/admissibility_regge_tt_record_observable_inverse_amplification_refinement_gate_2026_08_23.py"
PRIMARY_CACHE = "logs/runner-cache/admissibility_regge_tt_record_observable_inverse_amplification_refinement_gate_2026_08_23.txt"
FIXTURE = "scripts/regge_tt_observable_refinement_finite_fixture_2026_09_09.py"
REGGE = "scripts/frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09.py"
CHECKER = "scripts/regge_tt_observable_refinement_independent_check_2026_09_09.py"
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_REGGE_TT_RECORD_OBSERVABLE_INVERSE_AMPLIFICATION_REFINEMENT_GATE_BOUNDED_THEOREM_NOTE_2026-08-23.md",
    "scripts/admissibility_regge_tt_record_observable_inverse_amplification_refinement_gate_2026_08_23.py",
    "logs/runner-cache/admissibility_regge_tt_record_observable_inverse_amplification_refinement_gate_2026_08_23.txt",
    "scripts/regge_tt_observable_refinement_finite_fixture_2026_09_09.py",
    "scripts/frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09.py",
    "scripts/regge_tt_observable_refinement_independent_check_2026_09_09.py",
)


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, name: str, condition: bool, detail: str) -> None:
        ok = bool(condition)
        print(f"{'PASS' if ok else 'FAIL'} {name}: {detail}")
        self.passed += int(ok)
        self.failed += int(not ok)


def negative_fixed_schur_control() -> dict[str, float | bool]:
    """Check the block identity and the negative-definite F branch directly."""
    a = -np.diag([2.0, 3.0, 5.0])
    b = np.asarray([[0.2, -0.1], [0.3, 0.4], [-0.2, 0.1]])
    schur = np.asarray([[1.4, 0.25], [0.25, -0.8]])
    a_inverse = np.linalg.inv(a)
    d = schur + b.T @ a_inverse @ b
    hessian = np.block([[a, b], [b.T, d]])
    on = np.asarray([[1.0, 0.2], [0.1, 1.1], [0.4, -0.3]])
    od = np.asarray([[0.3, -0.4], [0.7, 0.2]])
    observable = np.vstack((on, od))

    fixed = on.T @ a_inverse @ on
    dressed = od - b.T @ a_inverse @ on
    correction = dressed.T @ np.linalg.solve(schur, dressed)
    direct = observable.T @ np.linalg.solve(hessian, observable)
    identity_error = float(np.linalg.norm(direct - fixed - correction))
    fixed_eigenvalues = np.linalg.eigvalsh(0.5 * (fixed + fixed.T))

    sign_normalized = eigvalsh(-correction, -fixed)
    direct_generalized = np.linalg.eigvals(np.linalg.solve(fixed, correction))
    generalized_error = float(
        np.linalg.norm(
            np.sort(sign_normalized)
            - np.sort(np.real_if_close(direct_generalized).real)
        )
    )
    return {
        "all_pass": bool(
            identity_error < 2.0e-14
            and np.max(fixed_eigenvalues) < -1.0e-3
            and generalized_error < 2.0e-13
        ),
        "identity_error": identity_error,
        "fixed_max_eigenvalue": float(np.max(fixed_eigenvalues)),
        "generalized_error": generalized_error,
        "ratio": float(np.max(np.abs(sign_normalized))),
    }


def metric_gauge_lift_control() -> dict[str, float | int | bool]:
    """Check the rank-five affine fiber and gauge inclusion independently."""
    maximum_factorization_error = 0.0
    maximum_target_error = 0.0
    maximum_gauge_error = 0.0
    fixture_count = 0
    for period in (5, 7, 9, 11):
        for axis in range(4):
            for harmonic in (1, 2):
                momentum = np.zeros(4)
                momentum[axis] = 2.0 * np.pi * harmonic / period
                metric = fixture.regge.metric_map(momentum)
                gauge = fixture.regge.gauge_map(momentum)
                transform = np.linalg.lstsq(metric, gauge, rcond=None)[0]
                factorization_error = float(
                    np.linalg.norm(metric @ transform - gauge)
                    / max(np.linalg.norm(gauge), 1.0e-30)
                )
                conserved = null_space(transform.conj().T)
                target = conserved[:, 0]
                base = metric @ np.linalg.solve(metric.conj().T @ metric, target)
                fiber = null_space(metric.conj().T)
                shifted = base + (1.0 + 2.0j) * fiber[:, 0]
                target_error = float(np.linalg.norm(metric.conj().T @ shifted - target))
                gauge_error = float(np.linalg.norm(gauge.conj().T @ shifted))
                maximum_factorization_error = max(
                    maximum_factorization_error, factorization_error
                )
                maximum_target_error = max(maximum_target_error, target_error)
                maximum_gauge_error = max(maximum_gauge_error, gauge_error)
                fixture_count += 1
                if np.linalg.matrix_rank(metric) != 10 or fiber.shape[1] != 5:
                    return {
                        "all_pass": False,
                        "fixtures": fixture_count,
                        "maximum_factorization_error": maximum_factorization_error,
                        "maximum_target_error": maximum_target_error,
                        "maximum_gauge_error": maximum_gauge_error,
                    }
    return {
        "all_pass": bool(
            maximum_factorization_error < 2.0e-12
            and maximum_target_error < 2.0e-12
            and maximum_gauge_error < 2.0e-12
        ),
        "fixtures": fixture_count,
        "maximum_factorization_error": maximum_factorization_error,
        "maximum_target_error": maximum_target_error,
        "maximum_gauge_error": maximum_gauge_error,
    }


def raw_fourier_encoder(period: int, harmonic: int) -> np.ndarray:
    phase = np.exp(2j * np.pi * harmonic * np.arange(period) / period)
    scale = np.sqrt(2.0 / period)
    encoder = np.zeros((15 * period, 30))
    for edge in range(15):
        encoder[edge::15, edge] = scale * phase.real
        encoder[edge::15, 15 + edge] = -scale * phase.imag
    return encoder


def metric_realification(period: int, harmonic: int, axis: int) -> np.ndarray:
    momentum = np.zeros(4)
    momentum[axis] = 2.0 * np.pi * harmonic / period
    metric = fixture.regge.metric_map(momentum)
    return np.block([[metric.real, -metric.imag], [metric.imag, metric.real]])


def refinement_control() -> dict[str, float | int | bool]:
    maximum_raw_error = 0.0
    minimum_gram_deviation = float("inf")
    minimum_encoder_defect = float("inf")
    count = 0
    for axis in (0, 1):
        for harmonic in (1, 2):
            for coarse, fine in zip((5, 7, 9), (7, 9, 11)):
                coarse_fourier = raw_fourier_encoder(coarse, harmonic)
                fine_fourier = raw_fourier_encoder(fine, harmonic)
                injection = fine_fourier @ coarse_fourier.T
                transported = injection @ coarse_fourier
                raw_error = float(
                    np.linalg.norm(transported.T @ transported - np.eye(30))
                )
                coarse_metric = metric_realification(coarse, harmonic, axis)
                fine_metric = metric_realification(fine, harmonic, axis)
                gram_values = eigvalsh(
                    fine_metric.T @ fine_metric,
                    coarse_metric.T @ coarse_metric,
                )
                gram_deviation = float(np.max(np.abs(gram_values - 1.0)))
                coarse_encoder = coarse_fourier @ coarse_metric
                fine_encoder = fine_fourier @ fine_metric
                encoder_defect = float(
                    np.linalg.norm(injection @ coarse_encoder - fine_encoder)
                    / np.linalg.norm(fine_encoder)
                )
                maximum_raw_error = max(maximum_raw_error, raw_error)
                minimum_gram_deviation = min(
                    minimum_gram_deviation, gram_deviation
                )
                minimum_encoder_defect = min(
                    minimum_encoder_defect, encoder_defect
                )
                count += 1
    return {
        "all_pass": bool(
            maximum_raw_error < 5.0e-12
            and minimum_gram_deviation > 1.0e-2
            and minimum_encoder_defect > 5.0e-2
        ),
        "comparisons": count,
        "maximum_raw_error": maximum_raw_error,
        "minimum_gram_deviation": minimum_gram_deviation,
        "minimum_encoder_defect": minimum_encoder_defect,
    }


def algebra_certificate() -> dict[str, object]:
    schur = negative_fixed_schur_control()
    lift = metric_gauge_lift_control()
    refinement = refinement_control()
    return {
        "all_pass": bool(
            schur["all_pass"] and lift["all_pass"] and refinement["all_pass"]
        ),
        "negative_fixed_schur": schur,
        "metric_gauge_lift": lift,
        "refinement": refinement,
    }


def primary_claims(cache: str) -> dict[str, object]:
    matches = re.findall(r"^CLAIMS_JSON: (\{.*\})$", cache, flags=re.MULTILINE)
    if len(matches) != 1:
        raise ValueError("primary cache must contain exactly one CLAIMS_JSON line")
    return json.loads(matches[0])


def main() -> int:
    checks = Checks()
    certificate = algebra_certificate()
    cache = (ROOT / PRIMARY_CACHE).read_text()
    note = " ".join((ROOT / NOTE).read_text().lower().split())
    claims = primary_claims(cache)

    checks.check(
        "literal-input-closure",
        all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS),
        f"inputs={len(AUDIT_INPUT_PATHS)}",
    )
    schur = certificate["negative_fixed_schur"]
    checks.check(
        "independent-negative-fixed-schur",
        schur["all_pass"],
        f"identity={schur['identity_error']:.2e}; generalized={schur['generalized_error']:.2e}",
    )
    lift = certificate["metric_gauge_lift"]
    checks.check(
        "shared-definition-affine-lift-fiber",
        lift["all_pass"],
        f"fixtures={lift['fixtures']}; target={lift['maximum_target_error']:.2e}; gauge={lift['maximum_gauge_error']:.2e}",
    )
    refinement = certificate["refinement"]
    checks.check(
        "shared-definition-raw-versus-metric-refinement",
        refinement["all_pass"],
        f"comparisons={refinement['comparisons']}; raw={refinement['maximum_raw_error']:.2e}; metric={refinement['minimum_encoder_defect']:.2e}",
    )
    primary_bound = (
        "TOTAL: PASS=8 FAIL=0" in cache
        and claims.get("claim_type") == "bounded_theorem"
        and claims.get("lift_fibers") == 12
        and claims.get("response_pairs") == 48
        and claims.get("physical_law_selected") is False
        and claims.get("audit_status") == "unset"
        and "distinct open obligations that may interact" in note
        and "no audit has run" in note
    )
    checks.check(
        "primary-cache-and-scope-binding",
        primary_bound,
        "primary=8/0; bounded finite scope; physical/audit authority absent",
    )
    print("CHECKER_JSON: " + json.dumps({
        "claim_type": "bounded_theorem",
        "negative_fixed_schur": bool(schur["all_pass"]),
        "metric_gauge_fixtures": int(lift["fixtures"]),
        "refinement_comparisons": int(refinement["comparisons"]),
        "physical_law_selected": False,
        "audit_status": "unset",
    }, sort_keys=True))
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return int(checks.failed != 0)


if __name__ == "__main__":
    raise SystemExit(main())
