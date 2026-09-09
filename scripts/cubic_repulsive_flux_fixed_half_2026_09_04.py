#!/usr/bin/env python3
"""Finite diagnostics for the fixed-half cubic repulsive flux theorem."""
from __future__ import annotations

import itertools
import sys

import numpy as np

AUDIT_TIMEOUT_SEC = 180
TOL = 2.0e-9


class Gates:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, name: str, ok: bool, detail: str) -> None:
        self.passed += int(ok)
        self.failed += int(not ok)
        status = "PASS" if ok else "FAIL"
        print(f"{status} {name}: {detail}")


def psd_sqrt(x: np.ndarray) -> np.ndarray:
    vals, vecs = np.linalg.eigh((x + x.conj().T) / 2)
    return (vecs * np.sqrt(np.maximum(vals, 0.0))) @ vecs.conj().T


def charge_hermitian(rng: np.random.Generator, charge: np.ndarray) -> np.ndarray:
    z = rng.normal(size=(4, 4)) + 1j * rng.normal(size=(4, 4))
    z *= charge[:, None] == charge[None, :]
    return (z + z.conj().T) / 2


def real_couplings(rng: np.random.Generator, charge: np.ndarray) -> list[np.ndarray]:
    up = np.zeros((4, 4))
    for i, j in itertools.product(range(4), repeat=2):
        if charge[i] == charge[j] + 1:
            up[i, j] = 0.35 * rng.normal()
    return [up, up.T, np.diag(0.25 * rng.normal(size=4))]


def coefficient(rng: np.random.Generator, charge: np.ndarray, q: int) -> np.ndarray:
    c = rng.normal(size=(4, 4)) + 1j * rng.normal(size=(4, 4))
    c *= charge[:, None] - charge[None, :] == q
    return c / np.linalg.norm(c)


def trace_energy(c: np.ndarray, a: np.ndarray, b: np.ndarray,
                 couplings: list[np.ndarray]) -> float:
    left, right = c @ c.conj().T, c.conj().T @ c
    value = np.trace(a @ left) + np.trace(b.T @ right)
    value -= sum(np.trace(c.conj().T @ k @ c @ k.T) for k in couplings)
    return float(value.real)


def polar_sample(rng: np.random.Generator, q: int) -> tuple[float, ...]:
    charge = np.array([0, 1, 1, 2])
    a, b = charge_hermitian(rng, charge), charge_hermitian(rng, charge)
    couplings, c = real_couplings(rng, charge), coefficient(rng, charge, q)
    ident = np.eye(4)
    total = np.kron(a, ident) + np.kron(ident, b)
    total -= sum(np.kron(k, k) for k in couplings)
    psi = c.reshape(-1)
    direct = float(np.vdot(psi, total @ psi).real)
    traced = trace_energy(c, a, b, couplings)
    left, right = psd_sqrt(c @ c.conj().T), psd_sqrt(c.conj().T @ c)
    reflected = 0.5 * (trace_energy(left, a, a.conj(), couplings)
                       + trace_energy(right, b.conj(), b, couplings))
    wrong = 0.5 * (trace_energy(left, a, a, couplings)
                   + trace_energy(right, b, b, couplings))
    vector = max(
        np.linalg.norm(np.kron(a, ident) @ psi - (a @ c).reshape(-1)),
        np.linalg.norm(np.kron(ident, b) @ psi - (c @ b.T).reshape(-1)),
        max(np.linalg.norm(np.kron(k, k) @ psi - (k @ c @ k.T).reshape(-1))
            for k in couplings),
    )
    charge_op = np.diag(charge)
    charge_defect = max(np.linalg.norm(charge_op @ x - x @ charge_op)
                        for x in (left, right))
    norm_defect = max(abs(np.trace(x @ x).real - 1.0) for x in (left, right))
    return (direct - reflected, direct - wrong, abs(direct - traced), vector,
            charge_defect, norm_defect, np.linalg.norm(total - total.conj().T))


def check_polar(gates: Gates) -> None:
    rows: dict[int, list[tuple[float, ...]]] = {}
    for q, count in ((0, 120), (-1, 60), (1, 60)):
        rng = np.random.default_rng(12030 + q)
        rows[q] = [polar_sample(rng, q) for _ in range(count)]
    all_rows = sum(rows.values(), [])
    direct = max(max(r[2], r[3], r[6]) for r in all_rows)
    structure = max(max(r[4], r[5]) for r in all_rows)
    gates.check("polar direct/trace/vectorization", direct < TOL,
                f"cases=240 max_residual={direct:.3e}")
    gates.check("polar roots preserve norm and charge", structure < TOL,
                f"max_residual={structure:.3e}")
    q0_margin = min(r[0] for r in rows[0])
    optional_margin = min(r[0] for q in (-1, 1) for r in rows[q])
    gates.check("polar fixed-half q=0 inequality", q0_margin >= -TOL,
                f"cases=120 min_margin={q0_margin:.9g}")
    gates.check("polar q=+-1 algebraic observation", optional_margin >= -TOL,
                f"cases=120 min_margin={optional_margin:.9g}; no off-half flux claim")
    mutation_rng = np.random.default_rng(415)
    mutation = [polar_sample(mutation_rng, 0)[1] for _ in range(200)]
    bad = min(mutation)
    gates.check("mutation requires complex conjugation", bad < -1.0e-4,
                f"seed=415 cases=200 wrong_min_margin={bad:.9g}")


def cube_geometry() -> tuple[list[tuple[int, int]], list[int], list[int]]:
    def site(x: int, y: int, z: int) -> int:
        return 4 * x + 2 * y + z
    edges = []
    for x, y, z in itertools.product(range(2), repeat=3):
        for axis in range(3):
            nxt = [x, y, z]
            if nxt[axis] == 0:
                nxt[axis] = 1
                edges.append((site(x, y, z), site(*nxt)))
    return edges, list(range(4)), list(range(4, 8))


def sector_basis(n_sites: int, number: int) -> list[int]:
    return [s for s in range(1 << n_sites) if s.bit_count() == number]


def sector_hamiltonian(h: np.ndarray, interaction: float, number: int,
                       centered: bool) -> np.ndarray:
    edges, _, _ = cube_geometry()
    basis = sector_basis(8, number)
    lookup = {s: i for i, s in enumerate(basis)}
    out = np.zeros((len(basis), len(basis)), dtype=complex)
    for col, state in enumerate(basis):
        for j in range(8):
            if not (state >> j) & 1:
                continue
            after = state ^ (1 << j)
            ann_sign = -1 if (state & ((1 << j) - 1)).bit_count() % 2 else 1
            for i in range(8):
                if abs(h[i, j]) == 0 or (after >> i) & 1:
                    continue
                cre_sign = -1 if (after & ((1 << i) - 1)).bit_count() % 2 else 1
                out[lookup[after | (1 << i)], col] += h[i, j] * ann_sign * cre_sign
        occupations = np.array([(state >> i) & 1 for i in range(8)], dtype=float)
        if centered:
            occupations -= 0.5
        out[col, col] += interaction * sum(occupations[i] * occupations[j]
                                           for i, j in edges)
    return out


def random_cube_field(rng: np.random.Generator) -> np.ndarray:
    edges, _, _ = cube_geometry()
    h = np.zeros((8, 8), dtype=complex)
    for i, j in edges:
        h[i, j] = -np.exp(1j * rng.uniform(-np.pi, np.pi))
        h[j, i] = h[i, j].conjugate()
    return h


def gauge_cube_crossing(h: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    _, left, right = cube_geometry()
    phases = np.ones(8, dtype=complex)
    for l, r in zip(left, right):
        phases[r] = -h[l, r].conjugate()
    gauged = phases.conjugate()[:, None] * h * phases[None, :]
    return gauged, phases


def ground_energy(h: np.ndarray, interaction: float, number: int = 4,
                  centered: bool = True) -> float:
    return float(np.linalg.eigvalsh(sector_hamiltonian(
        h, interaction, number, centered))[0])


def check_car(gates: Gates) -> None:
    rng = np.random.default_rng(67123)
    margins, hermitian, gauge_residual, crossing = [], 0.0, 0.0, 0.0
    shift_residual = 0.0
    _, left, right = cube_geometry()
    for _ in range(12):
        original = random_cube_field(rng)
        h, _ = gauge_cube_crossing(original)
        crossing = max(crossing, max(abs(h[l, r] + 1.0) for l, r in zip(left, right)))
        hll, hrr = h[np.ix_(left, left)], h[np.ix_(right, right)]
        reflected_left, reflected_right = h.copy(), h.copy()
        reflected_left[np.ix_(right, right)] = -hll
        reflected_right[np.ix_(left, left)] = -hrr
        hermitian = max(hermitian, *(np.linalg.norm(x - x.conj().T)
                                    for x in (h, reflected_left, reflected_right)))
        for interaction in (0.0, 0.2, 2.0, 12.0):
            original_energy = ground_energy(original, interaction)
            gauged_energy = ground_energy(h, interaction)
            gauge_residual = max(gauge_residual, abs(original_energy - gauged_energy))
            left_energy = ground_energy(reflected_left, interaction)
            right_energy = ground_energy(reflected_right, interaction)
            margins.append(gauged_energy - 0.5 * (left_energy + right_energy))
            centered = sector_hamiltonian(h, interaction, 4, True)
            uncentered = sector_hamiltonian(h, interaction, 4, False)
            shift_residual = max(shift_residual, np.linalg.norm(
                centered - uncentered + 3.0 * interaction * np.eye(70)))
    gates.check("CAR crossing gauge and Hermiticity",
                max(crossing, hermitian, gauge_residual) < TOL,
                f"fields=12 cross={crossing:.2e} herm={hermitian:.2e} gauge={gauge_residual:.2e}")
    gates.check("CAR fixed-half reflection inequality", min(margins) >= -TOL,
                f"cases=48 dim=70 min_margin={min(margins):.9g}")
    gates.check("CAR centered/uncentered N=4 shift", shift_residual < TOL,
                f"shift=-3V max_matrix_residual={shift_residual:.2e}")


def site_index(coord: tuple[int, int, int], lengths: tuple[int, int, int]) -> int:
    return int(np.ravel_multi_index(coord, lengths))


def step(coord: tuple[int, int, int], axis: int,
         lengths: tuple[int, int, int]) -> tuple[int, int, int]:
    out = list(coord)
    out[axis] = (out[axis] + 1) % lengths[axis]
    return tuple(out)


def link(coord: tuple[int, int, int], axis: int, lengths: tuple[int, int, int],
         twists: tuple[int, int, int]) -> int:
    x, y, _ = coord
    value = (1, (-1) ** x, (-1) ** (x + y))[axis]
    return value * (twists[axis] if coord[axis] == lengths[axis] - 1 else 1)


def ks_hopping(lengths: tuple[int, int, int], twists: tuple[int, int, int]) -> np.ndarray:
    validate_domain(lengths, 0.0)
    volume = int(np.prod(lengths))
    h = np.zeros((volume, volume), dtype=float)
    for coord in itertools.product(*(range(n) for n in lengths)):
        for axis in range(3):
            nxt = step(coord, axis, lengths)
            i, j = site_index(coord, lengths), site_index(nxt, lengths)
            h[i, j] = h[j, i] = -float(link(coord, axis, lengths, twists))
    return h


def bloch_spectrum(lengths: tuple[int, int, int],
                   twists: tuple[int, int, int]) -> np.ndarray:
    values = []
    grids = []
    for length, twist in zip(lengths, twists):
        delta = 0.5 if twist == -1 else 0.0
        grids.append([2 * np.pi * (m + delta) / length for m in range(length // 2)])
    for momentum in itertools.product(*grids):
        energy = 2 * np.sqrt(sum(np.cos(k) ** 2 for k in momentum))
        values.extend([-energy] * 4 + [energy] * 4)
    return np.sort(values)


def flux_wilson_residual(lengths: tuple[int, int, int],
                         twists: tuple[int, int, int]) -> tuple[float, float, int, int]:
    plaquette, wilson, pc, wc = 0.0, 0.0, 0, 0
    for coord in itertools.product(*(range(n) for n in lengths)):
        for a, b in itertools.combinations(range(3), 2):
            flux = (link(coord, a, lengths, twists)
                    * link(step(coord, a, lengths), b, lengths, twists)
                    * link(step(coord, b, lengths), a, lengths, twists)
                    * link(coord, b, lengths, twists))
            plaquette = max(plaquette, abs(flux + 1.0)); pc += 1
    for axis in range(3):
        others = [a for a in range(3) if a != axis]
        for transverse in itertools.product(*(range(lengths[a]) for a in others)):
            coord = [0, 0, 0]
            for a, value in zip(others, transverse):
                coord[a] = value
            product = 1
            for _ in range(lengths[axis]):
                product *= link(tuple(coord), axis, lengths, twists)
                coord[axis] = (coord[axis] + 1) % lengths[axis]
            wilson = max(wilson, abs(product - twists[axis])); wc += 1
    return plaquette, wilson, pc, wc


def canonical_twists(lengths: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple((-1) ** (length // 2 - 1) for length in lengths)


def validate_domain(lengths: tuple[int, int, int], interaction: float) -> None:
    if any(length < 4 or length % 2 for length in lengths):
        raise ValueError("simple tori require even lengths at least four")
    if interaction < 0:
        raise ValueError("reflection theorem requires repulsion V >= 0")


def undirected_edge(i: int, j: int) -> tuple[int, int]:
    return (i, j) if i < j else (j, i)


def geometry_certificate(lengths: tuple[int, int, int]) -> tuple[bool, int, int]:
    validate_domain(lengths, 0.0)
    coords = list(itertools.product(*(range(n) for n in lengths)))
    edges = {undirected_edge(site_index(c, lengths), site_index(step(c, a, lengths), lengths))
             for c in coords for a in range(3)}
    cycles: set[frozenset[tuple[int, int]]] = set()
    for c in coords:
        for a, b in itertools.combinations(range(3), 2):
            points = [c, step(c, a, lengths), step(step(c, a, lengths), b, lengths),
                      step(c, b, lengths)]
            cycles.add(frozenset(undirected_edge(site_index(points[k], lengths),
                                                  site_index(points[(k + 1) % 4], lengths))
                                    for k in range(4)))
    for axis in range(3):
        others = [a for a in range(3) if a != axis]
        for transverse in itertools.product(*(range(lengths[a]) for a in others)):
            c = [0, 0, 0]
            for a, value in zip(others, transverse): c[a] = value
            points = []
            for position in range(lengths[axis]):
                c[axis] = position; points.append(tuple(c))
            cycles.add(frozenset(undirected_edge(site_index(points[k], lengths),
                                                  site_index(points[(k + 1) % len(points)], lengths))
                                    for k in range(len(points))))
    cut_count, ok = 0, True
    for axis in range(3):
        def reflect_index(index: int) -> int:
            c = list(np.unravel_index(index, lengths))
            c[axis] = (1 - c[axis]) % lengths[axis]
            return site_index(tuple(c), lengths)
        mapped_edges = {undirected_edge(reflect_index(i), reflect_index(j)) for i, j in edges}
        ok &= mapped_edges == edges
        cuts = {undirected_edge(site_index(c, lengths), site_index(step(c, axis, lengths), lengths))
                for c in coords if c[axis] in (0, lengths[axis] // 2)}
        for cycle in cycles:
            image = frozenset(undirected_edge(reflect_index(i), reflect_index(j))
                              for i, j in cycle)
            ok &= image in cycles
            if cycle & cuts:
                cut_count += 1
                ok &= image == cycle
    return ok, len(cycles), cut_count


def check_tori(gates: Gates) -> None:
    sizes = [(4, 4, 4), (4, 4, 6), (6, 6, 6), (4, 6, 8)]
    fields = [((4, 4, 4), t) for t in itertools.product((-1, 1), repeat=3)]
    fields += [((6, 6, 6), t) for t in itertools.product((-1, 1), repeat=3)]
    fields += [(lengths, canonical_twists(lengths)) for lengths in sizes[1::2]]
    flux_residual = wilson_residual = spectrum_residual = 0.0
    plaquettes = wilsons = 0
    for lengths, twists in fields:
        flux, wilson, pc, wc = flux_wilson_residual(lengths, twists)
        flux_residual, wilson_residual = max(flux_residual, flux), max(wilson_residual, wilson)
        plaquettes += pc; wilsons += wc
        spectrum_residual = max(spectrum_residual, np.max(np.abs(
            np.linalg.eigvalsh(ks_hopping(lengths, twists)) - bloch_spectrum(lengths, twists))))
    flux_wilson = max(flux_residual, wilson_residual)
    gates.check("KS plaquettes and Wilson loops", flux_wilson < TOL,
                f"fields={len(fields)} plaquettes={plaquettes} loops={wilsons} residual={flux_wilson:.3e}")
    gates.check("KS direct/Bloch spectra", spectrum_residual < TOL,
                f"all8twists=4^3,6^3 max_residual={spectrum_residual:.3e}")
    gap_residual, canonical_min = 0.0, np.inf
    for lengths in sizes:
        spectrum = np.linalg.eigvalsh(ks_hopping(lengths, canonical_twists(lengths)))
        observed = np.min(np.abs(spectrum))
        predicted = 2 * np.sqrt(sum(np.sin(np.pi / length) ** 2 for length in lengths))
        gap_residual = max(gap_residual, abs(observed - predicted)); canonical_min = min(canonical_min, observed)
    gates.check("canonical finite-volume gap", gap_residual < TOL and canonical_min > TOL,
                f"sizes=4^3,4x4x6,6^3,4x6x8 min_gap={canonical_min:.9g} formula_res={gap_residual:.2e}")
    length = (4, 4, 4)
    periodic = np.linalg.eigvalsh(ks_hopping(length, (1, 1, 1)))
    canonical = np.linalg.eigvalsh(ks_hopping(length, canonical_twists(length)))
    half = len(periodic) // 2
    energy_delta = np.sum(periodic[:half]) - np.sum(canonical[:half])
    nodes = int(np.count_nonzero(np.abs(periodic) < TOL))
    mismatch = canonical_twists(length) != (1, 1, 1)
    gates.check("mutation rejects all-periodic 4^3", mismatch and nodes > 0 and energy_delta > TOL,
                f"zero_modes={nodes} E_periodic-E_canonical={energy_delta:.9g}")
    certs = [geometry_certificate(lengths) for lengths in sizes]
    gates.check("finite reflection/cycle geometry", all(c[0] for c in certs),
                f"sizes=4 cycles={sum(c[1] for c in certs)} cut_cycles={sum(c[2] for c in certs)}")


def check_boundaries(gates: Gates) -> None:
    h = np.zeros((8, 8), dtype=complex)
    residuals, shifts = [], []
    for number in (2, 4):
        centered = sector_hamiltonian(h, 1.0, number, True)
        uncentered = sector_hamiltonian(h, 1.0, number, False)
        expected = 3.0 - 1.5 * number
        residuals.append(np.linalg.norm(centered - uncentered - expected * np.eye(len(centered))))
        shifts.append(expected)
    gates.check("fixed-N versus full-Fock centering", max(residuals) < TOL and shifts[0] != shifts[1],
                f"cube shifts N=2:{shifts[0]:g}, N=4:{shifts[1]:g} max_res={max(residuals):.2e}")
    rejected = 0
    constructors = (lambda lengths: ks_hopping(lengths, (1, 1, 1)), geometry_certificate)
    for constructor, lengths in itertools.product(constructors, ((3, 4, 4), (2, 4, 4))):
        try:
            constructor(lengths)
        except ValueError:
            rejected += 1
    try:
        validate_domain((4, 4, 4), -0.1)
    except ValueError:
        rejected += 1
    gates.check("domain guards", rejected == 5,
                f"rejected={rejected}/5 (KS/geometry odd,length2; V<0)")


def main() -> int:
    np.set_printoptions(precision=10)
    gates = Gates()
    print("fixed-half cubic repulsive-flux finite diagnostics")
    check_polar(gates)
    check_car(gates)
    check_tori(gates)
    check_boundaries(gates)
    print(f"TOTAL: PASS={gates.passed} FAIL={gates.failed}")
    return 1 if gates.failed else 0


if __name__ == "__main__":
    sys.exit(main())
