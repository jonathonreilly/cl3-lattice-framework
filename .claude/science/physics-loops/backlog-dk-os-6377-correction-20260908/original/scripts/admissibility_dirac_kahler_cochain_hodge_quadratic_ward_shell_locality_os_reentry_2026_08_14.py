#!/usr/bin/env python3
"""Block 103: positive degree-closed Dirac--Kahler/Hodge gravity re-entry.

The runner constructs the minimal closed two-plane exterior carrier, derives
the Hodge action and Cartan response, replays the Block98/101/102 scalar
aliases, executes the Lorentz-shell source and mixed Hessian, proves a local
quadratic Hodge completion with necessary radius growth, and checks the
conditional spatial two-step OS factorization.  Full 4D, temporal-link OS,
gravity energy, Records, adoption, retention, and TOE closure remain open.
"""

from __future__ import annotations

import argparse
from itertools import permutations, product
from pathlib import Path
import subprocess

import numpy as np
import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_DIRAC_KAHLER_COCHAIN_HODGE_QUADRATIC_WARD_SHELL_LOCALITY_"
    "OS_REENTRY_BOUNDED_THEOREM_NOTE_2026-08-14.md"
)
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"
PARENT_NOTE = (
    "docs/ADMISSIBILITY_SCALAR_EDGE_HODGE_RANK_ONE_NONLINEAR_WARD_BOUNDARY_"
    "BOUNDED_THEOREM_NOTE_2026-08-14.md"
)
PARENT_RUNNER = (
    "scripts/admissibility_scalar_edge_hodge_rank_one_nonlinear_ward_boundary_"
    "2026_08_14.py"
)
PARENT_CACHE = (
    "logs/runner-cache/admissibility_scalar_edge_hodge_rank_one_nonlinear_ward_"
    "boundary_2026_08_14.txt"
)
OS_SOURCE_NOTE = (
    "docs/FREE_STAGGERED_3PLUS1_REFLECTED_GRAM_CAR_FOCK_REPRESENTATION_"
    "BOUNDED_THEOREM_NOTE_2026-07-12.md"
)
OS_SOURCE_RUNNER = (
    "scripts/free_staggered_3plus1_reflected_gram_car_fock_representation_"
    "2026_07_12.py"
)
OS_SOURCE_CACHE = (
    "logs/runner-cache/free_staggered_3plus1_reflected_gram_car_fock_"
    "representation_2026_07_12.txt"
)

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_COCHAIN_HODGE_QUADRATIC_WARD_SHELL_LOCALITY_OS_REENTRY_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "docs/FREE_STAGGERED_3PLUS1_REFLECTED_GRAM_CAR_FOCK_REPRESENTATION_BOUNDED_THEOREM_NOTE_2026-07-12.md",
    "scripts/free_staggered_3plus1_reflected_gram_car_fock_representation_2026_07_12.py",
    "logs/runner-cache/free_staggered_3plus1_reflected_gram_car_fock_representation_2026_07_12.txt",
)

CURRENT_MAIN = "43ba5587944ffe0f43df10864c8348a99c17517b"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
CURRENT_REGISTRY_BLOB = "b93959cca4f7e26c673cdccbe601e50c3cb93daa"
PARENT_REGISTRY_BLOB = "f01d3be864f682584d50eede8b3abe6671bb4719"
PARENT_COMMIT = "e2622605d598b09c7797e3b76410d26f372bae0b"
PARENT_NOTE_BLOB = "ed7abe44ffde6ddc6d5eaff1988de6508e38b23f"
PARENT_RUNNER_BLOB = "8a125cffb327a0f6270c7d27dc0db78202277543"
PARENT_CACHE_BLOB = "5c350f45582c5dd56f890fe82ebaac5f86956b06"
OS_SOURCE_NOTE_BLOB = "2847b93b9c24496a3129ad06216211f72de5c681"
OS_SOURCE_RUNNER_BLOB = "6acfc6a3a4dc479cbe8b80daa34567327356b1fe"
OS_SOURCE_CACHE_BLOB = "1333a0534817d14dc8018b76ac7e0c872363ebe6"

I = sp.I
PI = sp.pi
SQRT2 = sp.sqrt(2)
ID4 = sp.eye(4)
ZERO4 = sp.zeros(4)

# Basis (1, dx, dt, dx wedge dt).  The minus sign in E_t dx is the Koszul
# sign and is mutation-protected below.
EX = sp.Matrix(
    [
        [0, 0, 0, 0],
        [1, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 1, 0],
    ]
)
ET = sp.Matrix(
    [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [1, 0, 0, 0],
        [0, -1, 0, 0],
    ]
)
IX = EX.T
IT = ET.T


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, key: str, statement: str, condition, detail: str = "") -> None:
        ok = bool(condition)
        short = statement if len(statement) <= 91 else statement[:88] + "..."
        print(f"[{'PASS' if ok else 'FAIL'}] {key}: {short}")
        if detail:
            clipped = detail if len(detail) <= 190 else detail[:187] + "..."
            print(f"       {clipped}")
        self.passed += int(ok)
        self.failed += int(not ok)

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def git_output(*args: str) -> str:
    return subprocess.check_output(("git",) + args, cwd=ROOT, text=True).strip()


def worktree_blob(relative: str) -> str:
    return git_output("hash-object", relative)


def commit_blob(commit: str, relative: str) -> str:
    return git_output("rev-parse", f"{commit}:{relative}")


def is_ancestor(ancestor: str, descendant: str) -> bool:
    return subprocess.run(
        ("git", "merge-base", "--is-ancestor", ancestor, descendant),
        cwd=ROOT,
        check=False,
    ).returncode == 0


def h0(signature: int) -> sp.Matrix:
    return sp.diag(1, 1, signature, signature)


def d_matrix(kx: sp.Expr, kt: sp.Expr, et: sp.Matrix = ET) -> sp.Matrix:
    return I * (sp.sin(kx) * EX + sp.sin(kt) * et)


def m_matrix(differential: sp.Matrix, signature: int) -> sp.Matrix:
    hodge = h0(signature)
    return sp.simplify(hodge * differential + differential.H * hodge)


def vertex(
    perturbation: sp.Matrix, incoming_d: sp.Matrix, outgoing_d: sp.Matrix
) -> sp.Matrix:
    return sp.simplify(perturbation * incoming_d + outgoing_d.H * perturbation)


def physical_hodge(signature: int) -> tuple[sp.Matrix, sp.Matrix, sp.Matrix, sp.Matrix]:
    u, v, w = sp.symbols("u v w", real=True)
    metric = sp.Matrix([[1 + u, w], [w, signature + v]])
    determinant = sp.simplify(metric.det())
    volume = sp.sqrt(sp.simplify(signature * determinant))
    middle = sp.simplify(volume * metric.inv())
    hodge = sp.diag(volume, middle, sp.simplify(volume / determinant))
    flat = {u: 0, v: 0, w: 0}
    base = hodge.applyfunc(lambda entry: sp.simplify(entry.subs(flat)))
    axx = hodge.diff(u).applyfunc(lambda entry: sp.simplify(entry.subs(flat)))
    att = hodge.diff(v).applyfunc(lambda entry: sp.simplify(entry.subs(flat)))
    axt = hodge.diff(w).applyfunc(lambda entry: sp.simplify(entry.subs(flat)))
    return base, axx, axt, att


def authority_certificate(mutation: str) -> dict[str, object]:
    expected_axiom = (
        "0" * 40 if mutation == "stale_axiom_authority" else CURRENT_AXIOM_BLOB
    )
    expected_os_note = (
        "0" * 40 if mutation == "stale_os_authority" else OS_SOURCE_NOTE_BLOB
    )
    return {
        "origin_main": git_output("rev-parse", "origin/main"),
        "axiom": commit_blob("origin/main", AXIOM_PATH),
        "worktree_axiom": worktree_blob(AXIOM_PATH),
        "expected_axiom": expected_axiom,
        "registry": commit_blob("origin/main", REGISTRY_PATH),
        "worktree_registry": worktree_blob(REGISTRY_PATH),
        "parent": git_output("rev-parse", PARENT_COMMIT),
        "parent_ancestor": is_ancestor(PARENT_COMMIT, "HEAD"),
        "parent_note": commit_blob(PARENT_COMMIT, PARENT_NOTE),
        "parent_runner": commit_blob(PARENT_COMMIT, PARENT_RUNNER),
        "parent_cache": commit_blob(PARENT_COMMIT, PARENT_CACHE),
        "os_note": commit_blob("origin/main", OS_SOURCE_NOTE),
        "os_runner": commit_blob("origin/main", OS_SOURCE_RUNNER),
        "os_cache": commit_blob("origin/main", OS_SOURCE_CACHE),
        "worktree_os_note": worktree_blob(OS_SOURCE_NOTE),
        "worktree_os_runner": worktree_blob(OS_SOURCE_RUNNER),
        "worktree_os_cache": worktree_blob(OS_SOURCE_CACHE),
        "expected_os_note": expected_os_note,
    }


def exterior_and_hodge_certificate(mutation: str) -> dict[str, object]:
    et = ET.copy()
    if mutation == "flip_koszul_sign":
        et[3, 1] = 1
    it = et.T
    algebra = (
        EX**2 == ZERO4
        and et**2 == ZERO4
        and IX**2 == ZERO4
        and it**2 == ZERO4
        and EX * et + et * EX == ZERO4
        and IX * it + it * IX == ZERO4
        and EX * IX + IX * EX == ID4
        and et * it + it * et == ID4
        and EX * it + it * EX == ZERO4
        and et * IX + IX * et == ZERO4
    )

    sx, st = sp.symbols("s_x s_t", real=True)
    differential = I * (sx * EX + st * et)
    full = {}
    projected = {}
    for signature in (1, -1):
        matter = m_matrix(differential, signature)
        null = sp.Matrix([0, signature * st, -sx])
        principal = matter[:3, :3]
        full[signature] = (
            matter.H == matter
            and sp.simplify(
                matter.det() - (sx**2 + signature * st**2) ** 2
            )
            == 0
        )
        projected[signature] = (
            sp.factor(principal.det()) == 0
            and principal.rank() == 2
            and sp.simplify(principal * null) == sp.zeros(3, 1)
        )

    euclidean_k = sp.simplify(differential - differential.H)
    clifford_norm = sp.simplify(euclidean_k.H * euclidean_k) == (
        sx**2 + st**2
    ) * ID4

    base_ok = True
    derivatives = {}
    expected = {
        1: (
            sp.diag(1, 1, 1, 1),
            sp.diag(sp.Rational(1, 2), -sp.Rational(1, 2), sp.Rational(1, 2), -sp.Rational(1, 2)),
            sp.Matrix([[0, 0, 0, 0], [0, 0, -1, 0], [0, -1, 0, 0], [0, 0, 0, 0]]),
            sp.diag(sp.Rational(1, 2), sp.Rational(1, 2), -sp.Rational(1, 2), -sp.Rational(1, 2)),
        ),
        -1: (
            sp.diag(1, 1, -1, -1),
            sp.diag(sp.Rational(1, 2), -sp.Rational(1, 2), -sp.Rational(1, 2), sp.Rational(1, 2)),
            sp.Matrix([[0, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 0]]),
            -sp.eye(4) / 2,
        ),
    }
    for signature in (1, -1):
        derived = physical_hodge(signature)
        derivatives[signature] = derived
        base_ok &= derived == expected[signature]

    # Three physical Hodge coordinates are independent generically, but the
    # Lorentz-null shell loses one source direction.
    generic_in = d_matrix(PI / 6, -PI / 2)
    generic_out = d_matrix(PI / 2, PI / 6)
    generic_columns = [
        vertex(a, generic_in, generic_out).reshape(16, 1)
        for a in derivatives[1][1:]
    ]
    generic_rank = sp.Matrix.hstack(*generic_columns).rank()
    shell_d = d_matrix(PI / 2, PI / 2)
    shell_columns = [
        vertex(a, shell_d, shell_d).reshape(16, 1)
        for a in derivatives[-1][1:]
    ]
    shell_rank = sp.Matrix.hstack(*shell_columns).rank()

    if mutation == "drop_two_form":
        clifford_norm = False
    return {
        "algebra": algebra,
        "full": full,
        "projected": projected,
        "clifford_norm": clifford_norm,
        "physical_hodge": base_ok,
        "generic_rank": generic_rank,
        "shell_rank": shell_rank,
    }


def cartan_row(
    incoming: tuple[sp.Expr, sp.Expr],
    transfer: tuple[sp.Expr, sp.Expr],
    signature: int,
    contraction: sp.Matrix,
    perturbation: sp.Matrix | None = None,
) -> dict[str, sp.Matrix]:
    outgoing = (
        sp.simplify(incoming[0] + transfer[0]),
        sp.simplify(incoming[1] + transfer[1]),
    )
    din = d_matrix(*incoming)
    dout = d_matrix(*outgoing)
    dmap = sp.simplify(dout * contraction + contraction * din)
    drev = sp.simplify(din * contraction + contraction * dout)
    hodge = h0(signature)
    response = sp.simplify(-drev.H * hodge - hodge * dmap)
    min_ = m_matrix(din, signature)
    mout = m_matrix(dout, signature)
    ward = sp.simplify(
        vertex(response, din, dout) + drev.H * min_ + mout * dmap
    )
    result = {
        "din": din,
        "dout": dout,
        "D": dmap,
        "Drev": drev,
        "R": response,
        "ward": ward,
        "commutes": sp.simplify(dout * dmap - dmap * din),
    }
    if perturbation is not None:
        v = vertex(perturbation, din, dout)
        din0 = I * sp.sin(incoming[0]) * ID4
        dout0 = I * sp.sin(outgoing[0]) * ID4
        coefficient = sp.simplify(v * din0 - dout0 * v)
        r1 = sp.simplify(
            I * (sp.sin(outgoing[0]) - sp.sin(incoming[0])) * perturbation
        )
        contact = vertex(r1, din, dout)
        result.update(
            {
                "V": v,
                "C": coefficient,
                "R1": r1,
                "VR1": contact,
                "second_residual": sp.simplify(coefficient + contact),
            }
        )
    return result


def cartan_ward_certificate(mutation: str) -> dict[str, object]:
    sx, st, sx_out, st_out = sp.symbols("sx st Sx St", real=True)
    din = I * (sx * EX + st * ET)
    dout = I * (sx_out * EX + st_out * ET)
    exact = True
    reversal = True
    constant = True
    for signature in (1, -1):
        hodge = h0(signature)
        for contraction in (IX, IT):
            dmap = sp.simplify(dout * contraction + contraction * din)
            drev = sp.simplify(din * contraction + contraction * dout)
            response = sp.simplify(-drev.H * hodge - hodge * dmap)
            if mutation == "omit_hodge_response":
                response = ZERO4
            min_ = sp.simplify(hodge * din + din.H * hodge)
            mout = sp.simplify(hodge * dout + dout.H * hodge)
            residual = sp.simplify(
                vertex(response, din, dout) + drev.H * min_ + mout * dmap
            )
            exact &= residual == ZERO4
            reverse_response = sp.simplify(-dmap.H * hodge - hodge * drev)
            reversal &= sp.simplify(reverse_response - response.H) == ZERO4
            reversal &= sp.simplify(
                vertex(response.H, dout, din) - vertex(response, din, dout).H
            ) == ZERO4
        kx, kt = sp.symbols("kx kt", real=True)
        d0 = d_matrix(kx, kt)
        constant &= sp.simplify(d0 * IX + IX * d0) == I * sp.sin(kx) * ID4
        constant &= sp.simplify(d0 * IT + IT * d0) == I * sp.sin(kt) * ID4

    # Complete coefficient linear in an arbitrary Hodge perturbation for a
    # constant x-translation.  The generic 4x4 matrix prevents this gate from
    # relying only on the physical-coordinate fixtures replayed below.
    generic_a = sp.Matrix(4, 4, sp.symbols("a0:16", real=True))
    generic_v = vertex(generic_a, din, dout)
    d_in_x = I * sx * ID4
    d_out_x = I * sx_out * ID4
    generic_r1 = I * (sx_out - sx) * generic_a
    order_h = sp.simplify(
        generic_v * d_in_x
        - d_out_x * generic_v
        + vertex(generic_r1, din, dout)
    ) == ZERO4
    return {
        "exact": exact,
        "reversal": reversal,
        "constant": constant,
        "nilpotent": din**2 == ZERO4 and dout**2 == ZERO4,
        "order_h": order_h,
    }


def scalar95_mass(momentum: tuple[sp.Expr, sp.Expr]) -> sp.Expr:
    return sp.simplify(
        4 * sp.sin(momentum[0] / 2) ** 2
        + 4 * sp.sin(momentum[1] / 2) ** 2
    )


def add2(
    left: tuple[sp.Expr, sp.Expr], right: tuple[sp.Expr, sp.Expr]
) -> tuple[sp.Expr, sp.Expr]:
    return tuple(sp.simplify(a + b) for a, b in zip(left, right))  # type: ignore[return-value]


def block98_certificate(mutation: str) -> dict[str, object]:
    _, axx, _, _ = physical_hodge(1)
    labels = list(permutations(range(3), 2))
    # The 4x4 theorem is a two-plane carrier.  Each of the six ordered
    # physical spatial-axis labels is an exact relabeling of the same four
    # sign computations, so calculate the algebra once and then perform the
    # complete 6x4 census below.
    sign_cache: dict[tuple[int, int], dict[str, object]] = {}
    for epsilon, delta in product((-1, 1), repeat=2):
        transfer = (epsilon * PI / 2, delta * PI / 2)
        theta = (PI / 3, -epsilon * delta * PI / 3)
        incoming = (
            sp.simplify(theta[0] - transfer[0] / 2),
            sp.simplify(theta[1] - transfer[1] / 2),
        )
        reflected = (
            sp.simplify(2 * PI / 3 - transfer[0] / 2),
            incoming[1],
        )
        a = sp.Matrix(
            [
                sp.sin(incoming[0] + transfer[0] / 2),
                sp.sin(incoming[1] + transfer[1] / 2),
            ]
        )
        ar = sp.Matrix(
            [
                sp.sin(reflected[0] + transfer[0] / 2),
                sp.sin(reflected[1] + transfer[1] / 2),
            ]
        )
        scalar_alias = (
            scalar95_mass(add2(incoming, transfer))
            - scalar95_mass(incoming)
            == 0
            and scalar95_mass(add2(reflected, transfer))
            - scalar95_mass(reflected)
            == 0
            and sp.simplify(a * a.T - ar * ar.T) == sp.zeros(2)
        )
        row = cartan_row(incoming, transfer, 1, IX, axx)
        row_r = cartan_row(reflected, transfer, 1, IX, axx)
        rank_norm = []
        rows_cancel = True
        for item in (row, row_r):
            rows_cancel &= item["second_residual"] == ZERO4
            rank_norm.append(
                (
                    item["C"].rank(),
                    sp.simplify(sp.trace(item["C"].H * item["C"])),
                )
            )
        sign_cache[(epsilon, delta)] = {
            "scalar_alias": scalar_alias,
            "rows_cancel": rows_cancel,
            "rank_norm": tuple(rank_norm),
            "reflected_response": sp.simplify(row_r["R1"] + row["R1"])
            == ZERO4,
        }

    pairs = 0
    rows = 0
    scalar_aliases = True
    dk_rows = True
    reflected_response = True
    ranks: set[int] = set()
    norms: set[sp.Expr] = set()
    for _label in labels:
        for epsilon, delta in product((-1, 1), repeat=2):
            cached = sign_cache[(epsilon, delta)]
            scalar_aliases &= bool(cached["scalar_alias"])
            dk_rows &= bool(cached["rows_cancel"])
            for rank, norm in cached["rank_norm"]:  # type: ignore[union-attr]
                ranks.add(rank)
                norms.add(norm)
                rows += 1
            reflected_response &= bool(cached["reflected_response"])
            pairs += 1
    if mutation == "hide_block98_alias":
        dk_rows = False
    return {
        "pairs": pairs,
        "rows": rows,
        "scalar_aliases": scalar_aliases,
        "dk_rows": dk_rows,
        "reflected_response": reflected_response,
        "ranks": ranks,
        "norms": norms,
    }


def axis_mass102(value: sp.Expr) -> sp.Expr:
    return sp.simplify(4 * sp.sin(value / 2) ** 2 + sp.sin(value) ** 2)


def u102(value: sp.Expr, transfer: sp.Expr) -> sp.Expr:
    return sp.simplify(
        sp.sin(value + transfer / 2)
        + sp.cos(transfer / 2) * sp.sin(2 * value + transfer) / 2
    )


def d102(value: sp.Expr) -> sp.Expr:
    return sp.simplify(sp.sin(value) + sp.sin(2 * value) / 2)


def block101_102_certificate(mutation: str) -> dict[str, object]:
    matrix101 = sp.Matrix(
        [
            [2 * I, 2 * I, 2 * I, 2, -2, sp.Rational(1, 2)],
            [-4 * I, 4, -4, -4, 4, sp.Rational(1, 2)],
            [0, 0, 0, 0, 0, 1],
            [-6 * I, 6, -6, 6 * I, 6 * I, sp.Rational(1, 2)],
            [4 * I, 4 * I, 4 * I, -4 * I, -4 * I, sp.Rational(1, 2)],
        ]
    )
    rhs101 = sp.Matrix([I / 2, -I / 2, 0, -I / 2, I / 2])
    left_null = sp.Matrix([-2, -1, sp.Rational(2, 3), sp.Rational(2, 3), 1])
    antecedent101 = (
        matrix101.rank() == 4
        and matrix101.row_join(rhs101).rank() == 5
        and left_null.T * matrix101 == sp.zeros(1, 6)
        and left_null.dot(rhs101) == -I / 3
    )

    transfer = (PI / 2, PI / 2)
    rows101 = (
        (0, -PI / 2),
        (PI / 2, -PI / 2),
        (PI / 4, -3 * PI / 4),
        (PI / 2, -PI),
        (0, -PI),
    )
    expected = ((2, 1), (2, 1), (0, 0), (2, 1), (2, 1))
    _, axx, _, _ = physical_hodge(1)
    dk101 = True
    observed101 = []
    for incoming, target in zip(rows101, expected):
        row = cartan_row(incoming, transfer, 1, IX, axx)
        rank = row["C"].rank()
        norm = sp.simplify(sp.trace(row["C"].H * row["C"]))
        observed101.append((rank, norm))
        dk101 &= row["second_residual"] == ZERO4 and (rank, norm) == target

    rows102 = ((0, -PI / 2), (PI / 2, -PI))
    expected102 = (
        (3, 3, (3 * SQRT2 / 4, -3 * SQRT2 / 4), sp.Rational(9, 8), I),
        (7, 7, (SQRT2 / 4, -SQRT2 / 4), sp.Rational(1, 8), -I),
    )
    antecedent102 = True
    dk102 = True
    for incoming, target in zip(rows102, expected102):
        outgoing = add2(incoming, transfer)
        mass_in = sp.simplify(axis_mass102(incoming[0]) + axis_mass102(incoming[1]))
        mass_out = sp.simplify(axis_mass102(outgoing[0]) + axis_mass102(outgoing[1]))
        vector = (
            u102(incoming[0], transfer[0]),
            u102(incoming[1], transfer[1]),
        )
        stress = sp.simplify(vector[0] ** 2)
        delta_d = sp.simplify(I * (d102(outgoing[0]) - d102(incoming[0])))
        antecedent102 &= (mass_in, mass_out, vector, stress, delta_d) == target
        row = cartan_row(incoming, transfer, 1, IX, axx)
        norm = sp.simplify(sp.trace(row["C"].H * row["C"]))
        dk102 &= (
            row["second_residual"] == ZERO4
            and row["C"].rank() == 2
            and norm == 1
        )

    if mutation == "hide_block101_escape":
        dk101 = False
    if mutation == "hide_block102_escape":
        dk102 = False
    return {
        "antecedent101": antecedent101,
        "dk101": dk101,
        "observed101": observed101,
        "antecedent102": antecedent102,
        "dk102": dk102,
    }


def shell_and_mixed_hessian_certificate(mutation: str) -> dict[str, object]:
    signature = -1
    _, axx, axt, att = physical_hodge(signature)
    perturbations = (axx, axt, att)
    k_plus = (PI / 2, PI / 2)
    k_minus = (-PI / 2, PI / 2)
    v_plus = sp.Matrix([I, 1, 1, I]) / 2
    v_minus = sp.Matrix([I, -1, 1, -I]) / 2
    m_plus = m_matrix(d_matrix(*k_plus), signature)
    m_minus = m_matrix(d_matrix(*k_minus), signature)
    polarizations = (
        sp.simplify(v_plus.H * v_plus)[0] == 1
        and sp.simplify(v_minus.H * v_minus)[0] == 1
        and sp.simplify(m_plus * v_plus) == sp.zeros(4, 1)
        and sp.simplify(m_minus * v_minus) == sp.zeros(4, 1)
    )

    plus_source = []
    minus_source = []
    cross_zero = True
    for perturbation in perturbations:
        vp = vertex(perturbation, d_matrix(*k_plus), d_matrix(*k_plus))
        vm = vertex(perturbation, d_matrix(*k_minus), d_matrix(*k_minus))
        plus_source.append(sp.simplify((v_plus.H * vp * v_plus)[0]))
        minus_source.append(sp.simplify((v_minus.H * vm * v_minus)[0]))
        forward = vertex(perturbation, d_matrix(*k_plus), d_matrix(*k_minus))
        reverse = vertex(perturbation, d_matrix(*k_minus), d_matrix(*k_plus))
        cross_zero &= sp.simplify((v_minus.H * forward * v_plus)[0]) == 0
        cross_zero &= sp.simplify((v_plus.H * reverse * v_minus)[0]) == 0
    source = (
        tuple(plus_source)
        == (sp.Rational(1, 2), -1, sp.Rational(1, 2))
        and tuple(minus_source)
        == (sp.Rational(1, 2), 1, sp.Rational(1, 2))
        and tuple(sp.simplify(a + b) for a, b in zip(plus_source, minus_source))
        == (1, 0, 1)
    )

    # Execute the common-action mixed functional derivative for a genuine
    # 4x4 Hodge vertex, not an abstract Boolean label.
    zbar = sp.Matrix(sp.symbols("zb0:4"))
    z = sp.Matrix(sp.symbols("z0:4"))
    geometry = sp.symbols("h", real=True)
    v_exact = vertex(axx, d_matrix(PI / 6, -PI / 4), d_matrix(PI / 3, PI / 5))
    action = sp.expand(geometry * (zbar.T * v_exact * z)[0])
    source_functional = sp.diff(action, geometry)
    matter_variation = sp.Matrix([sp.diff(action, item) for item in zbar])
    mixed_hessian = sp.Matrix(
        [sp.diff(source_functional, item) for item in zbar]
    ) == matter_variation.diff(geometry)
    mixed_hessian &= matter_variation.diff(geometry) == v_exact * z

    if mutation == "fake_shell_source":
        source = False
    return {
        "polarizations": polarizations,
        "plus": tuple(plus_source),
        "minus": tuple(minus_source),
        "source": source,
        "cross_zero": cross_zero,
        "mixed_hessian": mixed_hessian,
    }


def cyclic_radius(matrix: sp.Matrix) -> int:
    size = matrix.rows
    radii = []
    for row in range(size):
        for column in range(size):
            if sp.simplify(matrix[row, column]) != 0:
                forward = (row - column) % size
                backward = (column - row) % size
                radii.append(min(forward, backward))
    return max(radii, default=0)


def quadratic_locality_certificate(mutation: str) -> dict[str, object]:
    # Generic noncommutative 2x2 Taylor check.
    epsilon = sp.symbols("epsilon", real=True)
    h_symbols = sp.symbols("h0:4", real=True)
    a_symbols = sp.symbols("a0:4", real=True)
    b_symbols = sp.symbols("b0:4", real=True)
    u_symbols = sp.symbols("u0:4", real=True)
    h_base = sp.Matrix(2, 2, h_symbols)
    a = sp.Matrix(2, 2, a_symbols)
    b = sp.Matrix(2, 2, b_symbols)
    u = sp.Matrix(2, 2, u_symbols)
    transform = sp.eye(2) - epsilon * u + epsilon**2 * u**2 / 2
    site = h_base + epsilon * a + epsilon**2 * b / 2
    orbit = (transform.T * site * transform).applyfunc(sp.expand)
    h1 = a - u.T * h_base - h_base * u
    h2 = (
        b / 2
        - u.T * a
        - a * u
        + (u.T**2) * h_base / 2
        + u.T * h_base * u
        + h_base * (u**2) / 2
    )
    taylor = True
    for row in range(2):
        for column in range(2):
            taylor &= sp.expand(orbit[row, column]).coeff(epsilon, 1) == sp.expand(
                h1[row, column]
            )
            taylor &= sp.expand(orbit[row, column]).coeff(epsilon, 2) == sp.expand(
                h2[row, column]
            )

    # Nilpotency makes every Cartan generator commute with d, so the same
    # conjugation closes M(H)=Hd+d^dagger H through the Taylor order.
    sx, st, xi_x, xi_t = sp.symbols("sx st xi_x xi_t", real=True)
    differential = I * (sx * EX + st * ET)
    contraction = xi_x * IX + xi_t * IT
    cartan = sp.simplify(differential * contraction + contraction * differential)
    commutator = sp.simplify(differential * cartan - cartan * differential)

    # Exact radius-growth witness in the 0-form block of the full
    # degree-preserving Cartan generator on an L=7 ring.  This block isolates
    # the support coefficient; the complete Cartan operator, checked above,
    # is what commutes with d.
    length = 7
    derivative = sp.zeros(length)
    for index in range(length):
        derivative[index, (index + 1) % length] = sp.Rational(1, 2)
        derivative[index, (index - 1) % length] = -sp.Rational(1, 2)
    xi_values = sp.symbols("x0:7", real=True)
    xi = sp.diag(*xi_values)
    local_u = xi * derivative
    local_h1 = sp.simplify(-(local_u.T + local_u))
    local_h2 = sp.simplify(
        ((local_u.T) ** 2 + 2 * local_u.T * local_u + local_u**2) / 2
    )
    symbolic_distance_two = all(
        sp.simplify(
            local_h2[index, (index + 2) % length]
            - xi_values[(index + 1) % length]
            * (
                xi_values[index]
                - 2 * xi_values[(index + 1) % length]
                + xi_values[(index + 2) % length]
            )
            / 8
        )
        == 0
        for index in range(length)
    )
    delta_substitution = {value: 0 for value in xi_values}
    delta_substitution[xi_values[1]] = 1
    delta_h2 = local_h2.subs(delta_substitution)
    distance_two = (
        delta_h2[0, 2] == -sp.Rational(1, 4)
        and delta_h2[2, 0] == -sp.Rational(1, 4)
        and cyclic_radius(local_h1.subs(delta_substitution)) == 1
        and cyclic_radius(delta_h2) == 2
    )
    if mutation in ("delete_distance_two", "claim_radius_one_closure"):
        distance_two = False
    return {
        "taylor": taylor,
        "cartan_commutator": commutator,
        "symbolic_distance_two": symbolic_distance_two,
        "distance_two": distance_two,
        "h1_radius": cyclic_radius(local_h1.subs(delta_substitution)),
        "h2_radius": cyclic_radius(delta_h2),
        "entry": delta_h2[0, 2],
    }


def os_factorization_certificate(mutation: str) -> dict[str, object]:
    tolerance = 2e-12
    cases = ((0.5, 0.0), (0.5, 0.6), (0.75, -0.8))
    max_error = 0.0
    minimum = float("inf")
    ranks = []
    for mass, lam in cases:
        radius = float(np.hypot(mass, lam))
        energy = float(np.arcsinh(radius))
        zeta = float(np.exp(-2 * energy))
        amplitude = complex(mass, lam)
        even = np.array([[-2 * amplitude, 1], [1, 0]], dtype=complex)
        transfer2 = even.conj().T @ even
        target_transfer = np.array([zeta, 1 / zeta])
        max_error = max(
            max_error,
            float(np.max(np.abs(np.sort(np.linalg.eigvalsh(transfer2)) - target_transfer))),
        )

        denominator = zeta - 1 / zeta
        gram = np.array(
            [
                [2 * (zeta - 1), -4 * zeta * amplitude],
                [-4 * zeta * amplitude.conjugate(), 2 * zeta * (zeta - 1)],
            ],
            dtype=complex,
        ) / denominator
        phase = amplitude / radius
        vector = np.array([1, np.sqrt(zeta) * phase.conjugate()]) / np.sqrt(
            1 + zeta
        )
        factor = np.sqrt(2 * zeta) * vector.conjugate()[None, :]
        max_error = max(max_error, float(np.max(np.abs(gram - factor.conj().T @ factor))))
        eigenvalues = np.linalg.eigvalsh(gram)
        max_error = max(
            max_error,
            float(np.max(np.abs(eigenvalues - np.array([0, 2 * zeta])))),
        )

        gram4 = np.kron(np.eye(2), gram)
        factor4 = np.kron(np.eye(2), factor)
        spatial = np.kron(
            np.eye(2) + 0.2 * np.array([[0, 1], [-1, 0]], dtype=float),
            np.eye(2),
        )
        pulled = spatial.conj().T @ gram4 @ spatial
        pulled_factor = factor4 @ spatial
        max_error = max(
            max_error,
            float(np.max(np.abs(pulled - pulled_factor.conj().T @ pulled_factor))),
        )
        pulled_eigenvalues = np.linalg.eigvalsh(pulled)
        minimum = min(minimum, float(np.min(pulled_eigenvalues)))
        ranks.append(int(np.sum(pulled_eigenvalues > tolerance)))
    passed = max_error < tolerance and minimum > -tolerance and ranks == [2, 2, 2]
    if mutation == "break_os_factorization":
        passed = False
    return {
        "passed": passed,
        "max_error": max_error,
        "minimum": minimum,
        "ranks": ranks,
        "scope": "spatial-pullback-free-massive-two-step-conditional",
    }


def scope_certificate(mutation: str) -> dict[str, bool]:
    note = " ".join(NOTE_PATH.read_text(encoding="utf-8").lower().split())
    result = {
        "minimal": "minimal degree-closed 0+1+2 two-plane carrier" in note,
        "connection": "operator-valued edge-hodge connection" in note,
        "block98": "all 24 block 98 alias pairs" in note,
        "block101": "block 101 five-row obstruction" in note,
        "block102": "block 102 two-row contradiction" in note,
        "radius": "radius two is necessary" in note,
        "quadratic": "finite through quadratic order" in note,
        "not_all_order": "not an all-order bounded-locality theorem" in note,
        "os": "conditional spatial two-step os factorization" in note,
        "temporal_open": "temporal-link os remains unexecuted" in note,
        "full4d_open": "full four-dimensional carrier remains unexecuted" in note,
        "joint_rp_open": "joint gravity reflection positivity remains unexecuted" in note,
        "embedding_open": "site possibility and record embedding remains an obligation" in note,
        "energy_open": "total discrete energy remains unexecuted" in note,
        "not_01_no_go": "not a 0+1 cochain no-go" in note,
        "n1_n8": all(f"n{index}" in note for index in range(1, 9)),
        "n2_pairwise": "w1 closes w2?" in note and "w2 closes w1?" in note,
        "n7_steelmen": "hostile steelman against w1" in note
        and "hostile steelman against w2" in note,
        "os_provenance": "free_staggered_3plus1_reflected_gram_car_fock_representation_bounded_theorem_note_2026-07-12.md"
        in note
        and "content-binds its source note, runner, and cache" in note,
        "axiom_unchanged": "no axiom amendment is justified" in note,
        "zero_retirement": "zero obligation retirement" in note,
        "zero_score": "no toe percentage moves" in note,
        "zero_e2e": "retained-positive end-to-end theory count remains zero" in note,
        "advance": "advance the radius-two degree-closed hodge carrier" in note,
    }
    if mutation == "claim_temporal_os":
        result["temporal_open"] = False
    if mutation == "weaken_no_go_packet":
        result["n1_n8"] = False
    if mutation == "claim_axiom_update":
        result["axiom_unchanged"] = False
    if mutation == "claim_toe_progress":
        result["zero_score"] = False
    if mutation == "claim_obligation_retirement":
        result["zero_retirement"] = False
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mutation",
        choices=(
            "stale_axiom_authority",
            "stale_os_authority",
            "drop_two_form",
            "flip_koszul_sign",
            "omit_hodge_response",
            "hide_block98_alias",
            "hide_block101_escape",
            "hide_block102_escape",
            "fake_shell_source",
            "delete_distance_two",
            "claim_radius_one_closure",
            "break_os_factorization",
            "claim_temporal_os",
            "weaken_no_go_packet",
            "claim_axiom_update",
            "claim_toe_progress",
            "claim_obligation_retirement",
        ),
        default="",
    )
    mutation = parser.parse_args().mutation
    checks = Checks()

    authority = authority_certificate(mutation)
    checks.check(
        "A-current-authority-Block102-parent-and-OS-source",
        "current axiom authority, exact stacked Block102 parent, and supplied-Gram source triple are content-bound",
        authority["origin_main"] == CURRENT_MAIN
        and authority["axiom"] == authority["expected_axiom"]
        and authority["worktree_axiom"] == CURRENT_AXIOM_BLOB
        and authority["registry"] == CURRENT_REGISTRY_BLOB
        and authority["worktree_registry"] == PARENT_REGISTRY_BLOB
        and authority["parent"] == PARENT_COMMIT
        and authority["parent_ancestor"]
        and authority["parent_note"] == PARENT_NOTE_BLOB
        and authority["parent_runner"] == PARENT_RUNNER_BLOB
        and authority["parent_cache"] == PARENT_CACHE_BLOB
        and authority["os_note"] == authority["expected_os_note"]
        and authority["os_runner"] == OS_SOURCE_RUNNER_BLOB
        and authority["os_cache"] == OS_SOURCE_CACHE_BLOB
        and authority["worktree_os_note"] == OS_SOURCE_NOTE_BLOB
        and authority["worktree_os_runner"] == OS_SOURCE_RUNNER_BLOB
        and authority["worktree_os_cache"] == OS_SOURCE_CACHE_BLOB,
        f"origin/main={str(authority['origin_main'])[:10]}; parent={str(authority['parent'])[:10]}; OS source={str(authority['os_note'])[:10]}",
    )

    exterior = exterior_and_hodge_certificate(mutation)
    checks.check(
        "B-minimal-degree-closed-carrier-and-physical-Hodge",
        "the full 0+1+2 two-plane exterior algebra is Clifford closed, while its 0+1 projection has one generic null direction",
        exterior["algebra"]
        and all(exterior["full"].values())
        and all(exterior["projected"].values())
        and exterior["clifford_norm"]
        and exterior["physical_hodge"]
        and exterior["generic_rank"] == 3
        and exterior["shell_rank"] == 2,
        f"det M=(sx^2+eps st^2)^2; physical Hodge vertex ranks generic/shell={exterior['generic_rank']}/{exterior['shell_rank']}",
    )

    cartan = cartan_ward_certificate(mutation)
    checks.check(
        "C-exact-Cartan-Hodge-first-and-constant-translation-order-h-Ward",
        "Cartan transport closes the first Ward coefficient for both signatures and the complete constant-translation order-h coefficient",
        cartan["exact"]
        and cartan["reversal"]
        and cartan["constant"]
        and cartan["nilpotent"]
        and cartan["order_h"],
        "[d,D]=0; R_H=-Drev^dag H-HD; reversal and constant sin(k) translations exact",
    )

    block98 = block98_certificate(mutation)
    checks.check(
        "D-all-Block98-aliases-cancel-in-matrix-Hodge-carrier",
        "all 24 scalar alias pairs remain exact antecedents while all 48 matrix-Hodge rows cancel by one response identity",
        block98["pairs"] == 24
        and block98["rows"] == 48
        and block98["scalar_aliases"]
        and block98["dk_rows"]
        and block98["reflected_response"]
        and block98["ranks"] == {2}
        and block98["norms"] == {sp.Rational(1, 2)},
        f"pairs/rows={block98['pairs']}/{block98['rows']}; rank(C)={block98['ranks']}; ||C||_F^2={block98['norms']}",
    )

    aliases = block101_102_certificate(mutation)
    checks.check(
        "E-Block101-and-Block102-obstructions-erase-identically",
        "the exact scalar inconsistency fixtures are reproduced before the degree-closed Hodge carrier cancels every corresponding row",
        aliases["antecedent101"]
        and aliases["dk101"]
        and aliases["antecedent102"]
        and aliases["dk102"],
        f"Block101 DK rank/norm rows={aliases['observed101']}; Block102 two rows rank=2,norm^2=1",
    )

    shell = shell_and_mixed_hessian_certificate(mutation)
    checks.check(
        "F-Lorentz-shell-source-cross-cancellation-and-mixed-Hessian",
        "exact normalized null polarizations give rho=tau=1 and j=0, zero cross terms, and common-action source/matter reciprocity",
        shell["polarizations"]
        and shell["source"]
        and shell["cross_zero"]
        and shell["mixed_hessian"],
        f"T+={shell['plus']}; T-={shell['minus']}; sum=(1,0,1)",
    )

    locality = quadratic_locality_certificate(mutation)
    checks.check(
        "G-quadratic-Hodge-closure-and-necessary-radius-two",
        "the exact conjugation Taylor coefficients close through second order and a distance-two coefficient forbids fixed radius-one closure",
        locality["taylor"]
        and locality["cartan_commutator"] == ZERO4
        and locality["symbolic_distance_two"]
        and locality["distance_two"]
        and locality["h1_radius"] == 1
        and locality["h2_radius"] == 2
        and locality["entry"] == -sp.Rational(1, 4),
        f"H1/H2 radii={locality['h1_radius']}/{locality['h2_radius']}; H2[0,2]={locality['entry']}",
    )

    os_gate = os_factorization_certificate(mutation)
    checks.check(
        "H-source-bound-spatial-two-step-Gram-congruence",
        "the content-bound supplied free Gram is A^dag A and remains positive under a purely spatial cochain congruence",
        os_gate["passed"]
        and os_gate["scope"] == "spatial-pullback-free-massive-two-step-conditional",
        f"all identities and eigenvalue bounds within tol=2e-12; ranks={os_gate['ranks']}",
    )

    scope = scope_certificate(mutation)
    checks.check(
        "I-scope-no-go-discipline-and-TOE-firewall",
        "N1-N8 preserve full-4D, temporal-link, joint-gravity, embedding, energy, axiom, audit, and TOE obligations",
        all(scope.values()),
    )

    print(
        f"AXIOM_AUTHORITY: origin/main={authority['origin_main']} axiom={CURRENT_AXIOM_BLOB}; Block102 parent={PARENT_COMMIT}"
    )
    print(
        "per_element: exact exterior/Koszul algebra, physical Hodge derivatives, phased Cartan response, Taylor coefficients, and source-bound Gram factors"
    )
    print(
        "per_site: the two-plane carrier dimension is checked; physical fine-site and Record embedding are not executed"
    )
    print(
        "per_mode: all 48 Block98 rows, five Block101 rows, two Block102 rows, and the Lorentz L4 shell cancel or source exactly as declared"
    )
    print(
        "per_block: one Hodge action closes the first Ward term, constant-translation order-h term, and O(h^2) support with radius growth 1->2"
    )
    print(
        "lattice_wide: checked and not executed — full 4D, temporal/dynamic and joint-gravity OS, constraint reduction, energy, Records, selection, adoption, and retention remain open"
    )
    print(
        "RESULT: the degree-closed 0+1+2 two-plane Dirac-Kahler/Hodge carrier erases every executed scalar nonlinear Ward alias by identity and has a finite radius-two quadratic completion"
    )
    print(
        "DECISION_CUT: advance the radius-two degree-closed Hodge carrier first to a same-action reflected-Gram/equivalence gate, then the actual ADM history transporter; stop scalar rank-one work inside Block102's declared class"
    )
    print(
        "TOE: zero obligation retirement, zero retained-positive end-to-end theories, and no percentage movement"
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
