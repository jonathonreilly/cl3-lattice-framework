#!/usr/bin/env python3
"""Finite carrier and fixed-frame protocol for corrected Eta Block-06."""
from __future__ import annotations

from itertools import product
from pathlib import Path
import sympy as sp

import independent_admissibility_d4_ordered_h1_front_carrier_interface_2026_08_29 as _packet_helper  # noqa: F401,E501

ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs/ADMISSIBILITY_D4_ORDERED_H1_FRONT_CARRIER_INTERFACE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md"
AUDIT_TIMEOUT_SEC = 30
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_D4_ORDERED_H1_FRONT_CARRIER_INTERFACE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md",
    "scripts/independent_admissibility_d4_ordered_h1_front_carrier_interface_2026_08_29.py",
)
I = sp.I
I2, I4, I8, I32 = sp.eye(2), sp.eye(4), sp.eye(8), sp.eye(32)
X = sp.Matrix(((0, 1), (1, 0)))
Y = sp.Matrix(((0, -I), (I, 0)))
Z = sp.diag(1, -1)
DELTA = (sp.diag(X, X), sp.diag(Y, -Y), sp.diag(Z, Z))
D = tuple(sp.kronecker_product(I8, d) for d in DELTA)
SHELL = ((-1, 0, 0), (1, 0, 0), (0, -1, 0),
         (0, 1, 0), (0, 0, -1), (0, 0, 1))


def equal(a: sp.MatrixBase, b: sp.MatrixBase) -> bool:
    return all(sp.simplify(x) == 0 for x in (a - b))


def root(direction: sp.MatrixBase, outcome: int, u: sp.Expr) -> sp.Matrix:
    ident = sp.eye(direction.rows)
    sign = 1 if outcome == 0 else -1
    same = (ident + sign * direction) / 2
    other = (ident - sign * direction) / 2
    return sp.sqrt((1 + u) / 2) * same + sp.sqrt((1 - u) / 2) * other


def cylinders(u: sp.Expr) -> tuple[sp.Expr, ...]:
    rho = I4 / 4
    out = []
    for b, c in product((0, 1), repeat=2):
        first = root(DELTA[1], b, u)
        second_direction = DELTA[1] if b == 0 else DELTA[0]
        second = root(second_direction, c, u)
        out.append(sp.simplify(sp.trace(second * first * rho * first.H * second.H)))
    return tuple(out)


def reset_cylinders(u: sp.Expr) -> tuple[sp.Expr, ...]:
    """Joint probabilities when the carrier is reset to I4/4 after event one."""
    rho = I4 / 4
    out = []
    for b, c in product((0, 1), repeat=2):
        first = root(DELTA[1], b, u)
        first_probability = sp.simplify(sp.trace(first * rho * first.H))
        second_direction = DELTA[1] if b == 0 else DELTA[0]
        second = root(second_direction, c, u)
        reset_probability = sp.simplify(sp.trace(second * rho * second.H))
        out.append(sp.simplify(first_probability * reset_probability))
    return tuple(out)


def branch_effect(direction: sp.MatrixBase, outcome: int, u: sp.Expr) -> sp.Matrix:
    k = root(direction, outcome, u)
    return sp.simplify(k.H * k)


def rotate(v: tuple[int, int, int], r: sp.MatrixBase) -> tuple[int, int, int]:
    answer = r * sp.Matrix(v)
    return tuple(int(answer[i]) for i in range(3))


def rotate_mask(mask: int, r: sp.MatrixBase) -> int:
    result = 0
    for i, direction in enumerate(SHELL):
        result |= ((mask >> i) & 1) << SHELL.index(rotate(direction, r))
    return result


def generated_rotation_group(*generators: sp.MatrixBase) -> set[tuple[int, ...]]:
    identity = tuple(int(x) for x in sp.eye(3))
    seen = {identity}
    frontier = [sp.eye(3)]
    while frontier:
        current = frontier.pop()
        for generator in generators:
            candidate = current * generator
            key = tuple(int(x) for x in candidate)
            if key not in seen:
                seen.add(key)
                frontier.append(candidate)
    return seen


def main() -> int:
    chi4 = sp.simplify(I * DELTA[0] * DELTA[1] * DELTA[2])
    chi32 = sp.kronecker_product(I8, chi4)
    projectors = ((I32 - chi32) / 2, (I32 + chi32) / 2)
    units: dict[tuple[int, int, int], sp.MatrixBase] = {}
    for sector in (-1, 1):
        p = (I4 + sector * chi4) / 2
        units[(sector, 0, 0)] = sp.simplify(p * (I4 + DELTA[2]) / 2)
        units[(sector, 1, 1)] = sp.simplify(p * (I4 - DELTA[2]) / 2)
        units[(sector, 0, 1)] = sp.simplify(
            p * (DELTA[0] - I * sector * DELTA[1]) / 2
        )
        units[(sector, 1, 0)] = sp.simplify(
            p * (DELTA[0] + I * sector * DELTA[1]) / 2
        )
    matrix_units = all(
        equal(
            units[(s, a, b)] * units[(t, c, d)],
            units[(s, a, d)] if s == t and b == c else sp.zeros(4),
        )
        for s, t, a, b, c, d in product((-1, 1), (-1, 1), (0, 1),
                                         (0, 1), (0, 1), (0, 1))
    ) and all(equal(units[(s, a, b)].H, units[(s, b, a)])
              for s, a, b in product((-1, 1), (0, 1), (0, 1)))
    words = (I4, DELTA[0], DELTA[1], DELTA[2],
             DELTA[0] * DELTA[1], DELTA[0] * DELTA[2],
             DELTA[1] * DELTA[2], DELTA[0] * DELTA[1] * DELTA[2])
    word_rank = sp.Matrix.hstack(*(sp.Matrix(w).reshape(16, 1) for w in words)).rank()

    kraus = []
    for m in range(8):
        k = sp.zeros(4, 32)
        k[:, 4*m:4*m+4] = I4
        kraus.append(k)
    complete = equal(sum((k.H * k for k in kraus), sp.zeros(32)), I32)
    intertwines = all(equal(k * d32, d4 * k)
                     for k in kraus for d32, d4 in zip(D, DELTA))

    uz = (I2 - I*Z) / sp.sqrt(2)
    uc = (I2 - I*(X + Y + Z)) / 2
    rz = sp.Matrix(((0, -1, 0), (1, 0, 0), (0, 0, 1)))
    rc = sp.Matrix(((0, 0, 1), (1, 0, 0), (0, 1, 0)))
    carrier_covariance = True
    for q, r in ((uz, rz), (uc, rc)):
        v = sp.diag(q, q.conjugate())
        u32 = sp.kronecker_product(I8, v)
        generator_transport = all(
            equal(v * DELTA[i] * v.H,
                  sum((r[j, i] * DELTA[j] for j in range(3)), sp.zeros(4)))
            for i in range(3)
        )
        carrier_covariance &= generator_transport and all(
            equal(k * u32, v * k) for k in kraus
        )
    rotation_group_size = len(generated_rotation_group(rz, rc))

    sharp = cylinders(sp.Integer(1))
    half = cylinders(sp.Rational(1, 2))
    expected_sharp = (sp.Rational(1, 2), 0, sp.Rational(1, 4), sp.Rational(1, 4))
    expected_half = (sp.Rational(5, 16), sp.Rational(3, 16),
                     sp.Rational(1, 4), sp.Rational(1, 4))

    x0, x1 = (0, 0, 0), (-1, -1, 0)
    shell0 = {tuple(x0[i] + d[i] for i in range(3)) for d in SHELL}
    shell1 = {tuple(x1[i] + d[i] for i in range(3)) for d in SHELL}
    fixed_geometry = shell0 & shell1 == {(-1, 0, 0), (0, -1, 0)}

    rotation = sp.Matrix(((0, 0, 1), (0, -1, 0), (1, 0, 0)))
    pure_mask = rotate_mask(17, rotation)
    rotated_detector = rotation * sp.Matrix((0, 1, 0))
    pure_branch = branch_effect(DELTA[1], 0, sp.Integer(1))
    transported_branch = branch_effect(-DELTA[1], 0, sp.Integer(1))
    covariance_residual = sp.simplify(pure_branch - transported_branch)
    covariance_residual_rank = covariance_residual.rank()

    bad = list(kraus)
    bad[0] = 2 * bad[0]
    bad_complete = equal(sum((k.H * k for k in bad), sp.zeros(32)), I32)
    reset_history = reset_cylinders(sp.Integer(1))
    fault_controls = (not bad_complete
                      and reset_history == (sp.Rational(1, 4),) * 4
                      and reset_history != sharp
                      and covariance_residual_rank == 4)

    note = " ".join(NOTE.read_text(encoding="utf-8").split())
    checks = (
        ("A_two_sector_algebra", [p.rank() for p in projectors] == [16, 16]
         and word_rank == 8 and matrix_units,
         "central ranks are 16+16 and explicit matrix units give M2 direct-sum M2"),
        ("B_cptp_multiplicity_trace", complete and intertwines,
         "eight explicit C32-to-C4 Kraus selectors are complete and intertwine all three generators"),
        ("C_carrier_covariance", carrier_covariance and rotation_group_size == 24,
         "two exact generators produce all 24 proper cubic carrier rotations and intertwine the multiplicity trace"),
        ("D_fixed_frame_cylinders", sharp == expected_sharp and half == expected_half and fixed_geometry,
         f"fixed-frame enlarged-register protocol has sharp={sharp}, half={half}, and the stated shell overlap"),
        ("E_stencil_covariance_counterexample", rotation.det() == 1 and pure_mask == 17
         and tuple(rotated_detector) == (0, -1, 0) and covariance_residual_rank == 4,
         "proper R fixes pure-permuted mask17 but flips its detector; branch residual rank is four"),
        ("F_actual_fault_controls", fault_controls,
         "rescaled Kraus, explicitly executed carrier reset, and changed branch-direction operands each fail their target identity"),
        ("G_scope", all(token in note for token in ("supplied enlarged register",
             "framework-native one-site", "whole-stencil cubic covariance is withdrawn",
             "No full mutation sweep is claimed", "no formal audit has run")),
         "physical encoding/readout, stencil covariance, full mutation sweep, and audit remain open"),
    )
    passed = sum(ok for _, ok, _ in checks)
    for name, ok, message in checks:
        print(f"{'PASS' if ok else 'FAIL'} {name}: {message}")
    print(f"ALGEBRA: word_rank={word_rank}; chirality_ranks={[p.rank() for p in projectors]}; carrier=M4.")
    print(f"HISTORY_FIXED_FRAME: sharp={sharp}; half={half}; reset={reset_history}; spatial_encoding=supplied_open_bridge.")
    print(f"COVARIANCE_BOUNDARY: pure_mask17={pure_mask}; rotated_detector={tuple(rotated_detector)}; residual_rank={covariance_residual_rank}.")
    print("FAULT_CONTROLS: executed=3; rejected=3; full_mutation_sweep=false.")
    print(f"TOTAL: PASS={passed} FAIL={len(checks)-passed}")
    return int(passed != len(checks))


if __name__ == "__main__":
    raise SystemExit(main())
