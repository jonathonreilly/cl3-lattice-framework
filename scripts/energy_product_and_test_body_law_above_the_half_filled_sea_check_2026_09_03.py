#!/usr/bin/env python3
"""Two real particle-hole pairs and a supplied finite quadratic response.
A: actual joint Slater projector; its row density need not add.
B: classical sum s=e1+e2 in response boxes, distinct from actual joint density.
C: finite extended/point vector comparisons, x components, incomplete old gauge.
D: changing filter energy AND shape, versus a separately fixed count source.
E: declared coordinate units, no physical coupling or coarse/fine theorem.
H: exact action/extended-convolution sign identity and actual nonzero point error.
R: actual same-box joint-density counterexample, full edge-gauge covariance,
and indefinite cross pairing of a PSD quadratic response. The law, preparation,
readout, response and U=A* physical identification remain supplied."""

from __future__ import annotations

import itertools
import sys

import numpy as np

AUDIT_TIMEOUT_SEC = 300

# Mutable proof/interpretation inputs are part of this runner's source identity.
AUDIT_INPUT_PATHS = ['docs/ENERGY_PRODUCT_AND_TEST_BODY_LAW_ABOVE_THE_HALF_FILLED_SEA_CONDITIONAL_BOUNDED_THEOREM_NOTE_2026-09-03.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/GRAVITY_WEAK_FIELD_SOURCE_RESPONSE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-11.md']
SOURCE_INPUT_SHA256 = {'docs/ENERGY_PRODUCT_AND_TEST_BODY_LAW_ABOVE_THE_HALF_FILLED_SEA_CONDITIONAL_BOUNDED_THEOREM_NOTE_2026-09-03.md': '0ea261e4f84fbb86b0ef4537ade32d32e485f61a9d960691ce63d08daefbdeea', 'docs/MINIMAL_AXIOMS_2026-06-29.md': '93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753', 'docs/GRAVITY_WEAK_FIELD_SOURCE_RESPONSE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-11.md': '71023af5e313037d74eb3efb56b0515c913e66947981950e1871b3acc398fdbf'}

def _source_input_guard():
    from pathlib import Path
    import hashlib
    root = Path(__file__).resolve().parents[1]
    if set(AUDIT_INPUT_PATHS) != set(SOURCE_INPUT_SHA256):
        raise RuntimeError("SOURCE_INPUTS: declaration/pin mismatch")
    for relative in AUDIT_INPUT_PATHS:
        p = root / relative
        if not p.is_file():
            raise RuntimeError("SOURCE_INPUTS: missing " + relative)
        if hashlib.sha256(p.read_bytes()).hexdigest() != SOURCE_INPUT_SHA256[relative]:
            raise RuntimeError("SOURCE_INPUTS: changed " + relative)
    print("SOURCE_INPUTS: " + " ".join(p+":"+SOURCE_INPUT_SHA256[p] for p in AUDIT_INPUT_PATHS))

_source_input_guard()

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


PI = np.pi
EX = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]

# Historical reference rows and explicitly retained finite numerical criteria.
# No parent status or discretization error estimate is supplied by a match.
NOTE_E_SEA_8 = -611.811768          # matter-above-the-sea note, T1
NOTE_GAP_8 = 2.651309               # matter-above-the-sea note, T1
NOTE_POINT_CONTROL = {32: 0.3307, 64: 0.3275}   # both parents' own row
NOTE_T4_COEFF = {4: 1.0194, 6: 1.0064, 8: 1.0009, 10: 0.9963}   # source note T4


# ================================================ the coarse lattice, the sea

def eta_ks(v, a):
    """Kawamoto-Smit link sign of the coarse bond (v, v + e_a), axes 0/1/2."""
    if a == 0:
        return 1
    if a == 1:
        return -1 if (v[0] & 1) else 1
    return -1 if ((v[0] + v[1]) & 1) else 1


def build(L, twist):
    """Coarse torus L^3 with the KS staggered sign field; twist[a] = 1 flips
    the bonds crossing the cut v_a = L-1 -> 0."""
    sites = list(itertools.product(range(L), repeat=3))
    idx = {v: i for i, v in enumerate(sites)}
    M = np.zeros((L ** 3, L ** 3))
    for v in sites:
        for a in range(3):
            w = tuple((v[i] + EX[a][i]) % L for i in range(3))
            s = eta_ks(v, a)
            if twist[a] and v[a] == L - 1:
                s = -s
            M[idx[w], idx[v]] += s
            M[idx[v], idx[w]] += s
    return M, sites, idx


L = 8
TWIST = (1, 1, 1)
V = L ** 3
NOCC = V // 2
M, SITES, IDX = build(L, TWIST)
WV, U = np.linalg.eigh(M)
P = U[:, :NOCC] @ U[:, :NOCC].T
E_SEA = float(np.sum(WV[:NOCC]))
GAP = float(WV[NOCC] - WV[NOCC - 1])
HALF_RES = float(np.max(np.abs(np.diag(P) - 0.5)))


# ==================================================== the response, unchanged

def ghat(Lb):
    """Fourier symbol of G0 P0: 1/lambda(k) off the constant mode, 0 on it."""
    k = 2 * PI * np.fft.fftfreq(Lb)
    lam = 6 - 2 * (np.cos(k)[:, None, None] + np.cos(k)[None, :, None]
                   + np.cos(k)[None, None, :])
    G = np.zeros_like(lam)
    nz = lam > 1e-12
    G[nz] = 1.0 / lam[nz]
    G[0, 0, 0] = 0.0
    return G


def green(Lb):
    return np.real(np.fft.ifftn(ghat(Lb)))


def solve(rho, Gh):
    return np.real(np.fft.ifftn(np.fft.fftn(rho) * Gh))


GH = {Lb: ghat(Lb) for Lb in (32, 64)}
GR = {Lb: green(Lb) for Lb in (32, 64)}


# ===================================================== pairs above that sea

def gauss(v0, s=1.0):
    """Normalised-shape Gaussian seed on the coarse torus, minimal image."""
    g = np.zeros(V)
    for i, v in enumerate(SITES):
        d2 = 0
        for a in range(3):
            dd = (v[a] - v0[a]) % L
            dd = min(dd, L - dd)
            d2 += dd * dd
        g[i] = np.exp(-d2 / (2 * s * s))
    return g


# The KS field is not translation invariant, only gauge equivalent: under
# v -> v + e_a it is carried by a diagonal +-1 sign field on the sites.
GAUGE = {0: lambda v: (-1) ** (v[1] + v[2]),
         1: lambda v: (-1) ** (v[2]),
         2: lambda v: 1}


def gauge_vec(sh):
    f = np.ones(V)
    for a in range(3):
        if abs(sh[a]) % 2:
            f = f * np.array([GAUGE[a](v) for v in SITES], float)
    return f


def wp(v0, which, E0=None, wf=1.0, gsign=None):
    """Gaussian seed projected into the empty ('p') or occupied ('h') span,
    optionally band-filtered toward +-E0 with width wf, optionally carried by
    the gauge sign field so a rebuilt packet is the exact gauge image."""
    g = gauss(v0)
    if gsign is not None:
        g = g * gsign
    if which == 'p':
        sub, ev = U[:, NOCC:], WV[NOCC:]
    else:
        sub, ev = U[:, :NOCC], WV[:NOCC]
    c = sub.T @ g
    if E0 is not None:
        c = c * np.exp(-(ev - (E0 if which == 'p' else -E0)) ** 2 / (2 * wf * wf))
    psi = sub @ c
    return psi / np.linalg.norm(psi)


def onb(cols):
    A = np.column_stack(cols)
    Q, S, _ = np.linalg.svd(A, full_matrices=False)
    return Q[:, S > 1e-10]


def eps_of(Pp):
    """The local excitation energy density and its total."""
    D = Pp - P
    return np.sum(M * D, axis=1), float(np.trace(M @ D))


def one_pair(vp, vh, **kw):
    pk = wp(vp, 'p', **kw)
    hk = wp(vh, 'h', **kw)
    Pp = P - np.outer(hk, hk) + np.outer(pk, pk)
    e, E = eps_of(Pp)
    return pk, hk, e, E, np.diag(Pp) - 0.5


def two_pair(pks, hks):
    """P'' = P - Q_h + Q_p with Q_h, Q_p the projectors onto the two-
    dimensional hole and particle spans."""
    Qp = onb(pks)
    Qh = onb(hks)
    Pp = P - Qh @ Qh.T + Qp @ Qp.T
    e, E = eps_of(Pp)
    return e, E, float(np.max(np.abs(Pp @ Pp - Pp))), int(round(np.trace(Pp))), np.diag(Pp) - 0.5


BASE = (2, 2, 3)   # the twist cut sits between x = 7 and x = 0; see the note


def make_pair(dp, off, gauge_from=None, **kw):
    """A pair of internal separation dp along z, offset by `off` from BASE."""
    vp = tuple((BASE[a] + off[a]) % L for a in range(3))
    vh = tuple((vp[a] + (0, 0, dp)[a]) % L for a in range(3))
    mid = tuple(int(round(BASE[a] + off[a] + (0, 0, dp)[a] / 2.0)) % L for a in range(3))
    if gauge_from is not None:
        kw = dict(kw)
        kw['gsign'] = gauge_vec(tuple(off[a] - gauge_from[a] for a in range(3)))
    pk, hk, e, E, r = one_pair(vp, vh, **kw)
    return pk, hk, e, E, r, mid


def unwrapped(vec, about):
    out = []
    for i, v in enumerate(SITES):
        q = []
        for a in range(3):
            t = (v[a] - about[a]) % L
            if t > L // 2:
                t -= L
            q.append(t)
        out.append((tuple(q), vec[i]))
    return out


def moments(pr):
    q = sum(x for _, x in pr)
    p = np.array([sum(x * o[a] for o, x in pr) for a in range(3)])
    Q = np.zeros((3, 3))
    for o, x in pr:
        r2 = sum(o[a] ** 2 for a in range(3))
        for a in range(3):
            for b in range(3):
                Q[a, b] += x * (3 * o[a] * o[b] - (r2 if a == b else 0))
    return q, p, Q


def prep(vec, about):
    """Unwrap about the pair midpoint, then recentre on the ROUNDED charge
    centroid; the integer shift is the same for two translated copies, so
    their centroid separation is exactly Dvec."""
    pr = unwrapped(vec, about)
    q, p, _ = moments(pr)
    c = np.round(p / q).astype(int)
    pr = [(tuple(o[a] - c[a] for a in range(3)), x) for o, x in pr]
    q, p, Q = moments(pr)
    return pr, q, p, Q


def place(pr, Lb, base):
    A = np.zeros((Lb,) * 3)
    for o, x in pr:
        A[(o[0] + base[0]) % Lb, (o[1] + base[1]) % Lb, (o[2] + base[2]) % Lb] += x
    return A


def multipole_rel(q1, p1, Q1, q2, p2, Q2, Dvec):
    """Relative correction to q1 q2 G(D) from the continuum expansion of
    1/(4 pi |R - (u - v)|) to dipole and traceless-quadrupole order."""
    D = np.linalg.norm(Dvec)
    n = np.array(Dvec, float) / D
    t1 = float(n @ (q2 * p1 - q1 * p2)) / (q1 * q2 * D)
    t2 = (q2 * float(n @ Q1 @ n) + q1 * float(n @ Q2 @ n)
          - 2 * (3 * float(n @ p1) * float(n @ p2) - float(p1 @ p2))) / (2 * q1 * q2 * D * D)
    return t1 + t2


DVECS = [(2, 0, 0), (3, 0, 0), (4, 0, 0), (3, 3, 0)]


# ================================================== A -- the two-pair state

ST = {}
A_ROWS = []
for dp in (1, 2):
    for Dvec in DVECS:
        p1, h1, e1, E1, r1, m1 = make_pair(dp, (0, 0, 0))
        p2, h2, e2, E2, r2, m2 = make_pair(dp, Dvec)
        e12, E12, idem, rk, r12 = two_pair([p1, p2], [h1, h2])
        ST[(dp, Dvec)] = dict(e1=e1, e2=e2, E1=E1, E2=E2, m1=m1, m2=m2,
                              r1=r1, r2=r2, r12=r12, e_joint=e12)
        A_ROWS.append(dict(dp=dp, D=Dvec, op=abs(float(p1 @ p2)), oh=abs(float(h1 @ h2)),
                           rel=(E12 - E1 - E2) / (E1 + E2),
                           dev=float(np.max(np.abs(e12 - e1 - e2))),
                           idem=idem, tr=rk))

# validation against the parent note's own pair table
VAL = []
for d in (1, 2, 3, 4):
    _, _, ev, Ev, _ = one_pair((0, 0, 0), (d % L, 0, 0))
    VAL.append((Ev, abs(float(ev.sum()) - Ev)))
po, ho = U[:, NOCC], U[:, NOCC - 1]
E_ORB = eps_of(P - np.outer(ho, ho) + np.outer(po, po))[1]

# the one-coarse-site translation residual of eps_v: naive vs gauge-corrected
_, _, e0, E0_, _, _ = make_pair(1, (0, 0, 0))
perm_x = np.array([IDX[tuple((v[b] + (1, 0, 0)[b]) % L for b in range(3))] for v in SITES])
_, _, e_nv, _, _, _ = make_pair(1, (1, 0, 0))
_, _, e_gv, _, _, _ = make_pair(1, (1, 0, 0), gauge_from=(0, 0, 0))
TR_NAIVE = float(np.max(np.abs(e_nv[perm_x] - e0)))
TR_GAUGE = float(np.max(np.abs(e_gv[perm_x] - e0)))

d1 = [r for r in A_ROWS if r['dp'] == 1]
d2 = [r for r in A_ROWS if r['dp'] == 2]
MAXIDEM = max(r['idem'] for r in A_ROWS)
MAXCNT = max(abs(float(ST[k]['r1'].sum())) for k in ST)
MAXCNT = max(MAXCNT, max(abs(float(ST[k]['r12'].sum())) for k in ST))

check("A1 [numerical, 1e-6] the conditioning vacuum: the half-filled staggered sea on 8^3 at twist (1,1,1), E_sea = %.6f (the matter note's, %.1e), gap %.6f = 2 sqrt(6 - 3 sqrt2) (%.1e), <n_v> = 1/2 at all 512 (%.1e)"
      % (E_SEA, abs(E_SEA - NOTE_E_SEA_8), GAP, abs(GAP - 2 * np.sqrt(6 - 3 * np.sqrt(2))), HALF_RES),
      abs(E_SEA - NOTE_E_SEA_8) < 1e-6 and abs(GAP - 2 * np.sqrt(6 - 3 * np.sqrt(2))) < 1e-12
      and HALF_RES < 1e-15 and abs(GAP - NOTE_GAP_8) < 1e-6)

check("A2 [numerical, 1e-13] single pairs: band-edge orbital E_exc = %.6f, localised wavepackets %.4f to %.4f over d = 1..4, sum_v eps_v = E_exc to %.0e -- the matter note's 2.651309, 2.6513-4.5163"
      % (E_ORB, min(r[0] for r in VAL), max(r[0] for r in VAL), max(r[1] for r in VAL)),
      abs(E_ORB - NOTE_GAP_8) < 1e-6 and max(r[1] for r in VAL) < 1e-13
      and abs(max(r[0] for r in VAL) - 4.5163) < 1e-3)

check("A3 [numerical, 1e-14] TWO pairs at D = (2,0,0)/(3,0,0)/(4,0,0)/(3,3,0): P'' = P - Q_h + Q_p is a projector to %.0e over eight states, trace exactly %d = V/2"
      % (MAXIDEM, A_ROWS[0]['tr']),
      MAXIDEM < 1e-14 and all(r['tr'] == 256 for r in A_ROWS))

check('A4 [finite samples] at four selected D, orbital overlaps are <p1|p2> = %.2f/%.2f/%.3f/%.3f, <h1|h2> = %.2f/%.3f/%.4f/%.4f'
      % tuple([r['op'] for r in d1] + [r['oh'] for r in d1]),
      d1[0]['op'] > 0.35 and d1[2]['op'] < 0.05 and d1[0]['oh'] > 0.37 and d1[2]['oh'] < 2e-3
      and d1[0]['op'] > d1[1]['op'] > d1[2]['op'])

check('A5 [finite samples] joint-energy relative nonadditivity = %+.1e/%+.1e/%+.1e/%+.1e at d_pair1, %+.1e/%+.1e at d_pair2; actual joint row-density defects %.1e/%.1e/%.1e'
      % (d1[0]['rel'], d1[1]['rel'], d1[2]['rel'], d1[3]['rel'], d2[1]['rel'], d2[2]['rel'],
         d1[0]['dev'], d1[1]['dev'], d1[2]['dev']),
      abs(d1[0]['rel']) > 8 * abs(d1[1]['rel']) and abs(d1[1]['rel']) > 8 * abs(d1[2]['rel'])
      and d1[0]['dev'] > 8 * d1[1]['dev'] and d1[1]['dev'] > 8 * d1[2]['dev'])

check('A6 [numerical, 1e-13] selected fixed-number preparations have sum_v (<n_v>-1/2)=0 to %.0e; this does not exclude charged even states'
      % MAXCNT, MAXCNT < 1e-13)


# ============================================== B -- the energy product

BROWS = {}
SYMMAX = 0.0
for Lb in (32, 64):
    Gh = GH[Lb]
    Gr = GR[Lb]
    b1 = (Lb // 2,) * 3
    for dp in (1, 2):
        for Dvec in DVECS:
            S = ST[(dp, Dvec)]
            pr1, q1, p1_, Q1 = prep(S['e1'], S['m1'])
            pr2, q2, p2_, Q2 = prep(S['e2'], S['m2'])
            b2 = tuple(b1[a] + Dvec[a] for a in range(3))
            A1 = place(pr1, Lb, b1)
            A2 = place(pr2, Lb, b2)
            F1 = np.fft.fftn(A1)
            F2 = np.fft.fftn(A2)
            Ei = float(np.real(np.sum(np.conj(F1) * Gh * F2)) / Lb ** 3)
            F12 = np.fft.fftn(A1 + A2)
            tot = float(np.real(np.sum(np.conj(F12) * Gh * F12)) / Lb ** 3)
            s1 = float(np.real(np.sum(np.conj(F1) * Gh * F1)) / Lb ** 3)
            s2 = float(np.real(np.sum(np.conj(F2) * Gh * F2)) / Lb ** 3)
            SYMMAX = max(SYMMAX, abs(tot - s1 - s2 - 2 * Ei))
            GD = float(Gr[Dvec[0] % Lb, Dvec[1] % Lb, Dvec[2] % Lb])
            pred = q1 * q2 * GD
            BROWS[(Lb, dp, Dvec)] = (Ei, pred, Ei / pred,
                                     1 + multipole_rel(q1, p1_, Q1, q2, p2_, Q2, Dvec))
            del A1, A2, F1, F2, F12

# finite response comparison against historical point-control rows
PC = {}
for Lb in (32, 64):
    r = Lb // 4
    PC[Lb] = 4 * PI * r * float(GR[Lb][r, 0, 0])

r64 = [BROWS[(64, 1, D)][2] for D in DVECS]
m64 = [BROWS[(64, 1, D)][3] for D in DVECS]
r64b = [BROWS[(64, 2, D)][2] for D in DVECS]
r32 = [BROWS[(32, 1, D)][2] for D in DVECS]
r32b = [BROWS[(32, 2, D)][2] for D in DVECS]

# large separation: two RIGID copies of one profile in the Lb = 64 box
Lb = 64
Gh = GH[Lb]
Gr = GR[Lb]
b1 = (Lb // 2,) * 3
S = ST[(1, (4, 0, 0))]
pr1, q1, p1_, Q1 = prep(S['e1'], S['m1'])
F1 = np.fft.fftn(place(pr1, Lb, b1))
kk = 2 * PI * np.fft.fftfreq(Lb)
KX, KY, KZ = np.meshgrid(kk, kk, kk, indexing='ij')
BIG = {}
for D in (2, 3, 4, 6, 8, 10, 12, 16):
    Ei = float(np.real(np.sum(np.conj(F1) * Gh * F1 * np.exp(-1j * KX * D))) / Lb ** 3)
    GD = float(Gr[D, 0, 0])
    BIG[D] = (Ei, q1 * q1 * GD, Ei / (q1 * q1 * GD),
              1 + multipole_rel(q1, p1_, Q1, q1, p1_, Q1, (D, 0, 0)))

check('B1 [numerical, 1e-4] reconstructed finite G0 multiplier off constant mode: point control 4 pi r G at r = Lb/4 = %.4f and %.4f at Lb32,64 against historical rows (%.0e)'
      % (PC[32], PC[64], max(abs(PC[Lb] - NOTE_POINT_CONTROL[Lb]) for Lb in (32, 64))),
      max(abs(PC[Lb] - NOTE_POINT_CONTROL[Lb]) for Lb in (32, 64)) < 1e-4)

check('B2 [numerical, 1e-9] supplied B=<e1,G P0 e2> divided by E1 E2 G(D), Lb64,d_pair1: %.4f/%.4f/%.4f/%.4f at four selected D; finite source-shape comparison'
      % tuple(r64), min(r64[1:]) > 0.90 and max(r64) < 1.0)

check('B3 [numerical, 1e-9] other declared finite fixtures: d_pair2 on Lb64 gives %.4f/%.4f at D3,4; Lb32 gives %.4f/%.4f at D4'
      % (r64b[1], r64b[2], r32[2], r32b[2]),
      abs(r64b[1] - 0.8757) < 5e-3 and abs(r64b[2] - 0.9188) < 5e-3
      and abs(r32[2] - 0.9575) < 5e-3 and abs(r32b[2] - 0.8997) < 5e-3)

check('B4 [numerical, 1e-14] classical sum s=e1+e2 ONLY: Q(s)-Q(e1)-Q(e2)=2B to %.0e over sixteen rows; actual joint Slater density is a different source'
      % SYMMAX, SYMMAX < 1e-14)

check('B5 [finite multipole diagnostic] point plus source dipole/quadrupole: %.4f/%.4f/%.4f/%.4f, within0.03 of the computed ratios at three stated points; no asymptotic error certificate'
      % tuple(m64),
      max(abs(m64[i] - r64[i]) for i in (1, 2, 3)) < 0.03 and abs(m64[1] - 0.9146) < 5e-3)

check('B6 [finite samples] two rigid copies, not a joint Slater state, give %.4f/%.4f/%.4f/%.4f at D3/4/8/16 on Lb64'
      % (BIG[3][2], BIG[4][2], BIG[8][2], BIG[16][2]),
      BIG[3][2] < BIG[4][2] < BIG[8][2] < BIG[16][2] and BIG[16][2] > 0.998)


# ============================================== C -- the test-body law

CR = {}
for dp in (1, 2):
    for Dvec in ((3, 0, 0), (4, 0, 0)):
        S = ST[(dp, Dvec)]
        pra, qa, _, _ = prep(S['e1'], S['m1'])
        prb, qb, _, _ = prep(S['e2'], S['m2'])
        b2 = tuple(b1[a] + Dvec[a] for a in range(3))
        A1 = place(pra, Lb, b1)
        Fa = np.fft.fftn(A1)
        phi1 = solve(A1, Gh)
        Fb = np.fft.fftn(place(prb, Lb, b2))
        Fpred = np.zeros(3)
        Fnum = np.zeros(3)
        for a in range(3):
            pp = list(b2)
            pp[a] = (pp[a] + 1) % Lb
            mm = list(b2)
            mm[a] = (mm[a] - 1) % Lb
            Fpred[a] = -qb * (phi1[tuple(pp)] - phi1[tuple(mm)]) / 2.0
            vals = []
            for sg in (+1, -1):
                s = [0, 0, 0]
                s[a] = sg
                ph = np.exp(-1j * (KX * s[0] + KY * s[1] + KZ * s[2]))
                vals.append(float(np.real(np.sum(np.conj(Fa) * Gh * Fb * ph)) / Lb ** 3))
            Fnum[a] = -(vals[0] - vals[1]) / 2.0
        cos = float(Fnum @ Fpred) / (np.linalg.norm(Fnum) * np.linalg.norm(Fpred))
        CR[(dp, Dvec)] = (Fnum[0] / Fpred[0], float(np.degrees(np.arccos(np.clip(cos, -1, 1)))))
        del A1, Fa, Fb, phi1

# the force on rigid copies, out to large D
FS = {}
phiR = solve(place(pr1, Lb, b1), Gh)
for D in (3, 4, 6, 8, 10, 16):
    Fnum = np.zeros(3)
    Fpred = np.zeros(3)
    pos = (b1[0] + D, b1[1], b1[2])
    for a in range(3):
        vals = []
        for sg in (+1, -1):
            s = [D, 0, 0]
            s[a] += sg
            ph = np.exp(-1j * (KX * s[0] + KY * s[1] + KZ * s[2]))
            vals.append(float(np.real(np.sum(np.conj(F1) * Gh * F1 * ph)) / Lb ** 3))
        Fnum[a] = -(vals[0] - vals[1]) / 2.0
        pp = list(pos)
        pp[a] = (pp[a] + 1) % Lb
        mm = list(pos)
        mm[a] = (mm[a] - 1) % Lb
        Fpred[a] = -q1 * (phiR[tuple(pp)] - phiR[tuple(mm)]) / 2.0
    cos = float(Fnum @ Fpred) / (np.linalg.norm(Fnum) * np.linalg.norm(Fpred))
    FS[D] = (Fnum[0] / Fpred[0], float(np.degrees(np.arccos(np.clip(cos, -1, 1)))),
             4 * PI * D * D * Fnum[0] / (q1 * q1), Fnum.copy(), Fpred.copy())

check('C1 [numerical, 1e-9] extended F_num=-D B versus point F_pred=-E2 D phi1: x ratios %.4f/%.4f at D3,4 d_pair1, %.4f/%.4f d_pair2; sign convention separately in H'
      % (CR[(1, (3, 0, 0))][0], CR[(1, (4, 0, 0))][0], CR[(2, (3, 0, 0))][0], CR[(2, (4, 0, 0))][0]),
      all(0.80 < CR[k][0] < 1.0 for k in CR))

check('C2 [finite samples] nonzero extended/point vector angle errors %.1f/%.1f/%.1f/%.1f degrees; no equality inferred'
      % (CR[(1, (3, 0, 0))][1], CR[(1, (4, 0, 0))][1], CR[(2, (3, 0, 0))][1], CR[(2, (4, 0, 0))][1]),
      max(CR[k][1] for k in CR) < 10.0)

check('C3 [incomplete-map diagnostic] naive source rebuild residual %.2e, KS-bulk-only %.2e; latter omits twist seam and is not a covariance no-go'
      % (TR_NAIVE, TR_GAUGE), TR_NAIVE > 0.3 and TR_GAUGE < 5e-3 and TR_NAIVE > 100 * TR_GAUGE)

check('C4 [finite rigid-copy samples] x ratios %.4f/%.4f/%.4f/%.4f/%.4f/%.4f and endpoint angles %.1f -> %.1f degrees'
      % (FS[3][0], FS[4][0], FS[6][0], FS[8][0], FS[10][0], FS[16][0], FS[3][1], FS[16][1]),
      FS[3][0] < FS[4][0] < FS[6][0] and FS[16][0] > 0.999 and FS[16][1] < FS[3][1])

check('C5 [finite x-component diagnostic] 4 pi D^2 F_num,x/(E1 E2) = %.4f/%.4f/%.4f/%.4f/%.4f/%.4f; not vector norm or a certified inverse-square law; historical point rows1.0194/1.0064/1.0009/0.9963 remain comparison only'
      % tuple(FS[D][2] for D in (3, 4, 6, 8, 10, 16)),
      all(abs(FS[d][2] - NOTE_T4_COEFF[d]) < 0.03 for d in (4, 6, 8, 10)))


# ============================================== D -- count versus energy

KNOB = []
for E0v in (1.35, 1.80, 2.40, 2.90, 3.15):
    kw = dict(E0=E0v, wf=0.6)
    _, _, ea, Ea, _, ma = make_pair(1, (0, 0, 0), **kw)
    pra, qa, _, _ = prep(ea, ma)
    Dvec = (4, 0, 0)
    _, _, eb, Eb, _, mb = make_pair(1, Dvec, **kw)
    prb, qb, _, _ = prep(eb, mb)
    b2 = tuple(b1[a] + Dvec[a] for a in range(3))
    Fa = np.fft.fftn(place(pra, Lb, b1))
    Fb = np.fft.fftn(place(prb, Lb, b2))
    Ei = float(np.real(np.sum(np.conj(Fa) * Gh * Fb)) / Lb ** 3)
    C1 = np.zeros((Lb,) * 3)
    C1[b1] = 1.0
    C1[b1[0], b1[1], b1[2] + 1] = 1.0
    C2 = np.zeros((Lb,) * 3)
    C2[b2] = 1.0
    C2[b2[0], b2[1], b2[2] + 1] = 1.0
    Ec = float(np.real(np.sum(np.conj(np.fft.fftn(C1)) * Gh * np.fft.fftn(C2))) / Lb ** 3)
    KNOB.append((qa, Ei, qa * qb, Ec))
    del Fa, Fb, C1, C2

E_RISE = KNOB[-1][1] / KNOB[0][1]
P_RISE = KNOB[-1][2] / KNOB[0][2]
C_SPREAD = max(k[3] for k in KNOB) - min(k[3] for k in KNOB)

EPROD = ST[(1, (4, 0, 0))]['E1'] * ST[(1, (4, 0, 0))]['E2']

check("D1 [numerical] COUNT VERSUS ENERGY. An energy knob -- a Gaussian seed band-filtered toward +-E0, width 0.6 -- moves E_exc through %.4f/%.4f/%.4f/%.4f/%.4f at D = 4: E_int rises to %.3f, E_1 E_2 to %.3f, ratio of ratios %.3f"
      % (KNOB[0][0], KNOB[1][0], KNOB[2][0], KNOB[3][0], KNOB[4][0], E_RISE, P_RISE, E_RISE / P_RISE),
      E_RISE > 2.4 and P_RISE > 2.4 and abs(E_RISE / P_RISE - 1.0) < 0.06)

check('D2 [numerical, 1e-12] separately fixed two-delta count source I=2 each: B_count=%.7f in every filter row, spread %.0e; excitation energy factor is about1.56, product factor2.425, not quadrupling'
      % (KNOB[0][3], C_SPREAD), C_SPREAD < 1e-12)

check('D3 [numerical, 1e-13] selected fixed-N sources have zero total number deviation to %.0e, while E1 E2=%.2f; different source/readout choices, not a consequence of vacuum alone'
      % (MAXCNT, EPROD), MAXCNT < 1e-13)

check('D4 [stated] historical empty-vacuum count-source claim is unaccepted context; this runner compares an explicitly chosen energy source with a separately fixed count source', True)


# ============================================== E -- units

check('E1 [stated] t=1 and coarse coordinates are supplied; no physical G_Newton, mass, coupling or coarse/fine factor-two theorem is derived here', True)

# ================================ H -- the on-shell action, and the direction

def hlap(f):
    """H = -Delta_lat on the response box, the seven-point stencil."""
    out = 6.0 * f
    for a in range(3):
        out = out - np.roll(f, 1, axis=a) - np.roll(f, -1, axis=a)
    return out


def action(rho):
    """(A[phi; rho] at its stationary point phi = G0 P0 rho, -(1/2)<P0 rho, phi>)."""
    phi = solve(rho, Gh)
    p0 = rho - rho.mean()
    return (0.5 * float(np.sum(phi * hlap(phi))) - float(np.sum(p0 * phi)),
            -0.5 * float(np.sum(p0 * phi)))


ONSH = 0.0
XTRM = 0.0
ACR = {}
for Dvec in DVECS:
    S = ST[(1, Dvec)]
    pra, _, _, _ = prep(S['e1'], S['m1'])
    prb, _, _, _ = prep(S['e2'], S['m2'])
    b2 = tuple(b1[a] + Dvec[a] for a in range(3))
    A1 = place(pra, Lb, b1)
    A2 = place(prb, Lb, b2)
    a12, h12 = action(A1 + A2)
    a1, _ = action(A1)
    a2, _ = action(A2)
    ONSH = max(ONSH, abs(a12 - h12) / abs(h12))
    XTRM = max(XTRM, abs((a12 - a1 - a2) + BROWS[(64, 1, Dvec)][0]))
    ACR[Dvec] = a12 - a1 - a2
    del A1, A2

check("H1 [numerical, 1e-14] THE ON-SHELL ACTION. A[phi; rho] = (1/2)<phi, H phi> - <P0 rho, phi> at phi = G0 P0 rho is A* = -(1/2)<P0 rho, G0 P0 rho> to %.0e; its cross term %.6f at D = 4 is exactly -E_int to %.0e"
      % (ONSH, ACR[(4, 0, 0)], XTRM), ONSH < 1e-14 and XTRM < 1e-14)


def ustar(shift):
    """A* for two rigid copies of eps_1 at the given offset in the box."""
    ph = np.exp(-1j * (KX * shift[0] + KY * shift[1] + KZ * shift[2]))
    Ft = F1 + F1 * ph
    return -0.5 * float(np.real(np.sum(np.conj(Ft) * Gh * Ft))) / Lb ** 3


FDEV = 0.0
MDEV = 0.0
NDEV = 0.0
EXTDEV = 0.0
FUX = {}
PhiN = -phiR
for D in (3, 4, 6, 8, 10, 16):
    FU = np.zeros(3)
    FN = np.zeros(3)
    pos = (b1[0] + D, b1[1], b1[2])
    for a in range(3):
        v = []
        for sg in (+1, -1):
            sh = [D, 0, 0]
            sh[a] += sg
            v.append(ustar(sh))
        FU[a] = -(v[0] - v[1]) / 2.0
        pp = list(pos)
        pp[a] = (pp[a] + 1) % Lb
        mm = list(pos)
        mm[a] = (mm[a] - 1) % Lb
        FN[a] = -q1 * (PhiN[tuple(pp)] - PhiN[tuple(mm)]) / 2.0
    FDEV = max(FDEV, float(np.max(np.abs(FU + FS[D][3]))))
    MDEV = max(MDEV, abs(float(np.linalg.norm(FU) - np.linalg.norm(FS[D][3]))))
    NDEV = max(NDEV, float(np.max(np.abs(FU - FN))))
    phase = np.exp(-1j * KX * D)
    rho2 = np.real(np.fft.ifftn(F1 * phase))
    FEXT = np.array([np.sum(rho2 * (np.roll(phiR,-1,axis=a)-np.roll(phiR,1,axis=a))/2) for a in range(3)])
    EXTDEV = max(EXTDEV, float(np.max(np.abs(FU-FEXT))))
    FUX[D] = float(FU[0])

check("H2 [numerical, 1e-14] SO THE PULL IS ATTRACTIVE. F_U = -grad_{x2} A*, same central differences, is -F_num to %.0e at unchanged magnitude (%.0e); F_U,x = %+.3e to %+.3e is NEGATIVE at every D = 3/4/6/8/10/16 -- pair 2 pulled TOWARD pair 1"
      % (FDEV, MDEV, FUX[3], FUX[16], ), FDEV < 1e-14 and MDEV < 1e-14
      and max(FUX.values()) < 0.0)

check("H3 [actual operands] extended FU versus point FN has nonzero discrepancy %.9f; exact extended convolution matches FU to %.1e; no false point equality" % (NDEV,EXTDEV), NDEV>1e-3 and EXTDEV<1e-14)



# Same-box true joint density versus the separately supplied classical sum.
JST=ST[(1,(2,0,0))];JG=ghat(8)
def _same_box_bilinear(a,b):
    return float(np.vdot(np.fft.fftn(a.reshape((8,)*3)),JG*np.fft.fftn(b.reshape((8,)*3))).real)/512
J1,J2,JJ=JST['e1'],JST['e2'],JST['e_joint']
CLASSICAL_RES=_same_box_bilinear(J1+J2,J1+J2)-_same_box_bilinear(J1,J1)-_same_box_bilinear(J2,J2)-2*_same_box_bilinear(J1,J2)
JOINT_RES=_same_box_bilinear(JJ,JJ)-_same_box_bilinear(J1,J1)-_same_box_bilinear(J2,J2)-2*_same_box_bilinear(J1,J2)
JD=float(np.max(abs(JJ-J1-J2)))
check("R1 [actual joint/classical distinction] density defect %.9f; same-box classical residual %.1e, true-joint residual %.9f" % (JD,CLASSICAL_RES,JOINT_RES), abs(CLASSICAL_RES)<1e-14 and abs(JOINT_RES+0.284741566)<1e-8 and abs(JD-0.210861615)<1e-8)
# Solve all actual translated edge equations, including the twist seam.
MP=np.zeros_like(M);MP[np.ix_(perm_x,perm_x)]=M;GG=np.zeros(512);GG[0]=1;todo=[0];edge_count=0;consistent=True
while todo:
    i=todo.pop()
    for j in np.flatnonzero(M[i]):
        z=GG[i]*MP[i,j]/M[i,j];edge_count+=1
        if GG[j]==0:GG[j]=z;todo.append(int(j))
        elif GG[j]!=z:consistent=False
p,h,_,_,_,_=make_pair(1,(0,0,0));DD=np.outer(p,p)-np.outer(h,h);DT=np.zeros_like(DD);DT[np.ix_(perm_x,perm_x)]=DD;DG=GG[:,None]*DT*GG[None,:];et=np.empty(512);et[perm_x]=np.sum(M*DD,axis=1);cov=float(np.max(abs(np.sum(M*DG,axis=1)-et)));mr=float(np.max(abs(MP-GG[:,None]*M*GG[None,:])))
check("R2 [complete actual translation] %d directed equations, matrix residual %.0e, row-energy residual %.1e; old KS-only residual retained separately" % (edge_count,mr,cov), edge_count==3072 and consistent and np.all(abs(GG)==1) and mr==0 and cov<1e-14)
POS=_same_box_bilinear(J1,J1);CROSS=_same_box_bilinear(J1,-J1)
check("R3 [PSD is quadratic] Q(e1)=%.9f positive but B(e1,-e1)=%.9f negative" % (POS,CROSS), POS>0 and CROSS<0 and abs(POS+CROSS)<1e-14)

print("SUMMARY: distinct joint/classical sources, exact conditional action and extended-force sign, finite point approximation. Physical preparation/readout/force identification remains supplied.")
print("per_element: checked finite source sums and exact stated scalar identities; physical interpretation is not supplied")
print("per_site: checked declared coordinate/record/source dictionaries on finite sites; no fine-site formation mechanism follows")
print("per_mode: checked the stated one-particle or Fourier modes only; no unexecuted interacting or APS boundary spectrum")
print("per_block: checked named finite preparations, response boxes or sign-field families at their stated tolerances")
print("lattice_wide: checked and not executed — no physical infinite-volume formation law or numerical limit error bound is certified")

print("TOTAL: PASS=%d FAIL=%d" % (PASS, FAIL))
sys.exit(0 if FAIL == 0 else 1)
