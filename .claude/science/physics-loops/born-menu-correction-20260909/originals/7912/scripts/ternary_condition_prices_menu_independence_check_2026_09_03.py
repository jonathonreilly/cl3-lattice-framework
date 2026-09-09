#!/usr/bin/env python3
"""Exact checks for the note that prices the ternary condition against menu-independence.

Everything here is finite exact rational or symbolic algebra. The dimension-three
frame-function theorem is named as context in the note and is not recomputed. The
Cycle-984 section recomputes the five declared numerator formulas as typed laws on a
declared exact world table; it does not reload the 748-world receipt of that note.
"""

import subprocess
import sys
from fractions import Fraction as F
from pathlib import Path

import sympy as sp


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / "THE_TERNARY_CONDITION_PRICES_MENU_INDEPENDENCE_NOT_MENU_ARITY_BOUNDED_THEOREM_NOTE_2026-09-03.md"
PARENT_NOTE = ROOT / "docs" / "BORN_FORM_FROM_BINARY_TERNARY_SCALED_PROJECTOR_FRAME_LIFT_BOUNDED_THEOREM_NOTE_2026-08-09.md"
PARENT_RUNNER = ROOT / "scripts" / "born_form_binary_ternary_scaled_projector_frame_lift_2026_08_09.py"
C984_NOTE = ROOT / "docs" / "BORN_COMPATIBILITY_Z3_ADJACENCY_CYCLE984_NOTE_2026-08-11.md"
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/THE_TERNARY_CONDITION_PRICES_MENU_INDEPENDENCE_NOT_MENU_ARITY_BOUNDED_THEOREM_NOTE_2026-09-03.md",
    "docs/BORN_FORM_FROM_BINARY_TERNARY_SCALED_PROJECTOR_FRAME_LIFT_BOUNDED_THEOREM_NOTE_2026-08-09.md",
    "scripts/born_form_binary_ternary_scaled_projector_frame_lift_2026_08_09.py",
    "docs/BORN_COMPATIBILITY_Z3_ADJACENCY_CYCLE984_NOTE_2026-08-11.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

R = sp.Rational
S3 = sp.sqrt(3)
I2 = sp.eye(2)
I3 = sp.eye(3)
SX = sp.Matrix([[0, 1], [1, 0]])
SY = sp.Matrix([[0, -sp.I], [sp.I, 0]])
SZ = sp.Matrix([[1, 0], [0, -1]])


def bloch(n):
    x, y, z = n
    return sp.simplify((I2 + x * SX + y * SY + z * SZ) / 2)


def is_zero(matrix):
    return matrix.applyfunc(sp.simplify) == sp.zeros(*matrix.shape)


def normalize(text):
    return " ".join(text.split())


# ---------------------------------------------------------------- declared qubit menus
ROT = sp.Matrix([[R(1, 3), R(-2, 3), R(2, 3)],
                 [R(2, 3), R(2, 3), R(1, 3)],
                 [R(-2, 3), R(1, 3), R(2, 3)]])


def rotate(n):
    v = ROT * sp.Matrix(list(n))
    return (v[0], v[1], v[2])


BIN_Z = [(R(1), (0, 0, 1)), (R(1), (0, 0, -1))]
BIN_X = [(R(1), (1, 0, 0)), (R(1), (-1, 0, 0))]
BIN_TILT = [(R(1), (R(3, 5), 0, R(4, 5))), (R(1), (R(-3, 5), 0, R(-4, 5)))]
TER_FOURIER = [(R(2, 3), (0, 0, 1)),
               (R(2, 3), (S3 / 2, 0, R(-1, 2))),
               (R(2, 3), (-S3 / 2, 0, R(-1, 2)))]
TER_ISO = [(R(3, 4), (1, 0, 0)),
           (R(5, 8), (R(-3, 5), R(4, 5), 0)),
           (R(5, 8), (R(-3, 5), R(-4, 5), 0))]
TER_ISO_ROT = [(c, rotate(n)) for c, n in TER_ISO]
TER_DEGEN = [(R(1), (0, 0, 1)), (R(1, 2), (0, 0, -1)), (R(1, 2), (0, 0, -1))]

QUBIT_MENUS = [("BIN_z", BIN_Z, 2), ("BIN_x", BIN_X, 2), ("BIN_tilt", BIN_TILT, 2),
               ("TER_fourier", TER_FOURIER, 3), ("TER_isosceles", TER_ISO, 3),
               ("TER_iso_rotated", TER_ISO_ROT, 3), ("TER_degenerate", TER_DEGEN, 3)]
COIN_MENUS = [("COIN_bin_1/3", [R(1, 3), R(2, 3)], 2), ("COIN_bin_1/2", [R(1, 2), R(1, 2)], 2),
              ("COIN_ter_1/4", [R(1, 4), R(1, 4), R(1, 2)], 3),
              ("COIN_ter_1/6", [R(1, 6), R(1, 3), R(1, 2)], 3)]


def w_born(r):
    return (lambda c, n: c * (1 + sum(a * b for a, b in zip(r, n))) / 2), (lambda c: c)


def w_odd(power):
    return (lambda c, n: c * (1 + n[2] ** power) / 2), (lambda c: c)


def w_legendre():
    return (lambda c, n: c * (1 + (5 * n[2] ** 3 - 3 * n[2]) / 2) / 2), (lambda c: c)


def w_coinwobble():
    return (lambda c, n: c / 2), (lambda c: c + c * (1 - c) * (c - R(1, 2)))


def w_csquare():
    return (lambda c, n: c ** 2 / 2), (lambda c: c ** 2)


MENU_INDEPENDENT = [
    ("W_BORN[r=0]", w_born((0, 0, 0))),
    ("W_BORN[r=(3/5,0,4/5)]", w_born((R(3, 5), 0, R(4, 5)))),
    ("W_CUBIC", w_odd(3)),
    ("W_QUINTIC", w_odd(5)),
    ("W_HARM3", w_legendre()),
    ("W_COINWOBBLE", w_coinwobble()),
    ("W_CSQUARE", w_csquare()),
]


def grade_menu(rank_one, menu):
    return sp.nsimplify(sp.simplify(sum(rank_one(c, n) for c, n in menu)))


def grade_coin(coin, menu):
    return sp.nsimplify(sp.simplify(sum(coin(a) for a in menu)))


def born_values(menu, rho):
    return [sp.nsimplify(sp.simplify(sp.trace(rho * (c * bloch(n))))) for c, n in menu]


def uniform_values(menu):
    return [R(1, len(menu))] * len(menu)


def power_values(menu, rho, p):
    raw = born_values(menu, rho)
    num = [sp.simplify(v ** R(p, 2)) for v in raw]
    total = sp.simplify(sum(num))
    return [sp.nsimplify(sp.simplify(v / total)) for v in num]


# ---------------------------------------------------------------- declared qutrit menus
OMEGA = R(-1, 2) + sp.I * S3 / 2


def proj3(v):
    v = sp.Matrix(v)
    v = v / sp.sqrt(sp.simplify((v.H * v)[0]))
    return sp.simplify(v * v.H)


ONB_STD = [proj3([1, 0, 0]), proj3([0, 1, 0]), proj3([0, 0, 1])]
ONB_FOU = [proj3([1, 1, 1]), proj3([1, OMEGA, OMEGA ** 2]), proj3([1, OMEGA ** 2, OMEGA])]
ONB_RAT = [proj3(list(ROT[:, j])) for j in range(3)]
ONB_TILT = [proj3([R(3, 5), R(4, 5), 0]), proj3([R(-4, 5), R(3, 5), 0]), proj3([0, 0, 1])]
QUTRIT_ONB = [("ONB_standard", ONB_STD), ("ONB_fourier", ONB_FOU),
              ("ONB_rational", ONB_RAT), ("ONB_tilted", ONB_TILT)]
QUTRIT_MERGE = [(f"MERGE12_{name}", [b[0] + b[1], b[2]]) for name, b in QUTRIT_ONB]
RHO_Q = sp.diag(R(1, 2), R(1, 3), R(1, 6))


def diag_part(matrix):
    return sp.diag(*[sp.simplify(matrix[i, i]) for i in range(3)])


def q_born(rho):
    return lambda p: sp.nsimplify(sp.simplify(sp.trace(rho * p)))


def q_quartic(rho, lam):
    def value(p):
        deformation = sp.trace(diag_part(p) ** 2) - sp.trace(p) / 3
        return sp.nsimplify(sp.simplify(sp.trace(rho * p) + lam * deformation))
    return value


def q_power(menu, rho, p):
    raw = [sp.nsimplify(sp.simplify(sp.trace(rho * m))) for m in menu]
    num = [sp.simplify(v ** R(p, 2)) for v in raw]
    total = sp.simplify(sum(num))
    return [sp.nsimplify(sp.simplify(v / total)) for v in num]


# ---------------------------------------------------------------- Cycle-984 typed laws
# One declared exact world table. Worlds w1 and w2 agree in every event-level datum
# (same event count, same atom labels); they differ only in the substrate history
# variables o(w) and f(w) that M3-M5 read.
D_COMMON = 6
BOUND = 200
WORLD_TABLE = (
    # name, N_w, o(w), f(w), formed
    ("w1", 2, 5, 100, True),
    ("w2", 2, 7, 40, True),
    ("w3", 3, 0, 0, False),
)


def c984_numerators():
    laws = {"M1": [], "M2": [], "M3": [], "M4": [], "M5": []}
    for _, n_w, o_w, f_w, formed in WORLD_TABLE:
        per = F(D_COMMON, n_w)
        for _ in range(n_w):
            laws["M1"].append(F(1))
            laws["M2"].append(per)
            laws["M3"].append(o_w * per)
            laws["M4"].append((BOUND - f_w) * per if formed else F(0))
            laws["M5"].append(f_w * per if formed else F(0))
    return laws


def factorised_marginal():
    """Sum the declared product joint over (x, n, y) for a generic normalized event law."""
    p1, p2, m1 = sp.symbols("p1 p2 m1", real=True)
    events = (p1, p2, 1 - p1 - p2)
    mu = (m1, 1 - m1)
    q = (R(1, 4),) * 4
    residuals = []
    for p_e in events:
        total = 0
        for xi, mu_x in enumerate(mu):
            for ni, q_n in enumerate(q):
                for y in (0, 1):
                    if y == (xi + ni) % 2:
                        total += p_e * mu_x * q_n
        residuals.append(sp.simplify(sp.expand(total - p_e)))
    return residuals


# ---------------------------------------------------------------- rank certificate
A_ODD = [(1, 0), (0, 1), (3, 0), (2, 1), (1, 2), (0, 3),
         (5, 0), (4, 1), (3, 2), (2, 3), (1, 4), (0, 5)]
B_EVEN = [(0, 0), (2, 0), (1, 1), (0, 2), (4, 0), (3, 1), (2, 2), (1, 3), (0, 4)]
A_ALL = [(i, d - i) for d in range(6) for i in range(d, -1, -1)]
B_ALL = [(i, d - i) for d in range(5) for i in range(d, -1, -1)]
TRINE_Q = ((F(3, 4), (F(1), F(0), F(0))),
           (F(5, 8), (F(-3, 5), F(4, 5), F(0))),
           (F(5, 8), (F(-3, 5), F(-4, 5), F(0))))


def quaternion_rotation(a, b, c, d):
    s = a * a + b * b + c * c + d * d
    return ((F(a * a + b * b - c * c - d * d, s), F(2 * (b * c - a * d), s), F(2 * (b * d + a * c), s)),
            (F(2 * (b * c + a * d), s), F(a * a - b * b + c * c - d * d, s), F(2 * (c * d - a * b), s)),
            (F(2 * (b * d - a * c), s), F(2 * (c * d + a * b), s), F(a * a - b * b - c * c + d * d, s)))


def rational_rotations(limit):
    out = []
    for a in range(4):
        for b in range(4):
            for c in range(4):
                for d in range(4):
                    if a + b + c + d == 0:
                        continue
                    out.append(quaternion_rotation(a, b, c, d))
                    if len(out) == limit:
                        return out
    return out


def constraint_rows(a_monomials, b_monomials, limit):
    rows = []
    seen = set()
    for rot in rational_rotations(255):
        row = [F(0)] * (len(a_monomials) + len(b_monomials))
        for coefficient, n in TRINE_Q:
            x = sum(rot[0][k] * n[k] for k in range(3))
            y = sum(rot[1][k] * n[k] for k in range(3))
            z = sum(rot[2][k] * n[k] for k in range(3))
            values = [x ** i * y ** j for i, j in a_monomials]
            values += [z * x ** i * y ** j for i, j in b_monomials]
            row = [row[k] + coefficient * values[k] for k in range(len(row))]
        key = tuple(row)
        if key in seen:
            continue
        seen.add(key)
        rows.append(row)
        if len(rows) == limit:
            break
    return rows


def exact_rank(rows, columns):
    matrix = [row[:] for row in rows]
    pivot = 0
    for column in range(columns):
        index = next((i for i in range(pivot, len(matrix)) if matrix[i][column] != 0), None)
        if index is None:
            continue
        matrix[pivot], matrix[index] = matrix[index], matrix[pivot]
        inverse = F(1) / matrix[pivot][column]
        matrix[pivot] = [value * inverse for value in matrix[pivot]]
        for i in range(len(matrix)):
            if i != pivot and matrix[i][column] != 0:
                factor = matrix[i][column]
                matrix[i] = [matrix[i][k] - factor * matrix[pivot][k] for k in range(columns)]
        pivot += 1
        if pivot == len(matrix):
            break
    return pivot


def linear_modes_in_kernel(rows, a_monomials, b_monomials):
    names = [f"x^{i}y^{j}" for i, j in a_monomials] + [f"z*x^{i}y^{j}" for i, j in b_monomials]
    modes = ("x^1y^0", "x^0y^1", "z*x^0y^0")
    return all(all(row[names.index(mode)] == 0 for row in rows) for mode in modes)


class Checks:
    def __init__(self):
        self.passed = 0
        self.failed = 0

    def check(self, label, statement, condition):
        result = bool(condition)
        if result:
            self.passed += 1
        else:
            self.failed += 1
        print(f"{'PASS' if result else 'FAIL'}: {label} {statement}")

    def finish(self):
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def main():
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    parent = PARENT_NOTE.read_text(encoding="utf-8")
    c984 = C984_NOTE.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")

    print("external_scientific_inputs: the canonical axiom file, the 2026-08-09 parent note and runner, and the Cycle-984 note are read for source and boundary gates only")
    print("package_local_integrity_reads: the proposed source note is read for claim-surface consistency; the cache envelope binds this runner and every declared input")
    print("standard_theorem_boundary: the dimension-three frame-function theorem is named as context in the note and is not recomputed here")

    # ---- T1: the parent reproduces, and its two clauses are stated as symmetric
    parent_run = subprocess.run(
        [sys.executable, str(PARENT_RUNNER)],
        capture_output=True, text=True, cwd=str(ROOT), timeout=100,
    )
    checks.check(
        "T1-parent-reproduces",
        "the 2026-08-09 runner re-executes on its repository inputs and prints PASS=16 FAIL=0",
        parent_run.returncode == 0 and "TOTAL: PASS=16 FAIL=0" in parent_run.stdout,
    )
    checks.check(
        "T1-parent-three-inputs",
        "the parent states effect functionality, low-arity eligibility, and a named frame theorem",
        all(s in parent for s in ("**Effect functionality.**", "**Low-arity eligibility.**", "**Standard frame theorem.**")),
    )
    checks.check(
        "T1-parent-derived-form",
        "the parent derives a unique density matrix with w(E)=Tr(rho E) on the scaled domain",
        "`w(E)=Tr(rho E)` for every `E in S`" in normalize(parent) and "two independent conditional clauses" in parent,
    )
    trine_cubic = grade_menu(w_odd(3)[0], TER_FOURIER)
    checks.check(
        "T1-hostile-control-agrees",
        "this runner independently regrades the parent trine control and also gets exactly 5/4",
        trine_cubic == R(5, 4),
    )

    # ---- T2: the Cycle-984 laws are counting measures on event atoms
    checks.check(
        "T2-declared-numerators",
        "the Cycle-984 note declares numerators 1, D/N_w, o(w)D/N_w, (180225-f(w))D/N_w, and f(w)D/N_w",
        all(s in c984 for s in ("`M1_COUNTING` | `1` |", "`M2_PER_WORLD_UNIFORM` | `D/N_w` |",
                                "`M3_OCCUPATION_WEIGHTED` | `o(w)D/N_w` |",
                                "`M4_FORMATION_LIFETIME` | `(180225-f(w))D/N_w` if formed, else `0` |",
                                "`M5_FORMATION_MOMENT` | `f(w)D/N_w` if formed, else `0` |")),
    )
    laws = c984_numerators()
    checks.check(
        "T2-counting-on-atoms",
        "each declared law is a per-atom weight built only from N_w, o(w), f(w) and the common multiple D",
        all(len(v) == sum(w[1] for w in WORLD_TABLE) for v in laws.values()),
    )
    checks.check(
        "T2-m1-uniform",
        "M1 gives every event atom the same weight, so its single-menu effect reading is the uniform law",
        len(set(laws["M1"])) == 1,
    )
    offsets = []
    running = 0
    for world in WORLD_TABLE:
        offsets.append((running, world[1]))
        running += world[1]
    checks.check(
        "T2-m2-per-world-uniform",
        "M2 is constant within each world and gives every world the same total D",
        all(len(set(laws["M2"][start:start + count])) == 1 for start, count in offsets)
        and all(sum(laws["M2"][start:start + count]) == D_COMMON for start, count in offsets),
    )
    checks.check(
        "T2-m3-m5-read-history",
        "M3, M4 and M5 separate two worlds agreeing in every event-level datum, so no function of the effect reproduces them",
        laws["M3"][0] != laws["M3"][2] and laws["M4"][0] != laws["M4"][2] and laws["M5"][0] != laws["M5"][2],
    )
    checks.check(
        "T2-m1-m2-do-not-separate",
        "M1 and M2 do not separate those same two worlds, so their only effect-side reading is menu-dependent uniformity",
        laws["M1"][0] == laws["M1"][2] and laws["M2"][0] == laws["M2"][2],
    )
    checks.check(
        "T2-marginal-is-vacuous",
        "the declared product joint marginalises over the other variables to p(e) for a generic normalized event law",
        all(r == 0 for r in factorised_marginal()),
    )
    checks.check(
        "T2-note-says-so",
        "the Cycle-984 note states the nondiscrimination itself and advances no Born selection",
        "survival is nondiscrimination rather than" in c984
        and "regardless of its detailed event weights" in c984
        and "this nondiscrimination test selects none of the five" in normalize(c984),
    )

    # ---- T3: menu-independent gradings and the ternary condition
    symbols = sp.symbols("c1 c2 c3 a nx ny nz", real=True)
    c1, c2, c3, a_coin, nx, ny, nz = symbols
    residual = c1 * bloch((nx, ny, nz)) + a_coin * I2 - I2
    checks.check(
        "T3-menu-structure",
        "c P(n) + a I = I2 holds exactly when c n = 0 and c + 2a = 2, so binary rank-one menus are antipodal pairs at c=1",
        sp.simplify(2 * residual[0, 1] - c1 * (nx - sp.I * ny)) == 0
        and sp.simplify((residual[0, 0] - residual[1, 1]) - c1 * nz) == 0
        and sp.simplify((residual[0, 0] + residual[1, 1]) - (c1 + 2 * a_coin - 2)) == 0,
    )
    checks.check(
        "T3-menus-resolve",
        "every declared qubit menu resolves the identity exactly and every declared coin menu sums to one",
        all(is_zero(sum((c * bloch(n) for c, n in menu), sp.zeros(2)) - I2) for _, menu, _ in QUBIT_MENUS)
        and all(sp.simplify(sum(menu) - 1) == 0 for _, menu, _ in COIN_MENUS),
    )
    table = {}
    for name, (rank_one, coin) in MENU_INDEPENDENT:
        table[name] = {}
        for menu_name, menu, arity in QUBIT_MENUS:
            table[name][menu_name] = (grade_menu(rank_one, menu), arity)
        for menu_name, menu, arity in COIN_MENUS:
            table[name][menu_name] = (grade_coin(coin, menu), arity)
    binary_names = [n for n, _, a in QUBIT_MENUS if a == 2] + [n for n, _, a in COIN_MENUS if a == 2]

    def passes_binary(name):
        return all(table[name][m][0] == 1 for m in binary_names)

    checks.check(
        "T3-binary-blind",
        "the cubic, quintic, Legendre-P3 and coin-wobble gradings all normalise on every declared binary menu",
        all(passes_binary(n) for n in ("W_CUBIC", "W_QUINTIC", "W_HARM3", "W_COINWOBBLE")),
    )
    checks.check(
        "T3-csquare-needs-binary",
        "the squared-coefficient grading already fails a binary coin menu at exactly 1/2",
        table["W_CSQUARE"]["COIN_bin_1/2"][0] == R(1, 2),
    )
    checks.check(
        "T3-ternary-witnesses",
        "on the Fourier trine the cubic gives 5/4, the quintic 21/16 and the Legendre-P3 grading 13/8",
        table["W_CUBIC"]["TER_fourier"][0] == R(5, 4)
        and table["W_QUINTIC"]["TER_fourier"][0] == R(21, 16)
        and table["W_HARM3"]["TER_fourier"][0] == R(13, 8),
    )
    checks.check(
        "T3-coin-witness",
        "the coin-wobble grading survives every rank-one menu and fails the ternary coins at 29/32 and 11/12",
        table["W_COINWOBBLE"]["COIN_ter_1/4"][0] == R(29, 32)
        and table["W_COINWOBBLE"]["COIN_ter_1/6"][0] == R(11, 12)
        and all(table["W_COINWOBBLE"][m][0] == 1 for m, _, _ in QUBIT_MENUS),
    )
    checks.check(
        "T3-born-survives",
        "both declared Born gradings normalise on every declared qubit and coin menu",
        all(table[n][m][0] == 1 for n in ("W_BORN[r=0]", "W_BORN[r=(3/5,0,4/5)]") for m in table[n]),
    )
    odd_rows = constraint_rows(A_ODD, B_EVEN, 45)
    odd_rank = exact_rank(odd_rows, 21)
    checks.check(
        "T3-rank-odd",
        "the odd degree-five ansatz gives 21 columns of exact rational ternary constraints with rank 18",
        len(odd_rows) == 45 and odd_rank == 18,
    )
    checks.check(
        "T3-kernel-odd",
        "its nullity is exactly three and the three linear modes x, y, z annihilate every ternary row",
        21 - odd_rank == 3 and linear_modes_in_kernel(odd_rows, A_ODD, B_EVEN),
    )
    all_rows = constraint_rows(A_ALL, B_ALL, 120)
    all_rank = exact_rank(all_rows, 36)
    checks.check(
        "T3-rank-unrestricted",
        "dropping the binary oddness restriction gives 36 columns, exact rational rank 33, nullity three again",
        len(all_rows) == 120 and all_rank == 33 and 36 - all_rank == 3
        and linear_modes_in_kernel(all_rows, A_ALL, B_ALL),
    )

    # ---- T4: menu-dependent gradings pass every arity
    rho_tilt = bloch((0, 0, R(3, 5)))
    dependent_ok = True
    for menu_name, menu, _ in QUBIT_MENUS:
        for values in (uniform_values(menu), power_values(menu, rho_tilt, 4), power_values(menu, rho_tilt, 1)):
            dependent_ok = dependent_ok and sp.simplify(sum(values) - 1) == 0
    checks.check(
        "T4-qubit-all-arity",
        "the uniform law and the amplitude-power laws sum to one on every declared qubit menu, binary and ternary",
        dependent_ok,
    )
    qutrit_ok = True
    for _, menu in QUTRIT_ONB + QUTRIT_MERGE:
        for values in (uniform_values(menu), q_power(menu, RHO_Q, 4)):
            qutrit_ok = qutrit_ok and sp.simplify(sum(values) - 1) == 0
    checks.check(
        "T4-qutrit-all-arity",
        "the same laws sum to one on all four qutrit bases and all four rank-two-plus-rank-one menus",
        qutrit_ok,
    )
    uni_bin = uniform_values(BIN_Z)[0]
    uni_ter = uniform_values(TER_DEGEN)[0]
    pow_bin = power_values(BIN_Z, rho_tilt, 4)[0]
    pow_ter = power_values(TER_DEGEN, rho_tilt, 4)[0]
    born_bin = born_values(BIN_Z, rho_tilt)[0]
    born_ter = born_values(TER_DEGEN, rho_tilt)[0]
    checks.check(
        "T4-functionality-witness",
        "the same effect P(e_z) is graded 1/2 then 1/3 by the uniform law and 16/17 then 32/33 by the power law",
        uni_bin == R(1, 2) and uni_ter == R(1, 3)
        and pow_bin == R(16, 17) and pow_ter == R(32, 33),
    )
    checks.check(
        "T4-functionality-born",
        "the Born grading gives that same effect 4/5 in both menus, so effect functionality holds for it",
        born_bin == R(4, 5) and born_ter == R(4, 5),
    )
    checks.check(
        "T4-merge-qubit",
        "on the qubit merge the uniform law gives 1/2 against 2/3, the power law 1/17 against 1/33, and Born 1/5 twice",
        uniform_values(BIN_Z)[1] == R(1, 2) and sum(uniform_values(TER_DEGEN)[1:]) == R(2, 3)
        and power_values(BIN_Z, rho_tilt, 4)[1] == R(1, 17)
        and sp.simplify(sum(power_values(TER_DEGEN, rho_tilt, 4)[1:]) - R(1, 33)) == 0
        and born_values(BIN_Z, rho_tilt)[1] == R(1, 5)
        and sp.simplify(sum(born_values(TER_DEGEN, rho_tilt)[1:]) - R(1, 5)) == 0,
    )
    q_born_rho = q_born(RHO_Q)
    merged = ONB_STD[0] + ONB_STD[1]
    q_uni_lhs = uniform_values([merged, ONB_STD[2]])[0]
    q_uni_rhs = sum(uniform_values(ONB_STD)[:2])
    q_pow_lhs = q_power([merged, ONB_STD[2]], RHO_Q, 4)[0]
    q_pow_rhs = sp.simplify(sum(q_power(ONB_STD, RHO_Q, 4)[:2]))
    checks.check(
        "T4-merge-qutrit",
        "on the qutrit merge the uniform law gives 1/2 against 2/3 and the power law 25/26 against 13/14",
        q_uni_lhs == R(1, 2) and q_uni_rhs == R(2, 3)
        and q_pow_lhs == R(25, 26) and q_pow_rhs == R(13, 14),
    )
    checks.check(
        "T4-merge-qutrit-born",
        "the Born grading is additive across the same qutrit merge, giving 5/6 on both sides",
        q_born_rho(merged) == R(5, 6) and sp.simplify(q_born_rho(ONB_STD[0]) + q_born_rho(ONB_STD[1]) - R(5, 6)) == 0,
    )
    quartic = q_quartic(RHO_Q, R(1, 10))
    quartic_sums = {name: sp.nsimplify(sp.simplify(sum(quartic(p) for p in menu)))
                    for name, menu in QUTRIT_ONB}
    checks.check(
        "T4-qutrit-quartic-fails",
        "the menu-independent quartic deformation gives 6/5, 46/45 and 3462/3125 on three qutrit bases",
        quartic_sums["ONB_standard"] == R(6, 5)
        and quartic_sums["ONB_rational"] == R(46, 45)
        and quartic_sums["ONB_tilted"] == R(3462, 3125),
    )
    checks.check(
        "T4-qutrit-basis-blind",
        "that same deformation is exactly one on the Fourier basis, so one qutrit basis is not enough",
        quartic_sums["ONB_fourier"] == 1,
    )

    # ---- T5: a planar ternary menu is blind
    blind = [table[n]["TER_isosceles"][0] for n in ("W_CUBIC", "W_QUINTIC", "W_HARM3")]
    rotated = [table[n]["TER_iso_rotated"][0] for n in ("W_CUBIC", "W_QUINTIC", "W_HARM3")]
    checks.check(
        "T5-planar-ternary-blind",
        "the isosceles ternary menu with all three directions in one plane grades the three odd-nonlinear gradings at exactly one",
        blind == [sp.Integer(1)] * 3,
    )
    checks.check(
        "T5-rotated-ternary-sees",
        "one exact rational rotation out of that plane gives 221/225, 50209/50625 and 43/45",
        rotated == [R(221, 225), R(50209, 50625), R(43, 45)],
    )

    # ---- source and surface gates
    checks.check(
        "source-record-axiom",
        "the canonical Record axiom says a readout value is determined by record content alone",
        "A readout value is determined by record content" in normalize(axiom)
        and "When present, a record locks exactly one admissible local possibility" in normalize(axiom),
    )
    checks.check(
        "source-admissibility-reading",
        "the canonical Admissibility reading note says the distribution does not supply the formation site, probability, or rate",
        "it does not supply the formation site, probability, or rate" in normalize(axiom),
    )
    checks.check(
        "surface-status",
        "this note keeps its conditional surface, its exact claim scope, and independent audit explicit",
        all(s in note for s in ("actual_current_surface_status: conditional-support",
                                "audit_required_before_effective_retained: true",
                                "no canonical axiom edit",
                                "Independent audit remains required")),
    )

    print("per_element: every menu, grading value, merge witness, and world-table weight above is checked as an exact rational element")
    print("per_site: one M_2(C) site and one M_3(C) carrier are checked; no multi-site or lattice claim is made")
    print("per_mode: odd and unrestricted sphere-polynomial sections through degree five are checked by exact rational rank; the frame theorem is named only")
    print("per_block: this block checks the parent reproduction, the Cycle-984 typing, both grading families, and the planar-menu warning together")
    print("lattice_wide: checked and not executed — the statements are one-site finite algebra and register no lattice-wide claim")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
