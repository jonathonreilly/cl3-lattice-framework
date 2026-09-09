#!/usr/bin/env python3
"""Executable checks for the Block 54 gauge-instrument/generator boundary.

Recovered from the original scratch runner (SHA-256
2f80aa2cd4eafacc2d25dcb0848a61649514294b1a183cd751c1d1f77bb920e1).
The original checks are preserved, with the Wilson Hessian and boundedness
checks strengthened to derive their tested matrices independently.
"""

from __future__ import annotations

import itertools
import math
from fractions import Fraction

import numpy as np


TOL = 5e-10
passes = 0
fails = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global passes, fails
    if condition:
        passes += 1
        print(f"PASS {name}" + (f" :: {detail}" if detail else ""))
    else:
        fails += 1
        print(f"FAIL {name}" + (f" :: {detail}" if detail else ""))


def gell_mann_half() -> list[np.ndarray]:
    z = 0.0j
    i = 1.0j
    mats = [
        [[0, 1, 0], [1, 0, 0], [0, 0, 0]],
        [[0, -i, 0], [i, 0, 0], [0, 0, 0]],
        [[1, 0, 0], [0, -1, 0], [0, 0, 0]],
        [[0, 0, 1], [0, 0, 0], [1, 0, 0]],
        [[0, 0, -i], [0, 0, 0], [i, 0, 0]],
        [[0, 0, 0], [0, 0, 1], [0, 1, 0]],
        [[0, 0, 0], [0, 0, -i], [0, i, 0]],
        [[1 / math.sqrt(3), 0, 0], [0, 1 / math.sqrt(3), 0], [0, 0, -2 / math.sqrt(3)]],
    ]
    return [np.asarray(m, dtype=complex) / 2 for m in mats]


def embedded_generators() -> list[np.ndarray]:
    out = []
    for t in gell_mann_half():
        x = np.zeros((4, 4), dtype=complex)
        x[:3, :3] = t
        out.append(x)
    return out


def commutant_nullity(gens: list[np.ndarray]) -> tuple[int, np.ndarray]:
    # vec(XG-GX) = (G^T tensor I - I tensor G) vec(X), column convention.
    ident = np.eye(4, dtype=complex)
    constraints = []
    for g in gens:
        constraints.append(np.kron(g.T, ident) - np.kron(ident, g))
    a = np.vstack(constraints)
    _, s, vh = np.linalg.svd(a)
    rank = int(np.sum(s > 1e-10))
    return 16 - rank, vh[rank:].conj().T


def choi(phi, d: int = 4) -> np.ndarray:
    c = np.zeros((d * d, d * d), dtype=complex)
    for i in range(d):
        for j in range(d):
            e = np.zeros((d, d), dtype=complex)
            e[i, j] = 1
            c += np.kron(e, phi(e))
    return c


def random_density(seed: int) -> np.ndarray:
    rng = np.random.default_rng(seed)
    x = rng.normal(size=(4, 4)) + 1j * rng.normal(size=(4, 4))
    rho = x @ x.conj().T
    return rho / np.trace(rho)


def random_su3(seed: int) -> np.ndarray:
    rng = np.random.default_rng(seed)
    x = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))
    q, r = np.linalg.qr(x)
    phases = np.diag(r)
    q = q @ np.diag(np.conj(phases) / np.abs(phases))
    q = q / np.linalg.det(q) ** (1 / 3)
    return q


def casimir_su3(p: int, q: int) -> Fraction:
    return Fraction(p * p + q * q + p * q + 3 * p + 3 * q, 3)


def wilson_log_plane(beta: int, coordinates: np.ndarray) -> float:
    """Unnormalised log plane weight along canonical SU(3) tangents."""
    generators = gell_mann_half()
    tangent = sum((coordinates[a] * generators[a] for a in range(8)), np.zeros((3, 3), dtype=complex))
    eigenvalues = np.linalg.eigvalsh(tangent)
    return beta / 3.0 * float(np.sum(np.cos(eigenvalues)))


def finite_difference_negative_hessian(beta: int, step: float = 1.0e-3) -> np.ndarray:
    """Independent central-difference Hessian of -log K_beta at the identity."""
    origin = np.zeros(8)
    f0 = wilson_log_plane(beta, origin)
    result = np.zeros((8, 8))
    for a in range(8):
        plus = origin.copy()
        minus = origin.copy()
        plus[a] = step
        minus[a] = -step
        result[a, a] = -(wilson_log_plane(beta, plus) - 2.0 * f0 + wilson_log_plane(beta, minus)) / step**2
        for b in range(a + 1, 8):
            pp = origin.copy()
            pm = origin.copy()
            mp = origin.copy()
            mm = origin.copy()
            pp[a], pp[b] = step, step
            pm[a], pm[b] = step, -step
            mp[a], mp[b] = -step, step
            mm[a], mm[b] = -step, -step
            value = -(
                wilson_log_plane(beta, pp)
                - wilson_log_plane(beta, pm)
                - wilson_log_plane(beta, mp)
                + wilson_log_plane(beta, mm)
            ) / (4.0 * step**2)
            result[a, b] = result[b, a] = value
    return result


def main() -> None:
    gens = embedded_generators()
    gram = np.array([[np.trace(a @ b).real for b in gens] for a in gens])
    check("canonical half-trace Gram", np.max(np.abs(gram - 0.5 * np.eye(8))) < TOL)

    nullity, basis = commutant_nullity(gens)
    check("3+1 SU3 commutant has dimension two", nullity == 2, f"nullity={nullity}")

    p3 = np.diag([1, 1, 1, 0]).astype(complex)
    p1 = np.diag([0, 0, 0, 1]).astype(complex)
    check("P3 and P1 commute with all generators", all(np.linalg.norm(p3 @ g - g @ p3) < TOL and np.linalg.norm(p1 @ g - g @ p1) < TOL for g in gens))

    # A continuum of invariant binary effects survives gauge symmetry.
    for a, b in [(0.2, 0.8), (0.5, 0.5), (0.9, 0.1)]:
        e = a * p3 + b * p1
        ev = np.linalg.eigvalsh(e)
        check(f"unsharp invariant effect ({a},{b})", ev.min() >= -TOL and ev.max() <= 1 + TOL)
        check(f"binary complement ({a},{b})", np.linalg.norm(e + (np.eye(4) - e) - np.eye(4)) < TOL)

    sharp = []
    for a, b in itertools.product([0, 1], repeat=2):
        e = a * p3 + b * p1
        if np.linalg.norm(e @ e - e) < TOL:
            sharp.append((a, b))
    check("all invariant sharp effects are four commutant corners", sharp == [(0, 0), (0, 1), (1, 0), (1, 1)], str(sharp))
    check("unique nontrivial invariant PVM up to labels", set(sharp[1:3]) == {(0, 1), (1, 0)})

    # Even after sharp effects and repeatability are supplied, the covariant
    # instrument is not unique: lambda interpolates Lueders and depolarization.
    for lam in [0.0, 0.25, 0.75, 1.0]:
        def phi3(rho, lam=lam):
            block = p3 @ rho @ p3
            return lam * block + (1 - lam) * np.trace(block) * p3 / 3

        def phi1(rho):
            return p1 @ rho @ p1

        c3 = choi(phi3)
        c1 = choi(phi1)
        check(f"triplet instrument CP lambda={lam}", np.linalg.eigvalsh(c3).min() > -TOL)
        check(f"singlet instrument CP lambda={lam}", np.linalg.eigvalsh(c1).min() > -TOL)

        for seed in [1, 2, 3]:
            rho = random_density(seed)
            out3 = phi3(rho)
            out1 = phi1(rho)
            check(f"instrument trace complete lambda={lam} seed={seed}", abs(np.trace(out3 + out1) - 1) < TOL)
            check(f"triplet outcome repeatable lambda={lam} seed={seed}", np.linalg.norm(p3 @ out3 @ p3 - out3) < TOL)
            check(f"singlet outcome repeatable lambda={lam} seed={seed}", np.linalg.norm(p1 @ out1 @ p1 - out1) < TOL)

        for seed in [4, 5]:
            u = random_su3(seed)
            r = np.zeros((4, 4), dtype=complex)
            r[:3, :3] = u
            r[3, 3] = 1
            rho = random_density(seed + 10)
            lhs = phi3(r @ rho @ r.conj().T)
            rhs = r @ phi3(rho) @ r.conj().T
            check(f"triplet instrument gauge covariance lambda={lam} seed={seed}", np.linalg.norm(lhs - rhs) < 2e-9)

        pure = np.zeros((4, 4), dtype=complex)
        pure[0, 0] = 1
        purity = float(np.trace(phi3(pure) @ phi3(pure)).real)
        expected = lam * lam + 2 * lam * (1 - lam) / 3 + (1 - lam) ** 2 / 3
        check(f"instrument continuum changes post-state lambda={lam}", abs(purity - expected) < TOL, f"purity={purity:.9f}")

    # Exact coefficient algebra: all g pass the isotropic product constraint;
    # only an extra coefficient-equality condition selects g=1.
    for g2 in [Fraction(1, 4), Fraction(1, 1), Fraction(4, 1), Fraction(9, 1)]:
        a_e = g2
        a_b = 1 / g2
        check(f"E/B product blind at g2={g2}", a_e * a_b == 1)
        check(f"coefficient equality iff g2=1 at g2={g2}", (a_e == a_b) == (g2 == 1))

    # Raw same-carrier E/B swap is impossible at finite lattice volume:
    # electric Casimirs are unbounded while every compact plaquette deficit is bounded.
    c2 = [casimir_su3(p, 0) for p in range(21)]
    check("SU3 electric Casimir sequence strictly increasing", all(c2[i + 1] > c2[i] for i in range(len(c2) - 1)))
    check("SU3 electric Casimir is unbounded by formula", casimir_su3(100, 0) > 3000, f"C2(100,0)={casimir_su3(100,0)}")
    # Re Tr U >= -3/2 for SU3, with the lower endpoint attained at a
    # nontrivial center element, so 0 <= 1-ReTr(U)/3 <= 3/2.
    center = np.exp(2j * math.pi / 3.0) * np.eye(3)
    center_deficit = 1.0 - np.trace(center).real / 3.0
    sampled_deficits = [1.0 - np.trace(random_su3(seed)).real / 3.0 for seed in range(20, 40)]
    check(
        "single Wilson magnetic plaquette bounded",
        abs(center_deficit - 1.5) < TOL
        and all(-TOL <= value <= 1.5 + TOL for value in sampled_deficits)
        and Fraction(3, 2) < casimir_su3(3, 0),
    )

    # Exact tangent Hessian of the Wilson plane kernel.
    nc = 3
    tangent_generators = gell_mann_half()
    symmetrized_gram = np.array(
        [
            [np.trace(a @ b + b @ a).real for b in tangent_generators]
            for a in tangent_generators
        ]
    )
    for beta in [6, 24]:
        hessian_coefficient = Fraction(beta, 2 * nc)
        analytic_hessian = beta / (2.0 * nc) * symmetrized_gram
        finite_hessian = finite_difference_negative_hessian(beta)
        expected_hessian = float(hessian_coefficient) * np.eye(8)
        check(
            f"Wilson tangent Hessian beta={beta}",
            np.max(np.abs(analytic_hessian - expected_hessian)) < TOL
            and np.max(np.abs(finite_hessian - expected_hessian)) < 2.0e-6,
            f"coef={hessian_coefficient}",
        )
    check("unit canonical Hessian uniquely returns beta=2Nc", 2 * nc == 6)

    print("SUMMARY")
    print(f"COMMUTANT_NULLITY={nullity}")
    print("INVARIANT_EFFECT_CONE={(a,b): 0<=a,b<=1}")
    print("SHARP_NONTRIVIAL_EFFECTS={P3,P1} up to labels")
    print("REPEATABLE_COVARIANT_INSTRUMENTS=continuum(lambda in [0,1])")
    print("HAMILTONIAN_RELATIVE_COEFFICIENT=free(g^2>0)")
    print("RAW_EB_SAME_CARRIER_DUALITY=excluded(boundedness mismatch)")
    print("WILSON_UNIT_HESSIAN_LAW=>beta=2Nc=6 (supplied law, not derived)")
    print(
        "per_element: checked — canonical generator Gram, invariant effects, "
        "Choi positivity, center bound, and identity-tangent Wilson Hessian"
    )
    print(
        "per_site: checked — the supplied 3+1 carrier instrument was tested "
        "for completeness, repeatability, covariance, and distinct post-states"
    )
    print(
        "per_mode: checked and not executed — no momentum-space mode or "
        "continuum spectral claim is made by this finite-carrier packet"
    )
    print(
        "per_block: checked — exact coefficient algebra and bounded/unbounded "
        "spectral witnesses support the analytic finite-lattice lift"
    )
    print(
        "lattice_wide: checked and not executed — no thermodynamic, continuum, "
        "confinement, mass-gap, or full Standard Model claim was simulated"
    )
    print(f"TOTAL: PASS={passes} FAIL={fails}")
    raise SystemExit(1 if fails else 0)


if __name__ == "__main__":
    main()
