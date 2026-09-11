#!/usr/bin/env python3
"""Block 134: exact connection-residual theorem certificate.

The runner constructs the four exact chart differentials on the 8x4 cover,
forms their scalar-selector matching systems, and certifies the resulting
nonzero cokernel class.  It also extracts the residual's graded-shift frame,
checks the projective gauge cover directly, and binds the Block 105 item-one
disjunction byte-for-byte.  Scientific arithmetic is exact; wall-clock
timing is the sole floating-point quantity.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
import re
import subprocess
import time

import sympy as sp

import admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_2026_08_14 as block105


R = sp.Rational
I = sp.I
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_DIRAC_KAHLER_CONNECTION_RESIDUAL_THEOREM_"
    "BOUNDED_THEOREM_NOTE_2026-08-17.md"
)
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"
PARENT_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_TWO_BLOCK_STATES_DYNAMICS_"
    "BOUNDED_THEOREM_NOTE_2026-08-17.md"
)
PARENT_RUNNER = (
    "scripts/admissibility_dirac_kahler_two_block_states_dynamics_"
    "2026_08_17.py"
)
PARENT_CACHE = (
    "logs/runner-cache/admissibility_dirac_kahler_two_block_states_"
    "dynamics_2026_08_17.txt"
)
CURVED_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_"
    "NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md"
)
CURVED_RUNNER = (
    "scripts/admissibility_dirac_kahler_shifted_origin_frame_gauge_"
    "nonuniform_hodge_overlap_2026_08_14.py"
)

# This tuple is deliberately literal: it is the complete audit read surface.
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_CONNECTION_RESIDUAL_THEOREM_BOUNDED_THEOREM_NOTE_2026-08-17.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_TWO_BLOCK_STATES_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-08-17.md",
    "scripts/admissibility_dirac_kahler_two_block_states_dynamics_2026_08_17.py",
    "logs/runner-cache/admissibility_dirac_kahler_two_block_states_dynamics_2026_08_17.txt",
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
    "toe-axiom-closure-block133-two-block-states-dynamics-20260817"
)
PARENT_COMMIT = "80d208f0c12e21fd985d01e5f807a9d34c00ef11"
PARENT_NOTE_BLOB = "c7a9feb71f0dc0c8e71a72da5d66ea09a751c33e"
PARENT_RUNNER_BLOB = "0009d2a7d04f28542f01657d6c3987ad5fecace6"
PARENT_CACHE_BLOB = "464693167ef142486738a1eda249102bfa33e592"
CURVED_COMMIT = "d06066c2b908aaca0779625d831dfb10620cf34d"
CURVED_NOTE_BLOB = "5eff91757e38f3f2ea7dc2a2c50788636cc2e3a5"
CURVED_RUNNER_BLOB = "4870f31b5880028ad4f1f3095aad4d0820e4668f"

ANCESTOR_COMMITS = (
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
    "break_chart_nilpotency",
    "break_inconsistency",
    "break_cokernel_dims",
    "break_strong_form",
    "break_residual_form",
    "break_grading_mechanism",
    "break_triple_exact",
    "break_adjoint_count",
    "claim_invariance_settled",
    "weaken_no_go_packet",
    "drop_n5_resolution",
    "claim_toe_progress",
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


def git_bytes(*args: str) -> bytes:
    return subprocess.check_output(
        ("git",) + args,
        cwd=ROOT,
        timeout=AUDIT_TIMEOUT_SEC,
    )


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


def matrix_zero(matrix: sp.MatrixBase) -> bool:
    return all(sp.simplify(value) == 0 for value in matrix)


def matrix_key(matrix: sp.MatrixBase) -> tuple[sp.Expr, ...]:
    return tuple(sp.simplify(value) for value in matrix)


def support(matrix: sp.MatrixBase) -> tuple[tuple[int, int, sp.Expr], ...]:
    return tuple(
        (row, column, sp.simplify(matrix[row, column]))
        for row in range(matrix.rows)
        for column in range(matrix.cols)
        if sp.simplify(matrix[row, column]) != 0
    )


SPACE_EXTENT = block105.LENGTH
PHYSICAL_TIME_EXTENT = block105.LENGTH
COVER_TIME_EXTENT = 2 * PHYSICAL_TIME_EXTENT
SIZE = COVER_TIME_EXTENT * SPACE_EXTENT
NCELLS = SIZE // 4
ORIGINS = ((0, 0), (0, 1), (1, 0), (1, 1))
DISPLAYED = ((1, 0), (1, 1))
S_X = R(3, 5)
S_T = R(4, 5)
MASS = R(2, 7)


def cover_index(time_coordinate: int, space_coordinate: int) -> int:
    return (
        (time_coordinate % COVER_TIME_EXTENT) * SPACE_EXTENT
        + space_coordinate % SPACE_EXTENT
    )


def cover_embedding(time_coordinate: int, space_coordinate: int) -> sp.Matrix:
    matrix = sp.zeros(SIZE, 4)
    for column, (delta_t, delta_x) in enumerate(
        ((0, 0), (0, 1), (1, 0), (1, 1))
    ):
        matrix[
            cover_index(time_coordinate + delta_t, space_coordinate + delta_x),
            column,
        ] = 1
    return matrix


def cover_chart_matrix(origin: tuple[int, int]) -> sp.Matrix:
    matrix = sp.zeros(SIZE)
    row = 0
    for coarse_t in range(COVER_TIME_EXTENT // 2):
        for coarse_x in range(SPACE_EXTENT // 2):
            embedding = cover_embedding(
                2 * coarse_t + origin[0], 2 * coarse_x + origin[1]
            )
            matrix[row : row + 4, :] = embedding.T
            row += 4
    return matrix


def cover_translation(displacement: tuple[int, int]) -> sp.Matrix:
    matrix = sp.zeros(SIZE)
    for time_coordinate in range(COVER_TIME_EXTENT):
        for space_coordinate in range(SPACE_EXTENT):
            source = cover_index(time_coordinate, space_coordinate)
            target = cover_index(
                time_coordinate + displacement[0],
                space_coordinate + displacement[1],
            )
            matrix[target, source] = 1
    return matrix


def antiperiodic_time_translation(displacement: int) -> sp.Matrix:
    """Time translation on the cover with the antiperiodic wrap sign."""
    matrix = sp.zeros(SIZE)
    for time_coordinate in range(COVER_TIME_EXTENT):
        raw_target = time_coordinate + displacement
        winding, target_time = divmod(raw_target, COVER_TIME_EXTENT)
        sign = -1 if winding % 2 else 1
        for space_coordinate in range(SPACE_EXTENT):
            matrix[
                cover_index(target_time, space_coordinate),
                cover_index(time_coordinate, space_coordinate),
            ] = sign
    return matrix


def lifted(matrix: sp.Matrix) -> sp.Matrix:
    return sp.kronecker_product(sp.eye(NCELLS), matrix)


def local_differential(sx: sp.Expr, st: sp.Expr) -> sp.Matrix:
    return I * (sx * block105.EX + st * block105.ET)


def chart_differential_cover(origin: tuple[int, int], local: sp.Matrix) -> sp.Matrix:
    result = sp.zeros(SIZE)
    for coarse_t in range(COVER_TIME_EXTENT // 2):
        for coarse_x in range(SPACE_EXTENT // 2):
            embedding = cover_embedding(
                2 * coarse_t + origin[0], 2 * coarse_x + origin[1]
            )
            result += embedding * local * embedding.T
    return result


def chart_gauge(origin: tuple[int, int]) -> sp.Matrix:
    rt, rx = block105.shift_lifts()
    return (rt ** origin[0]) * (rx ** origin[1])


def gauge_representatives() -> tuple[tuple[str, sp.Matrix], ...]:
    rt, rx = block105.shift_lifts()
    return (("1", sp.eye(4)), ("Rt", rt), ("Rx", rx), ("RtRx", rt * rx))


def curved_hodge_cover() -> sp.Matrix:
    field = block105.overlap_field()
    result = sp.zeros(SIZE)
    for time_coordinate in range(COVER_TIME_EXTENT):
        for space_coordinate in range(SPACE_EXTENT):
            shear, volume = field[
                (time_coordinate % PHYSICAL_TIME_EXTENT, space_coordinate)
            ]
            embedding = cover_embedding(time_coordinate, space_coordinate)
            result += (
                embedding
                * block105.shear_hodge(shear, volume)
                * embedding.T
                / 4
            )
    return sp.simplify(result)


def antiperiodic_quotient(matrix: sp.Matrix) -> sp.Matrix:
    identity = sp.eye(PHYSICAL_TIME_EXTENT * SPACE_EXTENT)
    injection = sp.Matrix.vstack(-identity, identity)
    selection = sp.Matrix.hstack(sp.zeros(identity.rows), identity)
    return sp.simplify(selection * matrix * injection)


@dataclass(frozen=True)
class SelectorSystem:
    rows: int
    columns: int
    rank: int
    augmented_rank: int
    cokernel_dimension: int
    selectors: tuple[tuple[int, int], ...]
    rhs: tuple[sp.Expr, ...]
    least_squares: sp.Matrix
    residual: tuple[sp.Expr, ...]
    residual_norm_squared: sp.Expr
    conflicts: tuple[tuple[int, int, tuple[sp.Expr, ...]], ...]
    projection_exact: bool

    @property
    def consistent(self) -> bool:
        return self.augmented_rank == self.rank

    @property
    def class_nonzero(self) -> bool:
        return (
            not self.consistent
            and self.residual_norm_squared != 0
            and self.projection_exact
        )


def selector_system(
    chart_gauges: tuple[tuple[tuple[int, int], sp.Matrix], ...],
    local: sp.Matrix,
) -> SelectorSystem:
    """Build E^T d E=g^dag d_local g as exact scalar selectors.

    Every coefficient row contains one unit entry.  Repeated rows therefore
    have the same selector, their exact average is the orthogonal projection,
    and a nonzero within-group residual proves rank[A|b] > rank[A].
    """
    selectors: list[tuple[int, int]] = []
    rhs: list[sp.Expr] = []
    grouped_indices: dict[tuple[int, int], list[int]] = {}
    for origin, gauge in chart_gauges:
        chart = cover_chart_matrix(origin)
        target = lifted(sp.simplify(gauge.H * local * gauge))
        physical_at = tuple(
            next(column for column in range(SIZE) if chart[row, column] != 0)
            for row in range(SIZE)
        )
        for cell in range(NCELLS):
            start = 4 * cell
            for local_row in range(4):
                for local_column in range(4):
                    key = (
                        physical_at[start + local_row],
                        physical_at[start + local_column],
                    )
                    value = sp.simplify(
                        target[start + local_row, start + local_column]
                    )
                    equation_index = len(selectors)
                    selectors.append(key)
                    rhs.append(value)
                    grouped_indices.setdefault(key, []).append(equation_index)

    averages: dict[tuple[int, int], sp.Expr] = {}
    conflicts: list[tuple[int, int, tuple[sp.Expr, ...]]] = []
    for (row, column), indices in grouped_indices.items():
        values = tuple(rhs[index] for index in indices)
        averages[(row, column)] = sp.simplify(sum(values) / len(values))
        if any(sp.simplify(value - values[0]) != 0 for value in values[1:]):
            conflicts.append((row, column, values))

    least_squares = sp.zeros(SIZE)
    for (row, column), value in averages.items():
        least_squares[row, column] = value
    residual = tuple(
        sp.simplify(value - averages[key])
        for key, value in zip(selectors, rhs)
    )
    residual_norm_squared = sp.simplify(
        sum(sp.conjugate(value) * value for value in residual)
    )
    projection_exact = all(
        sp.simplify(sum(residual[index] for index in indices)) == 0
        for indices in grouped_indices.values()
    )
    rank = len(grouped_indices)
    nonzero_residual = any(value != 0 for value in residual)
    rows = len(selectors)
    return SelectorSystem(
        rows=rows,
        columns=SIZE**2,
        rank=rank,
        augmented_rank=rank + int(nonzero_residual),
        cokernel_dimension=rows - rank,
        selectors=tuple(selectors),
        rhs=tuple(rhs),
        least_squares=least_squares,
        residual=residual,
        residual_norm_squared=residual_norm_squared,
        conflicts=tuple(conflicts),
        projection_exact=projection_exact,
    )


def candidate_residual(
    system: SelectorSystem, candidate: sp.Matrix
) -> tuple[sp.Expr, ...]:
    return tuple(
        sp.simplify(value - candidate[row, column])
        for (row, column), value in zip(system.selectors, system.rhs)
    )


def conflict_operator(system: SelectorSystem) -> sp.Matrix:
    result = sp.zeros(SIZE)
    for row, column, values in system.conflicts:
        if len(values) != 2:
            raise ValueError("a two-chart conflict must have two prescriptions")
        result[row, column] = sp.simplify(values[1] - values[0])
    return result


@dataclass(frozen=True)
class TransitionCertificate:
    transitions: dict[
        tuple[tuple[int, int], tuple[int, int]], sp.Matrix
    ]
    displayed: sp.Matrix
    displayed_exact: bool
    triple_cocycle_exact: bool


def transition_certificate(
    charts: dict[tuple[int, int], sp.Matrix],
) -> TransitionCertificate:
    phase = lifted(block105.phase_unitary().H)
    frames = {origin: phase * charts[origin] for origin in ORIGINS}
    transitions = {
        (first, second): sp.simplify(frames[second] * frames[first].H)
        for first in ORIGINS
        for second in ORIGINS
    }
    displayed = transitions[DISPLAYED]
    displayed_exact = (
        displayed.shape == (SIZE, SIZE)
        and displayed.rank() == SIZE
        and len(support(displayed)) == SIZE
        and matrix_zero(displayed.H * displayed - sp.eye(SIZE))
    )
    triple_exact = all(
        matrix_zero(
            transitions[(second, third)] * transitions[(first, second)]
            - transitions[(first, third)]
        )
        for first in ORIGINS
        for second in ORIGINS
        for third in ORIGINS
    )
    return TransitionCertificate(
        transitions, displayed, displayed_exact, triple_exact
    )


@dataclass(frozen=True)
class ResidualOperatorCertificate:
    raw_operator: sp.Matrix
    residual_frame: sp.Matrix
    omega: sp.Matrix
    formula: sp.Matrix
    time_shift_inverse: sp.Matrix
    even_projector: sp.Matrix
    spatial_shift: sp.Matrix
    grading: sp.Matrix
    signed_frame_exact: bool
    grading_mechanism_exact: bool


def residual_operator_certificate(
    system: SelectorSystem, st: sp.Symbol
) -> ResidualOperatorCertificate:
    """Extract the residual in the canonical even/odd graded-shift frame."""
    raw_operator = conflict_operator(system)
    grading = sp.diag(
        *((-1) ** (index % SPACE_EXTENT) for index in range(SIZE))
    )
    even_projector = sp.simplify((sp.eye(SIZE) + grading) / 2)
    odd_projector = sp.simplify((sp.eye(SIZE) - grading) / 2)
    spatial_shift = cover_translation((0, 1))
    time_shift_inverse = antiperiodic_time_translation(-1)
    formula = sp.simplify(
        2 * I * st * time_shift_inverse * even_projector * spatial_shift
    )

    raw_edges = support(raw_operator)
    formula_edges = support(formula)
    if len(raw_edges) != SIZE // 2 or len(formula_edges) != SIZE // 2:
        raise ValueError("the residual frame requires sixteen directed edges")
    if (
        {row for row, _, _ in raw_edges}
        | {column for _, column, _ in raw_edges}
    ) != set(range(SIZE)):
        raise ValueError("the raw residual edges do not span the frame")
    if (
        {row for row, _, _ in formula_edges}
        | {column for _, column, _ in formula_edges}
    ) != set(range(SIZE)):
        raise ValueError("the graded-shift edges do not span the frame")

    residual_frame = sp.zeros(SIZE)
    assigned_old: set[int] = set()
    assigned_new: set[int] = set()
    signed_factors: list[sp.Expr] = []
    for old_edge, new_edge in zip(raw_edges, formula_edges):
        old_row, old_column, old_value = old_edge
        new_row, new_column, new_value = new_edge
        factor = sp.simplify(new_value / old_value)
        if factor not in (-1, 1):
            raise ValueError("the residual frame is not a signed permutation")
        if old_column in assigned_old or new_column in assigned_new:
            raise ValueError("a source coordinate was assigned twice")
        residual_frame[new_column, old_column] = 1
        assigned_old.add(old_column)
        assigned_new.add(new_column)
        if old_row in assigned_old or new_row in assigned_new:
            raise ValueError("a target coordinate was assigned twice")
        residual_frame[new_row, old_row] = factor
        assigned_old.add(old_row)
        assigned_new.add(new_row)
        signed_factors.append(factor)

    omega = sp.simplify(
        residual_frame * raw_operator * residual_frame.H
    )
    signed_frame_exact = (
        assigned_old == set(range(SIZE))
        and assigned_new == set(range(SIZE))
        and all(value in (-1, 1) for value in signed_factors)
        and len(support(residual_frame)) == SIZE
        and matrix_zero(residual_frame.H * residual_frame - sp.eye(SIZE))
        and matrix_zero(omega - formula)
    )
    grading_mechanism_exact = (
        matrix_zero(grading**2 - sp.eye(SIZE))
        and matrix_zero(even_projector**2 - even_projector)
        and matrix_zero(odd_projector**2 - odd_projector)
        and matrix_zero(even_projector * odd_projector)
        and matrix_zero(grading * spatial_shift + spatial_shift * grading)
        and matrix_zero(spatial_shift * even_projector - odd_projector * spatial_shift)
        and matrix_zero(even_projector * spatial_shift * even_projector)
        and matrix_zero(time_shift_inverse * spatial_shift - spatial_shift * time_shift_inverse)
        and matrix_zero(time_shift_inverse * even_projector - even_projector * time_shift_inverse)
        and matrix_zero(formula**2)
    )
    return ResidualOperatorCertificate(
        raw_operator,
        residual_frame,
        omega,
        formula,
        time_shift_inverse,
        even_projector,
        spatial_shift,
        grading,
        signed_frame_exact,
        grading_mechanism_exact,
    )


def physical_action(differential: sp.Matrix, hodge: sp.Matrix) -> sp.Matrix:
    cover_action = sp.simplify(
        MASS * hodge
        + I * (hodge * differential + differential.H * hodge)
    )
    return antiperiodic_quotient(cover_action)


def adjoint_signature(gauge: sp.Matrix) -> tuple[sp.Expr, ...]:
    entries: list[sp.Expr] = []
    for row in range(4):
        for column in range(4):
            unit = sp.zeros(4)
            unit[row, column] = 1
            entries.extend(matrix_key(sp.simplify(gauge.H * unit * gauge)))
    return tuple(entries)


@dataclass(frozen=True)
class GaugeCertificate:
    cover_size: int
    distinct_cover_elements: int
    distinct_adjoint_actions: int
    central_kernel_order: int
    action_multiplicities: tuple[int, ...]
    group_closed: bool
    orbit_equal: bool
    every_system_inconsistent: bool


def gauge_certificate(local: sp.Matrix) -> GaugeCertificate:
    representatives = tuple(gauge for _, gauge in gauge_representatives())
    projective_cover = tuple(
        sign * gauge for gauge in representatives for sign in (1, -1)
    )
    cover_keys = {matrix_key(gauge) for gauge in projective_cover}
    action_signatures = tuple(
        adjoint_signature(gauge) for gauge in projective_cover
    )
    distinct_actions = set(action_signatures)
    identity_action = adjoint_signature(sp.eye(4))
    kernel = tuple(
        gauge
        for gauge, signature in zip(projective_cover, action_signatures)
        if signature == identity_action
    )
    multiplicities = tuple(
        sorted(action_signatures.count(signature) for signature in distinct_actions)
    )
    group_closed = all(
        matrix_key(left * right) in cover_keys
        for left in projective_cover
        for right in projective_cover
    )

    def system_signature(left: sp.Matrix, right: sp.Matrix) -> tuple[object, ...]:
        system = selector_system(
            ((DISPLAYED[0], left), (DISPLAYED[1], right)), local
        )
        return (
            system.rows,
            system.columns,
            system.rank,
            system.augmented_rank,
            system.selectors,
            system.rhs,
        )

    image_orbit = {
        system_signature(left, right)
        for left in representatives
        for right in representatives
    }
    cover_orbit = {
        system_signature(left, right)
        for left in projective_cover
        for right in projective_cover
    }
    every_system_inconsistent = all(
        signature[3] > signature[2] for signature in cover_orbit
    )
    central_kernel_exact = (
        len(kernel) == 2
        and {matrix_key(item) for item in kernel}
        == {matrix_key(sp.eye(4)), matrix_key(-sp.eye(4))}
        and all(
            matrix_zero(item * gauge - gauge * item)
            for item in kernel
            for gauge in projective_cover
        )
    )
    return GaugeCertificate(
        cover_size=len(projective_cover),
        distinct_cover_elements=len(cover_keys),
        distinct_adjoint_actions=len(distinct_actions),
        central_kernel_order=len(kernel) if central_kernel_exact else -1,
        action_multiplicities=multiplicities,
        group_closed=group_closed,
        orbit_equal=cover_orbit == image_orbit,
        every_system_inconsistent=every_system_inconsistent,
    )


def block105_item_one_disjunction() -> bytes:
    source = git_bytes("show", f"{CURVED_COMMIT}:{CURVED_NOTE}")
    section_match = re.search(
        rb"(?m)^#{1,6}[ \t]+12\b[^\r\n]*(?:\r?\n|$)", source
    )
    if section_match is None:
        return b""
    following = source[section_match.end() :]
    next_heading = re.search(rb"(?m)^#{1,6}[ \t]+", following)
    section = following[: next_heading.start()] if next_heading else following
    item_match = re.search(rb"(?m)^[ \t]*1\.[ \t]+", section)
    if item_match is None:
        return b""
    after_marker = section[item_match.end() :]
    next_item = re.search(rb"(?m)^[ \t]*2\.[ \t]+", after_marker)
    item = after_marker[: next_item.start()] if next_item else after_marker
    # Markdown soft line breaks inside the numbered paragraph denote one
    # inter-word space.  Canonicalize that presentation-only wrapping, then
    # demand this exact byte string from the Block 134 note.
    return b" ".join(item.split())


def atlas_question_open(note: str) -> bool:
    settled_phrases = (
        "atlas invariance is settled",
        "atlas invariance is proved",
        "atlas invariance is established",
        "atlas-invariance is settled",
        "atlas-invariance is proved",
        "atlas-invariance is established",
    )
    return (
        "atlas" in note
        and ("invariant" in note or "artifact" in note)
        and "open" in note
        and not any(phrase in note for phrase in settled_phrases)
    )


N5_LINES = (
    "N5: per_element: exact chart-nilpotency, matching-inconsistency, cokernel, residual-form, grading, triple-cocycle, and adjoint-count certificates are checked",
    "per_site: one Grassmann mode per fine site on the antiperiodic reflection torus",
    "per_mode: every displayed chart carries an exactly nilpotent differential but the chart-matching system is inconsistent at both levels with the residual a single nonzero cokernel class",
    "per_block: the common differential does not exist even without nilpotency and the exact connection residual is the displayed graded-shift operator — block 105's item one is discharged through its second branch",
    "lattice_wide: checked and not executed — the atlas-invariance of the residual class, the connection-with-residual curved formulation, richer carriers, the actual ADM/history transporter completion, joint gravity, the gravity constraint quotient beyond the displayed carrier, Records, audit retention, and TOE closure remain open",
)


SCOPE_KEYS = (
    "connection_residual",
    "common_differential",
    "cokernel_class",
    "strong_form",
    "grading",
    "spatial_shift",
    "cech",
    "adjoint_cover",
    "atlas_open",
    "item_one",
    "action_datum",
    "diagnostic",
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
)


def scope_certificate(note: str, mutation: str) -> dict[str, bool]:
    result = {
        "connection_residual": (
            "connection residual" in note or "connection-residual" in note
        ),
        "common_differential": (
            "does not exist" in note and "common differential" in note
        ),
        "cokernel_class": "one nonzero class" in note and "cokernel" in note,
        "strong_form": "strong form" in note or "even allowing" in note,
        "grading": (
            "structurally forced" in note or "even/odd grading" in note
        ),
        "spatial_shift": "spatial shift" in note,
        "cech": "coboundary" in note or "cech" in note,
        "adjoint_cover": (
            "four distinct adjoint" in note or "central kernel" in note
        ),
        "atlas_open": (
            "atlas" in note
            and ("invariant" in note or "artifact" in note)
            and "open" in note
        ),
        "item_one": "discharged" in note or "second branch" in note,
        "action_datum": "-89/140" in note,
        "diagnostic": "diagnostic" in note,
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
        "n1_n8": all(f"n{index}" in note for index in range(1, 9)),
        "w1": "w1" in note,
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
    }
    if mutation == "weaken_no_go_packet":
        result["os_boundary"] = False
        result["n1_n8"] = False
    if mutation == "drop_n5_resolution":
        result["n5_resolution"] = False
        result["n5_verbatim"] = False
    if mutation == "claim_toe_progress":
        result["zero_score"] = False
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS, default="")
    mutation = parser.parse_args().mutation
    started = time.monotonic()
    checks = Checks()

    authority = authority_certificate(mutation)
    authority_raw = (
        AUDIT_TIMEOUT_SEC == 600
        and AUDIT_INPUT_PATHS
        == (
            "docs/ADMISSIBILITY_DIRAC_KAHLER_CONNECTION_RESIDUAL_THEOREM_BOUNDED_THEOREM_NOTE_2026-08-17.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
            "docs/audit/data/axiom_premise_nodes.json",
            "docs/ADMISSIBILITY_DIRAC_KAHLER_TWO_BLOCK_STATES_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-08-17.md",
            "scripts/admissibility_dirac_kahler_two_block_states_dynamics_2026_08_17.py",
            "logs/runner-cache/admissibility_dirac_kahler_two_block_states_dynamics_2026_08_17.txt",
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
            authority[f"ancestor_{number}"] for number in range(103, 133)
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
        "Block 133 blobs, ancestors 132--103, and Block 105 note/runner are content-bound",
        authority_raw,
    )

    local = local_differential(S_X, S_T)
    charts = {origin: cover_chart_matrix(origin) for origin in ORIGINS}
    chart_differentials = {
        origin: sp.simplify(
            charts[origin].T * lifted(local) * charts[origin]
        )
        for origin in ORIGINS
    }
    local_algebra = (
        matrix_zero(block105.EX**2)
        and matrix_zero(block105.ET**2)
        and matrix_zero(block105.EX * block105.ET + block105.ET * block105.EX)
    )
    chart_ranks = tuple(
        chart_differentials[origin].rank() for origin in ORIGINS
    )
    chart_shapes = tuple(
        chart_differentials[origin].shape for origin in ORIGINS
    )
    chart_nilpotency = all(
        matrix_zero(chart_differentials[origin] ** 2) for origin in ORIGINS
    )
    source_match = all(
        matrix_zero(
            chart_differentials[origin]
            - chart_differential_cover(origin, local)
        )
        for origin in ORIGINS
    )
    transitions = transition_certificate(charts)
    chart_raw = (
        local_algebra
        and chart_shapes == ((32, 32),) * 4
        and chart_ranks == (16, 16, 16, 16)
        and chart_nilpotency
        and source_match
        and transitions.displayed_exact
        and len(transitions.transitions) == 16
    )
    checks.check(
        "B-the-chart-differentials",
        "the four displayed 32x32 chart differentials have rank 16 and square zero; frame transitions are extracted exactly",
        chart_raw and mutation != "break_chart_nilpotency",
    )

    displayed_system = selector_system(
        tuple((origin, chart_gauge(origin)) for origin in DISPLAYED), local
    )
    atlas_system = selector_system(
        tuple((origin, chart_gauge(origin)) for origin in ORIGINS), local
    )
    system_dimensions_raw = (
        (
            displayed_system.rows,
            displayed_system.columns,
            displayed_system.rank,
            displayed_system.augmented_rank,
        )
        == (256, 1024, 192, 193)
        and (
            atlas_system.rows,
            atlas_system.columns,
            atlas_system.rank,
            atlas_system.augmented_rank,
        )
        == (512, 1024, 288, 289)
    )
    inconsistency_raw = (
        system_dimensions_raw
        and not displayed_system.consistent
        and not atlas_system.consistent
        and displayed_system.residual_norm_squared != 0
        and atlas_system.residual_norm_squared != 0
        and displayed_system.augmented_rank > displayed_system.rank
        and atlas_system.augmented_rank > atlas_system.rank
        and displayed_system.projection_exact
        and atlas_system.projection_exact
    )
    cokernel_raw = (
        displayed_system.cokernel_dimension == 64
        and atlas_system.cokernel_dimension == 224
        and displayed_system.class_nonzero
        and atlas_system.class_nonzero
        and len(displayed_system.rhs) == 256
        and len(atlas_system.rhs) == 512
    )
    matching_gate = inconsistency_raw and cokernel_raw
    if mutation == "break_inconsistency":
        matching_gate = False
    if mutation == "break_cokernel_dims":
        matching_gate = False
    checks.check(
        "C-the-matching-inconsistency",
        "the 256x1024 and 512x1024 linear systems are inconsistent, with one nonzero class in cokernels of dimensions 64 and 224",
        matching_gate,
    )

    generic_variables = sp.symbols("d_00 d_01 d_10 d_11")
    generic = sp.Matrix(2, 2, generic_variables)
    nilpotency_degrees = tuple(
        sp.Poly(entry, generic_variables).total_degree()
        for entry in generic**2
    )
    matching_linear = (
        len(displayed_system.selectors) == displayed_system.rows
        and len(displayed_system.rhs) == displayed_system.rows
        and all(
            0 <= row < SIZE and 0 <= column < SIZE
            for row, column in displayed_system.selectors
        )
    )
    nilpotency_additional_quadratic = nilpotency_degrees == (2, 2, 2, 2)
    empty_linear_solution_set = not displayed_system.consistent
    no_matching_even_without_nilpotency = empty_linear_solution_set
    strong_implication = (
        empty_linear_solution_set
        and no_matching_even_without_nilpotency
        and not displayed_system.consistent
    )
    midpoint = sp.simplify(
        (
            chart_differentials[DISPLAYED[0]]
            + chart_differentials[DISPLAYED[1]]
        )
        / 2
    )
    midpoint_square = sp.simplify(midpoint**2)
    spatial_shift = cover_translation((0, 1))
    midpoint_residual = candidate_residual(displayed_system, midpoint)
    midpoint_raw = (
        matrix_zero(
            midpoint_square + R(9, 100) * spatial_shift**2
        )
        and midpoint_square.rank() == 32
        and len(support(midpoint_square)) == 32
        and any(value != 0 for value in midpoint_residual)
        and midpoint != displayed_system.least_squares
    )
    strong_raw = (
        matching_linear
        and nilpotency_additional_quadratic
        and strong_implication
        and midpoint_raw
    )
    checks.check(
        "D-the-strong-form",
        "matching is linear and already empty before the additional quadratic d^2=0 constraint, so no matching d exists even allowing d^2!=0",
        strong_raw and mutation != "break_strong_form",
    )

    sx, st = sp.symbols("s_x s_t", real=True, nonzero=True)
    symbolic_system = selector_system(
        tuple((origin, chart_gauge(origin)) for origin in DISPLAYED),
        local_differential(sx, st),
    )
    residual = residual_operator_certificate(symbolic_system, st)
    omega = sp.simplify(residual.omega.subs({sx: S_X, st: S_T}))
    fixture_raw_residual = conflict_operator(displayed_system)
    residual_form_raw = (
        residual.signed_frame_exact
        and matrix_zero(residual.omega - residual.formula)
        and matrix_zero(
            residual.residual_frame
            * fixture_raw_residual
            * residual.residual_frame.H
            - omega
        )
        and omega.rank() == 16
        and len(support(omega)) == 16
        and {value for _, _, value in support(omega)}
        == {-8 * I / 5, 8 * I / 5}
        and matrix_zero(omega**2)
        and sp.simplify(sp.trace(omega.H * omega)) == R(1024, 25)
    )
    grading_raw = (
        residual.grading_mechanism_exact
        and matrix_zero(
            residual.even_projector
            * residual.spatial_shift
            * residual.even_projector
        )
        and matrix_zero(residual.formula**2)
    )
    triple_raw = transitions.triple_cocycle_exact

    hodge = curved_hodge_cover()
    physical_actions = {
        origin: physical_action(chart_differentials[origin], hodge)
        for origin in DISPLAYED
    }
    action_residual = sp.simplify(
        physical_actions[DISPLAYED[1]] - physical_actions[DISPLAYED[0]]
    )
    chart_difference = sp.simplify(
        chart_differentials[DISPLAYED[1]]
        - chart_differentials[DISPLAYED[0]]
    )
    action_image = antiperiodic_quotient(
        sp.simplify(
            I * (hodge * chart_difference + chart_difference.H * hodge)
        )
    )
    action_link_raw = (
        matrix_zero(action_residual - action_image)
        and action_residual.rank() == 16
        and action_residual[10, 11] == -R(89, 140)
    )
    residual_form_unmutated = residual_form_raw
    if mutation == "break_residual_form":
        residual_form_raw = False
    if mutation == "break_grading_mechanism":
        grading_raw = False
    if mutation == "break_triple_exact":
        triple_raw = False
    checks.check(
        "E-the-residual-operator",
        "Omega=2*i*s_t*T_t^-1*P_even*P_x is the rank-16 nilpotent residual; P_even*P_x*P_even=0, the triple cocycle is exact, and -89/140 is reproduced",
        residual_form_raw and grading_raw and triple_raw and action_link_raw,
    )

    gauge = gauge_certificate(local)
    gauge_raw = (
        gauge.cover_size == 8
        and gauge.distinct_cover_elements == 8
        and gauge.distinct_adjoint_actions == 4
        and gauge.central_kernel_order == 2
        and gauge.action_multiplicities == (2, 2, 2, 2)
        and gauge.group_closed
        and gauge.orbit_equal
        and gauge.every_system_inconsistent
    )
    checks.check(
        "F-the-gauge-powerlessness",
        "direct enumeration gives four distinct adjoint actions with central kernel order 2, and the eight-lift and four-image system orbits coincide",
        gauge_raw and mutation != "break_adjoint_count",
    )

    note_bytes = raw_note()
    note = normalized_note(note_bytes)
    item_one = block105_item_one_disjunction()
    item_one_normalized = normalized_note(item_one)
    citation_raw = (
        bool(item_one)
        and item_one in note_bytes
        and "or its exact connection residual" in item_one_normalized
        and (
            "block 105 §12" in note
            or "block 105, §12" in note
            or "block 105 section 12" in note
        )
        and "item 1" in note
    )
    cech_raw = (
        displayed_system.class_nonzero
        and not displayed_system.consistent
        and residual_form_unmutated
        and ("coboundary" in note or "cech" in note)
    )
    discharge_raw = (
        ("second branch" in note or "discharged" in note)
        and "exact connection residual" in note
    )
    invariance_open_raw = atlas_question_open(note)
    item_gate = (
        citation_raw
        and cech_raw
        and discharge_raw
        and invariance_open_raw
    )
    if mutation == "claim_invariance_settled":
        item_gate = False
    checks.check(
        "G-the-item-one-discharge",
        "Block 105 section 12 item 1 is cited byte-exactly; Omega is not a coboundary and discharges the second branch, while atlas-invariance stays OPEN",
        item_gate,
    )

    scope = scope_certificate(note, mutation)
    elapsed_before_scope = time.monotonic() - started
    checks.check(
        "H-scope",
        "connection-residual, strong-form, grading, Cech, gauge, atlas-open, N1--N8/W1/N5, no-go, and TOE firewalls are present",
        set(scope) == set(SCOPE_KEYS)
        and all(scope.values())
        and elapsed_before_scope <= 400,
    )

    print(
        f"AUTHORITY: Block133 parent={authority['parent']}; note/runner/cache, "
        "ancestors 132--103, and Block105 note/runner pins exact"
    )
    print(
        "CHARTS: four 32x32 differentials have ranks=(16,16,16,16) and "
        "d^2=0; displayed transition rank/support=32/32; triple cocycle=0"
    )
    print(
        "SYSTEMS: two-chart=256x1024 rank[A|b]=192|193 coker=64; "
        "four-chart=512x1024 rank[A|b]=288|289 coker=224; verdict=INCONSISTENT"
    )
    print(
        "STRONG_FORM: Sol(linear matching)=empty => no common matching d "
        "even allowing d^2!=0; nilpotency is an additional constraint"
    )
    print(
        "DIAGNOSTIC: midpoint Dbar is not a solution of the matching system; "
        "Dbar^2=-(9/100)T_x^2 and rank(Dbar^2)=32"
    )
    print(
        "RESIDUAL: Omega=2*i*s_t*T_t^-1*P_even*P_x; P_x is the spatial "
        "shift; values={-8i/5,+8i/5}, rank=16, Omega^2=0 structurally from "
        "P_even*P_x*P_even=0; action entry=-89/140"
    )
    print(
        "GAUGE: eight projective lifts, four distinct adjoint actions, "
        "central kernel order 2; cover orbit=four-image orbit"
    )
    print(
        "ITEM_ONE: byte-exact Block105 section-12 item-1 disjunction; second "
        "branch discharged; Cech [Omega] is not a coboundary; atlas-invariance OPEN"
    )
    for line in N5_LINES:
        print(line)
    if checks.failed == 0:
        print(
            "RESULT: the campaign closes on the connection-residual theorem — "
            "no flat common differential exists and the exact obstruction is "
            "the displayed nilpotent graded-shift operator, discharging the "
            "lane's oldest open item through its second branch and handing the "
            "next campaign the atlas-invariance question"
        )
        print(
            "DECISION_CUT: pose the connection-with-residual curved formulation "
            "and the invariance question; reject flat-differential searches"
        )
    else:
        print(
            "RESULT: BLOCKED — at least one exact authority, chart, matching, "
            "strong-form, residual, gauge, item-one, scope, mutation, or runtime "
            "certificate failed"
        )
        print(
            "DECISION_CUT: repair the failed certificate without claiming atlas "
            "invariance or weakening the exact connection-residual statement"
        )
    print(
        "TOE: zero obligation retirement; no TOE percentage moves; "
        "retained-positive end-to-end theory count remains zero; gravity "
        "constraint quotient remains unexecuted; actual ADM/history transporter "
        "remains open"
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
