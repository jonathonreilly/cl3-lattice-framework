#!/usr/bin/env python3
"""Finite supplied gravity model, corrected after independent review.

No physical carrier, source law, clock, metric, or cosmological conclusion is
derived. See the source-bound companion note for all assumptions and scopes.
Central derivatives have O(g**2) error for smooth dependence; finite packet
Richardson values assume an unproved width expansion. Deterministic inputs do
not guarantee bitwise reproducibility across platforms. Historical originals
are archived outside active discovery.
"""
from __future__ import annotations

import sys

from pathlib import Path
import hashlib

# Exact note body supplies all model assumptions; every science helper is inline.
AUDIT_INPUT_PATHS = ('docs/THE_RECORD_MAP_KEEPS_THE_MASS_FRACTION_OF_THE_ENERGY_THE_VACUUMS_WEIGHTLESSNESS_IS_A_REFERENCE_CHOICE_BOUNDED_THEOREM_NOTE_2026-09-04.md',)
EXPECTED_INPUT_SHA256 = {'docs/THE_RECORD_MAP_KEEPS_THE_MASS_FRACTION_OF_THE_ENERGY_THE_VACUUMS_WEIGHTLESSNESS_IS_A_REFERENCE_CHOICE_BOUNDED_THEOREM_NOTE_2026-09-04.md': '4debfd875466c0be5b5d5bda5e686154fcfdeee0a84f8eb593cb6fe3b76b07aa'}

def verify_inputs():
    root = Path(__file__).resolve().parents[1]
    for rel, expected in EXPECTED_INPUT_SHA256.items():
        actual = hashlib.sha256((root / rel).read_bytes()).hexdigest()
        if actual != expected:
            raise RuntimeError(f"scientific input changed: {rel}")
    print("INPUT_BINDING: exact companion note verified; finite supplied definitions only")

verify_inputs()


import numpy as np
import scipy.sparse as sp
from scipy.special import jv

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


# Finite calculation group

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
        """The supplied two-weight family H(alpha, beta) on this box."""
        alpha, beta = ab
        H = np.zeros((self.V, self.V))
        w = self.vhop if Phi is None else self.vhop * (
            1.0 + 0.5 * alpha * (Phi[self.r] + Phi[self.c]))
        np.add.at(H, (self.r, self.c), w)
        d = m * self.sgn if Phi is None else m * self.sgn * (1.0 + beta * Phi)
        return H + np.diag(d)

    def sea(self, H):
        """The half-filled sea: negative levels occupied, zero modes half occupied (a covariance there)."""
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


# Finite calculation group

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
    'A1' + " " + f'Chosen rank-one occupation pinching, actual PERIODIC2x2x3 Fock dim{DIMF}: local hop diagonals={MAXHOP:.3e}; TOTAL SUMHOP Frobenius norms {NRM:.6f},{OFFW:.6f}. Odd periodic z is not a bipartite even torus.',
    MAXHOP == 0.0 and abs(OFFW - NRM) == 0.0,
)
check(
    'A2' + " " + f'Occupation pinching keeps diagonal mass and kills hopping: mass residual={DEVM:.3e}, total-vs-mass residual={DEVT:.3e}; B_v=I-2n_v is a definition, no physical six-record carrier supplied.',
    DEVM == 0.0 and DEVT == 0.0,
)
ONE1 = Box(4, 4, 4)
D1P = float(np.abs(np.diag(ONE1.hmat(0.0))).max())
check(
    'A3' + " " + f'One-particle4^3 hopping diagonal={D1P:.3e}; same chosen occupation pinching identity.',
    D1P == 0.0,
)
sys.stdout.flush()


# Finite calculation group

P8 = Box(8, 8, 8)
P12 = Box(12, 12, 12)
M8 = P8.hmat(0.0)
W2, U2 = np.linalg.eigh(M8 @ M8)


def closed_form(m):
    """r_v = -(m^2/2) [(M^2 + m^2)^{-1/2}]_vv, the staggered chiral condensate."""
    if m == 0.0:
        return np.zeros_like(W2)  # zero mass operator, not zero times singular inverse
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
    'B1' + " " + f'Even bipartite8^3, m>0: inverse-square-root formula residual={max(q[2] for q in BROWS):.3e};12^3 m1 mean={R12.mean():.12f}, spread={R12.max()-R12.min():.3e}. Requires anticommutation and gap.',
    max(q[2] for q in BROWS) < 1e-11 and R12.mean() < -1e-3
    and (R12.max() - R12.min()) < 1e-13,
)
check(
    'B2' + " " + f'm=0 diagonal mass is zero operator, max12^3 expectation={np.abs(R12_0).max():.3e}; only the stipulated D(H) source/coupling vanishes.',
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
    'B3' + " " + f'Uniform positive H(1,1) rescaling: occupation response={CH1[2]:.3e}, read response-self residual={abs(CH1[0]-CH1[1]):.3e}; read={CH1[0]:.9f}, total={CTOT}, fraction={abs(CH1[0]/CTOT["H(1,1)"]):.9f}.',
    CH1[2] < 1e-6 and abs(CH1[0] - CH1[1]) < 1e-9 and CH1[0] < 0
    and CTOT["H(1,1)"] < 0 and abs(CHI[0.0][0]) == 0.0,
)
# Same periodic2x2x3, full4096 Fock Hamiltonian; no dense4096**2 allocation.
EMOP = sum(MASSD).tocsr()
HF = (SUMHOP + EMOP).tocsr()
v0 = np.sin(np.arange(DIMF, dtype=float) + 0.37)
WC, UC = sp.linalg.eigsh(HF, k=1, which="SA", v0=v0, tol=1e-12)
GS = UC[:, 0]
PROB = abs(GS)**2
# D(|g><g|) has exactly PROB as its full occupation distribution.
# All dephased expectations are diagonal contractions, no density matrix needed.
NDIAG = np.array([NOP[v].diagonal() for v in range(NQ)])
RECDEV = float(np.abs(NDIAG @ PROB - NDIAG @ PROB).max())
EG = float(GS @ (HF @ GS))
EGD = float(PROB @ HF.diagonal())
HOPD_G = float(GS @ (SUMHOP @ GS))
HOPD_D = float(PROB @ SUMHOP.diagonal())
# The free-fermion many-body minimum is independently the sum of negative
# one-body eigenvalues minus the normal-ordering constant, even on this odd torus.
one_body = CUBE.hmat(MC)
one_levels = np.linalg.eigvalsh(one_body)
FREE_MIN = float(one_levels[one_levels < 0].sum() - 0.5*np.trace(one_body))
GROUND_RES = float(np.linalg.norm(HF @ GS - WC[0]*GS))
check(f"B4a same-fixture sparse ground residual={GROUND_RES:.3e}, free-fermion minimum error={abs(EG-FREE_MIN):.3e}",
      GROUND_RES < 1e-9 and abs(EG-FREE_MIN) < 1e-9)
check(
    'B4' + " " + f'Same PERIODIC2x2x3 Fock fixture: full occupation distribution preserved by dephasing; marginal residual={RECDEV:.3e}; energy={EG:.9f} vs dephased={EGD:.9f}; hop={HOPD_G:.9f} vs {HOPD_D:.9f}; per-site difference={(EG-EGD)/NQ:.6f}. This chosen distribution cannot reconstruct all state energies.',
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
    'B5' + " " + f'Even6^3 mass-sign occupation relation: (m,relation residual,offset)={CROWS}; closed-form residual={CFIMP:.3e}. Finite supplied model only.',
    max(q[1] for q in CROWS) < 1e-12 and CROWS[0][2] < 1e-12 and CROWS[2][2] > 0.1
    and CFIMP < 1e-12,
)
sys.stdout.flush()


# Finite calculation group

def disp2(p, m):
    return sum(2.0 - 2.0 * np.cos(pa) for pa in p) + m * m


def a_master(alpha, beta, p, m):
    """The supplied family's master acceleration law a_x/g."""
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
    'C1' + " " + f'Stipulate coupling to occupation-pinched density: alpha0,beta1; w=m**2/E and a_x/g=-4*m**2*cos(px)/E**2 for E>0; {BAD} mismatches over {len(MOMENTA)}x{len(MFIT)} formula controls.',
    BAD == 0,
)
BAND = [a_master(*READ, (0.0, 0.0, 0.0), m) for m in (0.25, 0.5, 1.0, 2.0, 4.0)]
NUMB = [-4.0 / m for m in (0.25, 0.5, 1.0, 2.0, 4.0)]
check(
    'C2' + " " + f'At p0, m>0 supplied band formula gives {BAND}; comparison count expression={NUMB}. Transverse a/-4=1-chi, chi=1-m**2/E**2, not physical speed squared.',
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
print("   sqrt(chi)  read(0,1)  tot(1,1)  full(2,1)   1-chi   1+chi")
for q in VROWS:
    print("  %4.2f  %9.6f %9.6f %11.6f %8.4f %7.4f"
          % (q[0], q[1], q[2], q[3], 1 - q[0] ** 2, 1 + q[0] ** 2))
MLESS = max(abs(a_master(*READ, (px, py, 0.0), 0.0))
            for px in (0.0, 0.3, 0.9) for py in (0.4, 0.7854, 1.2))
check(
    'C3' + " " + f'm=0: dH/dPhi=0 for READ coupling; nine momentum acceleration formulas max={MLESS:.3e}; chi-table identity residual={max(abs(q[1]-(1-q[0]**2)) for q in VROWS):.3e}. No photon/curvature claim.',
    MLESS == 0.0 and max(abs(q[1] - (1 - q[0] ** 2)) for q in VROWS) < 1e-12,
)
# Actual lattice group speed v/c=sin(py)/E at px=pz=0, with c=2.
# Equal physical speed need not give equal chi=1-m^2/E^2.
SPEED_ROWS = []
for py_control in (PI/3, PI/2):
    mass_control = np.sqrt(2.0)
    e2_control = disp2((0.,py_control,0.), mass_control)
    SPEED_ROWS.append((float(py_control),float(np.sin(py_control)/np.sqrt(e2_control)),
                       float(1-mass_control**2/e2_control),
                       float(a_master(*READ,(0.,py_control,0.),mass_control))))
check(f"C3a equal physical speed, different chi and acceleration (py,v/c,chi,a/g)={SPEED_ROWS}",
      abs(SPEED_ROWS[0][1]-.5) < 1e-12 and abs(SPEED_ROWS[1][1]-.5) < 1e-12
      and abs(SPEED_ROWS[0][3]+8/3) < 1e-12 and abs(SPEED_ROWS[1][3]+2) < 1e-12)

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
    'C4' + " " + f'Bipartite12^3: m<Eps>=m**2/E from anticommutator; nine selected energy eigenvectors, not specified momenta; max errors={max(q[4] for q in SROWS):.3e},{max(q[5] for q in SROWS):.3e}; rows={SROWS}. Lorentz scalar/stress tensor identification is unproved.',
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
    'C5' + " " + f'Definition check: returned read density is returned mass density, residual={max(q[2] for q in WROWS):.3e}; sea mass fractions={WROWS}. Not independent evidence for a record or source law.',
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
    """d<a_x>/dg by central difference; a_x = -<[H,[H,X]]>, never fitted."""
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
    'C6' + " " + f'96x32x4 finite packet central derivatives g={GSLAB:.1e}, widths10/14/20 with two-width Richardson assumption: max formula discrepancy={max(q[5] for q in EROWS):.7f}, massless={MZ[3]:.3e}, read/tot={MT[3]/TT[3]:.7f} vs {MT[4]/TT[4]:.7f}. Residual origin not isolated.',
    max(q[5] for q in EROWS) < 1e-1 and abs(MZ[3]) < 1e-12,
)
sys.stdout.flush()


# Finite calculation group

RADII = (1.0, 3.0, 10.0, 1.0e3, 1.0e6, 1.0e12)
LAM = [3.0 / (R * R) for R in RADII]
check(
    'D1' + " " + f'Separate finite-radius arithmetic R={RADII},3/R**2={LAM}; positive for every finite R>0. This supplies no cosmological conclusion from P0 or reference subtraction.',
    all(v > 0.0 for v in LAM) and LAM[-1] < 1e-20,
)
check(
    'D2' + " " + f'Supplied8^3 m1 sea total={CHI[1.0][3]:.7f} and pinched={CHI[1.0][1]:.7f} are nonzero dimensionless model densities. Neither determines cosmological Lambda or a radius.',
    abs(CHI[1.0][3]) > 0.1 and abs(CHI[1.0][1]) > 0.1,
)

print("SUMMARY: finite conditional identities and declared-fixture calculations only; physical source, carrier, metric and cosmology remain open.")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
sys.exit(1 if FAIL else 0)
