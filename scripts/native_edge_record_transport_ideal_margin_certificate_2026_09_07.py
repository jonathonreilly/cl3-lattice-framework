#!/usr/bin/env python3
"""Exact-rational ideal margins for the fixed five-event native edge protocol.

Independent eight-mode reconstruction; imports no other runner or receipt.
Scientific enclosure arithmetic uses only integers/Fractions; floating-point
runtime/resource measurements are presentation and execution-envelope checks.
Decimal enclosure output is rounded down and is presentation only.
The certificate is conditional on the specified
ideal nonbridge CAR instrument, for which deletion leaves the CAR state intact.
It does not certify actual finite-width observations or apparatus locality.
"""
from __future__ import annotations

import math
import os
import resource
import signal
import sys
import time
from fractions import Fraction as F

for _name in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[_name] = "1"
AUDIT_TIMEOUT_SEC = 180
AUDIT_MEMORY_MIB = 180
TAYLOR_DEGREE = 30
N = 8
EDGES = ((0, 1), (0, 2), (0, 4), (1, 3), (1, 5), (2, 3),
         (2, 6), (3, 7), (4, 5), (4, 6), (5, 7), (6, 7))
COEFF = (-1, -1, -1, -1, -1, 1, -1, -1, 1, 1, 1, -1)
PATH = (0, 3, 5, 6, 9)
DWELLS = (F(41, 100), F(37, 100), F(29, 100), F(23, 100), F(19, 100))


def zeros():
    return [[0] * N for _ in range(N)]


def identity():
    return [[int(i == j) for j in range(N)] for i in range(N)]


def imul(a, b):
    bt = list(zip(*b))
    return [[sum(x * y for x, y in zip(row, col)) for col in bt] for row in a]


class Matrix:
    """Gaussian-integer numerator with one positive common denominator."""

    def __init__(self, real, imag=None, denominator=1):
        self.r = real
        self.i = zeros() if imag is None else imag
        self.d = denominator
        common = denominator
        for row in self.r + self.i:
            for value in row:
                common = math.gcd(common, value)
        if common != 1:
            self.d //= common
            self.r = [[x // common for x in row] for row in self.r]
            self.i = [[x // common for x in row] for row in self.i]

    def __matmul__(self, other):
        rr, ii = imul(self.r, other.r), imul(self.i, other.i)
        ri, ir = imul(self.r, other.i), imul(self.i, other.r)
        return Matrix([[rr[a][b] - ii[a][b] for b in range(N)] for a in range(N)],
                      [[ri[a][b] + ir[a][b] for b in range(N)] for a in range(N)],
                      self.d * other.d)

    def adjoint(self):
        return Matrix([list(x) for x in zip(*self.r)],
                      [[-x for x in row] for row in zip(*self.i)], self.d)

    def hermitian(self):
        return all(self.r[a][b] == self.r[b][a] and self.i[a][b] == -self.i[b][a]
                   for a in range(N) for b in range(N))


def hopping(live):
    h = zeros()
    for e in live:
        u, v = EDGES[e]
        h[u][v] = h[v][u] = COEFF[e]
    return h


def taylor_unitary(h, duration, norm_bound):
    """P_30(-i duration h), with rigorous operator-norm remainder.

    In the absolute exponential tail, ratios after the first omitted term
    are at most x/(degree+2). This geometric bound needs no float or exp().
    """
    degree = TAYLOR_DEGREE
    coefficients = [duration ** k / math.factorial(k) for k in range(degree + 1)]
    denominator = math.lcm(*(q.denominator for q in coefficients))
    real, imag, power = zeros(), zeros(), identity()
    for k, coefficient in enumerate(coefficients):
        integer_coefficient = coefficient.numerator * (denominator // coefficient.denominator)
        target = real if k % 2 == 0 else imag
        sign = (1, -1, -1, 1)[k % 4]
        for a in range(N):
            for b in range(N):
                target[a][b] += sign * integer_coefficient * power[a][b]
        power = imul(power, h)
    x = abs(duration) * norm_bound
    assert x < degree + 2
    remainder = x ** (degree + 1) / math.factorial(degree + 1) / (1 - x / (degree + 2))
    return Matrix(real, imag, denominator), remainder


def evolve(covariance, covariance_error, h, duration, norm_bound):
    polynomial, remainder = taylor_unitary(h, duration, norm_bound)
    updated = polynomial @ covariance @ polynomial.adjoint()
    # True ideal covariance remains an orthogonal projector of norm one.
    # ||P Ctilde P* - U C U*|| <= (1+r)^2 eps + r(2+r).
    error = (1 + remainder) ** 2 * covariance_error + remainder * (2 + remainder)
    return updated, error


def connected(live):
    reached, stack = {0}, [0]
    while stack:
        vertex = stack.pop()
        for e in live:
            u, v = EDGES[e]
            if vertex == u and v not in reached:
                reached.add(v)
                stack.append(v)
            if vertex == v and u not in reached:
                reached.add(u)
                stack.append(u)
    return len(reached) == N


def down(value, places=10):
    scale = 10 ** places
    integer = value.numerator * scale // value.denominator
    sign = "-" if integer < 0 else ""
    whole, decimal = divmod(abs(integer), scale)
    return f"{sign}{whole}.{decimal:0{places}d}"


def main():
    signal.alarm(AUDIT_TIMEOUT_SEC)
    started = time.monotonic()
    checks = []

    def check(label, ok):
        checks.append(bool(ok))
        print(f"[{'PASS' if ok else 'FAIL'}] {label}")

    live = set(range(len(EDGES)))
    h0 = hopping(live)
    square = imul(h0, h0)
    check("signed cube has h0^2=3I exactly", square == [[3 * x for x in row] for row in identity()])
    # Every remaining signed hopping matrix has absolute row sum <=3.
    check("degree-three operator-norm bound", all(sum(abs(x) for x in row) <= 3 for row in h0))

    scale = 10 ** 24
    lower_integer = math.isqrt(3 * scale * scale)
    lo, hi = F(lower_integer, scale), F(lower_integer + 1, scale)
    check("integer-certified sqrt(3) enclosure", lo * lo < 3 < hi * hi)
    reciprocal = 1 / lo
    common = 2 * reciprocal.denominator
    real = [[(reciprocal.denominator if a == b else 0) - h0[a][b] * reciprocal.numerator
             for b in range(N)] for a in range(N)]
    covariance = Matrix(real, denominator=common)
    error = F(3, 2) * (1 / lo - 1 / hi)
    pulse = zeros()
    pulse[0][0], pulse[1][1] = 1, -1
    covariance, error = evolve(covariance, error, pulse, F(7, 10), F(1))
    initial_energy = sum((F(2 * COEFF[e] * covariance.r[u][v], covariance.d)
                          for e, (u, v) in enumerate(EDGES)), F(0))
    initial_energy_margin = -F(1, 10 ** 6) - initial_energy - 2 * len(EDGES) * error
    check("initial pulsed energy below -1e-6", initial_energy_margin > 0)
    print(f"initial_pulsed_negative_energy_slack>={down(initial_energy_margin)}")
    # Every pre-event Hamiltonian is the previous post-event Hamiltonian;
    # its dwell commutes with it. Initial + all post energy certificates
    # therefore cover every pre/post prefix. The energy-preserving battery
    # lift of that same-Hamiltonian dwell is simply the dwell tensor I_B.

    rows, front_candidates, requirements = [], [], []
    all_hermitian, all_connected = True, True
    for j, (selected, dwell) in enumerate(zip(PATH, DWELLS), start=1):
        covariance, error = evolve(covariance, error, hopping(live), dwell, F(3))
        all_hermitian &= covariance.hermitian()
        current_bounds = []
        for e in sorted(live):
            u, v = EDGES[e]
            # C_uv=<c_v^dag c_u>, so i<c_u^dag c_v-c_v^dag c_u>=2 Im C_uv.
            value = F(2 * COEFF[e] * covariance.i[u][v], covariance.d)
            absolute_lower = abs(value) - 2 * error
            current_bounds.append((absolute_lower, e))
            if e == selected:
                front_candidates.append((absolute_lower - F(5, 100), j, e))
        current_bounds.sort(reverse=True)
        fourth_margin = current_bounds[3][0] - F(2, 100)
        chosen = tuple(e for _, e in current_bounds[:4])
        if fourth_margin > 0:
            # pi<4 (from pi/4=int_0^1 1/(1+x^2) dx<1); hence pi^2<16.
            requirements.append((F(32 * (j - 1) * len(EDGES)) / fourth_margin,
                                 f"pre-current-{j}"))

        live.remove(selected)
        all_connected &= connected(live)
        post_current_bounds = [(bound, e) for bound, e in current_bounds if e in live]
        post_fourth_margin = post_current_bounds[3][0] - F(2, 100)
        post_chosen = tuple(e for _, e in post_current_bounds[:4])
        if post_fourth_margin > 0:
            requirements.append((F(32 * j * len(EDGES)) / post_fourth_margin,
                                 f"post-current-{j}"))
        density_margin = min(min(F(covariance.r[v][v], covariance.d) - F(1, 10),
                                 F(9, 10) - F(covariance.r[v][v], covariance.d)) - error
                             for v in range(N))
        energy = sum((F(2 * COEFF[e] * covariance.r[u][v], covariance.d)
                      for e in live for u, v in (EDGES[e],)), F(0))
        energy_error = 2 * len(live) * error
        energy_margin = -F(1, 10 ** 6) - energy - energy_error
        if density_margin > 0:
            requirements.append((F(16 * j * len(EDGES)) / density_margin, f"post-density-{j}"))
        if energy_margin > 0:
            # omega(H_j)<=||H_j||<=number of live unit-strength bonds.
            requirements.append((F(32 * j * len(EDGES) * len(live)) / energy_margin,
                                 f"post-negative-energy-{j}"))
        rows.append((j, chosen, fourth_margin, density_margin, energy_margin, error,
                     post_chosen, post_fourth_margin))

    check("all rational covariances exactly Hermitian", all_hermitian)
    check("every prescribed deletion leaves graph connected", all_connected)
    check("all five pre-event fourth-current slacks strictly positive", all(row[2] > 0 for row in rows))
    check("all five additional post-event fourth-current slacks strictly positive",
          all(row[7] > 0 for row in rows))
    check("all post-event densities strictly within [0.1,0.9]", all(row[3] > 0 for row in rows))
    check("all post-event energies below -1e-6 (stronger than parent minimum gate)",
          all(row[4] > 0 for row in rows))
    front_margin, front_step, front_edge = max(front_candidates)
    check("one pre-event selected-front current exceeds 0.05", front_margin > 0)
    if front_margin > 0:
        requirements.append((F(32 * (front_step - 1) * len(EDGES)) / front_margin, "front-witness"))

    for j, chosen, cm, dm, em, eps, post_chosen, post_cm in rows:
        print(f"prefix={j} chosen_four={chosen} current_slack>={down(cm)} "
              f"post_chosen_four={post_chosen} post_current_slack>={down(post_cm)} "
              f"density_slack>={down(dm)} negative_energy_slack>={down(em)} "
              f"covariance_error<1e-22={eps < F(1, 10**22)}")
    print(f"front_witness step={front_step} edge={front_edge} slack>={down(front_margin)}")
    check("covariance errors bounded strictly below 1e-22", all(row[5] < F(1, 10**22) for row in rows))

    if all(checks):
        ratio, bottleneck = max(requirements)
        width = math.isqrt(ratio.numerator // ratio.denominator) + 1
        check("chosen integer width strictly exceeds every sufficient bound", all(width * width > r for r, _ in requirements))
        original_requirements = [(r, label) for r, label in requirements
                                 if not label.startswith("post-current-")]
        original_ratio, original_bottleneck = max(original_requirements)
        original_width = math.isqrt(original_ratio.numerator // original_ratio.denominator) + 1
        check("original-only integer width strictly exceeds its sufficient bounds",
              all(original_width * original_width > r for r, _ in original_requirements))
        print(f"ORIGINAL_GATES_SUFFICIENT_WIDTH={original_width} "
              f"bottleneck={original_bottleneck} support=[24,{24+original_width}] "
              f"mean={F(48+original_width,2)} cap={48+original_width}")
        print(f"ADDED_POST_GATE_SUFFICIENT_WIDTH={width} derived_from=ideal_slacks_and_pi_squared_less_than_16 "
              f"bottleneck={bottleneck}")
        print(f"BATTERY support=[24,{24+width}] mean={F(48+width,2)} cap={48+width}; "
              "one retained continuous battery, no reset; width-one result unchanged")
    else:
        print("SUFFICIENT_WIDTH=UNAVAILABLE: a required ideal slack was not certified")
    print("Scope: original pre-current/front gates, added post-current gate, and "
          "post-density/all-prefix-negative-energy gates; no optimum-width claim")
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    mib = rss / (1024**2 if sys.platform == "darwin" else 1024)
    elapsed = time.monotonic() - started
    check("execution stays within 180 seconds and 180 MiB",
          elapsed < AUDIT_TIMEOUT_SEC and mib < AUDIT_MEMORY_MIB)
    print(f"runtime_seconds={elapsed:.2f} peak_rss_mib={mib:.1f}")
    print(f"TOTAL: PASS={sum(checks)} FAIL={len(checks)-sum(checks)}")
    signal.alarm(0)
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
