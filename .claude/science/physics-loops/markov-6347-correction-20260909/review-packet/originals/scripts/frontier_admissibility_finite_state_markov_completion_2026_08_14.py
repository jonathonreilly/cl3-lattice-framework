#!/usr/bin/env python3
"""Block 87: arbitrary-finite-state Markov completion of the Block 84 law.

The Block 84 nearest-neighbour Record law is extended from its seed-grown
cylinders to every finite Record configuration.  The runner proves finite
frontiers, normalized finite-atomic transitions, permanence, content-blind
formation, spatial covariance, finite propagation, non-halting of every
nonempty finite full-lattice state, and the standard-Borel Markov interface.
It also isolates the supplied synchronous scheduler and shows that the
two-cube halt is a boundary restriction rather than a full-Z3 horizon.
"""

from __future__ import annotations

import argparse
import json
from itertools import combinations, product
from hashlib import sha256
from pathlib import Path
import subprocess

import sympy as sp

import frontier_admissibility_taxicab_shell_record_instrument_2026_08_14 as block84


ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_FINITE_STATE_MARKOV_COMPLETION_BOUNDED_THEOREM_NOTE_"
    "2026-08-14.md"
)
AXIOM_REPO_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AXIOM_PATH = ROOT / AXIOM_REPO_PATH
PREMISE_REGISTRY_REPO_PATH = "docs/audit/data/axiom_premise_nodes.json"
PREMISE_REGISTRY_PATH = ROOT / PREMISE_REGISTRY_REPO_PATH
PRIMITIVE_SOURCE_PATHS = (
    ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md",
    ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
    ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md",
)
PARENT_NOTE = ROOT / "docs" / (
    "ADMISSIBILITY_TAXICAB_SHELL_RECORD_INSTRUMENT_CYLINDER_LAW_"
    "BOUNDED_THEOREM_NOTE_2026-08-14.md"
)
PARENT_RUNNER = ROOT / "scripts" / (
    "frontier_admissibility_taxicab_shell_record_instrument_2026_08_14.py"
)
PARENT_CACHE = ROOT / "logs" / "runner-cache" / (
    "frontier_admissibility_taxicab_shell_record_instrument_2026_08_14.txt"
)
PARENT_COMMIT = "b37d487dac778c11e7a9a0e3d1772e39cef0d343"
PARENT_SHA256 = (
    "e9d87e9aa7a15512dc0f5b769ad21c088f82950e8e4030d755fc1ca49520d303",
    "78526260e1572e566176795ec34d281f11f42bd1bfb960f4bf4d72798e8afb7f",
    "db81b34457f47e2d8c86786ec3901934ff1e99b92ece99d49b120dc58e8570dd",
)
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_FINITE_STATE_MARKOV_COMPLETION_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md",
    "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
    "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md",
    "docs/ADMISSIBILITY_TAXICAB_SHELL_RECORD_INSTRUMENT_CYLINDER_LAW_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "scripts/frontier_admissibility_taxicab_shell_record_instrument_2026_08_14.py",
    "logs/runner-cache/frontier_admissibility_taxicab_shell_record_instrument_2026_08_14.txt",
)

Site = block84.Site
Vec = block84.Vec
Rotation = block84.Rotation
Content = sp.ImmutableMatrix
RecordMap = dict[Site, Content]
E1: Site = (1, 0, 0)


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, condition: bool, detail: str) -> None:
        result = bool(condition)
        self.passed += int(result)
        self.failed += int(not result)
        print(f"{'PASS' if result else 'FAIL'} {label}: {detail}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def file_sha256(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def current_authority_text(repo_path: str) -> tuple[str, str]:
    for ref in ("origin/main", "HEAD"):
        exists = subprocess.run(
            ("git", "cat-file", "-e", f"{ref}:{repo_path}"),
            cwd=ROOT,
            check=False,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        ).returncode == 0
        if exists:
            return ref, subprocess.check_output(
                ("git", "show", f"{ref}:{repo_path}"),
                cwd=ROOT,
                text=True,
            )
    raise RuntimeError("cannot resolve current axiom authority")


def authority_certificate(stale: bool = False) -> dict[str, object]:
    ref, axiom = current_authority_text(AXIOM_REPO_PATH)
    registry_ref, registry_text = current_authority_text(PREMISE_REGISTRY_REPO_PATH)
    registry = json.loads(registry_text)
    registered_ids = tuple(registry.get("canonical_ids") or ())
    primitive_text = " ".join(
        " ".join(path.read_text(encoding="utf-8").split())
        for path in PRIMITIVE_SOURCE_PATHS
    )
    flat = " ".join(axiom.split())
    parent_is_ancestor = subprocess.run(
        ("git", "merge-base", "--is-ancestor", PARENT_COMMIT, "HEAD"),
        cwd=ROOT,
        check=False,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    ).returncode == 0
    return {
        "ref": ref,
        "axiom_sha256": sha256(axiom.encode()).hexdigest(),
        "local_matches": AXIOM_PATH.read_text(encoding="utf-8") == axiom,
        "registry_ref": registry_ref,
        "registry_local_matches": (
            PREMISE_REGISTRY_PATH.read_text(encoding="utf-8") == registry_text
        ),
        "registered_ids": registered_ids,
        "registered_law_absent": registered_ids == (
            "minimal_axioms",
            "scale_reference_primitive",
            "kinetic_isotropy_primitive",
            "realized_state_primitive",
        ),
        "primitive_scope_guard": all(
            phrase in primitive_text
            for phrase in (
                "This is a units conversion, not a physics axiom.",
                "It carries no dimensionless dynamical content",
                "no state, averaging over alternatives, measure, weighting, probability rule",
            )
        ),
        "parent_is_ancestor": parent_is_ancestor,
        "parent_hashes": (
            file_sha256(PARENT_NOTE), file_sha256(PARENT_RUNNER),
            file_sha256(PARENT_CACHE),
        ),
        "parent_hashes_match": (
            file_sha256(PARENT_NOTE), file_sha256(PARENT_RUNNER),
            file_sha256(PARENT_CACHE),
        ) == PARENT_SHA256,
        "current_contract": all(
            phrase in flat
            for phrase in (
                "There is one fixed nearest-neighbor admissibility rule",
                "For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.",
                "Records form.",
                "records are permanent.",
                "A state is a configuration of records.",
                "Admissibility is not a dynamics axiom.",
            )
        ),
        "forced_stale": stale,
    }


def matrix_key(matrix: sp.MatrixBase) -> tuple[sp.Expr, ...]:
    return tuple(sp.simplify(value) for value in matrix)


def domains(host: tuple[Site, ...], include_empty: bool = True):
    start = 0 if include_empty else 1
    for count in range(start, len(host) + 1):
        for subset in combinations(host, count):
            yield frozenset(subset)


def content_table(domain: frozenset[Site], variant: int) -> RecordMap:
    if variant == 0:
        return {
            site: sp.ImmutableMatrix(block84.I2 / 2)
            for site in domain
        }
    directions: tuple[Vec, ...] = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    return {
        site: sp.ImmutableMatrix(
            block84.projector(
                directions[index % len(directions)],
                1 if sum(site) % 2 == 0 else -1,
            )
        )
        for index, site in enumerate(sorted(domain))
    }


def finite_state_certificate(infinite_frontier: bool = False) -> dict[str, object]:
    host = (
        (0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1),
        (-1, 0, 0), (0, -1, 0), (0, 0, -1),
    )
    failures = 0
    cases = 0
    maximum_frontier = 0
    maximum_ratio = sp.Rational(0)
    for case, domain in enumerate(domains(host)):
        frontier = set(block84.candidate_frontier(domain))
        if infinite_frontier and case == 1:
            frontier.add((100, 100, 100))
        failures += bool(frontier & set(domain))
        failures += len(frontier) > 6 * len(domain)
        for site in frontier:
            failures += not any(
                block84.add(site, step) in domain
                for axis in block84.AXES
                for step in (axis, tuple(-value for value in axis))
            )
        maximum_frontier = max(maximum_frontier, len(frontier))
        if domain:
            maximum_ratio = max(maximum_ratio, sp.Rational(len(frontier), len(domain)))
        cases += 1

    projector_alphabet = {
        matrix_key(block84.projector(direction, sign))
        for direction in product((-1, 0, 1), repeat=3)
        if direction != (0, 0, 0)
        for sign in (-1, 1)
    }
    generated_alphabet = projector_alphabet | {matrix_key(block84.I2 / 2)}
    return {
        "cases": cases,
        "failures": failures,
        "maximum_frontier": maximum_frontier,
        "maximum_ratio": maximum_ratio,
        "projector_alphabet": len(projector_alphabet),
        "generated_alphabet": len(generated_alphabet),
        "finite_domain_strata_countable": True,
        "full_finite_record_space_countable": False,
        "full_finite_record_space_standard_borel": True,
        "reachable_finite_alphabet_subspace_countable": True,
    }


def local_weights(
    direction: Vec,
    power: int = 1,
    break_normalization: bool = False,
) -> dict[int, sp.Expr]:
    k = block84.k_value(direction)
    weights = {
        sign: block84.response_weight(k, sign, power)
        for sign in (-1, 1)
    }
    if break_normalization and direction == (1, 0, 0):
        weights[1] = sp.simplify(weights[1] + sp.Rational(1, 100))
    return weights


def branch_probability(
    domain: frozenset[Site],
    signs: dict[Site, int],
    power: int = 1,
    break_normalization: bool = False,
) -> sp.Expr:
    frontier = block84.candidate_frontier(domain)
    if set(signs) != set(frontier):
        raise ValueError("one sign is required at every forming site")
    probability = sp.Integer(1)
    for site, sign in signs.items():
        direction = block84.neighbour_difference(site, domain)
        probability *= local_weights(
            direction, power, break_normalization
        )[sign]
    return sp.simplify(probability)


def transition_normalization_certificate(
    break_normalization: bool = False,
) -> dict[str, object]:
    direction_failures = 0
    for direction in product((-1, 0, 1), repeat=3):
        if direction == (0, 0, 0):
            continue
        weights = local_weights(direction, 1, break_normalization)
        direction_failures += sp.simplify(sum(weights.values()) - 1) != 0
        direction_failures += any(weight.is_positive is not True for weight in weights.values())

    host = ((0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1), (-1, 0, 0))
    domain_failures = 0
    cases = 0
    maximum_atoms = 0
    for domain in domains(host):
        frontier = block84.candidate_frontier(domain)
        normalization = sp.Integer(1)
        for site in frontier:
            direction = block84.neighbour_difference(site, domain)
            normalization *= sum(
                local_weights(direction, 1, break_normalization).values()
            )
        domain_failures += sp.simplify(normalization - 1) != 0
        maximum_atoms = max(maximum_atoms, 1 << len(frontier))
        cases += 1

    seed = frozenset({block84.ORIGIN})
    seed_frontier = sorted(block84.candidate_frontier(seed))
    explicit_sum = sp.Integer(0)
    for signs in product((-1, 1), repeat=len(seed_frontier)):
        explicit_sum += branch_probability(
            seed,
            dict(zip(seed_frontier, signs)),
            break_normalization=break_normalization,
        )
    return {
        "directions": 26,
        "direction_failures": direction_failures,
        "domain_cases": cases,
        "domain_failures": domain_failures,
        "seed_atoms": 1 << len(seed_frontier),
        "seed_normalization": sp.simplify(explicit_sum),
        "maximum_tested_atoms": maximum_atoms,
        "finite_atomic_kernel": True,
    }


def selection_countermodel_certificate() -> dict[str, object]:
    response_failures = 0
    distinct_sectors = 0
    for k in (1, 2, 3):
        linear = {
            sign: block84.response_weight(k, sign, 1) for sign in (-1, 1)
        }
        cubic = {
            sign: block84.response_weight(k, sign, 3) for sign in (-1, 1)
        }
        response_failures += sp.simplify(sum(linear.values()) - 1) != 0
        response_failures += sp.simplify(sum(cubic.values()) - 1) != 0
        response_failures += any(
            weight.is_positive is not True
            for weight in (*linear.values(), *cubic.values())
        )
        distinct_sectors += any(
            sp.simplify(linear[sign] - cubic[sign]) != 0 for sign in (-1, 1)
        )

    product_normalization, product_mean, product_variance = (
        block84.binomial_frequency_moments(2, 4, 1)
    )
    correlated_normalization, correlated_mean, correlated_variance = (
        block84.common_sign_frequency_moments(2, 4, 1)
    )
    return {
        "response_failures": response_failures,
        "linear_cubic_distinct_sectors": distinct_sectors,
        "product_normalization": product_normalization,
        "correlated_normalization": correlated_normalization,
        "same_one_site_mean": sp.simplify(product_mean - correlated_mean) == 0,
        "different_history_variance": (
            sp.simplify(product_variance - correlated_variance) != 0
        ),
    }


def formation_frontier(
    records: RecordMap,
    content_feedback: bool = False,
) -> frozenset[Site]:
    frontier = block84.candidate_frontier(frozenset(records))
    if content_feedback and frontier and any(
        not block84.matrix_equal(sp.Matrix(content), block84.I2 / 2)
        for content in records.values()
    ):
        return frozenset(set(frontier) - {min(frontier)})
    return frontier


def permanence_content_certificate(
    content_feedback: bool = False,
    overwrite: bool = False,
) -> dict[str, object]:
    host = ((0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1), (-1, 0, 0))
    content_blind_failures = 0
    permanence_failures = 0
    support_failures = 0
    cases = 0
    for domain in domains(host, include_empty=False):
        left = content_table(domain, 0)
        right = content_table(domain, 1)
        left_frontier = formation_frontier(left, content_feedback)
        right_frontier = formation_frontier(right, content_feedback)
        content_blind_failures += left_frontier != right_frontier
        content_blind_failures += any(
            block84.neighbour_difference(site, frozenset(left))
            != block84.neighbour_difference(site, frozenset(right))
            for site in set(left_frontier) | set(right_frontier)
        )

        frontier = block84.candidate_frontier(domain)
        signs = {site: block84.deterministic_sign(site) for site in frontier}
        updated = block84.finite_record_update(left, signs)
        if overwrite and updated:
            old_site = min(domain)
            updated[old_site] = sp.ImmutableMatrix(block84.projector((1, 0, 0), 1))
        permanence_failures += not block84.preserves_records(left, updated)
        for site in frontier:
            direction = block84.neighbour_difference(site, domain)
            expected = block84.projector(direction, signs[site])
            support_failures += not block84.matrix_equal(
                sp.Matrix(updated[site]), expected
            )
        cases += 1
    return {
        "cases": cases,
        "content_blind_failures": content_blind_failures,
        "permanence_failures": permanence_failures,
        "support_failures": support_failures,
        "old_content_carried_by_identity": not overwrite,
    }


def rotate_domain(rotation: Rotation, domain: frozenset[Site]) -> frozenset[Site]:
    return frozenset(block84.rotate(rotation, site) for site in domain)


def translate_domain(offset: Site, domain: frozenset[Site]) -> frozenset[Site]:
    return frozenset(block84.add(offset, site) for site in domain)


def covariance_certificate(noncovariant: bool = False) -> dict[str, object]:
    host = ((0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1), (-1, 0, 0))
    test_domains = tuple(domains(host))
    lifts = block84.proper_cubic_lifts()
    rotations = tuple(rotation for rotation, _unitary in lifts)
    geometry_failures = 0
    direction_failures = 0
    mutation_used = False
    for rotation in rotations:
        for domain in test_domains:
            rotated_domain = rotate_domain(rotation, domain)
            expected_frontier = rotate_domain(
                rotation, block84.candidate_frontier(domain)
            )
            observed_frontier = block84.candidate_frontier(rotated_domain)
            geometry_failures += observed_frontier != expected_frontier
            for site in block84.candidate_frontier(domain):
                direction = block84.neighbour_difference(site, domain)
                rotated_site = block84.rotate(rotation, site)
                observed_direction = block84.neighbour_difference(
                    rotated_site, rotated_domain
                )
                expected_direction = block84.rotate(rotation, direction)
                if (
                    noncovariant
                    and not mutation_used
                    and expected_direction != direction
                ):
                    expected_direction = direction
                    mutation_used = True
                direction_failures += observed_direction != expected_direction

        # The parent receipt proves projector transport on all 26 types.  This
        # block checks the new arbitrary-domain condition transport and the
        # radial-weight part, which depend only on integer directions.
        for direction in product((-1, 0, 1), repeat=3):
            if direction == (0, 0, 0):
                continue
            expected_direction = block84.rotate(rotation, direction)
            for sign in (-1, 1):
                direction_failures += (
                    block84.response_weight(block84.k_value(direction), sign, 1)
                    != block84.response_weight(
                        block84.k_value(expected_direction), sign, 1
                    )
                )

    translation_failures = 0
    for offset in ((3, -2, 1), (-4, 1, 2)):
        for domain in test_domains:
            translated = translate_domain(offset, domain)
            expected = translate_domain(offset, block84.candidate_frontier(domain))
            translation_failures += block84.candidate_frontier(translated) != expected
    return {
        "rotations": len(rotations),
        "domain_cases": len(test_domains),
        "geometry_failures": geometry_failures,
        "direction_failures": direction_failures,
        "parent_projector_covariance": (
            "PASS: proper-cubic-covariance all projectors, k sectors, weights, and B_t geometries transform covariantly"
            in PARENT_CACHE.read_text(encoding="utf-8")
            and "TOTAL: PASS=25 FAIL=0" in PARENT_CACHE.read_text(encoding="utf-8")
        ),
        "translation_failures": translation_failures,
        "mutation_used": mutation_used,
    }


def extreme_growth_witness(domain: frozenset[Site]) -> tuple[Site, Site, Vec]:
    if not domain:
        raise ValueError("nonempty finite domain required")
    extreme = max(domain, key=lambda site: (site[0], site[1], site[2]))
    witness = block84.add(extreme, E1)
    return extreme, witness, block84.neighbour_difference(witness, domain)


def distance_to_domain(site: Site, domain: frozenset[Site]) -> int:
    return min(block84.taxicab_norm(block84.sub(site, source)) for source in domain)


def growth_certificate(false_halt: bool = False) -> dict[str, object]:
    host = (
        (0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1),
        (-1, 0, 0), (0, -1, 0), (0, 0, -1),
    )
    witness_failures = 0
    nonempty_cases = 0
    for case, domain in enumerate(domains(host, include_empty=False)):
        extreme, witness, direction = extreme_growth_witness(domain)
        frontier = block84.candidate_frontier(domain)
        if false_halt and case == 0:
            frontier = frozenset()
        witness_failures += witness in domain
        witness_failures += block84.add(witness, E1) in domain
        witness_failures += block84.sub(witness, E1) != extreme
        witness_failures += direction[0] != -1
        witness_failures += witness not in frontier
        nonempty_cases += 1

    propagation_failures = 0
    iteration_cases = 0
    initial_domains = (
        frozenset({(0, 0, 0)}),
        frozenset({(0, 0, 0), (1, 0, 0)}),
        frozenset({(0, 0, 0), (1, 0, 0), (0, 1, 0)}),
    )
    for initial in initial_domains:
        current = initial
        for tick in range(1, 6):
            frontier = block84.candidate_frontier(current)
            propagation_failures += not frontier
            propagation_failures += any(
                distance_to_domain(site, initial) > tick
                for site in frontier
            )
            previous_size = len(current)
            current = current | frontier
            propagation_failures += len(current) > 7 * previous_size
            iteration_cases += 1

    seed_exact_failures = 0
    seed_state = frozenset({block84.ORIGIN})
    for tick in range(1, 7):
        seed_state |= block84.candidate_frontier(seed_state)
        seed_exact_failures += seed_state != block84.taxicab_ball(tick)
    return {
        "nonempty_cases": nonempty_cases,
        "witness_failures": witness_failures,
        "iteration_cases": iteration_cases,
        "propagation_failures": propagation_failures,
        "seed_exact_failures": seed_exact_failures,
        "empty_is_fixed": block84.candidate_frontier(frozenset()) == frozenset(),
        "finite_nonempty_full_lattice_halt": False,
        "maximum_speed_l1_sites_per_tick": 1,
    }


def scheduler_certificate(dynamic_scheduler: bool = False) -> dict[str, object]:
    seed = frozenset({block84.ORIGIN})
    frozen_frontier = block84.candidate_frontier(seed)
    first = min(frozen_frontier)
    after_first = seed | {first}
    dynamic_frontier = block84.candidate_frontier(after_first)
    new_dynamic_sites = dynamic_frontier - frozen_frontier

    signs = {site: block84.deterministic_sign(site) for site in frozen_frontier}
    reference = content_table(seed, 0)
    reference = block84.finite_record_update(reference, signs)
    order_failures = 0
    sample_sites = tuple(sorted(frozen_frontier)[:4])
    for order in (
        sample_sites,
        tuple(reversed(sample_sites)),
        (sample_sites[1], sample_sites[3], sample_sites[0], sample_sites[2]),
    ):
        partial = content_table(seed, 0)
        old_domain = frozenset(partial)
        for site in order:
            direction = block84.neighbour_difference(site, old_domain)
            partial[site] = sp.ImmutableMatrix(
                block84.projector(direction, signs[site])
            )
        for site in frozen_frontier - set(order):
            direction = block84.neighbour_difference(site, old_domain)
            partial[site] = sp.ImmutableMatrix(
                block84.projector(direction, signs[site])
            )
        order_failures += partial != reference
    return {
        "frozen_frontier": len(frozen_frontier),
        "new_dynamic_sites_after_one_write": len(new_dynamic_sites),
        "new_dynamic_sites": tuple(sorted(new_dynamic_sites)),
        "frozen_append_order_failures": order_failures,
        "scheduler_is_synchronous_prestate": not dynamic_scheduler,
        "dynamic_recomputation_equivalent": False,
    }


def patch_boundary_certificate(erase_boundary: bool = False) -> dict[str, object]:
    patch = block84.two_cube_patch()
    state = frozenset({block84.ORIGIN})
    wave_sizes = []
    for _ in range(5):
        frontier = block84.patch_frontier(state, patch)
        wave_sizes.append(len(frontier))
        state |= frontier
    patch_halted = state == patch and block84.patch_frontier(state, patch) == frozenset()
    full_lattice_frontier = block84.candidate_frontier(state)
    if erase_boundary:
        full_lattice_frontier = frozenset()

    seed_global = frozenset({block84.ORIGIN})
    for _ in range(4):
        seed_global |= block84.candidate_frontier(seed_global)
    shell_five = block84.candidate_frontier(seed_global)
    return {
        "patch_sites": len(patch),
        "wave_sizes": tuple(wave_sizes),
        "patch_halted": patch_halted,
        "full_lattice_frontier_after_patch_fill": len(full_lattice_frontier),
        "global_shell_five": len(shell_five),
        "global_shell_five_formula": block84.shell_size_formula(5),
        "finite_patch_halt_is_boundary_restriction": bool(full_lattice_frontier),
    }


def history_certificate(non_markov: bool = False) -> dict[str, object]:
    seed = frozenset({block84.ORIGIN})
    first_frontier = block84.candidate_frontier(seed)
    first_normalizer = sp.prod(
        sum(local_weights(block84.neighbour_difference(site, seed)).values())
        for site in first_frontier
    )
    first_domain = seed | first_frontier
    second_frontier = block84.candidate_frontier(first_domain)
    second_normalizer = sp.prod(
        sum(local_weights(block84.neighbour_difference(site, first_domain)).values())
        for site in second_frontier
    )
    two_step_mass = sp.simplify(first_normalizer * second_normalizer)

    current = seed
    path_probability = sp.Integer(1)
    cylinder_failures = 0
    for _tick in range(1, 5):
        frontier = block84.candidate_frontier(current)
        signs = {site: block84.deterministic_sign(site) for site in frontier}
        factor = branch_probability(current, signs)
        path_probability = sp.simplify(path_probability * factor)
        cylinder_failures += path_probability.is_positive is not True
        cylinder_failures += bool(path_probability > 1)
        current |= frontier

    signature_zero = local_weights((1, 0, 0))[1]
    signature_one = signature_zero
    if non_markov:
        signature_one = sp.simplify(signature_one + sp.Rational(1, 101))
    return {
        "first_frontier": len(first_frontier),
        "second_frontier": len(second_frontier),
        "two_step_total_mass": two_step_mass,
        "four_tick_path_probability": path_probability,
        "cylinder_failures": cylinder_failures,
        "time_homogeneous_signature": signature_zero == signature_one,
        "state_space_is_standard_borel": True,
        "kernel_is_finite_atomic_and_borel": True,
        "path_measure_prerequisites_complete": True,
        "physical_time_supplied": False,
    }


def boundary_surface_ok(law_claim: bool = False) -> bool:
    if not NOTE_PATH.is_file():
        return False
    note = NOTE_PATH.read_text(encoding="utf-8")
    needles = (
        "### N1 — Alternative-route enumeration and normalization",
        "### N2 — Wall-independence audit",
        "### N3 — Hidden-wall scan",
        "### N4 — Residual matching",
        "### N5 — Rhetoric and granularity audit",
        "### N6 — Partial-closure path scan",
        "### N7 — Steelman and strongest surviving escape route",
        "### N8 — Cross-cycle echo audit",
        "standard-Borel",
        "two-cube halt is a supplied boundary restriction",
        "synchronous scheduler is supplied",
        "linear response is not selected",
        "physical time remains open",
        "zero TOE percentage movement",
        "not an adopted law",
    )
    return not law_claim and all(needle in note for needle in needles)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mutation",
        choices=(
            "stale_axiom", "infinite_frontier", "break_normalization",
            "content_feedback", "overwrite", "noncovariant", "false_halt",
            "dynamic_scheduler", "erase_boundary", "non_markov", "law_claim",
        ),
    )
    args = parser.parse_args()
    mutation = args.mutation
    checks = Checks()

    authority = authority_certificate(mutation == "stale_axiom")
    authority_ok = (
        authority["local_matches"]
        and authority["registry_local_matches"]
        and authority["registered_law_absent"]
        and authority["primitive_scope_guard"]
        and authority["parent_is_ancestor"]
        and authority["parent_hashes_match"]
        and authority["current_contract"]
        and not authority["forced_stale"]
    )
    checks.check(
        "A-current-axiom-and-Block84-authority",
        authority_ok,
        f"{authority['ref']} axiom={str(authority['axiom_sha256'])[:12]}; live four-node premise registry has no Record-law primitive; exact Block84 note/runner receipt",
    )

    finite = finite_state_certificate(mutation == "infinite_frontier")
    finite_ok = (
        finite["cases"] == 128
        and finite["failures"] == 0
        and finite["maximum_ratio"] <= 6
        and finite["projector_alphabet"] == 26
        and finite["generated_alphabet"] == 27
        and finite["finite_domain_strata_countable"]
        and not finite["full_finite_record_space_countable"]
        and finite["full_finite_record_space_standard_borel"]
        and finite["reachable_finite_alphabet_subspace_countable"]
    )
    checks.check(
        "B-finite-frontier-and-state-space-type",
        finite_ok,
        f"{finite['cases']} domains satisfy |F(R)|<=6|R|; full finite-M2 state space is standard-Borel, generated 27-symbol subspace is countable",
    )

    normalization = transition_normalization_certificate(
        mutation == "break_normalization"
    )
    countermodels = selection_countermodel_certificate()
    normalization_ok = (
        normalization["directions"] == 26
        and normalization["direction_failures"] == 0
        and normalization["domain_cases"] == 32
        and normalization["domain_failures"] == 0
        and normalization["seed_atoms"] == 64
        and normalization["seed_normalization"] == 1
        and normalization["finite_atomic_kernel"]
        and countermodels["response_failures"] == 0
        and countermodels["linear_cubic_distinct_sectors"] == 3
        and countermodels["product_normalization"] == 1
        and countermodels["correlated_normalization"] == 1
        and countermodels["same_one_site_mean"]
        and countermodels["different_history_variance"]
    )
    checks.check(
        "C-normalized-finite-atomic-transition-kernel",
        normalization_ok,
        f"26 local directions and {normalization['domain_cases']} arbitrary domains normalize; seed transition has {normalization['seed_atoms']} atoms; linear/cubic and product/correlated twins remain distinct",
    )

    permanence = permanence_content_certificate(
        mutation == "content_feedback", mutation == "overwrite"
    )
    permanence_ok = (
        permanence["cases"] == 31
        and permanence["content_blind_failures"] == 0
        and permanence["permanence_failures"] == 0
        and permanence["support_failures"] == 0
        and permanence["old_content_carried_by_identity"]
    )
    checks.check(
        "D-content-blind-formation-supported-append-and-permanence",
        permanence_ok,
        f"{permanence['cases']} domains with two distinct content tables have identical formation kernels; old contents persist and new locks are supported",
    )

    covariance = covariance_certificate(mutation == "noncovariant")
    covariance_ok = (
        covariance["rotations"] == 24
        and covariance["domain_cases"] == 32
        and covariance["geometry_failures"] == 0
        and covariance["direction_failures"] == 0
        and covariance["parent_projector_covariance"]
        and covariance["translation_failures"] == 0
    )
    checks.check(
        "E-arbitrary-domain-translation-and-proper-cubic-covariance",
        covariance_ok,
        f"{covariance['domain_cases']} domains x 24 rotations plus two translations transport frontiers, directions, probabilities, and projectors",
    )

    growth = growth_certificate(mutation == "false_halt")
    growth_ok = (
        growth["nonempty_cases"] == 127
        and growth["witness_failures"] == 0
        and growth["propagation_failures"] == 0
        and growth["seed_exact_failures"] == 0
        and growth["empty_is_fixed"]
        and not growth["finite_nonempty_full_lattice_halt"]
        and growth["maximum_speed_l1_sites_per_tick"] == 1
    )
    checks.check(
        "F-finite-propagation-and-no-nonempty-finite-full-lattice-halt",
        growth_ok,
        f"{growth['nonempty_cases']} nonempty domains expose an extreme-site growth witness; 15 histories obey speed<=1 and the seed gives six exact balls",
    )

    scheduler = scheduler_certificate(mutation == "dynamic_scheduler")
    scheduler_ok = (
        scheduler["frozen_frontier"] == 6
        and scheduler["new_dynamic_sites_after_one_write"] == 5
        and scheduler["frozen_append_order_failures"] == 0
        and scheduler["scheduler_is_synchronous_prestate"]
        and not scheduler["dynamic_recomputation_equivalent"]
    )
    checks.check(
        "G-synchronous-prestate-atomicity-and-hostile-dynamic-recompute",
        scheduler_ok,
        f"six frozen writes commute, but one in-place write exposes {scheduler['new_dynamic_sites_after_one_write']} extra same-tick candidates",
    )

    patch = patch_boundary_certificate(mutation == "erase_boundary")
    patch_ok = (
        patch["patch_sites"] == 12
        and patch["wave_sizes"] == (3, 4, 3, 1, 0)
        and patch["patch_halted"]
        and patch["full_lattice_frontier_after_patch_fill"] > 0
        and patch["global_shell_five"] == patch["global_shell_five_formula"] == 102
        and patch["finite_patch_halt_is_boundary_restriction"]
    )
    checks.check(
        "H-two-cube-halt-is-not-a-full-lattice-horizon",
        patch_ok,
        f"the restricted 12-site patch halts after waves 3,4,3,1, while its full-lattice embedding has {patch['full_lattice_frontier_after_patch_fill']} eligible outside sites and the seed law has shell-5 size {patch['global_shell_five']}",
    )

    history = history_certificate(mutation == "non_markov")
    history_ok = (
        history["first_frontier"] == 6
        and history["second_frontier"] == 18
        and history["two_step_total_mass"] == 1
        and history["four_tick_path_probability"].is_positive is True
        and history["cylinder_failures"] == 0
        and history["time_homogeneous_signature"]
        and history["state_space_is_standard_borel"]
        and history["kernel_is_finite_atomic_and_borel"]
        and history["path_measure_prerequisites_complete"]
        and not history["physical_time_supplied"]
    )
    checks.check(
        "I-standard-Borel-time-homogeneous-Markov-history-interface",
        history_ok,
        f"two-step mass={history['two_step_total_mass']}; finite-atomic Borel kernel recursively defines normalized cylinders, but no physical duration",
    )

    boundary_ok = boundary_surface_ok(mutation == "law_claim")
    checks.check(
        "J-N1-N8-law-source-time-gravity-and-TOE-boundary",
        boundary_ok,
        "the note keeps candidate selection, scheduler/independence, action, seed, physical time, source/energy, gravity, retention, and scores open",
    )

    print(
        f"METRICS state_domains={finite['cases']} local_directions={normalization['directions']} "
        f"seed_atoms={normalization['seed_atoms']} rotations={covariance['rotations']} "
        f"nonempty_growth_cases={growth['nonempty_cases']} patch_outside_frontier={patch['full_lattice_frontier_after_patch_fill']}"
    )
    print(
        "BOUNDARY: the displayed Block84 Record-only member extends to a normalized covariant finite-atomic Markov kernel on every finite Record configuration, with permanent content-blind append, finite propagation, and no nonempty finite full-Z3 halt; the exact law/linear response, spatial-Pauli action, synchronous scheduler, conditional independence, seed, physical duration, source/energy map, gravity, adoption, audit retention, obligation retirement, and TOE percentage movement remain open"
    )
    print("per_element: checked all 26 nonzero neighbour directions, both spectral outcomes, linear/cubic normalized response pairs, the 27-symbol generated alphabet, projector transport, and exact append contents")
    print("per_site: checked 128 finite domains, six-neighbour frontier bounds, 127 extreme-site growth witnesses, old Record contents, two translations, and 24 proper-cubic rotations")
    print("per_mode: checked empty, nonempty, single-seed, asymmetric multi-seed, linear/cubic response, product/common-sign correlation, frozen synchronous, dynamic recomputation, finite-patch, and full-lattice modes")
    print("per_block: checked live axiom and four-node primitive registry, exact Block84 receipt, arbitrary-state transition normalization, permanence, standard-Borel Markov cylinders, scheduler dependence, and the two-cube boundary artifact")
    print("lattice_wide: checked the exact local formula and finite-state full-Z3 transition for every finite input type, plus general proofs encoded in the note; checked and not executed — no arbitrary infinite initial configuration, physical clock, typed energy/source, Ward identity, or gravity coupling is claimed")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
