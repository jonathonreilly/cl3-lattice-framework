#!/usr/bin/env python3
"""Exact checks: the two-site block criterion of the covariant product rule on Z^3 — the block sensitivities exactly, the
obstruction for every coupling, and silence at the silent triples.

Scope.  Block 03 named the two-site block criterion as the cheapest sharper route toward the silent triples (3, 1, 2),
(5, 2, 4), (7, 3, 5).  Here the pair block V = {x, y} with its ten boundary slots is built from the rule; its x-marginal's
sensitivity rho to one outer slot and the second-order sensitivity rho' of the y-marginal are computed exactly; the
whole-block total variation under a change at an x-slot equals the x-marginal's (the block law factors as marginal times a
conditional that does not see the slot); for every coupling of the two block laws the expected Hamming distance is at
least the sum of the marginal total variations (Theorem N), so the block sum B_V is at least 10 (rho + rho'), which exceeds
the block size 2 at each silent triple: the criterion is silent there for every coupling.  The explicit sequential
coupling gives the upper bound 10 rho (1 + c_1).  Along the lines (t,1,1) and (t,t,1) the sequential number 5 rho (1 + c_1)
crosses 1 in the same scan cell as 6 c_1, and rho exceeds c_1 at strong couplings.  Nothing about uniqueness on Z^3 is
claimed from the block contraction (its Z^3 implication is not proved here).  Exact integer and rational arithmetic only;
the runner scans its own source for floating-point literals and conversion calls.
"""

from __future__ import annotations

import re
import sys
from fractions import Fraction
from itertools import combinations, combinations_with_replacement, product
from math import lcm
from pathlib import Path

AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_TWO_SITE_BLOCK_CRITERION_EXACT_AND_SILENT_FOR_EVERY_COUPLING_BOUNDED_THEOREM_NOTE_2026-09-07.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_RULE_EXACT_UNIQUENESS_REGION_ONE_SITE_CONTRACTION_COUPLING_BOUNDED_THEOREM_NOTE_2026-09-06.md",
)
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / AUDIT_INPUT_PATHS[0]
AXIOM_PATH = ROOT / AUDIT_INPUT_PATHS[1]
BLOCK03_PATH = ROOT / AUDIT_INPUT_PATHS[2]
CLAIM_ID = "admissibility_rule_two_site_block_criterion_exact_and_silent_for_every_coupling_bounded_theorem_note_2026-09-07"
BLOCK03_CLAIM_ID = "admissibility_rule_exact_uniqueness_region_one_site_contraction_coupling_bounded_theorem_note_2026-09-06"
BLOCK03_FRAGMENT = "the criterion is silent"
AXIOM_NEEDLES = (
    "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations.",
    "For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.",
    "Records form.",
    "Only records are readable.",
)

MUTATION_GATE = {
    "block_law_factorization_broken": "B",
    "coupling_marginals_broken": "B",
    "lower_bound_lemma_forged": "B",
    "sequential_upper_bound_forged": "B",
    "rho_literal_off": "C",
    "rho_prime_literal_off": "C",
    "ratio_bounded_by_one_claimed": "C",
    "silent_lower_bound_below_two": "C",
    "region_upper_bound_forged": "C",
    "c1_literal_off": "C",
    "crossing_cell_wrong": "D",
    "ratio_beyond_one_denied": "D",
    "claim_two_site_decides": "E",
    "claim_nonunique_at_silent": "E",
    "claim_phase_transition": "E",
    "claim_author_in_theorem": "E",
}
ACTIVE_MUTATION: str | None = None


def mut(name: str) -> bool:
    if name not in MUTATION_GATE:
        raise KeyError(name)
    return ACTIVE_MUTATION == name


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0
        self.failed_families: list[str] = []

    def check(self, label: str, condition: bool, detail: str) -> None:
        ok = bool(condition)
        self.passed += int(ok)
        self.failed += int(not ok)
        if not ok:
            self.failed_families.append(label[0])
        print(f"{'PASS' if ok else 'FAIL'}: {label} {detail}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def normalize_text(text: str) -> str:
    return " ".join(text.split())


def dec(x: Fraction, digits: int) -> str:
    """Exact decimal expansion rounded down; integer arithmetic; a label, not evidence."""
    sign = "-" if x < 0 else ""
    x = abs(x)
    scaled = (x.numerator * 10 ** digits) // x.denominator
    s = str(scaled).rjust(digits + 1, "0")
    return f"{sign}{s[:-digits]}.{s[-digits:]}"


# --------------------------------------------------------------------- menu and rule (rebuilt, not imported)
MENU_VECTORS = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
M = 6
PAIRS = tuple(combinations(range(M), 2))
SHELLS5 = tuple(combinations_with_replacement(range(M), 5))
SHELLS4 = tuple(combinations_with_replacement(range(M), 4))
SILENT = ((3, 1, 2), (5, 2, 4), (7, 3, 5))
REGION = ((2, 1, 2), (3, 2, 2), (5, 4, 4))
C1_LITERALS = {
    (3, 1, 2): Fraction(270, 989), (5, 2, 4): Fraction(8650000, 40615109), (7, 3, 5): Fraction(6391462, 29948925),
    (2, 1, 2): Fraction(2, 13), (3, 2, 2): Fraction(2079, 15566), (5, 4, 4): Fraction(4000000, 61385721),
}
RHO_LITERALS = {
    (3, 1, 2): Fraction(2168397, 7948400), (5, 2, 4): Fraction(271059507090000, 1298168979740633),
    (7, 3, 5): Fraction(239957740750, 1121635870169), (2, 1, 2): Fraction(67715, 446034),
    (3, 2, 2): Fraction(1471549788, 11145302999), (5, 4, 4): Fraction(81847628000000, 1305850357630907),
}
RHO_PRIME_LITERALS = {
    (3, 1, 2): Fraction(1350, 26077), (5, 2, 4): Fraction(1915425000, 55627392667), (7, 3, 5): Fraction(856455908, 27833079009),
}


def orbit(a: int, b: int) -> int:
    d = sum(x * y for x, y in zip(MENU_VECTORS[a], MENU_VECTORS[b]))
    return 0 if d == 1 else (1 if d == -1 else 2)


def phi_table(triple):
    return [[triple[orbit(a, b)] for b in range(M)] for a in range(M)]


def scaled_triple(triple):
    fr = tuple(Fraction(x) for x in triple)
    L = lcm(*[x.denominator for x in fr])
    return tuple(int(x * L) for x in fr)


def weights(phi, shell):
    w = [1] * M
    for s in range(M):
        acc = 1
        for e in shell:
            acc *= phi[s][e]
        w[s] = acc
    return w


def tv_frac(wa, Za, wb, Zb) -> Fraction:
    return Fraction(sum(abs(wa[s] * Zb - wb[s] * Za) for s in range(M)), 2 * Za * Zb)


def c1_of(triple) -> Fraction:
    """The one-site coefficient of block 03 (252 multisets x 15 pairs)."""
    phi = phi_table(triple)
    best = Fraction(0)
    for eta in SHELLS5:
        base = weights(phi, eta)
        w = [[base[s] * phi[s][t] for s in range(M)] for t in range(M)]
        Z = [sum(x) for x in w]
        for t, t2 in PAIRS:
            v = tv_frac(w[t], Z[t], w[t2], Z[t2])
            if v > best:
                best = v
    return best


def block_joint(phi, eta_y, eta_x_with_slot):
    """Unnormalized block law J[s_x][s_y] = w_x(s_x) phi(s_x, s_y) w_y(s_y) for the ten boundary slots."""
    wy = weights(phi, eta_y)
    wx = weights(phi, eta_x_with_slot)
    return [[wx[a] * phi[a][b] * wy[b] for b in range(M)] for a in range(M)]


def rho_of(triple):
    """sup over y's five outer slots, x's other four outer slots and a pair of values at one outer x-slot of TV(m_x, m_x')."""
    phi = phi_table(triple)
    best, arg = Fraction(0), None
    for eta_y in SHELLS5:
        wy = weights(phi, eta_y)
        h = [sum(phi[a][b] * wy[b] for b in range(M)) for a in range(M)]
        for eta_x in SHELLS4:
            base = weights(phi, eta_x)
            w = [[base[a] * phi[a][t] * h[a] for a in range(M)] for t in range(M)]
            Z = [sum(x) for x in w]
            for t, t2 in PAIRS:
                v = tv_frac(w[t], Z[t], w[t2], Z[t2])
                if v > best:
                    best, arg = v, (eta_y, eta_x, t, t2)
    return best, arg


def rho_prime_of(triple) -> Fraction:
    """sup of TV(m_y, m_y') under a change at one outer x-slot (second order)."""
    phi = phi_table(triple)
    best = Fraction(0)
    for eta_y in SHELLS5:
        for eta_x in SHELLS4:
            mys = []
            for t in range(M):
                J = block_joint(phi, eta_y, eta_x + (t,))
                mys.append(([sum(J[a][b] for a in range(M)) for b in range(M)], sum(sum(r) for r in J)))
            for t, t2 in PAIRS:
                v = tv_frac(mys[t][0], mys[t][1], mys[t2][0], mys[t2][1])
                if v > best:
                    best = v
    return best


def sequential_coupling(J, J2):
    """Explicit coupling of the two block laws (unnormalized joints J, J2 over M x M): the x values by the maximal coupling of
    the x-marginals, then the y values by the maximal coupling of the conditionals K(.|s_x), K2(.|s_x').  Returns the exact
    coupling as a dict ((a,b),(a2,b2)) -> probability, the two normalized laws, and the expected Hamming distance."""
    Z, Z2 = sum(map(sum, J)), sum(map(sum, J2))
    mu = {(a, b): Fraction(J[a][b], Z) for a in range(M) for b in range(M)}
    nu = {(a, b): Fraction(J2[a][b], Z2) for a in range(M) for b in range(M)}
    mx = [sum(mu[(a, b)] for b in range(M)) for a in range(M)]
    nx = [sum(nu[(a, b)] for b in range(M)) for a in range(M)]

    def maximal(p, q):
        m = [min(p[i], q[i]) for i in range(M)]
        common = sum(m)
        cp = {}
        for i in range(M):
            if m[i] > 0:
                cp[(i, i)] = cp.get((i, i), 0) + m[i]
        if common < 1:
            pe = [p[i] - m[i] for i in range(M)]
            qe = [q[i] - m[i] for i in range(M)]
            for i in range(M):
                for j in range(M):
                    if pe[i] > 0 and qe[j] > 0:
                        cp[(i, j)] = cp.get((i, j), 0) + pe[i] * qe[j] / (1 - common)
        return cp

    cx = maximal(mx, nx)
    coupling = {}
    for (a, a2), pa in cx.items():
        K = [mu[(a, b)] / mx[a] for b in range(M)]
        K2 = [nu[(a2, b)] / nx[a2] for b in range(M)]
        for (b, b2), pb in maximal(K, K2).items():
            coupling[((a, b), (a2, b2))] = coupling.get(((a, b), (a2, b2)), 0) + pa * pb
    if mut("coupling_marginals_broken"):
        k0 = next(iter(coupling))
        coupling[k0] = coupling[k0] + Fraction(1, 1000)
    dH = sum(p * ((a != a2) + (b != b2)) for ((a, b), (a2, b2)), p in coupling.items())
    return coupling, mu, nu, dH


def lcg_instances(count: int):
    """A fixed generator (seed 20260907) for boundary instances: y's five slots, x's four slots, the pair at the x-slot."""
    state = 20260907
    out = []
    while len(out) < count:
        v = []
        for _ in range(11):
            state = (1103515245 * state + 12345) % (2 ** 31)
            v.append((state >> 16) % M)
        if v[9] != v[10]:
            out.append((tuple(sorted(v[:5])), tuple(sorted(v[5:9])), v[9], v[10]))
    return out


# ============================================================================================ family A
def family_a(checks: Checks, note_text: str, axiom_text: str, b03_text: str) -> None:
    checks.check("A1", all((ROOT / p).is_file() for p in AUDIT_INPUT_PATHS) and len(set(AUDIT_INPUT_PATHS)) == 3, "the three declared audit inputs exist")
    flat = normalize_text(axiom_text)
    checks.check("A2", all(n in flat for n in AXIOM_NEEDLES), "axiom memo: the Admissibility and Record sentences verbatim")
    checks.check("A3", BLOCK03_CLAIM_ID in b03_text and BLOCK03_FRAGMENT in normalize_text(b03_text), "block 03's note: claim id and the silence fragment")
    checks.check("A4", CLAIM_ID in note_text, "this note carries its claim id")


# ============================================================================================ family B
def family_b(checks: Checks, report: dict) -> None:
    triple = (3, 1, 2)
    phi = phi_table(triple)
    c1 = C1_LITERALS[triple]
    # B1: Theorem O on every instance: TV(joint) == TV(m_x) under a change at an x-slot
    factor_ok, count = True, 0
    for eta_y in SHELLS5:
        wy = weights(phi, eta_y)
        for eta_x in SHELLS4:
            base = weights(phi, eta_x)
            joints, Zs, mxs = [], [], []
            for t in range(M):
                wx = [base[a] * phi[a][t] for a in range(M)]
                J = [[wx[a] * phi[a][b] * wy[b] for b in range(M)] for a in range(M)]
                joints.append(J)
                Zs.append(sum(map(sum, J)))
                mxs.append([sum(J[a]) for a in range(M)])
            for t, t2 in PAIRS:
                if mut("block_law_factorization_broken"):
                    J2 = block_joint(phi, eta_y[:4] + (t2,), eta_x + (t2,))
                else:
                    J2 = joints[t2]
                Z2 = sum(map(sum, J2))
                tv_joint = Fraction(sum(abs(joints[t][a][b] * Z2 - J2[a][b] * Zs[t]) for a in range(M) for b in range(M)), 2 * Zs[t] * Z2)
                tv_marg = tv_frac(mxs[t], Zs[t], [sum(J2[a]) for a in range(M)], Z2)
                count += 1
                if tv_joint != tv_marg:
                    factor_ok = False
                    break
            if not factor_ok:
                break
        if not factor_ok:
            break
    checks.check("B1", factor_ok, f"Theorem O: TV(block law) = TV(x-marginal) under a change at an x-slot on all {count} instances, (3,1,2)")
    # B2-B4: the sequential coupling on the declared family
    fam = lcg_instances(200) + [(RHO_ARG[0], RHO_ARG[1], RHO_ARG[2], RHO_ARG[3])]
    marg_ok, lower_ok, upper_ok = True, True, True
    cK = c1 / 2 if mut("sequential_upper_bound_forged") else c1
    for eta_y, eta_x, t, t2 in fam:
        J, J2 = block_joint(phi, eta_y, eta_x + (t,)), block_joint(phi, eta_y, eta_x + (t2,))
        coupling, mu, nu, dH = sequential_coupling(J, J2)
        left = {}
        right = {}
        for (u, v), p in coupling.items():
            left[u] = left.get(u, 0) + p
            right[v] = right.get(v, 0) + p
        marg_ok = marg_ok and all(left.get(k, 0) == mu[k] for k in mu) and all(right.get(k, 0) == nu[k] for k in nu) and all(p >= 0 for p in coupling.values())
        mx = [sum(mu[(a, b)] for b in range(M)) for a in range(M)]
        nx = [sum(nu[(a, b)] for b in range(M)) for a in range(M)]
        my = [sum(mu[(a, b)] for a in range(M)) for b in range(M)]
        ny = [sum(nu[(a, b)] for a in range(M)) for b in range(M)]
        tvx = sum(abs(p - q) for p, q in zip(mx, nx)) / 2
        tvy = sum(abs(p - q) for p, q in zip(my, ny)) / 2
        lower = 2 * (tvx + tvy) if mut("lower_bound_lemma_forged") else tvx + tvy
        lower_ok = lower_ok and dH >= lower
        upper_ok = upper_ok and dH <= tvx * (1 + cK)
    checks.check("B2", marg_ok, f"the sequential coupling is a coupling (both marginals exact, nonnegative) on {len(fam)} instances")
    checks.check("B3", lower_ok, "Theorem N: E d_H >= TV(m_x) + TV(m_y) on every instance (the marginal lower bound)")
    checks.check("B4", upper_ok, "sequential bound: E d_H <= TV(m_x) (1 + c_1) on every instance")


RHO_ARG = None


# ============================================================================================ family C
def family_c(checks: Checks, report: dict, exact: bool) -> None:
    global RHO_ARG
    c1 = {tr: c1_of(tr) for tr in SILENT + REGION}
    c1_lit = dict(C1_LITERALS)
    if mut("c1_literal_off"):
        c1_lit[(7, 3, 5)] = c1_lit[(7, 3, 5)] + Fraction(1, 10 ** 6)
    checks.check("C1", all(c1[tr] == c1_lit[tr] for tr in c1), "c_1 at the six triples equals block 03's literals (recomputed)")
    rho, args = {}, {}
    for tr in SILENT + REGION:
        rho[tr], args[tr] = rho_of(tr)
    RHO_ARG = args[(3, 1, 2)]
    rho_lit = dict(RHO_LITERALS)
    if mut("rho_literal_off"):
        rho_lit[(3, 1, 2)] = Fraction(2168398, 7948400)
    checks.check("C2", all(rho[tr] == rho_lit[tr] for tr in rho), "rho (the x-marginal's one-slot sensitivity) at the six triples equals the literals")
    print("info rho: " + " ".join(f"({tr[0]},{tr[1]},{tr[2]})={rho[tr]}" for tr in SILENT))
    print("info rho: " + " ".join(f"({tr[0]},{tr[1]},{tr[2]})={rho[tr]}" for tr in REGION))
    ratios = {tr: rho[tr] / c1[tr] for tr in rho}
    print("info rho/c_1: " + " ".join(f"({tr[0]},{tr[1]},{tr[2]})={dec(ratios[tr], 4)}" for tr in SILENT + REGION))
    ratio_claim = all(ratios[tr] <= 1 for tr in ratios) if mut("ratio_bounded_by_one_claimed") else (ratios[(7, 3, 5)] > 1 and all(ratios[tr] < 1 for tr in rho if tr != (7, 3, 5)))
    checks.check("C3", ratio_claim, "rho/c_1 < 1 at five triples and > 1 at (7,3,5): the pair block is not uniformly less sensitive than a site")
    rp = {tr: rho_prime_of(tr) for tr in SILENT}
    rp_lit = dict(RHO_PRIME_LITERALS)
    if mut("rho_prime_literal_off"):
        rp_lit[(3, 1, 2)] = Fraction(1351, 26077)
    checks.check("C4", all(rp[tr] == rp_lit[tr] for tr in rp), "rho' (the y-marginal's sensitivity to an x-slot) at the three silent triples equals the literals")
    print("info rho': " + " ".join(f"({tr[0]},{tr[1]},{tr[2]})={rp[tr]}" for tr in SILENT))
    lower = {tr: 10 * (rho[tr] + rp[tr]) for tr in SILENT}
    upper = {tr: 10 * rho[tr] * (1 + c1[tr]) for tr in SILENT}
    two = Fraction(2)
    silent_ok = all(lower[tr] > (two + 1 if mut("silent_lower_bound_below_two") else two) for tr in SILENT) and all(lower[tr] <= upper[tr] for tr in SILENT)
    print("info B_V bounds at the silent triples: " + "; ".join(f"({tr[0]},{tr[1]},{tr[2]}) [{dec(lower[tr], 4)}, {dec(upper[tr], 4)}]" for tr in SILENT))
    checks.check("C5", silent_ok, "Theorem N: B_V >= 10(rho + rho') > 2 = |V| at each silent triple: the two-site criterion is silent for every coupling")
    region_upper = {tr: 10 * rho[tr] * (1 + c1[tr]) for tr in REGION}
    bound = Fraction(1) if mut("region_upper_bound_forged") else two
    print("info B_V upper bound at the region triples: " + "; ".join(f"({tr[0]},{tr[1]},{tr[2]}) {dec(region_upper[tr], 4)}" for tr in REGION))
    checks.check("C6", all(region_upper[tr] < bound for tr in REGION), "the sequential upper bound 10 rho (1 + c_1) is below 2 at the three region triples")
    if exact:
        for tr in SILENT + REGION:
            print(f"exact rho{tr} = {rho[tr]} argmax {args[tr]} c_1 = {c1[tr]} ratio = {ratios[tr]}")
        for tr in SILENT:
            print(f"exact rho'{tr} = {rp[tr]}; B_V in [{lower[tr]}, {upper[tr]}]")
    report["C"] = {"c1": c1, "rho": rho, "rp": rp}


# ============================================================================================ family D
SCAN = tuple(Fraction(k, 20) for k in range(21, 40))
LINES = (("(t,1,1)", lambda t: (t, 1, 1), (Fraction(8, 5), Fraction(33, 20)), Fraction(39, 20)),
         ("(t,t,1)", lambda t: (t, t, 1), (Fraction(29, 20), Fraction(3, 2)), Fraction(3, 2)))


def family_d(checks: Checks, exact: bool) -> None:
    cells_ok, beyond_ok = True, True
    for name, line, cell, beyond in LINES:
        vals = []
        for t in SCAN:
            tr = scaled_triple(line(t))
            c = c1_of(tr)
            r = rho_of(tr)[0]
            vals.append((t, 6 * c, 5 * r * (1 + c), r / c))
        cross_one = [(vals[i][0], vals[i + 1][0]) for i in range(len(vals) - 1) if (vals[i][1] < 1) != (vals[i + 1][1] < 1)]
        cross_two = [(vals[i][0], vals[i + 1][0]) for i in range(len(vals) - 1) if (vals[i][2] < 1) != (vals[i + 1][2] < 1)]
        expected_cell = (cell[0] + Fraction(1, 20), cell[1] + Fraction(1, 20)) if mut("crossing_cell_wrong") else cell
        cells_ok = cells_ok and cross_one == [expected_cell] and cross_two == [expected_cell]
        first_beyond = next((t for t, _, _, ratio in vals if ratio > 1), None)
        if mut("ratio_beyond_one_denied"):
            beyond_ok = beyond_ok and first_beyond is None
        else:
            beyond_ok = beyond_ok and first_beyond == beyond and all(ratio > 1 for t, _, _, ratio in vals if t >= beyond)
        print(f"info {name}: 6c_1 and 5rho(1+c_1) both cross 1 in ({cell[0]}, {cell[1]}); rho/c_1 > 1 from t = {first_beyond}")
        if exact:
            print(f"exact {name}: " + "; ".join(f"t={t} 6c1={dec(a, 5)} two={dec(b, 5)} ratio={dec(r, 5)}" for t, a, b, r in vals))
    checks.check("D1", cells_ok, "the sequential number 5rho(1+c_1) crosses 1 in the same scan cell as 6c_1 on (t,1,1) and (t,t,1)")
    checks.check("D2", beyond_ok, "rho/c_1 exceeds 1 from t = 39/20 on (t,1,1) and from t = 3/2 on (t,t,1) on the declared scan")


# ============================================================================================ family E
FENCES = (
    "This note states that the two-site block criterion is silent at the three silent triples for every coupling of the block laws; it states nothing about one law or several there, and nothing about uniqueness on the cubic lattice from the block contraction, whose infinite-lattice implication is not proved here.",
    "No formation order, formation law, plane, bridge, Born or gravity statement enters this note; this note does not fire wake condition 1 of the parked statistical-bridge decision.",
    "The block criterion and the Hamming coupling distance are classical references re-proved here at the scope used; no value, constant or theorem is imported as authority.",
)
FORBIDDEN = (
    "non-unique", "nonunique", "phase transition", "several static laws", "the physical rule", "certified",
    "unique at (3,1,2)", "unique at (5,2,4)", "unique at (7,3,5)", "unique at the silent", "decides uniqueness",
    "selects the physical rule", "derives the Born", "fires wake condition", "the framework's action is", "closed the gate",
)
CLAIM_INJECTIONS = {
    "claim_two_site_decides": "The two-site block criterion decides uniqueness at (5,2,4).",
    "claim_nonunique_at_silent": "At (3,1,2) the static law is non-unique.",
    "claim_phase_transition": "The silent triples lie beyond a phase transition.",
}
AUTHOR_NAME = "dobrushin"
AUTHOR_SECTIONS = ("Prior art", "Imports")
SCAN_MARKER = "float-scan-marker-line"


def author_outside_allowed(note_text: str) -> list:
    parts = re.split(r"(?m)^## ", note_text)
    bad = []
    if AUTHOR_NAME in parts[0].lower():
        bad.append("<front matter or title>")
    for part in parts[1:]:
        heading = part.split("\n", 1)[0].strip()
        if AUTHOR_NAME in part.lower() and not heading.startswith(AUTHOR_SECTIONS):
            bad.append(heading)
    return bad


def family_e(checks: Checks, note_text: str) -> None:
    text = note_text
    for name, phrase in CLAIM_INJECTIONS.items():
        if mut(name):
            text = text + "\n" + phrase
    if mut("claim_author_in_theorem"):
        text = text.replace("\n## Theorem N", "\nBy Dobrushin's theorem the bound holds.\n## Theorem N", 1)
    flat = normalize_text(text)
    checks.check("E1", all(f in flat for f in FENCES), "the note carries the three fence sentences verbatim")
    hits = [ph for ph in FORBIDDEN if ph.lower() in flat.lower()]
    checks.check("E2", not hits, f"the note contains no forbidden phrase (hits: {hits})")
    bad = author_outside_allowed(text)
    checks.check("E3", not bad and len(text) > 0, f"the criterion's author is named only in the Prior art and Imports sections (violations: {bad})")
    source_lines = Path(__file__).read_text(encoding="utf-8").splitlines()
    scan = [ln for ln in source_lines if SCAN_MARKER not in ln]
    float_literal = re.compile(r"(?<![\w.])\d+\.\d+(?![\w.])|(?<![\w.])\d+[eE][-+]?\d+(?![\w.])")
    conversion = "flo" + "at("  # float-scan-marker-line
    evalf = "eva" + "lf("  # float-scan-marker-line
    numeric = "N" + "("  # float-scan-marker-line
    bad_lines = [ln for ln in scan if float_literal.search(ln) or conversion in ln or evalf in ln or numeric in ln]
    checks.check("E4", not bad_lines and len(scan) > 300, f"runner source: no floating-point literal or conversion call ({len(bad_lines)} hits)")


# ============================================================================================ family F
N5_LINES = (
    "per_element: executed — every boundary instance (252 x 126 multisets x 15 pairs) at each triple for rho and rho'; the factorization on every instance at (3,1,2)",
    "per_site: executed — the x-marginal and the y-marginal sensitivities separately; the coupling's x and y disagreement probabilities",
    "per_mode: executed — the sequential coupling built explicitly on 201 instances with exact marginals and Hamming distance",
    "per_block: executed — the two-site block with its ten boundary slots; the block sum bounds at six triples; the scans on two lines",
    "lattice_wide: not claimed — the block contraction's implication on Z^3 is not proved here; the silence at the three triples is a finite exact statement for every coupling",
)


def family_f(checks: Checks) -> None:
    for line in N5_LINES:
        print(line)
    checks.check("F1", len(N5_LINES) == 5 and all(len(l) >= 40 for l in N5_LINES), "the five N5 resolution lines are printed")


def main(argv) -> int:
    global ACTIVE_MUTATION
    if "--list-mutations" in argv:
        for name, fam in MUTATION_GATE.items():
            print(f"{name} {fam}")
        return 0
    if "--mutation" in argv:
        ACTIVE_MUTATION = argv[argv.index("--mutation") + 1]
        if ACTIVE_MUTATION not in MUTATION_GATE:
            print(f"unknown mutation {ACTIVE_MUTATION}")
            return 2
    exact = "--exact" in argv
    checks = Checks()
    note_text = NOTE_PATH.read_text(encoding="utf-8") if NOTE_PATH.is_file() else ""
    axiom_text = AXIOM_PATH.read_text(encoding="utf-8") if AXIOM_PATH.is_file() else ""
    b03_text = BLOCK03_PATH.read_text(encoding="utf-8") if BLOCK03_PATH.is_file() else ""
    print("AUDIT_INPUT_PATHS:")
    for p in AUDIT_INPUT_PATHS:
        print(f"  {p}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("scope: the two-site block of the covariant product rule; rho, rho' exactly; B_V >= 10(rho + rho') > 2 at (3,1,2), (5,2,4), (7,3,5): silent for every coupling; nothing on Z^3 uniqueness")
    print(f"mutation: {ACTIVE_MUTATION or 'none'}")
    report: dict = {}
    family_a(checks, note_text, axiom_text, b03_text)
    family_c(checks, report, exact)
    family_b(checks, report)
    family_d(checks, exact)
    family_e(checks, note_text)
    family_f(checks)
    if ACTIVE_MUTATION:
        observed = "".join(sorted(set(checks.failed_families))) or "none"
        print(f"mutation_family_expected: {MUTATION_GATE[ACTIVE_MUTATION]}")
        print(f"mutation_family_observed: {observed}")
    failed = checks.finish()
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
