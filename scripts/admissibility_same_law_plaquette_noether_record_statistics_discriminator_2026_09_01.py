#!/usr/bin/env python3
"""Exact same-law matter -> Noether current -> permanent Record probe.

One square-lattice hopping expression is executed in CAR/Jordan-Wigner and
commuting hard-core realizations.  The runner proves exact operator continuity,
an all-cadence opposite-corner transfer separation, and a common even
target/complement Record instrument.  The result is finite and conditional:
the hopping action, initial state, cadence, calibration premise, pointer, and
formation map are not derived from the four minimal axioms.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import subprocess
from dataclasses import dataclass
from functools import reduce
from pathlib import Path
from typing import Callable

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
PACKET = (
    ".claude/science/physics-loops/"
    "toe-matter-noether-record-vertical-slice-block44-20260901"
)
PREREG_COMMIT = "a9094e2d1a3a30c90baea87814a871663fad509a"
MINIMAL_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
MINIMAL_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
FROZEN_PACKET_BLOBS = {
    f"{PACKET}/GOAL.md": "80738535930447bbb2ef8faa204067912e69b215",
    f"{PACKET}/EXACT_TARGET_CONTRACT.md": "fb14e79958ad95bf4e21c7e38862506b665bdf7a",
    f"{PACKET}/ASSUMPTIONS_AND_IMPORTS.md": "2dc7c9e8bf64201e3cb3f329fc0da15b792a2424",
    f"{PACKET}/ROUTE_PORTFOLIO.md": "7a289b86efd59ac8354eaac9044c6bbc7f7caea6",
    f"{PACKET}/MUTATION_PLAN.md": "868afbfdcf7e196a7e01b7b46771362e2f3a45f0",
    f"{PACKET}/OPPORTUNITY_QUEUE.md": "02a59e0177b763b711a478da52ea6f0cf610b578",
    f"{PACKET}/PRIOR_ART_SEARCH.md": "24bf446132cb7e0098739c5f5aca428962caa4a0",
}

# Current mutable inputs; original Git pins below remain historical identities.
AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = (
    'docs/MINIMAL_AXIOMS_2026-06-29.md',
    '.claude/science/physics-loops/toe-matter-noether-record-vertical-slice-block44-20260901/GOAL.md',
    '.claude/science/physics-loops/toe-matter-noether-record-vertical-slice-block44-20260901/EXACT_TARGET_CONTRACT.md',
    '.claude/science/physics-loops/toe-matter-noether-record-vertical-slice-block44-20260901/ASSUMPTIONS_AND_IMPORTS.md',
    '.claude/science/physics-loops/toe-matter-noether-record-vertical-slice-block44-20260901/ROUTE_PORTFOLIO.md',
    '.claude/science/physics-loops/toe-matter-noether-record-vertical-slice-block44-20260901/MUTATION_PLAN.md',
    '.claude/science/physics-loops/toe-matter-noether-record-vertical-slice-block44-20260901/OPPORTUNITY_QUEUE.md',
    '.claude/science/physics-loops/toe-matter-noether-record-vertical-slice-block44-20260901/PRIOR_ART_SEARCH.md',
    'docs/SAME_LAW_PLAQUETTE_NOETHER_RECORD_DISCRIMINATOR_BOUNDED_THEOREM_NOTE_2026-09-08.md',
)
CURRENT_NOTE_PATH = 'docs/SAME_LAW_PLAQUETTE_NOETHER_RECORD_DISCRIMINATOR_BOUNDED_THEOREM_NOTE_2026-09-08.md'
CURRENT_NOTE_SHA256 = 'f8dea921b6993a6b48a3824cbe1c6f68d07c0104d7a64e6d53aa5d9c3b296c64'

MUTATIONS = (
    "drop_edge_both",
    "drop_edge_hcb_only",
    "reverse_current_01",
    "delete_current_01",
    "drop_car_string_site3",
    "swap_car_to_hcb",
    "wrong_initial_occupancy",
    "target_adjacent_occupancy",
    "product_specific_writer",
    "pointer_relabel_changes_weight",
    "born_without_calibration",
    "zero_cadence_as_nontrivial",
    "arbitrary_K_family_fixed",
    "overwrite_pointer",
    "ordinary_site_permutation_for_car",
    "delete_edge_consistently",
    "d4_allows_flux",
)

I2 = sp.eye(2)
X = sp.Matrix([[0, 1], [1, 0]])
Z = sp.diag(1, -1)
SM = sp.Matrix([[0, 1], [0, 0]])
EDGES = ((0, 1), (1, 2), (2, 3), (3, 0))
TWO_PARTICLE_BASIS = (3, 5, 6, 9, 10, 12)


def kron_all(*matrices: sp.MatrixBase) -> sp.Matrix:
    return sp.Matrix(reduce(sp.kronecker_product, matrices, sp.Matrix([[1]])))


def matrix_zero(matrix: sp.MatrixBase) -> bool:
    return all(sp.simplify(value) == 0 for value in matrix)


def adjoint(matrix: sp.MatrixBase) -> sp.Matrix:
    return sp.Matrix(matrix.conjugate().T)


def ket(index: int, dimension: int) -> sp.Matrix:
    result = sp.zeros(dimension, 1)
    result[index, 0] = 1
    return result


def restrict(matrix: sp.MatrixBase, basis: tuple[int, ...]) -> sp.Matrix:
    return sp.Matrix(matrix).extract(basis, basis)


def git_blob(commit: str, path: str) -> str:
    return subprocess.run(
        ["git", "rev-parse", f"{commit}:{path}"],
        cwd=ROOT,
        check=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    ).stdout.strip()


def worktree_blob(path: str) -> str:
    return subprocess.run(
        ["git", "hash-object", path],
        cwd=ROOT,
        check=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    ).stdout.strip()


def annihilator(realization: str, site: int, mutation: str | None) -> sp.Matrix:
    use_car = realization == "car" and mutation != "swap_car_to_hcb"
    factors = []
    for position in range(4):
        string_here = use_car and position < site
        if mutation == "drop_car_string_site3" and site == 3 and position == 1:
            string_here = False
        if string_here:
            factors.append(Z)
        elif position == site:
            factors.append(SM)
        else:
            factors.append(I2)
    return kron_all(*factors)


def operators(realization: str, mutation: str | None) -> tuple[sp.Matrix, ...]:
    return tuple(annihilator(realization, site, mutation) for site in range(4))


def ordered_car_operators(order: tuple[int, int, int, int]) -> tuple[sp.Matrix, ...]:
    position = {site: index for index, site in enumerate(order)}
    result = []
    for site in range(4):
        predecessors = {
            candidate
            for candidate in range(4)
            if position[candidate] < position[site]
        }
        result.append(
            kron_all(
                *(
                    Z
                    if factor_site in predecessors
                    else SM
                    if factor_site == site
                    else I2
                    for factor_site in range(4)
                )
            )
        )
    return tuple(result)


def active_edges(realization: str, mutation: str | None) -> tuple[tuple[int, int], ...]:
    edges = EDGES
    if mutation in {"drop_edge_both", "delete_edge_consistently"}:
        edges = tuple(edge for edge in edges if set(edge) != {0, 1})
    if mutation == "drop_edge_hcb_only" and realization == "hcb":
        edges = tuple(edge for edge in edges if set(edge) != {0, 1})
    return edges


def hopping(realization: str, mutation: str | None) -> sp.Matrix:
    annihilators = operators(realization, mutation)
    result = sp.zeros(16)
    for left, right in active_edges(realization, mutation):
        a_left, a_right = annihilators[left], annihilators[right]
        result -= adjoint(a_left) * a_right + adjoint(a_right) * a_left
    return sp.Matrix(result)


def number_operators(realization: str, mutation: str | None) -> tuple[sp.Matrix, ...]:
    return tuple(adjoint(value) * value for value in operators(realization, mutation))


def oriented_current(
    realization: str, source: int, target: int, mutation: str | None
) -> sp.Matrix:
    annihilators = operators(realization, mutation)
    a_source, a_target = annihilators[source], annihilators[target]
    current = sp.I * (
        adjoint(a_target) * a_source - adjoint(a_source) * a_target
    )
    if set((source, target)) == {0, 1} and mutation == "reverse_current_01":
        current = -current
    if set((source, target)) == {0, 1} and mutation == "delete_current_01":
        current = sp.zeros(16)
    if set((source, target)) == {0, 1} and mutation == "delete_edge_consistently":
        current = sp.zeros(16)
    return sp.Matrix(current)


def occupation_projector(
    realization: str, bits: tuple[int, int, int, int], mutation: str | None
) -> sp.Matrix:
    result = sp.eye(16)
    for bit, number in zip(bits, number_operators(realization, mutation)):
        result *= number if bit else sp.eye(16) - number
    return sp.Matrix(result)


def bit_tuple(index: int) -> tuple[int, int, int, int]:
    return tuple((index >> (3 - site)) & 1 for site in range(4))


def bit_index(bits: tuple[int, int, int, int]) -> int:
    value = 0
    for bit in bits:
        value = 2 * value + bit
    return value


def permutation_sign(sequence: list[int]) -> int:
    inversions = sum(
        sequence[left] > sequence[right]
        for left in range(len(sequence))
        for right in range(left + 1, len(sequence))
    )
    return -1 if inversions % 2 else 1


def site_permutation_lift(
    permutation: tuple[int, int, int, int], fermionic: bool
) -> sp.Matrix:
    result = sp.zeros(16)
    for column in range(16):
        occupied = [
            site for site, bit in enumerate(bit_tuple(column)) if bit
        ]
        mapped = [permutation[site] for site in occupied]
        sign = permutation_sign(mapped) if fermionic else 1
        output_bits = [0, 0, 0, 0]
        for site in mapped:
            output_bits[site] = 1
        result[bit_index(tuple(output_bits)), column] = sign
    return sp.Matrix(result)


@dataclass
class Harness:
    passed: int = 0
    failed: int = 0

    def check(self, label: str, condition: bool, detail: str) -> None:
        if condition:
            self.passed += 1
            print(f"PASS {label} :: {detail}")
        else:
            self.failed += 1
            print(f"FAIL {label} :: {detail}")


def source_and_prereg_certificate(harness: Harness, mutation: str | None) -> None:
    pinned = sum(
        git_blob(PREREG_COMMIT, path) == blob
        for path, blob in FROZEN_PACKET_BLOBS.items()
    )
    unchanged = sum(
        worktree_blob(path) == blob for path, blob in FROZEN_PACKET_BLOBS.items()
    )
    minimal_bound = worktree_blob(MINIMAL_PATH) == MINIMAL_BLOB
    contract = (ROOT / PACKET / "EXACT_TARGET_CONTRACT.md").read_text()
    harness.check(
        "preregistration and foundation are source-bound",
        pinned == 7
        and unchanged == 7
        and minimal_bound
        and hashlib.sha256((ROOT / CURRENT_NOTE_PATH).read_bytes()).hexdigest() == CURRENT_NOTE_SHA256
        and "NEW_CONDITIONAL_CONNECTOR" in contract
        and "BACKLOG_NO_PR" in contract,
        f"prereg={pinned}/7 unchanged={unchanged}/7 minimal={minimal_bound}",
    )


def local_algebra_and_common_input_certificate(
    harness: Harness, mutation: str | None
) -> None:
    car = operators("car", mutation)
    hcb = operators("hcb", mutation)
    local_ok = all(matrix_zero(value * value) for value in car + hcb)
    number_ok = all(
        matrix_zero(adjoint(car[site]) * car[site] - adjoint(hcb[site]) * hcb[site])
        for site in range(4)
    )
    car_ok = all(
        matrix_zero(car[left] * car[right] + car[right] * car[left])
        and matrix_zero(car[left] * adjoint(car[right]) + adjoint(car[right]) * car[left])
        for left in range(4)
        for right in range(left + 1, 4)
    )
    hcb_ok = all(
        matrix_zero(hcb[left] * hcb[right] - hcb[right] * hcb[left])
        and matrix_zero(hcb[left] * adjoint(hcb[right]) - adjoint(hcb[right]) * hcb[left])
        for left in range(4)
        for right in range(left + 1, 4)
    )
    one_basis = (1, 2, 4, 8)
    car_one = restrict(hopping("car", mutation), one_basis)
    hcb_one = restrict(hopping("hcb", mutation), one_basis)
    square_ok = (
        len(active_edges("car", mutation)) == 4
        and len(active_edges("hcb", mutation)) == 4
        and matrix_zero(car_one - hcb_one)
        and car_one.eigenvals() == {-2: 1, 0: 2, 2: 1}
    )
    harness.check(
        "hostile twins share all declared local and one-particle input data",
        local_ok and number_ok and car_ok and hcb_ok and square_ok,
        f"nilpotent={local_ok} number_equal={number_ok} one_particle_equal={matrix_zero(car_one-hcb_one)}",
    )


def jordan_wigner_order_invariance_certificate(
    harness: Harness, mutation: str | None
) -> None:
    initial_position = TWO_PARTICLE_BASIS.index(10)
    target_position = TWO_PARTICLE_BASIS.index(5)
    results = []
    for order in itertools.permutations(range(4)):
        annihilators = ordered_car_operators(order)
        hamiltonian = sp.zeros(16)
        for source, target in EDGES:
            hamiltonian -= (
                adjoint(annihilators[source]) * annihilators[target]
                + adjoint(annihilators[target]) * annihilators[source]
            )
        two_particle = restrict(hamiltonian, TWO_PARTICLE_BASIS)
        relations = all(
            matrix_zero(
                annihilators[left] * annihilators[right]
                + annihilators[right] * annihilators[left]
            )
            for left in range(4)
            for right in range(left + 1, 4)
        )
        results.append(
            relations
            and two_particle.eigenvals() == {-2: 2, 0: 2, 2: 2}
            and matrix_zero(two_particle * (two_particle**2 - 4 * sp.eye(6)))
            and two_particle[target_position, initial_position] == 0
            and (two_particle**2)[target_position, initial_position] == 0
        )
    harness.check(
        "all 24 Jordan-Wigner orders retain CAR, the spectrum, and the dark opposite-corner amplitude",
        all(results),
        f"orders={sum(results)}/{len(results)}",
    )


def charge_and_action_certificate(harness: Harness, mutation: str | None) -> None:
    results = []
    for realization in ("car", "hcb"):
        total_number = sum(number_operators(realization, mutation), sp.zeros(16))
        results.append(
            matrix_zero(hopping(realization, mutation) * total_number - total_number * hopping(realization, mutation))
        )
    harness.check(
        "the one supplied hopping expression conserves total U(1) charge in both realizations",
        all(results),
        f"charge_commutators={results}",
    )


def link_derivative_certificate(harness: Harness, mutation: str | None) -> None:
    phase = sp.symbols("A", real=True)
    coupling = sp.symbols("t", real=True, nonzero=True)
    results = []
    for realization in ("car", "hcb"):
        annihilators = operators(realization, mutation)
        for source, target in EDGES:
            a_source, a_target = annihilators[source], annihilators[target]
            if (
                mutation == "delete_edge_consistently"
                and set((source, target)) == {0, 1}
            ):
                phased_term = sp.zeros(16)
            else:
                phased_term = -coupling * (
                    sp.exp(-sp.I * phase) * adjoint(a_target) * a_source
                    + sp.exp(sp.I * phase) * adjoint(a_source) * a_target
                )
            derivative = sp.Matrix(phased_term).diff(phase).subs(phase, 0)
            results.append(
                matrix_zero(
                    derivative
                    - coupling
                    * oriented_current(realization, source, target, mutation)
                )
            )
    harness.check(
        "every oriented bond current tJ is the link-phase derivative of that same action tH",
        all(results),
        f"exact_link_derivatives={sum(results)}/{len(results)}",
    )


def continuity_certificate(harness: Harness, mutation: str | None) -> None:
    coupling = sp.symbols("t", real=True, nonzero=True)
    results = []
    for realization in ("car", "hcb"):
        hamiltonian = hopping(realization, mutation)
        numbers = number_operators(realization, mutation)
        for site in range(4):
            neighbors = tuple(
                right if left == site else left
                for left, right in EDGES
                if left == site or right == site
            )
            divergence = sum(
                (
                    oriented_current(realization, site, neighbor, mutation)
                    for neighbor in neighbors
                ),
                sp.zeros(16),
            )
            results.append(
                matrix_zero(
                    sp.I
                    * coupling
                    * (hamiltonian * numbers[site] - numbers[site] * hamiltonian)
                    + coupling * divergence
                )
            )
    harness.check(
        "operator continuity closes at all four vertices in both product theories",
        all(results),
        f"continuity_identities={sum(results)}/{len(results)}",
    )


def plaquette_covariance_certificate(harness: Harness, mutation: str | None) -> None:
    dihedral = tuple(
        permutation
        for offset in range(4)
        for permutation in (
            tuple((site + offset) % 4 for site in range(4)),
            tuple((offset - site) % 4 for site in range(4)),
        )
    )
    results = []
    current_results = []
    event_pair_results = []
    pair_projector = (
        ket(10, 16) * adjoint(ket(10, 16))
        + ket(5, 16) * adjoint(ket(5, 16))
    )
    for realization in ("car", "hcb"):
        fermionic = realization == "car"
        if mutation == "ordinary_site_permutation_for_car" and fermionic:
            fermionic = False
        hamiltonian = hopping(realization, mutation)
        for permutation in dihedral:
            lift = site_permutation_lift(permutation, fermionic)
            results.append(
                matrix_zero(lift * hamiltonian * adjoint(lift) - hamiltonian)
            )
            source, target = 0, 1
            current_results.append(
                matrix_zero(
                    lift
                    * oriented_current(realization, source, target, mutation)
                    * adjoint(lift)
                    - oriented_current(
                        realization,
                        permutation[source],
                        permutation[target],
                        mutation,
                    )
                )
            )
            event_pair_results.append(
                matrix_zero(lift * pair_projector * adjoint(lift) - pair_projector)
            )
    harness.check(
        "the law, oriented current, and opposite-corner event pair are covariant under all eight plaquette frames",
        len(dihedral) == 8
        and all(results)
        and all(current_results)
        and all(event_pair_results),
        f"law={sum(results)}/16 current={sum(current_results)}/16 events={sum(event_pair_results)}/16",
    )


def d4_quadratic_action_ray_certificate(
    harness: Harness, mutation: str | None
) -> None:
    real_parts = sp.symbols("r0:4", real=True)
    imaginary_parts = sp.symbols("q0:4", real=True)
    variables = (*real_parts, *imaginary_parts)
    dihedral = tuple(
        permutation
        for offset in range(4)
        for permutation in (
            tuple((site + offset) % 4 for site in range(4)),
            tuple((offset - site) % 4 for site in range(4)),
        )
    )
    if mutation == "d4_allows_flux":
        dihedral = dihedral[::2]
    solutions = []
    for realization in ("car", "hcb"):
        annihilators = operators(realization, mutation)
        general = sp.zeros(16)
        for index, (source, target) in enumerate(EDGES):
            weight = real_parts[index] + sp.I * imaginary_parts[index]
            general -= (
                weight * adjoint(annihilators[source]) * annihilators[target]
                + sp.conjugate(weight)
                * adjoint(annihilators[target])
                * annihilators[source]
            )
        equations = []
        for permutation in dihedral:
            lift = site_permutation_lift(
                permutation, fermionic=realization == "car"
            )
            defect = sp.simplify(lift * general * adjoint(lift) - general)
            equations.extend(value for value in defect if value != 0)
        solutions.append(sp.linsolve(equations, variables))
    expected = sp.FiniteSet(
        (
            real_parts[3],
            real_parts[3],
            real_parts[3],
            real_parts[3],
            0,
            0,
            0,
            0,
        )
    )
    harness.check(
        "within scalar nearest-neighbor quadratic actions D4 fixes the real uniform hopping ray up to t",
        len(dihedral) == 8 and all(solution == expected for solution in solutions),
        f"frames={len(dihedral)} CAR={solutions[0]} HCB={solutions[1]}",
    )


def sector_polynomial_certificate(
    harness: Harness, mutation: str | None
) -> tuple[sp.Matrix, sp.Matrix]:
    car_two = restrict(hopping("car", mutation), TWO_PARTICLE_BASIS)
    hcb_two = restrict(hopping("hcb", mutation), TWO_PARTICLE_BASIS)
    car_polynomial = matrix_zero(car_two * (car_two**2 - 4 * sp.eye(6)))
    hcb_polynomial = matrix_zero(hcb_two * (hcb_two**2 - 8 * sp.eye(6)))
    spectra_ok = car_two.eigenvals() == {-2: 2, 0: 2, 2: 2} and hcb_two.eigenvals() == {
        -2 * sp.sqrt(2): 1,
        0: 4,
        2 * sp.sqrt(2): 1,
    }
    harness.check(
        "the exact two-particle blocks have their claimed minimal-polynomial and spectral data",
        car_polynomial and hcb_polynomial and spectra_ok,
        f"CAR_poly={car_polynomial} HCB_poly={hcb_polynomial} spectra={spectra_ok}",
    )
    return car_two, hcb_two


def exact_transfer_certificate(
    harness: Harness,
    mutation: str | None,
    car_two: sp.Matrix,
    hcb_two: sp.Matrix,
) -> tuple[int, int]:
    initial = 9 if mutation == "wrong_initial_occupancy" else 10
    target = 6 if mutation == "target_adjacent_occupancy" else 5
    initial_position = TWO_PARTICLE_BASIS.index(initial)
    target_position = TWO_PARTICLE_BASIS.index(target)
    z = sp.symbols("z", real=True)
    car_evolution = (
        sp.eye(6)
        - sp.I * sp.sin(2 * z) * car_two / 2
        + (sp.cos(2 * z) - 1) * car_two**2 / 4
    )
    hcb_evolution = (
        sp.eye(6)
        - sp.I * sp.sin(2 * sp.sqrt(2) * z) * hcb_two / (2 * sp.sqrt(2))
        + (sp.cos(2 * sp.sqrt(2) * z) - 1) * hcb_two**2 / 8
    )
    car_amplitude = sp.simplify(car_evolution[target_position, initial_position])
    hcb_amplitude = sp.simplify(hcb_evolution[target_position, initial_position])
    expected_hcb = (sp.cos(2 * sp.sqrt(2) * z) - 1) / 2
    sample = 0 if mutation == "zero_cadence_as_nontrivial" else sp.pi / (2 * sp.sqrt(2))
    sample_hcb = sp.simplify(hcb_amplitude.subs(z, sample))
    ok = (
        initial == 10
        and target == 5
        and car_amplitude == 0
        and sp.simplify(hcb_amplitude - expected_hcb) == 0
        and sample_hcb == -1
    )
    harness.check(
        "opposite-corner transfer is CAR-dark for all cadence and HCB-deterministic at one exact cadence",
        ok,
        f"A_CAR={car_amplitude} A_HCB={hcb_amplitude} A_HCB(z*)={sample_hcb}",
    )
    return initial_position, target_position


def integrated_current_to_record_certificate(
    harness: Harness,
    mutation: str | None,
    hcb_two: sp.Matrix,
    initial_position: int,
) -> None:
    z = sp.symbols("z", real=True)
    evolution = (
        sp.eye(6)
        - sp.I * sp.sin(2 * sp.sqrt(2) * z) * hcb_two / (2 * sp.sqrt(2))
        + (sp.cos(2 * sp.sqrt(2) * z) - 1) * hcb_two**2 / 8
    )
    state = sp.simplify(evolution * ket(initial_position, 6))
    numbers = number_operators("hcb", mutation)
    densities = tuple(
        sp.simplify(
            (adjoint(state) * restrict(number, TWO_PARTICLE_BASIS) * state)[0]
        )
        for number in numbers
    )
    expected_densities = (
        sp.cos(sp.sqrt(2) * z) ** 2,
        sp.sin(sp.sqrt(2) * z) ** 2,
        sp.cos(sp.sqrt(2) * z) ** 2,
        sp.sin(sp.sqrt(2) * z) ** 2,
    )
    density_ok = all(
        sp.trigsimp(actual - expected) == 0
        for actual, expected in zip(densities, expected_densities)
    )
    sample = sp.pi / (2 * sp.sqrt(2))
    deltas = tuple(
        sp.simplify(density.subs(z, sample) - density.subs(z, 0))
        for density in densities
    )
    current_integrals = {}
    for source, target in EDGES:
        current = restrict(
            oriented_current("hcb", source, target, mutation),
            TWO_PARTICLE_BASIS,
        )
        expectation = sp.simplify((adjoint(state) * current * state)[0])
        current_integrals[(source, target)] = sp.simplify(
            sp.integrate(expectation, (z, 0, sample))
        )

    continuity_integrals = []
    for site, delta in enumerate(deltas):
        outgoing = 0
        for left, right in EDGES:
            if left == site:
                outgoing += current_integrals[(left, right)]
            elif right == site:
                outgoing -= current_integrals[(left, right)]
        continuity_integrals.append(sp.simplify(delta + outgoing) == 0)
    expected_currents = {
        (0, 1): sp.Rational(1, 2),
        (1, 2): -sp.Rational(1, 2),
        (2, 3): sp.Rational(1, 2),
        (3, 0): -sp.Rational(1, 2),
    }
    harness.check(
        "the deterministic target Record is reached by the exactly integrated action-derived current",
        density_ok
        and deltas == (-1, 1, -1, 1)
        and current_integrals == expected_currents
        and all(continuity_integrals),
        f"delta_n={deltas} integrated_J={tuple(current_integrals.values())} continuity={continuity_integrals}",
    )


def common_event_certificate(
    harness: Harness, mutation: str | None
) -> tuple[sp.Matrix, sp.Matrix]:
    target_bits = (0, 1, 1, 0) if mutation == "target_adjacent_occupancy" else (0, 1, 0, 1)
    car_projector = occupation_projector("car", target_bits, mutation)
    hcb_projector = occupation_projector("hcb", target_bits, mutation)
    if mutation == "product_specific_writer":
        car_projector = occupation_projector("car", (0, 1, 1, 0), mutation)
    expected = ket(5, 16) * adjoint(ket(5, 16))
    parity = kron_all(Z, Z, Z, Z)
    ok = (
        target_bits == (0, 1, 0, 1)
        and matrix_zero(car_projector - hcb_projector)
        and matrix_zero(car_projector - expected)
        and matrix_zero(parity * car_projector - car_projector * parity)
        and matrix_zero(car_projector**2 - car_projector)
    )
    harness.check(
        "the target event is the same even charge-spectral projector in both theories",
        ok,
        f"common={matrix_zero(car_projector-hcb_projector)} rank={car_projector.rank()} even={matrix_zero(parity*car_projector-car_projector*parity)}",
    )
    return car_projector, hcb_projector


def record_instrument_certificate(
    harness: Harness,
    mutation: str | None,
    car_two: sp.Matrix,
    hcb_two: sp.Matrix,
    initial_position: int,
    target_position: int,
    car_event_full: sp.Matrix,
    hcb_event_full: sp.Matrix,
) -> tuple[sp.Matrix, sp.Matrix]:
    car_projector = restrict(car_event_full, TWO_PARTICLE_BASIS)
    hcb_projector = restrict(hcb_event_full, TWO_PARTICLE_BASIS)
    record_zero, record_one = ket(0, 2), ket(1, 2)
    pointer_one = sp.kronecker_product(sp.eye(6), record_one * adjoint(record_one))

    def instrument(projector: sp.Matrix) -> tuple[sp.Matrix, sp.Matrix, bool, bool, bool]:
        complement = sp.eye(6) - projector
        k_zero = sp.kronecker_product(complement, record_zero)
        k_one = sp.kronecker_product(projector, record_one)
        complete = matrix_zero(
            adjoint(k_zero) * k_zero + adjoint(k_one) * k_one - sp.eye(6)
        )
        vec_zero = sp.Matrix(k_zero).reshape(k_zero.rows * k_zero.cols, 1)
        vec_one = sp.Matrix(k_one).reshape(k_one.rows * k_one.cols, 1)
        choi_factor = sp.Matrix.hstack(vec_zero, vec_one)
        choi = sp.simplify(choi_factor * adjoint(choi_factor))
        choi_gram = sp.simplify(adjoint(choi_factor) * choi_factor)
        choi_positive = (
            matrix_zero(choi - adjoint(choi))
            and choi.rank() == 2
            and sp.trace(choi) == 6
            and choi_gram == sp.diag(5, 1)
        )
        correlation = (
            matrix_zero(adjoint(k_one) * pointer_one * k_one - projector)
            and matrix_zero(adjoint(k_zero) * pointer_one * k_zero)
        )
        return k_zero, k_one, complete, choi_positive, correlation

    car_k_zero, car_k_one, car_complete, car_choi, car_correlation = instrument(
        car_projector
    )
    hcb_k_zero, hcb_k_one, hcb_complete, hcb_choi, hcb_correlation = instrument(
        hcb_projector
    )

    sample = 0 if mutation == "zero_cadence_as_nontrivial" else sp.pi / (2 * sp.sqrt(2))
    initial_ket = ket(initial_position, 6)
    hcb_star = (
        sp.eye(6)
        - sp.I * sp.sin(2 * sp.sqrt(2) * sample) * hcb_two / (2 * sp.sqrt(2))
        + (sp.cos(2 * sp.sqrt(2) * sample) - 1) * hcb_two**2 / 8
    )
    car_star = (
        sp.eye(6)
        - sp.I * sp.sin(2 * sample) * car_two / 2
        + (sp.cos(2 * sample) - 1) * car_two**2 / 4
    )
    hcb_state = sp.simplify(hcb_star * initial_ket)
    car_state = sp.simplify(car_star * initial_ket)
    hcb_weight = sp.simplify(
        (adjoint(hcb_state) * hcb_projector * hcb_state)[0]
    )
    car_weight = sp.simplify(
        (adjoint(car_state) * car_projector * car_state)[0]
    )
    hcb_density = hcb_state * adjoint(hcb_state)
    car_density = car_state * adjoint(car_state)
    hcb_output = sp.simplify(
        hcb_k_zero * hcb_density * adjoint(hcb_k_zero)
        + hcb_k_one * hcb_density * adjoint(hcb_k_one)
    )
    car_output = sp.simplify(
        car_k_zero * car_density * adjoint(car_k_zero)
        + car_k_one * car_density * adjoint(car_k_one)
    )
    pure_pointer_output = (
        matrix_zero(
            hcb_output
            - sp.kronecker_product(
                hcb_density, record_one * adjoint(record_one)
            )
        )
        and matrix_zero(
            car_output
            - sp.kronecker_product(
                car_density, record_zero * adjoint(record_zero)
            )
        )
    )
    harness.check(
        "one common even Kraus/Choi Record writer reports the exact 0-versus-1 action signal",
        matrix_zero(car_projector - hcb_projector)
        and car_complete
        and hcb_complete
        and car_choi
        and hcb_choi
        and car_correlation
        and hcb_correlation
        and car_weight == 0
        and hcb_weight == 1
        and pure_pointer_output,
        f"common={matrix_zero(car_projector-hcb_projector)} complete=({car_complete},{hcb_complete}) Choi_factor_PSD=({car_choi},{hcb_choi}) correlation=({car_correlation},{hcb_correlation}) weights=({car_weight},{hcb_weight}) pure_pointer={pure_pointer_output}",
    )
    return car_output, hcb_output


def permanence_certificate(
    harness: Harness, mutation: str | None, car_two: sp.Matrix, hcb_two: sp.Matrix
) -> None:
    record_one = ket(1, 2) * adjoint(ket(1, 2))
    pointer_event = sp.kronecker_product(sp.eye(6), record_one)
    results = []
    for hamiltonian in (car_two, hcb_two):
        future_generator = sp.kronecker_product(hamiltonian, I2)
        if mutation == "overwrite_pointer":
            future_generator += sp.kronecker_product(sp.eye(6), X)
        results.append(
            matrix_zero(
                future_generator * pointer_event - pointer_event * future_generator
            )
        )
    harness.check(
        "all later evolution under the same matter law fixes the written pointer Record projectors",
        all(results),
        f"Heisenberg_fixed={results}",
    )


def relabel_and_scope_certificate(
    harness: Harness,
    mutation: str | None,
    car_output: sp.Matrix,
    hcb_output: sp.Matrix,
) -> None:
    record_zero = ket(0, 2) * adjoint(ket(0, 2))
    record_one = ket(1, 2) * adjoint(ket(1, 2))
    relabel = X if mutation != "pointer_relabel_changes_weight" else sp.diag(1, sp.Rational(1, 2)) * X
    lifted_relabel = sp.kronecker_product(sp.eye(6), relabel)

    def weights(output: sp.Matrix) -> tuple[sp.Expr, sp.Expr]:
        return (
            sp.simplify(sp.trace(sp.kronecker_product(sp.eye(6), record_zero) * output)),
            sp.simplify(sp.trace(sp.kronecker_product(sp.eye(6), record_one) * output)),
        )

    label_ok = True
    for output in (car_output, hcb_output):
        before = weights(output)
        after = weights(sp.simplify(lifted_relabel * output * adjoint(lifted_relabel)))
        label_ok = label_ok and sorted(before) == sorted(after)

    assumptions = (ROOT / PACKET / "ASSUMPTIONS_AND_IMPORTS.md").read_text()
    goal = (ROOT / PACKET / "GOAL.md").read_text()
    calibration_present = "scoped conditional premise" in assumptions
    claims_relative_probabilities_without_calibration = mutation == "born_without_calibration"
    claims_full_response = mutation == "arbitrary_K_family_fixed"
    scope_ok = (
        calibration_present
        and not claims_relative_probabilities_without_calibration
        and not claims_full_response
        and "not an unconditional derivation" in goal
        and "no action" in assumptions
        and "no audit" in assumptions
    )
    harness.check(
        "actual pointer-label relabeling and the claim firewall preserve weights without promoting calibration or a full response family",
        label_ok and scope_ok,
        f"label_invariant={label_ok} calibration_conditional={calibration_present} relative_probability_overclaim={claims_relative_probabilities_without_calibration} full_K_claim={claims_full_response}",
    )


def run(mutation: str | None) -> Harness:
    harness = Harness()
    source_and_prereg_certificate(harness, mutation)
    local_algebra_and_common_input_certificate(harness, mutation)
    jordan_wigner_order_invariance_certificate(harness, mutation)
    charge_and_action_certificate(harness, mutation)
    link_derivative_certificate(harness, mutation)
    continuity_certificate(harness, mutation)
    plaquette_covariance_certificate(harness, mutation)
    d4_quadratic_action_ray_certificate(harness, mutation)
    car_two, hcb_two = sector_polynomial_certificate(harness, mutation)
    initial_position, target_position = exact_transfer_certificate(
        harness, mutation, car_two, hcb_two
    )
    integrated_current_to_record_certificate(
        harness, mutation, hcb_two, initial_position
    )
    car_event, hcb_event = common_event_certificate(harness, mutation)
    car_output, hcb_output = record_instrument_certificate(
        harness,
        mutation,
        car_two,
        hcb_two,
        initial_position,
        target_position,
        car_event,
        hcb_event,
    )
    permanence_certificate(harness, mutation, car_two, hcb_two)
    relabel_and_scope_certificate(harness, mutation, car_output, hcb_output)
    print(f"TOTAL: PASS={harness.passed} FAIL={harness.failed}")
    return harness


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS)
    arguments = parser.parse_args()
    result = run(arguments.mutation)
    return 1 if result.failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
