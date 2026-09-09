#!/usr/bin/env python3
"""Artifact integrity and covariance operations for historical ice receipts.

A valid artifact is not evidence that its producer is correct or current.
All long production and physical Maxwell identifications remain held.
"""
from __future__ import annotations

from dataclasses import dataclass
import hashlib
import json
from pathlib import Path
import re

import numpy as np

ROOT = Path(__file__).resolve().parent.parent
INDEX_PATH = "data/field/spin_half_cubic_ice_successor_historical_receipts_2026_09_09.json"
AUDIT_INPUT_PATHS = (
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/docs/NO_GO_DISCIPLINE_CHECKLIST_SPIN_HALF_INFRARED_FORWARD_REPLAY_2026-09-05.md',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/docs/SPIN_HALF_CUBIC_ICE_CUBIC_GAUGE_QUADRATIC_MAXWELL_KERNEL_UNIQUENESS_BOUNDED_THEOREM_NOTE_2026-09-04.md',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/docs/SPIN_HALF_CUBIC_ICE_FINITE_DETUNING_CHARGE_COULOMB_FLUX_STIFFNESS_JOIN_BOUNDED_THEOREM_NOTE_2026-09-03.md',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/docs/SPIN_HALF_CUBIC_ICE_FINITE_DETUNING_RELAXED_MAGNETIC_TWIST_STIFFNESS_BOUNDED_THEOREM_NOTE_2026-09-04.md',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/docs/SPIN_HALF_CUBIC_ICE_FINITE_DETUNING_TRANSVERSE_LINEAR_SPECTRAL_CROSSOVER_BOUNDED_THEOREM_NOTE_2026-09-03.md',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/docs/SPIN_HALF_CUBIC_ICE_FORWARD_LENGTH_CONVERGENCE_BOUNDED_THEOREM_NOTE_2026-09-04.md',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/docs/SPIN_HALF_CUBIC_ICE_INFRARED_FORWARD_REPLAY_RECOVERY_BOUNDARY_NOTE_2026-09-05.md',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/docs/SPIN_HALF_CUBIC_ICE_INFRARED_MAXWELL_JOIN_HEALTH_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-09-04.md',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/docs/SPIN_HALF_CUBIC_ICE_LATE_TIME_HIGHER_GRADIENT_MAXWELL_JOIN_LOCALIZATION_BOUNDED_THEOREM_NOTE_2026-09-04.md',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/docs/SPIN_HALF_CUBIC_ICE_OFF_AXIS_MAXWELL_HIGH_MOMENTUM_LOCALIZATION_BOUNDED_THEOREM_NOTE_2026-09-04.md',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_finite_delta_charge_coulomb_join_2026_09_03.txt',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_finite_delta_magnetic_twist_2026_09_04.txt',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_finite_delta_transverse_pole_2026_09_03.txt',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_forward_length_convergence_join_2026_09_04.txt',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_forward_length_finite_sample_reanalysis_2026_09_04.txt',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_forward_length_high_stat_extension_2026_09_04.txt',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_forward_length_high_stat_join_2026_09_04.txt',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_forward_length_ladder_2026_09_04.txt',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_infrared_forward_replay_2026_09_04.txt',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_infrared_forward_replay_join_2026_09_04.txt',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_infrared_ladder_2026_09_04.txt',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_infrared_maxwell_failure_localization_2026_09_04.txt',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_infrared_maxwell_health_reanalysis_2026_09_04.txt',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_infrared_maxwell_join_2026_09_04.txt',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_late_time_maxwell_join_2026_09_04.txt',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_off_axis_cubic_orbit_scout_2026_09_04.txt',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_off_axis_high_q_localization_2026_09_04.txt',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_off_axis_maxwell_isotropy_2026_09_04.txt',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_off_axis_maxwell_isotropy_join_2026_09_04.txt',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_off_axis_staggered_orbit_scout_2026_09_04.txt',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_off_axis_transverse_scout_2026_09_04.txt',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_quadratic_gauge_kernel_uniqueness_2026_09_04.txt',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_finite_delta_charge_coulomb_join_2026_09_03.py',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_finite_delta_magnetic_twist_2026_09_04.py',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_finite_delta_transverse_pole_2026_09_03.py',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_forward_length_convergence_join_2026_09_04.py',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_forward_length_finite_sample_reanalysis_2026_09_04.py',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_forward_length_high_stat_extension_2026_09_04.py',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_forward_length_high_stat_join_2026_09_04.py',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_forward_length_ladder_2026_09_04.py',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_infrared_forward_replay_2026_09_04.py',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_infrared_forward_replay_join_2026_09_04.py',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_infrared_ladder_2026_09_04.py',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_infrared_maxwell_failure_localization_2026_09_04.py',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_infrared_maxwell_health_reanalysis_2026_09_04.py',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_infrared_maxwell_join_2026_09_04.py',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_late_time_maxwell_join_2026_09_04.py',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_off_axis_cubic_orbit_scout_2026_09_04.py',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_off_axis_high_q_localization_2026_09_04.py',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_off_axis_maxwell_isotropy_2026_09_04.py',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_off_axis_maxwell_isotropy_join_2026_09_04.py',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_off_axis_staggered_orbit_scout_2026_09_04.py',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_off_axis_transverse_scout_2026_09_04.py',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_quadratic_gauge_kernel_uniqueness_2026_09_04.py',
    'data/field/spin_half_cubic_ice_successor_historical_receipts_2026_09_09.json',
    'docs/MINIMAL_AXIOMS_2026-06-29.md',
)
AUDIT_TIMEOUT_SEC = 150


@dataclass(frozen=True)
class HistoricalReceipt:
    header: dict[str, str]
    stdout: str
    stderr: str
    total: tuple[int, int] | None
    checks: tuple[tuple[str, int, str], ...]
    production_accepted: bool = False

    @property
    def recorded_green(self) -> bool:
        # This property describes the original header, never current physics.
        return (self.header["status"] == "ok" and self.header["exit_code"] == "0"
                and self.total is not None and self.total[1] == 0
                and float(self.header["elapsed_sec"]) <= float(self.header["timeout_sec"]))


def check_inputs(root: Path, expected: dict[str, str]) -> None:
    for name, digest in expected.items():
        path = root / name
        if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != digest:
            raise RuntimeError(f"current source/input identity mismatch: {name}")


def parse_receipt(text: str) -> HistoricalReceipt:
    """Parse exactly one cache envelope. Recovery annotations are data only."""
    if text.count("===== runner cache v1 =====") != 1 or not text.startswith("===== runner cache v1 =====\n"):
        raise ValueError("expected one historical cache header")
    if text.count("----- stdout -----\n") != 1 or text.count("----- stderr -----\n") != 1:
        raise ValueError("expected one stdout/stderr boundary")
    head, rest = text.split("----- stdout -----\n", 1)
    stdout, stderr = rest.split("----- stderr -----\n", 1)
    header = {}
    for line in head.splitlines()[1:]:
        if not line:
            continue
        key, sep, value = line.partition(": ")
        if not sep or key in header:
            raise ValueError("duplicate or malformed header")
        header[key] = value
    expected_keys = {"runner", "runner_sha256", "input_fingerprint_sha256", "timeout_sec", "exit_code", "elapsed_sec", "status"}
    if set(header) != expected_keys:
        raise ValueError("incomplete or extra historical header fields")
    for key in ("runner_sha256", "input_fingerprint_sha256"):
        if re.fullmatch(r"[0-9a-f]{64}", header[key]) is None:
            raise ValueError("malformed historical source identity")
    if (not np.isfinite(float(header["elapsed_sec"])) or float(header["elapsed_sec"]) < 0
            or float(header["timeout_sec"]) <= 0):
        raise ValueError("invalid historical timing")
    if header["status"] not in ("ok", "nonzero_exit") or (header["status"] == "ok") != (header["exit_code"] == "0"):
        raise ValueError("contradictory historical status/exit")
    for line in (stdout + stderr).splitlines():
        if any(line.startswith(key + ":") for key in expected_keys):
            raise ValueError("header field repeated inside payload")
    checks = []
    for line in stdout.splitlines():
        if line.startswith(("[PASS]", "[FAIL]")):
            match = re.fullmatch(r"\[(PASS|FAIL)\] (\d+) (.+)", line)
            if match is None:
                raise ValueError("malformed historical check")
            checks.append((match[1], int(match[2]), match[3]))
    if [row[1] for row in checks] != list(range(1, len(checks) + 1)):
        raise ValueError("duplicate or missing historical check IDs")
    totals = [line for line in stdout.splitlines() if line.startswith("TOTAL:")]
    if len(totals) > 1:
        raise ValueError("multiple historical totals")
    total = None
    if totals:
        match = re.fullmatch(r"TOTAL: PASS=(\d+) FAIL=(\d+)", totals[0])
        if match is None:
            raise ValueError("malformed historical total")
        total = (int(match[1]), int(match[2]))
        if total != (sum(c[0] == "PASS" for c in checks), sum(c[0] == "FAIL" for c in checks)):
            raise ValueError("historical total/check mismatch")
        if (total[1] == 0) != (header["status"] == "ok"):
            raise ValueError("historical total/status mismatch")
    elif header["status"] == "ok" or checks or "Traceback (most recent call last):" not in stdout + stderr:
        raise ValueError("missing historical total without recorded execution failure")
    return HistoricalReceipt(header, stdout, stderr, total, tuple(checks))


def load_receipt(name: str, *, require_green: bool = False) -> HistoricalReceipt:
    check_inputs(ROOT, AUDIT_EXPECTED_SHA256)
    index = json.loads((ROOT / INDEX_PATH).read_text())
    row = index["receipts"].get(name)
    if row is None:
        raise ValueError("undeclared historical receipt")
    data = (ROOT / row["archive_path"]).read_bytes()
    if hashlib.sha256(data).hexdigest() != row["sha256"]:
        raise ValueError("historical receipt payload identity mismatch")
    source = (ROOT / row["producer_archive"]).read_bytes()
    if hashlib.sha256(source).hexdigest() != row["producer_source_sha256"]:
        raise ValueError("historical producer archive identity mismatch")
    receipt = parse_receipt(data.decode())
    if receipt.header != row["header"] or receipt.total != (tuple(row["total"]) if row["total"] is not None else None):
        raise ValueError("historical envelope/fixture identity mismatch")
    if receipt.header["runner_sha256"] != row["producer_source_sha256"]:
        raise ValueError("historical producer source pin mismatch")
    if require_green and not receipt.recorded_green:
        raise ValueError("historical producer did not record a green bounded execution")
    return receipt


def historical_text(name: str, *, require_green: bool = False) -> str:
    """Return authenticated original text for the existing numerical parser."""
    load_receipt(name, require_green=require_green)
    row = json.loads((ROOT / INDEX_PATH).read_text())["receipts"][name]
    return (ROOT / row["archive_path"]).read_text()


def validate_covariance(covariance, errors=None, *, positive_definite=False):
    matrix = np.asarray(covariance, dtype=float)
    if matrix.ndim != 2 or matrix.shape[0] != matrix.shape[1] or not np.all(np.isfinite(matrix)):
        raise ValueError("covariance must be finite and square")
    scale = max(float(np.max(np.abs(matrix))), 1e-20)
    tolerance = max(1e-18, scale * 1e-11)  # .12e printed covariance and roundoff
    if not np.allclose(matrix, matrix.T, rtol=0, atol=tolerance):
        raise ValueError("covariance is not symmetric")
    eigenvalues = np.linalg.eigvalsh((matrix + matrix.T) / 2)
    if eigenvalues[0] < -tolerance or (positive_definite and eigenvalues[0] <= tolerance):
        raise ValueError("covariance is not positive on the required space")
    if errors is not None:
        errors = np.asarray(errors, dtype=float)
        if errors.shape != (len(matrix),) or not np.all(np.isfinite(errors)) or np.any(errors < 0):
            raise ValueError("invalid reported uncertainties")
        # Errors were printed to eight decimal places, covariance to .12e.
        rounding = 2 * np.abs(errors) * 5.0001e-9 + (5.0001e-9)**2 + tolerance
        if np.any(np.abs(np.diag(matrix) - errors**2) > rounding):
            raise ValueError("reported error/covariance estimator mismatch")
    return matrix


def shared_zero_covariance(errors, radii, zero_error: float, volume: int):
    """Independent continued-energy runs, independent of their shared zero run.

    The supplied marginal errors already include the zero-source variance.
    Other cross-correlations require a different full covariance, not this helper.
    """
    errors = np.asarray(errors, float); radii = np.asarray(radii, float)
    if (errors.shape != radii.shape or not np.all(np.isfinite(errors))
            or not np.all(np.isfinite(radii)) or not np.isfinite(zero_error)
            or np.any(errors < 0) or np.any(radii <= 0) or zero_error < 0 or volume <= 0):
        raise ValueError("invalid symmetric-source covariance inputs")
    zero_coefficients = 2 / (radii**2 * volume)
    common = np.outer(zero_coefficients, zero_coefficients) * zero_error**2
    if np.any(errors**2 < np.diag(common) - 1e-14):
        raise ValueError("marginal error omits its declared zero-source variance")
    matrix = np.diag(errors**2) + common - np.diag(np.diag(common))
    return validate_covariance(matrix, positive_definite=True)


def gls_mean(values, covariance):
    values = np.asarray(values, float)
    covariance = validate_covariance(covariance, positive_definite=True)
    if values.shape != (len(covariance),) or not np.all(np.isfinite(values)):
        raise ValueError("invalid GLS observations")
    one = np.ones(len(values)); solved = np.linalg.solve(covariance, one)
    weights = solved / (one @ solved)
    return float(weights @ values), float(np.sqrt(1 / (one @ solved)))


def historical_target() -> dict:
    """Keep the old central arithmetic, explicitly without a physical target/SE."""
    charge = load_receipt("spin_half_cubic_ice_finite_delta_charge_coulomb_join_2026_09_03.txt")
    magnetic = load_receipt("spin_half_cubic_ice_finite_delta_magnetic_twist_2026_09_04.txt")
    c = re.findall(r"^AXIAL_FIT V=0\.95 U_charge=([0-9.]+)\+/-([0-9.]+) U_flux=([0-9.]+) ", charge.stdout, re.M)
    m = re.findall(r"^SUMMARY V=0\.95 K=([0-9.]+)\+/-([0-9.]+) ", magnetic.stdout, re.M)
    if len(c) != 1 or len(m) != 1:
        raise ValueError("missing or duplicate historical static rows")
    u_charge, se_charge, u_flux = map(float, c[0]); k, old_se = map(float, m[0])
    return {"U_charge": u_charge, "U_charge_reported_error": se_charge,
            "U_flux": u_flux, "U_flux_error": None,
            "occupation_sign_response": k, "response_error": None,
            "historical_response_reported_error": old_se,
            "central_product": u_flux * k, "product_error": None,
            "physical_Maxwell_target": False,
            "reason": "U_flux has no matched uncertainty here; magnetic summary omits shared-zero covariance and its producer has the disclosed sampling bug"}


def held_production() -> int:
    print("EVIDENCE HOLD: no current long production receipt; authorize and bound a corrected production protocol separately.")
    return 2


def parse_ladder_payload(text: str, lengths, windows):
    """Complete unique coupling/volume/window rows; no invented health fields."""
    rows = {}
    pattern = re.compile(r"ROW_DONE V=(0\.95|1\.00) L=(\d+) gaps=(\S+)")
    item_pattern = re.compile(r"(\d+)-(\d+):([0-9.]+)\+/-([0-9.]+)")
    for line in text.splitlines():
        if not line.startswith("ROW_DONE"):
            continue
        match = pattern.fullmatch(line)
        if match is None:
            raise ValueError("malformed ladder row")
        items = match[3].split(',')
        if len(items) != len(windows):
            raise ValueError("missing or extra ladder window")
        seen = []
        for item in items:
            field = item_pattern.fullmatch(item)
            if field is None:
                raise ValueError("malformed ladder estimate")
            window = (int(field[1]), int(field[2])); seen.append(window)
            key = (float(match[1]), int(match[2]), window)
            if key in rows:
                raise ValueError("duplicate ladder estimate")
            gap, error = float(field[3]), float(field[4])
            if not np.isfinite(gap + error) or gap <= 0 or error <= 0:
                raise ValueError("invalid ladder estimate")
            rows[key] = (gap, error)
        if tuple(seen) != tuple(windows):
            raise ValueError("unexpected ladder window order")
    expected = {(v,l,w) for v in (0.95,1.0) for l in lengths for w in windows}
    if set(rows) != expected:
        raise ValueError("incomplete or extra ladder fixture")
    return rows


def parse_paired_payload(text: str):
    forwards = (6,12,20); windows = ((2,6),(8,14)); rows = {}
    pattern = re.compile(r"PAIRED_ROW V=(0\.95|1\.00) L=(16|18) window=(2-6|8-14) gaps=(\S+) cov=(\S+)")
    item_pattern = re.compile(r"(6|12|20):([0-9.]+)\+/-([0-9.]+)")
    for line in text.splitlines():
        if not line.startswith('PAIRED_ROW'):
            continue
        match = pattern.fullmatch(line)
        if match is None:
            raise ValueError("malformed paired row")
        items = match[4].split(','); parsed = [item_pattern.fullmatch(x) for x in items]
        if len(parsed) != 3 or any(x is None for x in parsed) or tuple(int(x[1]) for x in parsed) != forwards:
            raise ValueError("duplicate, reordered or incomplete endpoints")
        key = (float(match[1]),int(match[2]),tuple(map(int,match[3].split('-'))))
        if key in rows:
            raise ValueError("duplicate paired row")
        gaps = np.array([float(x[2]) for x in parsed]); errors = np.array([float(x[3]) for x in parsed])
        values = np.array([float(x) for x in match[5].split(',')])
        if values.size != 9 or np.any(gaps <= 0) or not np.all(np.isfinite(gaps)):
            raise ValueError("invalid paired data shape or values")
        covariance = values.reshape(3,3); validate_covariance(covariance,errors)
        rows[key] = (gaps,errors,covariance)
    if set(rows) != {(v,l,w) for v in (0.95,1.0) for l in (16,18) for w in windows}:
        raise ValueError("incomplete paired fixture")
    return rows


def paired_control(gaps, errors, covariance):
    validate_covariance(covariance,errors)
    contrast = np.array([[-1.,1.,0.],[-1.,0.,1.]])
    differences = contrast @ gaps; contrasts = contrast @ covariance @ contrast.T
    validate_covariance(contrasts,positive_definite=True)
    return (float(differences @ np.linalg.solve(contrasts,differences)),
            float(np.max(np.abs(differences)/np.sqrt(np.diag(contrasts)))),
            float(np.ptp(gaps)/np.mean(gaps)))


def charge_health(records) -> bool:
    return bool(records) and all(r.count_consistent and r.charge_consistent
        and r.minimum_effective_population_fraction > .90 and (r.length < 4 or r.final_unique_fraction > .25) for r in records)


def spectral_health(records, *, tau: int = 6, origin_floor: float = 10, forward_floor: float = 16) -> bool:
    # Distinct ancestry labels are a finite health statistic, not independent samples.
    return bool(records) and all(r.count_consistent and r.sector_consistent
        and r.minimum_effective_population_fraction > .85
        and r.population * r.origin_diversity_fractions[tau] >= origin_floor
        and r.population * r.forward_survival_fractions[0] >= forward_floor for r in records)



# Current source/input identity: literal finite closure.
AUDIT_EXPECTED_SHA256 = {
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/docs/NO_GO_DISCIPLINE_CHECKLIST_SPIN_HALF_INFRARED_FORWARD_REPLAY_2026-09-05.md': 'd005e28ff0cba15f5e5b27580055c2ae51958dfeb967c3603df0d01d8bd4526b',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/docs/SPIN_HALF_CUBIC_ICE_CUBIC_GAUGE_QUADRATIC_MAXWELL_KERNEL_UNIQUENESS_BOUNDED_THEOREM_NOTE_2026-09-04.md': 'd9c836c854ee20dddf399d51d7bab6b13f9164a920a10ed2c0713cd6b4f150e4',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/docs/SPIN_HALF_CUBIC_ICE_FINITE_DETUNING_CHARGE_COULOMB_FLUX_STIFFNESS_JOIN_BOUNDED_THEOREM_NOTE_2026-09-03.md': '1f6811e0f9a872c2a23946dbf313a32c378ca697f658423e0c13dcad708e0ff9',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/docs/SPIN_HALF_CUBIC_ICE_FINITE_DETUNING_RELAXED_MAGNETIC_TWIST_STIFFNESS_BOUNDED_THEOREM_NOTE_2026-09-04.md': '73d66f716fdfacc5c6d02f902b2021392e5139041b6018985d2886264a5007ed',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/docs/SPIN_HALF_CUBIC_ICE_FINITE_DETUNING_TRANSVERSE_LINEAR_SPECTRAL_CROSSOVER_BOUNDED_THEOREM_NOTE_2026-09-03.md': '862311719f14a9ba1ee6fc660477fd01510631a87db636f9098a626d5291316d',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/docs/SPIN_HALF_CUBIC_ICE_FORWARD_LENGTH_CONVERGENCE_BOUNDED_THEOREM_NOTE_2026-09-04.md': '9b2aba542ed2f36643ce4b511b1f85db9b96a0a5b3570e5f306e561b6b8b246e',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/docs/SPIN_HALF_CUBIC_ICE_INFRARED_FORWARD_REPLAY_RECOVERY_BOUNDARY_NOTE_2026-09-05.md': '1d22ab5c1f16784462b68ddf4021b7e14a110a6ca7be6cff92ffd279f9011715',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/docs/SPIN_HALF_CUBIC_ICE_INFRARED_MAXWELL_JOIN_HEALTH_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-09-04.md': '139bd99c4f1f9c86bf8f222cb6986957d8f24bfca335a5f3c0ea1654a5a4abbd',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/docs/SPIN_HALF_CUBIC_ICE_LATE_TIME_HIGHER_GRADIENT_MAXWELL_JOIN_LOCALIZATION_BOUNDED_THEOREM_NOTE_2026-09-04.md': '8a3369b50204369ddfd0311704cf71423a91c5c87df51a6e41dae4657b0ab947',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/docs/SPIN_HALF_CUBIC_ICE_OFF_AXIS_MAXWELL_HIGH_MOMENTUM_LOCALIZATION_BOUNDED_THEOREM_NOTE_2026-09-04.md': 'c47db40a423d54580b0e27ba844e302c0e9d5cb1105705fb1b5392f21ac00e36',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_finite_delta_charge_coulomb_join_2026_09_03.txt': '992136071fbd1f87efbae5daec0689ce7309913ccc12fd294bdfc39a54ae569f',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_finite_delta_magnetic_twist_2026_09_04.txt': '2e483ff3d5bc34e7fdde41b8ab06790be1ea487a167bb10b33936e35ff22c894',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_finite_delta_transverse_pole_2026_09_03.txt': '97687c182b2c0a8f095bea6ddc90018e2580163af81757e1bbeaf2650c04fde7',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_forward_length_convergence_join_2026_09_04.txt': '366e0cfbca4cc582cc28c34c2e822990b5a1216d42513417677e818584cd4fea',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_forward_length_finite_sample_reanalysis_2026_09_04.txt': 'db3f966552fb31bab95a3d487220dd0622b21b5da127515f197e7e441ad68445',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_forward_length_high_stat_extension_2026_09_04.txt': '484c30b66ccbe992290da328e785c22f597dfc698173044c4cec178d3fbaf8b6',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_forward_length_high_stat_join_2026_09_04.txt': '8ec096ed4b50bf92ee7d709470833d9355b8461c9e9c35e5579d1fec4402ed17',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_forward_length_ladder_2026_09_04.txt': 'd6ffe038be4e0a5dc6824965dbdcc24595aac7ba2241ef0ca059310ffeabd59e',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_infrared_forward_replay_2026_09_04.txt': '849646d782df0c360fd1d180b4d966b3499979b43d1c709b11b5c1e43c2a92e0',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_infrared_forward_replay_join_2026_09_04.txt': '5131098b985eab3d4991a5c767c1f057ba047ff694b5d074383037a27f65622c',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_infrared_ladder_2026_09_04.txt': '09f1e590b9cf2cade315bca1a854156a42faba262d22b55f21167bad7a6b798c',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_infrared_maxwell_failure_localization_2026_09_04.txt': '88552107e8ce428aec277c61645322a927b209b3a3936ec4471e3344b4d50a35',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_infrared_maxwell_health_reanalysis_2026_09_04.txt': 'e6e00baa0a8bcb38afdd7cf1e46e09e0c8f5b6ba4422bc2fdcb45fac72a6a92c',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_infrared_maxwell_join_2026_09_04.txt': '2c2dec102b9758f4249818ed2ce935a0c582a5a3c3fead19d91b12aadb8b51af',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_late_time_maxwell_join_2026_09_04.txt': '17345ac4bd2839c8d0cd315fdc0d5c6126e3b8879f1b3f49bd055c637d0ec481',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_off_axis_cubic_orbit_scout_2026_09_04.txt': 'acdfb65d3e785f08ba61b6958461db6154fcd2771e1d309834d00ece3ca48992',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_off_axis_high_q_localization_2026_09_04.txt': '82e2ad2b36cc44b9a367a16554a52dc5a68c94690a571d642f37e9ececcb5216',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_off_axis_maxwell_isotropy_2026_09_04.txt': '6ec74acaacd3909cd39b0520c0bc93e690ca949c54119a60e84a89d55a7ea1d0',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_off_axis_maxwell_isotropy_join_2026_09_04.txt': '7d7cfba76fe8a0de63de2ecd2b2a6241d7401e3904258a45969d30ae76b3f728',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_off_axis_staggered_orbit_scout_2026_09_04.txt': 'c77aab04384741c1bca11852b0554742db0b8c157545bded3c1b09735b3b42dc',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_off_axis_transverse_scout_2026_09_04.txt': '5eda05ddbf46d54e600839ecd30f552d3362e3704071037e38c0632dc2f86e81',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_quadratic_gauge_kernel_uniqueness_2026_09_04.txt': 'f28a3a727508e6c2df4a4f1e77d0d0bcfdb77a5d41a282f13219d9ef4a4aa202',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_finite_delta_charge_coulomb_join_2026_09_03.py': '97881c8721ee3177aeaa610a59f139ef44be809b49bc9c6ed9f0490fe6b10418',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_finite_delta_magnetic_twist_2026_09_04.py': 'a61b5ca89ea5b39ac932744b12e3af46167d81fd4ed5eb52acdb08644f74b28b',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_finite_delta_transverse_pole_2026_09_03.py': '5bb190ef328d095d83eacf927e2c3964499f178e6f41254368047957a893227d',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_forward_length_convergence_join_2026_09_04.py': 'aaa07511fdd1650fe317bd8fe03e4826beaa7f7cf5659c475b7b53e4a6b30733',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_forward_length_finite_sample_reanalysis_2026_09_04.py': '421cd0399b35947d90f208ddab78b38b2caf7e7cd5f593613ff53af300aaf434',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_forward_length_high_stat_extension_2026_09_04.py': '75461521b7bd0d3806e3a0598c4c82603f7127623762990d478784ad2ef542b1',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_forward_length_high_stat_join_2026_09_04.py': '1aa54dbb1b298ee8064603b89e97470d541900d7affb61bf329f269908a2ceca',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_forward_length_ladder_2026_09_04.py': '7ac21e04324b48c9215524d1e889693ee329a5fe0e3495d1a8c14832249bd953',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_infrared_forward_replay_2026_09_04.py': '8d87b4c4ffc219e7557cf0ad19213842738f8f8a2879493612e3740fd19d26da',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_infrared_forward_replay_join_2026_09_04.py': 'b0556cf80af1a4515ca1a134c435dd40c011f0dfb058acd743c2948522e12af8',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_infrared_ladder_2026_09_04.py': '80108851a3d3a77e8e2593502abfa17ee72eab7174ad7043f039afe2e5133867',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_infrared_maxwell_failure_localization_2026_09_04.py': '756173baab1c9966bf8c2cdd03860f7736710e17edb7b453fe9e69bf2e328dfb',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_infrared_maxwell_health_reanalysis_2026_09_04.py': '9b4fbd65bc089f160e90fef8d2e95b3eaaedb276fd582c9b4697ed393abd0eae',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_infrared_maxwell_join_2026_09_04.py': 'fdb9e0d0de5d10282c782cd888a9e3823c76a9c2a253887e76ae8a686de8da1f',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_late_time_maxwell_join_2026_09_04.py': '8cea10e54e91b643a39d2a757eb120ee992197defdf45dce4cac98e36d5197cd',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_off_axis_cubic_orbit_scout_2026_09_04.py': 'e93ddc34b6bdbca4e17a89aa1d1f2ebef140c8717138d9aa429c8911751dc189',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_off_axis_high_q_localization_2026_09_04.py': '8be752a7b03f7db990958e4813c7e029e85e06736a7cc6644db712452ceddf96',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_off_axis_maxwell_isotropy_2026_09_04.py': '6057a37e1415b3dce55c85923514ec481f6cb007921d2ed634c8237be18b7655',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_off_axis_maxwell_isotropy_join_2026_09_04.py': 'fef6248c3b90c88c1038af037cd152b8e3d33577dcc31286328bdffe6cdfa0ec',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_off_axis_staggered_orbit_scout_2026_09_04.py': 'ae6390773d562d8ffe37bae981cc64246e0cbebb817eff88b6383ca376e7eeac',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_off_axis_transverse_scout_2026_09_04.py': '477ca4a1af788464bb798ffa0bc5c2f42fd3c3c3591d22fd075b80e24cb82a4e',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_quadratic_gauge_kernel_uniqueness_2026_09_04.py': 'f621e2b2d00bf85525dae4a1a3f103dd156cb9ba837c5f8f4d5199282ae5c2cb',
    'data/field/spin_half_cubic_ice_successor_historical_receipts_2026_09_09.json': 'c1c7a1cdd92236409d829be9a8dad7700b169e6e8bc3f5d94e28fa34c25653a7',
    'docs/MINIMAL_AXIOMS_2026-06-29.md': '93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753',
}
