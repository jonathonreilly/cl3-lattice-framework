#!/usr/bin/env python3
"""Independent integer/rational checks for the finite Record Markov result."""

from __future__ import annotations

import json
from fractions import Fraction
from hashlib import sha256
from itertools import permutations, product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 30

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_FINITE_STATE_MARKOV_COMPLETION_BOUNDED_THEOREM_NOTE_"
    "2026-08-14.md"
)
PRIMARY_PATH = ROOT / "scripts" / (
    "frontier_admissibility_finite_state_markov_completion_2026_08_14.py"
)
PRIMARY_CACHE = ROOT / "logs" / "runner-cache" / (
    "frontier_admissibility_finite_state_markov_completion_2026_08_14.txt"
)
PARENT_RUNNER = ROOT / "scripts" / (
    "frontier_admissibility_taxicab_shell_record_instrument_2026_08_14.py"
)
PARENT_CACHE = ROOT / "logs" / "runner-cache" / (
    "frontier_admissibility_taxicab_shell_record_instrument_2026_08_14.txt"
)

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_FINITE_STATE_MARKOV_COMPLETION_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "scripts/frontier_admissibility_finite_state_markov_completion_2026_08_14.py",
    "logs/runner-cache/frontier_admissibility_finite_state_markov_completion_2026_08_14.txt",
    "scripts/frontier_admissibility_taxicab_shell_record_instrument_2026_08_14.py",
    "logs/runner-cache/frontier_admissibility_taxicab_shell_record_instrument_2026_08_14.txt",
)

# Exact frozen primary identities from the bounded final retry.
PRIMARY_SHA256 = "40d9744eeee5be137785d6f5ce18dc41bc02c4fc74d8c7e2689f2a4f0b4b1464"
PRIMARY_CACHE_SHA256 = "6bf65e31a932a8180600d298d44d626d80d7bffdbb7d54605083a112adf77350"
PARENT_RUNNER_SHA256 = "cad56c96f1b35dd1a4aba755aadabef52a33330ba1cf1b603667778079c43139"
PARENT_CACHE_SHA256 = "50e76fa95c78d2055838808eba8ff088163377a1fa5e46121f18489cb9cd36f9"

Site = tuple[int, int, int]
Rotation = tuple[tuple[int, int, int], tuple[int, int, int], tuple[int, int, int]]
AXES: tuple[Site, Site, Site] = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
STEPS: tuple[Site, ...] = tuple(
    tuple(sign * value for value in axis)
    for axis in AXES
    for sign in (-1, 1)
)  # type: ignore[assignment]
ORIGIN: Site = (0, 0, 0)


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


def add(left: Site, right: Site) -> Site:
    return tuple(left[i] + right[i] for i in range(3))  # type: ignore[return-value]


def difference(site: Site, domain: set[Site] | frozenset[Site]) -> Site:
    return tuple(
        int(add(site, axis) in domain)
        - int(add(site, tuple(-value for value in axis)) in domain)
        for axis in AXES
    )  # type: ignore[return-value]


def frontier(domain: set[Site] | frozenset[Site]) -> frozenset[Site]:
    candidates = {add(site, step) for site in domain for step in STEPS}
    return frozenset(
        site
        for site in candidates - set(domain)
        if difference(site, domain) != (0, 0, 0)
    )


def determinant(rotation: Rotation) -> int:
    a, b, c = rotation
    return (
        a[0] * (b[1] * c[2] - b[2] * c[1])
        - a[1] * (b[0] * c[2] - b[2] * c[0])
        + a[2] * (b[0] * c[1] - b[1] * c[0])
    )


def apply(rotation: Rotation, site: Site) -> Site:
    return tuple(
        sum(rotation[row][column] * site[column] for column in range(3))
        for row in range(3)
    )  # type: ignore[return-value]


def proper_signed_permutations() -> tuple[Rotation, ...]:
    rotations = set()
    for permutation in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            rows = []
            for row in range(3):
                entries = [0, 0, 0]
                entries[permutation[row]] = signs[row]
                rows.append(tuple(entries))
            rotation: Rotation = tuple(rows)  # type: ignore[assignment]
            if determinant(rotation) == 1:
                rotations.add(rotation)
    return tuple(sorted(rotations))


def finite_geometry_control() -> dict[str, int]:
    host = (
        (0, 0, 0),
        (2, 0, 0),
        (-1, 2, 0),
        (0, 1, -2),
        (3, -1, 1),
        (1, 1, 0),
        (0, -1, 0),
    )
    failures = 0
    growth_failures = 0
    for mask in range(1 << len(host)):
        domain = frozenset(
            site for index, site in enumerate(host) if mask & (1 << index)
        )
        formed = frontier(domain)
        failures += bool(set(domain) & set(formed))
        failures += len(formed) > 6 * len(domain)
        failures += any(difference(site, domain) == (0, 0, 0) for site in formed)
        if domain:
            extreme = max(domain, key=lambda site: (site[0], site[1], site[2]))
            witness = add(extreme, (1, 0, 0))
            growth_failures += witness not in formed
            growth_failures += difference(witness, domain)[0] != -1
    return {
        "domains": 1 << len(host),
        "frontier_failures": failures,
        "growth_witnesses": (1 << len(host)) - 1,
        "growth_failures": growth_failures,
    }


def covariance_control() -> dict[str, int]:
    host = ((0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1), (-1, 0, 0))
    rotations = proper_signed_permutations()
    failures = 0
    direction_failures = 0
    for mask in range(1 << len(host)):
        domain = frozenset(
            site for index, site in enumerate(host) if mask & (1 << index)
        )
        for rotation in rotations:
            rotated_domain = frozenset(apply(rotation, site) for site in domain)
            failures += frontier(rotated_domain) != frozenset(
                apply(rotation, site) for site in frontier(domain)
            )
            for site in frontier(domain):
                direction_failures += difference(
                    apply(rotation, site), rotated_domain
                ) != apply(rotation, difference(site, domain))
    return {
        "rotations": len(rotations),
        "domains": 1 << len(host),
        "frontier_failures": failures,
        "direction_failures": direction_failures,
    }


def normalization_control() -> dict[str, object]:
    directions = tuple(
        direction
        for direction in product((-1, 0, 1), repeat=3)
        if direction != (0, 0, 0)
    )
    k_values = tuple(sum(value * value for value in direction) for direction in directions)
    local_formula_valid = all(k in (1, 2, 3) and 0 < k < 9 for k in k_values)

    mass = Fraction(0)
    distinct_assignments = set()
    for signs in product((-1, 1), repeat=6):
        plus_count = signs.count(1)
        mass += Fraction(2, 3) ** plus_count * Fraction(1, 3) ** (6 - plus_count)
        distinct_assignments.add(signs)
    return {
        "directions": len(directions),
        "k_values": tuple(sorted(set(k_values))),
        "local_formula_valid": local_formula_valid,
        "seed_atoms": len(distinct_assignments),
        "seed_mass": mass,
    }


def scheduler_and_patch_control() -> dict[str, object]:
    seed = frozenset({ORIGIN})
    frozen = frontier(seed)
    first = min(frozen)
    dynamic_extra = frontier(seed | {first}) - frozen

    patch = frozenset(product(range(3), range(2), range(2)))
    state = seed
    waves = []
    for _ in range(5):
        formed = frontier(state) & patch
        waves.append(len(formed))
        state |= formed
    outside = frontier(state)
    patch_filled = state == patch

    shells = []
    state = seed
    for _ in range(6):
        formed = frontier(state)
        shells.append(len(formed))
        state |= formed
    return {
        "frozen": len(frozen),
        "dynamic_extra": len(dynamic_extra),
        "dynamic_extra_sites": tuple(sorted(dynamic_extra)),
        "waves": tuple(waves),
        "patch_filled": patch_filled,
        "outside": len(outside),
        "shells": tuple(shells),
    }


def primary_claims() -> dict[str, object]:
    for relative in AUDIT_INPUT_PATHS:
        (ROOT / relative).read_text(encoding="utf-8")
    cache = PRIMARY_CACHE.read_text(encoding="utf-8")
    claim_lines = [line for line in cache.splitlines() if line.startswith("CLAIMS_JSON ")]
    if len(claim_lines) != 1:
        raise ValueError("primary cache must contain exactly one CLAIMS_JSON line")
    return json.loads(claim_lines[0].split(" ", 1)[1])


def main() -> int:
    checks = Checks()
    print("independent_route: stdlib integer frontier/covariance and rational seed normalization")
    print("scientific_imports: none")

    claims = primary_claims()
    note = NOTE_PATH.read_text(encoding="utf-8")
    primary_cache_text = PRIMARY_CACHE.read_text(encoding="utf-8")
    parent_cache_text = PARENT_CACHE.read_text(encoding="utf-8")
    pins_ok = (
        file_sha256(PRIMARY_PATH) == PRIMARY_SHA256
        and file_sha256(PRIMARY_CACHE) == PRIMARY_CACHE_SHA256
        and file_sha256(PARENT_RUNNER) == PARENT_RUNNER_SHA256
        and file_sha256(PARENT_CACHE) == PARENT_CACHE_SHA256
        and "TOTAL: PASS=10 FAIL=0" in primary_cache_text
        and "TOTAL: PASS=26 FAIL=0" in parent_cache_text
        and all((ROOT / relative).is_file() for relative in AUDIT_INPUT_PATHS)
    )
    checks.check(
        "A-source-cache-and-input-pins",
        pins_ok,
        "the exact primary and corrected parent source/cache pairs plus five literal checker inputs are present",
    )

    geometry = finite_geometry_control()
    checks.check(
        "B-independent-frontier-and-growth",
        geometry["domains"] == 128
        and geometry["frontier_failures"] == 0
        and geometry["growth_witnesses"] == 127
        and geometry["growth_failures"] == 0,
        "an asymmetric seven-site host gives 128 valid frontier cases and 127 extreme-site witnesses",
    )

    covariance = covariance_control()
    checks.check(
        "C-independent-proper-cubic-geometry",
        covariance["rotations"] == 24
        and covariance["domains"] == 32
        and covariance["frontier_failures"] == 0
        and covariance["direction_failures"] == 0,
        "direct signed-permutation generation transports frontiers and directions on 32 domains",
    )

    normalization = normalization_control()
    checks.check(
        "D-independent-local-and-seed-normalization",
        normalization["directions"] == 26
        and normalization["k_values"] == (1, 2, 3)
        and normalization["local_formula_valid"]
        and normalization["seed_atoms"] == 64
        and normalization["seed_mass"] == 1,
        "26 local directions have k<9 and the independently enumerated 64-atom seed mass is one",
    )

    scheduler = scheduler_and_patch_control()
    checks.check(
        "E-independent-scheduler-operand",
        scheduler["frozen"] == 6 and scheduler["dynamic_extra"] == 5,
        "an actual in-place first write exposes five sites outside the frozen six-site frontier",
    )
    checks.check(
        "F-independent-patch-boundary",
        scheduler["waves"] == (3, 4, 3, 1, 0)
        and scheduler["patch_filled"]
        and scheduler["outside"] == 32
        and scheduler["shells"] == (6, 18, 38, 66, 102, 146),
        "the restricted patch waves, full-lattice outside frontier, and first six seed shells match the claimed values",
    )

    expected_claims = {
        "claim_type": "bounded_theorem",
        "declared_inputs": 14,
        "frontier_domains": 128,
        "local_directions": 26,
        "seed_atoms": 64,
        "covariance_rotations": 24,
        "growth_witnesses": 127,
        "dynamic_extra_sites": 5,
        "patch_waves": [3, 4, 3, 1, 0],
        "patch_outside": 32,
        "physical_time_supplied": False,
        "physical_law_adopted": False,
        "audit_status": "unset",
    }
    scope_ok = (
        claims == expected_claims
        and "standard-Borel" in note
        and "iteration ordinal" in note
        and "No physical law is selected or adopted" in note
        and "arbitrary infinite initial states" in note
        and "No audit has run" in note
    )
    checks.check(
        "G-primary-claims-and-proof-boundary",
        scope_ok,
        "the exact primary claims are reproduced and the note keeps finite proof, physical-law, time, infinite-state, and audit scopes explicit",
    )

    summary = {
        "claim_type": "bounded_theorem",
        "host_domains": geometry["domains"],
        "growth_witnesses": geometry["growth_witnesses"],
        "proper_rotations": covariance["rotations"],
        "seed_atoms": normalization["seed_atoms"],
        "dynamic_extra_sites": scheduler["dynamic_extra"],
        "patch_outside": scheduler["outside"],
        "audit_status": "unset",
    }
    print("CHECKER_JSON " + json.dumps(summary, sort_keys=True))
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
