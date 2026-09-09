#!/usr/bin/env python3
"""Join the source-pinned off-axis ladder to the static Maxwell target.

This runner performs no stochastic evolution. It parses the complete
four-family covariance receipt, tests one common infrared q-squared
coefficient against independent family coefficients and U K, and subjects the
result to mass, q-eighth, low-volume, and body-diagonal influence controls.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

import numpy as np
import sympy as sp

from spin_half_cubic_ice_quadratic_gauge_kernel_uniqueness_2026_09_04 import (
    quadratic_kernel_certificate,
)


AUDIT_INPUT_PATHS = (
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "scripts/spin_half_cubic_ice_quadratic_gauge_kernel_uniqueness_2026_09_04.py",
    "scripts/spin_half_cubic_ice_finite_delta_charge_coulomb_join_2026_09_03.py",
    "logs/runner-cache/spin_half_cubic_ice_finite_delta_charge_coulomb_join_2026_09_03.txt",
    "scripts/spin_half_cubic_ice_finite_delta_magnetic_twist_2026_09_04.py",
    "logs/runner-cache/spin_half_cubic_ice_finite_delta_magnetic_twist_2026_09_04.txt",
    "scripts/spin_half_cubic_ice_off_axis_maxwell_isotropy_2026_09_04.py",
    "logs/runner-cache/spin_half_cubic_ice_off_axis_maxwell_isotropy_2026_09_04.txt",
)

AUDIT_TIMEOUT_SEC = 300
REPO_ROOT = Path(__file__).resolve().parent.parent
LENGTHS = (8, 10, 12, 14)
FAMILIES = ("axis", "face_out", "face_in", "body")


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, condition: bool, label: str) -> None:
        if condition:
            self.passed += 1
            print(f"[PASS] {self.passed + self.failed:02d} {label}")
        else:
            self.failed += 1
            print(f"[FAIL] {self.passed + self.failed:02d} {label}")


@dataclass(frozen=True)
class ParsedRow:
    coupling: float
    length: int
    gaps: np.ndarray
    q_squared: np.ndarray
    covariance: np.ndarray


@dataclass(frozen=True)
class GLSFit:
    coefficients: np.ndarray
    coefficient_errors: np.ndarray
    coefficient_covariance: np.ndarray
    chi_squared: float
    observation_rank: int
    design_rank: int


def parse_ladder_cache() -> dict[tuple[float, int], ParsedRow]:
    cache_path = (
        REPO_ROOT
        / "logs/runner-cache/spin_half_cubic_ice_off_axis_maxwell_isotropy_2026_09_04.txt"
    )
    text = cache_path.read_text(encoding="utf-8")
    required = (
        "runner: scripts/spin_half_cubic_ice_off_axis_maxwell_isotropy_2026_09_04.py",
        "status: ok",
        "exit_code: 0",
        "TOTAL: PASS=5 FAIL=0",
    )
    if any(token not in text for token in required):
        raise RuntimeError("off-axis ladder cache is incomplete or unclean")
    row_pattern = re.compile(
        r"^OFF_AXIS_GAPS V=(?P<coupling>0\.95|1\.00) "
        r"L=(?P<length>\d+) values=(?P<values>.+)$",
        re.MULTILINE,
    )
    value_pattern = re.compile(
        r"(?P<family>[a-z_]+):(?P<q2>[0-9.]+):(?P<gap>[0-9.]+)"
    )
    covariance_pattern = re.compile(
        r"^OFF_AXIS_COVARIANCE V=(?P<coupling>0\.95|1\.00) "
        r"L=(?P<length>\d+) row_major=(?P<values>[-+0-9.eE,]+)$",
        re.MULTILINE,
    )
    raw_rows: dict[tuple[float, int], dict[str, tuple[float, float]]] = {}
    for match in row_pattern.finditer(text):
        key = (float(match.group("coupling")), int(match.group("length")))
        if key in raw_rows:
            raise RuntimeError(f"duplicate off-axis row: {key}")
        family_rows = {}
        for value in value_pattern.finditer(match.group("values")):
            family = value.group("family")
            if family not in FAMILIES or family in family_rows:
                raise RuntimeError(f"invalid off-axis family: {key}, {family}")
            family_rows[family] = (
                float(value.group("q2")),
                float(value.group("gap")),
            )
        raw_rows[key] = family_rows
    covariances = {}
    for match in covariance_pattern.finditer(text):
        key = (float(match.group("coupling")), int(match.group("length")))
        values = np.asarray(
            [float(value) for value in match.group("values").split(",")]
        )
        if len(values) != len(FAMILIES) ** 2 or key in covariances:
            raise RuntimeError(f"malformed off-axis covariance: {key}")
        covariances[key] = values.reshape((len(FAMILIES), len(FAMILIES)))
    expected = {
        (coupling, length)
        for coupling in (0.95, 1.0)
        for length in LENGTHS
    }
    if set(raw_rows) != expected or set(covariances) != expected:
        raise RuntimeError("off-axis cache has the wrong coupling/volume matrix")
    parsed = {}
    for key in sorted(expected):
        if tuple(raw_rows[key]) != FAMILIES:
            raise RuntimeError(f"off-axis family order or coverage changed: {key}")
        parsed[key] = ParsedRow(
            coupling=key[0],
            length=key[1],
            q_squared=np.asarray(
                [raw_rows[key][family][0] for family in FAMILIES]
            ),
            gaps=np.asarray(
                [raw_rows[key][family][1] for family in FAMILIES]
            ),
            covariance=covariances[key],
        )
    return parsed


def parse_static_maxwell_target() -> tuple[float, float]:
    """Derive U K and its propagated error from the two parent receipts."""

    charge_text = (
        REPO_ROOT
        / "logs/runner-cache/spin_half_cubic_ice_finite_delta_charge_coulomb_join_2026_09_03.txt"
    ).read_text(encoding="utf-8")
    magnetic_text = (
        REPO_ROOT
        / "logs/runner-cache/spin_half_cubic_ice_finite_delta_magnetic_twist_2026_09_04.txt"
    ).read_text(encoding="utf-8")
    charge_match = re.search(
        r"^AXIAL_FIT V=0\.95 U_charge=[0-9.]+\+/-"
        r"(?P<error>[0-9.]+) U_flux=(?P<value>[0-9.]+) ",
        charge_text,
        re.MULTILINE,
    )
    magnetic_match = re.search(
        r"^SUMMARY V=0\.95 K=(?P<value>[0-9.]+)\+/-"
        r"(?P<error>[0-9.]+) ",
        magnetic_text,
        re.MULTILINE,
    )
    if charge_match is None or magnetic_match is None:
        raise RuntimeError("static Maxwell parent receipts are incomplete")
    electric_stiffness = float(charge_match.group("value"))
    electric_stiffness_error = float(charge_match.group("error"))
    magnetic_stiffness = float(magnetic_match.group("value"))
    magnetic_stiffness_error = float(magnetic_match.group("error"))
    return (
        electric_stiffness * magnetic_stiffness,
        float(
            np.hypot(
                electric_stiffness * magnetic_stiffness_error,
                magnetic_stiffness * electric_stiffness_error,
            )
        ),
    )


def excess_row(
    detuned: ParsedRow,
    rk: ParsedRow,
) -> tuple[np.ndarray, np.ndarray]:
    if detuned.length != rk.length or not np.allclose(
        detuned.q_squared, rk.q_squared
    ):
        raise AssertionError("detuned and RK rows are unmatched")
    values = detuned.gaps**2 - rk.gaps**2
    detuned_jacobian = np.diag(2.0 * detuned.gaps)
    rk_jacobian = np.diag(2.0 * rk.gaps)
    covariance = (
        detuned_jacobian @ detuned.covariance @ detuned_jacobian
        + rk_jacobian @ rk.covariance @ rk_jacobian
    )
    return values, covariance


def select_dataset(
    rows: dict[tuple[float, int], ParsedRow],
    *,
    lengths: tuple[int, ...] = LENGTHS,
    families: tuple[str, ...] = FAMILIES,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    family_indices = [FAMILIES.index(family) for family in families]
    values = []
    q_squared = []
    labels = []
    blocks = []
    for length in lengths:
        row_values, row_covariance = excess_row(
            rows[(0.95, length)], rows[(1.0, length)]
        )
        values.extend(row_values[family_indices])
        q_squared.extend(rows[(0.95, length)].q_squared[family_indices])
        labels.extend(range(len(families)))
        blocks.append(row_covariance[np.ix_(family_indices, family_indices)])
    covariance = np.zeros((len(values), len(values)), dtype=float)
    offset = 0
    for block in blocks:
        width = len(block)
        covariance[offset : offset + width, offset : offset + width] = block
        offset += width
    return (
        np.asarray(values),
        covariance,
        np.asarray(q_squared),
        np.asarray(labels),
    )


def gls_fit(
    values: np.ndarray,
    covariance: np.ndarray,
    design: np.ndarray,
) -> GLSFit:
    inverse_covariance = np.linalg.pinv(
        covariance, rcond=1.0e-10, hermitian=True
    )
    normal = design.T @ inverse_covariance @ design
    coefficient_covariance = np.linalg.inv(normal)
    coefficients = coefficient_covariance @ (
        design.T @ inverse_covariance @ values
    )
    residual = values - design @ coefficients
    return GLSFit(
        coefficients=coefficients,
        coefficient_errors=np.sqrt(np.diag(coefficient_covariance)),
        coefficient_covariance=coefficient_covariance,
        chi_squared=float(residual @ inverse_covariance @ residual),
        observation_rank=int(np.linalg.matrix_rank(covariance, tol=1.0e-14)),
        design_rank=int(np.linalg.matrix_rank(design, tol=1.0e-12)),
    )


def independent_design(
    q_squared: np.ndarray,
    labels: np.ndarray,
    family_count: int,
) -> np.ndarray:
    matrix = np.zeros((len(q_squared), 3 * family_count))
    for row, (q2, family) in enumerate(zip(q_squared, labels, strict=True)):
        matrix[row, 3 * family : 3 * family + 3] = (q2, q2**2, q2**3)
    return matrix


def common_design(
    q_squared: np.ndarray,
    labels: np.ndarray,
    family_count: int,
    *,
    correction_order: int = 3,
    include_mass: bool = False,
) -> np.ndarray:
    leading_columns = 2 if include_mass else 1
    correction_count = correction_order - 1
    matrix = np.zeros(
        (len(q_squared), leading_columns + correction_count * family_count)
    )
    for row, (q2, family) in enumerate(zip(q_squared, labels, strict=True)):
        offset = 0
        if include_mass:
            matrix[row, 0] = 1.0
            matrix[row, 1] = q2
            offset = 2
        else:
            matrix[row, 0] = q2
            offset = 1
        for correction in range(2, correction_order + 1):
            matrix[
                row,
                offset + correction_count * family + correction - 2,
            ] = q2**correction
    return matrix


def common_fit_for_selection(
    rows: dict[tuple[float, int], ParsedRow],
    *,
    lengths: tuple[int, ...] = LENGTHS,
    families: tuple[str, ...] = FAMILIES,
) -> GLSFit:
    values, covariance, q_squared, labels = select_dataset(
        rows, lengths=lengths, families=families
    )
    return gls_fit(
        values,
        covariance,
        common_design(q_squared, labels, len(families)),
    )


def main() -> int:
    checks = Checks()
    kernel_certificate = quadratic_kernel_certificate()
    q0, q1, q2 = sp.symbols("q0:3")
    expected_maxwell_kernel = sp.Matrix(
        (
            (q1**2 + q2**2, -q0 * q1, -q0 * q2),
            (-q0 * q1, q0**2 + q2**2, -q1 * q2),
            (-q0 * q2, -q1 * q2, q0**2 + q1**2),
        )
    )
    checks.check(
        kernel_certificate.rotation_count == 24
        and kernel_certificate.cubic_only_dimension == 3
        and kernel_certificate.transverse_only_dimension == 6
        and kernel_certificate.joint_dimension == 1
        and kernel_certificate.normalized_kernel == expected_maxwell_kernel,
        "proper cubic covariance and gauge transversality uniquely force the quadratic Maxwell kernel",
    )
    rows = parse_ladder_cache()
    checks.check(
        len(rows) == 8
        and all(np.all(np.isfinite(row.gaps)) for row in rows.values()),
        "the source-pinned cache supplies all eight finite gap vectors",
    )
    checks.check(
        all(
            np.all(np.isfinite(row.covariance))
            and np.allclose(row.covariance, row.covariance.T, atol=1.0e-14)
            and np.min(np.linalg.eigvalsh(row.covariance)) > 0.0
            and np.linalg.matrix_rank(row.covariance, tol=1.0e-14)
            == len(FAMILIES)
            for row in rows.values()
        ),
        "every parsed four-family covariance is symmetric, positive definite, and full rank",
    )
    maximum_block_condition = max(
        np.linalg.cond(row.covariance) for row in rows.values()
    )
    checks.check(
        maximum_block_condition < 1.0e8,
        "every covariance block remains below the declared conditioning ceiling",
    )
    values, covariance, q_squared, labels = select_dataset(rows)
    independent = gls_fit(
        values,
        covariance,
        independent_design(q_squared, labels, len(FAMILIES)),
    )
    common = gls_fit(
        values,
        covariance,
        common_design(q_squared, labels, len(FAMILIES)),
    )
    diagonal_common = gls_fit(
        values,
        np.diag(np.diag(covariance)),
        common_design(q_squared, labels, len(FAMILIES)),
    )
    mass = gls_fit(
        values,
        covariance,
        common_design(
            q_squared, labels, len(FAMILIES), include_mass=True
        ),
    )
    q8 = gls_fit(
        values,
        covariance,
        common_design(
            q_squared, labels, len(FAMILIES), correction_order=4
        ),
    )

    maxwell_c_squared, maxwell_c_squared_error = (
        parse_static_maxwell_target()
    )
    primary_compatibility = abs(
        common.coefficients[0] - maxwell_c_squared
    ) / np.hypot(common.coefficient_errors[0], maxwell_c_squared_error)
    fixed_covariance = covariance + maxwell_c_squared_error**2 * np.outer(
        q_squared, q_squared
    )
    fixed = gls_fit(
        values - maxwell_c_squared * q_squared,
        fixed_covariance,
        common_design(q_squared, labels, len(FAMILIES))[:, 1:],
    )
    independent_c2 = independent.coefficients[::3]
    independent_c2_errors = independent.coefficient_errors[::3]
    face_variance = (
        independent.coefficient_covariance[3, 3]
        + independent.coefficient_covariance[6, 6]
        - 2.0 * independent.coefficient_covariance[3, 6]
    )
    face_difference_sigma = abs(independent_c2[1] - independent_c2[2]) / np.sqrt(
        max(face_variance, 1.0e-20)
    )
    l10plus = common_fit_for_selection(rows, lengths=(10, 12, 14))
    without_body = common_fit_for_selection(
        rows, families=("axis", "face_out", "face_in")
    )
    l10plus_compatibility = abs(
        l10plus.coefficients[0] - common.coefficients[0]
    ) / np.hypot(l10plus.coefficient_errors[0], common.coefficient_errors[0])
    without_body_compatibility = abs(
        without_body.coefficients[0] - common.coefficients[0]
    ) / np.hypot(
        without_body.coefficient_errors[0], common.coefficient_errors[0]
    )
    diagonal_compatibility = abs(
        diagonal_common.coefficients[0] - common.coefficients[0]
    ) / np.hypot(
        diagonal_common.coefficient_errors[0],
        common.coefficient_errors[0],
    )

    checks.check(
        common.coefficients[0] > 2.0 * common.coefficient_errors[0],
        "the covariance-aware common off-axis q-squared coefficient is positive at two errors",
    )
    checks.check(
        primary_compatibility < 2.0,
        "the common dynamical coefficient is compatible with independent U K",
    )
    checks.check(
        common.chi_squared - independent.chi_squared < 7.815,
        "four independent leading coefficients do not cross the nominal three-parameter improvement threshold",
    )
    checks.check(
        fixed.chi_squared < 15.507,
        "fixed U K with its common uncertainty passes the nominal five-percent eight-dof threshold",
    )
    checks.check(
        face_difference_sigma < 2.0,
        "face-diagonal in-plane and out-of-plane leading coefficients are compatible",
    )
    checks.check(
        abs(mass.coefficients[0]) < 2.0 * mass.coefficient_errors[0]
        and common.chi_squared - mass.chi_squared < 3.841,
        "a common mass term is unresolved and does not significantly improve the fit",
    )
    checks.check(
        common.chi_squared - q8.chi_squared < 9.488
        and abs(q8.coefficients[0] - common.coefficients[0])
        < 2.0
        * np.hypot(q8.coefficient_errors[0], common.coefficient_errors[0]),
        "family q-eighth terms do not significantly improve or destabilize the leading coefficient",
    )
    checks.check(
        l10plus_compatibility < 2.0 and without_body_compatibility < 2.0,
        "the common coefficient survives removal of L=8 and of the body-diagonal family",
    )
    checks.check(
        diagonal_compatibility < 2.0,
        "dropping within-volume off-diagonal covariances leaves the leading coefficient compatible",
    )

    print(
        "QUADRATIC_KERNEL",
        f"proper_rotations={kernel_certificate.rotation_count}",
        f"cubic_only_dimension={kernel_certificate.cubic_only_dimension}",
        f"transverse_only_dimension={kernel_certificate.transverse_only_dimension}",
        f"joint_dimension={kernel_certificate.joint_dimension}",
        "basis=q2_delta_minus_qiqj",
    )
    print(
        "ISOTROPY_JOIN",
        f"common_c2={common.coefficients[0]:.8f}"
        f"+/-{common.coefficient_errors[0]:.8f}",
        f"UK={maxwell_c_squared:.8f}+/-{maxwell_c_squared_error:.8f}",
        f"compatibility_sigma={primary_compatibility:.4f}",
        f"common_chi2={common.chi_squared:.4f}",
        f"independent_chi2={independent.chi_squared:.4f}",
        f"common_delta_chi2={common.chi_squared - independent.chi_squared:.4f}",
        f"fixed_target_chi2={fixed.chi_squared:.4f}",
    )
    print(
        "DIRECTION_COEFFICIENTS",
        " ".join(
            f"{family}={independent_c2[index]:.8f}"
            f"+/-{independent_c2_errors[index]:.8f}"
            for index, family in enumerate(FAMILIES)
        ),
        f"face_difference_sigma={face_difference_sigma:.4f}",
    )
    print(
        "MODEL_CONTROLS",
        f"mass2={mass.coefficients[0]:.8f}"
        f"+/-{mass.coefficient_errors[0]:.8f}",
        f"mass_delta_chi2={common.chi_squared - mass.chi_squared:.4f}",
        f"q8_c2={q8.coefficients[0]:.8f}"
        f"+/-{q8.coefficient_errors[0]:.8f}",
        f"q8_delta_chi2={common.chi_squared - q8.chi_squared:.4f}",
    )
    print(
        "INFLUENCE_CONTROLS",
        f"L10plus_c2={l10plus.coefficients[0]:.8f}"
        f"+/-{l10plus.coefficient_errors[0]:.8f}",
        f"L10plus_difference_sigma={l10plus_compatibility:.4f}",
        f"without_body_c2={without_body.coefficients[0]:.8f}"
        f"+/-{without_body.coefficient_errors[0]:.8f}",
        f"without_body_difference_sigma={without_body_compatibility:.4f}",
        f"diagonal_c2={diagonal_common.coefficients[0]:.8f}"
        f"+/-{diagonal_common.coefficient_errors[0]:.8f}",
        f"diagonal_difference_sigma={diagonal_compatibility:.4f}",
    )
    print(
        "COVARIANCE",
        f"observation_rank={common.observation_rank}",
        f"common_design_rank={common.design_rank}",
        f"independent_design_rank={independent.design_rank}",
        f"max_block_condition={maximum_block_condition:.4e}",
    )
    print(
        "CERTIFICATE: complete_cubic_orbits=True outer_population_covariance=True "
        "family_q4_q6=True mass_control=True q8_control=True "
        "static_target_source_pinned=True "
        "finite_volume=True thermodynamic_limit=False"
    )
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
