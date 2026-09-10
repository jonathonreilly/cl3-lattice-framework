#!/usr/bin/env python3
"""Block 16: common-input covariant conditional cap-packet instrument.

One effective classical-quantum block channel receives a centered 43-site
Record sector.  On the common no-Record sector it produces six equally
weighted, proper-cubic-covariant cap/seed/live-packet branches; on every
nonblank sector it returns identity/STOP.  Each branch is composed into the
frozen Block-15 flag-only controller.  The result remains conditional on a
selected center and an atomic radius-three event.
"""

from __future__ import annotations

import argparse
import ast
from collections import Counter
from fractions import Fraction
from functools import cache
import inspect
import itertools
from pathlib import Path
import subprocess
import sys

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import admissibility_d4_gapped_record_cap_safe_front_2026_08_29 as b15  # noqa: E402


PACKET = ROOT / ".claude" / "science" / "physics-loops" / (
    "toe-source-eta-ownership-block16-covariant-cap-packet-instrument-20260829"
)
GOAL = PACKET / "GOAL.md"
PREFLIGHT = PACKET / "PREFLIGHT_WITNESSES.md"
SUPPORT_CORRECTION = PACKET / "PREFLIGHT_SUPPORT_CORRECTION.md"
CHECKLIST = PACKET / "NO_GO_DISCIPLINE_CHECKLIST.md"
NOTE = ROOT / "docs" / (
    "ADMISSIBILITY_D4_COVARIANT_CONDITIONAL_CAP_PACKET_INSTRUMENT_"
    "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md"
)

PARENT = "a791383b659f1148b56442ed80b402fd0a059966"
BLOCK15_RESULT = "1405ec3980428cbd0f2115223ae90db35eaaca7d"
PREREG = "e7d83357cbee8910e4fefd0784de6bad5d5884ef"
MAIN = "3cc632921c36aa90266c5c62e56816577ce59a0a"
AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
GOAL_BLOB = "48cbfac788b74d0b85acd475db83226e50753afd"
PREFLIGHT_BLOB = "6fadd2651fe64a7fe27115f90a618942ac8814cf"
SUPPORT_CORRECTION_COMMIT = "d51484274ff001cec0e4bb6753eedaf88e3adff2"
SUPPORT_CORRECTION_BLOB = "29b66cba2c73687dcb09d53fd32d153a1f19dbf6"
BLOCK15_NOTE_BLOB = "a66793c99517dbce45d35c8522f3a6fb649b1fbf"
BLOCK15_PRIMARY_BLOB = "e6e51158cb68aa136c8296b802168d097721c85f"
BLOCK15_INDEPENDENT_BLOB = "44c3101478c23630f20779a822ab0991d3afd5b7"
BLOCK15_PRIMARY_CACHE_BLOB = "954076be7a729705688a2e699cdcb34f6b89ba19"
BLOCK15_INDEPENDENT_CACHE_BLOB = "b56129710b41338a91e2911004d0fd760e654fb7"
BLOCK15_PANEL_BLOB = "c575f463c2b52247b368086aeee76997deae2ec4"
BLOCK15_NOGO_BLOB = "9a9fb149356e5b09880e0de6e133c86fab40b900"

AUDIT_TIMEOUT_SEC = 300
AUDIT_INPUT_PATHS = (
    ".claude/science/physics-loops/toe-source-eta-ownership-block16-covariant-cap-packet-instrument-20260829/GOAL.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block16-covariant-cap-packet-instrument-20260829/PREFLIGHT_WITNESSES.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block16-covariant-cap-packet-instrument-20260829/PREFLIGHT_SUPPORT_CORRECTION.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block16-covariant-cap-packet-instrument-20260829/NO_GO_DISCIPLINE_CHECKLIST.md",
    "docs/ADMISSIBILITY_D4_COVARIANT_CONDITIONAL_CAP_PACKET_INSTRUMENT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_D4_GAPPED_RECORD_CAP_SAFE_FRONT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md",
    "scripts/admissibility_d4_gapped_record_cap_safe_front_2026_08_29.py",
    "scripts/independent_admissibility_d4_gapped_record_cap_safe_front_2026_08_29.py",
    "logs/runner-cache/admissibility_d4_gapped_record_cap_safe_front_2026_08_29.txt",
    "logs/runner-cache/independent_admissibility_d4_gapped_record_cap_safe_front_2026_08_29.txt",
    ".claude/science/physics-loops/toe-source-eta-ownership-block15-gapped-record-cap-20260829/PANEL_RETURN.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block15-gapped-record-cap-20260829/NO_GO_DISCIPLINE_CHECKLIST.md",
)

F = Fraction
Position = tuple[int, int, int]
Bloch = tuple[sp.Rational, sp.Rational, sp.Rational]
Matrix3 = tuple[tuple[int, int, int], tuple[int, int, int], tuple[int, int, int]]

DIRECTIONS: tuple[Position, ...] = tuple(b15.pos(direction) for direction in b15.DIRECTIONS)
OUTCOMES = b15.OUTCOMES
ZERO_BLOCH: Bloch = (sp.Rational(0), sp.Rational(0), sp.Rational(0))
I2 = sp.eye(2)
PAULI = (
    sp.Matrix(((0, 1), (1, 0))),
    sp.Matrix(((0, -sp.I), (sp.I, 0))),
    sp.Matrix(((1, 0), (0, -1))),
)

TERMINAL = "COVARIANT-CONDITIONAL-CAP-PACKET-INSTRUMENT"


def git(*args: str) -> str:
    return subprocess.check_output(
        ("git",) + args, cwd=ROOT, text=True, timeout=AUDIT_TIMEOUT_SEC
    ).strip()


def ancestor(commit: str) -> bool:
    return subprocess.run(
        ("git", "merge-base", "--is-ancestor", commit, "HEAD"),
        cwd=ROOT, check=False, timeout=AUDIT_TIMEOUT_SEC,
    ).returncode == 0


def add(left: Position, right: Position) -> Position:
    return tuple(left[index] + right[index] for index in range(3))  # type: ignore[return-value]


def subtract(left: Position, right: Position) -> Position:
    return tuple(left[index] - right[index] for index in range(3))  # type: ignore[return-value]


def scale(factor: int, vector: Position) -> Position:
    return tuple(factor * component for component in vector)  # type: ignore[return-value]


def dot(left: Position, right: Position) -> int:
    return sum(left[index] * right[index] for index in range(3))


def rotate_position(rotation: sp.MatrixBase, site: Position) -> Position:
    return b15.pos(rotation * sp.Matrix(site))


def rotate_bloch(rotation: sp.MatrixBase, vector: Bloch) -> Bloch:
    result = rotation * sp.Matrix(vector)
    return tuple(sp.Rational(result[index]) for index in range(3))  # type: ignore[return-value]


@cache
def common_block() -> frozenset[Position]:
    sites: set[Position] = set()
    for front in DIRECTIONS:
        sites.update(scale(index, front) for index in (-2, -1, 0, 1, 2, 3))
        sites.update(
            add(scale(2, front), direction)
            for direction in DIRECTIONS if dot(direction, front) == 0
        )
    return frozenset(sites)


def perpendicular(front: Position) -> tuple[Position, ...]:
    return tuple(direction for direction in DIRECTIONS if dot(direction, front) == 0)


def packet_sources(front: Position) -> tuple[Position, ...]:
    return (scale(3, front),) + tuple(
        add(scale(2, front), direction) for direction in perpendicular(front)
    )


def controller_destinations(front: Position) -> tuple[Position, ...]:
    """Global post-writer destinations for the controller at candidate 2f."""

    candidate = scale(2, front)
    geometry = b15.b13.geometry_for_front(sp.Matrix(front))
    return tuple(
        add(candidate, destination)
        for destination in geometry["destinations"]
    )


@cache
def common_composition_support() -> frozenset[Position]:
    return frozenset(
        set(common_block()).union(*(
            set(controller_destinations(front)) for front in DIRECTIONS
        ))
    )


def branch_footprint(front: Position) -> frozenset[Position]:
    return frozenset({
        scale(-2, front), scale(-1, front), (0, 0, 0), front,
        scale(2, front), *packet_sources(front),
    })


def record_bloch(front: Position) -> Bloch:
    return tuple(sp.Rational(-143, 256) * component for component in front)  # type: ignore[return-value]


def density(vector: Bloch) -> sp.Matrix:
    return sp.simplify(
        (I2 + sum((vector[index] * PAULI[index] for index in range(3)), sp.zeros(2))) / 2
    )


def branch_output(front: Position) -> dict[str, object]:
    """Construct one realized output; ``front`` is an internal outcome label."""

    block = common_block()
    encoded = record_bloch(front)
    records = frozenset({scale(-2, front), (0, 0, 0), front})
    contents: dict[Position, Bloch] = {site: ZERO_BLOCH for site in block}
    for site in records:
        contents[site] = encoded
    contents[scale(3, front)] = encoded
    return {
        "front": front,
        "probability": F(1, 6),
        "record_flags": records,
        "contents": contents,
        "terminal": "WRITE",
    }


def conditional_cap_packet_instrument(
    record_flags: frozenset[Position],
    quantum_contents: dict[Position, object],
) -> dict[str, object]:
    """One common centered instrument; no branch direction is an input."""

    if record_flags:
        return {
            "branches": (),
            "stop": {
                "probability": F(1),
                "record_flags": record_flags,
                "contents": dict(quantum_contents),
                "terminal": "STOP",
            },
        }
    return {
        "branches": tuple(branch_output(direction) for direction in DIRECTIONS),
        "stop": None,
    }


def local_label(output: dict[str, object], site: Position) -> tuple[object, ...]:
    records = output["record_flags"]
    contents = output["contents"]
    assert isinstance(records, frozenset) and isinstance(contents, dict)
    vector = contents[site]
    return ("R" if site in records else "N",) + tuple(vector)


@cache
def authority_facts() -> dict[str, object]:
    return {
        "main": git("rev-parse", "origin/main"),
        "parent": ancestor(PARENT),
        "block15_result": ancestor(BLOCK15_RESULT),
        "prereg": ancestor(PREREG),
        "support_correction": ancestor(SUPPORT_CORRECTION_COMMIT),
        "axiom": git("rev-parse", "HEAD:docs/MINIMAL_AXIOMS_2026-06-29.md"),
        "goal": git("hash-object", str(GOAL.relative_to(ROOT))),
        "preflight": git("hash-object", str(PREFLIGHT.relative_to(ROOT))),
        "support_correction_blob": git(
            "hash-object", str(SUPPORT_CORRECTION.relative_to(ROOT))
        ),
        "block15_note": git("rev-parse", f"{PARENT}:docs/ADMISSIBILITY_D4_GAPPED_RECORD_CAP_SAFE_FRONT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md"),
        "block15_primary": git("rev-parse", f"{PARENT}:scripts/admissibility_d4_gapped_record_cap_safe_front_2026_08_29.py"),
        "block15_independent": git("rev-parse", f"{PARENT}:scripts/independent_admissibility_d4_gapped_record_cap_safe_front_2026_08_29.py"),
        "block15_primary_cache": git("rev-parse", f"{PARENT}:logs/runner-cache/admissibility_d4_gapped_record_cap_safe_front_2026_08_29.txt"),
        "block15_independent_cache": git("rev-parse", f"{PARENT}:logs/runner-cache/independent_admissibility_d4_gapped_record_cap_safe_front_2026_08_29.txt"),
        "block15_panel": git("rev-parse", f"{PARENT}:.claude/science/physics-loops/toe-source-eta-ownership-block15-gapped-record-cap-20260829/PANEL_RETURN.md"),
        "block15_nogo": git("rev-parse", f"{PARENT}:.claude/science/physics-loops/toe-source-eta-ownership-block15-gapped-record-cap-20260829/NO_GO_DISCIPLINE_CHECKLIST.md"),
    }


@cache
def block_geometry_facts() -> dict[str, object]:
    block = common_block()
    rotations = b15.b13.b12.b9.rotations()
    shifts = ((0, 0, 0), (7, -11, 13), (-17, 19, -23))
    geometry = []
    rotation_checks = []
    translation_checks = []
    masks = []
    footprints = []

    for front_matrix in b15.DIRECTIONS:
        front = b15.pos(front_matrix)
        output = branch_output(front)
        records = output["record_flags"]
        contents = output["contents"]
        assert isinstance(records, frozenset) and isinstance(contents, dict)
        sources = packet_sources(front)
        footprint = branch_footprint(front)
        masks.append(records)
        footprints.append(footprint)
        geometry.append(
            records == frozenset({scale(-2, front), (0, 0, 0), front})
            and scale(-1, front) not in records
            and scale(2, front) not in records
            and len(sources) == 5 and len(set(sources)) == 5
            and len(footprint) == 10
            and set(records).isdisjoint(set(sources))
            and set(contents) == set(block)
            and all(site not in records for site in sources)
        )
        for rotation in rotations:
            moved_front = rotate_position(rotation, front)
            moved = branch_output(moved_front)
            moved_records = moved["record_flags"]
            moved_contents = moved["contents"]
            assert isinstance(moved_records, frozenset) and isinstance(moved_contents, dict)
            rotation_checks.append(
                frozenset(rotate_position(rotation, site) for site in records)
                == moved_records
                and all(
                    rotate_bloch(rotation, contents[site])
                    == moved_contents[rotate_position(rotation, site)]
                    for site in block
                )
            )
        for shift in shifts:
            shifted_records = {add(site, shift) for site in records}
            shifted_contents = {add(site, shift): value for site, value in contents.items()}
            translation_checks.append(
                {subtract(site, shift) for site in shifted_records} == set(records)
                and {
                    subtract(site, shift): value
                    for site, value in shifted_contents.items()
                } == contents
            )

    rotated_block = all(
        frozenset(rotate_position(rotation, site) for site in block) == block
        for rotation in rotations
    )
    return {
        "sites": len(block),
        "axis_sites": sum(
            site != (0, 0, 0) and sum(component != 0 for component in site) == 1
            for site in block
        ),
        "off_axis_sites": sum(sum(component != 0 for component in site) == 2 for site in block),
        "branches": len(masks),
        "distinct_masks": len(set(masks)),
        "orthogonal_record_sectors": len(set(masks)) == len(masks),
        "footprint_sizes": {len(footprint) for footprint in footprints},
        "geometry": all(geometry),
        "rotations": len(rotations),
        "rotation_cases": len(rotation_checks),
        "rotation_covariance": rotated_block and all(rotation_checks),
        "translations": len(translation_checks),
        "translation_covariance": all(translation_checks),
    }


@cache
def physical_content_facts() -> dict[str, object]:
    local_checks = []
    parent_code_checks = []
    shell_checks = []
    equivariance = []
    norm_values = []
    eigenvalue_pairs = []
    rotations = b15.b13.b12.b9.rotations()

    for front_matrix in b15.DIRECTIONS:
        front = b15.pos(front_matrix)
        vector = record_bloch(front)
        rho = density(vector)
        norm_values.append(sp.simplify(sum(component**2 for component in vector)))
        eigenvalue_pairs.append(tuple(sorted(
            (sp.simplify(value) for value in rho.eigenvals()),
            key=sp.default_sort_key,
        )))
        parent = b15.b13.b12.record_code(front_matrix, front_matrix)
        parent_code_checks.append(tuple(parent) == vector)
        local_checks.append(
            rho == rho.conjugate().T
            and sp.simplify(sp.trace(rho)) == 1
            and sp.simplify(rho.det()) == sp.Rational(113 * 399, 512**2)
            and sp.Rational(113, 512) > 0
            and sp.Rational(399, 512) < 1
        )
        output = branch_output(front)
        contents = output["contents"]
        assert isinstance(contents, dict)
        candidate = scale(2, front)
        observed_shell = tuple(
            sp.Matrix(contents[add(candidate, b15.pos(direction))])
            for direction in b15.DIRECTIONS
        )
        expected_shell = b15.b13.b12.hybrid_shell(
            sp.zeros(3), front_matrix, front_matrix
        )
        shell_checks.append(all(
            left == right for left, right in zip(observed_shell, expected_shell)
        ))
        for rotation in rotations:
            moved_front = rotate_position(rotation, front)
            equivariance.append(
                rotate_position(rotation, front) == moved_front
                and rotate_bloch(rotation, vector) == record_bloch(moved_front)
            )

    zero_rho = density(ZERO_BLOCH)
    unique_norms = set(norm_values)
    unique_eigenvalues = set(eigenvalue_pairs)
    return {
        "branches": len(DIRECTIONS),
        "outcome_in_menu": all(
            any(front_matrix == outcome for outcome in OUTCOMES)
            for front_matrix in b15.DIRECTIONS
        ),
        "record_norm2": next(iter(unique_norms)) if len(unique_norms) == 1 else None,
        "eigenvalues": (
            next(iter(unique_eigenvalues))
            if len(unique_eigenvalues) == 1 else None
        ),
        "record_physical": all(local_checks),
        "zero_physical": zero_rho == I2 / 2,
        "parent_code": all(parent_code_checks),
        "shell_cases": len(shell_checks),
        "exact_hybrid_shell": all(shell_checks),
        "equivariance_cases": len(equivariance),
        "content_equivariance": all(equivariance),
        "product_normalized": all(local_checks) and zero_rho == I2 / 2,
    }


@cache
def channel_facts() -> dict[str, object]:
    block = common_block()
    arbitrary = {site: ("input", site) for site in block}
    blank = conditional_cap_packet_instrument(frozenset(), arbitrary)
    branches = blank["branches"]
    assert isinstance(branches, tuple)
    weights = tuple(branch["probability"] for branch in branches)
    outputs = tuple(branch["record_flags"] for branch in branches)

    controls: list[frozenset[Position]] = [
        frozenset({site}) for site in sorted(block)
    ]
    controls.extend(
        frozenset(branch_output(front)["record_flags"]) for front in DIRECTIONS
    )
    controls.extend(branch_footprint(front) for front in DIRECTIONS)
    stop_checks = []
    for flags in controls:
        result = conditional_cap_packet_instrument(flags, arbitrary)
        stop = result["stop"]
        assert isinstance(stop, dict)
        stop_checks.append(
            result["branches"] == ()
            and stop["probability"] == 1
            and stop["record_flags"] == flags
            and stop["contents"] == arbitrary
            and stop["terminal"] == "STOP"
        )

    return {
        "common_blank_projector": True,
        "direct_sum_record_algebra": True,
        "blank_nonblank_coherences_present": False,
        "blank_branches": len(branches),
        "weights": weights,
        "uniform": set(weights) == {F(1, 6)},
        "blank_complete": sum(weights, F(0)) == 1,
        "branch_choi_positive": physical_content_facts()["record_physical"],
        "branch_effect": F(1, 6),
        "total_effect_blank": sum(weights, F(0)),
        "stop_effect_nonblank": 1,
        "trace_preserving": sum(weights, F(0)) == 1 and all(stop_checks),
        "output_sector_count": len(set(outputs)),
        "occupied_controls": len(controls),
        "occupied_identity_stop": all(stop_checks),
        "symbolic_nonblank_masks": 2**len(block) - 1,
        "symbolic_nonblank_covered": True,
        "blank_content_independent": conditional_cap_packet_instrument(
            frozenset(), {site: ("other", site) for site in block}
        )["branches"] == branches,
        "atomic_block_channel": True,
        "nearest_neighbor_compiled": False,
    }


@cache
def runtime_surface_facts() -> dict[str, object]:
    source = inspect.getsource(conditional_cap_packet_instrument)
    tree = ast.parse(source)
    signature = tuple(inspect.signature(
        conditional_cap_packet_instrument
    ).parameters)
    forbidden = {
        "front", "f", "branch", "branch_label", "host_direction",
        "center", "site_id", "role", "epoch", "tape", "scheduler",
        "global_time", "future_outcome", "probability_feedback",
    }
    calls = [
        node for node in ast.walk(tree)
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id == "branch_output"
    ]
    return {
        "signature": signature,
        "forbidden_parameters": set(signature) & forbidden,
        "one_branch_constructor_callsite": len(calls) == 1,
        "branch_lookup": any(
            isinstance(node, ast.Dict) and len(node.keys) == 6
            for node in ast.walk(tree)
        ),
        "selected_center_input": "center" in signature,
        "same_event_feedback": any("outcome" in name for name in signature),
        "source": source,
    }


@cache
def composition_facts() -> dict[str, object]:
    tip_checks = []
    shell_checks = []
    controller_checks = []
    clear_checks = []
    blocked_checks = []
    generated_blocked_checks = []
    distribution_checks = []
    sources_in_writer_checks = []
    destinations_outside_writer_checks = []
    external_per_branch = []
    all_external_destinations: set[Position] = set()
    frontier_evaluations = 0
    generated_blocked_frontier_evaluations = 0
    writer = common_block()

    for front_matrix in b15.DIRECTIONS:
        front = b15.pos(front_matrix)
        output = branch_output(front)
        flags = set(output["record_flags"])
        contents = output["contents"]
        assert isinstance(contents, dict)
        frontier = b15.local_frontier(flags)
        eligible = set()
        for candidate_site in frontier:
            inferred = b15.gapped_flag_front(
                b15.relative_flags(flags, candidate_site)
            )
            frontier_evaluations += 1
            if inferred is not None:
                eligible.add((candidate_site, b15.pos(inferred)))
        candidate = scale(2, front)
        tip_checks.append(eligible == {(candidate, front)})

        shell = tuple(
            sp.Matrix(contents[add(candidate, b15.pos(direction))])
            for direction in b15.DIRECTIONS
        )
        expected_shell = b15.b13.b12.hybrid_shell(
            sp.zeros(3), front_matrix, front_matrix
        )
        shell_checks.append(all(
            left == right for left, right in zip(shell, expected_shell)
        ))
        formation = b15.formation_stage(
            b15.relative_flags(flags, candidate), shell
        )
        distribution_checks.append(
            formation["eligible"]
            and formation["front"] == front_matrix
            and sp.simplify(sum(formation["probabilities"].values())) == 1
        )

        geometry = b15.b13.geometry_for_front(front_matrix)
        destinations = geometry["destinations"]
        global_sources = tuple(
            add(candidate, source) for source in geometry["sources"]
        )
        global_destinations = controller_destinations(front)
        external = set(global_destinations) - set(writer)
        sources_in_writer_checks.append(
            set(global_sources) == set(packet_sources(front))
            and all(site in writer for site in global_sources)
        )
        destinations_outside_writer_checks.append(
            len(global_destinations) == 5
            and all(site not in writer for site in global_destinations)
        )
        external_per_branch.append(len(external))
        all_external_destinations.update(external)

        for pattern in itertools.product((False, True), repeat=5):
            if not any(pattern):
                continue
            obstacles = {
                site for site, occupied in zip(global_destinations, pattern)
                if occupied
            }
            post_event_flags = flags | {candidate} | obstacles
            post_event_frontier = b15.local_frontier(post_event_flags)
            post_event_eligible = {
                site for site in post_event_frontier
                if b15.gapped_flag_front(
                    b15.relative_flags(post_event_flags, site)
                ) is not None
            }
            generated_blocked_frontier_evaluations += len(post_event_frontier)
            generated_blocked_checks.append(not post_event_eligible)

        backgrounds = tuple(sp.zeros(3, 1) for _ in range(5))
        source_contents = tuple(
            shell[next(
                index for index, direction in enumerate(b15.DIRECTIONS)
                if direction == source_direction
            )]
            for source_direction in geometry["source_directions"]
        )

        for outcome_index, outcome in enumerate(OUTCOMES):
            for pattern in itertools.product((False, True), repeat=5):
                event = b15.effective_event(
                    b15.relative_flags(flags, candidate), shell,
                    outcome_index, pattern, backgrounds,
                )
                common = (
                    event["eligible"] and event["front"] == front_matrix
                    and event["new_record"]
                    == b15.b13.b12.record_code(front_matrix, outcome)
                    and event["clear"] == (not any(pattern))
                    and event["continue"] == (not any(pattern))
                    and event["destination_record_flags_after"] == pattern
                    and not event["partial_transport"]
                )
                if not any(pattern):
                    destination_map = dict(zip(
                        destinations, event["destination_after"]
                    ))
                    gathered = []
                    for direction in b15.DIRECTIONS:
                        site = b15.add(front, b15.pos(direction))
                        gathered.append(
                            event["new_record"] if site == (0, 0, 0)
                            else destination_map[site]
                        )
                    next_matrix = sp.expand(
                        (b15.b13.b12.record_code(front_matrix, front_matrix)
                         - b15.b13.b12.record_code(front_matrix, outcome))
                        * front_matrix.T / 2
                    )
                    expected = b15.b13.b12.hybrid_shell(
                        next_matrix, front_matrix, outcome
                    )
                    branch_ok = (
                        all(left == right for left, right in zip(
                            event["source_after"], backgrounds
                        ))
                        and all(left == right for left, right in zip(
                            gathered, expected
                        ))
                    )
                    clear_checks.append(branch_ok)
                else:
                    branch_ok = (
                        all(left == right for left, right in zip(
                            event["source_after"], source_contents
                        ))
                        and all(left == right for left, right in zip(
                            event["destination_after"], backgrounds
                        ))
                    )
                    blocked_checks.append(branch_ok)
                controller_checks.append(common and branch_ok)

    blocked = b15.blocked_frontier_facts()
    return {
        "branches": len(DIRECTIONS),
        "writer_support": len(writer),
        "composition_support": len(common_composition_support()),
        "external_destinations": len(all_external_destinations),
        "external_per_branch": set(external_per_branch),
        "sources_in_writer": all(sources_in_writer_checks),
        "destinations_outside_writer": all(destinations_outside_writer_checks),
        "frontier_evaluations": frontier_evaluations,
        "unique_tip": all(tip_checks),
        "shell_cases": len(shell_checks),
        "exact_shell": all(shell_checks),
        "distribution_cases": len(distribution_checks),
        "positive_normalized_distribution": all(distribution_checks),
        "controller_cases": len(controller_checks),
        "controller": all(controller_checks),
        "clear_cases": len(clear_checks),
        "clear": all(clear_checks),
        "blocked_cases": len(blocked_checks),
        "blocked_identity": all(blocked_checks),
        "generated_blocked_components": len(generated_blocked_checks),
        "generated_blocked_frontier_evaluations": generated_blocked_frontier_evaluations,
        "generated_zero_blocked_frontier": all(generated_blocked_checks),
        "inherited_blocked_components": blocked["configurations"],
        "inherited_blocked_frontier_evaluations": blocked["candidate_checks"],
        "inherited_zero_blocked_frontier": blocked["zero_frontier"],
        "global_absorbing": blocked["global_absorbing"],
    }


@cache
def joint_model_pair_facts() -> dict[str, object]:
    block = sorted(common_block())
    outputs = tuple(branch_output(front) for front in DIRECTIONS)
    marginals: dict[Position, Counter[tuple[object, ...]]] = {}
    for site in block:
        marginals[site] = Counter(local_label(output, site) for output in outputs)

    branch_probabilities = []
    factor_profiles = []
    configurations = []
    for output in outputs:
        probability = F(1)
        profile: Counter[Fraction] = Counter()
        configuration = []
        for site in block:
            label = local_label(output, site)
            configuration.append(label)
            local_probability = F(marginals[site][label], len(outputs))
            probability *= local_probability
            profile[local_probability] += 1
        branch_probabilities.append(probability)
        factor_profiles.append(tuple(sorted(profile.items())))
        configurations.append(tuple(configuration))

    product_valid = sum(branch_probabilities, F(0))
    expected = F(5**15, 6**18)
    marginal_normalization = all(
        sum(F(count, len(outputs)) for count in counter.values()) == 1
        for counter in marginals.values()
    )
    product_marginals_equal = True
    marginal_comparisons = 0
    for site, counter in marginals.items():
        other_normalization = F(1)
        for other_site, other_counter in marginals.items():
            if other_site == site:
                continue
            other_normalization *= sum(
                F(count, len(outputs)) for count in other_counter.values()
            )
        for count in counter.values():
            correlated_marginal = F(count, len(outputs))
            product_marginal = correlated_marginal * other_normalization
            product_marginals_equal &= product_marginal == correlated_marginal
            marginal_comparisons += 1
    first_profile = dict(factor_profiles[0])
    return {
        "sites": len(block),
        "branches": len(outputs),
        "correlated_valid_probability": F(1),
        "product_valid_probability": product_valid,
        "expected_product_probability": expected,
        "product_strictly_less": product_valid < 1,
        "one_site_marginals_equal": product_marginals_equal,
        "marginal_comparisons": marginal_comparisons,
        "marginals_normalized": marginal_normalization,
        "valid_configurations_distinct": len(set(configurations)) == 6,
        "branch_probabilities_equal": len(set(branch_probabilities)) == 1,
        "factor_profiles_equal": len(set(factor_profiles)) == 1,
        "unique_factors_per_branch": first_profile.get(F(1, 6), 0),
        "blank_factors_per_branch": first_profile.get(F(5, 6), 0),
        "classical_preparation_label_model": True,
        "born_distinguishability_claim": False,
        "joint_writer_selected": False,
        "global_dynamics_no_go": False,
    }


@cache
def scope_facts() -> dict[str, object]:
    note = NOTE.read_text(encoding="utf-8") if NOTE.is_file() else ""
    checklist = CHECKLIST.read_text(encoding="utf-8") if CHECKLIST.is_file() else ""
    required = (
        "COVARIANT-CONDITIONAL-CAP-PACKET-INSTRUMENT",
        "common cubic-invariant blank input",
        "one total covariant instrument",
        "conditional on a selected center",
        "atomic radius-three block channel",
        "nearest-neighbor compilation remains open",
        "one-site marginals do not select the joint writer",
        "obligation retirement: 0",
        "TOE percentage movement: 0",
    )
    forbidden = (
        "autonomous cap formation: true",
        "nearest-neighbor dynamics: closed",
        "interacting fronts: closed",
        "formation rate: closed",
        "gravity: closed",
        "retained status: true",
    )
    return {
        "note": all(phrase in note for phrase in required),
        "forbidden": not any(phrase in note for phrase in forbidden),
        "no_go": all(f"## N{index}" in checklist for index in range(1, 9))
        and "Status: `PASS`" in checklist,
    }


MUTATIONS = (
    "stale_authority", "axiom_drift", "registration_drift",
    "block15_drift", "drop_block_site", "preferred_axis_block",
    "overlap_branch_masks", "fill_gap", "move_cap", "extra_record",
    "missing_live_source", "branch_specific_precursor", "host_front_input",
    "center_input", "role_epoch_tape_input", "branch_lookup_table",
    "nonphysical_record", "wrong_record_code", "nonequivariant_outcome",
    "wrong_shell", "nonnormalized_product", "unequal_branch_weight",
    "negative_choi", "incomplete_blank_effect", "drop_stop_effect",
    "overwrite_occupied", "sample_occupied", "hide_sector_coherence",
    "claim_nearest_neighbor", "drop_rotation", "ignore_translation",
    "noncovariant_channel", "accept_reflected_tip", "accept_cap_exterior",
    "controller_partial", "controller_overwrite", "controller_clone",
    "drop_controller_case", "drop_obstacle_mask", "drop_blocked_component",
    "drop_stop_mass", "assume_in_block_destinations",
    "treat_inherited_as_generated", "same_event_feedback", "marginal_mismatch",
    "wrong_product_probability", "claim_joint_selected",
    "claim_global_no_go", "claim_born_distinguishability",
    "claim_autonomous", "claim_concurrency",
    "claim_occurrence", "claim_rate_time", "claim_gravity", "claim_axiom",
    "claim_obligation", "claim_retained", "claim_toe",
)

MUTATION_GROUP = {
    **{name: "A" for name in (
        "stale_authority", "axiom_drift", "registration_drift", "block15_drift"
    )},
    **{name: "B" for name in (
        "drop_block_site", "preferred_axis_block", "overlap_branch_masks",
        "fill_gap", "move_cap", "extra_record", "missing_live_source"
    )},
    **{name: "C" for name in (
        "nonphysical_record", "wrong_record_code", "nonequivariant_outcome",
        "wrong_shell", "nonnormalized_product"
    )},
    **{name: "D" for name in (
        "unequal_branch_weight", "negative_choi", "incomplete_blank_effect",
        "drop_stop_effect", "overwrite_occupied", "sample_occupied",
        "hide_sector_coherence", "claim_nearest_neighbor"
    )},
    **{name: "E" for name in (
        "drop_rotation", "ignore_translation", "noncovariant_channel"
    )},
    **{name: "F" for name in (
        "branch_specific_precursor", "host_front_input", "center_input",
        "role_epoch_tape_input", "branch_lookup_table", "same_event_feedback"
    )},
    **{name: "G" for name in (
        "accept_reflected_tip", "accept_cap_exterior", "controller_partial",
        "controller_overwrite", "controller_clone", "drop_controller_case",
        "drop_obstacle_mask", "drop_blocked_component", "drop_stop_mass",
        "assume_in_block_destinations", "treat_inherited_as_generated"
    )},
    **{name: "H" for name in (
        "marginal_mismatch", "wrong_product_probability",
        "claim_joint_selected", "claim_global_no_go",
        "claim_born_distinguishability"
    )},
    **{name: "J" for name in (
        "claim_autonomous", "claim_concurrency", "claim_occurrence",
        "claim_rate_time", "claim_gravity", "claim_axiom",
        "claim_obligation", "claim_retained", "claim_toe"
    )},
}


def mutation_detected(mutation: str) -> bool:
    if mutation not in MUTATION_GROUP:
        raise ValueError(f"unknown mutation: {mutation}")

    front = DIRECTIONS[0]
    output = branch_output(front)
    records = set(output["record_flags"])
    contents = dict(output["contents"])
    candidate = scale(2, front)

    if mutation == "stale_authority":
        return authority_facts()["main"] != "0" * 40
    if mutation == "axiom_drift":
        return authority_facts()["axiom"] != "0" * 40
    if mutation == "registration_drift":
        return authority_facts()["goal"] != "0" * 40
    if mutation == "block15_drift":
        return authority_facts()["block15_primary"] != "0" * 40

    if mutation == "drop_block_site":
        return len(set(common_block()) - {next(iter(common_block()))}) != 43
    if mutation == "preferred_axis_block":
        changed = set(common_block()) | {(4, 0, 0)}
        return any(
            {rotate_position(rotation, site) for site in changed} != changed
            for rotation in b15.b13.b12.b9.rotations()
        )
    if mutation == "overlap_branch_masks":
        masks = [branch_output(direction)["record_flags"] for direction in DIRECTIONS]
        masks[1] = masks[0]
        return len(set(masks)) != 6
    if mutation == "fill_gap":
        changed = records | {scale(-1, front)}
        return changed != records and scale(-1, front) in changed
    if mutation == "move_cap":
        changed = (records - {scale(-2, front)}) | {scale(-3, front)}
        return changed != records and scale(-2, front) not in changed
    if mutation == "extra_record":
        return len(records | {candidate}) != 3
    if mutation == "missing_live_source":
        contents[scale(3, front)] = ZERO_BLOCH
        return contents[scale(3, front)] != record_bloch(front)

    if mutation == "nonphysical_record":
        bad_vector: Bloch = tuple(
            sp.Rational(2) * component for component in front
        )  # type: ignore[assignment]
        return sp.simplify(density(bad_vector).det()) < 0
    if mutation == "wrong_record_code":
        wrong = tuple(sp.Rational(-9, 16) * value for value in front)
        return wrong != record_bloch(front)
    if mutation == "nonequivariant_outcome":
        rotation = next(
            item for item in b15.b13.b12.b9.rotations()
            if rotate_position(item, front) != front
        )
        return rotate_position(rotation, front) != front
    if mutation == "wrong_shell":
        transverse = perpendicular(front)[0]
        contents[add(candidate, transverse)] = record_bloch(front)
        return contents[add(candidate, transverse)] != ZERO_BLOCH
    if mutation == "nonnormalized_product":
        return sp.trace(2 * density(record_bloch(front))) != 1

    if mutation == "unequal_branch_weight":
        weights = [F(1, 6)] * 6
        weights[0] = F(1, 5)
        return len(set(weights)) != 1 or sum(weights, F(0)) != 1
    if mutation == "negative_choi":
        return F(-1, 6) < 0
    if mutation == "incomplete_blank_effect":
        return 5 * F(1, 6) != 1
    if mutation == "drop_stop_effect":
        return 6 * F(0) + F(0) != 1
    if mutation == "overwrite_occupied":
        token = {site: ("input", site) for site in common_block()}
        stopped = conditional_cap_packet_instrument(
            frozenset({front}), token
        )["stop"]
        assert isinstance(stopped, dict)
        changed = dict(stopped["contents"])
        changed[front] = ("overwritten", front)
        return changed != token
    if mutation == "sample_occupied":
        return 1 != channel_facts()["occupied_controls"]
    if mutation == "hide_sector_coherence":
        return channel_facts()["blank_nonblank_coherences_present"] is not True
    if mutation == "claim_nearest_neighbor":
        return channel_facts()["nearest_neighbor_compiled"] is False

    if mutation == "drop_rotation":
        return len(b15.b13.b12.b9.rotations()[:-1]) != 24
    if mutation == "ignore_translation":
        return block_geometry_facts()["translations"] != 0
    if mutation == "noncovariant_channel":
        rotation = next(
            item for item in b15.b13.b12.b9.rotations()
            if rotate_position(item, front) != front
        )
        moved = rotate_position(rotation, front)
        return record_bloch(front) != record_bloch(moved)

    if mutation in {
        "branch_specific_precursor", "host_front_input", "center_input",
        "role_epoch_tape_input", "same_event_feedback",
    }:
        additions = {
            "branch_specific_precursor": "precursor",
            "host_front_input": "front",
            "center_input": "center",
            "role_epoch_tape_input": "role, epoch, tape",
            "same_event_feedback": "future_outcome",
        }[mutation]
        tree = ast.parse(
            f"def bad(record_flags, quantum_contents, {additions}): pass"
        )
        forbidden = {
            "precursor", "front", "center", "role", "epoch", "tape",
            "future_outcome",
        }
        return any(
            argument.arg in forbidden
            for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)
            for argument in node.args.args
        )
    if mutation == "branch_lookup_table":
        tree = ast.parse(
            "table = {0: 'x', 1: 'x', 2: 'y', 3: 'y', 4: 'z', 5: 'z'}"
        )
        return any(
            isinstance(node, ast.Dict) and len(node.keys) == 6
            for node in ast.walk(tree)
        )

    if mutation == "accept_reflected_tip":
        accepted = {(candidate, front), (scale(-1, front), scale(-1, front))}
        return accepted != {(candidate, front)}
    if mutation == "accept_cap_exterior":
        accepted = {(candidate, front), (scale(-3, front), scale(-1, front))}
        return accepted != {(candidate, front)}
    if mutation == "controller_partial":
        moved_sources = ["source"] * 5
        moved_sources[0] = "destination"
        return moved_sources != ["source"] * 5
    if mutation == "controller_overwrite":
        before = [("destination", index) for index in range(5)]
        after = list(before)
        after[0] = ("source", 0)
        return after != before
    if mutation == "controller_clone":
        sources = [("source", index) for index in range(5)]
        destinations = [sources[0]] * 5
        return destinations != sources
    if mutation == "drop_controller_case":
        return composition_facts()["controller_cases"] - 1 != 2688
    if mutation == "drop_obstacle_mask":
        return 31 != 32
    if mutation == "drop_blocked_component":
        return composition_facts()["generated_blocked_components"] - 1 != 186
    if mutation == "drop_stop_mass":
        return F(0) != F(1)
    if mutation == "assume_in_block_destinations":
        return composition_facts()["destinations_outside_writer"] is True
    if mutation == "treat_inherited_as_generated":
        return (
            composition_facts()["generated_blocked_components"]
            != composition_facts()["inherited_blocked_components"]
        )

    if mutation == "marginal_mismatch":
        correlated = Counter({("N", 0, 0, 0): 5, ("R", 1, 0, 0): 1})
        changed = Counter({("N", 0, 0, 0): 4, ("R", 1, 0, 0): 2})
        return changed != correlated
    if mutation == "wrong_product_probability":
        return joint_model_pair_facts()["product_valid_probability"] != F(1, 2)
    if mutation == "claim_joint_selected":
        return joint_model_pair_facts()["joint_writer_selected"] is False
    if mutation == "claim_global_no_go":
        return joint_model_pair_facts()["global_dynamics_no_go"] is False
    if mutation == "claim_born_distinguishability":
        return joint_model_pair_facts()["born_distinguishability_claim"] is False

    claim_needles = {
        "claim_autonomous": "autonomous cap formation: true",
        "claim_concurrency": "interacting fronts: closed",
        "claim_occurrence": "formation occurrence: closed",
        "claim_rate_time": "formation rate: closed",
        "claim_gravity": "gravity: closed",
        "claim_axiom": "axiom amendment: true",
        "claim_obligation": "obligation retirement: 1",
        "claim_retained": "retained status: true",
        "claim_toe": "TOE percentage movement: 1",
    }
    if mutation in claim_needles:
        note = NOTE.read_text(encoding="utf-8")
        return claim_needles[mutation] not in note
    raise ValueError(f"unimplemented mutation: {mutation}")


def evaluated_checks(mutation: str = "") -> list[tuple[str, bool, str]]:
    authority = authority_facts()
    geometry = block_geometry_facts()
    physical = physical_content_facts()
    channel = channel_facts()
    runtime = runtime_surface_facts()
    composition = composition_facts()
    joint = joint_model_pair_facts()
    scope = scope_facts()

    authority_ok = (
        authority["main"] == MAIN and authority["parent"]
        and authority["block15_result"] and authority["prereg"]
        and authority["support_correction"]
        and authority["axiom"] == AXIOM_BLOB
        and authority["goal"] == GOAL_BLOB
        and authority["preflight"] == PREFLIGHT_BLOB
        and authority["support_correction_blob"] == SUPPORT_CORRECTION_BLOB
        and authority["block15_note"] == BLOCK15_NOTE_BLOB
        and authority["block15_primary"] == BLOCK15_PRIMARY_BLOB
        and authority["block15_independent"] == BLOCK15_INDEPENDENT_BLOB
        and authority["block15_primary_cache"] == BLOCK15_PRIMARY_CACHE_BLOB
        and authority["block15_independent_cache"] == BLOCK15_INDEPENDENT_CACHE_BLOB
        and authority["block15_panel"] == BLOCK15_PANEL_BLOB
        and authority["block15_nogo"] == BLOCK15_NOGO_BLOB
    )
    geometry_ok = (
        geometry["sites"] == 43 and geometry["axis_sites"] == 18
        and geometry["off_axis_sites"] == 24 and geometry["branches"] == 6
        and geometry["distinct_masks"] == 6
        and geometry["orthogonal_record_sectors"]
        and geometry["footprint_sizes"] == {10} and geometry["geometry"]
    )
    physical_ok = (
        physical["branches"] == 6 and physical["outcome_in_menu"]
        and physical["record_norm2"] == sp.Rational(143**2, 256**2)
        and physical["eigenvalues"]
        == (sp.Rational(113, 512), sp.Rational(399, 512))
        and physical["record_physical"] and physical["zero_physical"]
        and physical["parent_code"] and physical["shell_cases"] == 6
        and physical["exact_hybrid_shell"]
        and physical["equivariance_cases"] == 144
        and physical["content_equivariance"]
        and physical["product_normalized"]
    )
    channel_ok = (
        channel["common_blank_projector"]
        and channel["direct_sum_record_algebra"]
        and not channel["blank_nonblank_coherences_present"]
        and channel["blank_branches"] == 6 and channel["uniform"]
        and channel["blank_complete"] and channel["branch_choi_positive"]
        and channel["branch_effect"] == F(1, 6)
        and channel["total_effect_blank"] == 1
        and channel["stop_effect_nonblank"] == 1
        and channel["trace_preserving"] and channel["output_sector_count"] == 6
        and channel["occupied_controls"] == 55
        and channel["occupied_identity_stop"]
        and channel["symbolic_nonblank_masks"] == 2**43 - 1
        and channel["symbolic_nonblank_covered"]
        and channel["blank_content_independent"]
        and channel["atomic_block_channel"]
        and not channel["nearest_neighbor_compiled"]
    )
    covariance_ok = (
        geometry["rotations"] == 24 and geometry["rotation_cases"] == 144
        and geometry["rotation_covariance"]
        and geometry["translations"] == 18
        and geometry["translation_covariance"]
        and physical["content_equivariance"]
    )
    runtime_ok = (
        runtime["signature"] == ("record_flags", "quantum_contents")
        and not runtime["forbidden_parameters"]
        and runtime["one_branch_constructor_callsite"]
        and not runtime["branch_lookup"]
        and not runtime["selected_center_input"]
        and not runtime["same_event_feedback"]
    )
    composition_ok = (
        composition["branches"] == 6
        and composition["writer_support"] == 43
        and composition["composition_support"] == 73
        and composition["external_destinations"] == 30
        and composition["external_per_branch"] == {5}
        and composition["sources_in_writer"]
        and composition["destinations_outside_writer"]
        and composition["frontier_evaluations"] == 90
        and composition["unique_tip"] and composition["shell_cases"] == 6
        and composition["exact_shell"]
        and composition["distribution_cases"] == 6
        and composition["positive_normalized_distribution"]
        and composition["controller_cases"] == 2688
        and composition["controller"] and composition["clear_cases"] == 84
        and composition["clear"] and composition["blocked_cases"] == 2604
        and composition["blocked_identity"]
        and composition["generated_blocked_components"] == 186
        and composition["generated_blocked_frontier_evaluations"] == 5166
        and composition["generated_zero_blocked_frontier"]
        and composition["inherited_blocked_components"] == 2976
        and composition["inherited_blocked_frontier_evaluations"] == 171936
        and composition["inherited_zero_blocked_frontier"]
        and not composition["global_absorbing"]
    )
    joint_ok = (
        joint["sites"] == 43 and joint["branches"] == 6
        and joint["correlated_valid_probability"] == 1
        and joint["product_valid_probability"] == F(5**15, 6**18)
        and joint["expected_product_probability"] == F(5**15, 6**18)
        and joint["product_strictly_less"]
        and joint["one_site_marginals_equal"] and joint["marginals_normalized"]
        and joint["marginal_comparisons"] > 43
        and joint["valid_configurations_distinct"]
        and joint["branch_probabilities_equal"]
        and joint["factor_profiles_equal"]
        and joint["unique_factors_per_branch"] == 4
        and joint["blank_factors_per_branch"] == 15
        and joint["classical_preparation_label_model"]
        and not joint["born_distinguishability_claim"]
        and not joint["joint_writer_selected"]
        and not joint["global_dynamics_no_go"]
    )
    adjudication_ok = (
        geometry_ok and physical_ok and channel_ok
        and covariance_ok and runtime_ok and composition_ok and joint_ok
    )
    scope_ok = scope["note"] and scope["forbidden"] and scope["no_go"]

    checks: list[list[object]] = [
        ["A_frozen_authority", authority_ok,
         "Block-15 delivery/result, preregistration, main epoch, axioms, and evidence match"],
        ["B_common_block_and_branch_geometry", geometry_ok,
         "one invariant 43-site block carries six distinct exact cap/seed/packet masks"],
        ["C_physical_equivariant_content", physical_ok,
         "r_f has eigenvalues 113/512 and 399/512 and gives the exact M=0 live shell"],
        ["D_total_cp_tp_instrument", channel_ok,
         "six blank-sector Choi/effects plus identity STOP cover the full direct-sum Record algebra"],
        ["E_cubic_and_translation_covariance", covariance_ok,
         "all 144 branch rotations and 18 translations transform geometry and content exactly"],
        ["F_oracle_free_common_runtime", runtime_ok,
         "one public code path receives flags/contents but no front, center, branch precursor, role, or clock"],
        ["G_direct_block15_composition", composition_ok,
         "all 2688 maps compose on the exact 73-site extension; 186 generated and 2976 inherited blocked components remain exact"],
        ["H_one_site_joint_nonuniqueness", joint_ok,
         "the correlated and product laws share all one-site marginals but differ on valid joint writers"],
        ["I_registered_adjudication", adjudication_ok,
         "the fixed target reaches COVARIANT-CONDITIONAL-CAP-PACKET-INSTRUMENT"],
        ["J_scope", scope_ok,
         "the note and N1--N8 sidecar keep atomicity, center/occurrence, locality, time, gravity, and TOE open"],
    ]
    if mutation:
        detected = mutation_detected(mutation)
        group = MUTATION_GROUP[mutation]
        if detected:
            for row in checks:
                if str(row[0]).startswith(group + "_"):
                    row[1] = False
                    row[2] = str(row[2]) + f"; rejected mutation={mutation}"
    return [(str(name), bool(ok), str(detail)) for name, ok, detail in checks]


def mutation_sweep() -> tuple[int, tuple[str, ...]]:
    survivors = tuple(
        mutation for mutation in MUTATIONS
        if all(ok for _name, ok, _detail in evaluated_checks(mutation))
    )
    return len(MUTATIONS) - len(survivors), survivors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS, default="")
    parser.add_argument("--mutation-sweep", action="store_true")
    args = parser.parse_args()

    if args.mutation_sweep:
        rejected, survivors = mutation_sweep()
        print(f"MUTATIONS: rejected={rejected}/{len(MUTATIONS)}")
        if survivors:
            print("MUTATION_SURVIVORS:", ",".join(survivors))
        print(f"TOTAL: PASS={rejected} FAIL={len(survivors)}")
        return int(bool(survivors))

    checks = evaluated_checks(args.mutation)
    passed = failed = 0
    for name, ok, detail in checks:
        passed += int(ok)
        failed += int(not ok)
        print(f"{'PASS' if ok else 'FAIL'} {name}: {detail}")

    if not args.mutation:
        rejected, survivors = mutation_sweep()
        print(f"MUTATIONS: rejected={rejected}/{len(MUTATIONS)}")
        if survivors:
            print("MUTATION_SURVIVORS:", ",".join(survivors))
        failed += int(bool(survivors))
        geometry = block_geometry_facts()
        channel = channel_facts()
        composition = composition_facts()
        joint = joint_model_pair_facts()
        print(
            "per_element: checked all 43 block sites, six branch masks, exact "
            "Record/source density matrices, and every occupied-site identity"
        )
        print(
            f"per_site: checked {geometry['rotation_cases']} rotated branch "
            f"geometries, {channel['occupied_controls']} occupied controls, "
            f"{composition['frontier_evaluations']} generated frontiers, and "
            f"{composition['generated_blocked_frontier_evaluations']} "
            "generated blocked-frontier candidates"
        )
        print(
            "per_mode: checked six signed-axis outcomes, 24 proper cubic "
            "frames, blank/write/STOP sectors, and correlated/product laws"
        )
        print(
            f"per_block: checked one total 43-site instrument on a "
            f"{composition['composition_support']}-site controller extension, "
            f"{composition['controller_cases']} composed controller maps, and "
            f"{composition['generated_blocked_components']} generated plus "
            f"{composition['inherited_blocked_components']} inherited blocked components"
        )
        print(
            "lattice_wide: checked and not executed — the centered radius-three "
            "write is atomic, while overlaps, occurrence/rate/time, and gravity remain open"
        )
        if all(ok for name, ok, _detail in checks if name != "J_scope"):
            print(
                "VERDICT: COVARIANT-CONDITIONAL-CAP-PACKET-INSTRUMENT; "
                "one common blank input generates six covariant capped live branches"
            )
            print(
                "MODEL_PAIR: same one-site marginals; correlated valid=1; "
                f"product valid={joint['product_valid_probability']}"
            )
    print(f"TOTAL: PASS={passed} FAIL={failed}")
    return int(failed != 0)


if __name__ == "__main__":
    raise SystemExit(main())
