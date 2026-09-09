#!/usr/bin/env python3
"""Independent sector, cylinder, and covariance-boundary check for Block-06."""
from __future__ import annotations

import hashlib
from itertools import product
from pathlib import Path
import re
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs/ADMISSIBILITY_D4_ORDERED_H1_FRONT_CARRIER_INTERFACE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md"
PRIMARY = ROOT / "scripts/admissibility_d4_ordered_h1_front_carrier_interface_2026_08_29.py"
PRIMARY_CACHE = ROOT / "logs/runner-cache/admissibility_d4_ordered_h1_front_carrier_interface_2026_08_29.txt"
AUDIT_TIMEOUT_SEC = 30
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_D4_ORDERED_H1_FRONT_CARRIER_INTERFACE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md",
    "scripts/admissibility_d4_ordered_h1_front_carrier_interface_2026_08_29.py",
    "logs/runner-cache/admissibility_d4_ordered_h1_front_carrier_interface_2026_08_29.txt",
)
I = sp.I
I4 = sp.eye(4)
X = sp.Matrix(((0, 1), (1, 0)))
Y = sp.Matrix(((0, -I), (I, 0)))
Z = sp.diag(1, -1)
D = (sp.diag(X, X), sp.diag(Y, -Y), sp.diag(Z, Z))
SHELL = ((-1, 0, 0), (1, 0, 0), (0, -1, 0),
         (0, 1, 0), (0, 0, -1), (0, 0, 1))


def cache_bound() -> bool:
    text = PRIMARY_CACHE.read_text(encoding="utf-8")
    digest = hashlib.sha256(PRIMARY.read_bytes()).hexdigest()
    match = re.search(r"^runner_sha256:\s*([0-9a-f]{64})$", text, re.M)
    return bool(match and match.group(1) == digest and "status: ok" in text
                and "TOTAL: PASS=7 FAIL=0" in text)


def root(direction: sp.MatrixBase, outcome: int, u: sp.Expr) -> sp.Matrix:
    sign = 1 if outcome == 0 else -1
    same = (I4 + sign * direction) / 2
    other = (I4 - sign * direction) / 2
    return sp.sqrt((1 + u) / 2) * same + sp.sqrt((1 - u) / 2) * other


def direct_cylinders(u: sp.Expr) -> tuple[sp.Expr, ...]:
    answer = []
    for first_outcome, second_outcome in product((0, 1), repeat=2):
        k = root(D[1], first_outcome, u)
        direction = D[1] if first_outcome == 0 else D[0]
        q = root(direction, second_outcome, u)
        answer.append(sp.simplify(sp.trace(q*k*k.H*q.H) / 4))
    return tuple(answer)


def direct_reset_cylinders(u: sp.Expr) -> tuple[sp.Expr, ...]:
    rho = I4 / 4
    answer = []
    for first_outcome, second_outcome in product((0, 1), repeat=2):
        first = root(D[1], first_outcome, u)
        first_probability = sp.simplify(sp.trace(first * rho * first.H))
        direction = D[1] if first_outcome == 0 else D[0]
        second = root(direction, second_outcome, u)
        second_probability = sp.simplify(sp.trace(second * rho * second.H))
        answer.append(sp.simplify(first_probability * second_probability))
    return tuple(answer)


def branch_effect(direction: sp.MatrixBase, outcome: int, u: sp.Expr) -> sp.Matrix:
    k = root(direction, outcome, u)
    return sp.simplify(k.H * k)


def main() -> int:
    chi = sp.simplify(I * D[0] * D[1] * D[2])
    projectors = ((I4 - chi) / 2, (I4 + chi) / 2)
    central_ok = [p.rank() for p in projectors] == [2, 2]
    anticommutation = all(sp.simplify(D[i]*D[j] + D[j]*D[i]) == sp.zeros(4)
                           for i in range(3) for j in range(i + 1, 3))

    sharp = direct_cylinders(sp.Integer(1))
    half = direct_cylinders(sp.Rational(1, 2))
    rotation = sp.Matrix(((0, 0, 1), (0, -1, 0), (1, 0, 0)))
    permuted = 0
    for i, direction in enumerate(SHELL):
        image = tuple(int(x) for x in rotation * sp.Matrix(direction))
        permuted |= ((17 >> i) & 1) << SHELL.index(image)
    pure_branch = branch_effect(D[1], 0, sp.Integer(1))
    transported_branch = branch_effect(-D[1], 0, sp.Integer(1))
    residual = sp.simplify(pure_branch - transported_branch)

    reset = direct_reset_cylinders(sp.Integer(1))
    checks = (
        ("A_primary_identity", cache_bound(), "primary cache matches current primary source"),
        ("B_independent_sector_algebra", central_ok and anticommutation,
         "independent M4 matrices have two central rank-two sectors and Clifford anticommutation"),
        ("C_independent_cylinders", sharp == (sp.Rational(1, 2), 0,
             sp.Rational(1, 4), sp.Rational(1, 4))
         and half == (sp.Rational(5, 16), sp.Rational(3, 16),
                      sp.Rational(1, 4), sp.Rational(1, 4)),
         f"direct traces give sharp={sharp} and half={half}"),
        ("D_covariance_boundary", rotation.det() == 1 and permuted == 17
         and tuple(rotation * sp.Matrix((0, 1, 0))) == (0, -1, 0)
         and residual.rank() == 4,
         "pure shell action fixes mask17 while detector transport flips sign, giving rank-four residual"),
        ("E_fault_witness", reset != sharp,
         "an explicitly executed reset-to-I4/4 protocol removes the sharp correlation"),
    )
    passed = sum(ok for _, ok, _ in checks)
    for name, ok, message in checks:
        print(f"{'PASS' if ok else 'FAIL'} {name}: {message}")
    print(f"INDEPENDENT_HISTORY: sharp={sharp}; half={half}; reset={reset}.")
    print("INDEPENDENT_SCOPE: enlarged_register=supplied; whole_stencil_covariance=false; physical_bridge=open.")
    print("FAULT_CONTROLS: executed=1; rejected=1; full_mutation_sweep=false.")
    print(f"TOTAL: PASS={passed} FAIL={len(checks)-passed}")
    return int(passed != len(checks))


if __name__ == "__main__":
    raise SystemExit(main())
