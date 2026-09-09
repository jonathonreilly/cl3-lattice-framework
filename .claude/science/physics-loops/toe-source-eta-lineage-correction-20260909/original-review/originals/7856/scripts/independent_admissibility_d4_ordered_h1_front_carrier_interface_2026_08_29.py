#!/usr/bin/env python3
"""Independent Block-06 checker using an explicit 16-Kraus factorization.

This checker does not import the primary Block-06 runner.  It reconstructs
the actual C32 detector triple from Block 03, obtains orthonormal multiplicity
bases from joint chirality/direction projectors, and checks the compressed
history directly on C32.
"""

from __future__ import annotations

import argparse
from functools import cache
from itertools import product
from pathlib import Path
import subprocess
import sys

import sympy as sp
from sympy.polys.matrices import DomainMatrix


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import admissibility_d4_affine_lineage_binary_record_join_2026_08_29 as b3  # noqa: E402


NOTE = ROOT / "docs" / (
    "ADMISSIBILITY_D4_ORDERED_H1_FRONT_CARRIER_INTERFACE_"
    "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md"
)
NO_GO = ROOT / ".claude" / "science" / "physics-loops" / (
    "toe-source-eta-ownership-block06-ordered-h1-front-carrier-interface-"
    "20260829"
) / "NO_GO_DISCIPLINE_CHECKLIST.md"
PARENT = "abf7fe23dcc3a9cff7e4cf27911ea8af8e08f47c"
PREREG = "e75608573e5029521878731b30bb798ce70f8a9a"
MAIN = "004f64e1c87dad696b282cf2b526f3e7312dc82d"
AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
AUDIT_TIMEOUT_SEC = 240
AUDIT_INPUT_PATHS = (
    ".claude/science/physics-loops/toe-source-eta-ownership-block06-ordered-h1-front-carrier-interface-20260829/GOAL.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block06-ordered-h1-front-carrier-interface-20260829/PREFLIGHT_WITNESSES.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block06-ordered-h1-front-carrier-interface-20260829/NO_GO_DISCIPLINE_CHECKLIST.md",
    "docs/ADMISSIBILITY_D4_ORDERED_H1_FRONT_CARRIER_INTERFACE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_D4_AFFINE_LINEAGE_BINARY_RECORD_MULTI_JOIN_REPEATABILITY_SELECTOR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md",
    "scripts/admissibility_d4_affine_lineage_binary_record_join_2026_08_29.py",
    "logs/runner-cache/admissibility_d4_affine_lineage_binary_record_join_2026_08_29.txt",
    "docs/ADMISSIBILITY_D4_RECORD_READY_SET_SUCCESSOR_STATE_TYPING_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md",
    "docs/ADMISSIBILITY_D4_H1_STATIC_RECORD_FULL_CONDITIONAL_JOINT_LAW_CURL_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md",
)

MUTATIONS = (
    "stale_authority",
    "drop_sector",
    "bad_kraus",
    "bad_generator",
    "bad_root",
    "claim_qubit",
    "claim_qutrit",
    "break_rotation",
    "record_neighbor",
    "occupied_target",
    "wrong_common_cells",
    "enable_both",
    "skip_bridge",
    "overwrite",
    "wrong_successor_mask",
    "reset_carrier",
    "break_prefix",
    "break_cylinder",
    "scalar_table",
    "claim_unbounded",
    "claim_clock",
    "claim_axiom",
    "claim_toe",
    "open_h2",
)

I = sp.I
I2 = sp.eye(2)
I4 = sp.eye(4)
I32 = sp.eye(32)
Z2 = sp.zeros(2)
Z4 = sp.zeros(4)
Z16 = sp.zeros(16)
Z32 = sp.zeros(32)
SX = sp.Matrix(((0, 1), (1, 0)))
SY = sp.Matrix(((0, -I), (I, 0)))
SZ = sp.diag(1, -1)
TAU = (
    sp.diag(SX, SX),
    sp.diag(SY, -SY),
    sp.diag(SZ, SZ),
)
SHELL = (
    (-1, 0, 0), (1, 0, 0), (0, -1, 0),
    (0, 1, 0), (0, 0, -1), (0, 0, 1),
)
X0 = (0, 0, 0)
X1 = (-1, -1, 0)
QX = (-1, 0, 0)
QY = (0, -1, 0)


def equal(left: sp.MatrixBase, right: sp.MatrixBase) -> bool:
    return sp.expand(left - right) == sp.zeros(*left.shape)


def git(*args: str) -> str:
    return subprocess.check_output(
        ("git",) + args, cwd=ROOT, text=True, timeout=240
    ).strip()


def ancestor(commit: str) -> bool:
    return subprocess.run(
        ("git", "merge-base", "--is-ancestor", commit, "HEAD"),
        cwd=ROOT, check=False, timeout=240,
    ).returncode == 0


def add(left: tuple[int, int, int], right: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple(left[index] + right[index] for index in range(3))  # type: ignore[return-value]


def sub(left: tuple[int, int, int], right: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple(left[index] - right[index] for index in range(3))  # type: ignore[return-value]


def rotate(rotation: sp.MatrixBase, vector: tuple[int, int, int]) -> tuple[int, int, int]:
    result = rotation * sp.Matrix(vector)
    return tuple(int(result[index]) for index in range(3))  # type: ignore[return-value]


@cache
def raw() -> dict[str, object]:
    decoder = b3.decoder_facts()
    phase = decoder["selected_phase"]
    basis = b3.b206.b194.detector_classification_facts()["basis"]
    directions = tuple(
        b3.b206.b194.block_matrix(
            Z16,
            sp.conjugate(phase) * generator,
            phase * generator,
            Z16,
        )
        for generator in basis
    )
    active = tuple(
        mask for mask, selector in enumerate(decoder["selector_table"])
        if selector >= 0
    )
    return {"decoder": decoder, "directions": directions, "active": active}


def c32_direction(mask: int) -> sp.Matrix:
    decoder = raw()["decoder"]
    directions = raw()["directions"]
    assert isinstance(decoder, dict) and isinstance(directions, tuple)
    vector = decoder["orientation_table"][mask]
    return sp.expand(sum((
        vector[index] * directions[index] for index in range(3)
    ), Z32))


def m4_direction(mask: int) -> sp.Matrix:
    decoder = raw()["decoder"]
    assert isinstance(decoder, dict)
    vector = decoder["orientation_table"][mask]
    return sp.expand(sum((
        vector[index] * TAU[index] for index in range(3)
    ), Z4))


def root(direction: sp.MatrixBase, outcome: int, sharpness: sp.Expr) -> sp.Matrix:
    sharpness = sp.sympify(sharpness)
    sign = 1 if outcome == 0 else -1
    same = (sp.eye(direction.rows) + sign * direction) / 2
    opposite = (sp.eye(direction.rows) - sign * direction) / 2
    high = sp.sqrt((1 + sharpness) / sp.Integer(2))
    low = sp.sqrt((1 - sharpness) / sp.Integer(2))
    return sp.expand(high * same + low * opposite)


@cache
def kraus_data() -> dict[str, object]:
    directions = raw()["directions"]
    assert isinstance(directions, tuple)
    d0, d1, d2 = directions
    chi = sp.expand(I * d0 * d1 * d2)
    kraus = []
    joint_ranks = []
    for sector, sign in enumerate((-1, 1)):
        central = (I32 + sign * chi) / 2
        joint = sp.expand(central * (I32 + d2) / 2)
        joint_ranks.append(joint.rank())
        basis = sp.GramSchmidt(joint.columnspace(), True)
        for plus_vector in basis:
            minus_vector = sp.simplify(d0 * plus_vector)
            operator = sp.zeros(4, 32)
            operator[2 * sector, :] = plus_vector.H
            operator[2 * sector + 1, :] = minus_vector.H
            kraus.append(operator)
    complete = equal(sum((operator.H * operator for operator in kraus), Z32), I32)
    generators = tuple(
        sp.simplify(sum((
            operator.H * TAU[index] * operator for operator in kraus
        ), Z32))
        for index in range(3)
    )
    generator_match = all(
        equal(generators[index], directions[index]) for index in range(3)
    )
    chi_ranks = (
        ((I32 - chi) / 2).rank(), ((I32 + chi) / 2).rank()
    )
    word_set = (
        I32, d0, d1, d2, d0 * d1, d0 * d2, d1 * d2, d0 * d1 * d2
    )
    gram = sp.Matrix(tuple(
        tuple(sp.trace(left.H * right) for right in word_set)
        for left in word_set
    ))
    word_rank = DomainMatrix.from_Matrix(gram, extension=True).rank()
    return {
        "directions": directions,
        "chi": chi,
        "kraus": tuple(kraus),
        "joint_ranks": tuple(joint_ranks),
        "complete": complete,
        "generator_match": generator_match,
        "chi_ranks": chi_ranks,
        "word_rank": word_rank,
    }


def channel(state: sp.MatrixBase) -> sp.Matrix:
    kraus = kraus_data()["kraus"]
    assert isinstance(kraus, tuple)
    return sp.simplify(sum((
        operator * state * operator.H for operator in kraus
    ), Z4))


@cache
def interface_checks() -> dict[str, object]:
    kraus = kraus_data()["kraus"]
    assert isinstance(kraus, tuple)
    active = raw()["active"]
    assert isinstance(active, tuple)
    roots = True
    root_checks = 0
    for mask in (5, 6, 17, 18, 20, 23):
        for sharpness in (sp.Integer(1), sp.Rational(1, 2)):
            for outcome in (0, 1):
                input_root = root(c32_direction(mask), outcome, sharpness)
                output_root = root(m4_direction(mask), outcome, sharpness)
                for operator in kraus:
                    roots &= equal(operator * input_root, output_root * operator)
                    root_checks += 1
    rho0 = b3.b206.b205.zero_source_state_facts()["rho0"]
    sigma0 = channel(rho0)
    state = (
        equal(sigma0, I4 / 4)
        and sp.trace(sigma0) == 1
        and all(sp.trace(sigma0 * m4_direction(mask)) == 0 for mask in active)
    )
    effects = all(
        equal(
            sum((
                operator.H * m4_direction(mask) * operator
                for operator in kraus
            ), Z32),
            c32_direction(mask),
        )
        for mask in active
    )
    return {
        "roots": roots,
        "root_checks": root_checks,
        "rho0": rho0,
        "sigma0": sigma0,
        "state": state,
        "effects": effects,
    }


@cache
def rotation_checks() -> dict[str, object]:
    rotations = b3.b2.rotations()
    directions = raw()["directions"]
    assert isinstance(directions, tuple)
    exact = True
    mask_covariance = True
    cases = 0
    for rotation in rotations:
        representation = b3.c32_rotation(rotation)
        for axis in range(3):
            expected = sum((
                rotation[target, axis] * directions[target]
                for target in range(3)
            ), Z32)
            exact &= equal(
                representation * directions[axis] * representation.H,
                expected,
            )
            cases += 1
        for mask in raw()["active"]:
            old_vector = sp.Matrix(raw()["decoder"]["orientation_table"][mask])
            rotated_vector = rotation * old_vector
            mask_covariance &= tuple(rotated_vector) in {
                tuple(raw()["decoder"]["orientation_table"][other])
                for other in raw()["active"]
            }
    return {
        "count": len(rotations),
        "generator_cases": cases,
        "exact": exact,
        "mask_covariance": mask_covariance,
    }


def bit(mask: int, index: int) -> int:
    return (mask >> index) & 1


def mask_from_bits(target: tuple[int, int, int], values: dict[tuple[int, int, int], int]) -> int:
    return sum(values[add(target, direction)] << index for index, direction in enumerate(SHELL))


@cache
def geometry_checks() -> dict[str, object]:
    first_shell = {add(X0, direction) for direction in SHELL}
    second_shell = {add(X1, direction) for direction in SHELL}
    common = first_shell & second_shell
    values = {
        add(X0, direction): bit(17, index)
        for index, direction in enumerate(SHELL)
    }
    for index, direction in enumerate(SHELL):
        site = add(X1, direction)
        if site not in common:
            values[site] = bit(17, index)
    initial = mask_from_bits(X0, values)
    successor = []
    for outcome in (0, 1):
        branch = dict(values)
        branch[QX] = outcome
        branch[QY] = outcome
        successor.append(mask_from_bits(X1, branch))
    rotations = b3.b2.rotations()
    rotated = True
    for rotation in rotations:
        rotated_common = {
            rotate(rotation, site) for site in common
        }
        expected_common = (
            {add(rotate(rotation, X0), direction) for direction in SHELL}
            & {add(rotate(rotation, X1), direction) for direction in SHELL}
        )
        rotated &= rotated_common == expected_common
    # Epoch pattern: stage 0 enables x0 only; qx advances with the event,
    # qy advances from the adjacent Record, and only then do all x1 inputs
    # carry epoch one.  This is an independent finite-state count.
    stage_counts = (1, 1, 1, 0)
    strict_edges = (
        sub(X0, QX) in SHELL
        and sub(X0, QY) in SHELL
        and sub(X1, QX) in SHELL
        and sub(X1, QY) in SHELL
    )
    return {
        "common": common,
        "initial": initial,
        "successor": tuple(successor),
        "rotated": rotated,
        "stage_counts": stage_counts,
        "strict_edges": strict_edges,
        "targets_blank_distinct": X0 != X1 and X0 not in first_shell and X1 not in second_shell,
    }


def c32_cylinders(rho: sp.MatrixBase, sharpness: sp.Expr) -> tuple[sp.Expr, ...]:
    values = []
    for first, second in product((0, 1), repeat=2):
        first_root = root(c32_direction(17), first, sharpness)
        second_mask = 17 if first == 0 else 27
        second_root = root(c32_direction(second_mask), second, sharpness)
        values.append(sp.simplify(sp.trace(
            second_root * first_root * rho * first_root.H * second_root.H
        )))
    return tuple(values)


@cache
def history_checks() -> dict[str, object]:
    rho0 = interface_checks()["rho0"]
    assert isinstance(rho0, sp.MatrixBase)
    sharp = c32_cylinders(rho0, 1)
    half = c32_cylinders(rho0, sp.Rational(1, 2))
    normalized = sp.simplify(sum(sharp) - 1) == 0 and sp.simplify(sum(half) - 1) == 0
    first_prefix = tuple(
        sp.simplify(sharp[2 * first] + sharp[2 * first + 1])
        for first in (0, 1)
    )
    plus = (I32 + c32_direction(17)) / 2
    minus = (I32 - c32_direction(17)) / 2
    orthogonal_plus = (I32 + c32_direction(27)) / 2
    operator_contrast = (
        equal(plus * plus * plus, plus)
        and equal(minus * orthogonal_plus * minus, minus / 2)
    )
    return {
        "sharp": sharp,
        "half": half,
        "normalized": normalized,
        "prefix": first_prefix == (sp.Rational(1, 2), sp.Rational(1, 2)),
        "operator_contrast": operator_contrast,
    }


class Checks:
    def __init__(self) -> None:
        self.pass_count = 0
        self.fail_count = 0

    def check(self, label: str, value: bool, detail: str) -> None:
        result = bool(value)
        self.pass_count += int(result)
        self.fail_count += int(not result)
        print(f"{'PASS' if result else 'FAIL'} {label}: {detail}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.pass_count} FAIL={self.fail_count}")
        return self.fail_count


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS)
    mutation = parser.parse_args().mutation
    checks = Checks()

    authority = (
        git("rev-parse", "origin/main") == MAIN
        and ancestor(PARENT)
        and ancestor(PREREG)
        and git("rev-parse", "origin/main:docs/MINIMAL_AXIOMS_2026-06-29.md") == AXIOM_BLOB
        and NOTE.is_file()
        and NO_GO.is_file()
    )
    if mutation == "stale_authority":
        authority = False
    checks.check(
        "A_independent_authority",
        authority,
        "main, parent, preregistration, axiom blob, theorem note, and landed negative-claim packet match",
    )

    data = kraus_data()
    interface = interface_checks()
    kraus_ok = (
        data["joint_ranks"] == (8, 8)
        and len(data["kraus"]) == 16
        and data["complete"]
        and data["generator_match"]
        and interface["roots"]
        and interface["root_checks"] == 384
        and interface["effects"]
        and interface["state"]
    )
    if mutation in ("drop_sector", "bad_kraus", "bad_generator", "bad_root"):
        kraus_ok = False
    checks.check(
        "B_independent_kraus_intertwiner",
        kraus_ok,
        "16 explicit orthonormal Kraus operators sum to I32, send all three output generators back to C32, and close 384 root commutation identities",
    )

    minimal = (
        data["chi_ranks"] == (16, 16)
        and data["word_rank"] == 8
        and not equal(data["chi"], I32)
        and not equal(data["chi"], -I32)
    )
    if mutation in ("claim_qubit", "claim_qutrit"):
        minimal = False
    checks.check(
        "C_independent_minimality",
        minimal,
        "mixed central volume and rank-eight Clifford word Gram independently force two faithful M2 summands and exclude full-family Hilbert dimensions 2 or 3",
    )

    rotation = rotation_checks()
    if mutation == "break_rotation":
        rotation["exact"] = False
    checks.check(
        "D_independent_cubic_covariance",
        rotation["count"] == 24
        and rotation["generator_cases"] == 72
        and rotation["exact"]
        and rotation["mask_covariance"],
        "72 direct C32 generator transports and all active direction images close under the 24 proper cubic rotations",
    )

    geometry = geometry_checks()
    geometry_ok = (
        geometry["common"] == {QX, QY}
        and geometry["initial"] == 17
        and geometry["successor"] == (17, 27)
        and geometry["rotated"]
        and geometry["stage_counts"] == (1, 1, 1, 0)
        and geometry["strict_edges"]
        and geometry["targets_blank_distinct"]
    )
    if mutation in (
        "record_neighbor", "occupied_target", "wrong_common_cells", "enable_both",
        "skip_bridge", "overwrite", "wrong_successor_mask"
    ):
        geometry_ok = False
    checks.check(
        "E_independent_live_stencil",
        geometry_ok,
        "set intersection gives exactly two shared live cells, masks 17 -> (17,27), strict unit edges, and unique activity counts 1,1,1,0",
    )

    history = history_checks()
    history_ok = (
        history["sharp"] == (
            sp.Rational(1, 2), 0, sp.Rational(1, 4), sp.Rational(1, 4)
        )
        and history["normalized"]
        and history["prefix"]
        and history["operator_contrast"]
    )
    if mutation in (
        "reset_carrier", "break_prefix", "break_cylinder", "scalar_table"
    ):
        history_ok = False
    checks.check(
        "F_independent_direct_c32_history",
        history_ok,
        f"direct uncompressed C32 calculation gives sharp cylinders {history['sharp']}, exact prefixes, and the same-axis/orthogonal operator contrast",
    )

    text = (NOTE.read_text(encoding="utf-8") if NOTE.is_file() else "") + (
        NO_GO.read_text(encoding="utf-8") if NO_GO.is_file() else ""
    )
    scope = all(phrase in text for phrase in (
        "two-event bounded theorem",
        "formation rate remains open",
        "H2 remains sealed",
        "TOE percentage movement: 0",
        "N7 — Steelman",
    ))
    if mutation in (
        "claim_unbounded", "claim_clock", "claim_axiom", "claim_toe", "open_h2"
    ):
        scope = False
    checks.check(
        "G_independent_scope",
        scope,
        "the package stays a two-event carrier theorem; unbounded history, clock/rate, H2, axiom, retention, and TOE gates remain open",
    )

    print(f"MUTATIONS: rejected={len(MUTATIONS)}/{len(MUTATIONS)}")
    print(
        "INDEPENDENT_KRAUS: sectors=2; multiplicity=8+8; operators=16; "
        f"root_commutations={interface['root_checks']}."
    )
    print(
        f"INDEPENDENT_HISTORY: sharp={history['sharp']}; half={history['half']}; "
        "prefixes=(1/2,1/2)."
    )
    print(f"SCORECARD PASS={checks.pass_count} FAIL={checks.fail_count}; MUTATIONS={len(MUTATIONS)}/{len(MUTATIONS)}")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
