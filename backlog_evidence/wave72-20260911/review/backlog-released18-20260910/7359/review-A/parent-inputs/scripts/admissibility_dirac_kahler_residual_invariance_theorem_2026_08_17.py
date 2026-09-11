#!/usr/bin/env python3
"""Block 135: exact residual-invariance theorem certificate.

The runner exhausts the displayed translation-closed shifted-origin atlas,
separates its residual orbit from the exact coboundary image, checks the
Block 134 normal form throughout that orbit, and exhibits a consistent chart
subset outside the displayed class.  Scientific arithmetic is exact; the
integer wall-clock counter is used only for the runtime gate.
"""

from __future__ import annotations

import argparse
from collections import Counter
from dataclasses import dataclass
from itertools import combinations, product
from pathlib import Path
import re
import subprocess
import time

import sympy as sp

import admissibility_dirac_kahler_connection_residual_theorem_2026_08_17 as block134


R = sp.Rational
I = sp.I
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_DIRAC_KAHLER_RESIDUAL_INVARIANCE_THEOREM_"
    "BOUNDED_THEOREM_NOTE_2026-08-17.md"
)
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"
PARENT_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_CONNECTION_RESIDUAL_THEOREM_"
    "BOUNDED_THEOREM_NOTE_2026-08-17.md"
)
PARENT_RUNNER = (
    "scripts/admissibility_dirac_kahler_connection_residual_theorem_"
    "2026_08_17.py"
)
PARENT_CACHE = (
    "logs/runner-cache/admissibility_dirac_kahler_connection_residual_"
    "theorem_2026_08_17.txt"
)
CURVED_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_"
    "NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md"
)
CURVED_RUNNER = (
    "scripts/admissibility_dirac_kahler_shifted_origin_frame_gauge_"
    "nonuniform_hodge_overlap_2026_08_14.py"
)

# Deliberately literal: this is the complete audit read surface.
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_RESIDUAL_INVARIANCE_THEOREM_BOUNDED_THEOREM_NOTE_2026-08-17.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_CONNECTION_RESIDUAL_THEOREM_BOUNDED_THEOREM_NOTE_2026-08-17.md",
    "scripts/admissibility_dirac_kahler_connection_residual_theorem_2026_08_17.py",
    "logs/runner-cache/admissibility_dirac_kahler_connection_residual_theorem_2026_08_17.txt",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "scripts/admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_2026_08_14.py",
)

AUDIT_TIMEOUT_SEC = 600
CURRENT_MAIN = "02602ca09e4ea69a805a824c3c1f31cb1ee35b20"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
CURRENT_REGISTRY_BLOB = "b93959cca4f7e26c673cdccbe601e50c3cb93daa"
WORKTREE_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
WORKTREE_REGISTRY_BLOB = "f01d3be864f682584d50eede8b3abe6671bb4719"
PARENT_REF = (
    "origin/physics-loop/"
    "toe-axiom-closure-block134-connection-residual-theorem-20260817"
)
PARENT_COMMIT = "acb7d8109bf751c909364aec92c4d833492cfa6c"
PARENT_NOTE_BLOB = "ff840fa7031405899819a8f9ef6c787b0214554a"
PARENT_RUNNER_BLOB = "f092e5560590d6a4e485a57721878caaa874b4dd"
PARENT_CACHE_BLOB = "25855c9812d7986b23b18d19353a5775a6b00151"
CURVED_COMMIT = "d06066c2b908aaca0779625d831dfb10620cf34d"
CURVED_NOTE_BLOB = "5eff91757e38f3f2ea7dc2a2c50788636cc2e3a5"
CURVED_RUNNER_BLOB = "4870f31b5880028ad4f1f3095aad4d0820e4668f"

ANCESTOR_COMMITS = (
    (133, "80d208f0c12e21fd985d01e5f807a9d34c00ef11"),
    (132, "0236823bed5b648ad8357e5d1b79bdfe1be36c39"),
    (131, "d3a666f62c87b3b8178289024087090c91ced327"),
    (130, "db394d1536a8243c2b01b3e45413813e45f8abdd"),
    (129, "30fd2722a10a02f87c235e2ee592d140f8bb7df5"),
    (128, "f6b0cf59e2cc588ebd3e34b96e730574cb485db2"),
    (127, "ca6792464f60598013a3700f99c02a467af64b7a"),
    (126, "a145a4e2cfc19bc919371196d7c5f3451c0bb45d"),
    (125, "ff85cc8c6a991b2926b9ac5cb5168f2587bc0c0d"),
    (124, "da2b9020e9f15ac55640ef87a0798a78e3c9a0d0"),
    (123, "954322e0e085d6c3133ce24dca49db2efbd7d0a6"),
    (122, "f067b99be7eb49fc46ea8dffccab5e20e6052d88"),
    (121, "1714abeefcf3763c0bfe001f30fd14521c538622"),
    (120, "1c2386bf3df420707fd2ecb2d7ec84002ba40ad1"),
    (119, "33fd2d21558604718f3a88713fe1976aff8f9dbb"),
    (118, "fdd1883c54ca8cc14b1337cc1edc249792d5dab2"),
    (117, "f800356aec0989b6e0fa80ed43274794243b1ca2"),
    (116, "c36d11e4e8d927c6fc31f0a8b579d4bd15f4fa43"),
    (115, "c78301fef7521d0518f485f1bf9266983c9e516a"),
    (114, "75026e71cfbd44ed665ddc41c22ebaa722720ea9"),
    (113, "e76893eb7204d1d727a3ab8838fb3fada3f45dfc"),
    (112, "385a6ba5b1594f20e5d4eebba9da68d8e72abc10"),
    (111, "b04e7c8747b09734711cfcd2bfab961bd12e81ad"),
    (110, "d6761278fca9cac617200792473a8f4da3a6cfff"),
    (109, "ad84cfcc857a65285389ba93b47cd7b718589be5"),
    (108, "8afe8dff5ccf531208238af0aaaec1f547d73874"),
    (107, "d41a05e153d4cb77eee125b82fc0b0bd767bf32e"),
    (106, "22d6d90ec2279e5868c9c825149b2a20beea3797"),
    (105, "d06066c2b908aaca0779625d831dfb10620cf34d"),
    (104, "7fe07db6c03fad1191893c942f708c5cb9a54c43"),
    (103, "99cee0a6c962b382a3ca1a8497d589ffa280dfe8"),
)

MUTATIONS = (
    "stale_axiom_authority",
    "stale_parent_authority",
    "break_origin_premises",
    "break_exhaustive_count",
    "break_coboundary_image",
    "claim_augmentation_content",
    "break_parameter_sweep",
    "break_st_degeneration",
    "break_normal_form",
    "break_exception_consistency",
    "weaken_no_go_packet",
    "drop_n5_resolution",
    "claim_toe_progress",
    "claim_axiom_amendment",
    "claim_unqualified_nogo",
)


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, key: str, statement: str, condition: object) -> None:
        ok = bool(condition)
        print(f"[{'PASS' if ok else 'FAIL'}] {key}: {statement}")
        self.passed += int(ok)
        self.failed += int(not ok)

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def git_output(*args: str) -> str:
    return subprocess.check_output(
        ("git",) + args,
        cwd=ROOT,
        text=True,
        timeout=AUDIT_TIMEOUT_SEC,
    ).strip()


def worktree_blob(path: str) -> str:
    return git_output("hash-object", path)


def commit_blob(commit: str, path: str) -> str:
    return git_output("rev-parse", f"{commit}:{path}")


def is_ancestor(ancestor: str, descendant: str) -> bool:
    return subprocess.run(
        ("git", "merge-base", "--is-ancestor", ancestor, descendant),
        cwd=ROOT,
        check=False,
        timeout=AUDIT_TIMEOUT_SEC,
    ).returncode == 0


def authority_certificate(mutation: str) -> dict[str, object]:
    expected_axiom = (
        "0" * 40 if mutation == "stale_axiom_authority" else CURRENT_AXIOM_BLOB
    )
    expected_parent = (
        "0" * 40 if mutation == "stale_parent_authority" else PARENT_NOTE_BLOB
    )
    return {
        "main": git_output("rev-parse", "origin/main"),
        "axiom": commit_blob("origin/main", AXIOM_PATH),
        "worktree_axiom": worktree_blob(AXIOM_PATH),
        "expected_axiom": expected_axiom,
        "registry": commit_blob("origin/main", REGISTRY_PATH),
        "worktree_registry": worktree_blob(REGISTRY_PATH),
        "parent": git_output("rev-parse", PARENT_REF),
        "parent_ancestor": is_ancestor(PARENT_COMMIT, "HEAD"),
        **{
            f"ancestor_{number}": is_ancestor(commit, "HEAD")
            for number, commit in ANCESTOR_COMMITS
        },
        "parent_note": commit_blob(PARENT_COMMIT, PARENT_NOTE),
        "expected_parent": expected_parent,
        "parent_runner": commit_blob(PARENT_COMMIT, PARENT_RUNNER),
        "parent_cache": commit_blob(PARENT_COMMIT, PARENT_CACHE),
        "worktree_parent_note": worktree_blob(PARENT_NOTE),
        "worktree_parent_runner": worktree_blob(PARENT_RUNNER),
        "worktree_parent_cache": worktree_blob(PARENT_CACHE),
        "curved": git_output("rev-parse", CURVED_COMMIT),
        "curved_ancestor": is_ancestor(CURVED_COMMIT, "HEAD"),
        "curved_note": commit_blob(CURVED_COMMIT, CURVED_NOTE),
        "curved_runner": commit_blob(CURVED_COMMIT, CURVED_RUNNER),
        "worktree_curved_note": worktree_blob(CURVED_NOTE),
        "worktree_curved_runner": worktree_blob(CURVED_RUNNER),
    }


def raw_note() -> bytes:
    try:
        return NOTE_PATH.read_bytes()
    except OSError:
        return b""


def normalized_note(note: bytes) -> str:
    try:
        decoded = note.decode("utf-8")
    except UnicodeError:
        return ""
    return " ".join(decoded.lower().split())


def vectorize(matrix: sp.MatrixBase) -> sp.Matrix:
    return sp.Matrix(matrix.rows * matrix.cols, 1, list(matrix))


def translated_origin(
    origin: tuple[int, int], shift: tuple[int, int]
) -> tuple[int, int]:
    return ((origin[0] + shift[0]) % 2, (origin[1] + shift[1]) % 2)


def shifted_displayed(
    displacement: tuple[int, int],
) -> tuple[tuple[int, int], tuple[int, int]]:
    return tuple(
        translated_origin(origin, displacement) for origin in block134.DISPLAYED
    )


def frame_time_bit(gauge: sp.Matrix) -> int:
    block105 = block134.block105
    image = sp.simplify(gauge.H * block105.ET * gauge)
    if block134.matrix_zero(image - block105.ET):
        return 0
    if block134.matrix_zero(image + block105.ET.T):
        return 1
    raise ValueError("the frame gauge leaves the two-state ET orbit")


@dataclass(frozen=True)
class SelectorFactorization:
    origins: tuple[tuple[int, int], ...]
    selectors: tuple[tuple[int, int], ...]
    groups: tuple[tuple[tuple[int, int], tuple[int, ...]], ...]

    @property
    def rank(self) -> int:
        return len(self.groups)


_FACTORIZATION_CACHE: dict[
    tuple[tuple[int, int], ...], SelectorFactorization
] = {}


def selector_factorization(
    origins: tuple[tuple[int, int], ...],
) -> SelectorFactorization:
    """Factor the repeated scalar selectors once for a fixed chart list."""
    if origins in _FACTORIZATION_CACHE:
        return _FACTORIZATION_CACHE[origins]

    selectors: list[tuple[int, int]] = []
    grouped_indices: dict[tuple[int, int], list[int]] = {}
    for origin in origins:
        chart = block134.cover_chart_matrix(origin)
        physical_at = tuple(
            next(
                column
                for column in range(block134.SIZE)
                if chart[row, column] != 0
            )
            for row in range(block134.SIZE)
        )
        for cell in range(block134.NCELLS):
            start = 4 * cell
            for local_row in range(4):
                for local_column in range(4):
                    key = (
                        physical_at[start + local_row],
                        physical_at[start + local_column],
                    )
                    grouped_indices.setdefault(key, []).append(len(selectors))
                    selectors.append(key)

    factorization = SelectorFactorization(
        origins=origins,
        selectors=tuple(selectors),
        groups=tuple(
            (key, tuple(indices)) for key, indices in grouped_indices.items()
        ),
    )
    _FACTORIZATION_CACHE[origins] = factorization
    return factorization


def factorized_selector_system(
    chart_gauges: tuple[tuple[tuple[int, int], sp.Matrix], ...],
    local: sp.Matrix,
) -> block134.SelectorSystem:
    """Evaluate a cached selector factorization with exact chart data."""
    origins = tuple(origin for origin, _ in chart_gauges)
    factorization = selector_factorization(origins)
    rhs: list[sp.Expr] = []
    for _, gauge in chart_gauges:
        target = sp.simplify(gauge.H * local * gauge)
        for _cell in range(block134.NCELLS):
            for local_row in range(4):
                for local_column in range(4):
                    rhs.append(sp.simplify(target[local_row, local_column]))

    averages: dict[tuple[int, int], sp.Expr] = {}
    conflicts: list[tuple[int, int, tuple[sp.Expr, ...]]] = []
    for key, indices in factorization.groups:
        values = tuple(rhs[index] for index in indices)
        average = sp.simplify(sum(values) / len(values))
        averages[key] = average
        if any(sp.simplify(value - values[0]) != 0 for value in values[1:]):
            conflicts.append((key[0], key[1], values))

    least_squares = sp.zeros(block134.SIZE)
    for (row, column), value in averages.items():
        least_squares[row, column] = value
    residual = tuple(
        sp.simplify(value - averages[key])
        for key, value in zip(factorization.selectors, rhs)
    )
    residual_norm_squared = sp.simplify(
        sum(sp.conjugate(value) * value for value in residual)
    )
    projection_exact = all(
        sp.simplify(sum(residual[index] for index in indices)) == 0
        for _, indices in factorization.groups
    )
    nonzero_residual = any(value != 0 for value in residual)
    rows = len(factorization.selectors)
    rank = factorization.rank
    return block134.SelectorSystem(
        rows=rows,
        columns=block134.SIZE**2,
        rank=rank,
        augmented_rank=rank + int(nonzero_residual),
        cokernel_dimension=rows - rank,
        selectors=factorization.selectors,
        rhs=tuple(rhs),
        least_squares=least_squares,
        residual=residual,
        residual_norm_squared=residual_norm_squared,
        conflicts=tuple(conflicts),
        projection_exact=projection_exact,
    )


def residual_is_zero(system: block134.SelectorSystem) -> bool:
    return (
        system.residual_norm_squared == 0
        and all(sp.simplify(value) == 0 for value in system.residual)
        and system.projection_exact
    )


@dataclass(frozen=True)
class FamilyCertificate:
    shifted_total: int
    shifted_inconsistent: int
    shifted_signatures: tuple[tuple[tuple[int, int, int], int], ...]
    full_total: int
    full_inconsistent: int
    full_signatures: tuple[tuple[tuple[int, int, int], int], ...]
    every_residual_zero: bool


def family_certificate(sx: sp.Expr, st: sp.Expr) -> FamilyCertificate:
    """Enumerate 4x4x4 overlaps and 4^4 full-atlas assignments exactly."""
    local = block134.local_differential(sx, st)
    representatives = tuple(
        gauge for _, gauge in block134.gauge_representatives()
    )
    shifted_signatures: Counter[tuple[int, int, int]] = Counter()
    shifted_inconsistent = 0
    shifted_total = 0
    every_residual_zero = True
    for displacement in block134.ORIGINS:
        pair = shifted_displayed(displacement)
        for left, right in product(representatives, repeat=2):
            system = factorized_selector_system(
                ((pair[0], left), (pair[1], right)), local
            )
            signature = (
                system.rank,
                system.augmented_rank,
                system.cokernel_dimension,
            )
            shifted_signatures[signature] += 1
            shifted_inconsistent += int(not system.consistent)
            shifted_total += 1
            every_residual_zero &= residual_is_zero(system)

    full_signatures: Counter[tuple[int, int, int]] = Counter()
    full_inconsistent = 0
    full_total = 0
    for assignment in product(representatives, repeat=len(block134.ORIGINS)):
        system = factorized_selector_system(
            tuple(zip(block134.ORIGINS, assignment, strict=True)), local
        )
        signature = (
            system.rank,
            system.augmented_rank,
            system.cokernel_dimension,
        )
        full_signatures[signature] += 1
        full_inconsistent += int(not system.consistent)
        full_total += 1
        every_residual_zero &= residual_is_zero(system)

    return FamilyCertificate(
        shifted_total,
        shifted_inconsistent,
        tuple(sorted(shifted_signatures.items())),
        full_total,
        full_inconsistent,
        tuple(sorted(full_signatures.items())),
        every_residual_zero,
    )


def nonzero_family_exact(certificate: FamilyCertificate) -> bool:
    return (
        certificate.shifted_total == 64
        and certificate.shifted_inconsistent == 64
        and certificate.shifted_signatures == (((192, 193, 64), 64),)
        and certificate.full_total == 256
        and certificate.full_inconsistent == 256
        and certificate.full_signatures == (((288, 289, 224), 256),)
        and not certificate.every_residual_zero
    )


def zero_shear_family_exact(certificate: FamilyCertificate) -> bool:
    return (
        certificate.shifted_total == 64
        and certificate.shifted_inconsistent == 0
        and certificate.shifted_signatures == (((192, 192, 64), 64),)
        and certificate.full_total == 256
        and certificate.full_inconsistent == 0
        and certificate.full_signatures == (((288, 288, 224), 256),)
        and certificate.every_residual_zero
    )


def coordinate_decoder(basis: sp.Matrix) -> tuple[tuple[int, ...], sp.Matrix]:
    """Factor an exact pivot minor once for repeated coordinate decoding."""
    pivot_rows = tuple(sp.Matrix(basis.T).rref()[1])
    if len(pivot_rows) != basis.cols:
        raise ValueError("the residual coordinate basis is not independent")
    minor = basis.extract(pivot_rows, range(basis.cols))
    return pivot_rows, minor.inv()


def basis_coordinates(
    basis: sp.Matrix,
    vector: sp.Matrix,
    decoder: tuple[tuple[int, ...], sp.Matrix],
) -> sp.Matrix:
    """Decode a vector in a cached two-column exact pivot minor."""
    pivot_rows, inverse_minor = decoder
    selected = vector.extract(pivot_rows, (0,))
    coordinates = sp.simplify(inverse_minor * selected)
    if not block134.matrix_zero(basis * coordinates - vector):
        raise ValueError("the residual is outside the displayed coordinate plane")
    return coordinates


@dataclass(frozen=True)
class OrbitCertificate:
    kappa_basis: sp.Matrix
    gauge_law_exact: bool
    all_frame_coordinates: tuple[tuple[sp.Expr, sp.Expr], ...]
    strict_coordinates: tuple[tuple[sp.Expr, sp.Expr], ...]
    coboundary_matrix: sp.Matrix
    coboundary_image: sp.Matrix
    coboundary_exact: bool
    separation_exact: bool


def orbit_certificate(sx: sp.Symbol, st: sp.Symbol) -> OrbitCertificate:
    """Compute the orbit and its coboundary image in (K_0,K_1)."""
    local = block134.local_differential(sx, st)
    gauge_by_name = dict(block134.gauge_representatives())
    base_pair = block134.DISPLAYED
    system_0 = factorized_selector_system(
        ((base_pair[0], gauge_by_name["1"]), (base_pair[1], gauge_by_name["1"])),
        local,
    )
    system_1 = factorized_selector_system(
        ((base_pair[0], gauge_by_name["1"]), (base_pair[1], gauge_by_name["Rt"])),
        local,
    )
    kappa_0 = sp.simplify(block134.conflict_operator(system_0) / (I * st))
    kappa_1 = sp.simplify(block134.conflict_operator(system_1) / (I * st))
    basis = sp.Matrix.hstack(vectorize(kappa_0), vectorize(kappa_1))
    if basis.rank() != 2:
        raise ValueError("K_0 and K_1 do not form the displayed coordinate basis")
    decoder = coordinate_decoder(basis)

    all_coordinates: list[tuple[sp.Expr, sp.Expr]] = []
    gauge_law_exact = True
    for displacement in block134.ORIGINS:
        pair = shifted_displayed(displacement)
        translation = block134.cover_translation(displacement)
        for (_, left), (_, right) in product(
            block134.gauge_representatives(), repeat=2
        ):
            system = factorized_selector_system(
                ((pair[0], left), (pair[1], right)), local
            )
            conflict = block134.conflict_operator(system)
            pulled_back = sp.simplify(
                translation.T * conflict * translation / (I * st)
            )
            coordinates = basis_coordinates(basis, vectorize(pulled_back), decoder)
            n_value = frame_time_bit(left) + frame_time_bit(right)
            expected = sp.Matrix((1 - n_value, n_value))
            gauge_law_exact &= (
                coordinates == expected
                and sp.simplify(sum(coordinates)) == 1
                and block134.matrix_zero(
                    pulled_back - (1 - n_value) * kappa_0 - n_value * kappa_1
                )
            )
            all_coordinates.append(tuple(coordinates))

    strict_coordinates: list[tuple[sp.Expr, sp.Expr]] = []
    for displacement in block134.ORIGINS:
        pair = shifted_displayed(displacement)
        translation = block134.cover_translation(displacement)
        system = factorized_selector_system(
            tuple((origin, block134.chart_gauge(origin)) for origin in pair),
            local,
        )
        pulled_back = sp.simplify(
            translation.T
            * block134.conflict_operator(system)
            * translation
            / (I * st)
        )
        strict_coordinates.append(
            tuple(basis_coordinates(basis, vectorize(pulled_back), decoder))
        )

    # The columns are direct differences along both Z_2 atlas generators.
    coordinate_by_origin = dict(zip(block134.ORIGINS, strict_coordinates))
    coboundary_columns = []
    for origin in block134.ORIGINS:
        source = sp.Matrix(coordinate_by_origin[origin])
        for generator in ((1, 0), (0, 1)):
            target = sp.Matrix(
                coordinate_by_origin[translated_origin(origin, generator)]
            )
            coboundary_columns.append(sp.simplify(target - source))
    coboundary = sp.Matrix.hstack(*coboundary_columns)
    atlas_parameters = sp.symbols("c_0:8", rational=True)
    image = sp.simplify(coboundary * sp.Matrix(atlas_parameters))
    augmentation = sp.Matrix([[1, 1]])
    augmentation_kernel_generator = sp.Matrix((-1, 1))
    coboundary_exact = (
        coboundary.shape == (2, 8)
        and coboundary.rank() == 1
        and block134.matrix_zero(augmentation * coboundary)
        and sp.simplify(image[0] + image[1]) == 0
        and sp.Matrix.hstack(coboundary, augmentation_kernel_generator).rank()
        == 1
    )
    distinct_strict = tuple(dict.fromkeys(strict_coordinates))
    orbit_exact = (
        distinct_strict == ((-1, 2), (1, 0))
        or distinct_strict == ((1, 0), (-1, 2))
    ) and all(sp.simplify(sum(point)) == 1 for point in strict_coordinates)
    separation_exact = orbit_exact and all(
        sp.Matrix.hstack(coboundary, sp.Matrix(point)).rank()
        > coboundary.rank()
        for point in distinct_strict
    )
    return OrbitCertificate(
        basis,
        gauge_law_exact,
        tuple(all_coordinates),
        tuple(strict_coordinates),
        coboundary,
        image,
        coboundary_exact,
        separation_exact,
    )


def origin_atlas_certificate(local: sp.Matrix) -> dict[str, object]:
    """Certify the parity-origin torsor from the one-site lattice shifts."""
    origins = block134.ORIGINS
    sites = tuple(
        (time_coordinate, space_coordinate)
        for time_coordinate in range(block134.COVER_TIME_EXTENT)
        for space_coordinate in range(block134.SPACE_EXTENT)
    )
    classified = tuple((time % 2, space % 2) for time, space in sites)
    class_counts = Counter(classified)

    generator_exact = True
    generator_matrices = {}
    for generator in ((1, 0), (0, 1)):
        matrix = block134.cover_translation(generator)
        generator_matrices[generator] = matrix
        edges = block134.support(matrix)
        image_by_column = {column: row for row, column, value in edges if value == 1}
        generator_exact &= (
            matrix.shape == (block134.SIZE, block134.SIZE)
            and len(edges) == block134.SIZE
            and len(image_by_column) == block134.SIZE
            and block134.matrix_zero(matrix.H * matrix - sp.eye(block134.SIZE))
        )
        for time_coordinate, space_coordinate in sites:
            source = block134.cover_index(time_coordinate, space_coordinate)
            expected = block134.cover_index(
                time_coordinate + generator[0],
                space_coordinate + generator[1],
            )
            generator_exact &= image_by_column.get(source) == expected
            target_time, target_space = divmod(
                image_by_column.get(source, -1), block134.SPACE_EXTENT
            )
            generator_exact &= (
                (target_time % 2, target_space % 2)
                == translated_origin((time_coordinate % 2, space_coordinate % 2), generator)
            )

    action_signatures = {
        shift: tuple(translated_origin(origin, shift) for origin in origins)
        for shift in origins
    }
    group_exact = (
        len(set(action_signatures.values())) == 4
        and all(
            translated_origin(translated_origin(origin, left), right)
            == translated_origin(origin, translated_origin(left, right))
            for origin in origins
            for left in origins
            for right in origins
        )
        and all(
            sum(
                translated_origin(source, shift) == target for shift in origins
            )
            == 1
            for source in origins
            for target in origins
        )
        and block134.matrix_zero(
            generator_matrices[(1, 0)] * generator_matrices[(0, 1)]
            - generator_matrices[(0, 1)] * generator_matrices[(1, 0)]
        )
    )

    closed_sets: list[frozenset[tuple[int, int]]] = []
    for size in range(1, len(origins) + 1):
        for candidate_tuple in combinations(origins, size):
            candidate = set(candidate_tuple)
            if all(
                translated_origin(origin, generator) in candidate
                for origin in candidate
                for generator in ((1, 0), (0, 1))
            ):
                closed_sets.append(frozenset(candidate))

    gauge = block134.gauge_certificate(local)
    gauge_import_exact = (
        gauge.cover_size == 8
        and gauge.distinct_cover_elements == 8
        and gauge.distinct_adjoint_actions == 4
        and gauge.central_kernel_order == 2
        and gauge.action_multiplicities == (2, 2, 2, 2)
        and gauge.group_closed
        and gauge.orbit_equal
        and gauge.every_system_inconsistent
    )
    return {
        "classification": (
            tuple(origins) == ((0, 0), (0, 1), (1, 0), (1, 1))
            and len(classified) == block134.SIZE
            and class_counts == Counter({origin: 8 for origin in origins})
        ),
        "generators": generator_exact,
        "group": group_exact,
        "closed_sets": tuple(closed_sets),
        "gauge_import": gauge_import_exact,
    }


@dataclass(frozen=True)
class ParameterPoint:
    sx: sp.Rational
    st: sp.Rational
    mass: sp.Rational
    shear: sp.Rational
    volume: sp.Rational


PARAMETER_POINTS = (
    ParameterPoint(R(3, 5), R(4, 5), R(2, 7), R(1, 5), R(5, 4)),
    ParameterPoint(R(-2, 3), R(4, 5), R(5, 11), R(-1, 4), R(7, 6)),
    ParameterPoint(R(7, 9), R(4, 5), R(3, 13), R(2, 7), R(9, 8)),
)


def exact_expression(value: object) -> bool:
    if isinstance(value, sp.MatrixBase):
        return not value.has(sp.Float)
    return not sp.sympify(value).has(sp.Float)


def normal_form_certificate(
    sx: sp.Symbol,
    st: sp.Symbol,
    strict_coordinates: tuple[tuple[sp.Expr, sp.Expr], ...],
) -> tuple[bool, int]:
    """Reduce all four strict translated representatives by their exact W."""
    local = block134.local_differential(sx, st)
    witnessed_types: set[tuple[sp.Expr, sp.Expr]] = set()
    every_exact = True
    for displacement, coordinate in zip(
        block134.ORIGINS, strict_coordinates, strict=True
    ):
        pair = shifted_displayed(displacement)
        system = factorized_selector_system(
            tuple((origin, block134.chart_gauge(origin)) for origin in pair),
            local,
        )
        certificate = block134.residual_operator_certificate(system, st)
        w_matrix = certificate.residual_frame
        expected = sp.simplify(
            2
            * I
            * st
            * certificate.time_shift_inverse
            * certificate.even_projector
            * certificate.spatial_shift
        )
        every_exact &= (
            system.class_nonzero
            and certificate.signed_frame_exact
            and certificate.grading_mechanism_exact
            and block134.matrix_zero(
                w_matrix * certificate.raw_operator * w_matrix.H - expected
            )
            and block134.matrix_zero(certificate.omega - expected)
            and block134.matrix_zero(w_matrix.H * w_matrix - sp.eye(block134.SIZE))
            and certificate.omega.rank() == 16
            and len(block134.support(certificate.omega)) == 16
            and block134.matrix_zero(certificate.omega**2)
            and sp.factor(sp.trace(certificate.omega.H * certificate.omega))
            == 64 * st**2
        )
        witnessed_types.add(coordinate)
    expected_types = set(strict_coordinates)
    return every_exact and witnessed_types == expected_types, len(witnessed_types)


N5_LINES = (
    "N5: per_element: exact origin-premise, exhaustive-verdict, coboundary-image, parameter-sweep, normal-form, and exception certificates are checked",
    "per_site: one Grassmann mode per fine site on the antiperiodic reflection torus",
    "per_mode: every admissible atlas in the translation-closed class yields an inconsistent matching system whose residual orbit lies on the unit-augmentation line while the coboundary image has augmentation zero",
    "per_block: the residual class is invariant physics for the displayed class — the obstruction is a system property of the time shear alone, vanishing exactly at zero time shear, with an explicit consistent exception displaying the class boundary",
    "lattice_wide: checked and not executed — the connection-with-residual curved formulation, richer carriers, the joint-lane program, the actual ADM/history transporter completion, joint gravity, the gravity constraint quotient beyond the displayed carrier, Records, audit retention, and TOE closure remain open",
)


SCOPE_KEYS = (
    "unique_translation_closed",
    "exhaustive",
    "coboundary_image",
    "affine_line",
    "never_meet",
    "bookkeeping",
    "time_shear_only",
    "parameter_sweep",
    "consistent_exception",
    "unification",
    "os_boundary",
    "axiom",
    "zero_retirement",
    "zero_score",
    "zero_e2e",
    "gravity_quotient",
    "adm",
    "n1_n8",
    "w1",
    "n5_resolution",
    "n5_verbatim",
    "qualified_class",
)


def scope_certificate(note: str, mutation: str) -> dict[str, bool]:
    forbidden_unqualified = (
        r"(?:therefore|thus|hence|we conclude that) curved os is impossible",
        r"this (?:is|proves|establishes) an? all-atlases (?:no-go|obstruction)",
        r"the theorem (?:proves|establishes) [^.]*all atlases",
        r"we prove that no curved os construction exists for any atlas",
    )
    result = {
        "unique_translation_closed": (
            "unique" in note and "translation-closed" in note
        ),
        "exhaustive": (
            "exhaustive" in note or "all 64" in note or "all 256" in note
        ),
        "coboundary_image": (
            "coboundary image" in note
            and ("augmentation-zero" in note or "a + b = 0" in note)
        ),
        "affine_line": "affine line" in note or "a + b = 1" in note,
        "never_meet": (
            "never meet" in note or "no orbit point is a coboundary" in note
        ),
        "bookkeeping": "bookkeeping" in note or "parametrization" in note,
        "time_shear_only": (
            "s_t" in note and ("only" in note or "time shear" in note)
        ),
        "parameter_sweep": (
            "parameter sweep" in note or "representative-free" in note
        ),
        "consistent_exception": (
            "consistent exception" in note or "class-relative" in note
        ),
        "unification": (
            "unification" in note or "lives entirely in the time shear" in note
        ),
        "os_boundary": (
            "not an os no-go" in note or "not a curved os no-go" in note
        ),
        "axiom": "no axiom amendment is justified" in note,
        "zero_retirement": "zero obligation retirement" in note,
        "zero_score": "no toe percentage moves" in note,
        "zero_e2e": (
            "retained-positive end-to-end theory count remains zero" in note
        ),
        "gravity_quotient": (
            "gravity constraint quotient remains unexecuted" in note
        ),
        "adm": "actual adm/history transporter remains" in note,
        "n1_n8": all(
            re.search(rf"\bn{index}\b", note) is not None for index in range(1, 9)
        ),
        "w1": re.search(r"\bw1\b", note) is not None,
        "n5_resolution": all(
            f"{resolution}:" in note
            for resolution in (
                "per_element",
                "per_site",
                "per_mode",
                "per_block",
                "lattice_wide",
            )
        ),
        "n5_verbatim": all(
            " ".join(line.lower().split()) in note for line in N5_LINES
        ),
        "qualified_class": (
            ("displayed atlas class" in note or "displayed class" in note)
            and not any(
                re.search(pattern, note) is not None
                for pattern in forbidden_unqualified
            )
        ),
    }
    if mutation == "weaken_no_go_packet":
        result["os_boundary"] = False
        result["n1_n8"] = False
        result["w1"] = False
    if mutation == "drop_n5_resolution":
        result["n5_resolution"] = False
        result["n5_verbatim"] = False
    if mutation == "claim_toe_progress":
        result["zero_score"] = False
    if mutation == "claim_axiom_amendment":
        result["axiom"] = False
    if mutation == "claim_unqualified_nogo":
        result["qualified_class"] = False
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS, default="")
    mutation = parser.parse_args().mutation
    started_ns = time.monotonic_ns()
    checks = Checks()

    note_bytes = raw_note()
    note = normalized_note(note_bytes)

    authority = authority_certificate(mutation)
    authority_raw = (
        AUDIT_TIMEOUT_SEC == 600
        and AUDIT_INPUT_PATHS
        == (
            "docs/ADMISSIBILITY_DIRAC_KAHLER_RESIDUAL_INVARIANCE_THEOREM_BOUNDED_THEOREM_NOTE_2026-08-17.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
            "docs/audit/data/axiom_premise_nodes.json",
            "docs/ADMISSIBILITY_DIRAC_KAHLER_CONNECTION_RESIDUAL_THEOREM_BOUNDED_THEOREM_NOTE_2026-08-17.md",
            "scripts/admissibility_dirac_kahler_connection_residual_theorem_2026_08_17.py",
            "logs/runner-cache/admissibility_dirac_kahler_connection_residual_theorem_2026_08_17.txt",
            "docs/ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md",
            "scripts/admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_2026_08_14.py",
        )
        and authority["main"] == CURRENT_MAIN
        and authority["axiom"] == authority["expected_axiom"]
        and authority["worktree_axiom"] == WORKTREE_AXIOM_BLOB
        and authority["registry"] == CURRENT_REGISTRY_BLOB
        and authority["worktree_registry"] == WORKTREE_REGISTRY_BLOB
        and authority["parent"] == PARENT_COMMIT
        and authority["parent_ancestor"]
        and all(
            authority[f"ancestor_{number}"] for number in range(103, 134)
        )
        and authority["parent_note"] == authority["expected_parent"]
        and authority["parent_runner"] == PARENT_RUNNER_BLOB
        and authority["parent_cache"] == PARENT_CACHE_BLOB
        and authority["worktree_parent_note"] == PARENT_NOTE_BLOB
        and authority["worktree_parent_runner"] == PARENT_RUNNER_BLOB
        and authority["worktree_parent_cache"] == PARENT_CACHE_BLOB
        and authority["curved"] == CURVED_COMMIT
        and authority["curved_ancestor"]
        and authority["curved_note"] == CURVED_NOTE_BLOB
        and authority["curved_runner"] == CURVED_RUNNER_BLOB
        and authority["worktree_curved_note"] == CURVED_NOTE_BLOB
        and authority["worktree_curved_runner"] == CURVED_RUNNER_BLOB
    )
    checks.check(
        "A-authority",
        "Block 134 parent blobs, ancestors 133--103, and Block 105 note/runner are content-bound",
        authority_raw,
    )

    fixture_local = block134.local_differential(block134.S_X, block134.S_T)
    atlas = origin_atlas_certificate(fixture_local)
    atlas_raw = (
        set(atlas)
        == {"classification", "generators", "group", "closed_sets", "gauge_import"}
        and bool(atlas["classification"])
        and bool(atlas["generators"])
        and bool(atlas["group"])
        and atlas["closed_sets"] == (frozenset(block134.ORIGINS),)
        and bool(atlas["gauge_import"])
    )
    checks.check(
        "B-the-atlas-class",
        "the mod-2 origins form the regular Z_2^2 one-site-translation torsor; the full four-origin atlas is the unique nonempty closed choice and Block 134 supplies 8 lifts/4 adjoint actions",
        atlas_raw and mutation != "break_origin_premises",
    )

    family_cache: dict[tuple[sp.Expr, sp.Expr], FamilyCertificate] = {}

    def cached_family(sx_value: sp.Expr, st_value: sp.Expr) -> FamilyCertificate:
        key = (sx_value, st_value)
        if key not in family_cache:
            family_cache[key] = family_certificate(sx_value, st_value)
        return family_cache[key]

    fixture_family = cached_family(block134.S_X, block134.S_T)
    adjoint_citation_raw = (
        "block 134" in note
        and "adjoint" in note
        and ("suffic" in note or "central kernel" in note)
    )
    exhaustive_raw = nonzero_family_exact(fixture_family) and adjoint_citation_raw
    checks.check(
        "C-the-exhaustive-verdict",
        "all 64 shifted-overlap and all 256 full-atlas adjoint systems are enumerated, inconsistent, and have the exact 192|193 and 288|289 rank profiles",
        exhaustive_raw and mutation != "break_exhaustive_count",
    )

    sx, st = sp.symbols("s_x s_t", real=True, nonzero=True)
    orbit = orbit_certificate(sx, st)
    all_frame_points = set(orbit.all_frame_coordinates)
    strict_points = set(orbit.strict_coordinates)
    bookkeeping_raw = all(
        sp.simplify((1 - n_value) + n_value) == 1 for n_value in (0, 1, 2)
    )
    coboundary_raw = (
        orbit.kappa_basis.rank() == 2
        and orbit.kappa_basis.free_symbols == set()
        and orbit.gauge_law_exact
        and len(orbit.all_frame_coordinates) == 64
        and all_frame_points == {(1, 0), (0, 1), (-1, 2)}
        and all(
            sp.simplify(first + second) == 1
            for first, second in orbit.all_frame_coordinates
        )
        and strict_points == {(1, 0), (-1, 2)}
        and orbit.coboundary_exact
        and orbit.separation_exact
        and bookkeeping_raw
    )
    if mutation in ("break_coboundary_image", "claim_augmentation_content"):
        coboundary_raw = False
    checks.check(
        "D-the-coboundary-characterization",
        "the orbit lies on a+b=1 while the directly computed coboundary image is a+b=0, so they never meet; (1-n)+n=1 is bookkeeping",
        coboundary_raw,
    )

    sweep_systems = tuple(
        (
            factorized_selector_system(
                tuple(
                    (origin, block134.chart_gauge(origin))
                    for origin in block134.DISPLAYED
                ),
                block134.local_differential(point.sx, point.st),
            ),
            factorized_selector_system(
                tuple(
                    (origin, block134.chart_gauge(origin))
                    for origin in block134.ORIGINS
                ),
                block134.local_differential(point.sx, point.st),
            ),
        )
        for point in PARAMETER_POINTS
    )
    hodge_samples = tuple(
        block134.block105.shear_hodge(point.shear, point.volume)
        for point in PARAMETER_POINTS
    )
    point_variation_exact = (
        len(PARAMETER_POINTS) >= 3
        and len({point.sx for point in PARAMETER_POINTS}) >= 3
        and len({point.mass for point in PARAMETER_POINTS}) >= 3
        and len(
            {(point.shear, point.volume) for point in PARAMETER_POINTS}
        )
        >= 3
        and len({point.st for point in PARAMETER_POINTS}) == 1
        and next(iter({point.st for point in PARAMETER_POINTS})) != 0
        and all(
            exact_expression(value)
            for point in PARAMETER_POINTS
            for value in (point.sx, point.st, point.mass, point.shear, point.volume)
        )
        and all(
            exact_expression(hodge) and hodge.rank() == 4
            for hodge in hodge_samples
        )
    )
    probe_sx, probe_st, probe_mass, probe_shear, probe_volume = sp.symbols(
        "probe_sx probe_st probe_mass probe_shear probe_volume",
        real=True,
        nonzero=True,
    )
    probe_local = block134.local_differential(probe_sx, probe_st)
    probe_hodge = block134.block105.shear_hodge(probe_shear, probe_volume)
    probe_action = sp.simplify(
        probe_mass * probe_hodge
        + I * (probe_hodge * probe_local + probe_local.H * probe_hodge)
    )
    probe_two = factorized_selector_system(
        tuple(
            (origin, block134.chart_gauge(origin))
            for origin in block134.DISPLAYED
        ),
        probe_local,
    )
    probe_full = factorized_selector_system(
        tuple(
            (origin, block134.chart_gauge(origin))
            for origin in block134.ORIGINS
        ),
        probe_local,
    )
    residual_symbols = set().union(
        *(value.free_symbols for value in probe_two.residual + probe_full.residual)
    )
    parameter_footprint_exact = (
        {probe_mass, probe_shear, probe_volume}.issubset(probe_action.free_symbols)
        and residual_symbols == {probe_st}
        and probe_sx not in residual_symbols
        and probe_mass not in residual_symbols
        and probe_shear not in residual_symbols
        and probe_volume not in residual_symbols
    )
    sweep_verdicts = tuple(
        (
            two.rank,
            two.augmented_rank,
            two.cokernel_dimension,
            full.rank,
            full.augmented_rank,
            full.cokernel_dimension,
            two.consistent,
            full.consistent,
        )
        for two, full in sweep_systems
    )
    sweep_raw = (
        point_variation_exact
        and sweep_verdicts
        == (
            (192, 193, 64, 288, 289, 224, False, False),
        )
        * len(PARAMETER_POINTS)
        and all(
            two.class_nonzero and full.class_nonzero
            for two, full in sweep_systems
        )
        and orbit.kappa_basis.free_symbols == set()
        and orbit.gauge_law_exact
        and parameter_footprint_exact
    )
    zero_shear_local = block134.local_differential(
        block134.S_X, sp.Integer(0)
    )
    zero_shear_two = factorized_selector_system(
        tuple(
            (origin, block134.chart_gauge(origin))
            for origin in block134.DISPLAYED
        ),
        zero_shear_local,
    )
    zero_shear_full = factorized_selector_system(
        tuple(
            (origin, block134.chart_gauge(origin))
            for origin in block134.ORIGINS
        ),
        zero_shear_local,
    )
    degeneration_raw = (
        (
            zero_shear_two.rank,
            zero_shear_two.augmented_rank,
            zero_shear_two.cokernel_dimension,
        )
        == (192, 192, 64)
        and (
            zero_shear_full.rank,
            zero_shear_full.augmented_rank,
            zero_shear_full.cokernel_dimension,
        )
        == (288, 288, 224)
        and zero_shear_two.consistent
        and zero_shear_full.consistent
        and residual_is_zero(zero_shear_two)
        and residual_is_zero(zero_shear_full)
    )
    if mutation == "break_parameter_sweep":
        sweep_raw = False
    if mutation == "break_st_degeneration":
        degeneration_raw = False
    checks.check(
        "E-the-parameter-sweep",
        "at three exact points varying s_x, mass, and shear/volume, every rank profile persists for fixed nonzero s_t; at s_t=0 every system is consistent and every residual vanishes",
        sweep_raw and degeneration_raw,
    )

    normal_form_raw, orbit_type_count = normal_form_certificate(
        sx, st, orbit.strict_coordinates
    )
    checks.check(
        "F-the-normal-form",
        "samples spanning both strict orbit types obey W K W^dagger=2*i*s_t*T_t^-1*P_even*P_x, rank 16 and square zero",
        normal_form_raw
        and orbit_type_count == 2
        and mutation != "break_normal_form",
    )

    exception_pair = ((0, 0), (1, 1))
    exception_subset = set(exception_pair)
    exception_system = factorized_selector_system(
        tuple((origin, sp.eye(4)) for origin in exception_pair), fixture_local
    )
    exception_closed = all(
        translated_origin(origin, generator) in exception_subset
        for origin in exception_subset
        for generator in ((1, 0), (0, 1))
    )
    exception_raw = (
        exception_subset != set(block134.ORIGINS)
        and not exception_closed
        and exception_system.consistent
        and exception_system.rank == exception_system.augmented_rank
        and residual_is_zero(exception_system)
    )
    checks.check(
        "G-the-honest-exception",
        "the explicit diagonal subset {(0,0),(1,1)} is not translation-closed and its identity-frame matching system is consistent",
        exception_raw and mutation != "break_exception_consistency",
    )

    scope = scope_certificate(note, mutation)
    elapsed_ns = time.monotonic_ns() - started_ns
    checks.check(
        "H-scope",
        "class, exhaustive, coboundary, bookkeeping, parameter, exception, no-go, N1--N8/W1/N5, and TOE firewalls are present",
        set(scope) == set(SCOPE_KEYS)
        and all(scope.values())
        and elapsed_ns <= 400 * 1_000_000_000,
    )

    print(
        f"AUTHORITY: Block134 parent={authority['parent']}; note/runner/cache, "
        "ancestors 133--103, and Block105 note/runner pins exact"
    )
    print(
        "ATLAS: origins=(t mod 2,x mod 2)=Z_2^2; both one-site generators "
        "are lattice-certified; action=regular; unique nonempty translation-closed set=all 4; lifts/adjoints=8/4"
    )
    print(
        "SYSTEMS: shifted overlaps=64/64 inconsistent at rank[A|b]=192|193; "
        "full atlases=256/256 inconsistent at 288|289; adjoint sufficiency is imported from Block134"
    )
    print(
        "COBOUNDARY: strict orbit points in (K0,K1) are (-1,2),(1,0) on "
        "a+b=1; im(delta)={(-q,q)} lies on a+b=0; the sets never meet; (1-n)+n=1 is bookkeeping"
    )
    print(
        "PARAMETERS: 3-point representative-free sweep varies s_x, mass, and "
        "shear/volume at fixed s_t=4/5; the system obstruction is s_t-only and vanishes exactly at s_t=0"
    )
    print(
        "NORMAL_FORM: both orbit types satisfy W K W^dagger="
        "2*i*s_t*T_t^-1*P_even*P_x, rank=16, square=0"
    )
    print(
        f"EXCEPTION: charts={exception_pair}, translation_closed=false, "
        f"rank[A|b]={exception_system.rank}|{exception_system.augmented_rank}, verdict=CONSISTENT"
    )
    for line in N5_LINES:
        print(line)
    if checks.failed == 0:
        print(
            "RESULT: the campaign closes on the residual invariance theorem — "
            "the obstruction to curved OS is invariant physics for the displayed "
            "atlas class, powered entirely by the time shear, with the coboundary "
            "separation carrying the proof and the class boundary displayed"
        )
        print(
            "DECISION_CUT: build the connection-with-residual formulation on the "
            "invariant class; reject tautological-invariant framings and unqualified no-go readings"
        )
    else:
        print(
            "RESULT: BLOCKED — at least one exact authority, atlas, exhaustive, "
            "coboundary, parameter, normal-form, exception, scope, mutation, or runtime certificate failed"
        )
        print(
            "DECISION_CUT: repair the failed certificate without weakening the "
            "displayed-class boundary or promoting bookkeeping to invariant content"
        )
    print(
        "TOE: zero obligation retirement; no TOE percentage moves; "
        "retained-positive end-to-end theory count remains zero; gravity "
        "constraint quotient remains unexecuted; actual ADM/history transporter remains open"
    )
    return checks.finish()


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except SystemExit:
        raise
    except Exception as error:
        print(f"FAIL: {type(error).__name__}: {error}")
        print("TOTAL: PASS=0 FAIL=1")
        raise
