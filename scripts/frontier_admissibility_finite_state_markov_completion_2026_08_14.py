#!/usr/bin/env python3
"""Bounded checks for one supplied finite-state Record Markov kernel.

The adjacent note proves the general finite-domain and standard-Borel
statements. This runner checks the exact local algebra, current Block84 source
binding, finite implementation, covariance, growth, scheduler, and boundary
controls. It does not select a physical law or identify an iteration with
physical time.
"""

from __future__ import annotations

import json
from hashlib import sha256
from itertools import combinations, product
from pathlib import Path

import sympy as sp

import frontier_admissibility_taxicab_shell_record_instrument_2026_08_14 as block84


AUDIT_TIMEOUT_SEC = 30

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_FINITE_STATE_MARKOV_COMPLETION_BOUNDED_THEOREM_NOTE_"
    "2026-08-14.md"
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

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_FINITE_STATE_MARKOV_COMPLETION_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/ADMISSIBILITY_TAXICAB_SHELL_RECORD_INSTRUMENT_CYLINDER_LAW_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md",
    "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
    "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md",
    "docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md",
    "docs/ADMISSIBILITY_BARYCENTER_EVALUATION_MENU_KERNEL_BOUNDED_THEOREM_NOTE_2026-08-12.md",
    "docs/BORN_FORM_FROM_BINARY_TERNARY_SCALED_PROJECTOR_FRAME_LIFT_BOUNDED_THEOREM_NOTE_2026-08-09.md",
    "docs/ADMISSIBILITY_REGISTERED_PARTITION_BARYCENTER_PUSHFORWARD_BOUNDED_THEOREM_NOTE_2026-08-12.md",
    "docs/RECORD_CONTENT_ONLY_SHARED_EFFECT_DESCENT_BOUNDED_THEOREM_NOTE_2026-08-12.md",
    "scripts/frontier_admissibility_taxicab_shell_record_instrument_2026_08_14.py",
    "logs/runner-cache/frontier_admissibility_taxicab_shell_record_instrument_2026_08_14.txt",
)

PARENT_SHA256 = {
    PARENT_NOTE: "28e0f8c2e5e77a02b511783a0e29aef8edbbc837d8cdee686603585b96bd8f4b",
    PARENT_RUNNER: "cad56c96f1b35dd1a4aba755aadabef52a33330ba1cf1b603667778079c43139",
    PARENT_CACHE: "50e76fa95c78d2055838808eba8ff088163377a1fa5e46121f18489cb9cd36f9",
}

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


def domains(host: tuple[Site, ...], include_empty: bool = True):
    start = 0 if include_empty else 1
    for count in range(start, len(host) + 1):
        for subset in combinations(host, count):
            yield frozenset(subset)


def matrix_key(matrix: sp.MatrixBase) -> tuple[sp.Expr, ...]:
    return tuple(sp.simplify(value) for value in matrix)


def current_input_certificate() -> dict[str, object]:
    helper_inputs = tuple(AUDIT_INPUT_PATHS[1:12])
    paths_exist = all((ROOT / relative).is_file() for relative in AUDIT_INPUT_PATHS)
    input_bytes = sum(
        len((ROOT / relative).read_bytes()) for relative in AUDIT_INPUT_PATHS
    )
    parent_hashes = {path: file_sha256(path) for path in PARENT_SHA256}
    cache = PARENT_CACHE.read_text(encoding="utf-8")
    return {
        "declared_inputs": len(AUDIT_INPUT_PATHS),
        "paths_exist": paths_exist,
        "input_bytes": input_bytes,
        "helper_inputs_match": helper_inputs == tuple(block84.AUDIT_INPUT_PATHS),
        "parent_hashes_match": parent_hashes == PARENT_SHA256,
        "parent_total": "TOTAL: PASS=26 FAIL=0" in cache,
        "parent_projector_covariance": (
            "PASS: proper-cubic-covariance all projectors, k sectors, weights, "
            "and B_t geometries transform covariantly" in cache
        ),
        "parent_stderr_empty": cache.rstrip().endswith("----- stderr -----"),
    }


def finite_frontier_certificate() -> dict[str, int]:
    host = (
        (0, 0, 0),
        (1, 0, 0),
        (0, 1, 0),
        (0, 0, 1),
        (-1, 0, 0),
        (0, -1, 0),
        (0, 0, -1),
    )
    failures = 0
    cases = 0
    maximum_frontier = 0
    for domain in domains(host):
        frontier = block84.candidate_frontier(domain)
        failures += bool(set(frontier) & set(domain))
        failures += len(frontier) > 6 * len(domain)
        for site in frontier:
            failures += not any(
                block84.add(site, step) in domain
                for axis in block84.AXES
                for step in (axis, tuple(-value for value in axis))
            )
            failures += block84.neighbour_difference(site, domain) == (0, 0, 0)
        maximum_frontier = max(maximum_frontier, len(frontier))
        cases += 1
    return {
        "cases": cases,
        "failures": failures,
        "maximum_frontier": maximum_frontier,
    }


def local_kernel_certificate() -> dict[str, object]:
    directions = tuple(
        direction
        for direction in product((-1, 0, 1), repeat=3)
        if direction != (0, 0, 0)
    )
    local_failures = 0
    projector_alphabet: set[tuple[sp.Expr, ...]] = set()
    for direction in directions:
        k = block84.k_value(direction)
        plus = block84.projector(direction, 1)
        minus = block84.projector(direction, -1)
        projector_alphabet.update((matrix_key(plus), matrix_key(minus)))
        local_failures += k not in (1, 2, 3)
        local_failures += not block84.matrix_equal(plus * plus, plus)
        local_failures += not block84.matrix_equal(minus * minus, minus)
        local_failures += not block84.matrix_equal(plus + minus, block84.I2)
        local_failures += not block84.matrix_equal(plus * minus, sp.zeros(2))
        local_failures += block84.matrix_equal(plus, minus)
        weights = {
            sign: block84.response_weight(k, sign, 1) for sign in (-1, 1)
        }
        local_failures += sp.simplify(sum(weights.values()) - 1) != 0
        local_failures += any(
            weight.is_positive is not True for weight in weights.values()
        )

    seed = frozenset({block84.ORIGIN})
    frontier = tuple(sorted(block84.candidate_frontier(seed)))
    atom_keys: set[tuple[tuple[sp.Expr, ...], ...]] = set()
    mass = sp.Integer(0)
    for signs in product((-1, 1), repeat=len(frontier)):
        probability = sp.Integer(1)
        atom = []
        for site, sign in zip(frontier, signs):
            direction = block84.neighbour_difference(site, seed)
            probability *= block84.response_weight(
                block84.k_value(direction), sign, 1
            )
            atom.append(matrix_key(block84.projector(direction, sign)))
        atom_keys.add(tuple(atom))
        mass += probability

    host = ((0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1), (-1, 0, 0))
    normalization_failures = 0
    domain_cases = 0
    for domain in domains(host):
        normalizer = sp.Integer(1)
        for site in block84.candidate_frontier(domain):
            direction = block84.neighbour_difference(site, domain)
            k = block84.k_value(direction)
            normalizer *= sum(
                block84.response_weight(k, sign, 1) for sign in (-1, 1)
            )
        normalization_failures += sp.simplify(normalizer - 1) != 0
        domain_cases += 1

    return {
        "directions": len(directions),
        "local_failures": local_failures,
        "projector_alphabet": len(projector_alphabet),
        "domain_cases": domain_cases,
        "normalization_failures": normalization_failures,
        "seed_frontier": len(frontier),
        "seed_atoms": len(atom_keys),
        "seed_mass": sp.simplify(mass),
        "empty_identity_atom": block84.candidate_frontier(frozenset()) == frozenset(),
    }


def content_table(domain: frozenset[Site], variant: int) -> RecordMap:
    directions: tuple[Vec, ...] = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    if variant == 0:
        return {site: Content(block84.I2 / 2) for site in domain}
    return {
        site: Content(
            block84.projector(
                directions[index % len(directions)],
                1 if sum(site) % 2 == 0 else -1,
            )
        )
        for index, site in enumerate(sorted(domain))
    }


def permanence_certificate() -> dict[str, int]:
    host = ((0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1), (-1, 0, 0))
    content_blind_failures = 0
    permanence_failures = 0
    support_failures = 0
    cases = 0
    for domain in domains(host, include_empty=False):
        left = content_table(domain, 0)
        right = content_table(domain, 1)
        left_frontier = block84.candidate_frontier(frozenset(left))
        right_frontier = block84.candidate_frontier(frozenset(right))
        content_blind_failures += left_frontier != right_frontier

        signs = {site: block84.deterministic_sign(site) for site in left_frontier}
        updated = block84.finite_record_update(left, signs)
        permanence_failures += not block84.preserves_records(left, updated)
        for site in left_frontier:
            expected = block84.projector(
                block84.neighbour_difference(site, domain), signs[site]
            )
            support_failures += not block84.matrix_equal(
                sp.Matrix(updated[site]), expected
            )
        cases += 1
    return {
        "cases": cases,
        "content_blind_failures": content_blind_failures,
        "permanence_failures": permanence_failures,
        "support_failures": support_failures,
    }


def rotate_domain(rotation: Rotation, domain: frozenset[Site]) -> frozenset[Site]:
    return frozenset(block84.rotate(rotation, site) for site in domain)


def translate_domain(offset: Site, domain: frozenset[Site]) -> frozenset[Site]:
    return frozenset(block84.add(offset, site) for site in domain)


def covariance_certificate() -> dict[str, int]:
    host = ((0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1), (-1, 0, 0))
    test_domains = tuple(domains(host))
    directions = tuple(
        direction
        for direction in product((-1, 0, 1), repeat=3)
        if direction != (0, 0, 0)
    )
    lifts = block84.proper_cubic_lifts()
    geometry_failures = 0
    direction_failures = 0
    weight_failures = 0
    for rotation, _unitary in lifts:
        for domain in test_domains:
            rotated_domain = rotate_domain(rotation, domain)
            geometry_failures += (
                block84.candidate_frontier(rotated_domain)
                != rotate_domain(rotation, block84.candidate_frontier(domain))
            )
            for site in block84.candidate_frontier(domain):
                rotated_site = block84.rotate(rotation, site)
                direction_failures += block84.neighbour_difference(
                    rotated_site, rotated_domain
                ) != block84.rotate(
                    rotation, block84.neighbour_difference(site, domain)
                )
        for direction in directions:
            rotated = block84.rotate(rotation, direction)
            weight_failures += (
                block84.k_value(rotated) != block84.k_value(direction)
            )
            for sign in (-1, 1):
                weight_failures += sp.simplify(
                    block84.response_weight(block84.k_value(direction), sign, 1)
                    - block84.response_weight(block84.k_value(rotated), sign, 1)
                ) != 0

    translation_failures = 0
    for offset in ((3, -2, 1), (-4, 1, 2)):
        for domain in test_domains:
            translated = translate_domain(offset, domain)
            translation_failures += (
                block84.candidate_frontier(translated)
                != translate_domain(offset, block84.candidate_frontier(domain))
            )
    return {
        "rotations": len(lifts),
        "domain_cases": len(test_domains),
        "geometry_failures": geometry_failures,
        "direction_failures": direction_failures,
        "weight_failures": weight_failures,
        "translation_failures": translation_failures,
    }


def extreme_growth_witness(domain: frozenset[Site]) -> tuple[Site, Site, Vec]:
    if not domain:
        raise ValueError("nonempty finite domain required")
    extreme = max(domain, key=lambda site: (site[0], site[1], site[2]))
    witness = block84.add(extreme, E1)
    return extreme, witness, block84.neighbour_difference(witness, domain)


def distance_to_domain(site: Site, domain: frozenset[Site]) -> int:
    return min(block84.taxicab_norm(block84.sub(site, source)) for source in domain)


def growth_certificate() -> dict[str, int | bool]:
    host = (
        (0, 0, 0),
        (1, 0, 0),
        (0, 1, 0),
        (0, 0, 1),
        (-1, 0, 0),
        (0, -1, 0),
        (0, 0, -1),
    )
    witness_failures = 0
    nonempty_cases = 0
    for domain in domains(host, include_empty=False):
        extreme, witness, direction = extreme_growth_witness(domain)
        witness_failures += witness in domain
        witness_failures += block84.add(witness, E1) in domain
        witness_failures += block84.sub(witness, E1) != extreme
        witness_failures += direction[0] != -1
        witness_failures += witness not in block84.candidate_frontier(domain)
        nonempty_cases += 1

    propagation_failures = 0
    histories = 0
    initial_domains = (
        frozenset({(0, 0, 0)}),
        frozenset({(0, 0, 0), (1, 0, 0)}),
        frozenset({(0, 0, 0), (1, 0, 0), (0, 1, 0)}),
    )
    for initial in initial_domains:
        current = initial
        for tick in range(1, 6):
            frontier = block84.candidate_frontier(current)
            propagation_failures += any(
                distance_to_domain(site, initial) > tick for site in frontier
            )
            current |= frontier
            histories += 1

    seed_failures = 0
    seed = frozenset({block84.ORIGIN})
    for tick in range(1, 7):
        seed |= block84.candidate_frontier(seed)
        seed_failures += seed != block84.taxicab_ball(tick)
    return {
        "nonempty_cases": nonempty_cases,
        "witness_failures": witness_failures,
        "propagation_histories": histories,
        "propagation_failures": propagation_failures,
        "seed_failures": seed_failures,
        "empty_fixed": block84.candidate_frontier(frozenset()) == frozenset(),
    }


def scheduler_certificate() -> dict[str, object]:
    seed = frozenset({block84.ORIGIN})
    frozen_frontier = block84.candidate_frontier(seed)
    first = min(frozen_frontier)
    dynamic_frontier = block84.candidate_frontier(seed | {first})
    dynamic_extra = dynamic_frontier - frozen_frontier

    signs = {site: block84.deterministic_sign(site) for site in frozen_frontier}
    reference = block84.finite_record_update(content_table(seed, 0), signs)
    order_failures = 0
    orders = (
        tuple(sorted(frozen_frontier)),
        tuple(reversed(sorted(frozen_frontier))),
        tuple(sorted(frozen_frontier)[2:] + sorted(frozen_frontier)[:2]),
    )
    for order in orders:
        updated = content_table(seed, 0)
        old_domain = frozenset(updated)
        for site in order:
            direction = block84.neighbour_difference(site, old_domain)
            updated[site] = Content(block84.projector(direction, signs[site]))
        order_failures += updated != reference
    return {
        "frozen_frontier": len(frozen_frontier),
        "dynamic_extra": len(dynamic_extra),
        "dynamic_extra_sites": tuple(sorted(dynamic_extra)),
        "order_failures": order_failures,
    }


def patch_certificate() -> dict[str, object]:
    patch = block84.two_cube_patch()
    state = frozenset({block84.ORIGIN})
    waves = []
    for _ in range(5):
        frontier = block84.patch_frontier(state, patch)
        waves.append(len(frontier))
        state |= frontier
    outside = block84.candidate_frontier(state)
    seed = frozenset({block84.ORIGIN})
    shells = []
    for _ in range(6):
        frontier = block84.candidate_frontier(seed)
        shells.append(len(frontier))
        seed |= frontier
    return {
        "patch_sites": len(patch),
        "waves": tuple(waves),
        "patch_filled": state == patch,
        "outside": len(outside),
        "shells": tuple(shells),
    }


def history_certificate() -> dict[str, object]:
    seed = frozenset({block84.ORIGIN})
    state = seed
    normalization_failures = 0
    path_factor_failures = 0
    path_factors = 0
    frontier_sizes = []
    for _step in range(4):
        frontier = block84.candidate_frontier(state)
        frontier_sizes.append(len(frontier))
        normalizer = sp.Integer(1)
        for site in frontier:
            direction = block84.neighbour_difference(site, state)
            k = block84.k_value(direction)
            normalizer *= sum(
                block84.response_weight(k, sign, 1) for sign in (-1, 1)
            )
            chosen = block84.deterministic_sign(site)
            weight = block84.response_weight(k, chosen, 1)
            path_factor_failures += weight.is_positive is not True
            path_factor_failures += (1 - weight).is_nonnegative is not True
            path_factors += 1
        normalization_failures += sp.simplify(normalizer - 1) != 0
        state |= frontier
    note = NOTE_PATH.read_text(encoding="utf-8")
    proof_tokens = (
        "finite-dimensional and Polish",
        "standard-Borel",
        "Borel probability kernel",
        "iterated-kernel construction",
        "iteration ordinal",
    )
    return {
        "frontier_sizes": tuple(frontier_sizes),
        "normalization_failures": normalization_failures,
        "path_factors": path_factors,
        "path_factor_failures": path_factor_failures,
        "proof_surface_complete": all(token in note for token in proof_tokens),
    }


def selection_certificate() -> dict[str, object]:
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
            value.is_positive is not True
            for value in (*linear.values(), *cubic.values())
        )
        distinct_sectors += any(
            sp.simplify(linear[sign] - cubic[sign]) != 0 for sign in (-1, 1)
        )
    product_values = block84.binomial_frequency_moments(2, 4, 1)
    correlated_values = block84.common_sign_frequency_moments(2, 4, 1)
    note = NOTE_PATH.read_text(encoding="utf-8")
    return {
        "response_failures": response_failures,
        "distinct_sectors": distinct_sectors,
        "product_normalization": product_values[0],
        "correlated_normalization": correlated_values[0],
        "same_mean": sp.simplify(product_values[1] - correlated_values[1]) == 0,
        "different_variance": sp.simplify(product_values[2] - correlated_values[2]) != 0,
        "scope_tokens": all(
            token in note
            for token in (
                "No physical law is selected or adopted",
                "arbitrary infinite initial states",
                "iteration ordinal",
                "audit retention",
                "TOE percentage movement",
            )
        ),
    }


def main() -> int:
    checks = Checks()
    print("external_scientific_inputs: none")
    print(
        "package_local_inputs: corrected Block84 source/cache and its eleven declared text inputs"
    )
    print(
        "claim_boundary: one supplied finite-state kernel; no adopted law, physical time, infinite-state process, source, or gravity"
    )

    inputs = current_input_certificate()
    checks.check(
        "A-current-Block84-and-input-closure",
        inputs["declared_inputs"] == 14
        and inputs["paths_exist"]
        and inputs["input_bytes"] > 0
        and inputs["helper_inputs_match"]
        and inputs["parent_hashes_match"]
        and inputs["parent_total"]
        and inputs["parent_projector_covariance"]
        and inputs["parent_stderr_empty"],
        "14 literal inputs bind the corrected parent triple and its complete eleven-text-input closure",
    )

    frontier = finite_frontier_certificate()
    checks.check(
        "B-finite-frontier",
        frontier["cases"] == 128 and frontier["failures"] == 0,
        f"{frontier['cases']} domains satisfy disjointness, adjacency, nonzero direction, and |F(D)|<=6|D|",
    )

    kernel = local_kernel_certificate()
    checks.check(
        "C-normalized-finite-atomic-kernel",
        kernel["directions"] == 26
        and kernel["local_failures"] == 0
        and kernel["projector_alphabet"] == 26
        and kernel["domain_cases"] == 32
        and kernel["normalization_failures"] == 0
        and kernel["seed_frontier"] == 6
        and kernel["seed_atoms"] == 64
        and kernel["seed_mass"] == 1
        and kernel["empty_identity_atom"],
        "all 26 directions have two positive normalized projector branches; the seed has 64 distinct atoms of total mass one",
    )

    permanence = permanence_certificate()
    checks.check(
        "D-content-blind-supported-permanent-update",
        permanence["cases"] == 31
        and permanence["content_blind_failures"] == 0
        and permanence["permanence_failures"] == 0
        and permanence["support_failures"] == 0,
        "31 nonempty domains with two content tables have the same frontier; old contents persist and appended contents match the supplied projectors",
    )

    covariance = covariance_certificate()
    checks.check(
        "E-conditional-complete-kernel-covariance",
        covariance["rotations"] == 24
        and covariance["domain_cases"] == 32
        and covariance["geometry_failures"] == 0
        and covariance["direction_failures"] == 0
        and covariance["weight_failures"] == 0
        and covariance["translation_failures"] == 0,
        "32 domains under 24 proper rotations and two translations transport frontiers, directions, and weights; the pinned corrected parent certifies projector transport",
    )

    history = history_certificate()
    checks.check(
        "F-finite-history-and-Borel-proof-prerequisites",
        history["frontier_sizes"] == (6, 18, 38, 66)
        and history["normalization_failures"] == 0
        and history["path_factors"] == 128
        and history["path_factor_failures"] == 0
        and history["proof_surface_complete"],
        "four normalized finite steps give a positive bounded cylinder; the note carries the separate standard-Borel stratum proof",
    )

    growth = growth_certificate()
    checks.check(
        "G-finite-state-growth-and-propagation",
        growth["nonempty_cases"] == 127
        and growth["witness_failures"] == 0
        and growth["propagation_histories"] == 15
        and growth["propagation_failures"] == 0
        and growth["seed_failures"] == 0
        and growth["empty_fixed"],
        "127 nonempty hostile domains realize the extreme-site witness; 15 histories stay within one edge per iteration and the seed gives six exact balls",
    )

    scheduler = scheduler_certificate()
    checks.check(
        "H-actual-frozen-versus-in-place-scheduler",
        scheduler["frozen_frontier"] == 6
        and scheduler["dynamic_extra"] == 5
        and scheduler["order_failures"] == 0,
        "three frozen-prestate append orders agree, while an actual first in-place write exposes five additional candidates",
    )

    patch = patch_certificate()
    checks.check(
        "I-finite-patch-boundary",
        patch["patch_sites"] == 12
        and patch["waves"] == (3, 4, 3, 1, 0)
        and patch["patch_filled"]
        and patch["outside"] == 32
        and patch["shells"] == (6, 18, 38, 66, 102, 146),
        "the restricted patch fills in waves 3,4,3,1,0, while its full-lattice embedding has 32 outside candidates",
    )

    selection = selection_certificate()
    checks.check(
        "J-selection-and-physical-boundary",
        selection["response_failures"] == 0
        and selection["distinct_sectors"] == 3
        and selection["product_normalization"] == 1
        and selection["correlated_normalization"] == 1
        and selection["same_mean"]
        and selection["different_variance"]
        and selection["scope_tokens"],
        "linear/cubic and product/correlated alternatives remain distinct; the note keeps law choice, physical time, infinite states, source, gravity, and audit open",
    )

    claims = {
        "claim_type": "bounded_theorem",
        "declared_inputs": inputs["declared_inputs"],
        "frontier_domains": frontier["cases"],
        "local_directions": kernel["directions"],
        "seed_atoms": kernel["seed_atoms"],
        "covariance_rotations": covariance["rotations"],
        "growth_witnesses": growth["nonempty_cases"],
        "dynamic_extra_sites": scheduler["dynamic_extra"],
        "patch_waves": list(patch["waves"]),
        "patch_outside": patch["outside"],
        "physical_time_supplied": False,
        "physical_law_adopted": False,
        "audit_status": "unset",
    }
    print("CLAIMS_JSON " + json.dumps(claims, sort_keys=True))
    print(
        "per_element: all 26 nonzero directions have exact complementary projectors and positive normalized linear weights"
    )
    print(
        "per_site: finite frontier, supported append, and extreme-site growth predicates are checked on the declared hostile domains"
    )
    print(
        "per_mode: empty/nonempty, frozen/dynamic, finite-patch/full-lattice, linear/cubic, and product/correlated controls are distinguished"
    )
    print(
        "per_block: corrected Block84 source/cache/input closure, finite kernel, covariance, histories, scheduler, and boundary are checked"
    )
    print(
        "lattice_wide: general finite-domain conclusions follow from the adjacent proofs; arbitrary infinite states and physical spacetime are unasserted"
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
