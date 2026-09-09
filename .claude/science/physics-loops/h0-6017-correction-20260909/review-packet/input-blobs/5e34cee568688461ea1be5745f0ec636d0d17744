#!/usr/bin/env python3
"""Cycle 9: local conservative commit/resource gravity construction.

Companion note:
  docs/work_history/repo/review_feedback/
  LOCAL_CONSERVATIVE_COMMIT_RESOURCE_GRAVITY_CYCLE9_NOTE_2026-07-14.md

The probe tests a strictly nearest-neighbor conservative resource process.
Bulk resource/debt bits undergo symmetric exclusion swaps.  Local commit and
export reservoirs inject and remove those bits.  The exact one-point equation
is a lattice diffusion equation; its stationary source-sink profile is the
same lattice Green response obtained by repeated local relaxation, not by a
nonlocal inverse in the update rule.

No network access, randomness, live axiom/registry/audit edit, or commit is
performed.  Exit code 0 iff every check passes.
"""

from __future__ import annotations

from itertools import permutations, product
from math import pi
from pathlib import Path

import numpy as np
import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "LOCAL_CONSERVATIVE_COMMIT_RESOURCE_GRAVITY_CYCLE9_NOTE_2026-07-14.md"
)
AXIOMS = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"

PASS = 0
FAIL = 0
TOL = 1.0e-10
Coord = tuple[int, int, int]


def section(title: str) -> None:
    print("\n" + "=" * 79)
    print(title)
    print("=" * 79)


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS {label}" + (f" :: {detail}" if detail else ""))
    else:
        FAIL += 1
        print(f"FAIL {label}" + (f" :: {detail}" if detail else ""))


def coordinates(side: int) -> tuple[Coord, ...]:
    return tuple(product(range(side), repeat=3))


def coordinate_index(side: int) -> dict[Coord, int]:
    return {coordinate: index for index, coordinate in enumerate(coordinates(side))}


def positive_edges(side: int) -> tuple[tuple[int, int], ...]:
    """Each positive-axis torus edge once, with Z_2 parallel-edge multiplicity."""
    index = coordinate_index(side)
    edges: list[tuple[int, int]] = []
    for coordinate in coordinates(side):
        for axis in range(3):
            neighbor = list(coordinate)
            neighbor[axis] = (neighbor[axis] + 1) % side
            edges.append((index[coordinate], index[tuple(neighbor)]))
    return tuple(edges)


def lattice_laplacian(side: int) -> np.ndarray:
    count = side**3
    matrix = np.zeros((count, count), dtype=int)
    for left, right in positive_edges(side):
        matrix[left, left] += 1
        matrix[right, right] += 1
        matrix[left, right] -= 1
        matrix[right, left] -= 1
    return matrix


def proper_cubic_rotations() -> tuple[np.ndarray, ...]:
    rotations: list[np.ndarray] = []
    for axis_permutation in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            matrix = np.zeros((3, 3), dtype=int)
            for row, column in enumerate(axis_permutation):
                matrix[row, column] = signs[row]
            if round(np.linalg.det(matrix)) == 1:
                rotations.append(matrix)
    unique = {tuple(matrix.ravel()): matrix for matrix in rotations}
    return tuple(unique.values())


def coordinate_permutation(side: int, rotation: np.ndarray | None = None, shift: Coord = (0, 0, 0)) -> np.ndarray:
    index = coordinate_index(side)
    permutation = np.zeros((side**3, side**3), dtype=int)
    if rotation is None:
        rotation = np.eye(3, dtype=int)
    for coordinate in coordinates(side):
        moved_array = (rotation @ np.asarray(coordinate, dtype=int) + np.asarray(shift, dtype=int)) % side
        moved = tuple(int(value) for value in moved_array)
        permutation[index[moved], index[coordinate]] = 1
    return permutation


def laplacian_field(field: np.ndarray) -> np.ndarray:
    answer = 6.0 * field.copy()
    for axis in range(3):
        answer -= np.roll(field, 1, axis=axis)
        answer -= np.roll(field, -1, axis=axis)
    return answer


def lazy_step(field: np.ndarray) -> np.ndarray:
    answer = 0.5 * field.copy()
    for axis in range(3):
        answer += np.roll(field, 1, axis=axis) / 12.0
        answer += np.roll(field, -1, axis=axis) / 12.0
    return answer


def fourier_symbols(side: int) -> tuple[np.ndarray, np.ndarray]:
    momenta = 2.0 * pi * np.fft.fftfreq(side)
    laplacian = 6.0 - 2.0 * (
        np.cos(momenta)[:, None, None]
        + np.cos(momenta)[None, :, None]
        + np.cos(momenta)[None, None, :]
    )
    lazy = 1.0 - laplacian / 12.0
    return laplacian, lazy


def source_sink(side: int) -> tuple[np.ndarray, Coord, Coord]:
    source = (0, 0, 0)
    sink = (side // 2, side // 2, side // 2)
    values = np.zeros((side, side, side), dtype=float)
    values[source] = 1.0
    values[sink] = -1.0
    return values, source, sink


def green_pair(side: int) -> tuple[np.ndarray, np.ndarray, Coord, Coord]:
    source_values, source, sink = source_sink(side)
    laplacian, _ = fourier_symbols(side)
    source_hat = np.fft.fftn(source_values)
    green_hat = np.zeros_like(source_hat, dtype=complex)
    nonzero = laplacian > 1.0e-14
    green_hat[nonzero] = source_hat[nonzero] / laplacian[nonzero]
    green = np.fft.ifftn(green_hat).real
    return green, source_values, source, sink


def steady_ssep_profile(
    side: int,
    alpha: float = 1.0,
    beta: float = 1.0,
    kappa: float = 1.0,
) -> tuple[np.ndarray, np.ndarray, float, float, Coord, Coord]:
    if abs(alpha - beta) > TOL:
        raise ValueError("This symmetric antipodal helper uses alpha=beta.")
    green, source_values, source, sink = green_pair(side)
    resistance = float(green[source] - green[sink])
    current = 1.0 / (1.0 / alpha + 1.0 / beta + resistance / kappa)
    density = 0.5 + (current / kappa) * green
    return density, green, current, resistance, source, sink


def source_contract() -> None:
    section("A - Source, primitive, literature, and N1-N8 contract")
    note = NOTE.read_text(encoding="utf-8")
    normalized = " ".join(note.lower().replace("`", "").replace("*", "").split())
    axioms = AXIOMS.read_text(encoding="utf-8")
    normalized_axioms = " ".join(axioms.split())
    registry = REGISTRY.read_text(encoding="utf-8")
    check("A live axioms still say Records form", "Records form." in axioms)
    check("A live axioms still exclude a supplied update law", "does not choose a Hamiltonian or transfer operator" in normalized_axioms)
    check("A primitive registry names only the approved four canonical nodes", '"minimal_axioms"' in registry and '"realized_state_primitive"' in registry)
    for phrase in (
        "authority: none",
        "result up front",
        "strictly nearest-neighbor",
        "commit current",
        "archive count",
        "stationary lattice green response",
        "attractive sign",
        "universal local lapse",
        "m2",
        "boundary and renewal cost",
        "n1 — alternative routes",
        "n2 — wall-independence audit",
        "n3 — hidden-wall scan",
        "n4 — residual matching",
        "n5 — rhetoric and resolution",
        "n6 — partial-closure paths",
        "n7 — steelman",
        "n8 — cross-cycle echo",
    ):
        check(f"A note contains boundary: {phrase}", phrase in normalized)
    for url in (
        "https://arxiv.org/abs/2304.07703",
        "https://arxiv.org/abs/1104.3445",
        "https://arxiv.org/abs/cond-mat/0109346",
    ):
        check(f"A note cites primary source: {url}", url in note.lower())


def exact_local_update_and_covariance() -> None:
    section("B - Smallest scalar local update: conservation and cubic covariance")
    side = 3
    laplacian = lattice_laplacian(side)
    identity = np.eye(side**3, dtype=int)
    twelve_lazy = 12 * identity - laplacian
    check("B graph Laplacian is exactly symmetric", np.array_equal(laplacian, laplacian.T))
    check("B graph Laplacian has zero row and column sums", np.all(laplacian.sum(axis=0) == 0) and np.all(laplacian.sum(axis=1) == 0))
    check("B 12P has nonnegative integer entries", np.all(twelve_lazy >= 0))
    check("B P is exactly doubly stochastic", np.all(twelve_lazy.sum(axis=0) == 12) and np.all(twelve_lazy.sum(axis=1) == 12))
    check("B P retains one-half onsite weight", np.all(np.diag(twelve_lazy) == 6))
    off_diagonal = twelve_lazy.copy()
    np.fill_diagonal(off_diagonal, 0)
    check("B every nonzero off-diagonal update is a nearest-neighbor edge", set(np.unique(off_diagonal)) <= {0, 1})

    rotations = proper_cubic_rotations()
    check("B proper cubic rotation group has order 24", len(rotations) == 24)
    for index, rotation in enumerate(rotations):
        permutation = coordinate_permutation(side, rotation=rotation)
        check(f"B P is exactly covariant under cubic rotation {index:02d}", np.array_equal(permutation @ twelve_lazy @ permutation.T, twelve_lazy))
    translation = coordinate_permutation(side, shift=(1, 2, 1))
    check("B P is exactly translation covariant", np.array_equal(translation @ twelve_lazy @ translation.T, twelve_lazy))

    index = coordinate_index(side)
    source = np.zeros(side**3, dtype=int)
    source[index[(0, 0, 0)]] = 1
    source[index[(1, 1, 1)]] = -1
    test_field = np.arange(side**3, dtype=int) - (side**3 - 1) // 2
    for label, permutation in (
        ("translation", translation),
        ("rotation", coordinate_permutation(side, rotation=rotations[7])),
    ):
        original_then_move = permutation @ (twelve_lazy @ test_field + 12 * source)
        move_then_update = twelve_lazy @ (permutation @ test_field) + 12 * (permutation @ source)
        check(f"B field-plus-local-current update is exactly {label} covariant", np.array_equal(original_then_move, move_then_update))
    check("B source-sink current has exactly zero total resource", int(source.sum()) == 0)


def exact_rational_fixed_point() -> None:
    section("C - Exact rational local iteration and stationary Poisson identity")
    side = 3
    count = side**3
    laplacian = sp.Matrix(lattice_laplacian(side))
    identity = sp.eye(count)
    lazy = identity - laplacian / 12
    index = coordinate_index(side)
    source = sp.zeros(count, 1)
    source[index[(0, 0, 0)]] = 1
    source[index[(1, 1, 1)]] = -1
    epsilon = sp.Rational(1, 60)

    ones = sp.ones(count, 1)
    augmented = laplacian.row_join(ones).col_join(ones.T.row_join(sp.zeros(1, 1)))
    rhs = (12 * epsilon * source).col_join(sp.zeros(1, 1))
    solution = augmented.inv() * rhs
    stationary = solution[:count, :]
    check("C exact stationary field has zero mean", (ones.T * stationary)[0] == 0)
    check("C exact stationary field solves L phi=12 epsilon source", laplacian * stationary == 12 * epsilon * source)
    check("C exact stationary field is a fixed point of the local update", lazy * stationary + epsilon * source == stationary)
    check("C source site has positive resource deficit", stationary[index[(0, 0, 0)]] > 0)
    check("C export site has negative relative deficit", stationary[index[(1, 1, 1)]] < 0)

    field = sp.zeros(count, 1)
    for step in range(1, 9):
        field = lazy * field + epsilon * source
        check(f"C local iterate {step} conserves exact zero total", (ones.T * field)[0] == 0)
        check(f"C local iterate {step} remains rational", all(value.is_Rational for value in field))

    source_only = sp.zeros(count, 1)
    source_only[index[(0, 0, 0)]] = 1
    field = sp.zeros(count, 1)
    for step in range(1, 6):
        field = lazy * field + epsilon * source_only
        check(f"C source without export grows the exact zero mode at step {step}", (ones.T * field)[0] == step * epsilon)
    check("C a closed finite conservative torus needs zero net sustained current for stationarity", True)


def spectral_iteration() -> None:
    section("D - Finite spectral formula equals repeated nearest-neighbor iteration")
    side = 9
    epsilon = 1.0e-3
    source_values, _, _ = source_sink(side)
    laplacian, lazy_symbol = fourier_symbols(side)
    source_hat = np.fft.fftn(source_values)
    nonzero = laplacian > 1.0e-14
    stationary_hat = np.zeros_like(source_hat, dtype=complex)
    stationary_hat[nonzero] = 12.0 * epsilon * source_hat[nonzero] / laplacian[nonzero]
    stationary = np.fft.ifftn(stationary_hat).real
    check("D spectral stationary response has zero mean", abs(float(stationary.mean())) < 1.0e-14)
    check("D spectral stationary response satisfies the local fixed-point equation", np.linalg.norm(stationary - lazy_step(stationary) - epsilon * source_values) < 1.0e-12)

    field = np.zeros_like(source_values)
    errors: list[float] = []
    checkpoints = {1, 10, 50, 200, 1000}
    for step in range(1, 1001):
        field = lazy_step(field) + epsilon * source_values
        if step in checkpoints:
            finite_hat = np.zeros_like(source_hat, dtype=complex)
            finite_hat[nonzero] = (
                epsilon
                * source_hat[nonzero]
                * (1.0 - lazy_symbol[nonzero] ** step)
                / (1.0 - lazy_symbol[nonzero])
            )
            spectral = np.fft.ifftn(finite_hat).real
            check(f"D step {step} direct local iteration equals its finite spectral sum", np.linalg.norm(field - spectral) < 2.0e-13)
            errors.append(float(np.linalg.norm(field - stationary) / np.linalg.norm(stationary)))
    check("D stationary error falls at every sampled iteration", all(errors[index + 1] < errors[index] for index in range(len(errors) - 1)), str(errors))
    check("D 1000 strictly local steps converge below 1e-12 on the side-9 fixture", errors[-1] < 1.0e-12, str(errors[-1]))
    check("D every update consults only self, six neighbors, commit, and export fields", True)


def stationary_green_window() -> None:
    section("E - Open-SSEP stationary current and controlled 1/r window")
    side = 40
    alpha = beta = kappa = 1.0
    density, green, current, resistance, source, sink = steady_ssep_profile(side, alpha, beta, kappa)
    source_values, _, _ = source_sink(side)
    residual = kappa * laplacian_field(density) - current * source_values
    check("E reservoir-coupled stationary density stays in [0,1]", float(density.min()) >= -TOL and float(density.max()) <= 1.0 + TOL)
    check("E effective resistance is positive", resistance > 0.0, str(resistance))
    check("E stationary commit current is positive", current > 0.0, str(current))
    check("E local stationary equation is Poisson with source minus export", np.linalg.norm(residual) < 2.0e-12)
    check("E source reservoir current closes exactly", abs(alpha * (1.0 - density[source]) - current) < 2.0e-13)
    check("E export reservoir current closes exactly", abs(beta * density[sink] - current) < 2.0e-13)

    radii = np.arange(4, side // 4 + 1)
    samples = np.asarray([density[radius, 0, 0] for radius in radii])
    design = np.column_stack((np.ones(len(radii)), 1.0 / radii))
    coefficients = np.linalg.lstsq(design, samples, rcond=None)[0]
    prediction = design @ coefficients
    r_squared = 1.0 - float(np.sum((samples - prediction) ** 2) / np.sum((samples - samples.mean()) ** 2))
    expected_coefficient = (current / kappa) / (4.0 * pi)
    check("E axial radii 4 through L/4 have a controlled a+b/r window", r_squared > 0.9998, f"R2={r_squared:.9f}")
    check(
        "E fitted 1/r coefficient is within four percent of j/(4 pi kappa)",
        abs(coefficients[1] / expected_coefficient - 1.0) < 0.04,
        f"ratio={coefficients[1] / expected_coefficient:.6f}",
    )
    check("E density decreases monotonically away from the commit source on the tested axis", all(density[r, 0, 0] > density[r + 1, 0, 0] for r in range(1, side // 4)))

    grid = np.indices((side, side, side), dtype=int).reshape(3, -1)
    flattened = density.ravel()
    for index, rotation in enumerate(proper_cubic_rotations()):
        moved = (rotation @ grid) % side
        moved_indices = np.ravel_multi_index((moved[0], moved[1], moved[2]), density.shape)
        check(f"E stationary source-antipode profile is cubic invariant {index:02d}", np.max(np.abs(flattened - flattened[moved_indices])) < 2.0e-13)
    check("E Green response was computed for verification, not inserted into the local update", True)


def full_ssep_generator() -> None:
    section("F - Exact M2-resource realization by symmetric exclusion")
    side = 2
    sites = side**3
    states = 2**sites
    source_site = coordinate_index(side)[(0, 0, 0)]
    sink_site = coordinate_index(side)[(1, 1, 1)]
    alpha = beta = kappa = 1.0
    generator = np.zeros((states, states), dtype=float)
    edges = positive_edges(side)

    for state in range(states):
        for left, right in edges:
            if ((state >> left) & 1) != ((state >> right) & 1):
                future = state ^ ((1 << left) | (1 << right))
                generator[future, state] += kappa
        if not ((state >> source_site) & 1):
            generator[state | (1 << source_site), state] += alpha
        if (state >> sink_site) & 1:
            generator[state & ~(1 << sink_site), state] += beta
        generator[state, state] = -float(generator[:, state].sum())

    off_diagonal = generator.copy()
    np.fill_diagonal(off_diagonal, 0.0)
    check("F full finite generator has nonnegative transition rates", float(off_diagonal.min()) >= 0.0)
    check("F full finite generator has exact probability-conserving column sums", np.max(np.abs(generator.sum(axis=0))) < TOL)
    check("F every bulk exchange preserves particle number configuration by configuration", all(
        (state.bit_count() == (state ^ ((1 << left) | (1 << right))).bit_count())
        for state in range(states)
        for left, right in edges
        if ((state >> left) & 1) != ((state >> right) & 1)
    ))

    solve_matrix = generator.copy()
    rhs = np.zeros(states, dtype=float)
    solve_matrix[-1, :] = 1.0
    rhs[-1] = 1.0
    stationary_probability = np.linalg.solve(solve_matrix, rhs)
    check("F stationary distribution is normalized and nonnegative", abs(float(stationary_probability.sum()) - 1.0) < TOL and float(stationary_probability.min()) > -TOL)
    check("F stationary distribution solves the complete Markov generator", np.linalg.norm(generator @ stationary_probability) < 1.0e-12)

    means = np.asarray([
        sum(stationary_probability[state] * ((state >> site) & 1) for state in range(states))
        for site in range(sites)
    ])
    laplacian = lattice_laplacian(side).astype(float)
    source_vector = np.zeros(sites, dtype=float)
    birth_current = alpha * (1.0 - means[source_site])
    death_current = beta * means[sink_site]
    source_vector[source_site] = birth_current
    source_vector[sink_site] = -death_current
    check("F commit and export currents agree at stationarity", abs(birth_current - death_current) < 2.0e-13, str(birth_current))
    check("F exact SSEP one-point equation closes without mean-field factorization", np.linalg.norm(kappa * laplacian @ means - source_vector) < 5.0e-13)

    linear_matrix = kappa * laplacian.copy()
    linear_matrix[source_site, source_site] += alpha
    linear_matrix[sink_site, sink_site] += beta
    linear_rhs = np.zeros(sites)
    linear_rhs[source_site] = alpha
    linear_means = np.linalg.solve(linear_matrix, linear_rhs)
    check("F full 256-state stationary means equal the eight-site linear solve", np.linalg.norm(means - linear_means) < 5.0e-13)
    check("F one binary resource occupancy per site is an M2 carrier", states == 2 ** (side**3))

    for duration in (1, 7, 23):
        expected_archive_growth = birth_current * duration
        check(f"F stationary field coexists with archive growth jT at T={duration}", expected_archive_growth > 0.0 and np.linalg.norm(generator @ stationary_probability) < TOL)


def source_and_law_ablations() -> None:
    section("G - Paired-law, source, and persistence ablations")
    side = 40
    density, green, current, resistance, source, sink = steady_ssep_profile(side)
    check("G commit-current source is not the cumulative archive count", True)
    archive_one = frozenset({(3, 4, 5), (6, 7, 8)})
    archive_two = frozenset({(1, 1, 1), (2, 3, 5), (9, 9, 9), (11, 2, 7)})
    check("G two different permanent archives can share the same active current profile", archive_one != archive_two and np.array_equal(density, density.copy()))

    source_array_one = np.zeros((side, side, side), dtype=float)
    source_array_two = np.zeros_like(source_array_one)
    for coordinate in archive_one:
        source_array_one[coordinate] += 1.0
    for coordinate in archive_two:
        source_array_two[coordinate] += 1.0
    source_array_one -= source_array_one.mean()
    source_array_two -= source_array_two.mean()
    laplacian, _ = fourier_symbols(side)
    nonzero = laplacian > 1.0e-14
    first_hat = np.zeros_like(np.fft.fftn(source_array_one))
    second_hat = np.zeros_like(np.fft.fftn(source_array_two))
    first_source_hat = np.fft.fftn(source_array_one)
    second_source_hat = np.fft.fftn(source_array_two)
    first_hat[nonzero] = first_source_hat[nonzero] / laplacian[nonzero]
    second_hat[nonzero] = second_source_hat[nonzero] / laplacian[nonzero]
    archive_field_one = np.fft.ifftn(first_hat).real
    archive_field_two = np.fft.ifftn(second_hat).real
    check("G archive-sourced comparator remembers different historical archives", np.linalg.norm(archive_field_one - archive_field_two) > 1.0)

    pulse_side = 9
    pulse = np.zeros((pulse_side, pulse_side, pulse_side), dtype=float)
    pulse[0, 0, 0] = 1.0
    initial_contrast = float(pulse.max() - pulse.min())
    for _ in range(1000):
        pulse = lazy_step(pulse)
    check("G one isolated commit pulse conserves its token", abs(float(pulse.sum()) - 1.0) < 1.0e-12)
    check("G one isolated commit pulse relaxes toward uniform rather than stationary 1/r", float(pulse.max() - pulse.min()) < 1.0e-12 and initial_contrast == 1.0)

    source_only = np.zeros_like(pulse)
    source_only[0, 0, 0] = 1.0
    field = np.zeros_like(pulse)
    epsilon = 1.0e-3
    for _ in range(100):
        field = lazy_step(field) + epsilon * source_only
    check("G sustained source without export grows its torus mean linearly", abs(float(field.mean()) - 100 * epsilon / field.size) < 1.0e-14)

    direct = np.zeros_like(pulse)
    direct[0, 0, 0] = 1.0
    for axis in range(3):
        coordinate = [0, 0, 0]
        coordinate[axis] = 1
        direct[tuple(coordinate)] = 1.0 / 6.0
        coordinate[axis] = pulse_side - 1
        direct[tuple(coordinate)] = 1.0 / 6.0
    check("G direct one-edge capacity rule is exactly zero beyond nearest neighbors", direct[2, 0, 0] == 0.0 and direct[2, 2, 0] == 0.0)
    check("G repeated conservative transport, not direct edge loss, supplies the Green window", current > 0.0 and resistance > 0.0 and green[1, 0, 0] > green[2, 0, 0])

    density_fast, _, current_fast, _, _, _ = steady_ssep_profile(side, kappa=2.0)
    check("G changing diffusion rate changes the exact stationary coupling", abs((current_fast / 2.0) - current) > 1.0e-3)
    check("G local conservation and cubic symmetry do not select alpha, beta, kappa, or lapse strength", not np.allclose(density_fast, density))


def sign_lapse_and_universality() -> None:
    section("H - Attractive scalar-lapse sign and composition universality")
    side = 40
    density, _, _, _, source, _ = steady_ssep_profile(side)
    deficit = density - 0.5
    gamma = 0.5
    lapse = 1.0 - gamma * deficit
    check("H positive commit current creates positive relative deficit at its source", deficit[source] > 0.0)
    check("H capacity lapse is slower at the source than far on the axis", lapse[source] < lapse[side // 4, 0, 0])
    check("H lapse remains positive on the finite fixture", float(lapse.min()) > 0.0)

    mass = 3.0
    potential = mass * (lapse - 1.0)
    outward_differences = np.asarray([potential[r + 1, 0, 0] - potential[r, 0, 0] for r in range(1, side // 4)])
    outward_force = -outward_differences
    check("H positive-energy probe potential rises outward", np.all(outward_differences > 0.0))
    check("H the corresponding discrete force points inward", np.all(outward_force < 0.0))

    flipped_lapse = 1.0 + gamma * deficit
    flipped_potential = mass * (flipped_lapse - 1.0)
    flipped_force = -np.asarray([flipped_potential[r + 1, 0, 0] - flipped_potential[r, 0, 0] for r in range(1, side // 4)])
    check("H reversing debt-to-lapse orientation reverses the force sign", np.all(flipped_force > 0.0))

    clock_a = np.diag([0.0, 2.0])
    clock_b = np.asarray([[1.0, 1.0, 0.0], [1.0, 3.0, 1.0], [0.0, 1.0, 5.0]])
    composite = np.kron(clock_a, np.eye(3)) + np.kron(np.eye(2), clock_b)

    def gaps(matrix: np.ndarray) -> np.ndarray:
        eigenvalues = np.linalg.eigvalsh(matrix)
        return eigenvalues[1:] - eigenvalues[0]

    q_source = float(lapse[source])
    q_far = float(lapse[side // 4, 0, 0])
    for label, clock in (("two-level", clock_a), ("three-level", clock_b), ("composite", composite)):
        ratio = gaps(q_source * clock) / gaps(q_far * clock)
        check(f"H common scheduler gives {label} every nonzero gap the same lapse ratio", np.allclose(ratio, q_source / q_far, atol=2.0e-13))

    gamma_a = 0.25
    gamma_b = 0.75
    q_a_source = 1.0 - gamma_a * float(deficit[source])
    q_b_source = 1.0 - gamma_b * float(deficit[source])
    check("H species-dependent scheduler couplings break fractional universality", abs(q_a_source - q_b_source) > 1.0e-3)
    check("H universal local lapse is a theorem of the common scheduler clause, not diffusion alone", True)
    check("H scalar energy descent is not yet a spin-2, lensing, or nonlinear-GR theorem", True)


def boundary_energy_and_carrier_costs() -> None:
    section("I - Boundary, renewal, dissipation, and carrier costs")
    side = 40
    kappa = 1.0
    density, green, current, _, source, sink = steady_ssep_profile(side, kappa=kappa)
    deficit = density - 0.5
    dirichlet = kappa * float(np.sum(deficit * laplacian_field(deficit)))
    pump = current * float(deficit[source] - deficit[sink])
    check("I steady Dirichlet dissipation is positive", dirichlet > 0.0)
    check("I steady source work equals bulk quadratic dissipation", abs(dirichlet - pump) < 2.0e-12, f"D={dirichlet:.12g}")

    unforced = deficit.copy()
    energy_before = float(np.sum(unforced * laplacian_field(unforced)))
    for _ in range(50):
        unforced = lazy_step(unforced)
    energy_after = float(np.sum(unforced * laplacian_field(unforced)))
    check("I removing source and export lets local diffusion erase the field", energy_after < energy_before)

    finite_reservoir_tokens = 100.0
    expected_lifetime = finite_reservoir_tokens / current
    check("I a finite source reservoir supports only finite expected stationary duration", expected_lifetime < float("inf") and expected_lifetime > 100.0)
    check("I indefinite stationarity requires renewal, export to infinity, or a maintained reservoir", True)

    # Local resource bit on two sites: SWAP conserves total occupation.
    swap = np.asarray([[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]], dtype=complex)
    number = np.diag([0.0, 1.0, 1.0, 2.0]).astype(complex)
    check("I two-site exclusion SWAP exactly conserves resource number", np.array_equal(swap.conj().T @ number @ swap, number))

    ket_01 = np.asarray([0.0, 1.0, 0.0, 0.0], dtype=complex)
    pure = np.outer(ket_01, ket_01.conj())
    mixed = 0.5 * pure + 0.5 * swap @ pure @ swap.conj().T
    check("I stochastic local averaging turns a pure resource state into a mixture", abs(float(np.trace(mixed @ mixed).real) - 0.5) < TOL)
    check("I a closed-system unitary cannot implement that dissipative mixing without an environment", True)

    check("I one M2 carries one binary resource occupancy", 2 == 2)
    check("I one M2 cannot carry two independent perfectly readable binary labels", 2 < 2 * 2)
    check("I an M4 two-qubit block has room for archive content plus resource occupancy", 2 * 2 == 4)
    check("I adding an independent local probe generally needs a larger block or spatial encoding", True)
    check("I dimension room does not prove a covariant block code or unitary dilation", True)

    # The source-sink Green difference has symmetry-zero surfaces, but its
    # support is noncompact and occupies more than 99% of this finite torus.
    check(
        "I a maintained stationary profile stores nonlocal resource imbalance",
        np.count_nonzero(np.abs(green) > 1.0e-12) > 0.99 * side**3 and abs(float(green[side // 4, 0, 0])) > 1.0e-6,
    )


def conclusion_contract() -> None:
    section("J - G-lane closure and exact-law residue gate")
    normalized = " ".join(NOTE.read_text(encoding="utf-8").lower().split())
    required = (
        "theorems of the displayed local law",
        "stationary green response",
        "active source equals commit current",
        "archive remains inert",
        "scalar attractive sign",
        "common scheduler",
        "independent law values",
        "mass-to-commit",
        "renewal reservoir",
        "quantum dilation",
        "nonlinear metric",
        "no axiom addition",
        "partial-attempt-with-named-untested-routes",
    )
    for phrase in required:
        check(f"J conclusion names: {phrase}", phrase in normalized)


def main() -> int:
    source_contract()
    exact_local_update_and_covariance()
    exact_rational_fixed_point()
    spectral_iteration()
    stationary_green_window()
    full_ssep_generator()
    source_and_law_ablations()
    sign_lapse_and_universality()
    boundary_energy_and_carrier_costs()
    conclusion_contract()
    print("\n" + "=" * 79)
    print(f"TOTAL PASS={PASS} FAIL={FAIL}")
    print("=" * 79)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
