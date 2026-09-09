#!/usr/bin/env python3
"""The record map keeps the mass fraction of the energy, and the vacuum's
weightlessness is a reference choice, not a readability theorem.

Class-A runner.  Conditional on exactly what the vacuum-response note is
conditional on -- the designed fermion law, the landed weak-field response
surface phi = G0 P0 rho, the CHOICE of the half-filled staggered sea as the
vacuum, and the landed two-weight family

    H(alpha, beta) = sum_bonds [1 + alpha (Phi_v + Phi_j)/2] M_vj
                   + sum_v     [1 + beta  Phi_v]            m eps_v n_v

-- and on two STIPULATIONS made here and derived from nothing: (W1) the record
map of the canonical record-outcome principle, D(O) = sum_k P_k O P_k, is read
at the site-occupation decomposition, so a record pattern is a full occupation
configuration and D is the diagonal in the record basis; (W2) the reference an
energy density is counted from is a law-level declaration, half filling (I/2)
and the sea both being carried.

  A  (T1)  THE RECORD MAP ON THE ENERGY DENSITY, EXACTLY.  D(eps^hop_v) = 0 at
           every site and D(eps^tot_v) = m s_v (n_v - 1/2) = -(m/2) s_v B_v.
  B  (T2)  THE SEA'S READABLE ENERGY DOES NOT VANISH FOR m != 0.  The closed
           form, its Phi-response, the m = 0 zero operator, the
           record-dephased twin, and PR #7892's C relation.
  C  (T3)  THE READABLE-SOURCE COUPLING IS (alpha, beta) = (0, 1).  Bending
           factor 0, free fall -4 at rest for every mass, -4 (1 - v^2) in
           velocity, a massless packet that does not fall, the trace source
           m^2/E, and the mass-fraction identity.
  D  (T4)  THE COSMOLOGICAL-CONSTANT IDENTITY, BY DOMAIN.  3/R^2 > 0 at every
           finite R, so Lambda_vac = 0 evacuates the antecedent R > 0 rather
           than contradicting the conclusion.

Groups A1-A3, B4a, C1-C3 and D1 are exact identities; every other check is a
finite floating-point computation reporting its residual against a tolerance
declared before the run.  Every response is an exact central difference in the
field knob, so the O(Phi^2) part cancels by construction, and nothing is
fitted except the declared two-point Richardson extrapolation in 1/sigma_x^2,
whose inputs are printed.

NO RANDOM NUMBER IS DRAWN ANYWHERE: every mass, momentum, box, slab, packet
width and field knob is a declared constant, so the runner is bit-reproducible
without a seed.

Largest dense object: the 12 x 12 x 12 periodic sea's one-body matrix,
1728 x 1728.  The many-body statements are the 2 x 2 x 3 coarse cube read in
its 12-qubit space, dim 2^12 = 4096; nothing above 4096 x 4096 is formed.  The
slabs are handled matrix-free by Chebyshev propagation on vectors.

This runner is self-contained: it re-declares the coarse lattice, the KS sign
field, the record-native staggered mass, the record map, the two-weight family,
the local energy density, the two references and the slab propagator, and
imports nothing from the repository.

Output: one PASS/FAIL line per check and a final `TOTAL: PASS=N FAIL=M`.
Exit code 0 iff FAIL = 0.
"""
from __future__ import annotations

import sys

import numpy as np
import scipy.sparse as sp
from scipy.special import jv

AUDIT_TIMEOUT_SEC = 300

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
GK = 1.0e-5                        # the field knob; every response is a central difference
GSLAB = 2.0e-4                     # the slab's field gradient
READ, ENERGY, FULLM = (0.0, 1.0), (1.0, 1.0), (2.0, 1.0)
MASSES = (0.0, 0.3, 1.0, 2.0, 6.0)
# the DECLARED FIXED momentum list for the closed-form cross-check (no seed)
MOMENTA = ((0.0, 0.0, 0.0), (0.3, 0.0, 0.0), (0.0, 0.5, 0.0), (0.7, 0.2, 0.4),
           (1.1, 0.9, 0.3), (-0.6, 0.4, 1.0), (0.2, -0.8, 0.5), (1.2, 1.2, 1.2),
           (0.05, 0.05, 0.05), (0.9, 0.0, 0.6), (-1.0, 0.7, -0.2), (0.4, 1.1, 0.8))
MFIT = (0.05, 0.4, 1.0, 2.0)


# ===================================================== THE LATTICE, DECLARED HERE

def eta_ks(v, a):
    """Kawamoto-Smit sign of the coarse bond (v, v + e_a)."""
    if a == 0:
        return 1
    if a == 1:
        return -1 if (v[0] & 1) else 1
    return -1 if ((v[0] + v[1]) & 1) else 1


class Box:
    """A dense coarse box: KS hopping matrix, half-filled sea, energy density."""

    def __init__(self, Lx, Ly, Lz, per=(True, True, True)):
        self.L = (Lx, Ly, Lz)
        self.V = Lx * Ly * Lz
        ix, iy, iz = np.meshgrid(*[np.arange(n) for n in self.L], indexing="ij")
        self.sgn = (-1.0) ** (ix + iy + iz).ravel()
        r, c, val, pair = [], [], [], []

        def idx(a, b, k):
            return (a * Ly + b) * Lz + k

        for a in range(Lx):
            for b in range(Ly):
                for k in range(Lz):
                    i, v = idx(a, b, k), (a, b, k)
                    for ax in range(3):
                        w = [a, b, k]
                        w[ax] += 1
                        if w[ax] >= self.L[ax]:
                            if not per[ax]:
                                continue
                            w[ax] = 0
                        j = idx(*w)
                        if j == i:
                            continue
                        s = float(eta_ks(v, ax))
                        r += [i, j]
                        c += [j, i]
                        val += [s, s]
                        pair.append((i, j, s))
        self.r, self.c = np.array(r), np.array(c)
        self.vhop = np.array(val)
        self.pairs = pair
        self.zero = np.zeros(self.V)
        self.one = np.ones(self.V)

    def hmat(self, m, Phi=None, ab=ENERGY):
        """The landed two-weight family H(alpha, beta) on this box."""
        alpha, beta = ab
        H = np.zeros((self.V, self.V))
        w = self.vhop if Phi is None else self.vhop * (
            1.0 + 0.5 * alpha * (Phi[self.r] + Phi[self.c]))
        np.add.at(H, (self.r, self.c), w)
        d = m * self.sgn if Phi is None else m * self.sgn * (1.0 + beta * Phi)
        return H + np.diag(d)

    def sea(self, H):
        """The half-filled sea: the spectral projector on the negative levels."""
        w, U = np.linalg.eigh(H)
        occ = (w < -1e-12).astype(float) + 0.5 * (np.abs(w) <= 1e-12)
        return (U * occ) @ U.T

    def dens(self, m, Phi=None, ab=ENERGY):
        """(readable r_v, total E_v, mass part), all counted from HALF FILLING."""
        H = self.hmat(m, Phi, ab)
        Rt = self.sea(H) - 0.5 * np.eye(self.V)
        Ev = np.einsum("vj,jv->v", H, Rt)
        Em = np.diag(H) * np.diag(Rt)
        return Em.copy(), Ev, Em

    def occ(self, m, Phi=None, ab=ENERGY):
        return np.diag(self.sea(self.hmat(m, Phi, ab))).copy()

    def wave(self, nvec):
        """The declared plane-wave field profile cos(k.v)."""
        ix, iy, iz = np.meshgrid(*[np.arange(n) for n in self.L], indexing="ij")
        kk = [2 * PI * nvec[i] / self.L[i] for i in range(3)]
        f = np.cos(kk[0] * ix + kk[1] * iy + kk[2] * iz).ravel()
        return f, 6.0 - 2.0 * sum(np.cos(kk[a]) for a in range(3))


# ============================== A (T1).  THE RECORD MAP ON THE ENERGY DENSITY

CUBE = Box(2, 2, 3)
NQ = CUBE.V
DIMF = 1 << NQ
MC = 1.0

I2 = sp.identity(2, format="csr")
ZM = sp.csr_matrix(np.array([[1.0, 0.0], [0.0, -1.0]]))
AM = sp.csr_matrix(np.array([[0.0, 1.0], [0.0, 0.0]]))


def kron(ops):
    out = ops[0]
    for o in ops[1:]:
        out = sp.kron(out, o, format="csr")
    return out


COP = [kron([ZM] * v + [AM] + [I2] * (NQ - v - 1)) for v in range(NQ)]
NOP = [(COP[v].T @ COP[v]).tocsr() for v in range(NQ)]
IDF = sp.identity(DIMF, format="csr")


def hop_density(v):
    """eps^hop_v = (1/2) sum_{j~v} M_vj (c^+_v c_j + c^+_j c_v)."""
    out = sp.csr_matrix((DIMF, DIMF))
    for (i, j, s) in CUBE.pairs:
        if i == v or j == v:
            out = out + 0.5 * s * (COP[i].T @ COP[j] + COP[j].T @ COP[i])
    return out.tocsr()


def mass_density(v, m):
    """eps^mass_v = m s_v (n_v - 1/2) = -(m/2) s_v B_v, B_v = I - 2 n_v."""
    return ((m * CUBE.sgn[v]) * (NOP[v] - 0.5 * IDF)).tocsr()


def record_map(O):
    """D(O) = sum_r P_r O P_r with P_r = |record config><record config|."""
    return sp.diags(O.diagonal()).tocsr()


HOPD = [hop_density(v) for v in range(NQ)]
MASSD = [mass_density(v, MC) for v in range(NQ)]
MAXHOP = max(float(np.abs(h.diagonal()).max()) for h in HOPD)
DEVM = max(float(abs(record_map(x) - x).max()) for x in MASSD)
DEVT = max(float(abs(record_map(HOPD[v] + MASSD[v]) - MASSD[v]).max()) for v in range(NQ))
SUMHOP = HOPD[0]
for h in HOPD[1:]:
    SUMHOP = SUMHOP + h
SUMHOP = SUMHOP.tocsr()
NRM = float(sp.linalg.norm(SUMHOP))
OFFW = float(sp.linalg.norm(SUMHOP - record_map(SUMHOP)))
check(
    "A1 [exact] THE RECORD MAP ANNIHILATES THE HOP ENERGY DENSITY. On the 2x2x3 cube in its "
    "%d-qubit space (dim %d), D(eps^hop_v) = 0 at EVERY site, max |diag| = %.3e -- structurally "
    "zero, since c^+_v c_j with j != v changes the record configuration. The hop energy is there "
    "and wholly unreadable: ||eps^hop||_F = %.6f = ||eps^hop - D(eps^hop)||_F = %.6f, %.1f per "
    "cent off-diagonal in the record basis"
    % (NQ, DIMF, MAXHOP, NRM, OFFW, 100.0 * OFFW / NRM),
    MAXHOP == 0.0 and abs(OFFW - NRM) == 0.0,
)
check(
    "A2 [exact] AND KEEPS THE MASS TERM WHOLE. D(eps^mass_v) = eps^mass_v to %.3e and "
    "D(eps^tot_v) = m s_v (n_v - 1/2) = -(m/2) s_v B_v to %.3e at every site, B_v = I - 2 n_v the "
    "landed corner parity: one operator identity, not an approximation"
    % (DEVM, DEVT),
    DEVM == 0.0 and DEVT == 0.0,
)
ONE1 = Box(4, 4, 4)
D1P = float(np.abs(np.diag(ONE1.hmat(0.0))).max())
check(
    "A3 [exact] THE SAME IDENTITY IN THE ONE-PARTICLE SECTOR THE GRAVITY LANE USES. The KS hop "
    "matrix on the 4^3 torus has zero diagonal, max %.3e, so D kills eps^hop there too and leaves "
    "m s_v |psi_v|^2: one-record readability carries no hop energy at any single time" % D1P,
    D1P == 0.0,
)
sys.stdout.flush()


# ======================= B (T2).  THE SEA'S READABLE ENERGY DOES NOT VANISH

P8 = Box(8, 8, 8)
P12 = Box(12, 12, 12)
M8 = P8.hmat(0.0)
W2, U2 = np.linalg.eigh(M8 @ M8)


def closed_form(m):
    """r_v = -(m^2/2) [(M^2 + m^2)^{-1/2}]_vv, the staggered chiral condensate."""
    f = (U2 * (1.0 / np.sqrt(np.maximum(W2, 0.0) + m * m))) @ U2.T
    return -(m * m / 2.0) * np.diag(f)


BROWS = []
for m in MASSES:
    r, Ev, Em = P8.dens(m)
    dev = 0.0 if m == 0.0 else float(np.abs(r - closed_form(m)).max())
    BROWS.append((m, float(r.mean()), dev,
                  float(r.max() - r.min()), float(r.mean() / Ev.mean()) if m else 0.0,
                  float(abs(Em.mean() / Ev.mean()))))
R12, EV12, EM12 = P12.dens(1.0)
R12_0, _, _ = P12.dens(0.0)
print("   m      r_v         dev     spread   r_v/E^(0)_v        w_m")
for q in BROWS:
    print("  %4.1f  %+13.9f %8.1e %8.1e  %11.9f  %11.9f"
          % (q[0], q[1], q[2], q[3], q[4], q[5]))
check(
    "B1 [numerical, 1e-11] THE SEA'S READABLE ENERGY IS NONZERO FOR m != 0, UNIFORM, NEGATIVE. "
    "<D(eps^tot_v)>_sea = m s_v (<n_v> - 1/2) = -(m^2/2) [(M^2 + m^2)^{-1/2}]_vv, the staggered "
    "chiral condensate, to %.1e on 8^3 over m = 0.3, 1, 2, 6; on the 12^3 sea at m = 1 it is "
    "%+0.12f per site, uniform in v to %.1e"
    % (max(q[2] for q in BROWS), float(R12.mean()), float(R12.max() - R12.min())),
    max(q[2] for q in BROWS) < 1e-11 and R12.mean() < -1e-3
    and (R12.max() - R12.min()) < 1e-13,
)
check(
    "B2 [exact] AT m = 0 THE READABLE OPERATOR IS THE ZERO OPERATOR, SO READABILITY WOULD MAKE "
    "ALL MATTER WEIGHTLESS. D(eps^tot_v) carries an explicit factor m, so at m = 0 it vanishes as "
    "an OPERATOR, not by cancellation in a state: max |r_v| = %.1e on the 12^3 sea and exactly "
    "zero on every one-particle state"
    % float(np.abs(R12_0).max()),
    float(np.abs(R12_0).max()) == 0.0,
)
CHI = {}
for m in (0.0, 0.3, 1.0, 2.0):
    rp, _, _ = P8.dens(m, +GK * P8.one, ENERGY)
    rm, _, _ = P8.dens(m, -GK * P8.one, ENERGY)
    npv = P8.occ(m, +GK * P8.one, ENERGY)
    nmv = P8.occ(m, -GK * P8.one, ENERGY)
    r0, Ev0, _ = P8.dens(m)
    CHI[m] = (float(((rp - rm) / (2 * GK)).mean()), float(r0.mean()),
              float(np.abs(npv - nmv).max() / (2 * GK)), float(Ev0.mean()))
CH1 = CHI[1.0]
CTOT = {}
for ab, nm in ((ENERGY, "H(1,1)"), (FULLM, "H(2,1)")):
    ep, em = [P8.dens(1.0, s * GK * P8.one, ab)[1].mean() for s in (+1.0, -1.0)]
    CTOT[nm] = float((ep - em) / (2 * GK))
check(
    "B3 [numerical, 1e-9] AND ITS Phi-RESPONSE IS EXACTLY ITSELF, SAME SIGN AS THE TOTAL. Under "
    "H(1,1) and uniform Phi, H(Phi) = (1 + Phi) H_0 is a pure rescaling, so the sea projector is "
    "Phi-independent (d<n_v>/dPhi <= %.1e) and only m(1 + Phi) varies: chi_read(0) = r_v to %.1e, "
    "= %+0.9f at m = 1 on 8^3 against the total chi_0[H(1,1)] = %+0.6f -- %.2f per cent of it. D "
    "removes %.2f per cent of the vacuum response and not the last %.2f per cent"
    % (CH1[2], abs(CH1[0] - CH1[1]), CH1[0], CTOT["H(1,1)"],
       100 * abs(CH1[0] / CTOT["H(1,1)"]), 100 - 100 * abs(CH1[0] / CTOT["H(1,1)"]),
       100 * abs(CH1[0] / CTOT["H(1,1)"])),
    CH1[2] < 1e-6 and abs(CH1[0] - CH1[1]) < 1e-9 and CH1[0] < 0
    and CTOT["H(1,1)"] < 0 and abs(CHI[0.0][0]) == 0.0,
)
WC, UC = np.linalg.eigh((SUMHOP + sum(MASSD)).toarray())
GS = UC[:, 0]
RHO = np.outer(GS, GS)
RHOD = np.diag(np.diag(RHO))
MTOT = SUMHOP.toarray()
EMOP = sum(MASSD).toarray()
NDIAG = np.array([NOP[v].diagonal() for v in range(NQ)])
RECDEV = float(np.abs(NDIAG @ (np.diag(RHO) - np.diag(RHOD))).max())
EG = float(np.trace(RHO @ (MTOT + EMOP)))
EGD = float(np.trace(RHOD @ (MTOT + EMOP)))
HOPD_G = float(np.trace(RHO @ MTOT))
HOPD_D = float(np.trace(RHOD @ MTOT))
check(
    "B4 [exact] THE RECORD-DEPHASED TWIN. For |g> the cube's exact many-body ground state at "
    "m = 1 and rho_D = D(|g><g|), every record readout agrees -- max |<n_v>_g - <n_v>_D| = %.1e at "
    "all %d sites -- yet <H>_g = %+0.9f against <H>_D = %+0.9f, %.6f per site, all of it hop "
    "energy (<hop>_g = %+0.9f, <hop>_D = %+0.9f). A record-content source cannot be an energy "
    "source"
    % (RECDEV, NQ, EG, EGD, (EG - EGD) / NQ, HOPD_G, HOPD_D),
    RECDEV == 0.0 and abs(HOPD_D) < 1e-12 and abs(EG - EGD) > 1.0,
)
P6 = Box(6, 6, 6)
CROWS = []
for m in (0.0, 0.5, 1.0, 2.0):
    np_, nm_ = P6.occ(m), P6.occ(-m)
    CROWS.append((m, float(np.abs(nm_ - (1.0 - np_)).max()), float(np.abs(np_ - 0.5).max())))
CF6 = Box(6, 6, 6)
M6 = CF6.hmat(0.0)
W6, U6 = np.linalg.eigh(M6 @ M6)
CFIMP = max(
    float(np.abs((CF6.occ(m) - 0.5) + (m / 2.0) * CF6.sgn
                 * np.diag((U6 * (1.0 / np.sqrt(np.maximum(W6, 0.0) + m * m))) @ U6.T)).max())
    for m in (0.5, 1.0, 2.0))
check(
    "B5 [numerical, 1e-12] THE LANDED C-SYMMETRY STATEMENT IS CONFIRMED AND COMPLETED, NOT "
    "DISTURBED. <n_v>_{-m} = 1 - <n_v>_m holds site by site on the 6^3 sea to %.1e over "
    "m = 0, 0.5, 1, 2, with max |<n_v> - 1/2| = %.9f / %.9f / %.9f / %.9f: <n_v> = 1/2 is the C "
    "fixed point at m = 0 ONLY, as that note scopes it, and the closed form implies the relation "
    "to %.1e. C kills the readable CHARGE density; the m s_v weight un-staggers <n_v> - 1/2, so it "
    "does not kill the readable ENERGY density"
    % (max(q[1] for q in CROWS), CROWS[0][2], CROWS[1][2], CROWS[2][2], CROWS[3][2], CFIMP),
    max(q[1] for q in CROWS) < 1e-12 and CROWS[0][2] < 1e-12 and CROWS[2][2] > 0.1
    and CFIMP < 1e-12,
)
sys.stdout.flush()


# ================== C (T3).  THE READABLE-SOURCE COUPLING IS (alpha, beta) = (0, 1)

def disp2(p, m):
    return sum(2.0 - 2.0 * np.cos(pa) for pa in p) + m * m


def a_master(alpha, beta, p, m):
    """The landed family's master acceleration law a_x/g."""
    E2 = disp2(p, m)
    c, s = np.cos(p[0]), np.sin(p[0])
    return -4 * alpha * c + 8 * alpha * s * s / E2 + 4 * (alpha - beta) * m * m * c / E2


def a_weight(alpha, beta, p, m):
    """a_x/g = -4 w E''_xx + 4 E'_x w'_x with the band weight w, coded independently."""
    E = np.sqrt(disp2(p, m))
    c, s = np.cos(p[0]), np.sin(p[0])
    Epp, Ep = c / E - s * s / E ** 3, s / E
    w = alpha * (E * E - m * m) / E + beta * m * m / E
    wp = Ep * (alpha * (1.0 + m * m / (E * E)) - beta * m * m / (E * E))
    return -4 * w * Epp + 4 * Ep * wp


BAD = 0
for p in MOMENTA:
    for m in MFIT:
        E2 = disp2(p, m)
        d1 = abs(a_weight(*READ, p, m) - a_master(*READ, p, m))
        d2 = abs(a_weight(*READ, p, m) + 4 * m * m * np.cos(p[0]) / E2)
        d3 = abs((0.0 * (E2 - m * m) + 1.0 * m * m) / np.sqrt(E2) - m * m / np.sqrt(E2))
        if max(d1, d2, d3) > 1e-12:
            BAD += 1
check(
    "C1 [exact] THE READABLE SOURCE IS THE (alpha, beta) = (0, 1) CORNER OF THE LANDED TWO-WEIGHT "
    "FAMILY. Since D annihilates the hop and keeps the mass term, H_Phi = H_0 + sum_v Phi_v "
    "D(eps^tot_v) = M + m Eps (1 + Phi). Its band weight is w_read = m^2/E, and the master law and "
    "the independent -4 w E''_xx + 4 E'_x w'_x both give a_x/g = -4 m^2 cos p_x / E^2, %d "
    "mismatches over a DECLARED FIXED list of %d momenta x %d masses" % (BAD, len(MOMENTA), len(MFIT)),
    BAD == 0,
)
BAND = [a_master(*READ, (0.0, 0.0, 0.0), m) for m in (0.25, 0.5, 1.0, 2.0, 4.0)]
NUMB = [-4.0 / m for m in (0.25, 0.5, 1.0, 2.0, 4.0)]
check(
    "C2 [exact] IT PASSES AT REST AND FAILS IN VELOCITY WITH THE OPPOSITE SIGN. At rest "
    "a_x/g = %+0.12f for EVERY mass in 0.25, 0.5, 1, 2, 4, band %.1e -- not chromatic, unlike the "
    "count source's -4/m = %s. The exact transverse corollary "
    "a_perp/g = -4 [beta + (alpha - beta) v_t^2] gives -4 (1 - v_t^2) = -4/gamma^2, the mirror "
    "image about the Newtonian value of general relativity's -4 (1 + v_t^2)"
    % (BAND[0], max(BAND) - min(BAND), "/".join("%.0f" % v for v in NUMB)),
    max(BAND) - min(BAND) == 0.0 and abs(BAND[0] + 4.0) < 1e-13,
)
VROWS = []
PY = 0.4
KY = 2 - 2 * np.cos(PY)
for vt in (0.0, 0.3, 0.6, 0.9, 1.0):
    m = 0.0 if vt >= 1.0 else np.sqrt(KY * (1 - vt * vt) / max(vt * vt, 1e-300))
    p = (0.0, PY, 0.0)
    VROWS.append((vt, a_master(*READ, p, m) / -4.0, a_master(*ENERGY, p, m) / -4.0,
                  a_master(*FULLM, p, m) / -4.0))
print("   v_t  read(0,1)  tot(1,1)  full(2,1)=GR   1-v^2   1+v^2")
for q in VROWS:
    print("  %4.2f  %9.6f %9.6f %11.6f %8.4f %7.4f"
          % (q[0], q[1], q[2], q[3], 1 - q[0] ** 2, 1 + q[0] ** 2))
MLESS = max(abs(a_master(*READ, (px, py, 0.0), 0.0))
            for px in (0.0, 0.3, 0.9) for py in (0.4, 0.7854, 1.2))
check(
    "C3 [exact] SO THE LIGHT-BENDING FACTOR IS ZERO: LIGHT DOES NOT BEND AT ALL. The landed "
    "factor alpha/beta is 0/1 = 0 here, against 1 for the energy-density coupling and 2 for "
    "general relativity. At m = 0 the coupling operator dH/dPhi = m Eps is the ZERO OPERATOR: "
    "max |a_x/g| = %.1e over nine declared momenta, and a(v)/a(0) tracks 1 - v_t^2 to %.1e"
    % (MLESS, max(abs(q[1] - (1 - q[0] ** 2)) for q in VROWS)),
    MLESS == 0.0 and max(abs(q[1] - (1 - q[0] ** 2)) for q in VROWS) < 1e-12,
)
SROWS = []
for m in (0.3, 1.0, 2.0):
    wm_, Um_ = np.linalg.eigh(P12.hmat(m))
    pos = np.where(wm_ > 1e-9)[0]
    for pick in (pos[0], pos[len(pos) // 3], pos[-1]):
        psi, E = Um_[:, pick], wm_[pick]
        Sread = m * float(psi @ (P12.sgn * psi))
        SROWS.append((m, float(E), Sread, m * m / E, abs(Sread - m * m / E),
                      abs(Sread / E - m * m / (E * E))))
check(
    "C4 [numerical, 1e-14] THE READABLE SOURCE OF MATTER IS NEITHER THE ENERGY NOR THE COUNT: IT "
    "IS THE TRACE OF THE STRESS TENSOR. On 12^3 one-particle band states at m = 0.3, 1, 2 and "
    "three momenta each, <D(eps^tot)> = m <Eps> = m^2/E to %.1e on all %d rows -- the "
    "Lorentz-scalar m psi-bar psi. Hence S_read/S_tot = m^2/E^2 = 1/gamma^2 to %.1e, equal to the "
    "total only at rest and zero at m = 0: a readable-source bridge is scalar gravity"
    % (max(q[4] for q in SROWS), len(SROWS), max(q[5] for q in SROWS)),
    max(q[4] for q in SROWS) < 1e-14 and max(q[5] for q in SROWS) < 1e-14,
)
WROWS = []
for Ln in (4, 8):
    bx = Box(Ln, Ln, Ln)
    for m in (0.3, 1.0, 2.0, 6.0):
        r_, Ev_, Em_ = bx.dens(m)
        WROWS.append((Ln, m, float(np.abs(r_ - Em_).max()),
                      float(r_.mean() / Ev_.mean()), float(Em_.mean() / Ev_.mean())))
check(
    "C5 [exact] THE UNIFYING IDENTITY: D KEEPS EXACTLY THE MASS FRACTION OF THE ENERGY. For the "
    "sea r_v IS the mass part of the total energy density, deviation %.1e on the 4^3 and 8^3 boxes "
    "at m = 0.3, 1, 2, 6, so r_v/E^(0)_v = w_m exactly (%.9f at m = 1 on 8^3); for matter "
    "S_read/S_tot = 1/gamma^2 is the same statement. One identity covers vacuum and matter" % (max(q[2] for q in WROWS), [q for q in WROWS if q[0] == 8 and q[1] == 1.0][0][3]),
    max(q[2] for q in WROWS) == 0.0
    and max(abs(q[3] - q[4]) for q in WROWS) < 1e-15,
)
sys.stdout.flush()


# ---------------- the slab: matrix-free Chebyshev propagation on vectors, no dense object

class Slab:
    """Coarse slab, open in x, periodic in y and z; sparse bonds only."""

    def __init__(self, Lx, Ly, Lz):
        self.Lx, self.Ly, self.Lz = Lx, Ly, Lz
        self.V = Lx * Ly * Lz
        ix, iy, iz = np.meshgrid(np.arange(Lx), np.arange(Ly), np.arange(Lz), indexing="ij")
        self.xs, self.ys, self.zs = (a.ravel().astype(float) for a in (ix, iy, iz))
        self.sgn = (-1.0) ** (ix + iy + iz).ravel()
        r, c, val, dx = [], [], [], []

        def idx(a, b, k):
            return (a * Ly + b) * Lz + k

        for a in range(Lx):
            for b in range(Ly):
                for k in range(Lz):
                    i, v = idx(a, b, k), (a, b, k)
                    for ax in range(3):
                        w = [a, b, k]
                        w[ax] += 1
                        if ax == 0:
                            if w[0] >= Lx:
                                continue
                        else:
                            w[ax] %= (Ly if ax == 1 else Lz)
                        j = idx(*w)
                        s = float(eta_ks(v, ax))
                        r += [i, j]
                        c += [j, i]
                        val += [s, s]
                        d = 1.0 if ax == 0 else 0.0
                        dx += [d, -d]
        self.r, self.c = np.array(r), np.array(c)
        self.vhop, self.dxb = np.array(val), np.array(dx)

    def _coo(self, vals):
        return sp.csr_matrix((vals, (self.r, self.c)), shape=(self.V, self.V))

    def bond(self, Phi, alpha):
        return self.vhop * (1.0 + 0.5 * alpha * (Phi[self.r] + Phi[self.c]))

    def H(self, m, Phi, ab):
        alpha, beta = ab
        return (self._coo(self.bond(Phi, alpha))
                + sp.diags(m * self.sgn * (1.0 + beta * Phi))).tocsr()

    def Cx(self, Phi, alpha):
        return self._coo(self.bond(Phi, alpha) * self.dxb)


def gersh(m, pmax):
    return 6.0 * (1.0 + 2.0 * abs(pmax)) + abs(m) * (1.0 + abs(pmax)) + 0.05


def cheb_evolve(H, psi, dt, B):
    th = B * dt
    N = int(th + 25 + 4 * th ** (1.0 / 3.0))
    n = np.arange(N + 1)
    cf = (2.0 - (n == 0)) * (-1j) ** n * jv(n, th)
    N = int(np.where(np.abs(cf) > 1e-16)[0].max())
    t0, t1 = psi, H.dot(psi) / B
    out = cf[0] * t0 + cf[1] * t1
    for k in range(2, N + 1):
        t2 = 2.0 * (H.dot(t1) / B) - t0
        out = out + cf[k] * t2
        t0, t1 = t1, t2
    return out


def cheb_apply(H, psi, f, B, N=700, K=4096):
    th = PI * (np.arange(K) + 0.5) / K
    fv = f(B * np.cos(th))
    cf = np.array([(2.0 - (n == 0)) / K * np.sum(fv * np.cos(n * th)) for n in range(N + 1)])
    t0, t1 = psi, H.dot(psi) / B
    out = cf[0] * t0 + cf[1] * t1
    for k in range(2, N + 1):
        t2 = 2.0 * (H.dot(t1) / B) - t0
        out = out + cf[k] * t2
        t0, t1 = t1, t2
    return out


def packet(L, m, p, x0, sx, sy):
    """Positive-band Gaussian wavepacket at Dirac momentum p; no random number."""
    dx = L.xs - x0
    dy = (L.ys - L.Ly / 2.0 + L.Ly / 2) % L.Ly - L.Ly / 2
    env = np.exp(-dx ** 2 / (2 * sx ** 2) - dy ** 2 / (2 * sy ** 2))
    k = [(PI + pa) / 2.0 for pa in p]
    ph = np.exp(1j * (k[0] * L.xs + k[1] * L.ys + k[2] * L.zs))
    E0 = np.sqrt(disp2(p, m))
    w = max(0.12, 0.30 * E0)
    H = L.H(m, np.zeros(L.V), ENERGY)
    psi = cheb_apply(H, (env * ph).astype(complex),
                     lambda e: np.exp(-(e - E0) ** 2 / (2 * w * w)), gersh(m, 0.0))
    return psi / np.linalg.norm(psi)


def ehrenfest(L, m, p, ab, g, sx, T=10.0, dt=0.25):
    """d<a_x>/dg by exact central difference; a_x = -<[H,[H,X]]>, never fitted."""
    psi0 = packet(L, m, p, L.Lx / 2.0, sx, 9.0)
    Phi1 = L.xs - L.Lx / 2.0
    acc = {}
    for sgn in (+1.0, -1.0):
        Phi = sgn * g * Phi1
        H, Cx = L.H(m, Phi, ab), L.Cx(Phi, ab[0])
        B = gersh(m, float(np.max(np.abs(Phi))))
        psi, ax = psi0.copy(), []
        for it in range(int(round(T / dt)) + 1):
            ax.append(-2.0 * np.vdot(H.dot(psi), Cx.dot(psi)).real)
            if it < int(round(T / dt)):
                psi = cheb_evolve(H, psi, dt, B)
        acc[sgn] = np.array(ax)
    return float(((acc[1.0] - acc[-1.0]) / (2 * g)).mean())


SL = Slab(96, 32, 4)
EROWS = []
print("    m    p_y      cp     sx=10      sx=14      sx=20   Richardson     closed")
for (m, py) in ((1.0, 0.0), (0.4, 0.7854), (0.0, 0.7854)):
    for ab, nm in ((READ, "read"), (ENERGY, "tot")):
        vals = [ehrenfest(SL, m, (0.0, py, 0.0), ab, GSLAB, sx) for sx in (10.0, 14.0, 20.0)]
        rich = (vals[2] * 400.0 - vals[1] * 196.0) / (400.0 - 196.0)
        ac = a_master(*ab, (0.0, py, 0.0), m)
        EROWS.append((m, py, nm, rich, ac, abs(rich - ac)))
        print("  %4.1f %6.4f %7s %10.6f %10.6f %10.6f %11.6f %10.6f"
              % (m, py, nm, vals[0], vals[1], vals[2], rich, ac))
MZ = [q for q in EROWS if q[0] == 0.0 and q[2] == "read"][0]
MT = [q for q in EROWS if q[0] == 0.4 and q[2] == "read"][0]
TT = [q for q in EROWS if q[0] == 0.4 and q[2] == "tot"][0]
check(
    "C6 [numerical, extrapolated, 1e-1] AND IT IS MEASURED, NOT ONLY ARGUED. Exact Ehrenfest "
    "accelerations on the 96 x 32 x 4 slab under Phi = g (x - x_c), g = %.0e, differenced "
    "centrally in g and Richardson-extrapolated in 1/sigma_x^2 from sigma_x = 14, 20, match the "
    "closed form on every row to %.1e, and the massless row is EXACTLY %.1e. Measured read/tot at "
    "m = 0.4, p_y = pi/4 is %.6f against the closed %.6f. REPORTED HONESTLY: the m = 1 at-rest "
    "read row is %.1f per cent short of -4 after extrapolation because w_read = m^2/E is curved in "
    "E and the packet has a finite momentum spread; the tot rows close to %.1f per cent"
    % (GSLAB, max(q[5] for q in EROWS), MZ[3], MT[3] / TT[3], MT[4] / TT[4],
       100 * EROWS[0][5] / 4.0, 100 * EROWS[1][5] / 4.0),
    max(q[5] for q in EROWS) < 1e-1 and abs(MZ[3]) < 1e-12,
)
sys.stdout.flush()


# ============= D (T4).  THE COSMOLOGICAL-CONSTANT IDENTITY IS RECONCILED BY DOMAIN

RADII = (1.0, 3.0, 10.0, 1.0e3, 1.0e6, 1.0e12)
LAM = [3.0 / (R * R) for R in RADII]
check(
    "D1 [statement + exact arithmetic] Lambda_vac = 0 DOES NOT CONTRADICT Lambda = 3/R^2; IT "
    "EVACUATES ITS ANTECEDENT. Both legs are GEOMETRIC: Leg A trace-contracts the textbook vacuum "
    "Einstein equation on a GIVEN de Sitter throat, and Leg B is the Obata equality on the round "
    "three-sphere; no energy density enters either. Condition 4 reads 'for any R > 0', an OPEN ray "
    "not containing its limit point, and 3/R^2 = %s at R = %s is positive at every finite radius. "
    "Lambda_vac = 0 is R = infinity, off that domain: the antecedent is not instantiated"
    % ("/".join("%.0e" % v for v in LAM), "/".join("%.0e" % R for R in RADII)),
    all(v > 0.0 for v in LAM) and LAM[-1] < 1e-20,
)
check(
    "D2 [statement] SO KEEPING BOTH NEEDS A THIRD DECLARATION OF WHAT Lambda NAMES. Leg A takes "
    "Lambda from where a vacuum energy density sits in the field equation; Leg B reads it as the "
    "spectral gap of the retained spatial slice. On the first reading a chain whose vacuum source "
    "vanishes at every k says Lambda_vac = 0 about that same object; on the second, Lambda is a "
    "datum of the retained S^3 topology. The sea's total density (%+0.4f per site at m = 1 on 8^3) "
    "and its readable part (%+0.4f) are both cutoff scale, so the choice is urgent. NOT made here" % (CHI[1.0][3], CHI[1.0][1]),
    abs(CHI[1.0][3]) > 0.1 and abs(CHI[1.0][1]) > 0.1,
)

print(
    "SUMMARY: the record map keeps exactly the mass fraction of the energy, so the readable "
    "source is the trace of the stress tensor and a readable-source bridge is scalar gravity with "
    "bending factor zero and the wrong velocity sign. The sea's readable energy does not vanish "
    "for m != 0 and responds to Phi with the sign of the total, so weightlessness does not follow "
    "from readability: it is a reference choice, the sea-referenced source the landed notes "
    "already use, and it must be declared as such."
)
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
sys.exit(1 if FAIL else 0)
