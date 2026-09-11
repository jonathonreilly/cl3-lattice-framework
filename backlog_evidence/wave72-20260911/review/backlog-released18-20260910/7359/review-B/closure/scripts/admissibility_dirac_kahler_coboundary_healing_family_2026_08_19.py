#!/usr/bin/env python3
# Final path: scripts/admissibility_dirac_kahler_coboundary_healing_family_2026_08_19.py
"""Block 141: exact coboundary healing-family theorem on the displayed atlas.

Block 137 recorded that its selector-projected edge dressing heals every edge
of the committed four-chart Block 105 atlas -- (d_i+Omega_ij)**2 = 0 -- while
leaving the forward companion coefficient

    B_i = (quotient action of d_i)[4:8, 0:4]

at rank 3 with kernel span(0,1,0,0) on the displayed pair, and attributed the
miss to the even grading parity of that dressing.  This runner replaces that
attribution with an exact mechanism and an exact positive construction:

  * the rank-3 companion is a property of the two cover-time-ODD chart origins
    (1,0) and (1,1); the two cover-time-EVEN origins (0,0) and (0,1) already
    carry rank-4 companions with explicit determinants;
  * atlas-wide, the Block 137 companion correction is zero on 14 of the 16
    ordered edges -- 12 of them because the selector dressing itself is zero --
    and is nonzero exactly on the two edges joining the cover-time-even charts,
    so the displayed pair is the only genuine miss;
  * grading parity is neither necessary nor sufficient: the grading-EVEN
    Omega* = d_(0,0) - d_(1,0) corrects the read column, while the
    parity-MIXING d_(1,1) - d_(1,0) leaves it identically zero;
  * the coboundary family Omega_ij = (x_j-x_i)*Omega* with x = (0,0,1/2,-1/3)
    keeps all 16 dressed edges square-zero, has 0/64 Cech curvature, and lifts
    the companion to rank 4 on 14 of the 16 ordered edges; and
  * 14/16 is a hard maximum, because zero Cech curvature forces Omega_ii = 0
    and therefore leaves the two cover-time-odd self-edges at rank 3.

Every scientific comparison below is exact SymPy arithmetic at the committed
fixture s_x = 3/5, s_t = 4/5 with a symbolic real mass m; the integer monotonic
clock is used only for the runtime gate.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
import re
import subprocess
import sys
import time

import sympy as sp


R = sp.Rational
MASS = sp.symbols("m", real=True)
SX, ST = sp.symbols("s_x s_t", real=True)

_FINAL_LOCATION_ROOT = Path(__file__).resolve().parents[1]
# This fallback keeps the scratchpad draft executable before it is moved to
# scripts/, where the final-location branch is used.
ROOT = (
    _FINAL_LOCATION_ROOT
    if (_FINAL_LOCATION_ROOT / ".git").exists()
    else Path.cwd()
)
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import admissibility_dirac_kahler_twisted_scouting_record_2026_08_19 as b137
import admissibility_dirac_kahler_connection_residual_theorem_2026_08_17 as b134


NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_DIRAC_KAHLER_COBOUNDARY_HEALING_FAMILY_"
    "BOUNDED_THEOREM_NOTE_2026-08-19.md"
)
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"
BLOCK140_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_ISOSPECTRAL_SIMILARITY_THEOREM_"
    "BOUNDED_THEOREM_NOTE_2026-08-19.md"
)
BLOCK140_RUNNER = (
    "scripts/admissibility_dirac_kahler_isospectral_similarity_theorem_"
    "2026_08_19.py"
)
BLOCK140_CACHE = (
    "logs/runner-cache/admissibility_dirac_kahler_isospectral_similarity_"
    "theorem_2026_08_19.txt"
)
BLOCK137_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_TWISTED_SCOUTING_RECORD_"
    "BOUNDED_THEOREM_NOTE_2026-08-19.md"
)
BLOCK137_RUNNER = (
    "scripts/admissibility_dirac_kahler_twisted_scouting_record_2026_08_19.py"
)
BLOCK134_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_CONNECTION_RESIDUAL_THEOREM_"
    "BOUNDED_THEOREM_NOTE_2026-08-17.md"
)
BLOCK134_RUNNER = (
    "scripts/admissibility_dirac_kahler_connection_residual_theorem_"
    "2026_08_17.py"
)
PARENT_ARTIFACTS = (
    BLOCK140_NOTE,
    BLOCK140_RUNNER,
    BLOCK140_CACHE,
    BLOCK137_NOTE,
    BLOCK137_RUNNER,
    BLOCK134_NOTE,
    BLOCK134_RUNNER,
)

# Deliberately literal: this is the complete audit read surface.
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_COBOUNDARY_HEALING_FAMILY_BOUNDED_THEOREM_NOTE_2026-08-19.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_ISOSPECTRAL_SIMILARITY_THEOREM_BOUNDED_THEOREM_NOTE_2026-08-19.md",
    "scripts/admissibility_dirac_kahler_isospectral_similarity_theorem_2026_08_19.py",
    "logs/runner-cache/admissibility_dirac_kahler_isospectral_similarity_theorem_2026_08_19.txt",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_TWISTED_SCOUTING_RECORD_BOUNDED_THEOREM_NOTE_2026-08-19.md",
    "scripts/admissibility_dirac_kahler_twisted_scouting_record_2026_08_19.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_CONNECTION_RESIDUAL_THEOREM_BOUNDED_THEOREM_NOTE_2026-08-17.md",
    "scripts/admissibility_dirac_kahler_connection_residual_theorem_2026_08_17.py",
)

AUDIT_TIMEOUT_SEC = 600
CURRENT_MAIN = "29d17653c9c043a74041f070e311f03fce114c0a"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
CURRENT_REGISTRY_BLOB = "b93959cca4f7e26c673cdccbe601e50c3cb93daa"
WORKTREE_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
WORKTREE_REGISTRY_BLOB = "f01d3be864f682584d50eede8b3abe6671bb4719"
PARENT_REF = (
    "origin/physics-loop/"
    "toe-axiom-closure-block140-isospectral-similarity-20260819"
)
# Landing supervisor: replace this placeholder with the Block 140 branch tip.
# Until it is a 40-hex commit the pin is resolved through PARENT_REF, which is
# a real and verifiable binding; the immutable commit pin lands with the block.
PARENT_COMMIT = "23ad6d38be6a39d1f4d1821961318a60fc9e10b2"
# Block 139's tip: a real ancestor that predates the Block 140 artifacts and is
# therefore the honest "stale pin" control for the authority mutation.
STALE_PARENT_COMMIT = "23ad6d38be6a39d1f4d1821961318a60fc9e10b2"
# Block 137's recorded main: a real but superseded authority head.
STALE_MAIN = "2dc8dd9b2778a01454874d19b262569ae19ebc6e"

MUTATIONS = (
    "stale_main_authority",
    "stale_parent_authority",
    "break_even_chart_determinant",
    "break_odd_chart_kernel",
    "break_selector_edge_count",
    "break_selector_correction_value",
    "assert_parity_necessity",
    "break_cover_time_support",
    "break_edge_square_count",
    "claim_twentyfour_of_sixtyfour",
    "break_healed_determinant",
    "break_cocycle_system_rank",
    "drop_self_edge_forcing",
    "claim_in_class_dressing",
    "drop_n5_fence",
)

MUTATION_GATE = {
    "stale_main_authority": "A",
    "stale_parent_authority": "A",
    "break_even_chart_determinant": "B",
    "break_odd_chart_kernel": "B",
    "break_selector_edge_count": "C",
    "break_selector_correction_value": "C",
    "assert_parity_necessity": "D",
    "break_cover_time_support": "D",
    "break_edge_square_count": "E",
    "claim_twentyfour_of_sixtyfour": "E",
    "break_healed_determinant": "E",
    "break_cocycle_system_rank": "F",
    "drop_self_edge_forcing": "F",
    "claim_in_class_dressing": "G",
    "drop_n5_fence": "H",
}


class Checks:
    def __init__(self) -> None:
        self.results: list[tuple[str, str, bool]] = []

    def check(self, key: str, statement: str, condition: object) -> None:
        self.results.append((key, statement, bool(condition)))

    def report(self) -> None:
        for key, statement, value in self.results:
            print(f"[{'PASS' if value else 'FAIL'}] {key}: {statement}")
        print(
            "GATES "
            + " ".join(
                f"{key}={'PASS' if value else 'FAIL'}"
                for key, _, value in self.results
            )
        )

    def finish(self) -> int:
        passed = sum(value for _, _, value in self.results)
        failed = len(self.results) - passed
        print(f"TOTAL: PASS={passed} FAIL={failed}")
        return failed


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
    """The blob at a path in a commit, or "" when the path is absent there.

    Absence is a real answer here: the stale-pin control deliberately probes a
    commit that predates some of the pinned artifacts.
    """
    result = subprocess.run(
        ("git", "rev-parse", f"{commit}:{path}"),
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
        timeout=AUDIT_TIMEOUT_SEC,
    )
    return result.stdout.strip() if result.returncode == 0 else ""


def is_ancestor(ancestor: str, descendant: str) -> bool:
    return subprocess.run(
        ("git", "merge-base", "--is-ancestor", ancestor, descendant),
        cwd=ROOT,
        check=False,
        timeout=AUDIT_TIMEOUT_SEC,
    ).returncode == 0


def is_hash(value: str) -> bool:
    return re.fullmatch(r"[0-9a-f]{40}", value) is not None


def raw_note() -> str:
    try:
        return NOTE_PATH.read_text(encoding="utf-8")
    except OSError:
        return ""


def normalized_note(text: str) -> str:
    return " ".join(text.lower().split())


def no_float(value: object) -> bool:
    if isinstance(value, sp.MatrixBase):
        return not value.has(sp.Float)
    if isinstance(value, (tuple, list, set, frozenset)):
        return all(no_float(item) for item in value)
    if isinstance(value, dict):
        return all(
            no_float(key) and no_float(item) for key, item in value.items()
        )
    return not sp.sympify(value).has(sp.Float)


def canonical(value: sp.Expr) -> sp.Expr:
    return sp.cancel(sp.expand(value))


def zero(matrix: sp.MatrixBase) -> bool:
    return b134.matrix_zero(matrix)


# ---------------------------------------------------------------------------
# A. authority
# ---------------------------------------------------------------------------
@dataclass(frozen=True)
class AuthorityCertificate:
    fixed_authority: bool
    parent_pin_is_commit: bool
    parent_ref_and_ancestry: bool
    parent_artifact_blobs: bool
    stale_parent_artifact_blobs: bool


def resolved_parent_commit() -> str:
    return PARENT_COMMIT if is_hash(PARENT_COMMIT) else git_output(
        "rev-parse", PARENT_REF
    )


def authority_certificate(main_head: str) -> AuthorityCertificate:
    fixed_authority = bool(
        AUDIT_TIMEOUT_SEC == 600
        and main_head == CURRENT_MAIN
        and commit_blob("origin/main", AXIOM_PATH) == CURRENT_AXIOM_BLOB
        and commit_blob("origin/main", REGISTRY_PATH) == CURRENT_REGISTRY_BLOB
        and worktree_blob(AXIOM_PATH) == WORKTREE_AXIOM_BLOB
        and worktree_blob(REGISTRY_PATH) == WORKTREE_REGISTRY_BLOB
    )

    parent = resolved_parent_commit()
    worktree_blobs = tuple(worktree_blob(path) for path in PARENT_ARTIFACTS)
    committed_blobs = tuple(
        commit_blob(parent, path) for path in PARENT_ARTIFACTS
    )
    stale_blobs = tuple(
        commit_blob(STALE_PARENT_COMMIT, path) for path in PARENT_ARTIFACTS
    )
    return AuthorityCertificate(
        fixed_authority,
        is_hash(PARENT_COMMIT),
        bool(
            is_hash(parent)
            and is_ancestor(parent, "HEAD")
            and (
                not is_hash(PARENT_COMMIT)
                or git_output("rev-parse", PARENT_REF) == PARENT_COMMIT
            )
        ),
        bool(
            len(committed_blobs) == 7
            and all(is_hash(value) for value in committed_blobs)
            and committed_blobs == worktree_blobs
        ),
        bool(
            len(stale_blobs) == 7
            and all(is_hash(value) for value in stale_blobs)
            and stale_blobs == worktree_blobs
        ),
    )


# ---------------------------------------------------------------------------
# atlas machinery, imported wholesale from the committed Blocks 137 and 134
# ---------------------------------------------------------------------------
SIZE = b134.SIZE
ORIGINS = b134.ORIGINS
DISPLAYED = b134.DISPLAYED
INDEX = {origin: position for position, origin in enumerate(ORIGINS)}
KERNEL_DIRECTION = sp.Matrix([0, 1, 0, 0])
GRADING = sp.diag(*((-1) ** (position % 4) for position in range(SIZE)))
EVEN_PROJECTOR = sp.expand((sp.eye(SIZE) + GRADING) / 2)
ODD_PROJECTOR = sp.expand(sp.eye(SIZE) - EVEN_PROJECTOR)
COVER_TIME_EVEN = tuple(origin for origin in ORIGINS if origin[0] % 2 == 0)
COVER_TIME_ODD = tuple(origin for origin in ORIGINS if origin[0] % 2 == 1)
HEALING_WEIGHTS = (sp.Integer(0), sp.Integer(0), R(1, 2), R(-1, 3))

DETERMINANT_EVEN_ORIGIN = -R(1303) * (
    718239375 * MASS**2 - 253923671672
) / 689509800000000
DETERMINANT_SHIFTED_ORIGIN = R(4728571336637, 7182393750000)
HEALED_DISPLAYED_DETERMINANT = R(1303) * (
    9049816125 * MASS**2 + 2180604558616
) / 10425388176000000
SELECTOR_CORRECTION_SCALE = R(1303, 750)
STAR_CORRECTION_SCALE = R(1303, 1500)
SYMBOLIC_CORRECTION_SCALE = R(1303, 1200)
SELECTOR_TIME_BLOCK_SUPPORT = ((1, 2), (3, 4), (5, 6), (7, 0))
SELECTOR_CORRECTION_BLOCK_SUPPORT = (
    (0, 0),
    (0, 2),
    (0, 3),
    (1, 2),
    (2, 0),
    (2, 1),
    (2, 2),
    (3, 0),
)
READ_WINDOW_BLOCK = (1, 0)


def companion(differential: sp.Matrix, hodge: sp.Matrix) -> sp.Matrix:
    """The forward (t=1,t=0) 4x4 block of the quotient action of d."""
    return sp.expand(
        b137.quotient_action(differential, hodge, MASS)[4:8, 0:4]
    )


def correction_block(dressing: sp.Matrix, hodge: sp.Matrix) -> sp.Matrix:
    return sp.expand(b137.quotient_correction(dressing, hodge))


def companion_correction(dressing: sp.Matrix, hodge: sp.Matrix) -> sp.Matrix:
    return correction_block(dressing, hodge)[4:8, 0:4]


def read_column(dressing: sp.Matrix, hodge: sp.Matrix) -> sp.Matrix:
    return sp.expand(companion_correction(dressing, hodge) * KERNEL_DIRECTION)


def parity_kind(matrix: sp.Matrix) -> str:
    if zero(sp.expand(GRADING * matrix * GRADING - matrix)):
        return "even"
    if zero(sp.expand(GRADING * matrix * GRADING + matrix)):
        return "odd"
    return "mixed"


def parity_mixing(matrix: sp.Matrix) -> bool:
    return not zero(sp.expand(EVEN_PROJECTOR * matrix * ODD_PROJECTOR)) or (
        not zero(sp.expand(ODD_PROJECTOR * matrix * EVEN_PROJECTOR))
    )


def block_support(matrix: sp.MatrixBase) -> tuple[tuple[int, int], ...]:
    return tuple(
        sorted({(row // 4, column // 4) for row, column, _ in b134.support(matrix)})
    )


# ---------------------------------------------------------------------------
# measured facts (computed once, before any mutation flag is consulted)
# ---------------------------------------------------------------------------
@dataclass(frozen=True)
class Facts:
    main_head: str
    authority: AuthorityCertificate
    chart_ranks: dict
    chart_determinants: dict
    chart_kernels: dict
    rank_four_origins: tuple
    selector_zero_edges: tuple
    selector_live_edges: tuple
    selector_correction_edges: tuple
    selector_correction_values: dict
    star_parity: str
    star_parity_blocks_vanish: bool
    star_read_column: sp.Matrix
    star_healed_rank: int
    mixed_parity: str
    mixed_is_parity_mixing: bool
    mixed_read_column: sp.Matrix
    mixed_healed_rank: int
    selector_time_blocks: tuple
    selector_correction_blocks: tuple
    edge_square_zero_count: int
    dressed_edge_rank16_count: int
    curvature_nonzero_triples: int
    companion_rank_four_count: int
    rank_three_leftovers: tuple
    genuine_correction_count: int
    healed_displayed_determinant: sp.Expr
    healed_determinant_real_roots: tuple
    cocycle_system_shape: tuple
    cocycle_system_rank: int
    cocycle_solution_dimension: int
    potential_reproduces_every_solution: bool
    self_edges_forced_zero: bool
    odd_self_edge_ranks: tuple
    mask_violation_count: int
    selector_mask_size: int
    projection_is_not_star: bool
    symbolic_read_column: sp.Matrix
    symbolic_read_column_degree: int
    symbolic_read_column_free_symbols: frozenset
    exact_no_float: bool
    scope: dict


def measure() -> Facts:
    main_head = git_output("rev-parse", "origin/main")
    authority = authority_certificate(main_head)

    fixture = b137.connection_data(b134.S_X, b134.S_T)
    symbolic = b137.connection_data(SX, ST)
    differentials = fixture["d"]
    hodge = b134.curved_hodge_cover()

    # --- B: the per-chart companion anchor --------------------------------
    chart_companions = {
        origin: companion(differentials[origin], hodge) for origin in ORIGINS
    }
    chart_ranks = {
        origin: chart_companions[origin].rank() for origin in ORIGINS
    }
    chart_determinants = {
        origin: sp.factor(chart_companions[origin].det()) for origin in ORIGINS
    }
    chart_kernels = {
        origin: tuple(chart_companions[origin].nullspace())
        for origin in ORIGINS
    }
    rank_four_origins = tuple(
        origin for origin in ORIGINS if chart_ranks[origin] == 4
    )

    # --- C: the Block 137 selector dressing, edge by edge ------------------
    selector = {
        (left, right): b137.pair_data(fixture, left, right)[1]
        for left in ORIGINS
        for right in ORIGINS
    }
    selector_zero_edges = tuple(
        sorted(
            (INDEX[left], INDEX[right])
            for left in ORIGINS
            for right in ORIGINS
            if zero(selector[(left, right)])
        )
    )
    selector_live_edges = tuple(
        sorted(
            (INDEX[left], INDEX[right])
            for left in ORIGINS
            for right in ORIGINS
            if not zero(selector[(left, right)])
        )
    )
    selector_correction_values = {}
    for left in ORIGINS:
        for right in ORIGINS:
            column = read_column(selector[(left, right)], hodge)
            if not zero(column):
                selector_correction_values[(INDEX[left], INDEX[right])] = (
                    sp.Matrix(column)
                )
    selector_correction_edges = tuple(sorted(selector_correction_values))

    # --- D: the mechanism witnesses ---------------------------------------
    star = sp.expand(
        differentials[(0, 0)] - differentials[(1, 0)]
    )  # grading-EVEN generator
    mixed = sp.expand(
        differentials[(1, 1)] - differentials[(1, 0)]
    )  # parity-MIXING control
    displayed_first, displayed_second = DISPLAYED
    star_read = read_column(star, hodge)
    mixed_read = read_column(mixed, hodge)
    star_healed_rank = companion(
        sp.expand(differentials[displayed_first] + star), hodge
    ).rank()
    mixed_healed_rank = companion(
        sp.expand(differentials[displayed_first] + mixed), hodge
    ).rank()
    displayed_selector = selector[DISPLAYED]
    selector_time_blocks = block_support(displayed_selector)
    selector_correction_blocks = block_support(
        correction_block(displayed_selector, hodge)
    )

    # --- E: the coboundary healing family ---------------------------------
    weights = {
        origin: HEALING_WEIGHTS[INDEX[origin]] for origin in ORIGINS
    }
    family = {
        (left, right): sp.expand(
            (weights[right] - weights[left]) * star
        )
        for left in ORIGINS
        for right in ORIGINS
    }
    edge_square_zero_count = 0
    dressed_edge_rank16_count = 0
    companion_rank_four_count = 0
    rank_three_leftovers = []
    genuine_correction_count = 0
    for left in ORIGINS:
        for right in ORIGINS:
            dressed = sp.expand(differentials[left] + family[(left, right)])
            if zero(sp.expand(dressed**2)):
                edge_square_zero_count += 1
            if dressed.rank() == 16:
                dressed_edge_rank16_count += 1
            if companion(dressed, hodge).rank() == 4:
                companion_rank_four_count += 1
            else:
                rank_three_leftovers.append((INDEX[left], INDEX[right]))
            if left != right and not zero(
                read_column(family[(left, right)], hodge)
            ):
                genuine_correction_count += 1
    curvature_nonzero_triples = 0
    for left in ORIGINS:
        for middle in ORIGINS:
            for right in ORIGINS:
                if not zero(
                    sp.expand(
                        family[(left, right)]
                        - family[(middle, right)]
                        - family[(left, middle)]
                    )
                ):
                    curvature_nonzero_triples += 1
    healed_displayed = companion(
        sp.expand(differentials[displayed_first] + family[DISPLAYED]), hodge
    )
    healed_displayed_determinant = sp.factor(healed_displayed.det())
    healed_determinant_real_roots = tuple(
        sp.solve(sp.Eq(healed_displayed_determinant, 0), MASS)
    )

    # --- F: the cocycle converse ------------------------------------------
    pairs = tuple((left, right) for left in range(4) for right in range(4))
    pair_index = {pair: position for position, pair in enumerate(pairs)}
    rows = []
    for left in range(4):
        for middle in range(4):
            for right in range(4):
                row = [sp.Integer(0)] * 16
                row[pair_index[(left, right)]] += 1
                row[pair_index[(middle, right)]] -= 1
                row[pair_index[(left, middle)]] -= 1
                rows.append(row)
    cocycle_system = sp.Matrix(rows)
    cocycle_solutions = cocycle_system.nullspace()
    potential_reproduces_every_solution = all(
        sp.simplify(
            solution[pair_index[(left, right)]]
            - (
                solution[pair_index[(0, right)]]
                - solution[pair_index[(0, left)]]
            )
        )
        == 0
        for solution in cocycle_solutions
        for left in range(4)
        for right in range(4)
    )
    self_edges_forced_zero = all(
        sp.simplify(solution[pair_index[(index, index)]]) == 0
        for solution in cocycle_solutions
        for index in range(4)
    )
    odd_self_edge_ranks = tuple(
        chart_ranks[origin] for origin in COVER_TIME_ODD
    )

    # --- G: out-of-class membership and the s_t rider ----------------------
    full_difference = sp.expand(
        differentials[displayed_second] - differentials[displayed_first]
    )
    mask = b137.selector_mask(displayed_first, displayed_second)
    mask_violation_count = sum(
        1
        for row in range(SIZE)
        for column in range(SIZE)
        if sp.simplify(star[row, column]) != 0
        and sp.simplify(star[row, column] - full_difference[row, column]) != 0
    )
    projection_is_not_star = not zero(
        sp.expand(b137.project(full_difference, mask) - star)
    )
    symbolic_star = sp.expand(
        symbolic["d"][(0, 0)] - symbolic["d"][(1, 0)]
    )
    symbolic_read = read_column(symbolic_star, hodge)
    symbolic_read_degree = max(
        sp.Poly(sp.expand(entry), ST).total_degree()
        for entry in symbolic_read
    )
    symbolic_read_free = frozenset().union(
        *(sp.expand(entry).free_symbols for entry in symbolic_read)
    )

    exact_no_float = no_float(
        (
            tuple(chart_companions.values()),
            tuple(chart_determinants.values()),
            tuple(selector.values()),
            tuple(selector_correction_values.values()),
            tuple(family.values()),
            star,
            mixed,
            star_read,
            mixed_read,
            healed_displayed_determinant,
            symbolic_star,
            symbolic_read,
            cocycle_system,
        )
    )

    return Facts(
        main_head=main_head,
        authority=authority,
        chart_ranks=chart_ranks,
        chart_determinants=chart_determinants,
        chart_kernels=chart_kernels,
        rank_four_origins=rank_four_origins,
        selector_zero_edges=selector_zero_edges,
        selector_live_edges=selector_live_edges,
        selector_correction_edges=selector_correction_edges,
        selector_correction_values=selector_correction_values,
        star_parity=parity_kind(star),
        star_parity_blocks_vanish=(
            zero(sp.expand(EVEN_PROJECTOR * star * ODD_PROJECTOR))
            and zero(sp.expand(ODD_PROJECTOR * star * EVEN_PROJECTOR))
        ),
        star_read_column=sp.Matrix(star_read),
        star_healed_rank=star_healed_rank,
        mixed_parity=parity_kind(mixed),
        mixed_is_parity_mixing=parity_mixing(mixed),
        mixed_read_column=sp.Matrix(mixed_read),
        mixed_healed_rank=mixed_healed_rank,
        selector_time_blocks=selector_time_blocks,
        selector_correction_blocks=selector_correction_blocks,
        edge_square_zero_count=edge_square_zero_count,
        dressed_edge_rank16_count=dressed_edge_rank16_count,
        curvature_nonzero_triples=curvature_nonzero_triples,
        companion_rank_four_count=companion_rank_four_count,
        rank_three_leftovers=tuple(rank_three_leftovers),
        genuine_correction_count=genuine_correction_count,
        healed_displayed_determinant=healed_displayed_determinant,
        healed_determinant_real_roots=healed_determinant_real_roots,
        cocycle_system_shape=tuple(cocycle_system.shape),
        cocycle_system_rank=cocycle_system.rank(),
        cocycle_solution_dimension=len(cocycle_solutions),
        potential_reproduces_every_solution=(
            potential_reproduces_every_solution
        ),
        self_edges_forced_zero=self_edges_forced_zero,
        odd_self_edge_ranks=odd_self_edge_ranks,
        mask_violation_count=mask_violation_count,
        selector_mask_size=len(mask),
        projection_is_not_star=projection_is_not_star,
        symbolic_read_column=sp.Matrix(symbolic_read),
        symbolic_read_column_degree=symbolic_read_degree,
        symbolic_read_column_free_symbols=symbolic_read_free,
        exact_no_float=exact_no_float,
        scope=scope_certificate(raw_note()),
    )


# ---------------------------------------------------------------------------
# H. note scope
# ---------------------------------------------------------------------------
N5_FENCE = "N5: per_element: the uncorrected companion B_i=quotient_action(d_i)[4:8,0:4] is rank 4 on the two cover-time-EVEN charts, det_(0,0)=-1303(718239375 m^2-253923671672)/689509800000000 and det_(0,1)=4728571336637/7182393750000, and rank 3 with kernel span(0,1,0,0) and det 0 on the two cover-time-ODD charts\nper_site: atlas-wide the selector dressing's companion correction is zero on 14/16 ordered edges -- 12 trivially because Omega itself vanishes there, plus the displayed (1,0)<->(1,1) pair as the only genuine miss -- and nonzero exactly on (0,0)->(0,1) and (0,1)->(0,0) with values (0,-+1303/750,0,0); Block 137's landed W1 stands, its gate having been displayed-edge-only and symbolic in m\nper_mode: the mechanism is cover-time support, not parity: the grading-even Omega*=d_(0,0)-d_(1,0) corrects by (0,1303/1500,0,0) and heals to rank 4, the parity-mixing d_(1,1)-d_(1,0) leaves the read column identically zero at rank 3, and the displayed backward-hop selector with time-block support {(1,2),(3,4),(5,6),(7,0)} omits exactly the (1,0) read window\nper_block: Omega_ij=(x_j-x_i)Omega* with x=(0,0,1/2,-1/3) gives (d_i+Omega_ij)^2=0 on all 16 edges, atlas curvature 0/64 (down from 24/64), companion rank 4 on 14/16 ordered edges, and displayed-edge det 1303(9049816125 m^2+2180604558616)/10425388176000000 positive for all real m\nlattice_wide: on the full four-chart nerve C_ijk=0 on all 64 triples is a rank-13 system with three-dimensional solution space Omega_ij=c_j-c_i, the i=j triples force Omega_ii=0, and the two cover-time-odd self-edges then stay rank 3, so 14/16 is the exact maximum and the family is optimal\nRESULT: on the displayed atlas and fixtures a coboundary dressing family heals every genuine edge companion with exact edge nilpotency and zero atlas curvature, lies outside Block 137's transition-derived class, and is s_t-only and linear in s_t\nDECISION_CUT: test reflection positivity of the healed action; decide the two forced self-edges; decide the admissibility class of coboundary dressings; execute the joint-lane program; curved OS is not claimed\nTOE: zero axiom retirement; zero obligation retirement; zero TOE movement; no TOE percentage moves; retained-positive end-to-end theory count remains zero"


SCOPE_KEYS = (
    "chart_anchor_ranks",
    "chart_anchor_cover_time",
    "anchor_correction_displayed_only",
    "anchor_correction_mass_identity",
    "anchor_correction_cover_time_support",
    "parity_neither_necessary_nor_sufficient",
    "healing_family_zero_curvature",
    "healing_family_fourteen_of_sixteen",
    "healing_family_ten_genuine_edges",
    "healing_family_determinant",
    "converse_base_chart_potential",
    "converse_hard_maximum",
    "converse_system_rank",
    "out_of_class",
    "st_linear_rider",
    "independence_disclosure",
    "os_no_go",
    "curved_os_no_go",
    "axiom",
    "firewalls",
    "zero_retirement",
    "zero_score",
    "zero_e2e",
    "gravity_quotient",
    "adm",
    "n1_n8",
    "w1",
    "n5_verbatim",
)


def scope_certificate(note_text: str) -> dict[str, bool]:
    note = normalized_note(note_text)
    return {
        "chart_anchor_ranks": "rank 4" in note and "rank 3" in note,
        "chart_anchor_cover_time": (
            "cover-time-even" in note and "cover-time-odd" in note
        ),
        "anchor_correction_displayed_only": "displayed-edge-only" in note,
        "anchor_correction_mass_identity": (
            "identically in the symbolic mass" in note
        ),
        "anchor_correction_cover_time_support": "cover-time support" in note,
        "parity_neither_necessary_nor_sufficient": (
            "neither necessary nor sufficient" in note
        ),
        "healing_family_zero_curvature": (
            "0/64" in note or "0 of 64" in note
        ),
        "healing_family_fourteen_of_sixteen": (
            "14/16" in note or "14 of 16" in note
        ),
        "healing_family_ten_genuine_edges": (
            "10 of the 12 genuine edges" in note
        ),
        "healing_family_determinant": "10425388176000000" in note,
        "converse_base_chart_potential": "base-chart potential" in note,
        "converse_hard_maximum": "hard maximum" in note,
        "converse_system_rank": "rank 13" in note,
        "out_of_class": "not any coordinate mask" in note,
        "st_linear_rider": "linear in s_t" in note,
        "independence_disclosure": "cross-context" in note,
        "os_no_go": "not an os no-go" in note,
        "curved_os_no_go": "not a curved os no-go" in note,
        "axiom": "no axiom amendment is justified" in note,
        "firewalls": "firewall" in note,
        "zero_retirement": "zero obligation retirement" in note,
        "zero_score": (
            "no toe percentage moves" in note
            or "no toe percentage movement" in note
        ),
        "zero_e2e": (
            "retained-positive end-to-end theory count remains zero" in note
        ),
        "gravity_quotient": (
            "gravity constraint quotient remains unexecuted" in note
        ),
        "adm": "actual adm/history transporter remains" in note,
        "n1_n8": all(
            re.search(rf"\bn{index}\b", note) is not None
            for index in range(1, 9)
        ),
        "w1": re.search(r"\bw1\b", note) is not None,
        # Raw substring membership makes the printed eight-line fence
        # byte-identical to its note occurrence.
        "n5_verbatim": N5_FENCE in note_text,
    }


# ---------------------------------------------------------------------------
# claims: the only thing a mutation is allowed to touch
# ---------------------------------------------------------------------------
def build_claims(mutation: str) -> dict[str, object]:
    claims: dict[str, object] = {
        "main_head": CURRENT_MAIN,
        "parent_pin": "resolved",
        "even_chart_determinants": (
            DETERMINANT_EVEN_ORIGIN,
            DETERMINANT_SHIFTED_ORIGIN,
        ),
        "odd_chart_kernel": KERNEL_DIRECTION,
        "selector_correction_edge_count": 2,
        "selector_correction_scale": SELECTOR_CORRECTION_SCALE,
        "parity_is_necessary": False,
        "selector_time_block_support": SELECTOR_TIME_BLOCK_SUPPORT,
        "edge_square_zero_count": 16,
        "curvature_nonzero_triples": 0,
        "healed_displayed_determinant": HEALED_DISPLAYED_DETERMINANT,
        "cocycle_system_rank": 13,
        "self_edges_forced_zero": True,
        "mask_violation_count": 32,
        "required_scope_keys": SCOPE_KEYS,
    }
    if mutation == "stale_main_authority":
        claims["main_head"] = STALE_MAIN
    elif mutation == "stale_parent_authority":
        claims["parent_pin"] = "stale"
    elif mutation == "break_even_chart_determinant":
        claims["even_chart_determinants"] = (
            -R(1303) * (718239375 * MASS**2 - 253923671671) / 689509800000000,
            DETERMINANT_SHIFTED_ORIGIN,
        )
    elif mutation == "break_odd_chart_kernel":
        claims["odd_chart_kernel"] = sp.Matrix([1, 0, 0, 0])
    elif mutation == "break_selector_edge_count":
        claims["selector_correction_edge_count"] = 4
    elif mutation == "break_selector_correction_value":
        claims["selector_correction_scale"] = R(1303, 751)
    elif mutation == "assert_parity_necessity":
        claims["parity_is_necessary"] = True
    elif mutation == "break_cover_time_support":
        claims["selector_time_block_support"] = ((1, 2), (3, 4), (5, 6), (7, 1))
    elif mutation == "break_edge_square_count":
        claims["edge_square_zero_count"] = 15
    elif mutation == "claim_twentyfour_of_sixtyfour":
        claims["curvature_nonzero_triples"] = 24
    elif mutation == "break_healed_determinant":
        claims["healed_displayed_determinant"] = R(1303) * (
            9049816125 * MASS**2 + 2180604558615
        ) / 10425388176000000
    elif mutation == "break_cocycle_system_rank":
        claims["cocycle_system_rank"] = 14
    elif mutation == "drop_self_edge_forcing":
        claims["self_edges_forced_zero"] = False
    elif mutation == "claim_in_class_dressing":
        claims["mask_violation_count"] = 0
    elif mutation == "drop_n5_fence":
        claims["required_scope_keys"] = tuple(
            key for key in SCOPE_KEYS if key != "n5_verbatim"
        )
    return claims


# ---------------------------------------------------------------------------
# gates: pure functions of the measured facts and the claims
# ---------------------------------------------------------------------------
def evaluate_gates(
    facts: Facts, claims: dict[str, object], elapsed_ns: int
) -> dict[str, bool]:
    authority = facts.authority
    parent_blobs_ok = (
        authority.parent_artifact_blobs
        if claims["parent_pin"] == "resolved"
        else authority.stale_parent_artifact_blobs
    )
    gate_a = bool(
        AUDIT_INPUT_PATHS
        == (
            "docs/ADMISSIBILITY_DIRAC_KAHLER_COBOUNDARY_HEALING_FAMILY_BOUNDED_THEOREM_NOTE_2026-08-19.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
            "docs/audit/data/axiom_premise_nodes.json",
            "docs/ADMISSIBILITY_DIRAC_KAHLER_ISOSPECTRAL_SIMILARITY_THEOREM_BOUNDED_THEOREM_NOTE_2026-08-19.md",
            "scripts/admissibility_dirac_kahler_isospectral_similarity_theorem_2026_08_19.py",
            "logs/runner-cache/admissibility_dirac_kahler_isospectral_similarity_theorem_2026_08_19.txt",
            "docs/ADMISSIBILITY_DIRAC_KAHLER_TWISTED_SCOUTING_RECORD_BOUNDED_THEOREM_NOTE_2026-08-19.md",
            "scripts/admissibility_dirac_kahler_twisted_scouting_record_2026_08_19.py",
            "docs/ADMISSIBILITY_DIRAC_KAHLER_CONNECTION_RESIDUAL_THEOREM_BOUNDED_THEOREM_NOTE_2026-08-17.md",
            "scripts/admissibility_dirac_kahler_connection_residual_theorem_2026_08_17.py",
        )
        and PARENT_ARTIFACTS
        == (
            BLOCK140_NOTE,
            BLOCK140_RUNNER,
            BLOCK140_CACHE,
            BLOCK137_NOTE,
            BLOCK137_RUNNER,
            BLOCK134_NOTE,
            BLOCK134_RUNNER,
        )
        and facts.main_head == claims["main_head"]
        and authority.fixed_authority
        and authority.parent_ref_and_ancestry
        and parent_blobs_ok
    )

    even_determinants = claims["even_chart_determinants"]
    gate_b = bool(
        facts.chart_ranks
        == {(0, 0): 4, (0, 1): 4, (1, 0): 3, (1, 1): 3}
        and facts.rank_four_origins == COVER_TIME_EVEN
        and canonical(
            facts.chart_determinants[(0, 0)] - even_determinants[0]
        )
        == 0
        and canonical(
            facts.chart_determinants[(0, 1)] - even_determinants[1]
        )
        == 0
        and facts.chart_determinants[(1, 0)] == 0
        and facts.chart_determinants[(1, 1)] == 0
        and facts.chart_kernels[(0, 0)] == ()
        and facts.chart_kernels[(0, 1)] == ()
        and facts.chart_kernels[(1, 0)] == (claims["odd_chart_kernel"],)
        and facts.chart_kernels[(1, 1)] == (claims["odd_chart_kernel"],)
        and COVER_TIME_ODD == ((1, 0), (1, 1))
        and facts.exact_no_float
    )

    scale = claims["selector_correction_scale"]
    gate_c = bool(
        len(facts.selector_zero_edges) == 12
        and facts.selector_live_edges
        == ((0, 1), (1, 0), (2, 3), (3, 2))
        and len(facts.selector_correction_edges)
        == claims["selector_correction_edge_count"]
        and facts.selector_correction_edges == ((0, 1), (1, 0))
        and facts.selector_correction_values.get((0, 1))
        == sp.Matrix([0, -scale, 0, 0])
        and facts.selector_correction_values.get((1, 0))
        == sp.Matrix([0, scale, 0, 0])
        and (2, 3) not in facts.selector_correction_values
        and (3, 2) not in facts.selector_correction_values
        and facts.exact_no_float
    )

    star_read_zero = facts.star_read_column == sp.zeros(4, 1)
    mixed_read_zero = facts.mixed_read_column == sp.zeros(4, 1)
    gate_d = bool(
        facts.star_parity == "even"
        and facts.star_parity_blocks_vanish
        and facts.star_read_column
        == sp.Matrix([0, STAR_CORRECTION_SCALE, 0, 0])
        and facts.star_healed_rank == 4
        and facts.mixed_parity == "mixed"
        and facts.mixed_is_parity_mixing
        and mixed_read_zero
        and facts.mixed_healed_rank == 3
        and bool(claims["parity_is_necessary"])
        == bool(star_read_zero and not mixed_read_zero)
        and facts.selector_time_blocks
        == claims["selector_time_block_support"]
        and facts.selector_correction_blocks
        == SELECTOR_CORRECTION_BLOCK_SUPPORT
        and READ_WINDOW_BLOCK not in facts.selector_correction_blocks
        and facts.exact_no_float
    )

    gate_e = bool(
        facts.edge_square_zero_count == claims["edge_square_zero_count"]
        and facts.dressed_edge_rank16_count == 16
        and facts.curvature_nonzero_triples
        == claims["curvature_nonzero_triples"]
        and facts.companion_rank_four_count == 14
        and facts.rank_three_leftovers == ((2, 2), (3, 3))
        and facts.genuine_correction_count == 10
        and canonical(
            facts.healed_displayed_determinant
            - claims["healed_displayed_determinant"]
        )
        == 0
        and facts.healed_determinant_real_roots == ()
        and facts.exact_no_float
    )

    gate_f = bool(
        facts.cocycle_system_shape == (64, 16)
        and facts.cocycle_system_rank == claims["cocycle_system_rank"]
        and facts.cocycle_solution_dimension == 3
        and facts.potential_reproduces_every_solution
        and facts.self_edges_forced_zero
        == bool(claims["self_edges_forced_zero"])
        and facts.odd_self_edge_ranks == (3, 3)
        and facts.companion_rank_four_count == 14
    )

    gate_g = bool(
        facts.mask_violation_count == claims["mask_violation_count"]
        and facts.selector_mask_size == 64
        and facts.projection_is_not_star
        and facts.symbolic_read_column
        == sp.Matrix([0, SYMBOLIC_CORRECTION_SCALE * ST, 0, 0])
        and facts.symbolic_read_column_degree == 1
        and facts.symbolic_read_column_free_symbols == frozenset({ST})
        and facts.symbolic_read_column.subs(ST, 0) == sp.zeros(4, 1)
        and facts.exact_no_float
    )

    required = tuple(claims["required_scope_keys"])
    gate_h = bool(
        set(facts.scope) == set(required)
        and all(facts.scope.values())
        and len(MUTATIONS) == 15
        and len(set(MUTATIONS)) == 15
        and set(MUTATION_GATE) == set(MUTATIONS)
        and set(MUTATION_GATE.values()) == set("ABCDEFGH")
        and N5_FENCE.count("\n") == 7
        and elapsed_ns <= 500 * 1_000_000_000
    )

    return {
        "A": gate_a,
        "B": gate_b,
        "C": gate_c,
        "D": gate_d,
        "E": gate_e,
        "F": gate_f,
        "G": gate_g,
        "H": gate_h,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS, default="")
    mutation = parser.parse_args().mutation
    started_ns = time.monotonic_ns()

    # Every measurement happens once, before any mutation flag is consulted,
    # so a mutation can only rewrite a CLAIM.  No gate can cascade into
    # another because no gate feeds a measurement.
    facts = measure()
    elapsed_ns = time.monotonic_ns() - started_ns

    raw_gates = evaluate_gates(facts, build_claims(""), elapsed_ns)
    gate_values = dict(raw_gates)
    if mutation:
        target = MUTATION_GATE[mutation]
        gate_values = evaluate_gates(
            facts, build_claims(mutation), elapsed_ns
        )
        changed = {
            key for key in raw_gates if raw_gates[key] != gate_values[key]
        }
        if changed - {target} or gate_values[target]:
            raise AssertionError(
                "mutation did not fail exactly its own gate"
            )

    checks = Checks()
    checks.check(
        "A-authority",
        "main plus the committed Block 140, 137 and 134 note/runner/cache artifacts are content-bound",
        gate_values["A"],
    )
    checks.check(
        "B-chart-anchor",
        "the forward companion B_i is rank 4 with the exact determinants on the cover-time-even charts and rank 3 with kernel span(0,1,0,0) on the cover-time-odd charts",
        gate_values["B"],
    )
    checks.check(
        "C-selector-edge-profile",
        "Block 137's selector dressing corrects the read column on exactly 2 of 16 ordered edges, is itself zero on 12, and genuinely misses the displayed pair",
        gate_values["C"],
    )
    checks.check(
        "D-mechanism-witnesses",
        "the grading-even Omega* corrects the read column and heals to rank 4 while the parity-mixing control leaves it identically zero, and the selector's cover-time support omits the read window",
        gate_values["D"],
    )
    checks.check(
        "E-coboundary-healing-family",
        "Omega_ij=(x_j-x_i)Omega* keeps all 16 edges square-zero, has 0/64 Cech curvature, reaches companion rank 4 on 14/16 edges, and gives the displayed edge a determinant with no real mass root",
        gate_values["E"],
    )
    checks.check(
        "F-cocycle-converse",
        "the zero-curvature system has rank 13, every solution is the base-chart coboundary c_j-c_i, Omega_ii=0 is forced, and 14/16 is therefore a hard maximum",
        gate_values["F"],
    )
    checks.check(
        "G-out-of-class-and-riders",
        "Omega* is not any coordinate mask of the displayed full difference (32 violating entries) and its read column is exactly (0,1303*s_t/1200,0,0), linear in s_t and zero at s_t=0",
        gate_values["G"],
    )
    checks.check(
        "H-note-scope",
        "the chart anchor, the anchor correction, the healing family, the converse, the out-of-class rider, the disclosures, the firewalls, and the exact N5 fence are present",
        gate_values["H"],
    )
    checks.report()
    print(N5_FENCE)
    return checks.finish()


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except SystemExit:
        raise
    except Exception as error:
        print(f"[FAIL] INTERNAL-EXCEPTION: {type(error).__name__}: {error}")
        print("TOTAL: PASS=0 FAIL=1")
        raise
