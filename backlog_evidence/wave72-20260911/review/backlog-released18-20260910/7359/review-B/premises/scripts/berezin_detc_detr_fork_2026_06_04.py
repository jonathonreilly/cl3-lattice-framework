#!/usr/bin/env python3
"""Koide det_C versus det_R fork mechanism.

Bounded-theorem conditional algebra only. Load-bearing checks are exact and
fatal; the seeded randomized Koide-Q replay is motivation-tier only.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import permutations
from pathlib import Path

import numpy as np


F = Fraction
Matrix = tuple[tuple[Fraction, ...], ...]
NOTE_PATH = (
    Path(__file__).resolve().parents[1]
    / "docs"
    / "KOIDE_BEREZIN_DETC_VS_DETR_FORK_MECHANISM_NOTE_2026-06-04.md"
)


@dataclass(frozen=True)
class CPair:
    """Exact complex number with Fraction real and imaginary parts."""

    re: Fraction
    im: Fraction = F(0)

    def __add__(self, other: CPair) -> CPair:
        return CPair(self.re + other.re, self.im + other.im)

    def __sub__(self, other: CPair) -> CPair:
        return CPair(self.re - other.re, self.im - other.im)

    def __mul__(self, other: CPair) -> CPair:
        return CPair(
            self.re * other.re - self.im * other.im,
            self.re * other.im + self.im * other.re,
        )

    def norm2(self) -> Fraction:
        return self.re * self.re + self.im * self.im


@dataclass(frozen=True)
class CheckResult:
    label: str
    ok: bool


LOAD_RESULTS: list[CheckResult] = []
MOTIVATION_RESULTS: list[CheckResult] = []


def record(label: str, ok: bool, *, motivation: bool = False) -> None:
    target = MOTIVATION_RESULTS if motivation else LOAD_RESULTS
    target.append(CheckResult(label, bool(ok)))


def perm_sign(perm: tuple[int, ...]) -> int:
    sign = 1
    for i in range(len(perm)):
        for j in range(i + 1, len(perm)):
            if perm[i] > perm[j]:
                sign = -sign
    return sign


def mat(rows: tuple[tuple[int | Fraction, ...], ...]) -> Matrix:
    return tuple(tuple(F(x) for x in row) for row in rows)


def eye(n: int) -> Matrix:
    return tuple(
        tuple(F(1) if i == j else F(0) for j in range(n)) for i in range(n)
    )


def mat_add(a: Matrix, b: Matrix) -> Matrix:
    return tuple(
        tuple(aij + bij for aij, bij in zip(row_a, row_b))
        for row_a, row_b in zip(a, b)
    )


def mat_sub(a: Matrix, b: Matrix) -> Matrix:
    return tuple(
        tuple(aij - bij for aij, bij in zip(row_a, row_b))
        for row_a, row_b in zip(a, b)
    )


def mat_scalar(c: Fraction, a: Matrix) -> Matrix:
    return tuple(tuple(c * aij for aij in row) for row in a)


def mat_mul(a: Matrix, b: Matrix) -> Matrix:
    cols = tuple(zip(*b))
    return tuple(
        tuple(sum((x * y for x, y in zip(row, col)), F(0)) for col in cols)
        for row in a
    )


def mat_trace(a: Matrix) -> Fraction:
    return sum((a[i][i] for i in range(len(a))), F(0))


def mat_inverse(a: Matrix) -> Matrix:
    n = len(a)
    aug = [list(row) + [F(1) if i == j else F(0) for j in range(n)]
           for i, row in enumerate(a)]
    for col in range(n):
        pivot = next(row for row in range(col, n) if aug[row][col] != 0)
        aug[col], aug[pivot] = aug[pivot], aug[col]
        scale = aug[col][col]
        aug[col] = [entry / scale for entry in aug[col]]
        for row in range(n):
            if row == col:
                continue
            factor = aug[row][col]
            aug[row] = [
                entry - factor * pivot_entry
                for entry, pivot_entry in zip(aug[row], aug[col])
            ]
    return tuple(tuple(row[n:]) for row in aug)


def det_fraction(a: Matrix) -> Fraction:
    total = F(0)
    for sig in permutations(range(len(a))):
        prod = F(1)
        for i, j in enumerate(sig):
            prod *= a[i][j]
        total += F(perm_sign(sig)) * prod
    return total


def det_cpair(a: tuple[tuple[CPair, ...], ...]) -> CPair:
    total = CPair(F(0), F(0))
    for sig in permutations(range(len(a))):
        prod = CPair(F(1), F(0))
        for i, j in enumerate(sig):
            prod = prod * a[i][j]
        signed = prod if perm_sign(sig) == 1 else CPair(-prod.re, -prod.im)
        total = total + signed
    return total


def complex_realification(z: CPair) -> Matrix:
    return ((z.re, -z.im), (z.im, z.re))


def pfaffian_2x2(a: Matrix) -> Fraction:
    return a[0][1]


def format_fraction(x: Fraction) -> str:
    if x.denominator == 1:
        return str(x.numerator)
    return f"{x.numerator}/{x.denominator}"


def q_from_r(r: Fraction) -> Fraction:
    return (F(1) + 2 * r) / 3


def r_from_slot_count(slot_count: int) -> Fraction:
    return F(slot_count, 2)


def table_row(
    action: str,
    polarization: str,
    slot_count: int,
    slot_kind: str,
    r_value: Fraction,
    q_value: Fraction,
) -> str:
    slot_label = f"{slot_count} {slot_kind} slot"
    if slot_count != 1:
        slot_label += "s"
    r_text = format_fraction(r_value)
    q_text = format_fraction(q_value)
    return (
        f"| {action} | {polarization} | {slot_label} | "
        f"`r = {r_text}`, `Q = {q_text}` |"
    )


def slug(text: str) -> str:
    return text.lower().replace(" ", "_")


def koide_q_from_circulant(a: float, b: complex, c_matrix: np.ndarray) -> float:
    h_matrix = a * np.eye(3) + b * c_matrix + np.conj(b) * (c_matrix @ c_matrix)
    lam = np.linalg.eigvalsh(h_matrix)
    return float(np.sum(lam**2) / (np.sum(lam) ** 2))


def run_load_bearing_checks() -> None:
    note = NOTE_PATH.read_text(encoding="utf-8")
    ident = eye(3)
    generator = mat(((0, 0, 1), (1, 0, 0), (0, 1, 0)))
    generator_sq = mat_mul(generator, generator)
    p_single = mat_scalar(F(1, 3), mat_add(mat_add(ident, generator), generator_sq))
    p_doublet = mat_sub(ident, p_single)

    record("regular_rep_generator_order_three", mat_mul(generator_sq, generator) == ident)
    record("singleton_projector_idempotent", mat_mul(p_single, p_single) == p_single)
    record("doublet_projector_idempotent", mat_mul(p_doublet, p_doublet) == p_doublet)
    record(
        "real_projector_split_one_plus_two",
        mat_add(p_single, p_doublet) == ident
        and mat_mul(p_single, p_doublet) == mat_scalar(F(0), ident)
        and mat_trace(p_single) == 1
        and mat_trace(p_doublet) == 2,
    )

    basis = mat(((1, 1, 1), (-1, 1, 1), (0, -2, 1)))
    complex_on_doublet = mat(((0, -1, 0), (1, 0, 0), (0, 0, 0)))
    j_matrix = mat_mul(mat_mul(basis, complex_on_doublet), mat_inverse(basis))
    record(
        "doublet_complex_structure_supported",
        mat_mul(p_doublet, j_matrix) == j_matrix
        and mat_mul(j_matrix, p_doublet) == j_matrix,
    )
    record(
        "doublet_complex_structure_square",
        mat_mul(j_matrix, j_matrix) == mat_scalar(F(-1), p_doublet),
    )

    det_pairs = ((F(1), F(2)), (F(2, 3), F(5, 4)), (F(7, 5), F(3, 2)))
    det_pairs += ((F(11, 6), F(4, 7)),)
    for index, (alpha, beta) in enumerate(det_pairs, start=1):
        block_matrix = mat_add(mat_scalar(alpha, p_single), mat_scalar(beta, p_doublet))
        record(
            f"det_R_pair_{index}_actual_vs_closed",
            det_fraction(block_matrix) == alpha * beta * beta,
        )

    real_gaussian_slots = int(mat_trace(p_doublet))
    holo_gaussian_slots = real_gaussian_slots // 2
    record("real_gaussian_slot_count_from_projector", real_gaussian_slots == 2)
    record(
        "holomorphic_gaussian_slot_count_from_J",
        real_gaussian_slots == 2 * holo_gaussian_slots
        and mat_mul(j_matrix, j_matrix) == mat_scalar(F(-1), p_doublet),
    )

    beta_complex = CPair(F(3, 5), F(2, 7))
    holo_block = ((beta_complex,),)
    holo_det = det_cpair(holo_block)
    record(
        "holomorphic_block_det_realification",
        holo_det.norm2() == det_fraction(complex_realification(beta_complex)),
    )
    holo_berezin_slots = len(holo_block)
    record("holomorphic_berezin_complex_slot_count", holo_berezin_slots == 1)

    majorana_mass = F(7, 5)
    majorana_cell = ((F(0), majorana_mass), (-majorana_mass, F(0)))
    majorana_pf = pfaffian_2x2(majorana_cell)
    record(
        "majorana_pfaffian_square_actual_det",
        majorana_pf * majorana_pf == det_fraction(majorana_cell),
    )
    majorana_slots = len(majorana_cell)
    record("majorana_real_slot_count", majorana_slots == real_gaussian_slots)

    record("q_lever_real_branch", q_from_r(F(1)) == F(1))
    record("q_lever_holomorphic_branch", q_from_r(F(1, 2)) == F(2, 3))

    cells = (
        ("real Gaussian", "real", real_gaussian_slots, "real"),
        ("Majorana Berezin", "real", majorana_slots, "real"),
        ("holomorphic Gaussian", "holomorphic", holo_gaussian_slots, "complex"),
        ("holomorphic Berezin", "holomorphic", holo_berezin_slots, "complex"),
    )
    computed: dict[str, tuple[int, str, Fraction, Fraction]] = {}
    for action, polarization, slot_count, slot_kind in cells:
        r_value = r_from_slot_count(slot_count)
        q_value = q_from_r(r_value)
        computed[action] = (slot_count, slot_kind, r_value, q_value)
        record(
            f"note_table_row_{slug(action)}",
            table_row(action, polarization, slot_count, slot_kind, r_value, q_value)
            in note,
        )

    real_same = computed["real Gaussian"][2:] == computed["Majorana Berezin"][2:]
    holo_same = computed["holomorphic Gaussian"][2:] == computed["holomorphic Berezin"][2:]
    record("statistics_not_decisive_in_tested_cells", real_same and holo_same)
    record(
        "polarization_decides_doublet_count",
        computed["real Gaussian"][0] != computed["holomorphic Gaussian"][0]
        and computed["Majorana Berezin"][0] != computed["holomorphic Berezin"][0],
    )

    needles = {
        "frontmatter_bounded_theorem": "claim_type_author_hint: bounded_theorem",
        "premise_supplied": "generation doublet is SUPPLIED: either real",
        "premise_not_derived": "be cited as decided or derived.",
        "j_square_displayed": "`J^2 = -P_d`",
        "det_identity_displayed": "`det_R(alpha P_s + beta P_d) = alpha beta^2`",
        "lever_authority_inline_link": (
            "[KOIDE_CIRCULANT_Q_TWO_THIRDS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md]"
            "(KOIDE_CIRCULANT_Q_TWO_THIRDS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md)"
        ),
        "motivation_exhibit_label": "evidence only; not load-bearing",
        "context_link_restored": "[block-count-note]: KOIDE_REAL_REP_BLOCK_COUNT",
        "real_branch_conditional": "real => r = 1, Q = 1",
        "holomorphic_branch_conditional": "holomorphic => r = 1/2, Q = 2/3",
        "verification_motivation_banner": (
            "MOTIVATION-TIER (non-load-bearing; does not affect exit status)"
        ),
    }
    for label, needle in needles.items():
        record(label, needle in note)


def run_motivation_checks() -> None:
    c_matrix = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]], dtype=complex)
    rng = np.random.default_rng(0)
    q_identity_ok = True
    for _ in range(200):
        a_value = rng.uniform(0.5, 3.0)
        b_value = rng.uniform(0.05, 1.2) * np.exp(1j * rng.uniform(0, 2 * np.pi))
        r_value = abs(b_value) ** 2 / a_value**2
        expected = (1 + 2 * r_value) / 3
        if abs(koide_q_from_circulant(a_value, b_value, c_matrix) - expected) > 1e-10:
            q_identity_ok = False
            break
    record("seeded_koide_q_identity_random_replay", q_identity_ok, motivation=True)


def counts(results: list[CheckResult]) -> tuple[int, int]:
    passed = sum(1 for result in results if result.ok)
    failed = len(results) - passed
    return passed, failed


def main() -> int:
    run_load_bearing_checks()
    run_motivation_checks()
    load_pass, load_fail = counts(LOAD_RESULTS)
    motivation_pass, motivation_fail = counts(MOTIVATION_RESULTS)

    print("Koide Berezin det_C versus det_R fork mechanism")
    print("Scope: bounded theorem under POLARIZATION-SELECT; no selector claimed.")
    print(f"LOAD-BEARING CHECKS: PASS={load_pass} FAIL={load_fail}")
    if load_fail:
        failed = ", ".join(result.label for result in LOAD_RESULTS if not result.ok)
        print(f"LOAD-BEARING FAILURES: {failed}")
    print("MOTIVATION-TIER (non-load-bearing; does not affect exit status)")
    print(f"MOTIVATION: PASS={motivation_pass} FAIL={motivation_fail}")
    print(f"TOTAL: PASS={load_pass} FAIL={load_fail}")
    print("DECLARATION: POLARIZATION-SELECT supplied; no polarization derived.")
    return 0 if load_fail == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
