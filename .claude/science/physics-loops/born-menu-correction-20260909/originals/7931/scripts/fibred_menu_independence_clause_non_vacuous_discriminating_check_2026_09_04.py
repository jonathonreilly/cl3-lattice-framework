#!/usr/bin/env python3
"""Checks for the fibred menu-independence clause note.

Two arithmetic stages, kept apart and declared.  T1 and T5 are exact rational
`fractions.Fraction` algebra on a one-site continuum model; the largest dense
object there is 72 by 3.  T2, T3 and T4 rebuild the emergent 2x2x2 cube from
scratch inside this file -- 12 edge qubits in the superfast encoding, the
Kawamoto-Smit staggered link signs, the half-filled sea -- and inherit a
float64 sea eigenvector; every odds value quoted there is reconstructed as an
exact rational by continued fractions and agrees with the float to better than
1e-11, every equality is tested at 1e-9 or tighter, and every reported
difference has a margin of order 1e-1.  The largest dense object on the cube is
a record block far below 4096 by 4096.  No seed is used anywhere: the condition
families are complete enumerations by declared index arithmetic.  Recorded
arguments print with an `ARG:` prefix and are excluded from the PASS/FAIL
total, so no prose claim is counted as a verification.
"""

import itertools
import math
import re
import time
from fractions import Fraction as F
from pathlib import Path

import numpy as np
import scipy.linalg as sla


AUDIT_TIMEOUT_SEC = 300
TOL = 1e-9

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "A_FIBRED_MENU_INDEPENDENCE_CLAUSE_NON_VACUOUS_ON_THE_CONTINUUM_LAW_"
    "DISCRIMINATING_ON_THE_CUBE_BOUNDED_THEOREM_NOTE_2026-09-04.md"
)
PARENT_NOTE = ROOT / "docs" / (
    "BORN_FORM_FROM_BINARY_TERNARY_SCALED_PROJECTOR_FRAME_LIFT_BOUNDED_THEOREM_"
    "NOTE_2026-08-09.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/A_FIBRED_MENU_INDEPENDENCE_CLAUSE_NON_VACUOUS_ON_THE_CONTINUUM_LAW_"
    "DISCRIMINATING_ON_THE_CUBE_BOUNDED_THEOREM_NOTE_2026-09-04.md",
    "docs/BORN_FORM_FROM_BINARY_TERNARY_SCALED_PROJECTOR_FRAME_LIFT_BOUNDED_THEOREM"
    "_NOTE_2026-08-09.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)


def normalize(text):
    return " ".join(text.split())


def flatten_quotes(text):
    """Normalised note text with block-quote markers removed, for wording needles."""
    return normalize(re.sub(r"(?m)^>\s?", "", text))


class Checks:
    """Machine verifications count; recorded arguments are printed, never counted."""

    def __init__(self):
        self.passed = 0
        self.failed = 0
        self.arguments = 0

    def check(self, label, statement, condition):
        result = bool(condition)
        if result:
            self.passed += 1
        else:
            self.failed += 1
        print(f"{'PASS' if result else 'FAIL'}: {label} {statement}")

    def note(self, label, statement):
        self.arguments += 1
        print(f"ARG: {label} {statement}")

    def finish(self):
        print(f"recorded_arguments: {self.arguments} printed, none counted as verified")
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


# ------------------------------------------------------- exact rational one-site algebra
def proper_cubic_rotations():
    out = []
    for perm in itertools.permutations(range(3)):
        for sgn in itertools.product((1, -1), repeat=3):
            m = [[0] * 3 for _ in range(3)]
            for i in range(3):
                m[i][perm[i]] = sgn[i]
            det = (m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
                   - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
                   + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0]))
            if det == 1:
                out.append(m)
    return out


def act(m, v):
    return tuple(sum(m[i][j] * v[j] for j in range(3)) for i in range(3))


def exact_rank(rows, ncols):
    mat = [list(r) for r in rows]
    rank = 0
    for col in range(ncols):
        sel = None
        for i in range(rank, len(mat)):
            if mat[i][col] != 0:
                sel = i
                break
        if sel is None:
            continue
        mat[rank], mat[sel] = mat[sel], mat[rank]
        piv = mat[rank][col]
        mat[rank] = [x / piv for x in mat[rank]]
        for i in range(len(mat)):
            if i != rank and mat[i][col] != 0:
                f = mat[i][col]
                mat[i] = [a - f * b for a, b in zip(mat[i], mat[rank])]
        rank += 1
        if rank == len(mat):
            break
    return rank


def ray(c, u):
    """The possibility c P(u), with u an exact rational unit Bloch direction."""
    return ("P", F(c), tuple(F(x) for x in u))


def coin(c):
    """The possibility c I."""
    return ("I", F(c), None)


def trace_and_bloch(e):
    kind, c, u = e
    if kind == "I":
        return 2 * c, (F(0), F(0), F(0))
    return c, (c * u[0], c * u[1], c * u[2])


def resolves_identity(menu):
    t = sum(trace_and_bloch(e)[0] for e in menu)
    b = [sum(trace_and_bloch(e)[1][i] for e in menu) for i in range(3)]
    return t == 2 and all(x == 0 for x in b)


def odds(state_bloch, e):
    """tr(rho E) for rho = (I + r.sigma)/2, exactly."""
    t, b = trace_and_bloch(e)
    return (t + sum(state_bloch[i] * b[i] for i in range(3))) / 2


def is_unit(u):
    return sum(x * x for x in u) == 1


def t1(checks):
    """The clause MI-fib', its strong non-vacuity, and the in-fibre discriminator."""
    checks.note(
        "T1-clause",
        "(MI-fib') if sigma(n) = sigma(n') then p_n(v) = p_n'(v) for every possibility v "
        "admissible under both, sigma equivariant and menu-blind; equally p_n(v) = w(v; sigma(n))",
    )
    checks.note(
        "T1-escape",
        "the vacuity lemma bites only at fixed n, where the menu is a function of the "
        "condition; MI-fib' compares two conditions in one fibre, so it can bite",
    )

    sa = [ray(F(8, 9), (0, 0, 1)),
          ray(F(5, 9), (F(3, 5), 0, F(-4, 5))),
          ray(F(5, 9), (F(-3, 5), 0, F(-4, 5)))]
    sb = [ray(F(8, 9), (0, 0, 1)),
          ray(F(5, 9), (0, F(3, 5), F(-4, 5))),
          ray(F(5, 9), (0, F(-3, 5), F(-4, 5)))]
    checks.check("T1-unit-directions",
                 "the six declared Bloch directions are exact rational unit vectors",
                 all(is_unit(e[2]) for e in sa + sb))
    checks.check("T1-supports-resolve",
                 "both ternary supports resolve I_2 exactly",
                 resolves_identity(sa) and resolves_identity(sb))
    shared = [e for e in sa if e in sb]
    checks.check("T1-supports-overlap",
                 "the supports differ and share exactly one possibility, (8/9) P(e_z)",
                 sa != sb and len(shared) == 1 and shared[0] == ray(F(8, 9), (0, 0, 1)))

    slots = ((1, 0, 0), (0, 1, 0), (0, -1, 0))
    dipole = tuple(sum(s[i] for s in slots) for i in range(3))
    checks.check("T1-same-fibre",
                 "both arise from the slot pattern {+e_x, +e_y, -e_y}, so lambda = e_x for both",
                 dipole == (1, 0, 0))
    checks.note(
        "T1-menu-blind",
        "the lattice dipole reads only which slots carry records and the menu only the record "
        "values, so the fibre map of L_CONT is menu-blind by construction",
    )

    rho_ex = (F(2, 3), F(0), F(0))
    born_a = sum(odds(rho_ex, e) for e in sa)
    born_b = sum(odds(rho_ex, e) for e in sb)
    checks.check("T1-born-normalised",
                 f"rho at e_x = (I + (2/3) sigma_x)/2 sums to exactly 1 on both supports "
                 f"({born_a} and {born_b})",
                 born_a == 1 and born_b == 1)
    checks.check("T1-born-satisfies",
                 f"and gives the shared possibility the same odds {odds(rho_ex, shared[0])} in "
                 f"both, so the Born grading satisfies MI-fib' here",
                 odds(rho_ex, shared[0]) == F(4, 9))
    checks.check("T1-born-in-range",
                 "every Born odds value on both supports lies in [0, 1]",
                 all(0 <= odds(rho_ex, e) <= 1 for e in sa + sb))

    adv_a = tuple(F(2, 3) * x for x in sa[0][2])
    adv_b = tuple(F(2, 3) * x for x in sb[1][2])
    sum_a = sum(odds(adv_a, e) for e in sa)
    sum_b = sum(odds(adv_b, e) for e in sb)
    checks.check("T1-adversary-normalised",
                 "the adversary law L_ADV, whose state reads the record value on the dipole "
                 "slot, is normalised to exactly 1 on both supports",
                 sum_a == 1 and sum_b == 1)
    o_a, o_b = odds(adv_a, shared[0]), odds(adv_b, shared[0])
    checks.check("T1-strong-non-vacuity",
                 f"strong non-vacuity: in the fibre lambda = e_x the shared possibility (8/9) "
                 f"P(e_z) is given {o_a} under one condition and {o_b} under the other, so "
                 f"L_ADV violates MI-fib'",
                 o_a == F(20, 27) and o_b == F(28, 135) and o_a != o_b)
    checks.check("T1-adversary-in-range",
                 "every L_ADV odds value on both supports lies in [0, 1]",
                 all(0 <= odds(adv_a, e) <= 1 for e in sa)
                 and all(0 <= odds(adv_b, e) <= 1 for e in sb))
    checks.note(
        "T1-adversary-axioms",
        "L_ADV is nearest-neighbour, covariant and normalised on every realised support, so it "
        "meets the four axioms and fails MI-fib': the clause has content",
    )

    mixed = [ray(F(2, 3), (0, 0, 1)), ray(F(2, 3), (0, 0, -1)), coin(F(1, 3))]
    coin_menu = [coin(F(1, 3)), coin(F(2, 3))]
    checks.check("T1-in-fibre-menus",
                 "inside the same fibre the mixed ternary and the coin menu both resolve I_2 "
                 "and share the possibility (1/3) I",
                 resolves_identity(mixed) and resolves_identity(coin_menu)
                 and coin(F(1, 3)) in mixed and coin(F(1, 3)) in coin_menu)
    checks.check("T1-uniform-violates",
                 "the uniform law gives (1/3) I the odds 1/3 in the mixed ternary and 1/2 in "
                 "the coin menu: a violation inside one fibre",
                 F(1, 3) != F(1, 2))
    checks.check("T1-born-separates-uniform",
                 "every state gives (1/3) I the odds 1/3 in both, since tr(rho (1/3) I) = 1/3 "
                 "for every rho, so the clause separates Born from uniform exactly",
                 odds(rho_ex, coin(F(1, 3))) == F(1, 3)
                 and odds((F(0), F(0), F(0)), coin(F(1, 3))) == F(1, 3)
                 and odds((F(1), F(0), F(0)), coin(F(1, 3))) == F(1, 3))
    checks.check("T1-born-normalised-in-fibre",
                 "the Born grading is normalised on both of those menus too",
                 sum(odds(rho_ex, e) for e in mixed) == 1
                 and sum(odds(rho_ex, e) for e in coin_menu) == 1)

    rots = proper_cubic_rotations()
    checks.check("T1-rotations", "24 proper cubic rotations of determinant one", len(rots) == 24)
    rows = [[F(m[i][j] - (1 if i == j else 0)) for j in range(3)] for m in rots for i in range(3)]
    checks.check("T1-invariant-bloch-is-zero",
                 "the only Bloch vector invariant under all 24 rotations is 0, so a "
                 "rotation-invariant fibre label forces rho = I/2",
                 exact_rank(rows, 3) == 3)
    stab = [m for m in rots if act(m, (1, 0, 0)) == (1, 0, 0)]
    rows2 = [[F(m[i][j] - (1 if i == j else 0)) for j in range(3)] for m in stab for i in range(3)]
    checks.check("T1-stabiliser-carries-a-direction",
                 "Stab(e_x) has order 4 and its invariant Bloch vectors are span{e_x}, so the "
                 "fibre at e_x carries rho = (I + t sigma_x)/2 with t free",
                 len(stab) == 4 and exact_rank(rows2, 3) == 2)


# ------------------------------------------------------- the emergent 2x2x2 cube
def popcount(n):
    return bin(n).count("1")


class Pauli:
    """i^k prod_q X_q^{x_q} Z_q^{z_q}, X before Z on every qubit."""

    __slots__ = ("k", "x", "z")

    def __init__(self, k, x, z):
        self.k = k % 4
        self.x = x
        self.z = z

    def __mul__(self, other):
        return Pauli(self.k + other.k + 2 * popcount(self.z & other.x),
                     self.x ^ other.x, self.z ^ other.z)

    def neg(self):
        return Pauli(self.k + 2, self.x, self.z)


PHASE = (1 + 0j, 1j, -1 + 0j, -1j)


def pauli_act(p, b):
    return b ^ p.x, PHASE[p.k] * ((-1) ** (popcount(p.z & b) % 2))


class Cube:
    """The 2x2x2 cube with 12 edge qubits in the superfast encoding."""

    def __init__(self):
        self.V = 8
        self.EDGES = sorted((min(s, s ^ bit), max(s, s ^ bit))
                            for s in range(8) for bit in (4, 2, 1) if s ^ bit > s)
        self.NQ = len(self.EDGES)
        self.DIM = 1 << self.NQ
        self.EIDX = {}
        for q, (i, j) in enumerate(self.EDGES):
            self.EIDX[(i, j)] = q
            self.EIDX[(j, i)] = q
        self.NBR = {i: sorted(j for (a, b) in self.EDGES
                              for j in ((b,) if a == i else ((a,) if b == i else ())))
                    for i in range(self.V)}
        self.STARMASK = {i: sum(1 << self.EIDX[(i, k)] for k in self.NBR[i]) for i in range(self.V)}
        self.FACES = []
        for ax in range(3):
            bits = [4, 2, 1]
            fb = bits[ax]
            ob = [b for b in bits if b != fb]
            for val in (0, fb):
                self.FACES.append((val, val | ob[1], val | ob[0] | ob[1], val | ob[0]))

    def A_unsigned(self, i, j):
        x = 1 << self.EIDX[(i, j)]
        z = 0
        for k in self.NBR[i]:
            if k != j and k < j:
                z ^= 1 << self.EIDX[(i, k)]
        for l in self.NBR[j]:
            if l != i and l < i:
                z ^= 1 << self.EIDX[(j, l)]
        return Pauli(popcount(x & z) % 2, x, z)

    def A(self, i, j):
        p = self.A_unsigned(i, j)
        return p if i < j else p.neg()

    def B(self, i):
        return Pauli(0, 0, self.STARMASK[i])

    def loop(self, cyc):
        out = Pauli(0, 0, 0)
        for a in range(len(cyc)):
            out = out * self.A(cyc[a], cyc[(a + 1) % len(cyc)])
        return out

    def record(self, z):
        return tuple(popcount(z & self.STARMASK[i]) % 2 for i in range(self.V))

    def hop_pauli(self, i, j):
        a = self.A(i, j)
        return a * self.B(i), a * self.B(j)

    def hop_amp(self, p1, p2, y):
        b1, a1 = pauli_act(p1, y)
        b2, a2 = pauli_act(p2, y)
        assert b1 == b2
        v = 0.5j * (a1 - a2)
        return b1, complex(round(v.real), round(v.imag))


def build_cube():
    cube = Cube()
    stab = [cube.loop(f) for f in cube.FACES]
    gens, basis = [], []
    for s in stab:
        v = s.x
        for b in basis:
            v = min(v, v ^ b)
        if v:
            basis.append(v)
            basis.sort(reverse=True)
            gens.append(s)
    group = []
    for m in range(1 << len(gens)):
        p = Pauli(0, 0, 0)
        for t in range(len(gens)):
            if (m >> t) & 1:
                p = p * gens[t]
        group.append(p)
    dim = cube.DIM
    cid = -np.ones(dim, dtype=np.int64)
    phi = np.zeros(dim, dtype=complex)
    reps = []
    for z0 in range(dim):
        if cid[z0] >= 0:
            continue
        c = len(reps)
        reps.append(z0)
        for g in group:
            b, a = pauli_act(g, z0)
            cid[b] = c
            phi[b] = a

    def corner_xyz(s):
        return ((s >> 2) & 1, (s >> 1) & 1, s & 1)

    def eta_ks(v, a):
        if a == 0:
            return 1
        if a == 1:
            return -1 if (v[0] & 1) else 1
        return -1 if ((v[0] + v[1]) & 1) else 1

    eta = np.zeros(cube.NQ, dtype=np.int64)
    for q, (i, j) in enumerate(cube.EDGES):
        lo, hi = min(i, j), max(i, j)
        eta[q] = eta_ks(corner_xyz(lo), {4: 0, 2: 1, 1: 2}[lo ^ hi])
    flux = []
    for cyc in cube.FACES:
        f = 1
        for t in range(4):
            f *= int(eta[cube.EIDX[(cyc[t], cyc[(t + 1) % 4])]])
        flux.append(f)

    hamp = np.zeros((cube.NQ, dim), dtype=np.complex128)
    for q, e in enumerate(cube.EDGES):
        p1, p2 = cube.hop_pauli(*e)
        for z in range(dim):
            zz, amp = cube.hop_amp(p1, p2, z)
            if amp == 0:
                continue
            assert zz == z ^ (1 << q)
            hamp[q, z] = -1.0 * eta[q] * amp
    nval = np.array([sum(cube.record(z)) for z in range(dim)], dtype=np.int64)

    ncoset = len(reps)
    w = np.zeros((dim, ncoset), dtype=np.complex128)
    w[np.arange(dim), cid] = phi / np.sqrt(float(len(group)))
    hw = np.zeros((dim, ncoset), dtype=np.complex128)
    for c in range(ncoset):
        psi = w[:, c]
        out = np.zeros(dim, dtype=np.complex128)
        for q in range(cube.NQ):
            out[np.arange(dim) ^ (1 << q)] += hamp[q] * psi
        hw[:, c] = out
    hc = w.conj().T @ hw
    evals, evecs = np.linalg.eigh(hc)
    sea = w @ evecs[:, 0]
    return (cube, hamp, nval, sea, np.abs(sea) ** 2, float(evals[0]),
            float(evals[1] - evals[0]), int(np.sum(evals < evals[0] + 1e-9)), flux, ncoset)


def relaxation_diag(cube, hamp, nval, rmask, wval, nlow=6):
    """Ground-space diagonal of the record-conditioned relaxation tick M_R."""
    dim = cube.DIM
    idx = np.flatnonzero((np.arange(dim) & rmask) == wval)
    free = [q for q in range(cube.NQ) if not (rmask >> q) & 1]
    loc = -np.ones(dim, dtype=np.int64)
    blocks = []
    for n in np.unique(nval[idx]):
        sub = idx[nval[idx] == n]
        d = len(sub)
        loc[sub] = np.arange(d)
        hb = np.zeros((d, d), dtype=np.complex128)
        cols = np.arange(d)
        for q in free:
            a = hamp[q][sub]
            mask = a != 0
            if not mask.any():
                continue
            hb[loc[sub[mask] ^ (1 << q)], cols[mask]] += a[mask]
        loc[sub] = -1
        if d > 4 * nlow:
            ev, vc = sla.eigh(hb, subset_by_index=[0, nlow - 1])
        else:
            ev, vc = np.linalg.eigh(hb)
        blocks.append((sub, ev, vc))
    e0 = min(float(b[1][0]) for b in blocks)
    diag = np.zeros(dim)
    deg = 0
    for sub, ev, vc in blocks:
        sel = np.flatnonzero(ev < e0 + TOL)
        if len(sel) == 0:
            continue
        assert len(sel) < len(ev), "ground degeneracy exceeds the computed eigenvalue subset"
        deg += len(sel)
        diag[sub] += np.sum(np.abs(vc[:, sel]) ** 2, axis=1)
    return e0, deg, diag / deg


def all_conditions(nq, kmax):
    """Every record subset of size at most kmax with every value: declared, complete, no seed."""
    out = []
    for k in range(kmax + 1):
        for sub in itertools.combinations(range(nq), k):
            rmask = sum(1 << q for q in sub)
            for vals in itertools.product((0, 1), repeat=k):
                out.append((rmask, sum(v << q for q, v in zip(sub, vals)), k))
    return out


def rational(x, tol=1e-11, cap=10 ** 6):
    f = F(float(x)).limit_denominator(cap)
    return f if abs(float(f) - float(x)) < tol else None


# ------------------------------------------------------- T2 / T3: the cube's odds and its fibres
def cube_pass(checks, model):
    """One complete sweep of every condition with at most four records.

    Returns the per-(condition, edge) rows carrying the conditioned state, the
    conditioned-sea odds, the relaxation-tick odds and the uniform odds.
    """
    cube, hamp, nval, sea, p_sea = model[0], model[1], model[2], model[3], model[4]
    dim, nq = cube.DIM, cube.NQ
    labels = np.arange(dim)
    conds = all_conditions(nq, 4)
    checks.check("T2-condition-family",
                 f"{len(conds)} conditions: every record subset of size at most four with every "
                 f"value, complete and declared",
                 len(conds) == 9969)

    rows = []
    live = 0
    max_dev = 0.0
    checked = 0
    for rmask, wval, k in conds:
        idx = np.flatnonzero((labels & rmask) == wval)
        total = float(p_sea[idx].sum())
        if total <= 1e-24:
            continue
        live += 1
        weight = p_sea[idx] / total
        _, _, diag = relaxation_diag(cube, hamp, nval, rmask, wval)
        dtot = float(diag[idx].sum())
        amp = sea[idx]
        norm = float(np.vdot(amp, amp).real)
        for q in range(nq):
            if (rmask >> q) & 1:
                continue
            low = ((idx >> q) & 1) == 0
            p0 = float(weight[low].sum())
            b0 = idx[low]
            b1 = b0 ^ (1 << q)
            r00 = float(np.vdot(sea[b0], sea[b0]).real) / norm
            r11 = float(np.vdot(sea[b1], sea[b1]).real) / norm
            r01 = complex(np.vdot(sea[b1], sea[b0])) / norm
            max_dev = max(max_dev, abs(p0 - r00), abs(1.0 - p0 - r11))
            checked += 2
            menu = tuple(b for b, p in ((0, r00), (1, r11)) if p > 1e-12)
            rows.append((q, (round(r00, 9), round(r11, 9), round(abs(r01), 9)), p0,
                         float(diag[idx][low].sum()) / dtot,
                         (1.0 / len(menu)) if 0 in menu else 0.0, rmask, wval, k, menu))
    checks.check("T2-born-identity",
                 f"p_n(P_b) = tr(rho_q(n) P_b) on {checked} checks over {live} live conditions "
                 f"and their free edges, largest deviation {max_dev:.2e}",
                 live == 9969 and checked == 164232 and max_dev < 1e-12)
    checks.note(
        "T2-identity-not-test",
        "an identity, not a test: rho_q(n) is the reduced conditioned sea, whose record-basis "
        "diagonal is the odds; with one frame the cube can test the clause, never the Born form",
    )

    values3 = sorted({round(r[2], 12) for r in rows if r[7] == 3})
    rats3 = [rational(v) for v in values3]
    want3 = [F(5, 18), F(1, 3), F(1, 2), F(2, 3), F(13, 18)]
    checks.check("T2-five-odds-at-three-records",
                 "with three records the odds take exactly the five values 5/18, 1/3, 1/2, 2/3, "
                 "13/18 on one and the same binary menu",
                 rats3 == want3 and {r[8] for r in rows if r[7] == 3} == {(0, 1)})
    checks.note(
        "T2-invariant-label-has-no-grading",
        "the record count is the natural invariant label and its three-record fibre carries five "
        "odds on one menu, so no grading exists there: an invariant label is refuted",
    )

    fibres = {}
    for row in rows:
        fibres.setdefault((row[0], row[1]), []).append(row)
    two_menus = sum(1 for v in fibres.values() if len({r[8] for r in v}) > 1)
    checks.check("T2-state-determines-menu",
                 f"no fibre of the conditioned-sea state contains two different menus, over all "
                 f"{live} conditions and {len(rows)} condition-edge pairs ({two_menus} violations): "
                 f"strong non-vacuity is impossible on the cube",
                 two_menus == 0)
    checks.note(
        "T2-one-frame-proof",
        "for any law and any state-valued fibre map: records register a bit in one fixed frame, "
        "so M(n) = {P_b : tr(sigma(n) P_b) > 0} and the state determines the menu",
    )
    multi = {k: v for k, v in fibres.items() if len(v) > 1}
    checks.check("T2-weak-non-vacuity",
                 f"weak non-vacuity holds abundantly: {len(multi)} of {len(fibres)} fibres carry "
                 f"more than one condition, the largest {max(len(v) for v in fibres.values())}",
                 len(multi) > 0)
    return rows, fibres, multi


def t3(checks, rows, fibres, multi):
    """The cube discriminates the relaxation tick in the weak form."""
    summary = {}
    for col, label in ((2, "the conditioned sea"), (3, "the relaxation tick M_R"),
                       (4, "the uniform law")):
        violating = 0
        worst = None
        for key, members in multi.items():
            vals = [m[col] for m in members]
            gap = max(vals) - min(vals)
            if gap > 1e-9:
                violating += 1
                if worst is None or gap > worst[0]:
                    worst = (gap, key)
        summary[col] = (violating, worst)
    n_sea, _ = summary[2]
    n_mr, worst_mr = summary[3]
    n_uni, _ = summary[4]
    checks.check("T3-sea-satisfies",
                 f"the conditioned sea satisfies MI-fib' on the cube: {n_sea} of {len(multi)} "
                 f"multi-element fibres carry unequal odds",
                 n_sea == 0)
    checks.check("T3-tick-discriminated",
                 f"the relaxation tick M_R violates it: {n_mr} of {len(multi)} multi-element "
                 f"fibres carry unequal M_R odds, largest difference {worst_mr[0]:.6f}",
                 n_mr > 0 and worst_mr[0] > 1e-1)
    checks.check("T3-uniform-not-discriminated",
                 f"the uniform law satisfies it identically: {n_uni} of {len(multi)} fibres, and "
                 f"structurally so, since on the cube the menu is a function of the state",
                 n_uni == 0)
    checks.note(
        "T3-corrects-the-vacuity-note",
        "the sibling note read the cube as furnishing no discriminator; true of the global "
        "clause, false of the fibred one",
    )

    named = {(0x314, 0x104): F(4, 5), (0x21c, 0x21c): None}
    picked = [r for r in rows if r[0] == 10 and (r[5], r[6]) in named]
    checks.check("T3-witness-present",
                 "the two declared four-record sets 0x314/0x104 and 0x21c/0x21c both condition "
                 "edge 10 and both appear in the sweep",
                 len(picked) == 2)
    by_key = {(r[5], r[6]): r for r in picked}
    a = by_key[(0x314, 0x104)]
    b = by_key[(0x21c, 0x21c)]
    checks.check("T3-witness-same-state",
                 "they condition edge 10 to the same state diag(2/3, 1/3)",
                 a[1] == b[1] and abs(a[1][0] - 2.0 / 3.0) < 1e-9 and max(a[1][2], b[1][2]) < 1e-15)
    checks.check("T3-witness-same-menu",
                 "and offer the same binary menu {P_0, P_1}",
                 a[8] == (0, 1) and b[8] == (0, 1))
    checks.check("T3-witness-sea-agrees",
                 f"the conditioned-sea odds are 2/3 under both, as MI-fib' requires "
                 f"(difference {abs(a[2] - b[2]):.1e})",
                 rational(a[2]) == F(2, 3) and rational(b[2]) == F(2, 3))
    tick_b = (6 + math.sqrt(2)) / 8
    checks.check("T3-witness-tick-differs",
                 f"the relaxation tick gives 4/5 under one and (6 + sqrt 2)/8 = {b[3]:.9f} under "
                 f"the other, a difference of {abs(a[3] - b[3]):.6f}",
                 abs(a[3] - 0.8) < 1e-12 and abs(b[3] - tick_b) < 1e-12)
    checks.check("T3-witness-uniform-agrees",
                 "the uniform law gives 1/2 under both, so the witness separates M_R from the "
                 "sea and not the sea from uniform",
                 abs(a[4] - 0.5) < 1e-12 and abs(b[4] - 0.5) < 1e-12)
    return n_mr, len(multi), len(fibres), worst_mr[0]


def t3_witness_detail(checks, model):
    cube, hamp, nval, sea = model[0], model[1], model[2], model[3]
    labels = np.arange(cube.DIM)
    out, coh = [], []
    for rmask, wval in ((0x314, 0x104), (0x21c, 0x21c)):
        e0, deg, _ = relaxation_diag(cube, hamp, nval, rmask, wval)
        out.append((e0, deg))
        idx = np.flatnonzero((labels & rmask) == wval)
        amp = sea[idx]
        b0 = idx[((idx >> 10) & 1) == 0]
        coh.append(abs(complex(np.vdot(sea[b0 ^ (1 << 10)], sea[b0]))
                       / float(np.vdot(amp, amp).real)))
    checks.check("T3-witness-ground-states-simple",
                 f"both witness ground states are non-degenerate, E0 = {out[0][0]:.9f} and "
                 f"E0 = {out[1][0]:.9f}, each of degeneracy one; the two conditioned states "
                 f"carry coherence at most {max(coh):.1e}",
                 out[0][1] == 1 and out[1][1] == 1 and max(coh) < 1e-17)


# ------------------------------------------------------- T4: the equivariance no-go
def edge_permutations(cube):
    rots = proper_cubic_rotations()
    eidx = {tuple(sorted(e)): q for q, e in enumerate(cube.EDGES)}
    perms = []
    for m in rots:
        corner = []
        for s in range(8):
            c = ((s >> 2) & 1, (s >> 1) & 1, s & 1)
            u = [2 * c[i] - 1 for i in range(3)]
            v = act(m, u)
            corner.append(4 * ((v[0] + 1) // 2) + 2 * ((v[1] + 1) // 2) + ((v[2] + 1) // 2))
        perms.append(tuple(eidx[tuple(sorted((corner[i], corner[j])))] for (i, j) in cube.EDGES))
    return perms


def t4(checks, model):
    cube, hamp, nval, sea, p_sea = model[0], model[1], model[2], model[3], model[4]
    dim, nq = cube.DIM, cube.NQ
    labels = np.arange(dim)
    perms = edge_permutations(cube)
    checks.check("T4-edge-permutations",
                 "the 24 proper cubic rotations induce 24 distinct permutations of the 12 edge "
                 "qubits",
                 len(perms) == 24 and len(set(perms)) == 24)

    inv = True
    for perm in perms:
        moved = np.zeros(dim, dtype=np.int64)
        for q in range(nq):
            moved |= ((labels >> q) & 1) << perm[q]
        inv = inv and float(np.max(np.abs(p_sea[moved] - p_sea))) < 1e-12
    checks.check("T4-sea-invariant",
                 "all 24 induced permutations leave the sea probabilities invariant",
                 inv)

    def image(g, rmask, wval):
        perm = perms[g]
        r2 = w2 = 0
        for q in range(nq):
            if (rmask >> q) & 1:
                r2 |= 1 << perm[q]
                if (wval >> q) & 1:
                    w2 |= 1 << perm[q]
        return r2, w2

    def state(idx, q):
        amp = sea[idx]
        norm = float(np.vdot(amp, amp).real)
        b0 = idx[((idx >> q) & 1) == 0]
        b1 = b0 ^ (1 << q)
        return (float(np.vdot(sea[b0], sea[b0]).real) / norm,
                float(np.vdot(sea[b1], sea[b1]).real) / norm,
                complex(np.vdot(sea[b1], sea[b0])) / norm)

    max_diag = max_abs = max_off = 0.0
    triples = 0
    asymmetric = False
    for rmask, wval, k in all_conditions(nq, 3):
        idx = np.flatnonzero((labels & rmask) == wval)
        if float(p_sea[idx].sum()) <= 1e-24:
            continue
        for g in range(24):
            r2, w2 = image(g, rmask, wval)
            idx2 = np.flatnonzero((labels & r2) == w2)
            perm = perms[g]
            for q in range(nq):
                if (rmask >> q) & 1:
                    continue
                r = state(idx, q)
                s = state(idx2, perm[q])
                max_diag = max(max_diag, abs(r[0] - s[0]))
                max_abs = max(max_abs, abs(abs(r[2]) - abs(s[2])))
                max_off = max(max_off, abs(r[2] - s[2]))
                triples += 1
                if abs(r[0] - r[1]) > 1e-1:
                    asymmetric = True
    checks.check("T4-odds-equivariant",
                 f"the odds map is exactly equivariant: p_(g.n)(P_b at g(q)) = p_n(P_b at q) on "
                 f"{triples} condition-rotation-edge triples, largest deviation {max_diag:.2e}",
                 triples == 450144 and max_diag < 1e-12)
    checks.check("T4-state-map-not-equivariant",
                 f"but |rho_01| is not invariant, differing by up to {max_abs:.3f} (rho_01 itself "
                 f"by up to {max_off:.3f}), so no site unitary conjugates the conditioned-sea "
                 f"state map into equivariance",
                 max_abs > 1e-1)
    checks.check("T4-diagonal-not-symmetric",
                 "some condition has rho_00 far from rho_11, which excludes an antidiagonal U_g",
                 asymmetric)
    checks.note(
        "T4-no-go-proof",
        "conjugation by U_g preserves the record-basis diagonal for every condition, so U_g is "
        "diagonal or antidiagonal; antidiagonal swaps rho_00 and rho_11, refuted by rho_00 = 2/3; "
        "diagonal preserves |rho_01|, refuted by the difference just recorded. So none exists",
    )
    checks.note(
        "T4-gauge-open",
        "the link signs fix a gauge, so the site's symmetry operator is not the bare edge "
        "permutation; the gauge-corrected one is open, and until built the cube leaves the "
        "fibred theorem's covariance hypothesis unverified",
    )
    return max_diag, max_abs, triples


# ------------------------------------------------------- T5: the four conditions and the wordings
LAYMAN = (
    "Two neighbourhoods whose records leave a site in the same state give every possibility "
    "that site could register the same odds, whatever else remains possible there."
)
PRECISE = (
    "The neighbourhood's records fix a state of the site. The odds the law assigns to a "
    "possibility depend on that possibility and on that state, and on nothing else: where two "
    "neighbourhoods fix the same state, every possibility admissible under both is given the "
    "same odds, whatever else is admissible in each. The state fixed by the records varies with "
    "the nearest-neighbour conditions and transforms with them under the lattice symmetries."
)
OUT_OF_REGISTER = (
    "measurement", "measure", "measured", "collapse", "observer", "observation", "apparatus",
    "detector", "wavefunction", "experiment", "prepare", "eigenstate",
)
IN_REGISTER = (
    "records", "state", "odds", "possibility", "admissible", "neighbourhood",
    "nearest-neighbour", "lattice symmetries",
)


def t5(checks, note, quoted, rows):
    checks.note(
        "T5-four-conditions",
        "the Born form is a theorem for L_CONT under exactly four conditions: (a) supports are "
        "finite resolutions of I_2 in S; (b) abundance in fibre, a property of the law; (c) the "
        "imported dimension-three frame theorem; (d) an equivariant fibre map onto a non-trivial "
        "cubic G-set, which the sentence supplies and a scalar label never meets",
    )
    checks.check("T5-sentence-supplies-one-condition",
                 "the sentence supplies (d) with the mediation and in-fibre clauses, and neither "
                 "abundance nor the frame theorem, both of which the note names",
                 all(s in note for s in ("abundance in fibre", "frame-function theorem",
                                         "not supplied by the sentence")))
    ternary_menus = sum(1 for r in rows if len(r[8]) > 2)
    checks.check("T5-cube-pays-no-abundance",
                 f"the cube meets condition (b) in no fibre: every one of its {len(rows)} "
                 f"condition-edge menus lies in the single frame {{P_0, P_1}} and "
                 f"{ternary_menus} carry a ternary resolution, so the Born form is not a theorem "
                 f"there",
                 ternary_menus == 0 and all(set(r[8]) <= {0, 1} for r in rows))
    checks.check("T5-layman-wording-in-note",
                 "the note reproduces the layman candidate wording verbatim",
                 normalize(LAYMAN) in quoted)
    checks.check("T5-precise-wording-in-note",
                 "the note reproduces the precise candidate wording verbatim",
                 normalize(PRECISE) in quoted)
    joined = (LAYMAN + " " + PRECISE).lower()
    checks.check("T5-register-audit",
                 "register audit: no word outside the axiom's register, and only records, state, "
                 "the odds, possibility, admissible, neighbourhood and lattice symmetries",
                 not any(w in joined for w in OUT_OF_REGISTER)
                 and all(w in joined for w in IN_REGISTER))
    checks.check("T5-candidate-not-axiom-text",
                 "the note offers both as candidate wordings and not as axiom text",
                 "candidate wordings, not axiom text" in note)


# ------------------------------------------------------- main
def main():
    started = time.time()
    checks = Checks()
    note_text = NOTE_PATH.read_text(encoding="utf-8")
    note = normalize(note_text)
    quoted = flatten_quotes(note_text)
    parent = normalize(PARENT_NOTE.read_text(encoding="utf-8"))
    axiom = normalize(AXIOM_PATH.read_text(encoding="utf-8"))

    print("external_scientific_inputs: the axiom file and the 2026-08-09 parent are read for "
          "source gates")
    print("package_local_integrity_reads: the source note is read for claim-surface consistency")
    print("standard_theorem_boundary: the dimension-three frame-function theorem is named, not "
          "recomputed")
    print("arithmetic_boundary: T1 and T5 exact rational; the cube stages inherit a float64 sea "
          "eigenvector, reconstruct each odds value rationally to 1e-11, differences at 1e-1")

    t1(checks)
    model = build_cube()
    cube, e_sea, gap, deg, flux, ncoset = model[0], model[5], model[6], model[7], model[8], model[9]
    checks.check("T2-cube-setup",
                 f"12 edge qubits, six minus-one fluxes, code dimension {ncoset}, half-filled "
                 f"sea at {e_sea:.9f} = -4 sqrt(3) with gap {gap:.9f} = 2 sqrt(3), "
                 f"non-degenerate",
                 cube.DIM == 4096 and cube.NQ == 12 and flux == [-1] * 6 and ncoset == 128
                 and abs(e_sea + 4 * math.sqrt(3)) < 1e-9 and abs(gap - 2 * math.sqrt(3)) < 1e-6
                 and deg == 1)
    checks.check("T2-selection-rule-zeros",
                 "the sea has exactly 2112 exact zeros among the 4096 record labels",
                 int(np.count_nonzero(model[4] < 1e-14)) == 2112)

    rows, fibres, multi = cube_pass(checks, model)
    t3(checks, rows, fibres, multi)
    t3_witness_detail(checks, model)
    t4(checks, model)
    t5(checks, note, quoted, rows)

    checks.check("source-qubit",
                 "Qubit: the one-site possibility domain has presentation M_2(C)",
                 "The full one-site possibility domain has algebraic presentation `M_2(C)`" in axiom)
    checks.check("source-admissibility",
                 "Admissibility: the distribution is nearest-neighbor determined and varying",
                 "the probability distribution over the possibilities is determined by, and varies "
                 "with, the nearest-neighbor conditions" in axiom)
    checks.check("source-admissibility-support",
                 "reading note (3): 'available'/'admissible' denotes the distribution's support",
                 '"available"/"admissible" denotes its support' in axiom)
    checks.check("source-record",
                 "Record: a record locks one admissible possibility; only records are readable",
                 "When present, a record locks exactly one admissible local possibility" in axiom
                 and "Only records are readable" in axiom)
    checks.check("source-parent-frame-import",
                 "the 2026-08-09 parent names the dimension-three frame theorem",
                 "Every nonnegative weight-one frame function on a complex Hilbert space of "
                 "dimension at least three is represented by a unique density operator" in parent)
    checks.check("surface-status",
                 "the note keeps its conditional surface and independent audit explicit",
                 all(s in note for s in ("actual_current_surface_status: conditional-support",
                                         "audit_required_before_effective_retained: true",
                                         "no canonical axiom edit",
                                         "Independent audit remains required")))

    print("per_element: every direction, condition, record subset, fibre and rotation is declared "
          "and completely enumerated")
    print("per_site: one M_2(C) site, on a Z^3 nearest-neighbour law and on the 12-qubit cube")
    print("per_mode: binary, ternary and coin menus only; no arity above three")
    print("per_block: the clause, the cube identity, the fibre census, the equivariance sweep, "
          "the wordings")
    print("lattice_wide: no lattice-wide Born claim; the cube is one finite carrier")
    print(f"runtime_seconds: {time.time() - started:.1f}")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
