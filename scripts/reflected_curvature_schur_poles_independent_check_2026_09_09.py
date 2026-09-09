#!/usr/bin/env python3
"""Independent finite checks for the corrected PR #7338 Schur-pole claim.

This companion uses a complete QR complement rather than the primary's SVD
``null_space`` construction and computes temporal quotient moments directly.
It shares the declared source-only action fixture; it is independent evidence
for the two finite consequences, not an independent source for that action.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re
import sys

import numpy as np
from scipy.optimize import brentq


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import reflected_curvature_schur_poles_finite_fixture_2026_09_09 as finite  # noqa: E402

NOTE_REL = "docs/ADMISSIBILITY_REFLECTED_CURVATURE_CANONICAL_REDUCTION_SCHUR_POLE_TT_SPECTRAL_WEIGHT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-23.md"
PRIMARY_REL = "scripts/admissibility_reflected_curvature_canonical_reduction_schur_pole_tt_spectral_weight_boundary_2026_08_23.py"
PRIMARY_CACHE_REL = "logs/runner-cache/admissibility_reflected_curvature_canonical_reduction_schur_pole_tt_spectral_weight_boundary_2026_08_23.txt"
FIXTURE_REL = "scripts/reflected_curvature_schur_poles_finite_fixture_2026_09_09.py"
REGGE_REL = "scripts/frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09.py"
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_REFLECTED_CURVATURE_CANONICAL_REDUCTION_SCHUR_POLE_TT_SPECTRAL_WEIGHT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-23.md",
    "scripts/admissibility_reflected_curvature_canonical_reduction_schur_pole_tt_spectral_weight_boundary_2026_08_23.py",
    "logs/runner-cache/admissibility_reflected_curvature_canonical_reduction_schur_pole_tt_spectral_weight_boundary_2026_08_23.txt",
    "scripts/reflected_curvature_schur_poles_finite_fixture_2026_09_09.py",
    "scripts/frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09.py",
)
AUDIT_TIMEOUT_SEC = 30


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, key: str, statement: str, condition: bool, detail: str = "") -> None:
        ok = bool(condition)
        print(f"[{'PASS' if ok else 'FAIL'}] {key}: {statement}")
        if detail:
            print(f"       {detail}")
        self.passed += int(ok)
        self.failed += int(not ok)


def flat(path: Path) -> str:
    return " ".join(path.read_text(encoding="utf-8").lower().split())


def source_closure_certificate(module=finite) -> bool:
    """Cheap import-time contract used by the primary source gate."""
    required = (
        "build_reflection_union",
        "centered_curvature_intertwiner",
        "cross_action_symbol",
        "hankel_minimum",
        "local_tt_observables",
        "metric_coefficients",
        "union_gauge_map",
        "union_line_metric_map",
        "union_symbol",
    )
    return (
        all(callable(getattr(module, name, None)) for name in required)
        and module.MU == 1.0 / 1024.0
        and len(module.ORIGINAL_DIRECTIONS) == 15
        and module.SHIFTS.ndim == 2
        and module.MATRICES.shape[0] == module.SHIFTS.shape[0]
        and len(module.EXTRACTION_PROVENANCE) == 6
    )


def independent_action(union, momentum: np.ndarray) -> np.ndarray:
    q = np.asarray(momentum, dtype=complex)
    curvature = finite.centered_curvature_intertwiner(union, q)
    penalty = finite.centered_curvature_intertwiner(union, -q).T @ curvature
    return finite.union_symbol(union, q) + finite.MU * penalty


def independent_metric_map(union, momentum: np.ndarray) -> np.ndarray:
    directions = np.asarray(union.directions, dtype=float)
    half_phase = directions @ np.asarray(momentum, dtype=complex) / 2.0
    factors = np.ones(len(directions), dtype=complex)
    nonzero = np.abs(half_phase) >= 1.0e-13
    factors[nonzero] = (
        np.exp(1j * half_phase[nonzero])
        * np.sin(half_phase[nonzero])
        / half_phase[nonzero]
    )
    return factors[:, None] * finite.metric_coefficients(directions)


def qr_complement(matrix: np.ndarray) -> np.ndarray:
    return np.linalg.qr(matrix, mode="complete")[0][:, matrix.shape[1] :]


def section_certificate(union) -> dict[str, dict[str, object]]:
    fixed = qr_complement(independent_metric_map(union, np.zeros(4)))
    output: dict[str, dict[str, object]] = {}
    cases = (
        ("moving", True, (-2.0, 0.0, 1.0, 0.0), 9),
        ("fixed", False, (-4.0, -4.0, 1.0, 0.0), 10),
    )
    for name, moving, endpoint, eigenvalue_index in cases:
        start = np.asarray((0.4, 0.0, 0.0, 0.0))
        stop = np.asarray(endpoint) * (2.0 * np.pi / 9.0)

        def matrices(parameter: float):
            momentum = (1.0 - parameter) * start + parameter * stop
            metric = independent_metric_map(union, momentum)
            complement = qr_complement(metric) if moving else fixed
            operator = independent_action(union, momentum)
            vertical = complement.conj().T @ operator @ complement
            vertical = 0.5 * (vertical + vertical.conj().T)
            return momentum, metric, complement, operator, vertical

        def eigenvalue(parameter: float) -> float:
            return float(np.linalg.eigvalsh(matrices(parameter)[-1])[eigenvalue_index])

        parameter = brentq(eigenvalue, 0.0, 1.0, xtol=1.0e-14)
        momentum, metric, complement, operator, vertical = matrices(parameter)
        values, vectors = np.linalg.eigh(vertical)
        slot = int(np.argmin(np.abs(values)))
        null_vector = vectors[:, slot]
        mixing = float(
            np.linalg.norm(
                null_vector.conj() @ complement.conj().T @ operator @ metric
            )
        )
        singular = np.linalg.svd(operator, compute_uv=False)
        ward = float(
            np.linalg.norm(operator @ finite.union_gauge_map(union, momentum))
        )
        output[name] = {
            "parameter": float(parameter),
            "momentum": [float(value) for value in momentum],
            "vertical_zero": float(values[slot]),
            "mixing": mixing,
            "full_rank": int(np.sum(singular > 1.0e-9)),
            "ward": ward,
        }
    return output


def temporal_certificate(union) -> dict[str, object]:
    directions = np.asarray(union.directions)
    index = {tuple(direction): slot for slot, direction in enumerate(directions)}
    observable = np.zeros(len(directions))
    observable[index[(0, 1, 0, 0)]] = 1.0
    observable[index[(0, 0, 1, 0)]] = -1.0
    results = {}
    for samples in (256, 512):
        frequencies = np.arange(samples) * (2.0 * np.pi / samples)
        covariance = []
        for frequency in frequencies:
            momentum = np.asarray((np.pi / 2.0, 0.0, 0.0, frequency))
            operator = -independent_action(union, momentum)
            gauge = finite.union_gauge_map(union, momentum)
            quotient = qr_complement(gauge)
            projected = quotient.conj().T @ observable
            reduced = quotient.conj().T @ operator @ quotient
            covariance.append(
                float(np.real(projected.conj() @ np.linalg.solve(reduced, projected)))
            )
        values = np.asarray(covariance)
        moments = np.asarray(
            [np.mean(values * np.cos(index * frequencies)) for index in range(13)]
        )
        one_step = np.asarray(
            [[moments[left + right + 1] for right in range(2)] for left in range(2)]
        )
        two_step = np.asarray(
            [[moments[2 * (left + right)] for right in range(3)] for left in range(3)]
        )
        results[str(samples)] = {
            "moments": [float(value) for value in moments],
            "one_step_minimum": float(np.linalg.eigvalsh(one_step)[0]),
            "two_step_minimum": float(np.linalg.eigvalsh(two_step)[0]),
        }

    positive_moments = 0.581884812 * 0.266171727 ** np.arange(13)
    positive_minima = []
    for step, order, shift in ((1, 2, 1), (2, 3, 0)):
        hankel = np.asarray(
            [
                [
                    positive_moments[step * (left + right + shift)]
                    for right in range(order)
                ]
                for left in range(order)
            ]
        )
        positive_minima.append(float(np.linalg.eigvalsh(hankel)[0]))
    return {"samples": results, "positive_control_minima": positive_minima}


def primary_cache_certificate() -> dict[str, object]:
    primary = ROOT / PRIMARY_REL
    cache = ROOT / PRIMARY_CACHE_REL
    body = cache.read_text(encoding="utf-8")
    runner_match = re.search(r"^runner:\s*(.+)$", body, re.MULTILINE)
    sha_match = re.search(r"^runner_sha256:\s*([0-9a-f]{64})$", body, re.MULTILINE)
    status_match = re.search(r"^status:\s*(\S+)$", body, re.MULTILINE)
    claims_lines = [line for line in body.splitlines() if line.startswith("CLAIMS_JSON: ")]
    claims = json.loads(claims_lines[0].split(": ", 1)[1]) if len(claims_lines) == 1 else {}
    return {
        "runner": runner_match.group(1) if runner_match else None,
        "runner_sha_matches": bool(
            sha_match
            and sha_match.group(1) == hashlib.sha256(primary.read_bytes()).hexdigest()
        ),
        "status": status_match.group(1) if status_match else None,
        "total_present": "TOTAL: PASS=8 FAIL=0" in body,
        "claims": claims,
    }


def main() -> int:
    checks = Checks()
    union = finite.build_reflection_union()
    sections = section_certificate(union)
    temporal = temporal_certificate(union)
    cache = primary_cache_certificate()
    note = flat(ROOT / NOTE_REL)

    sections_ok = all(
        item["mixing"] > 1.0e-3
        and item["full_rank"] == 18
        and abs(item["vertical_zero"]) < 1.0e-10
        and item["ward"] < 1.0e-10
        for item in sections.values()
    )
    checks.check(
        "independent-qr-section-poles",
        "a complete-QR construction reproduces two metric-coupled vertical poles",
        sections_ok,
        json.dumps(sections, sort_keys=True),
    )

    sample_data = temporal["samples"]
    temporal_ok = all(
        item["one_step_minimum"] < -1.0e-13
        and item["two_step_minimum"] < -1.0e-8
        for item in sample_data.values()
    )
    checks.check(
        "independent-full-quotient-hankel",
        "direct 256- and 512-mode quotient moments violate both raw Hankel tests",
        temporal_ok,
        json.dumps(
            {
                key: (value["one_step_minimum"], value["two_step_minimum"])
                for key, value in sample_data.items()
            },
            sort_keys=True,
        ),
    )

    checks.check(
        "positive-dominant-root-control",
        "the isolated positive dominant branch is positive semidefinite",
        min(temporal["positive_control_minima"]) > -1.0e-14,
        repr(temporal["positive_control_minima"]),
    )

    claims = cache["claims"]
    cache_ok = (
        cache["runner"] == PRIMARY_REL
        and cache["runner_sha_matches"]
        and cache["status"] == "ok"
        and cache["total_present"]
        and claims.get("tested_stationary_charts") == 2
        and claims.get("finite_nonzero_roots") == 14
        and claims.get("tt_coupled_inside_roots") == 3
        and claims.get("atlas_exhausted") is False
        and claims.get("audit_status") == "unset"
    )
    checks.check(
        "source-bound-primary-interface",
        "the fresh primary cache exposes the declared finite claim interface",
        cache_ok,
        json.dumps(cache, sort_keys=True),
    )

    scope_ok = (
        source_closure_certificate()
        and "two separately chosen charts" in note
        and "no exhaustive atlas theorem" in note
        and "no formal audit has run" in note
        and "no physical gravity law" in note
    )
    checks.check(
        "bounded-scope-and-source-closure",
        "the companion shares only the disclosed fixture and preserves the open physical scope",
        scope_ok,
    )

    summary = {
        "tested_stationary_charts": 2,
        "temporal_sample_counts": [256, 512],
        "positive_dominant_root_control": True,
        "shared_action_fixture": True,
        "physical_gravity_selected": False,
        "audit_status": "unset",
    }
    print("CHECKER_JSON: " + json.dumps(summary, sort_keys=True))
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return int(checks.failed != 0)


if __name__ == "__main__":
    raise SystemExit(main())
