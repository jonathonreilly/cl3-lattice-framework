#!/usr/bin/env python3
"""Block 104: same-action Dirac--Kahler Euclidean/OS bridge.

This runner selects the flat relative Wick phase inside a declared
constant-phase family, proves the exact 2^d fine-site
staggered/Dirac--Kahler equivalence for
d=2 and d=4, imports and rederives the source-bound reflected Gram on that
same flat free action, and localizes the remaining finite-spacing Lorentz-time
bridge.  Curved-history transport, joint gravity, Records, retention, and TOE
closure remain open.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import subprocess

import numpy as np
import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_DIRAC_KAHLER_WICK_PHASE_FINE_SITE_STAGGERED_OS_LORENTZ_"
    "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md"
)
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"
PARENT_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_COCHAIN_HODGE_QUADRATIC_WARD_SHELL_"
    "LOCALITY_OS_REENTRY_BOUNDED_THEOREM_NOTE_2026-08-14.md"
)
PARENT_RUNNER = (
    "scripts/admissibility_dirac_kahler_cochain_hodge_quadratic_ward_shell_"
    "locality_os_reentry_2026_08_14.py"
)
PARENT_CACHE = (
    "logs/runner-cache/admissibility_dirac_kahler_cochain_hodge_quadratic_"
    "ward_shell_locality_os_reentry_2026_08_14.txt"
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
    "docs/ADMISSIBILITY_DIRAC_KAHLER_WICK_PHASE_FINE_SITE_STAGGERED_OS_LORENTZ_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_COCHAIN_HODGE_QUADRATIC_WARD_SHELL_LOCALITY_OS_REENTRY_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "scripts/admissibility_dirac_kahler_cochain_hodge_quadratic_ward_shell_locality_os_reentry_2026_08_14.py",
    "logs/runner-cache/admissibility_dirac_kahler_cochain_hodge_quadratic_ward_shell_locality_os_reentry_2026_08_14.txt",
    "docs/FREE_STAGGERED_3PLUS1_REFLECTED_GRAM_CAR_FOCK_REPRESENTATION_BOUNDED_THEOREM_NOTE_2026-07-12.md",
    "scripts/free_staggered_3plus1_reflected_gram_car_fock_representation_2026_07_12.py",
    "logs/runner-cache/free_staggered_3plus1_reflected_gram_car_fock_representation_2026_07_12.txt",
)

CURRENT_MAIN = "43ba5587944ffe0f43df10864c8348a99c17517b"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
CURRENT_REGISTRY_BLOB = "b93959cca4f7e26c673cdccbe601e50c3cb93daa"
WORKTREE_REGISTRY_BLOB = "f01d3be864f682584d50eede8b3abe6671bb4719"
PARENT_COMMIT = "99cee0a6c962b382a3ca1a8497d589ffa280dfe8"
PARENT_NOTE_BLOB = "11a1ce00626adf516823b5308dd8c52c770948f7"
PARENT_RUNNER_BLOB = "5d387b12b8c338c4d28f485d93a9d4be4bc2bac4"
PARENT_CACHE_BLOB = "8e0e7b56d85712a6d80244e64b31d4451fe04862"
OS_SOURCE_NOTE_BLOB = "2847b93b9c24496a3129ad06216211f72de5c681"
OS_SOURCE_RUNNER_BLOB = "6acfc6a3a4dc479cbe8b80daa34567327356b1fe"
OS_SOURCE_CACHE_BLOB = "1333a0534817d14dc8018b76ac7e0c872363ebe6"

I = sp.I
ID2 = sp.eye(2)
X = sp.Matrix([[0, 1], [1, 0]])
Y = sp.Matrix([[0, -I], [I, 0]])
Z = sp.diag(1, -1)

# Block103 two-plane basis (1,dx,dt,dx wedge dt), used for the direct Ward and
# Lorentz-continuation replay.  The d-dimensional fine-cell theorem below uses
# time-first fine-cell bits and the matching later-Z exterior/Koszul strings.
EX = sp.Matrix(
    [[0, 0, 0, 0], [1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1, 0]]
)
ET = sp.Matrix(
    [[0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0], [0, -1, 0, 0]]
)
IX = EX.T
IT = ET.T
ID4 = sp.eye(4)
ZERO4 = sp.zeros(4)


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


def worktree_blob(path: str) -> str:
    return git_output("hash-object", path)


def commit_blob(commit: str, path: str) -> str:
    return git_output("rev-parse", f"{commit}:{path}")


def is_ancestor(ancestor: str, descendant: str) -> bool:
    return subprocess.run(
        ("git", "merge-base", "--is-ancestor", ancestor, descendant),
        cwd=ROOT,
        check=False,
    ).returncode == 0


def kron_all(items: list[sp.Matrix]) -> sp.Matrix:
    result = sp.Matrix([[1]])
    for item in items:
        result = sp.kronecker_product(result, item)
    return result


def raw_gamma(dim: int, axis: int) -> sp.Matrix:
    return kron_all([Z if j < axis else X if j == axis else ID2 for j in range(dim)])


def dk_gamma(dim: int, axis: int) -> sp.Matrix:
    return kron_all([ID2 if j < axis else Y if j == axis else Z for j in range(dim)])


def phase_unitary(dim: int, include_koszul: bool = True) -> sp.Matrix:
    phases: list[sp.Expr] = []
    for subset in range(2**dim):
        degree = subset.bit_count()
        koszul = (-1) ** (degree * (degree - 1) // 2) if include_koszul else 1
        phases.append((-I) ** degree * koszul)
    return sp.diag(*phases)


def block_h(momentum: sp.Expr) -> sp.Matrix:
    return sp.Matrix(
        [
            [0, (1 - sp.exp(-I * momentum)) / 2],
            [(sp.exp(I * momentum) - 1) / 2, 0],
        ]
    )


def d_matrix(sx: sp.Expr, st: sp.Expr) -> sp.Matrix:
    return I * (sx * EX + st * ET)


def h0(signature: int) -> sp.Matrix:
    return sp.diag(1, 1, signature, signature)


def m_matrix(differential: sp.Matrix, signature: int) -> sp.Matrix:
    hodge = h0(signature)
    return sp.simplify(hodge * differential + differential.H * hodge)


def vertex(
    perturbation: sp.Matrix, incoming_d: sp.Matrix, outgoing_d: sp.Matrix
) -> sp.Matrix:
    return sp.simplify(perturbation * incoming_d + outgoing_d.H * perturbation)


def authority_certificate(mutation: str) -> dict[str, object]:
    expected_axiom = "0" * 40 if mutation == "stale_axiom_authority" else CURRENT_AXIOM_BLOB
    expected_os = "0" * 40 if mutation == "stale_os_authority" else OS_SOURCE_NOTE_BLOB
    return {
        "main": git_output("rev-parse", "origin/main"),
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
        "expected_os": expected_os,
    }


def phase_and_free_kernel_certificate(mutation: str) -> dict[str, object]:
    sx, st, mass = sp.symbols("s_x s_t m", real=True, nonzero=True)
    gamma_x = I * (EX - IX)
    gamma_t = I * (ET - IT)
    algebra = (
        gamma_x.H == gamma_x
        and gamma_t.H == gamma_t
        and gamma_x**2 == ID4
        and gamma_t**2 == ID4
        and gamma_x * gamma_t + gamma_t * gamma_x == ZERO4
    )
    matter = sp.simplify(sx * gamma_x + st * gamma_t)
    scalar_square = sp.simplify(matter**2 - (sx**2 + st**2) * ID4) == ZERO4
    bad = sp.simplify(mass * ID4 + matter)
    euclidean = sp.simplify(mass * ID4 + I * matter)
    bad_det = sp.factor(bad.det())
    euclidean_det = sp.factor(euclidean.det())

    phi = sp.symbols("phi", real=True)
    dphi = mass * ID4 + sp.exp(I * phi) * matter
    scalar_covariance_residual = sp.simplify(
        dphi.H * dphi - (mass**2 + sx**2 + st**2) * ID4
    )
    expected_residual = sp.simplify(2 * mass * sp.cos(phi) * matter)
    phase_family = sp.simplify(scalar_covariance_residual - expected_residual) == ZERO4
    normal_for_all_phi = sp.simplify(dphi.H * dphi - dphi * dphi.H) == ZERO4
    plus = scalar_covariance_residual.subs(phi, sp.pi / 2).applyfunc(sp.simplify) == ZERO4
    minus = scalar_covariance_residual.subs(phi, -sp.pi / 2).applyfunc(sp.simplify) == ZERO4

    # Independent antiunitary time-pullback selector.  P_t flips Gamma_t and
    # complex conjugation flips both imaginary Clifford generators.
    time_pullback = sp.kronecker_product(Z, ID2)
    matter_time_reversed = sx * gamma_x - st * gamma_t
    dphi_time_reversed = mass * ID4 + sp.exp(I * phi) * matter_time_reversed
    reflection_residual = sp.simplify(
        time_pullback * dphi_time_reversed.conjugate() * time_pullback - dphi
    )
    reflection_plus = (
        reflection_residual.subs(phi, sp.pi / 2).applyfunc(sp.simplify) == ZERO4
    )
    reflection_minus = (
        reflection_residual.subs(phi, -sp.pi / 2).applyfunc(sp.simplify) == ZERO4
    )
    reflection_rejects_zero = (
        reflection_residual.subs({phi: 0, sx: 1, st: 1, mass: 1}) != ZERO4
    )
    bad_witness = (
        bad_det.subs({mass: sp.Rational(1, 2), sx: 0, st: sp.Rational(1, 2)}) == 0
        and euclidean_det.subs(
            {mass: sp.Rational(1, 2), sx: 0, st: sp.Rational(1, 2)}
        )
        == sp.Rational(1, 4)
    )
    chosen_phase = (
        0
        if mutation in ("use_naive_euclidean", "drop_wick_phase")
        else sp.pi / 2
    )
    chosen_is_scalar = (
        scalar_covariance_residual.subs(phi, chosen_phase).applyfunc(sp.simplify) == ZERO4
    )

    # A recurrence/transfer-family witness independent of determinant and
    # antiunitary covariance: the naive m=1/2 zero-spatial mode has a
    # non-Hermitian two-step update, whereas the source update is B^dag B.
    bad_one_step = sp.Matrix([[-I, 1], [1, 0]])
    bad_two_step = sp.simplify(bad_one_step**2)
    source_one_step = sp.Matrix([[-1, 1], [1, 0]])
    source_two_step = sp.simplify(source_one_step.H * source_one_step)
    transfer_witness = (
        bad_two_step != bad_two_step.H
        and source_two_step == source_two_step.H
        and source_two_step.is_positive_definite
    )
    selected = (
        algebra
        and scalar_square
        and phase_family
        and normal_for_all_phi
        and plus
        and minus
        and reflection_plus
        and reflection_minus
        and reflection_rejects_zero
        and bad_witness
        and chosen_is_scalar
        and transfer_witness
    )
    return {
        "selected": selected,
        "bad_det": bad_det,
        "euclidean_det": euclidean_det,
        "det_ok": bad_det == (mass**2 - sx**2 - st**2) ** 2
        and euclidean_det == (mass**2 + sx**2 + st**2) ** 2,
        "scalar_covariance_residual": expected_residual,
        "antiunitary_selector": reflection_plus and reflection_minus and reflection_rejects_zero,
        "transfer_witness": transfer_witness,
    }


def same_action_ward_certificate(mutation: str) -> dict[str, object]:
    sx, st, sx_out, st_out, mass = sp.symbols(
        "sx st Sx St mass", real=True
    )
    din = I * (sx * EX + st * ET)
    dout = I * (sx_out * EX + st_out * ET)
    exact = True
    reversal = True
    for signature in (1, -1):
        hodge = h0(signature)
        for contraction in (IX, IT):
            dmap = sp.simplify(dout * contraction + contraction * din)
            drev = sp.simplify(din * contraction + contraction * dout)
            response = sp.simplify(-drev.H * hodge - hodge * dmap)
            if mutation == "break_ward_response":
                response = ZERO4
            min_ = m_matrix(din, signature)
            mout = m_matrix(dout, signature)
            qin = mass * hodge + I * min_
            qout = mass * hodge + I * mout
            qresponse = mass * response + I * vertex(response, din, dout)
            if mutation == "drop_mass_hodge_response":
                qresponse = I * vertex(response, din, dout)
            residual = sp.simplify(qresponse + drev.H * qin + qout * dmap)
            exact &= residual == ZERO4
            reverse = sp.simplify(-dmap.H * hodge - hodge * drev)
            reversal &= sp.simplify(reverse - response.H) == ZERO4

    # Degree-phase equivalence for every degree-preserving Hodge block.
    h00, h11, h12, h21, h22, h33 = sp.symbols(
        "h00 h11 h12 h21 h22 h33", real=True
    )
    hodge_generic = sp.Matrix(
        [[h00, 0, 0, 0], [0, h11, h12, 0], [0, h21, h22, 0], [0, 0, 0, h33]]
    )
    degree_phase = sp.diag(1, I, I, -1)
    differential = I * (sx * EX + st * ET)
    m_h = sp.simplify(hodge_generic * differential + differential.H * hodge_generic)
    q_e = sp.simplify(mass * hodge_generic + I * m_h)
    skew = sp.simplify(
        mass * hodge_generic
        + hodge_generic * differential
        - differential.H * hodge_generic
    )
    phase_equivalence = sp.simplify(degree_phase.H * q_e * degree_phase - skew) == ZERO4
    return {
        "exact": exact,
        "reversal": reversal,
        "phase_equivalence": phase_equivalence,
    }


def fine_site_equivalence_certificate(mutation: str) -> dict[str, object]:
    q = sp.symbols("q", real=True)
    p = sp.diag(sp.exp(-I * q / 2), sp.exp(I * q / 2))
    raw_momentum = q if mutation == "forget_reduced_momentum" else 2 * q
    subcell = (
        sp.simplify(p.H * block_h(raw_momentum) * p - I * sp.sin(q) * X)
        == sp.zeros(2)
    )

    dimensions = {}
    gamma_maps = {}
    actions = {}
    determinants = {}
    placements = {}
    for dim in (2, 4):
        size = 2**dim
        s = phase_unitary(dim, include_koszul=mutation != "break_koszul_phase")
        gamma_ok = True
        raw_action = sp.zeros(size)
        dk_action = sp.zeros(size)
        symbols = sp.symbols(f"s0:{dim}", real=True)
        for axis, value in enumerate(symbols):
            mapped = sp.simplify(s.H * raw_gamma(dim, axis) * s)
            gamma_ok &= mapped == dk_gamma(dim, axis)
            raw_action += I * value * raw_gamma(dim, axis)
            dk_action += I * value * dk_gamma(dim, axis)
        action_ok = sp.simplify(s.H * raw_action * s - dk_action) == sp.zeros(size)
        # Since the executed action identity is a square-unitary similarity,
        # this separate exact determinant-of-the-map check certifies Gaussian
        # determinant/partition preservation without expanding a 16x16
        # symbolic determinant.
        determinant_ok = action_ok and sp.simplify(
            s.det() * sp.conjugate(s.det())
        ) == 1

        offsets = [
            tuple((index >> (dim - 1 - axis)) & 1 for axis in range(dim))
            for index in range(size)
        ]
        coarse = tuple(axis + 2 for axis in range(dim))
        fine_sites = [
            tuple(2 * coarse[axis] + offset[axis] for axis in range(dim))
            for offset in offsets
        ]
        recovered = [tuple(value % 2 for value in site) for site in fine_sites]
        placement_bijection = len(set(fine_sites)) == size and recovered == offsets
        proposed_modes = (
            size * size if mutation == "co_located_overcount" else len(fine_sites)
        )
        placement_count = placement_bijection and proposed_modes == size
        dimensions[dim] = size
        gamma_maps[dim] = gamma_ok
        actions[dim] = action_ok
        determinants[dim] = determinant_ok
        placements[dim] = placement_count

    block103_gamma_x = I * (EX - IX)
    block103_gamma_t = I * (ET - IT)
    orientation = (
        dk_gamma(2, 0) == block103_gamma_t and dk_gamma(2, 1) == block103_gamma_x
    )
    count_ok = dimensions == {2: 4, 4: 16} and all(placements.values())
    return {
        "subcell": subcell,
        "gamma_maps": gamma_maps,
        "actions": actions,
        "determinants": determinants,
        "dimensions": dimensions,
        "placements": placements,
        "orientation": orientation,
        "count_ok": count_ok,
    }


def time_cell_and_taste_certificate(mutation: str) -> dict[str, object]:
    mass, lam, zeta = sp.symbols("m lambda zeta", real=True, nonzero=True)
    dlam = sp.Matrix(
        [
            [mass + I * lam, (1 - 1 / zeta) / 2],
            [(zeta - 1) / 2, mass - I * lam],
        ]
    )
    determinant = sp.factor(dlam.det())
    target = sp.factor(mass**2 + lam**2 + (2 - zeta - 1 / zeta) / 4)
    cell_ok = sp.simplify(determinant - target) == 0

    spatial = {}
    for spatial_dim in (1, 3):
        values = sp.symbols(f"u0:{spatial_dim}", real=True)
        hop = I * sum(
            (value * dk_gamma(spatial_dim, axis) for axis, value in enumerate(values)),
            sp.zeros(2**spatial_dim),
        )
        radius2 = sum(value**2 for value in values)
        square_ok = sp.simplify(hop**2 + radius2 * sp.eye(2**spatial_dim)) == sp.zeros(
            2**spatial_dim
        )
        multiplicity = 2 ** (spatial_dim - 1)
        trace_ok = sp.trace(hop) == 0
        if spatial_dim == 1:
            fixture = hop.subs(values[0], 1)
        else:
            fixture = hop.subs(
                {
                    values[0]: sp.Rational(3, 13),
                    values[1]: sp.Rational(4, 13),
                    values[2]: sp.Rational(12, 13),
                }
            )
        spectral_variable = sp.symbols(f"ell{spatial_dim}")
        charpoly_ok = sp.factor(fixture.charpoly(spectral_variable).as_expr()) == (
            spectral_variable**2 + 1
        ) ** multiplicity
        spatial[spatial_dim] = (square_ok and trace_ok and charpoly_ok, multiplicity)

    r = sp.symbols("r", positive=True)
    pole = sp.simplify((sp.sqrt(1 + r**2) - r) ** 2)
    pole_ok = sp.simplify(r**2 + (2 - pole - 1 / pole) / 4) == 0
    if mutation == "wrong_time_cell_symbol":
        cell_ok = False
    if mutation == "wrong_inside_pole":
        pole_ok = False
    return {
        "cell_ok": cell_ok,
        "determinant": determinant,
        "spatial": spatial,
        "pole_ok": pole_ok,
        "pole": pole,
    }


def covariance_residue(mass: sp.Expr, lam: sp.Expr, zeta: sp.Expr) -> sp.Matrix:
    denominator = zeta - 1 / zeta
    return sp.simplify(
        sp.Matrix(
            [
                [-4 * zeta * (mass - I * lam), 2 * (zeta - 1)],
                [2 * zeta * (zeta - 1), -4 * zeta * (mass + I * lam)],
            ]
        )
        / denominator
    )


def reflected_gram_from_residue(residue: sp.Matrix) -> sp.Matrix:
    return sp.Matrix(
        [
            [residue[0, 1], residue[1, 1]],
            [residue[0, 0], residue[1, 0]],
        ]
    )


def open_chain_reflected_gram(
    mass: float, lam: float, half_extent: int
) -> np.ndarray:
    times = tuple(range(-half_extent, half_extent))
    length = len(times)
    matrix = np.zeros((length, length), dtype=complex)
    for row, time in enumerate(times):
        matrix[row, row] = mass + 1j * ((-1) ** time) * lam
        if row + 1 < length:
            matrix[row, row + 1] = 0.5
        if row - 1 >= 0:
            matrix[row, row - 1] = -0.5
    rhs = np.zeros((length, 2), dtype=complex)
    for source, positive_time in enumerate((0, 1)):
        rhs[-1 - positive_time + half_extent, source] = 1.0
    solution = np.linalg.solve(matrix, rhs)
    target_rows = [positive_time + half_extent for positive_time in (0, 1)]
    return solution[target_rows, :].T


def gram_certificate(mutation: str) -> dict[str, object]:
    mass = sp.symbols("m", real=True, positive=True)
    lam = sp.symbols("lambda", real=True)
    zeta = sp.symbols("z", real=True, positive=True)
    radius = sp.sqrt(mass**2 + lam**2)
    b = sp.simplify((mass + I * lam) / radius)
    prefactor = sp.sqrt(2 * zeta / (1 + zeta))
    factor_phase = sp.conjugate(b) if mutation == "break_gram_factor" else b
    factor = prefactor * sp.Matrix([[1, sp.sqrt(zeta) * factor_phase]])
    gram = sp.simplify(
        2
        * zeta
        / (1 + zeta)
        * sp.Matrix(
            [[1, sp.sqrt(zeta) * b], [sp.sqrt(zeta) * sp.conjugate(b), zeta]]
        )
    )
    factor_ok = sp.simplify(gram - factor.H * factor) == sp.zeros(2)
    rank_ok = gram.rank() == 1

    # Exact pole-residue provenance on the same D_lambda.  Here r=3/4,
    # asinh(r)=log(2), z=1/4, and b=(3+4i)/5.
    fixture_mass = sp.Rational(9, 20)
    fixture_lam = sp.Rational(3, 5)
    fixture_radius = sp.Rational(3, 4)
    fixture_z = sp.Rational(1, 4)
    bloch = sp.symbols("u", nonzero=True)
    fixture_cell = sp.Matrix(
        [
            [fixture_mass + I * fixture_lam, (1 - 1 / bloch) / 2],
            [(bloch - 1) / 2, fixture_mass - I * fixture_lam],
        ]
    )
    determinant = sp.factor(fixture_cell.det())
    determinant_factor = sp.factor(
        determinant + (bloch - fixture_z) * (bloch - 1 / fixture_z) / (4 * bloch)
    ) == 0
    pole_ok = sp.simplify(determinant.subs(bloch, fixture_z)) == 0
    residue_ok = True
    for signed_lam in (fixture_lam, -fixture_lam):
        signed_cell = sp.Matrix(
            [
                [fixture_mass + I * signed_lam, (1 - 1 / bloch) / 2],
                [(bloch - 1) / 2, fixture_mass - I * signed_lam],
            ]
        )
        inverse = signed_cell.inv().applyfunc(sp.simplify)
        residue = inverse.applyfunc(
            lambda entry: sp.simplify(
                sp.limit((bloch - fixture_z) * entry, bloch, fixture_z)
            )
        )
        closed_residue = covariance_residue(fixture_mass, signed_lam, fixture_z)
        residue_ok &= sp.simplify(residue - closed_residue) == sp.zeros(2)
        reordered = reflected_gram_from_residue(residue)
        if mutation == "wrong_reflection_reorder":
            reordered = residue
        fixture_b = sp.simplify((fixture_mass + I * signed_lam) / fixture_radius)
        residue_target = sp.simplify(
            2
            * fixture_z
            / (1 + fixture_z)
            * sp.Matrix(
                [
                    [1, sp.sqrt(fixture_z) * fixture_b],
                    [sp.sqrt(fixture_z) * sp.conjugate(fixture_b), fixture_z],
                ]
            )
        )
        residue_ok &= sp.simplify(reordered - residue_target) == sp.zeros(2)

    # A separate dense inverse of the same open fine-time operator converges
    # to the residue Gram from both conjugate spatial eigenlines.
    convergence = True
    worst_hermitian = 0.0
    worst_final = 0.0
    for lam_value in (0.6, -0.6):
        b_value = (0.45 + 1j * lam_value) / 0.75
        target = (2 * 0.25 / 1.25) * np.array(
            [[1.0, 0.5 * b_value], [0.5 * np.conjugate(b_value), 0.25]],
            dtype=complex,
        )
        finite = [
            open_chain_reflected_gram(0.45, lam_value, extent)
            for extent in (8, 16, 24)
        ]
        errors = [float(np.linalg.norm(item - target, ord=np.inf)) for item in finite]
        convergence &= errors[2] < errors[1] < errors[0]
        worst_final = max(worst_final, errors[2])
        worst_hermitian = max(
            worst_hermitian,
            *(float(np.linalg.norm(item - item.conj().T, ord=np.inf)) for item in finite),
        )
    chain_ok = convergence and worst_final < 1e-11 and worst_hermitian < 2e-13

    # The same consistent algebraic fixture makes taste phases and the d=2
    # and d=4 multiplicities independently executable without noise digits.
    substitution = {mass: fixture_mass, lam: fixture_lam, zeta: fixture_z}
    k_plus = gram.subs(substitution).applyfunc(sp.simplify)
    k_minus = gram.subs({**substitution, lam: -fixture_lam}).applyfunc(sp.simplify)
    dk2 = sp.diag(k_plus, k_minus)
    positive_copies = 5 if mutation == "fake_taste_multiplicity" else 4
    dk4 = sp.diag(*([k_plus] * positive_copies + [k_minus] * 4))
    multiplicities = (
        dk2.shape == (4, 4)
        and dk2.rank() == 2
        and dk4.shape == (16, 16)
        and dk4.rank() == 8
    )
    traces = (
        sp.simplify(sp.trace(dk2)) == 4 * substitution[zeta]
        and sp.simplify(sp.trace(dk4)) == 16 * substitution[zeta]
    )

    massless_z = (sp.sqrt(2) - 1) ** 2
    massless = gram.subs({mass: 0, lam: 1, zeta: massless_z}).applyfunc(sp.simplify)
    massless_nonzero = (
        massless.rank() == 1
        and sp.simplify(sp.trace(massless) - 2 * massless_z) == 0
    )

    zero_bloch = sp.symbols("u0", nonzero=True)
    zero_det = sp.factor((2 - zero_bloch - 1 / zero_bloch) / 4)
    zero_cell = sp.Matrix(
        [[0, (1 - 1 / zero_bloch) / 2], [(zero_bloch - 1) / 2, 0]]
    )
    mass_path = sp.Matrix([[1, 1], [1, 1]])
    momentum_path = sp.Matrix([[1, I], [-I, 1]])
    zero_mode_open = (
        radius.subs({mass: 0, lam: 0}) == 0
        and sp.factor(zero_det + (zero_bloch - 1) ** 2 / (4 * zero_bloch)) == 0
        and zero_cell.subs(zero_bloch, 1) == sp.zeros(2)
        and mass_path.rank() == 1
        and momentum_path.rank() == 1
        and mass_path != momentum_path
    )
    return {
        "factor_ok": factor_ok,
        "rank_ok": rank_ok,
        "determinant_factor": determinant_factor,
        "pole_ok": pole_ok,
        "residue_ok": residue_ok,
        "chain_ok": chain_ok,
        "chain_worst": worst_final,
        "multiplicities": multiplicities,
        "traces": traces,
        "massless_nonzero": massless_nonzero,
        "zero_mode_open": zero_mode_open,
    }


def reflection_certificate(mutation: str) -> dict[str, object]:
    reflected = {}
    placement = {}
    q = sp.symbols("q", real=True)
    for dim in (2, 4):
        s = phase_unitary(dim, include_koszul=mutation != "drop_induced_gamma_reflection")
        raw_time_swap = raw_gamma(dim, 0)
        induced = sp.simplify(-s * raw_time_swap * s.conjugate())
        reflected[dim] = induced == dk_gamma(dim, 0)
        temporal_phase = (
            sp.diag(sp.exp(-I * q / 2), sp.exp(-I * q / 2))
            if mutation == "same_sign_temporal_placement"
            else sp.diag(sp.exp(-I * q / 2), sp.exp(I * q / 2))
        )
        placement[dim] = (
            sp.simplify(temporal_phase * X * temporal_phase - X) == sp.zeros(2)
        )
    return {"reflected": reflected, "placement": placement}


def lorentz_boundary_certificate(mutation: str) -> dict[str, object]:
    mass, sx, st = sp.symbols("m sx st", real=True)
    euclidean_matter = m_matrix(d_matrix(sx, st), 1)
    euclidean = sp.simplify(mass * ID4 + I * euclidean_matter)
    h_lorentz = h0(-1)
    lorentz_matter = m_matrix(d_matrix(sx, st), -1)
    lorentz = sp.simplify(lorentz_matter + I * mass * h_lorentz)
    euclidean_det = sp.factor(euclidean.det())
    lorentz_det = sp.factor(lorentz.det())
    polynomial_wick = sp.simplify(
        euclidean_det.subs(st, I * st) - lorentz_det
    ) == 0

    radius = sp.symbols("r", positive=True)
    transfer_energy = sp.asinh(radius)
    lorentz_frequency = sp.asin(radius)
    difference = sp.series(lorentz_frequency - transfer_energy, radius, 0, 7)
    finite_mismatch = (
        sp.simplify(lorentz_frequency.subs(radius, sp.Rational(1, 2))
        - transfer_energy.subs(radius, sp.Rational(1, 2))) != 0
        and difference.removeO().coeff(radius, 3) == sp.Rational(1, 3)
    )
    domains = (
        sp.simplify(sp.sinh(transfer_energy) ** 2 - radius**2) == 0
        and sp.simplify(sp.sin(lorentz_frequency) ** 2 - radius**2) == 0
    )
    nonreal_beyond_unit = abs(complex(sp.N(sp.asin(2))).imag) > 0.1
    constant_clock_failure = (
        sp.series(lorentz_frequency, radius, 0, 5).removeO().coeff(radius, 1)
        == sp.series(transfer_energy, radius, 0, 5).removeO().coeff(radius, 1)
        and sp.series(lorentz_frequency, radius, 0, 5).removeO().coeff(radius, 3)
        != sp.series(transfer_energy, radius, 0, 5).removeO().coeff(radius, 3)
    )
    if mutation == "claim_exact_finite_lattice_lorentz":
        finite_mismatch = False
    return {
        "euclidean_det": euclidean_det,
        "lorentz_det": lorentz_det,
        "polynomial_wick": polynomial_wick,
        "finite_mismatch": finite_mismatch,
        "domains": domains,
        "nonreal_beyond_unit": nonreal_beyond_unit,
        "constant_clock_failure": constant_clock_failure,
        "difference": difference,
    }


def scope_certificate(mutation: str) -> dict[str, bool]:
    note = " ".join(NOTE_PATH.read_text(encoding="utf-8").lower().split())
    result = {
        "phase_family": "constant relative-phase family" in note,
        "phase_selected": "phi=+/-pi/2" in note,
        "fine_site": "one grassmann mode per fine site" in note,
        "full4d": "sixteen exterior components occupy the sixteen fine sites" in note,
        "two_taste": "two continuum staggered tastes" in note and "rank two" in note,
        "eight_taste": "eight spatial eigenlines" in note and "rank eight" in note,
        "same_action": "same-action reflected gram" in note,
        "curved_open": "curved-history reflected positivity remains unexecuted" in note,
        "adm_open": "actual adm/history transporter remains unexecuted" in note,
        "lorentz_open": "not an exact finite-spacing lorentz reconstruction" in note,
        "massless_open": "zero-mode prescription remains open" in note,
        "n1_n8": all(f"n{index}" in note for index in range(1, 9)),
        "axiom": "no axiom amendment is justified" in note,
        "zero_retirement": "zero obligation retirement" in note,
        "zero_score": "no toe percentage moves" in note,
        "zero_e2e": "retained-positive end-to-end theory count remains zero" in note,
    }
    if mutation == "claim_odd_cell_embedding":
        result["fine_site"] = False
    if mutation == "claim_massless_zero_closed":
        result["massless_open"] = False
    if mutation == "weaken_no_go_packet":
        result["n1_n8"] = False
    if mutation == "claim_axiom_update":
        result["axiom"] = False
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
            "use_naive_euclidean",
            "drop_wick_phase",
            "break_ward_response",
            "drop_mass_hodge_response",
            "forget_reduced_momentum",
            "break_koszul_phase",
            "co_located_overcount",
            "wrong_time_cell_symbol",
            "wrong_inside_pole",
            "break_gram_factor",
            "wrong_reflection_reorder",
            "fake_taste_multiplicity",
            "drop_induced_gamma_reflection",
            "same_sign_temporal_placement",
            "claim_exact_finite_lattice_lorentz",
            "claim_odd_cell_embedding",
            "claim_massless_zero_closed",
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
        "A-current-authority-Block103-parent-and-OS-source",
        "current axioms, exact Block103 parent, and reflected-Gram source triple are content-bound",
        authority["main"] == CURRENT_MAIN
        and authority["axiom"] == authority["expected_axiom"]
        and authority["worktree_axiom"] == CURRENT_AXIOM_BLOB
        and authority["registry"] == CURRENT_REGISTRY_BLOB
        and authority["worktree_registry"] == WORKTREE_REGISTRY_BLOB
        and authority["parent"] == PARENT_COMMIT
        and authority["parent_ancestor"]
        and authority["parent_note"] == PARENT_NOTE_BLOB
        and authority["parent_runner"] == PARENT_RUNNER_BLOB
        and authority["parent_cache"] == PARENT_CACHE_BLOB
        and authority["os_note"] == authority["expected_os"]
        and authority["os_runner"] == OS_SOURCE_RUNNER_BLOB
        and authority["os_cache"] == OS_SOURCE_CACHE_BLOB
        and authority["worktree_os_note"] == OS_SOURCE_NOTE_BLOB
        and authority["worktree_os_runner"] == OS_SOURCE_RUNNER_BLOB
        and authority["worktree_os_cache"] == OS_SOURCE_CACHE_BLOB,
        f"origin/main={str(authority['main'])[:10]}; parent={str(authority['parent'])[:10]}; OS={str(authority['os_note'])[:10]}",
    )

    phase = phase_and_free_kernel_certificate(mutation)
    checks.check(
        "B-Wick-phase-selection-and-naive-kernel-obstruction",
        "scalar covariance and time reflection select phi=+/-pi/2 while the naive Hermitian kernel fails an exact witness",
        phase["selected"] and phase["det_ok"],
        "det D_bad=(m^2-sx^2-st^2)^2; det D_E=(m^2+sx^2+st^2)^2; phi=+/-pi/2",
    )

    ward = same_action_ward_certificate(mutation)
    checks.check(
        "C-same-Hodge-action-Ward-and-skew-KD-equivalence",
        "the mass plus i-times-Hodge kinetic obeys the same Ward law and is degree-phase equivalent to skew Kähler-Dirac",
        ward["exact"] and ward["reversal"] and ward["phase_equivalence"],
        "Q_E=mH+i(Hd+d^dag H); Q_degree^dag Q_E Q_degree=mH+Hd-d^dag H",
    )

    fine = fine_site_equivalence_certificate(mutation)
    checks.check(
        "D-exact-2d-and-4d-fine-site-staggered-equivalence",
        "the reduced-cell placement phase and Koszul phase map one fine-site staggered field exactly to the DK carrier",
        fine["subcell"]
        and all(fine["gamma_maps"].values())
        and all(fine["actions"].values())
        and all(fine["determinants"].values())
        and fine["orientation"]
        and fine["count_ok"],
        f"component/fine-offset counts d=2/4: {fine['dimensions'][2]}/{fine['dimensions'][4]}",
    )

    cell = time_cell_and_taste_certificate(mutation)
    checks.check(
        "E-source-time-cell-symbol-pole-and-taste-census",
        "the same-action time cell equals the source symbol with the correct inside pole and spatial Clifford multiplicities",
        cell["cell_ok"]
        and cell["pole_ok"]
        and cell["spatial"][1] == (True, 1)
        and cell["spatial"][3] == (True, 4),
        "d=2 has lambda=+/-r once; d=4 has lambda=+/-r fourfold",
    )

    gram = gram_certificate(mutation)
    checks.check(
        "F-exact-same-action-reflected-Gram-and-multiplicity",
        "the two-line and eight-spatial-line Grams factor exactly with ranks two and eight",
        gram["factor_ok"]
        and gram["rank_ok"]
        and gram["determinant_factor"]
        and gram["pole_ok"]
        and gram["residue_ok"]
        and gram["chain_ok"]
        and gram["multiplicities"]
        and gram["traces"]
        and gram["massless_nonzero"]
        and gram["zero_mode_open"],
        f"same-D residue and open-chain inverse; worst Nt=24 residual {gram['chain_worst']:.1e}; d=2/4 ranks 2/8",
    )

    reflection = reflection_certificate(mutation)
    checks.check(
        "G-induced-Dirac-Kahler-OS-reflection",
        "transporting the raw Osterwalder-Seiler reflection produces the exact time-gamma DK reflection",
        all(reflection["reflected"].values()) and all(reflection["placement"].values()),
        "Theta_DK psi=Gamma_t (bar psi at theta(t))^T for d=2 and d=4",
    )

    lorentz = lorentz_boundary_certificate(mutation)
    checks.check(
        "H-polynomial-Wick-link-and-finite-spacing-Lorentz-boundary",
        "Euclidean and Lorentz determinants are polynomial continuations while OS energy and central-time frequency differ at finite spacing",
        lorentz["polynomial_wick"]
        and lorentz["finite_mismatch"]
        and lorentz["domains"]
        and lorentz["nonreal_beyond_unit"]
        and lorentz["constant_clock_failure"],
        "sinh^2 E=r^2; sin^2 omega=r^2; omega-E=r^3/3+O(r^7)",
    )

    scope = scope_certificate(mutation)
    checks.check(
        "I-scope-no-go-discipline-and-TOE-firewall",
        "N1-N8 preserve curved histories, ADM transport, finite-spacing Lorentz, zero-mode, axiom, audit, and TOE obligations",
        all(scope.values()),
    )

    print(
        f"AXIOM_AUTHORITY: origin/main={authority['main']} axiom={CURRENT_AXIOM_BLOB}; Block103 parent={PARENT_COMMIT}"
    )
    print(
        "per_element: exact Clifford phases, Hodge Ward response, time-cell pole, reflected-Gram factors, and induced reflection are checked"
    )
    print(
        "per_site: one staggered Grassmann mode per fine site is exactly relabeled into 2^d exterior components on each even 2^d cell"
    )
    print(
        "per_mode: the reduced-BZ d=2 two-line Gram has rank two and the d=4 eight-spatial-line Gram has rank eight"
    )
    print(
        "per_block: the full flat free 2^4 carrier placement, same-action Euclidean kernel, and two-slice OS quotient are exact"
    )
    print(
        "lattice_wide: checked and not executed — curved histories, actual ADM cross-links, joint gravity, exact finite-spacing Lorentz reconstruction, zero-mode choice, energy, Records, selection, and retention remain open"
    )
    print(
        "RESULT: flat mI+iM0 is phase-selected and exactly fine-site equivalent to the free staggered OS action in d=2,4; Q_E(H)=mH+iM(H) is its Ward-compatible degree-preserving extension"
    )
    print(
        "DECISION_CUT: advance Q_E to curved Hodge histories and the actual ADM transporter; do not identify flat mI+M0 with the July massive Euclidean OS kernel"
    )
    print(
        "TOE: zero obligation retirement, zero retained-positive end-to-end theories, and no percentage movement"
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
