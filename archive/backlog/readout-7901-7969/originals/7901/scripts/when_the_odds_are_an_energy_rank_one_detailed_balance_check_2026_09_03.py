#!/usr/bin/env python3
"""When the odds are an energy: rank-one and detailed-balance tests for
breakable neighbourhood conditions.

Class-A finite-object runner, self-contained.  Nothing is derived from any
axiom; every object below is DECLARED here and derived from nothing.

  THE COARSE TORUS.  Z_L^3 at L = 8: 512 sites, nearest-neighbour adjacency,
  coordination 6, bipartite.  A GROUP OF RECORDS is a finite set of occupied
  sites, one record each.  A(S) counts adjacent record pairs and
  B(S) = (n-1) - A(S), exact for n <= 3.  Groups: the dimer (n = 2) and the
  bent trimer {(0,0,0), (1,0,0), (1,1,0)} (n = 3).

  A PROPOSAL is (which record shifts, one of the 6 unit directions d).  The
  target is t = source + d.  A target carrying a record makes the tick NULL.
  Otherwise the shift is registered with odds

      P(shift registered | proposal) = (1/n) p_prop(d) Acc(c, D),
      Acc(c, D) = min(1, e^{-w(c, D)}).

  D = dB = B(new) - B(old) = adjacencies broken minus made -- the
  CONFIGURATION CHANGE.  Writing A(others) for the adjacency the two records
  that do not shift already carry, A(old) = A(others) + m_s and
  A(new) = A(others) + m_t, so D = m_s - m_t exactly.

  THE NEIGHBOURHOOD CONDITION c has four declared coordinates:
      m_t  records other than the mover adjacent to the TARGET   (0, 1, 2)
      m_s  records adjacent to the mover's SOURCE before the shift (0, 1, 2)
      s    +1 for d = +x, -1 for d = -x, 0 otherwise
      a    (x+y+z) mod 2 of the mover's SOURCE site -- the declared
           two-sublattice ACTIVITY.

  FOUR DECLARED TABLES of log-odds w(c, D).  Constants g0 = 1, mu = 1/2,
  nu = 1/4; g, h, kappa swept.  All rational, so every odds matrix has an
  EXACT RANK OVER Q by Fraction row reduction.

      A   separable, the control:  w = beta(c) D,
          beta(c) = g0 (1 + mu m_t)(1 + nu a);  uniform proposal 1/6.
      B   PR #7899's Metropolis rule BR(g, h, 1):  w = g D; the field is in
          the PROPOSAL, p_prop(d) = e^{h[d = +x]}/(5 + e^{h}).
      C   non-separable, TARGET crowding:  w = g D + kappa D^2 1[m_t >= 1]
          + h s;  uniform proposal, so the field is in the ODDS.
      C'  non-separable, MOVER crowding:  w = g D + kappa D^2 1[m_s >= 2]
          + h s;  uniform proposal.  Declared in response to a computed
          degeneracy of C on the bent trimer, not fitted to a target.

  THE MATRIX UNDER TEST, in the gauge that fixes the constant:
      M_acc(c, D) = -ln Acc(c, D) = max(0, w(c, D))
      M_rel(c, D) = M_acc(c, D) - M_acc(c, 0)
  M_rel is the extra log-odds of separating at the same neighbourhood.  The
  raw -ln of the odds carries the additive ln 6 or ln p_prop, which makes it
  rank >= 2 for EVERY table with no energy content; the D = 0 column is
  subtracted throughout.

  THE CHAINS, all classical record-pattern chains, largest 1022 x 1022:
   (1) the dimer RELATIVE chain, 511 states r = v - u.  Valid only for a
       fully translation-covariant table (B, C, C'); table A reads the
       declared sublattice, so this lumping is not a reduction for it.
   (2) the dimer FULL chain reduced by EVEN translations, state (p, r) with
       p the parity of record 1's site: 2 x 511 = 1022 classes.  Even
       translations are an exact symmetry of every declared table, so every
       4-cycle of the absolute chain is an even translate of one of these.
   (3) the WINDING cycles of length L = 8 in chain (2).
   (4) the TRIMER chain on ABSOLUTE configurations, no lumping: the declared
       finite subgraph of 4-cycles based at the bent trimer and at each of
       its one-tick successors.

Records are PERMANENT.  Every sentence below in which a record SHIFTS sits
inside a STIPULATED tick model, declared as such, whose axiom cost is the one
PR #7889 names and hands to its owner.  A record REGISTERS a value at a site;
it does not report one the site already had.

Check groups:
  A  T1  the rank-one test on M_rel: exact ranks over Q, the derived energy
         E(D) = max(0, D) and the temperatures, and the dimer trap.
  B  T2  Kolmogorov's cycle criterion on all four chains, the exact scaling
         of every violation, the stationary laws, and the lumping trap.
  C  T3  Arrhenius / van 't Hoff on the bent trimer's two break channels.
  D  T4  reproduction of PR #7899's closed forms by table B.

Line tags.  `[exact]` = integer or `Fraction` arithmetic with no floating
point in the statement.  `[numerical]` = a deterministic double-precision
evaluation of an exactly specified quantity at a stated threshold.  There is
no sampling, no seed and no random number anywhere in this runner, and no
line is a witness.

Output: one PASS/FAIL line per check and a final `TOTAL: PASS=N FAIL=M`.
Exit code 0 iff FAIL = 0.
"""

from __future__ import annotations

import math
import sys
from fractions import Fraction as Fr

import numpy as np

AUDIT_TIMEOUT_SEC = 150

PASS = 0
FAIL = 0


def check(label, cond):
    """Record and print one check."""
    global PASS, FAIL
    ok = bool(cond)
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print(("PASS " if ok else "FAIL ") + label)


# ============================================================== the L^3 torus

L = 8
NSITE = L ** 3
DIRS = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
NEGK = [1, 0, 3, 2, 5, 4]
SGNK = [1, -1, 0, 0, 0, 0]


def pack(v):
    return (v[0] % L) * L * L + (v[1] % L) * L + (v[2] % L)


def unpack(i):
    return (i // (L * L), (i // L) % L, i % L)


SITE = [unpack(i) for i in range(NSITE)]
PAR = [sum(SITE[i]) % 2 for i in range(NSITE)]
NBR = [[pack((SITE[i][0] + d[0], SITE[i][1] + d[1], SITE[i][2] + d[2]))
        for d in DIRS] for i in range(NSITE)]
ADJ = [bytearray(NSITE) for _ in range(NSITE)]
for _i in range(NSITE):
    for _j in NBR[_i]:
        ADJ[_i][_j] = 1
ADJ0 = ADJ[0]                       # ADJ0[r] = 1 iff the relative vector r is a unit step
REL = list(range(1, NSITE))         # the 511 nonzero relative vectors
BENT = (pack((0, 0, 0)), pack((1, 0, 0)), pack((1, 1, 0)))

# ------------------------------------------- the four declared tables of odds

G0, MU, NU = Fr(1), Fr(1, 2), Fr(1, 4)


def wA(mt, s, a, D, g=Fr(1), h=Fr(0), kap=Fr(1, 2)):
    return G0 * (1 + MU * mt) * (1 + NU * a) * D


def wB(mt, s, a, D, g=Fr(1), h=Fr(0), kap=Fr(1, 2)):
    return g * D


def wC(mt, s, a, D, g=Fr(1), h=Fr(0), kap=Fr(1, 2)):
    return g * D + kap * D * D * (1 if mt >= 1 else 0) + h * s


def wCp(ms, s, D, g=Fr(1), h=Fr(0), kap=Fr(1, 2)):
    return g * D + kap * D * D * (1 if ms >= 2 else 0) + h * s


def pprop(table, s, h):
    """The declared proposal odds for one direction."""
    if table != "B":
        return 1.0 / 6.0
    eh = math.exp(float(h))
    return (eh if s == 1 else 1.0) / (5.0 + eh)


def acc_f(w):
    return 1.0 if w <= 0.0 else math.exp(-w)


# ============================================ the occurring (c, D) cells

def dimer_cells():
    """Every (m_t, s, a, D) and (m_s, s, D) that occurs for the dimer over the
    whole L = 8 torus: all 511 relative vectors x 2 parities x 2 movers x 6
    directions, blocked targets dropped."""
    ct, cs, npr = set(), set(), 0
    for r in REL:
        ms = ADJ0[r]
        for k in range(6):
            s = SGNK[k]
            r1 = NBR[r][NEGK[k]]        # record 1 shifts by d: r -> r - d
            r2 = NBR[r][k]              # record 2 shifts by d: r -> r + d
            for (rn, moved_first) in ((r1, True), (r2, False)):
                if rn == 0:
                    continue            # the target carries the other record
                mt = ADJ0[rn]
                D = ms - mt
                for p in (0, 1):
                    a = p if moved_first else (p + PAR[r]) % 2
                    ct.add((mt, s, a, D))
                cs.add((ms, s, D))
                npr += 2
    return ct, cs, npr


def trimer_cells():
    """Every (m_t, s, a, D) and (m_s, s, D) that occurs for 3-record groups
    over the whole torus.  One pass over all C(511,2) = 130305 translation
    class representatives {0, x, y} x 2 parities x 3 movers x 6 directions."""
    ct, cs, npr = set(), set(), 0
    for i in range(1, NSITE):
        Ai = ADJ[i]
        pi = PAR[i]
        for j in range(i + 1, NSITE):
            cfg = (0, i, j)
            pcfg = (0, pi, PAR[j])
            for wi in range(3):
                src = cfg[wi]
                o1, o2 = [cfg[k] for k in range(3) if k != wi]
                As = ADJ[src]
                ms = As[o1] + As[o2]
                asrc = pcfg[wi]
                nb = NBR[src]
                for k in range(6):
                    t = nb[k]
                    if t == o1 or t == o2:
                        continue
                    At = ADJ[t]
                    mt = At[o1] + At[o2]
                    D = ms - mt         # = A(old) - A(new), the two others' bond cancels
                    s = SGNK[k]
                    for p in (0, 1):
                        ct.add((mt, s, (p + asrc) % 2, D))
                    cs.add((ms, s, D))
                    npr += 2
    return ct, cs, npr


# ================================================== exact rank over Q and SVD

def exact_rank(rows):
    """Rank over Q of a matrix of Fractions, by exact row reduction."""
    M = [list(r) for r in rows]
    R = len(M)
    C = len(M[0]) if R else 0
    rk = 0
    for col in range(C):
        piv = None
        for i in range(rk, R):
            if M[i][col] != 0:
                piv = i
                break
        if piv is None:
            continue
        M[rk], M[piv] = M[piv], M[rk]
        pv = M[rk][col]
        for i in range(R):
            if i != rk and M[i][col] != 0:
                f = M[i][col] / pv
                for k in range(col, C):
                    M[i][k] -= f * M[rk][k]
        rk += 1
        if rk == R:
            break
    return rk


def sv_ratio(rows):
    """(sigma_2/sigma_1, best rank-one relative residual) of a Fraction matrix."""
    Mf = np.array([[float(v) for v in r] for r in rows], dtype=float)
    sv = np.linalg.svd(Mf, compute_uv=False)
    s1 = float(sv[0])
    s2 = float(sv[1]) if len(sv) > 1 else 0.0
    tail = math.sqrt(max(0.0, float((sv[1:] ** 2).sum())))
    fro = math.sqrt(float((sv ** 2).sum()))
    return (s2 / s1 if s1 > 0 else 0.0), (tail / fro if fro > 0 else 0.0)


def odds_matrix(cells, table, g, h, kap):
    """(conditions, D values, M_acc, M_rel) for one declared table."""
    if table == "Cp":
        cond = sorted({(c[0], c[1]) for c in cells})
        Ds = sorted({c[2] for c in cells})

        def w(c, D):
            return wCp(c[0], c[1], D, g, h, kap)
    else:
        cond = sorted({(c[0], c[1], c[2]) for c in cells})
        Ds = sorted({c[3] for c in cells})
        base = {"A": wA, "B": wB, "C": wC}[table]

        def w(c, D):
            return base(c[0], c[1], c[2], D, g, h, kap)

    Macc = [[max(Fr(0), w(c, D)) for D in Ds] for c in cond]
    Mrel = [[max(Fr(0), w(c, D)) - max(Fr(0), w(c, 0)) for D in Ds]
            for c in cond]
    return cond, Ds, Macc, Mrel


def energy_and_temperatures(cond, Ds, M):
    """Where M is rank one, the factorisation M = beta(c) x E(D) in the gauge
    E(D = +1) = 1.  Returns (E, {c: beta}) or None."""
    if exact_rank(M) != 1:
        return None
    j1 = Ds.index(1)
    col = [M[i][j1] for i in range(len(cond))]
    i0 = max(range(len(cond)), key=lambda i: col[i])
    E = [M[i0][j] / M[i0][j1] for j in range(len(Ds))]
    return E, {cond[i]: col[i] for i in range(len(cond))}


# ======================================================== the classical chains

def dimer_full_edges(table, g, h, kap):
    """Out-edges of chain (2), the 1022 even-translation classes (p, r)."""
    n = len(REL)
    E = [dict() for _ in range(2 * n)]
    base = {"A": wA, "B": wB, "C": wC}.get(table)
    for r in REL:
        ms = ADJ0[r]
        for p in (0, 1):
            i = p * n + (r - 1)
            for k in range(6):
                s = SGNK[k]
                pp = pprop(table, s, h)
                for moved_first in (True, False):
                    rn = NBR[r][NEGK[k]] if moved_first else NBR[r][k]
                    if rn == 0:
                        continue
                    mt = ADJ0[rn]
                    D = ms - mt
                    a = p if moved_first else (p + PAR[r]) % 2
                    pn = 1 - p if moved_first else p
                    if table == "Cp":
                        w = float(wCp(ms, s, D, g, h, kap))
                    else:
                        w = float(base(mt, s, a, D, g, h, kap))
                    j = pn * n + (rn - 1)
                    E[i][j] = E[i].get(j, 0.0) + 0.5 * pp * acc_f(w)
    return E


def dimer_rel_edges(table, g, h, kap):
    """Out-edges of chain (1), the 511 relative classes.  A valid reduction
    only for a translation-covariant table."""
    n = len(REL)
    E = [dict() for _ in range(n)]
    base = {"A": wA, "B": wB, "C": wC}.get(table)
    for r in REL:
        ms = ADJ0[r]
        i = r - 1
        for k in range(6):
            s = SGNK[k]
            pp = pprop(table, s, h)
            for moved_first in (True, False):
                rn = NBR[r][NEGK[k]] if moved_first else NBR[r][k]
                if rn == 0:
                    continue
                mt = ADJ0[rn]
                D = ms - mt
                if table == "Cp":
                    w = float(wCp(ms, s, D, g, h, kap))
                else:
                    w = float(base(mt, s, 0, D, g, h, kap))
                E[i][rn - 1] = E[i].get(rn - 1, 0.0) + 0.5 * pp * acc_f(w)
    return E


def cycles4(E, label=""):
    """Every distinct 4-cycle x0 -> x1 -> x2 -> x3 -> x0 of distinct states;
    returns (count, max |ln(product forward / product backward)|)."""
    best = 0.0
    ncyc = 0
    seen = set()
    for x0 in range(len(E)):
        e0 = E[x0]
        for x1 in e0:
            if x1 == x0:
                continue
            e1 = E[x1]
            for x2 in e1:
                if x2 == x0 or x2 == x1:
                    continue
                e2 = E[x2]
                for x3 in e2:
                    if x3 == x0 or x3 == x1 or x3 == x2:
                        continue
                    e3 = E[x3]
                    if x0 not in e3:
                        continue
                    key = min((x0, x1, x2, x3), (x1, x2, x3, x0),
                              (x2, x3, x0, x1), (x3, x0, x1, x2),
                              (x0, x3, x2, x1), (x3, x2, x1, x0),
                              (x2, x1, x0, x3), (x1, x0, x3, x2))
                    if key in seen:
                        continue
                    seen.add(key)
                    ncyc += 1
                    f = e0[x1] * e1[x2] * e2[x3] * e3[x0]
                    b = e0.get(x3, 0.0) * e3.get(x2, 0.0) * \
                        e2.get(x1, 0.0) * e1.get(x0, 0.0)
                    if f <= 0.0 or b <= 0.0:
                        continue
                    v = abs(math.log(f / b))
                    if v > best:
                        best = v
    return ncyc, best


def winding(table, g, h, kap):
    """The length-L cycles of chain (2): record 2 shifts +x L times and
    returns.  The mover's source parity is tracked, so table A is read with
    its declared activity."""
    base = {"A": wA, "B": wB, "C": wC}.get(table)
    best = 0.0
    n = 0
    for r0 in REL:
        seq = []
        rr = r0
        ok = True
        for _ in range(L):
            rn = NBR[rr][0]
            if rn == 0:
                ok = False
                break
            seq.append((rr, rn))
            rr = rn
        if not ok or rr != r0:
            continue
        n += 1
        for p in (0, 1):
            f = b = 1.0
            for (ra, rb) in seq:
                a = (p + PAR[ra]) % 2
                D = ADJ0[ra] - ADJ0[rb]
                w = float(wCp(ADJ0[ra], 1, D, g, h, kap)) if table == "Cp" \
                    else float(base(ADJ0[rb], 1, a, D, g, h, kap))
                f *= pprop(table, 1, h) * acc_f(w)
            for (ra, rb) in reversed(seq):
                a = (p + PAR[rb]) % 2
                D = ADJ0[rb] - ADJ0[ra]
                w = float(wCp(ADJ0[rb], -1, D, g, h, kap)) if table == "Cp" \
                    else float(base(ADJ0[ra], -1, a, D, g, h, kap))
                b *= pprop(table, -1, h) * acc_f(w)
            best = max(best, abs(math.log(f / b)))
    return n, best


def trimer_out(cfg, table, g, h, kap):
    """The one-tick successors of an absolute 3-record configuration, with the
    odds of registering each."""
    base = {"A": wA, "B": wB, "C": wC}.get(table)
    res = {}
    for wi in range(3):
        src = cfg[wi]
        o1, o2 = [cfg[k] for k in range(3) if k != wi]
        ms = ADJ[src][o1] + ADJ[src][o2]
        a = PAR[src]
        for k in range(6):
            t = NBR[src][k]
            if t == o1 or t == o2:
                continue
            mt = ADJ[t][o1] + ADJ[t][o2]
            D = ms - mt
            s = SGNK[k]
            w = float(wCp(ms, s, D, g, h, kap)) if table == "Cp" \
                else float(base(mt, s, a, D, g, h, kap))
            new = tuple(sorted((t, o1, o2)))
            res[new] = res.get(new, 0.0) + \
                (1.0 / 3.0) * pprop(table, s, h) * acc_f(w)
    return res


def trimer_cycles(table, g, h, kap):
    """The declared finite subgraph: 4-cycles based at the bent trimer and at
    each of its one-tick successors, on absolute configurations."""
    cache = {}

    def out(c):
        if c not in cache:
            cache[c] = trimer_out(c, table, g, h, kap)
        return cache[c]

    starts = [BENT] + sorted(out(BENT).keys())
    best = 0.0
    ncyc = 0
    seen = set()
    for x0 in starts:
        for x1 in out(x0):
            if x1 == x0:
                continue
            for x2 in out(x1):
                if x2 in (x0, x1):
                    continue
                for x3 in out(x2):
                    if x3 in (x0, x1, x2):
                        continue
                    if x0 not in out(x3):
                        continue
                    key = min((x0, x1, x2, x3), (x1, x2, x3, x0),
                              (x2, x3, x0, x1), (x3, x0, x1, x2),
                              (x0, x3, x2, x1), (x3, x2, x1, x0),
                              (x2, x1, x0, x3), (x1, x0, x3, x2))
                    if key in seen:
                        continue
                    seen.add(key)
                    ncyc += 1
                    f = out(x0)[x1] * out(x1)[x2] * out(x2)[x3] * out(x3)[x0]
                    b = out(x0)[x3] * out(x3)[x2] * out(x2)[x1] * out(x1)[x0]
                    best = max(best, abs(math.log(f / b)))
    return ncyc, best


def stationary(E, nstates):
    """The stationary law of the row-stochastic chain built from E, by a
    linear solve with the normalisation replacing one equation."""
    P = np.zeros((nstates, nstates))
    for i in range(nstates):
        tot = 0.0
        for j, v in E[i].items():
            P[i, j] += v
            tot += v
        P[i, i] += 1.0 - tot            # null ticks and unregistered proposals
    Amat = (P.T - np.eye(nstates))
    Amat[-1, :] = 1.0
    rhs = np.zeros(nstates)
    rhs[-1] = 1.0
    pi = np.linalg.solve(Amat, rhs)
    for _ in range(3):                  # iterative refinement, so the small
        pi = pi + np.linalg.solve(Amat, rhs - Amat @ pi)   # entries are solved
    return P, pi, float(np.abs(pi @ P - pi).max())


def gibbs_gap(pi, gval, nstates):
    """max_i |pi_i - pi^Gibbs_i| / max pi^Gibbs for pi^Gibbs ~ e^{-g B}."""
    n = len(REL)
    Bv = np.array([0.0 if ADJ0[REL[i % n]] else 1.0 for i in range(nstates)])
    wg = np.exp(-gval * Bv)
    pg = wg / wg.sum()
    return float(np.abs(pi - pg).max() / pg.max())


def bent_channels(table, g, h, kap):
    """Out of the bent trimer: the acceptance of every unblocked proposal,
    grouped by D, with the (m_s, m_t) census of the breaking proposals."""
    base = {"A": wA, "B": wB, "C": wC}.get(table)
    ch, cen, nblock = {}, {}, 0
    for wi in range(3):
        src = BENT[wi]
        o1, o2 = [BENT[k] for k in range(3) if k != wi]
        ms = ADJ[src][o1] + ADJ[src][o2]
        a = PAR[src]
        for k in range(6):
            t = NBR[src][k]
            if t == o1 or t == o2:
                nblock += 1
                continue
            mt = ADJ[t][o1] + ADJ[t][o2]
            D = ms - mt
            s = SGNK[k]
            w = float(wCp(ms, s, D, g, h, kap)) if table == "Cp" \
                else float(base(mt, s, a, D, g, h, kap))
            ch.setdefault(D, []).append(acc_f(w))
            if D > 0:
                cen.setdefault(D, set()).add((ms, mt))
    return ch, cen, nblock


def activations(ch):
    """a(D) = -ln(mean acceptance in channel D), for the breaking channels."""
    return {D: -math.log(sum(v) / len(v)) for D, v in ch.items() if D > 0}


# ==================================================== group A -- T1, rank one

STORE = {}


def group_A():
    dct, dcs, dnp = dimer_cells()
    tct, tcs, tnp = trimer_cells()
    STORE["cells"] = (dct, dcs, tct, tcs)
    dD = sorted({c[3] for c in dct})
    tD = sorted({c[3] for c in tct})
    ncp = len({(c[0], c[1]) for c in tcs})
    check("A1 [exact] occurring (c, D) cells, by complete enumeration over the L = 8 torus: DIMER "
          "%d cells over %d unblocked proposals, D in %s, m_t in %s; 3-record %d cells over %d "
          "proposals (all %d {0,x,y} representatives), D in %s, m_t in %s; %d conditions (m_s, s) "
          "for table C'"
          % (len(dct), dnp, dD, sorted({c[0] for c in dct}), len(tct), tnp,
             len(REL) * (len(REL) - 1) // 2, tD, sorted({c[0] for c in tct}), ncp),
          len(dct) == 18 and dnp == 12240 and dD == [-1, 0, 1] and len(tct) == 36
          and tnp == 4672620 and tD == [-2, -1, 0, 1, 2] and ncp == 9)

    res = {}
    for tab in ("A", "B", "C"):
        for grp, cells in (("dimer", dct), ("3-record", tct)):
            for hv in (Fr(0), Fr(1)):
                cond, Ds, Macc, Mrel = odds_matrix(cells, tab, Fr(1), hv, Fr(1, 2))
                r2r1, resid = sv_ratio(Mrel)
                res[(tab, grp, hv)] = (exact_rank(Mrel), r2r1, resid,
                                       energy_and_temperatures(cond, Ds, Mrel),
                                       len(cond), len(Ds), Ds)
    for kv in (Fr(1, 2), Fr(1)):
        cond, Ds, Macc, Mrel = odds_matrix(tcs, "Cp", Fr(1), Fr(0), kv)
        r2r1, resid = sv_ratio(Mrel)
        res[("Cp", "3-record", kv)] = (exact_rank(Mrel), r2r1, resid, None,
                                       len(cond), len(Ds), Ds)
    cond, Ds, _, Mrel = odds_matrix(tcs, "Cp", Fr(1), Fr(1), Fr(1, 2))
    res[("Cp", "3-record", "h1")] = (exact_rank(Mrel), sv_ratio(Mrel)[0], 0.0,
                                     None, len(cond), len(Ds), Ds)
    STORE["res"] = res

    Ta = res[("A", "3-record", Fr(0))]
    ladder = sorted({Fr(1) / b for b in Ta[3][1].values()})
    check("A2 [exact] TABLE A, separable by construction: M_rel is EXACTLY RANK ONE over Q on the "
          "dimer (%dx%d) and on 3-record groups (%dx%d), at h = 0 and h = 1 alike, "
          "sigma_2/sigma_1 <= %.6e, with the exact temperature ladder T(c) = 1/beta(c) = %s"
          % (res[("A", "dimer", Fr(0))][4], res[("A", "dimer", Fr(0))][5], Ta[4], Ta[5],
             max(res[("A", g, hv)][1] for g in ("dimer", "3-record") for hv in (Fr(0), Fr(1))),
             ", ".join(str(t) for t in ladder)),
          all(res[("A", g, hv)][0] == 1 for g in ("dimer", "3-record")
              for hv in (Fr(0), Fr(1)))
          and max(res[("A", g, hv)][1] for g in ("dimer", "3-record")
                  for hv in (Fr(0), Fr(1))) < 1e-15
          and ladder == [Fr(2, 5), Fr(1, 2), Fr(8, 15), Fr(2, 3), Fr(4, 5), Fr(1)])

    Tb = res[("B", "3-record", Fr(0))]
    check("A3 [exact] TABLE B, PR #7899's Metropolis rule: M_rel is EXACTLY RANK ONE on both groups "
          "at h = 0 and h = 1 (sigma_2/sigma_1 <= %.6e) with the SAME beta = g at all %d "
          "conditions, so one temperature T = 1/g -- a field in the PROPOSAL never enters the cost "
          "matrix"
          % (max(res[("B", g, hv)][1] for g in ("dimer", "3-record") for hv in (Fr(0), Fr(1))),
             Tb[4]),
          all(res[("B", g, hv)][0] == 1 for g in ("dimer", "3-record")
              for hv in (Fr(0), Fr(1))) and set(Tb[3][1].values()) == {Fr(1)})

    Tc0, Tc1 = res[("C", "3-record", Fr(0))], res[("C", "3-record", Fr(1))]
    check("A4 [exact] TABLE C, non-separable by construction: on 3-record groups M_rel has EXACT "
          "RANK %d over Q at h = 0, sigma_2/sigma_1 = %.6e, rank-one residual %.6e, and rank %d at "
          "h = 1 (%.6e): no beta(c) x E(D) exists, so no energy and no temperature"
          % (Tc0[0], Tc0[1], Tc0[2], Tc1[0], Tc1[1]),
          Tc0[0] == 2 and abs(Tc0[1] - 3.411710e-02) < 1e-8 and Tc1[0] == 4)

    Cp2, Cp1 = res[("Cp", "3-record", Fr(1, 2))], res[("Cp", "3-record", Fr(1))]
    check("A5 [exact] TABLE C', the same family keyed to the MOVER's own neighbourhood: M_rel is "
          "%dx%d of EXACT RANK %d, sigma_2/sigma_1 = %.6e at kappa = 1/2 and %.6e at kappa = 1, "
          "rank %d at h = 1 (%.6e) -- the departure grows with the declared kappa"
          % (Cp2[4], Cp2[5], Cp2[0], Cp2[1], Cp1[1], res[("Cp", "3-record", "h1")][0],
             res[("Cp", "3-record", "h1")][1]),
          Cp2[0] == 2 and Cp1[0] == 2
          and abs(Cp2[1] / 5.018675e-02 - 1.0) < 1e-6
          and abs(Cp1[1] / 1.304845e-01 - 1.0) < 1e-6)

    one = [k for k in res if res[k][3] is not None]
    good = all(res[k][3][0] == [Fr(max(0, D)) for D in res[k][6]] for k in one)
    check("A6 [exact] WHICH energy: in all %d rank-one cases the factorisation in the gauge "
          "E(D = +1) = 1 gives E(D) = max(0, D) -- E(-2) = E(-1) = E(0) = 0, E(+1) = 1, E(+2) = 2 "
          "-- a ONE-SIDED BARRIER, not the configuration energy: the odds say nothing about the "
          "downhill half of the move set" % len(one),
          good and len(one) == 9)

    condC, DsC, MaccC, MrelC = odds_matrix(dct, "C", Fr(1), Fr(0), Fr(1, 2))
    et = energy_and_temperatures(condC, DsC, MrelC)
    tl = sorted({Fr(1) / b for b in et[1].values()}) if et else []
    lp = -math.log(1.0 / 6.0)
    Mtot = np.array([[float(MaccC[i][j]) + lp for j in range(len(DsC))]
                     for i in range(len(condC))])
    svt = np.linalg.svd(Mtot, compute_uv=False)
    check("A7 [exact] TWO TRAPS. (i) A DIMER CANNOT RUN THIS TEST: D in {-1, 0, +1} makes "
          "D^2 = |D|, so table C is EXACTLY RANK ONE there (sigma_2/sigma_1 = %.6e) with a "
          "plausible T = %s; three records are needed. (ii) Leave ln p_prop in and even table C "
          "gives %.6e, so subtract the D = 0 column"
          % (sv_ratio(MrelC)[0], ", ".join(str(t) for t in tl), svt[1] / svt[0]),
          exact_rank(MrelC) == 1 and sv_ratio(MrelC)[0] == 0.0
          and tl == [Fr(2, 3), Fr(1)] and svt[1] / svt[0] > 1e-3)


# ============================================= group B -- T2, cycle criterion

def group_B():
    n2 = 2 * len(REL)
    out = {}
    for (tab, gv, hv, kv) in (("A", 1.0, 0.0, 0.5), ("B", 1.0, 0.0, 0.5),
                              ("B", 1.0, 1.0, 0.5), ("C", 1.0, 0.0, 0.5)):
        Ef = dimer_full_edges(tab, gv, hv, kv)
        nf, bf = cycles4(Ef)
        P, pi, resid = stationary(Ef, n2)
        gap = gibbs_gap(pi, gv, n2)
        nw, bw = winding(tab, gv, hv, kv)
        nt, bt = trimer_cycles(tab, gv, hv, kv)
        rel = (None, None)
        if tab != "A":
            rel = cycles4(dimer_rel_edges(tab, gv, hv, kv))
        out[(tab, hv)] = (nf, bf, resid, gap, nw, bw, nt, bt, rel)
    STORE["cyc"] = out
    A0, B0, B1, C0 = out[("A", 0.0)], out[("B", 0.0)], out[("B", 1.0)], out[("C", 0.0)]

    check("B1 [exact] the CYCLE CENSUS, complete where stated: %d distinct 4-cycles of the "
          "%d-state even-translation dimer chain, %d of the %d-state relative chain, %d winding "
          "cycles of length L = %d, and the declared subgraph of %d trimer 4-cycles on absolute "
          "configurations" % (A0[0], n2, B0[8][0], len(REL), A0[4], L, A0[6]),
          A0[0] == 56454 and B0[8][0] == 1524 and A0[4] == 504 and A0[6] == 1620)

    check("B2 [exact] TABLE A -- RANK ONE GIVES NO GIBBS STATE: cycle products fail by exactly "
          "nu = 1/4 on the dimer chain (%.15e) and the trimer chain (%.15e), winding clean (%.1e); "
          "the stationary law (|pi P - pi| = %.1e) misses e^{-g B} by %.6e"
          % (A0[1], A0[7], A0[5], A0[2], A0[3]),
          abs(A0[1] - 0.25) < 1e-12 and abs(A0[7] - 0.25) < 1e-12 and A0[5] < 1e-12
          and A0[2] < 1e-14 and abs(A0[3] - 1.199957e-01) < 1e-6)

    check("B3 [exact] TABLE B at h = 0 -- BOTH tests pass: every cycle product is 1 to machine zero "
          "on all four chains (dimer %.1e, relative %.1e, winding %.1e, trimer %.1e) and the law is "
          "exactly pi ~ e^{-g B} (%.1e, |pi P - pi| = %.1e). Here the odds ARE an energy"
          % (B0[1], B0[8][1], B0[5], B0[7], B0[3], B0[2]),
          max(B0[1], B0[8][1], B0[5], B0[7]) < 1e-12 and B0[3] < 1e-12)

    check("B4 [exact] TABLE B WITH A FIELD -- A GIBBS LAW IS NOT SUFFICIENT: at h = 1 the odds "
          "matrix is still rank one and the law still exactly Gibbs (%.1e), yet cycle products fail "
          "by exactly 4h = %.15f on the dimer chain and L h = %.15f on the winding cycles: a DRIVEN "
          "steady state" % (B1[3], B1[1], B1[5]),
          B1[3] < 1e-12 and abs(B1[1] - 4.0) < 1e-12 and abs(B1[5] - 8.0) < 1e-12)

    check("B5 [exact] TABLE C at h = 0 -- DETAILED BALANCE GIVES NO RANK ONE: at kappa = 1/2 every "
          "cycle product is 1 (dimer %.1e, relative %.1e, winding %.1e, trimer %.1e) and the law is "
          "exactly Gibbs (%.1e) while the odds matrix is rank 2: a symmetric kappa D^2 BARRIER "
          "cancels in every ratio" % (C0[1], C0[8][1], C0[5], C0[7], C0[3]),
          max(C0[1], C0[8][1], C0[5], C0[7]) < 1e-12 and C0[3] < 1e-12)

    cp = {}
    for (gv, kv) in ((1.0, 0.0), (1.0, 0.25), (1.0, 0.5), (1.0, 1.0), (2.0, 0.5)):
        cp[(gv, kv)] = trimer_cycles("Cp", gv, 0.0, kv)
    STORE["cp"] = cp
    check("B6 [exact] TABLE C' -- a crowding barrier keyed to the MOVER does break detailed "
          "balance: over the %d declared trimer 4-cycles at h = 0 the defect is exactly 4 kappa -- "
          "%.12f, %.12f, %.12f, %.12f at kappa = 0, 1/4, 1/2, 1 -- and %.12f at g = 2, "
          "coupling-independent"
          % (cp[(1.0, 0.5)][0], cp[(1.0, 0.0)][1], cp[(1.0, 0.25)][1], cp[(1.0, 0.5)][1],
             cp[(1.0, 1.0)][1], cp[(2.0, 0.5)][1]),
          cp[(1.0, 0.0)][1] < 1e-12
          and all(abs(cp[(1.0, kv)][1] - 4 * kv) < 1e-12 for kv in (0.25, 0.5, 1.0))
          and abs(cp[(2.0, 0.5)][1] - cp[(1.0, 0.5)][1]) < 1e-12)

    check("B7 [exact] THE LUMPING TRAP: at h = 1 the translation-reduced relative chain PASSES "
          "(%.1e) and so does the declared trimer subgraph (%.1e) while the unlumped chain fails by "
          "4h (%.6f) and the winding cycles by L h (%.6f): a 4-cycle test on a reduced chain is not "
          "a detailed-balance test" % (B1[8][1], B1[7], B1[1], B1[5]),
          B1[8][1] < 1e-12 and B1[7] < 1e-12 and abs(B1[1] - 4.0) < 1e-12)


# ============================================ group C -- T3, Arrhenius census

def group_C():
    slopesB = {}
    for gv in (1.0, 2.0, 4.0):
        ch, cen, nb = bent_channels("B", gv, 0.0, 0.5)
        slopesB[gv] = {D: v / D for D, v in activations(ch).items()}
    check("C1 [exact] TABLE B on the bent trimer: its %d proposals split %d null, %d at D = 0, %d "
          "at D = +1, %d at D = +2, and both break channels carry the COMMON SLOPE a(D)/D = g at "
          "g = 1, 2, 4 (%s): Arrhenius holds"
          % (nb + sum(len(v) for v in ch.values()), nb, len(ch[0]), len(ch[1]), len(ch[2]),
             ", ".join("%.12f" % slopesB[gv][1] for gv in (1.0, 2.0, 4.0))),
          nb == 4 and len(ch[0]) == 2 and len(ch[1]) == 8 and len(ch[2]) == 4
          and all(abs(slopesB[gv][1] - gv) < 1e-12 and abs(slopesB[gv][2] - gv) < 1e-12
                  for gv in (1.0, 2.0, 4.0)))

    gaps, aa, cenP = {}, {}, None
    for gv in (1.0, 2.0, 4.0):
        for kv in (0.5, 1.0):
            ch, cenP, _ = bent_channels("Cp", gv, 0.0, kv)
            a = activations(ch)
            aa[(gv, kv)] = a
            gaps[(gv, kv)] = a[2] / 2 - a[1]
    STORE["gaps"] = gaps
    check("C2 [exact] TABLE C' on the bent trimer: every D = +1 break is an END record (m_s = 1) so "
          "a(1) = g, every D = +2 break the CENTRE (m_s = 2) so a(2) = 2g + 4 kappa; the van 't "
          "Hoff gap a(2)/2 - a(1) = 2 kappa EXACTLY, %.12f at g = 1, 2, 4 for kappa = 1/2 and %.12f "
          "for kappa = 1" % (gaps[(1.0, 0.5)], gaps[(1.0, 1.0)]),
          all(abs(aa[(gv, kv)][1] - gv) < 1e-12
              and abs(aa[(gv, kv)][2] - (2 * gv + 4 * kv)) < 1e-12
              and abs(gaps[(gv, kv)] - 2 * kv) < 1e-12
              for gv in (1.0, 2.0, 4.0) for kv in (0.5, 1.0))
          and cenP[1] == {(1, 0)} and cenP[2] == {(2, 0)})

    def tau(gv, kv):
        return 18.0 / (8.0 * math.exp(-gv) + 4.0 * math.exp(-2 * gv - 4 * kv))
    lf = []
    for gv in (1.0, 2.0, 4.0):
        ch, _, _ = bent_channels("Cp", gv, 0.0, 0.5)
        rate = sum(sum(ch[D]) for D in ch if D > 0) / 18.0
        lf.append((1.0 / rate, tau(gv, 0.5), tau(gv, 0.0)))
    check("C3 [exact] the bent trimer's lifetime under C' is 18/(8 e^{-g} + 4 e^{-2g - 4 kappa}), "
          "matched by the enumerated proposals to %.1e: %.12f ticks at g = 1, kappa = 1/2 against "
          "PR #7899's %.12f, %.12f against %.12f, %.12f against %.12f at g = 2 and 4"
          % (max(abs(a - b) for a, b, _c in lf), lf[0][0], lf[0][2], lf[1][0], lf[1][2],
             lf[2][0], lf[2][2]),
          max(abs(a - b) for a, b, _c in lf) < 1e-11
          and abs(lf[0][0] - 5.967579958344) < 1e-9
          and abs(lf[0][2] - 5.165916817967) < 1e-9)

    slopesC, cenC, nbrk = {}, None, 0
    for kv in (0.0, 0.5, 1.0):
        ch, cenC, _ = bent_channels("C", 1.0, 0.0, kv)
        a = activations(ch)
        slopesC[kv] = (a[1], a[2] / 2)
        nbrk = sum(len(v) for D, v in ch.items() if D > 0)
    check("C4 [exact] THE NULL RESULT: table C, keyed to the TARGET's crowding, is Arrhenius on the "
          "bent trimer at EVERY kappa (a(1) = a(2)/2 = %.12f at kappa = 0, 1/2, 1) because all %d "
          "of its breaking proposals land on a site with no occupied neighbour (m_t = 0), so C's "
          "rank-2 signature lives in the re-binding moves alone" % (slopesC[0.5][0], nbrk),
          all(abs(slopesC[kv][0] - 1.0) < 1e-12 and abs(slopesC[kv][1] - 1.0) < 1e-12
              for kv in (0.0, 0.5, 1.0))
          and {m for st in cenC.values() for (_ms, m) in st} == {0})

    cp = STORE["cp"]
    check("C5 [exact] THE TWO DISCRIMINATORS, a factor of two apart: the Kolmogorov defect is "
          "4 kappa and the van 't Hoff gap 2 kappa, so defect = 2 x gap exactly -- %.12f against "
          "2 x %.12f at kappa = 1/2, %.12f against 2 x %.12f at kappa = 1; the rank-one departure "
          "%.6e is the third"
          % (cp[(1.0, 0.5)][1], gaps[(1.0, 0.5)], cp[(1.0, 1.0)][1], gaps[(1.0, 1.0)],
             STORE["res"][("Cp", "3-record", Fr(1, 2))][1]),
          all(abs(cp[(1.0, kv)][1] - 2 * gaps[(1.0, kv)]) < 1e-12 for kv in (0.5, 1.0)))


# ====================================== group D -- T4, PR #7899's closed forms

def group_D():
    n = len(REL)
    rows = []
    for gv in (1.0, 2.0, 4.0):
        for hv in (0.0, 1.0):
            E = dimer_rel_edges("B", gv, hv, 0.0)
            P, pi, resid = stationary(E, n)
            intact = float(sum(pi[r - 1] for r in REL if ADJ0[r]))
            eh = math.exp(hv)
            t = [1.0 / sum(v for j, v in E[r0 - 1].items() if not ADJ0[REL[j]])
                 for r0 in (pack((1, 0, 0)), pack((0, 1, 0)))]
            cf = (2 * math.exp(gv) * (5 + eh) / (9 + eh),
                  math.exp(gv) * (5 + eh) / (4 + eh))
            rows.append((t, cf, intact, 6.0 / (6.0 + 505.0 * math.exp(-gv)), resid))
    dtau = max(max(abs(t[0] / c[0] - 1.0), abs(t[1] / c[1] - 1.0))
               for t, c, _i, _c, _r in rows)
    dint = max(abs(i - c) for _t, _cf, i, c, _r in rows)
    check("D1 [exact] CONSISTENCY with PR #7899, dimer: table B reproduces 2 e^{g}(5 + e^{h})/"
          "(9 + e^{h}) aligned and e^{g}(5 + e^{h})/(4 + e^{h}) transverse over six (g, h) cells to "
          "%.2e relative -- both (6/5) e^{g} at h = 0 -- and 6/(6 + 505 e^{-g}) to %.2e AT EVERY h "
          "(|pi P - pi| <= %.1e)" % (dtau, dint, max(r[4] for r in rows)),
          dtau < 1e-14 and dint < 1e-14)

    ch, _cen, nb = bent_channels("B", 1.0, 0.0, 0.0)
    tri = []
    for gv in (1.0, 2.0, 4.0):
        chg, _c, _n = bent_channels("B", gv, 0.0, 0.0)
        rate = sum(sum(chg[D]) for D in chg if D > 0) / 18.0
        tri.append((1.0 / rate, 18.0 / (8 * math.exp(-gv) + 4 * math.exp(-2 * gv))))
    dtri = max(abs(a - b) for a, b in tri)
    check("D2 [exact] CONSISTENCY with PR #7899, bent trimer: with the 1/n record-choice factor and "
          "D = B(new) - B(old) = A(old) - A(new) both as declared, table B returns "
          "18/(8 e^{-g} + 4 e^{-2g}) to %.2e -- %.12f, %.12f, %.12f ticks at g = 1, 2, 4"
          % (dtri, tri[0][0], tri[1][0], tri[2][0]),
          dtri < 1e-11 and abs(tri[0][0] - 5.165916817967) < 1e-9)


def main():
    group_A()
    group_B()
    group_C()
    group_D()
    print("SUMMARY: the odds are an energy only when the odds matrix is rank one AND every cycle "
          "product is 1; neither gives the other, and a Gibbs resting law gives neither.")
    print("TOTAL: PASS=%d FAIL=%d" % (PASS, FAIL))
    return 1 if FAIL else 0


if __name__ == "__main__":
    sys.exit(main())
