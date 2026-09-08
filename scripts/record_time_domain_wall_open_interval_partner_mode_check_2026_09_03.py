#!/usr/bin/env python3
"""The record-time domain wall on an open interval: where the partner Weyl mode lives.

Self-contained free-field one-particle runner.  Record time is a SUPPLIED extra
coordinate `s`: an ordered chain of `N_s` sites with nearest-neighbour
adjacency, a hermitian momentum `K_s`, a Wilson Laplacian `r_s L_s`, a fifth
Clifford generator `Gamma_s`, a supplied mass field `m(s)`, a supplied length
`L_5 = N_s` and a supplied boundary condition.  The four-component embedding is

    Gamma_i = tau_1 (x) sigma_i,  Gamma_s = tau_2 (x) I,  Gamma_m = tau_3 (x) I,
    chi = i Gamma_s Gamma_m = -tau_1 (x) I,

    H(p) = sum_i sin(p_i) Gamma_i + K_s (x) Gamma_s
           + [ diag(m(s)) + r_s L_s + r sum_i (1 - cos p_i) ] (x) Gamma_m.

  A  T1  Reconstruct the historical periodic finite diagnostic.
  B  T2  Open low spaces below numerical resolution, approximate Weyl
         dispersion and signed finite WINDOW diagnostic across an avoided gap.
  C  T3  All 2592 executed finite cutoff-count/net-chi cases, not every
         localized species or an all-parameter finite cutoff theorem.
  D  T4  Finite window/length data and balanced pairing, not exact unpairing.
  E  T5  Nonindependent supplied inputs and distinct withdrawal/comparator
         operators; no physical Record-time or readout mechanism supplied.

The lattice is physical.  Nothing here is derived from any axiom, no axiom is
amended, no status is set and no registry entry is created.  Group C is a
verification on a declared finite family, not a proof, and not a general no-go.

Output: one PASS/FAIL line per check and a final `TOTAL: PASS=N FAIL=M`.
Exit code 0 iff FAIL = 0.
"""

from __future__ import annotations

import itertools
import hashlib
from pathlib import Path
from fractions import Fraction
from decimal import Decimal, localcontext
import math
import sys

import numpy as np

AUDIT_TIMEOUT_SEC = 150

# Semantic input identity: the model is self-contained; these are the current
# note and exact quoted ontology/comparison boundaries, not parent campaigns.
AUDIT_INPUT_PATHS = ('docs/THE_RECORD_TIME_DOMAIN_WALL_ON_AN_OPEN_INTERVAL_WHERE_THE_PARTNER_WEYL_MODE_LIVES_BOUNDED_THEOREM_NOTE_2026-09-03.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/NO_PER_SITE_CHIRALITY_THEOREM_NOTE_2026-05-02.md')
EXPECTED_INPUT_SHA256 = {'docs/THE_RECORD_TIME_DOMAIN_WALL_ON_AN_OPEN_INTERVAL_WHERE_THE_PARTNER_WEYL_MODE_LIVES_BOUNDED_THEOREM_NOTE_2026-09-03.md': 'ac911d59c9bfaa54a1553f102df533a2dc1cdaae42df316adc3c250471eb7c52', 'docs/MINIMAL_AXIOMS_2026-06-29.md': '93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753', 'docs/NO_PER_SITE_CHIRALITY_THEOREM_NOTE_2026-05-02.md': '03747906f5b5b63ae6e4c0d26f017893b95fc23c3df56974c595292f6d8706ef'}

def current_input_guard():
    root = Path(__file__).resolve().parents[1]
    errors = []
    if set(AUDIT_INPUT_PATHS) != set(EXPECTED_INPUT_SHA256):
        errors.append("declared semantic input set differs from pinned set")
    for rel in AUDIT_INPUT_PATHS:
        try:
            actual = hashlib.sha256((root / rel).read_bytes()).hexdigest()
        except OSError as exc:
            errors.append(rel + ": " + str(exc))
            continue
        print("INPUT_SHA " + rel + " " + actual)
        if actual != EXPECTED_INPUT_SHA256[rel]:
            errors.append(rel + ": current semantic input changed")
    if errors:
        print("FAIL G0 current source/input guard: " + "; ".join(errors))
        print("TOTAL: PASS=0 FAIL=1")
        raise SystemExit(1)
    print("SOURCE_INPUT_GUARD: exact current inputs; broader parent claims unaccepted")

current_input_guard()


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


# ===================================================== the four-component embedding

I2 = np.eye(2, dtype=complex)
S1 = np.array([[0, 1], [1, 0]], dtype=complex)
S2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
S3 = np.array([[1, 0], [0, -1]], dtype=complex)
SIG = [S1, S2, S3]
I4 = np.eye(4, dtype=complex)
G_SP = [np.kron(S1, s) for s in SIG]          # Gamma_i = tau_1 (x) sigma_i
G_S = np.kron(S2, I2)                          # Gamma_s = tau_2 (x) I
G_M = np.kron(S3, I2)                          # Gamma_m = tau_3 (x) I
CHI = 1j * G_S @ G_M                           # chi = -tau_1 (x) I

M_DEF = 0.8
R_S = 1.0
R_SPACE = 1.0


def nrm(a):
    return float(np.linalg.norm(a))


# =============================================== the supplied record-time coordinate

def record_time_ops(n_s, bc, end_mode="hard"):
    """SUPPLIED item 1/2/3/7: the ordered chain, K_s, r_s L_s, the end convention.

    bc       'periodic' (a circle) or 'open' (an interval)
    end_mode 'hard' -- Dirichlet completion, Laplacian diagonal held at 1.0 at
                       the two ends, as if a psi = 0 ghost site sat outside
             'free' -- Neumann, diagonal 0.5 at the ends, only existing links
    """
    k = np.zeros((n_s, n_s), dtype=complex)
    lap = np.zeros((n_s, n_s), dtype=complex)
    if bc == "periodic":
        for s in range(n_s):
            k[s, (s + 1) % n_s] += -0.5j
            k[s, (s - 1) % n_s] += 0.5j
            lap[s, s] += 1.0
            lap[s, (s + 1) % n_s] += -0.5
            lap[s, (s - 1) % n_s] += -0.5
        return k, lap
    for s in range(n_s - 1):
        k[s, s + 1] += -0.5j
        k[s + 1, s] += 0.5j
        lap[s, s] += 0.5
        lap[s + 1, s + 1] += 0.5
        lap[s, s + 1] += -0.5
        lap[s + 1, s] += -0.5
    if end_mode == "hard":
        lap[0, 0] += 0.5
        lap[n_s - 1, n_s - 1] += 0.5
    return k, lap


def hamiltonian(n_s, m, bc, end_mode="hard", p=(0.0, 0.0, 0.0)):
    """The five-dimensional Wilson-Dirac diagnostic at transverse momentum p."""
    k, lap = record_time_ops(n_s, bc, end_mode)
    w = R_SPACE * sum(1.0 - math.cos(x) for x in p)
    mass = np.diag(np.asarray(m, dtype=float) + w) + R_S * lap
    ham = np.kron(k, G_S) + np.kron(mass, G_M)
    for i, pi in enumerate(p):
        ham = ham + np.kron(np.eye(n_s, dtype=complex), math.sin(pi) * G_SP[i])
    return ham


def profile_periodic(n_s, mm=M_DEF):
    """The landed circle: m = -M outside [n/4, 3n/4), +M inside: one wall, one anti-wall."""
    w, aw = n_s // 4, n_s // 4 + n_s // 2
    m = -mm * np.ones(n_s)
    m[w:aw] = mm
    return m, w, aw


def profile_flip(n_s, mm=M_DEF, left=-1.0):
    m = left * mm * np.ones(n_s)
    m[n_s // 2:] = -left * mm
    return m


def dist(n_s, centre, bc):
    d = np.abs(np.arange(n_s) - centre)
    return np.minimum(d, n_s - d) if bc == "periodic" else d


# ============================================================== analysis primitives

def light_set(ev, cut):
    idx = np.where(np.abs(ev) < cut)[0]
    rest = np.abs(ev[np.abs(ev) >= cut])
    return idx, (float(rest.min()) if rest.size else float("inf"))


def chirality_density(evec, idx, n_s):
    """chi(s) = sum_{k in light} <psi_k| Pi_s chi |psi_k>, basis independent."""
    v = evec[:, idx].reshape(n_s, 4, -1)
    return np.einsum("scm,cd,sdm->s", v.conj(), CHI, v).real


def window_basis(ham, n_s, centre, bc, cut, width=2.0):
    """Diagonalize a Gaussian window of the named interface inside the light space."""
    ev, evec = np.linalg.eigh(ham)
    idx, _ = light_set(ev, cut)
    v = evec[:, idx]
    w = np.exp(-((dist(n_s, centre, bc) / width) ** 2))
    wv, wvec = np.linalg.eigh(v.conj().T @ np.kron(np.diag(w), I4) @ v)
    o = np.argsort(wv)[::-1]
    return wv[o], v @ wvec[:, o]


def mode_report(vec, n_s, bc):
    p = np.sum(np.abs(vec.reshape(n_s, 4)) ** 2, axis=1)
    p = p / p.sum()
    peak = int(np.argmax(p))
    xis = {}
    for side, step in (("L", -1), ("R", 1)):
        ds, ys = [], []
        for d in range(1, min(12, n_s // 2)):
            j = peak + step * d
            if bc == "periodic":
                j %= n_s
            elif not 0 <= j < n_s:
                break
            if p[j] < 1e-15:
                break
            ds.append(d)
            ys.append(math.log(p[j]))
        sl = np.polyfit(np.array(ds, float), np.array(ys), 1)[0] if len(ds) >= 4 else 0.0
        xis[side] = -2.0 / sl if sl < 0 else float("nan")
    return peak, float(np.sum(p ** 2)), xis["L"], xis["R"]


def weyl_data(u, n_s, rank=2):
    """Projected spatial velocities: Weyl cone, handedness Tr(V1V2V3)/2i, <chi>."""
    proj = u[:, :rank]
    big = np.eye(n_s, dtype=complex)
    vs = [proj.conj().T @ np.kron(big, g) @ proj for g in G_SP]
    sq = max(nrm(v @ v - np.eye(rank, dtype=complex)) for v in vs)
    ac = max(nrm(vs[i] @ vs[j] + vs[j] @ vs[i]) for i in range(3) for j in range(i + 1, 3))
    hand = float(np.real(np.trace(vs[0] @ vs[1] @ vs[2]) / 2j))
    chi = float(np.real(np.trace(proj.conj().T @ np.kron(big, CHI) @ proj)) / rank)
    return sq, ac, hand, chi


def interface_report(ham, n_s, centre, bc, cut=0.40):
    wv, u = window_basis(ham, n_s, centre, bc, cut)
    if wv.size < 2 or wv[1] < 0.05:
        return None
    peak, ipr, xil, xir = mode_report(u[:, 0], n_s, bc)
    sq, ac, hand, chi = weyl_data(u, n_s)
    return dict(top2=wv[:2], peak=peak, ipr=ipr, xiL=xil, xiR=xir,
                sq=sq, ac=ac, hand=hand, chi=chi)


# ================================================================== GROUP A -- T1

print("== A  T1  the historical periodic circle, N_s = 64, M = 0.8, r = r_s = 1")
NS = 64
M_PER, W_P, AW_P = profile_periodic(NS)
H_PER = hamiltonian(NS, M_PER, "periodic")
EV_P, EVEC_P = np.linalg.eigh(H_PER)
IDX_P, GAP_P = light_set(EV_P, 1e-5)
check("A1 [1e-6] wall s=%d, anti-wall s=%d: %d light states at p=0, max|E| %.3e, next gap %.6f "
      "(historical 0.801204)" % (W_P, AW_P, IDX_P.size, np.abs(EV_P[IDX_P]).max(), GAP_P),
      IDX_P.size == 4 and np.abs(EV_P[IDX_P]).max() < 1e-6 and abs(GAP_P - 0.801204) < 5e-7)

RW = interface_report(H_PER, NS, W_P, "periodic", cut=1e-5)
RA = interface_report(H_PER, NS, AW_P, "periodic", cut=1e-5)
check("A2 [1e-8] wall: window top-2 %.9f %.9f (historical 0.798565653), peak %d, xi_L %.6f, xi_R "
      "%.6f, <chi> %+.12f, handedness %+.0f"
      % (RW["top2"][0], RW["top2"][1], RW["peak"], RW["xiL"], RW["xiR"], RW["chi"], RW["hand"]),
      abs(RW["top2"][0] - 0.798565653) < 5e-9 and abs(RW["top2"][1] - 0.798565653) < 5e-9
      and RW["peak"] == 15 and abs(RW["xiL"] - 0.621335) < 5e-7
      and abs(RW["xiR"] - 1.701298) < 5e-7 and abs(RW["chi"] - 1.0) < 1e-9
      and abs(RW["hand"] + 1.0) < 1e-6 and RW["sq"] < 1e-13 and RW["ac"] < 1e-13)
check("A3 [1e-8] anti-wall: window top-2 %.9f %.9f (historical 0.880610823), peak %d, xi_L %.6f, "
      "xi_R %.6f, <chi> %+.12f, handedness %+.0f"
      % (RA["top2"][0], RA["top2"][1], RA["peak"], RA["xiL"], RA["xiR"], RA["chi"], RA["hand"]),
      abs(RA["top2"][0] - 0.880610823) < 5e-9 and abs(RA["top2"][1] - 0.880610823) < 5e-9
      and RA["peak"] == 48 and abs(RA["xiL"] - 1.701298) < 5e-7
      and abs(RA["xiR"] - 0.621335) < 5e-7 and abs(RA["chi"] + 1.0) < 1e-9
      and abs(RA["hand"] - 1.0) < 1e-6 and RA["sq"] < 1e-13 and RA["ac"] < 1e-13)

CNT_P = [int(np.sum(np.abs(np.linalg.eigvalsh(hamiltonian(NS, M_PER, "periodic", p=p))) < 1e-5))
         for p in itertools.product([0.0, math.pi], repeat=3)]
check("A4 [exact] light counts at the eight BZ corners %s: the species sits at the supplied p=0 "
      "corner alone" % (CNT_P,), CNT_P == [4, 0, 0, 0, 0, 0, 0, 0])

CD_P = chirality_density(EVEC_P, IDX_P, NS)
ZW = float(CD_P[W_P - 8:W_P + 8].sum())
ZA = float(CD_P[AW_P - 8:AW_P + 8].sum())
check("A5 [1e-10] chirality density %+.12f in the wall zone [%d,%d), %+.12f in the anti-wall "
      "zone, residual %.1e, net on the circle %+.12f"
      % (ZW, W_P - 8, W_P + 8, ZA, abs(float(CD_P.sum()) - ZW - ZA), float(CD_P.sum())),
      abs(ZW - 2.0) < 1e-4 and abs(ZA + 2.0) < 1e-4 and abs(float(CD_P.sum())) < 1e-10)

# ================================================================== GROUP B -- T2

print("== B  T2  the open record-time interval, N_s = 64, light cut |E| < 0.40")
CUT = 0.40
LAM, NPIN = 4.0, 4
GEO = {
    "open_hard_1wall": (profile_flip(NS), "open", "hard", {"left_end": 0, "wall": 32, "right_end": 63}),
    "open_free_1wall": (profile_flip(NS), "open", "free", {"left_end": 0, "wall": 32, "right_end": 63}),
    "open_hard_mirror": (profile_flip(NS, left=1.0), "open", "hard", {"left_end": 0, "wall": 32, "right_end": 63}),
    "open_uniform_topological": (-M_DEF * np.ones(NS), "open", "hard", {"left_end": 0, "right_end": 63}),
    "open_uniform_trivial": (M_DEF * np.ones(NS), "open", "hard", {"left_end": 0, "right_end": 63}),
}
_mp = profile_flip(NS).copy()
_mp[:NPIN] = LAM
_mp[-NPIN:] = LAM
GEO["open_pinned_ends"] = (_mp, "open", "hard",
                           {"left_end": 0, "pin_edge": NPIN, "wall": 32, "right_end": 63})

RES = {}
for key, (m, bc, em, ifaces) in GEO.items():
    ham = hamiltonian(NS, m, bc, em)
    ev, evec = np.linalg.eigh(ham)
    idx, gap = light_set(ev, CUT)
    cd = chirality_density(evec, idx, NS)
    cs = sorted(set(ifaces.values()))
    lab = {v: k for k, v in ifaces.items()}
    zone = {lab[c]: 0.0 for c in cs}
    for s in range(NS):
        zone[lab[min(cs, key=lambda c: abs(s - c))]] += cd[s]
    RES[key] = dict(n=idx.size, mx=float(np.abs(ev[idx]).max()) if idx.size else 0.0, gap=gap,
                    net=float(cd.sum()), zone=zone,
                    ifc={k: interface_report(ham, NS, c, bc, CUT) for k, c in ifaces.items()})

B1 = RES["open_hard_1wall"]
check("B1 [1e-12] one wall, hard ends: %d light states, max|E| %.2e -- below floating resolution, not exact zeros -- next "
      "|E| %.6f, net chirality %+.12f" % (B1["n"], B1["mx"], B1["gap"], B1["net"]),
      B1["n"] == 4 and B1["mx"] < 1e-14 and abs(B1["net"]) < 1e-12)
check("B2 [1e-8] the wall doublet (peak s=%d) has <chi> %+.9f, handedness %+.0f, xi_L %.4f, xi_R "
      "%.4f; the PARTNER doublet sits at the left end (peak s=%d, IPR %.4f), <chi> %+.9f, "
      "handedness %+.0f"
      % (B1["ifc"]["wall"]["peak"], B1["ifc"]["wall"]["chi"], B1["ifc"]["wall"]["hand"],
         B1["ifc"]["wall"]["xiL"], B1["ifc"]["wall"]["xiR"], B1["ifc"]["left_end"]["peak"],
         B1["ifc"]["left_end"]["ipr"], B1["ifc"]["left_end"]["chi"], B1["ifc"]["left_end"]["hand"]),
      abs(B1["ifc"]["wall"]["chi"] - 1.0) < 1e-8 and abs(B1["ifc"]["wall"]["hand"] + 1.0) < 1e-6
      and B1["ifc"]["wall"]["peak"] == 31 and abs(B1["ifc"]["left_end"]["chi"] + 1.0) < 1e-8
      and abs(B1["ifc"]["left_end"]["hand"] - 1.0) < 1e-6
      and B1["ifc"]["left_end"]["peak"] == 0 and abs(B1["ifc"]["left_end"]["ipr"] - 0.9231) < 5e-5)
check("B3 [1e-6] the right end is EMPTY (no rank-2 light doublet): zone chirality %+.9f left end, "
      "%+.9f wall, %+.9f right end"
      % (B1["zone"]["left_end"], B1["zone"]["wall"], B1["zone"]["right_end"]),
      B1["ifc"]["right_end"] is None and abs(B1["zone"]["left_end"] + 2.0) < 1e-6
      and abs(B1["zone"]["wall"] - 2.0) < 1e-6 and abs(B1["zone"]["right_end"]) < 1e-6)

B2 = RES["open_free_1wall"]
check("B4 [1e-12] FREE (Neumann) ends give the IDENTICAL count: %d light states, max|E| %.2e, net "
      "%+.12f, partner still at s=%d, bound less tightly (IPR %.4f against %.4f)"
      % (B2["n"], B2["mx"], B2["net"], B2["ifc"]["left_end"]["peak"], B2["ifc"]["left_end"]["ipr"],
         B1["ifc"]["left_end"]["ipr"]),
      B2["n"] == 4 and B2["mx"] < 1e-14 and abs(B2["net"]) < 1e-12
      and B2["ifc"]["left_end"]["peak"] == 0 and abs(B2["ifc"]["left_end"]["chi"] + 1.0) < 1e-8
      and abs(B2["ifc"]["left_end"]["ipr"] - 0.8427) < 5e-5)

B3 = RES["open_hard_mirror"]
check("B5 [1e-8] a MIRRORED mass puts the partner on the other end: peak s=%d, IPR %.4f, <chi> "
      "%+.9f, zone %+.9f against the wall's %+.9f -- the hosting end is fixed by the profile, not "
      "by the end convention"
      % (B3["ifc"]["right_end"]["peak"], B3["ifc"]["right_end"]["ipr"], B3["ifc"]["right_end"]["chi"],
         B3["zone"]["right_end"], B3["zone"]["wall"]),
      B3["n"] == 4 and B3["ifc"]["right_end"]["peak"] == 63
      and abs(B3["ifc"]["right_end"]["chi"] - 1.0) < 1e-8
      and abs(B3["ifc"]["right_end"]["ipr"] - 0.9231) < 5e-5
      and abs(B3["zone"]["right_end"] - 2.0) < 1e-6 and abs(B3["net"]) < 1e-12)

B6 = RES["open_pinned_ends"]
check("B6 [1e-8] pinning the Wilson mass to the TRIVIAL sign (m=+%.1f) on the %d end sites leaves "
      "the partner in the spectrum at s=%d, the inner edge of the pinned region: IPR %.4f, <chi> "
      "%+.9f, zone %+.9f, net %+.12f"
      % (LAM, NPIN, B6["ifc"]["pin_edge"]["peak"], B6["ifc"]["pin_edge"]["ipr"],
         B6["ifc"]["pin_edge"]["chi"], B6["zone"]["pin_edge"], B6["net"]),
      B6["n"] == 4 and B6["ifc"]["pin_edge"]["peak"] == NPIN
      and abs(B6["ifc"]["pin_edge"]["chi"] + 1.0) < 1e-8
      and abs(B6["ifc"]["pin_edge"]["ipr"] - 0.8548) < 5e-5
      and abs(B6["zone"]["pin_edge"] + 1.9969) < 5e-4 and abs(B6["net"]) < 1e-12)

B4 = RES["open_uniform_topological"]
B5 = RES["open_uniform_trivial"]
check("B7 [1e-12] a UNIFORM topological mass with NO WALL gives the same pair on the two "
      "boundaries: %d light states, max|E| %.2e, <chi> %+.9f at s=%d and %+.9f at s=%d, net "
      "%+.12f -- the wall is sufficient for localisation, not necessary"
      % (B4["n"], B4["mx"], B4["ifc"]["left_end"]["chi"], B4["ifc"]["left_end"]["peak"],
         B4["ifc"]["right_end"]["chi"], B4["ifc"]["right_end"]["peak"], B4["net"]),
      B4["n"] == 4 and B4["mx"] < 1e-14 and abs(B4["ifc"]["left_end"]["chi"] + 1.0) < 1e-8
      and abs(B4["ifc"]["right_end"]["chi"] - 1.0) < 1e-8 and abs(B4["net"]) < 1e-12)
check("B8 [exact] a UNIFORM trivial mass gives %d light states (next |E| %.6f): the light "
      "chirality is an interface effect, not a bulk mode" % (B5["n"], B5["gap"]), B5["n"] == 0)

OKC, ROW = True, []
for f in (0.05, 0.10, 0.20):
    q = f * math.pi
    eo = float(np.sort(np.abs(np.linalg.eigvalsh(
        hamiltonian(NS, GEO["open_hard_1wall"][0], "open", "hard", (q, 0.0, 0.0)))))[0])
    ep = float(np.sort(np.abs(np.linalg.eigvalsh(hamiltonian(NS, M_PER, "periodic", p=(q, 0.0, 0.0)))))[0])
    ROW.append("%.2f %.8f %.8f %.8f" % (f, eo, ep, abs(math.sin(q))))
    OKC = OKC and abs(eo - abs(math.sin(q))) < 5e-9 and abs(ep - abs(math.sin(q))) < 5e-9
print("   q/pi, open |E|, circle |E|, |sin q|:  " + " | ".join(ROW))
check("B9 [5e-9] approximate finite Weyl dispersion: |E| agrees with |sin q| to eight decimals through "
      "q = 0.2 pi, identical on the interval and on the circle", OKC)

CNT_O = [int(np.sum(np.abs(np.linalg.eigvalsh(
    hamiltonian(NS, GEO["open_hard_1wall"][0], "open", "hard", p))) < CUT))
    for p in itertools.product([0.0, math.pi], repeat=3)]
CNT_U = [int(np.sum(np.abs(np.linalg.eigvalsh(
    hamiltonian(NS, GEO["open_uniform_topological"][0], "open", "hard", p))) < CUT))
    for p in itertools.product([0.0, math.pi], repeat=3)]
check("B10 [exact] BZ corner counts %s (open, one wall) and %s (open, uniform topological) agree "
      "with the circle's" % (CNT_O, CNT_U),
      CNT_O == [4, 0, 0, 0, 0, 0, 0, 0] and CNT_U == [4, 0, 0, 0, 0, 0, 0, 0])


# ------------------------------------------- finite flux-WINDOW sign-switch diagnostic, one flux quantum

FLUX_ORIENTATION_ERRORS = []

def covariant_xy(lx, ly):
    """Peierls phases for exactly one U(1) flux quantum through the x-y torus."""
    n = lx * ly
    b = 2.0 * math.pi / n
    kx = np.zeros((n, n), dtype=complex)
    ky = np.zeros((n, n), dtype=complex)
    lap = np.zeros((n, n), dtype=complex)
    ix = lambda x, y: (x % lx) * ly + (y % ly)
    for x in range(lx):
        for y in range(ly):
            i = ix(x, y)
            uy = np.exp(1j * b * x)
            ux = np.exp(-1j * b * lx * y) if x == lx - 1 else 1.0 + 0j
            for j, u, k in ((ix(x + 1, y), ux, kx), (ix(x, y + 1), uy, ky)):
                k[i, j] += -0.5j * u
                k[j, i] += 0.5j * np.conj(u)
                lap[i, i] += 0.5
                lap[j, j] += 0.5
                lap[i, j] += -0.5 * u
                lap[j, i] += -0.5 * np.conj(u)
    # Recover the actually constructed oriented links, not merely the scalar b.
    ux_link = lambda x,y: 2j*kx[ix(x,y),ix(x+1,y)]
    uy_link = lambda x,y: 2j*ky[ix(x,y),ix(x,y+1)]
    target = np.exp(2j*math.pi/(lx*ly))
    err = max(abs(ux_link(x,y)*uy_link(x+1,y)*np.conj(ux_link(x,y+1))
                  *np.conj(uy_link(x,y))-target) for x in range(lx) for y in range(ly))
    FLUX_ORIENTATION_ERRORS.append(float(err))
    return kx, ky, lap


def spectral_flow(m, bc, em, ifaces, ns=16, lx=3, ly=3, lz=7, steps=15,
                  twist=0.31, wcut=0.10, chicut=0.40, ecut=0.30):
    """Track window-selected labels through twist 0 -> 2 pi; not continuous eigenbranch spectral flow."""
    kx, ky, lapxy = covariant_xy(lx, ly)
    nxy = lx * ly
    ixy, isr = np.eye(nxy, dtype=complex), np.eye(ns, dtype=complex)
    big = np.eye(nxy * ns, dtype=complex)
    ks, lap = record_time_ops(ns, bc, em)
    base = (np.kron(np.kron(kx, isr), G_SP[0]) + np.kron(np.kron(ky, isr), G_SP[1])
            + np.kron(np.kron(ixy, ks), G_S)
            + np.kron(np.kron(lapxy, isr) + np.kron(ixy, np.diag(m) + lap), G_M))
    hzw, hzk, chop = np.kron(big, G_M), np.kron(big, G_SP[2]), np.kron(big, CHI)
    wins = {k: np.exp(-((dist(ns, c, bc) / 2.0) ** 2)) for k, c in ifaces.items()}
    flow = {k: 0 for k in wins}
    for zi in range(lz):
        prev = {k: None for k in wins}
        hist = {k: [] for k in wins}
        for phi in np.linspace(0.0, 2 * math.pi, steps):
            kz = float((2 * math.pi * (zi + twist) / lz - math.pi + phi / lz + math.pi)
                       % (2 * math.pi) - math.pi)
            ev, evec = np.linalg.eigh(base + (1 - math.cos(kz)) * hzw + math.sin(kz) * hzk)
            chis = np.einsum("ij,ij->j", evec.conj(), chop @ evec).real
            arr = evec.reshape(nxy, ns, 4, -1)
            for k, win in wins.items():
                w = np.sum(np.abs(arr) ** 2 * win[None, :, None, None], axis=(0, 1, 2)).real
                cand = np.where((w > wcut) & (np.abs(chis) > chicut))[0]
                score = w * np.abs(chis) / (1 + np.abs(ev))
                if cand.size == 0:
                    cand = np.argsort(score)[-12:]
                sc = (score[cand] if prev[k] is None
                      else np.abs(evec[:, cand].conj().T @ prev[k]) + 1e-3 * score[cand])
                i = int(cand[int(np.argmax(sc))])
                prev[k] = evec[:, i]
                hist[k].append(float(ev[i]))
        for k in wins:
            for j in range(steps - 1):
                e0, e1 = hist[k][j], hist[k][j + 1]
                if max(abs(e0), abs(e1)) >= ecut:
                    continue
                flow[k] += 1 if e0 < 0 < e1 else (-1 if e0 > 0 > e1 else 0)
    return flow


NSF = 16
FLOW = {}
for key, ifc in (("circle_2wall", {"wall": 4, "anti": 12}),
                 ("open_1wall", {"left_end": 0, "wall": 8, "right_end": 15}),
                 ("open_pinned", {"left_end": 0, "pin_edge": NPIN, "wall": 8, "right_end": 15}),
                 ("open_uniform_top", {"left_end": 0, "right_end": 15})):
    if key == "circle_2wall":
        mf, bcf, emf = profile_periodic(NSF)[0], "periodic", "hard"
    elif key == "open_uniform_top":
        mf, bcf, emf = -M_DEF * np.ones(NSF), "open", "hard"
    elif key == "open_pinned":
        mf = profile_flip(NSF).copy()
        mf[:NPIN] = LAM
        mf[-NPIN:] = LAM
        bcf, emf = "open", "hard"
    else:
        mf, bcf, emf = profile_flip(NSF), "open", "hard"
    FLOW[key] = spectral_flow(mf, bcf, emf, ifc)

EXPECTED_FLOW = {"circle_2wall": {"wall":1,"anti":-1},
                 "open_1wall": {"left_end":-1,"wall":1,"right_end":0},
                 "open_pinned": {"left_end":-1,"pin_edge":0,"wall":1,"right_end":0},
                 "open_uniform_top": {"left_end":-1,"right_end":1}}
FTXT = "; ".join("%s %s = %+d" % (k, " ".join("%s%+d" % (a, b) for a, b in v.items()), sum(v.values()))
                 for k, v in FLOW.items())
check("B11 [labelled integer diagnostic] finite flux-WINDOW switches for actual POSITIVE flux through x-y torus "
      "(L_x=L_y=3, N_s=16, L_z=7, 15 twist steps): %s -- +1 on the wall branch, -1 on its "
      "partner under these window labels only; avoided gap, no inflow theorem" % FTXT,
      FLOW == EXPECTED_FLOW and len(FLUX_ORIENTATION_ERRORS) == 4
      and max(FLUX_ORIENTATION_ERRORS) < 1e-12
      and all(sum(v.values()) == 0 and list(v.values()).count(1) == 1
          and list(v.values()).count(-1) == 1 and set(v.values()) <= {-1, 0, 1}
          for v in FLOW.values()))

# ================================================================== GROUP C -- T3

print("== C  T3  the counting rule on a DECLARED family: complete enumeration, no randomness")
GRID = (8, 16, 24)
ALPHA = (-3.0, -1.5, -0.5, 0.5, 1.5, 3.0)
NSC = 32


def tau(m, r=R_S):
    """1D Wilson-Dirac band-inversion index: M(0) = m and M(pi) = m + 2r of opposite sign."""
    return 1 if -2.0 * r < m < 0.0 else 0


def family():
    """Every piecewise-constant profile with breakpoints on GRID, adjacent values distinct."""
    for kk in range(4):
        for cuts in itertools.combinations(GRID, kk):
            for vals in itertools.product(ALPHA, repeat=kk + 1):
                if any(a == b for a, b in zip(vals, vals[1:])):
                    continue
                yield cuts, vals


PROFILES = list(family())
BY_K = [sum(1 for c, _ in PROFILES if len(c) == j) for j in range(4)]
check("C1 [exact] the declared family is the COMPLETE ENUMERATION of piecewise-constant profiles "
      "on N_s=32 with breakpoints on the coarse grid %s, adjacent segment values distinct, from "
      "the alphabet %s: %d profiles, %s by transition count, each on the open interval and on the "
      "circle -- %d members, no randomness and no seed anywhere"
      % (GRID, ALPHA, len(PROFILES), BY_K, 2 * len(PROFILES)),
      len(PROFILES) == 1296 and BY_K == [6, 90, 450, 750])

WORST = 0.0
MISM = []
COUNTS = {"open": 0, "periodic": 0}
# Independent full declared Cartesian family, then bind completed solver keys.
EXPECTED_KEYS = {(bc,cuts,vals) for k in range(4) for cuts in itertools.combinations((8,16,24),k)
                 for vals in itertools.product((-3.,-1.5,-.5,.5,1.5,3.),repeat=k+1)
                 if all(a!=b for a,b in zip(vals,vals[1:])) for bc in ("open","periodic")}
EXECUTED_KEYS = set()
DUPLICATE_KEYS = 0
for cuts, vals in PROFILES:
    edges = (0,) + cuts + (NSC,)
    m = np.empty(NSC)
    for j in range(len(vals)):
        m[edges[j]:edges[j + 1]] = vals[j]
    taus = [tau(v) for v in vals]
    for bc in ("open", "periodic"):
        seq = [0] + taus + [0] if bc == "open" else taus + [taus[0]]
        pred = 2 * sum(1 for a, b in zip(seq, seq[1:]) if a != b)
        ev, evec = np.linalg.eigh(hamiltonian(NSC, m, bc, "hard"))
        idx, gap = light_set(ev, 0.25)
        net = float(chirality_density(evec, idx, NSC).sum())
        WORST = max(WORST, abs(net))
        COUNTS[bc] += 1
        executed_key=(bc,cuts,vals)
        DUPLICATE_KEYS += int(executed_key in EXECUTED_KEYS)
        EXECUTED_KEYS.add(executed_key)
        if idx.size != pred:
            MISM.append((bc, cuts, vals, pred, int(idx.size), gap))

check("C2 [cutoff/count] on each EXECUTED member the number of |E|<.25 states is TWICE the tau-"
      "transition count of the sequence bracketed by the trivial vacuum ([0, tau_1..tau_k, 0] "
      "open, cyclic on the circle): %d open and %d periodic members, MISMATCHES = %d"
      % (COUNTS["open"], COUNTS["periodic"], len(MISM)), not MISM
      and COUNTS == {"open":1296,"periodic":1296} and DUPLICATE_KEYS == 0
      and len(EXPECTED_KEYS)==2592 and EXECUTED_KEYS == EXPECTED_KEYS)
for row in MISM[:4]:
    print("   MISMATCH bc=%s cuts=%s vals=%s predicted=%d found=%d next|E|=%.4f" % row)
check("C3 [1e-14] net chirality is zero on EVERY member: worst |net| %.3e over all %d members"
      % (WORST, len(EXECUTED_KEYS)), WORST < 1e-14 and EXECUTED_KEYS==EXPECTED_KEYS
      and COUNTS == {"open":1296,"periodic":1296} and DUPLICATE_KEYS==0)

OKW, ROW = True, []
for m0 in (-3.0, -2.5, -1.5, -1.0, -0.5, 0.5, 1.5, 3.0):
    ev, evec = np.linalg.eigh(hamiltonian(48, m0 * np.ones(48), "open", "hard"))
    idx, gap = light_set(ev, 0.30)
    net = float(chirality_density(evec, idx, 48).sum())
    ROW.append("%+.1f/%d/%d" % (m0, tau(m0), idx.size))
    OKW = OKW and idx.size == 4 * tau(m0) and abs(net) < 1e-13
print("   uniform open slab N_s=48, m/tau/n_light:  " + "  ".join(ROW))
check("C4 [eight finite samples] bulk interval -2 r_s < m < 0 compared at eight declared masses: "
      "four |E|<.30 states at the three tested inside masses, zero at five tested outside; no complete finite interval theorem",
      OKW)

# ================================================================== GROUP D -- T4

print("== D  T4  how unpaired the wall's species is")
NSD = 128
MD = -M_DEF * np.ones(NSD)
MD[NSD // 2:] = M_DEF
EVD, EVECD = np.linalg.eigh(hamiltonian(NSD, MD, "open", "hard"))
IDXD, _ = light_set(EVD, 0.30)
CDD = chirality_density(EVECD, IDXD, NSD)
DEF = {w: 2.0 - float(CDD[NSD // 2 - w:NSD // 2 + w].sum()) for w in (2, 4, 8, 16, 24, 32)}
print("   half-width W, deficit of the window chirality from +2:  " +
      "  ".join("%d %.3e" % (w, d) for w, d in DEF.items()))
check("D1 [1e-14] the wall's local chirality inside a half-width-32 window is +2 to %.1e "
      "(N_s=128), against %.2e at W=8 and %.2e at W=16: a finite local-window deficit, "
      "balanced globally in this finite model" % (abs(DEF[32]), abs(DEF[8]), abs(DEF[16])),
      abs(DEF[32]) < 1e-14 and abs(DEF[24]) < 1e-12 and abs(DEF[16]) < 1e-8
      and abs(DEF[8]) > 1e-6 and abs(float(CDD.sum())) < 1e-12)

SPL = []
for n in (16, 24, 32, 48, 64):
    mm = -M_DEF * np.ones(n)
    mm[n // 2:] = M_DEF
    ep = np.linalg.eigvalsh(hamiltonian(n, profile_periodic(n)[0], "periodic"))
    eo = np.linalg.eigvalsh(hamiltonian(n, mm, "open", "hard"))
    SPL.append((n, float(np.abs(ep[light_set(ep, 0.40)[0]]).max()),
                float(np.abs(eo[light_set(eo, 0.40)[0]]).max())))
print("   L_5, circle max|E_light|, interval max|E_light|:  " + "  ".join("%d %.2e %.2e" % r for r in SPL))
check("D2 [monotone finite data] the light levels decrease above numerical floor on both geometries, "
      "and the interval values fall faster at sampled sizes, consistent with the short-"
      "xi side (xi_L %.6f against xi_R %.6f) -- reaching numerical floor by L_5 = 48, not exact zero"
      % (RW["xiL"], RW["xiR"]),
      all(SPL[i][1] > SPL[i + 1][1] for i in range(len(SPL) - 1))
      and all(SPL[i][2] > SPL[i + 1][2] for i in range(len(SPL) - 1) if SPL[i][2] > 1e-13)
      and SPL[-1][2] < 1e-14)

# ================================================================== GROUP E -- T5

print("== E  T5  a nonindependent supplied-data inventory; actual withdrawal domains")
SUPPLIED = ("an ordered coordinate s with nearest-neighbour adjacency", "K_s", "r_s L_s",
            "Gamma_s", "m(s), not necessarily sign-changing", "a chosen finite L_5", "a boundary condition")
K64, L64 = record_time_ops(NS, "open", "hard")
H_REBUILT = np.kron(K64, G_S) + np.kron(np.diag(profile_flip(NS)) + R_S * L64, G_M)
RESID = nrm(H_REBUILT - hamiltonian(NS, profile_flip(NS), "open", "hard"))
check("E1 [exact reconstruction] a nonindependent supplied-data inventory -- %s -- and "
      "rebuilt from them alone it reproduces group B's open one-wall operator at residual %.1e"
      % ("; ".join(SUPPLIED), RESID), RESID == 0.0)

DROP = (nrm(np.kron(K64, G_S)), nrm(np.kron(R_S * L64, G_M)), nrm(np.kron(K64, G_S)),
        nrm(np.kron(np.diag(profile_flip(NS)), G_M)))
check("E2 [full-operator norms] removing K_s, r_s L_s, the coupled Gamma_s term, or m(s) changes the operator "
      "by %s" % ", ".join("%.3f" % v for v in DROP), all(v > 1e-9 for v in DROP))

ZEROS = [p for p in itertools.product([0.0, math.pi], repeat=3)
         if nrm(sum(math.sin(x) * SIG[i] for i, x in enumerate(p))) < 1e-12]
WIND = [int(np.sign(math.prod(math.cos(x) for x in p))) for p in ZEROS]
check("E3 [separate comparator] additionally remove spatial Wilson data and halve the embedding to obtain the naive spatial "
      "operator D(p) = i sum_i sigma_i sin(p_i): %d zeros on the Brillouin torus, winding signs "
      "%d positive and %d negative, net %+d.  Record / Fixed Reality reads \"A site never carries "
      "more than one record; records are permanent\", so the per-site record set is EMPTY OR SINGLETON "
      "and record time is a supplied extra dimension, not a re-reading of a per-site stack; the "
      "axiom memo's Open Gates list puts \"arrow, record-production dynamics, physical persistence "
      "dynamics, time metric, and local observability of records\" outside axiom content"
      % (len(ZEROS), WIND.count(1), WIND.count(-1), sum(WIND)),
      len(ZEROS) == 8 and sum(WIND) == 0 and WIND.count(1) == 4)

EPS = np.array([(-1.0) ** (x + y + z) for x in range(8) for y in range(8)
                for z in range(8)]).reshape(8, 8, 8)
FAULT = float(np.abs(EPS[1:, :, :] + EPS[:-1, :, :]).max())
MSTAG = np.where(np.arange(8)[:, None, None] < 4, 1.0, -1.0) * EPS
check("E4 [exact diagonal comparison] the companion spatial-wall model is DIFFERENT, with no common physical "
      "no-go inferred: there eps_{v+e_x} = -eps_v at residual %.1f, so a supplied sign flip is a one-"
      "site translation of the alternating pattern and min|m(x)| = %.1f -- no plane carries a "
      "vanishing mass -- while here tau steps %d -> %d across the wall and the light states are "
      "finite low levels, not generic exact zeros" % (FAULT, float(np.abs(MSTAG).min()), tau(-M_DEF), tau(M_DEF)),
      FAULT == 0.0 and float(np.abs(MSTAG).min()) == 1.0 and tau(-M_DEF) == 1 and tau(M_DEF) == 0)


# Finite correction witnesses, independent of below-resolution eigenvalue labels.
def bidiagonal_inverse_bounds(diag):
    """For lower bidiagonal B (subdiagonal -1), 1/||B^-1||F <= sigma_min
    <= 1/max_j ||B^-1 e_j||. Decimal arithmetic avoids loss of tiny values.
    """
    with localcontext() as ctx:
        ctx.prec=80
        cols=[]
        for j in range(len(diag)):
            v=Decimal(1);norm2=Decimal(0)
            for i in range(j,len(diag)):
                v=v/diag[i]
                norm2+=v*v
            cols.append(norm2)
        return +(Decimal(1)/sum(cols).sqrt()), +(Decimal(1)/max(cols).sqrt())

DET_CONTROLS=[]
for name,mm,em in (("hard",profile_flip(64),"hard"),
                   ("free",profile_flip(64),"free"),
                   ("uniform",-M_DEF*np.ones(64),"hard")):
    k,lap=record_time_ops(64,"open",em)
    B=np.diag(mm)+lap+1j*k
    d=np.diag(B).real
    expected=np.diag(d)-np.diag(np.ones(63),-1)
    exact_det=math.prod(Fraction(float(x)) for x in d)
    ut=np.array([[1.,1.],[1.,-1.]])/np.sqrt(2)
    rot=np.kron(np.eye(64),np.kron(ut,np.eye(2)))
    hh=rot.conj().T@hamiltonian(64,mm,"open",em)@rot
    up=np.array([4*i+j for i in range(64) for j in (0,1)]); dn=up+2
    block_error=float(np.abs(hh[np.ix_(up,dn)]-np.kron(B,np.eye(2))).max())
    diagonal_error=max(float(np.abs(hh[np.ix_(up,up)]).max()),float(np.abs(hh[np.ix_(dn,dn)]).max()))
    intended=[Decimal(1)+(-Decimal(4)/5 if x<0 else Decimal(4)/5) for x in mm]
    if em=="free":intended[0]-=Decimal('.5');intended[-1]-=Decimal('.5')
    low,high=bidiagonal_inverse_bounds(intended)
    DET_CONTROLS.append((name,max(float(np.abs(B-expected).max()),block_error,diagonal_error),str(exact_det),str(low),str(high)))
check("F1 [exact determinant/Decimal bounds] declared finite hard/free bidiagonal diagonals are nonzero; intended rational splitting has positive inverse-norm bounds below 1e-20, not exact zero",
      all(err<1e-13 and Fraction(det)!=0 and Decimal(0)<Decimal(lo)<=Decimal(hi)<Decimal('1e-20')
          for name,err,det,lo,hi in DET_CONTROLS))

# Same Ns16 open-one-wall +flux construction as the original window diagnostic.
kx,ky,lp=covariant_xy(3,3); ks,ls=record_time_ops(16,"open","hard")
i9=np.eye(9); i16=np.eye(16); big=np.eye(144)
fb=(np.kron(np.kron(kx,i16),G_SP[0])+np.kron(np.kron(ky,i16),G_SP[1])
    +np.kron(np.kron(i9,ks),G_S)
    +np.kron(np.kron(lp,i16)+np.kron(i9,np.diag(profile_flip(16))+ls),G_M))
gm=np.kron(big,G_M); gz=np.kron(big,G_SP[2])
FLUX_ENDPOINT_GAPS=[float(np.abs(np.linalg.eigvalsh(fb+z*gm)).min()) for z in (0.,2.)]
fk=fb+(1-np.cos(.19))*gm+np.sin(.19)*gz
fsq=float(np.abs(fk@fk-(fb+(1-np.cos(.19))*gm)@(fb+(1-np.cos(.19))*gm)-np.sin(.19)**2*np.eye(576)).max())
check("F2 [actual finite flux matrices] square identity and positive endpoint gaps .00407991368,1.60326484 exclude continuous zero crossings; window switches span an AVOIDED gap",
      fsq<1e-12 and max(abs(a-b) for a,b in zip(FLUX_ENDPOINT_GAPS,(.00407991368,1.60326484)))<1e-8
      and max(FLUX_ORIENTATION_ERRORS)<1e-12)

NEAR_WINDOW=[]
for mass in (-2.01,-1.99,-.01,.01):
    ev=np.linalg.eigvalsh(hamiltonian(48,mass*np.ones(48),"open","hard"))
    NEAR_WINDOW.append((mass,tau(mass),int((np.abs(ev)<.30).sum())))
check("F3 [finite cutoff counterexamples] all four near-boundary Ns48 fixtures have 20 |E|<.30 states on BOTH sides of bulk window",
      [x[1] for x in NEAR_WINDOW]==[0,1,1,0] and [x[2] for x in NEAR_WINDOW]==[20]*4)

p0=(.4,.2,.1)
remaining=sum(np.sin(x)*G_SP[i] for i,x in enumerate(p0))+sum(1-np.cos(x) for x in p0)*G_M
full_delta=hamiltonian(4,profile_flip(4),"open","hard",p0)-hamiltonian(4,profile_flip(4),"open","hard")
naive=sum(np.sin(x)*SIG[i] for i,x in enumerate(p0))
WITHDRAWAL=(np.linalg.eigvalsh(remaining),np.linalg.eigvalsh(naive))
check("F4 [actual withdrawal] remaining4x4 spatial Wilson block differs from separate naive2x2; full removed Gamma_s term norm equals K term, not ||Gamma_s||=2",
      np.max(np.abs(full_delta-np.kron(np.eye(4),remaining)))<1e-13
      and abs(WITHDRAWAL[0][-1]-.460294987413)<1e-12
      and abs(WITHDRAWAL[1][-1]-.448422634804)<1e-12
      and abs(DROP[2]-DROP[0])<1e-13 and DROP[2]>10)
print("SUMMARY: supplied finite boundary-localized low spaces, balanced chiral pairing, full finite cutoff census and signed window diagnostics across an avoided gap. No exact generic finite zero, anomaly inflow, independent-wall count or physical Record-time/readout supplier.")
print("TOTAL: PASS=%d FAIL=%d" % (PASS, FAIL))
sys.exit(0 if FAIL == 0 else 1)
