#!/usr/bin/env python3
"""L3c core -- tick model: record formation interleaved with pre-record hopping dynamics.

Reuses the verified BKSF encoding of L3/L3b on the 2x2x2 cube (8 corners, 12 edge
sites, 12 qubits, dim 4096).  Everything here lives inside the N=2 record sector,
which is the 896-dimensional span of the |z> whose corner-parity pattern has weight 2.
That sector is exactly invariant under every hop term, so no dense object above
896 x 896 is ever formed (the one 4096-sized object is the state vector itself,
which we index by the 896 sector positions).
"""
import sys, itertools, time
import numpy as np

sys.path.insert(0, "/private/tmp/claude-501/-Users-jonreilly/c26e73d8-5c00-4f5e-8060-c64e52ce77bc/scratchpad/L3")
from l3_core import (cube_cluster, cube_faces, Enc, audit, code_space,
                     sector_matrix, fermi_sector, gauge_match, P, ID, PH, pc, pact)

T0 = time.time()

# ------------------------------------------------------------------ encoding
V, EDG = cube_cluster()
FAC = cube_faces()
En = Enc(V, sorted(EDG), FAC, "cube")
AUD = audit(En)
assert all(AUD[k] for k in ("R0_welldef", "R0_antisym", "R1", "R2", "R3", "R4", "grp_ok"))
KSTAB = AUD["k"]                      # 5 independent face stabilizers
CID, PHI, REPS, RECS = code_space(En, AUD)
D = En.DIM                            # 4096
NQ = En.NQ                            # 12 edge sites
assert D == 4096 and NQ == 12 and KSTAB == 5

# ------------------------------------------------------------------ N=2 record sector
_recz = np.array([En.record(z) for z in range(D)], dtype=np.int8)   # 4096 x 8 corner parities
_wt = _recz.sum(1)
ZL = np.flatnonzero(_wt == 2).astype(np.int64)     # the 896 patterns carrying two registered fermions
NZ = len(ZL)
assert NZ == 28 * 32 == 896
POS = -np.ones(D, dtype=np.int64)
POS[ZL] = np.arange(NZ)

PAIRS = [(i, j) for i in range(8) for j in range(i + 1, 8)]          # the 28-pattern dictionary
PIDX = {p: i for i, p in enumerate(PAIRS)}
PATZ = np.array([PIDX[tuple(np.flatnonzero(_recz[z]))] for z in ZL], dtype=np.int64)

# ------------------------------------------------------------------ hop terms on the sector
_hp = {e: En.hop_pauli(*e) for e in En.EDGES}
TGT = np.zeros((NQ, NZ), dtype=np.int64)
AMP = np.zeros((NQ, NZ), dtype=np.complex128)
for q, e in enumerate(En.EDGES):
    P1, P2 = _hp[e]
    for a in range(NZ):
        z = int(ZL[a])
        zz, amp = En.hop_amp(P1, P2, z)
        if amp == 0:
            TGT[q, a] = -1
        else:
            assert zz == z ^ (1 << q)
            assert POS[zz] >= 0
            TGT[q, a] = POS[zz]
            AMP[q, a] = amp

# H = sum_edges T_e  (the L3b sign convention: this IS the encoded hopping H, ground energy -4)
H896 = np.zeros((NZ, NZ), dtype=np.complex128)
for q in range(NQ):
    m = AMP[q] != 0
    H896[TGT[q][m], np.flatnonzero(m)] += AMP[q][m]
assert np.max(np.abs(H896 - H896.conj().T)) < 1e-12
EV896, VC896 = np.linalg.eigh(H896)
# the 896-dim sector is 32 flux (syndrome) copies of the 28-dim code sector; the code
# sector (zero flux) carries the -4 ground level, other flux sectors go lower.
assert abs(EV896[0] + 2.0 + 2.0*np.sqrt(2.0)) < 1e-9, EV896[0]

FREEQ = [np.array([q for q in range(NQ) if not (mask >> q) & 1], dtype=np.int64)
         for mask in range(1 << NQ)]
FULLMASK = (1 << NQ) - 1
_LOC = -np.ones(NZ, dtype=np.int64)


# ------------------------------------------------------------------ initial states
def _sector_gauge():
    sel, posc, Hoff, bond, ss, sd = sector_matrix(En, AUD, CID, PHI, REPS, RECS, lambda r: sum(r) == 2)
    pats = [RECS[c] for c in sel]
    idx, T, Dg = fermi_sector(En.EDGES, pats)
    assert all(idx[p] == posc[sel[a]] for a, p in enumerate(pats))
    d, msg = gauge_match(Hoff, T)
    assert msg == "ok"
    return sel, posc, pats, np.round(T).astype(np.int64), d


SEL, POSC, PATS28, TFERM, GAUGE = _sector_gauge()
# coset order in SEL -> pattern index in PAIRS
SELPAT = np.array([PIDX[tuple(i for i, b in enumerate(p) if b)] for p in PATS28], dtype=np.int64)


def _chi(s, u):
    return -1 if pc(s & u) % 2 else 1


def slater(s, t):
    w = np.zeros(len(PATS28), dtype=np.int64)
    for a, p in enumerate(PATS28):
        u, x = [i for i, b in enumerate(p) if b]
        w[a] = _chi(s, u) * _chi(t, x) - _chi(s, x) * _chi(t, u)
    return w


def state_from_coset_amps(amps):
    """amps: dict coset-id -> complex.  Returns the normalised 896-vector on the sector."""
    v = np.zeros(NZ, dtype=np.complex128)
    for a in range(NZ):
        z = int(ZL[a])
        c = CID[z]
        A = amps.get(c, 0.0)
        if A:
            v[a] = A * PHI[z]
    n = np.linalg.norm(v)
    assert n > 1e-12
    return v / n


def st_ground():
    w = slater(0, 4)
    return state_from_coset_amps({SEL[a]: complex(w[a]) * GAUGE[a] for a in range(len(SEL)) if w[a]})


def st_pair(v0=0, v1=1):
    rec = tuple(1 if u in (v0, v1) else 0 for u in range(V))
    c = [c for c in range(len(REPS)) if RECS[c] == rec][0]
    return state_from_coset_amps({c: 1.0})


def st_uniform():
    return state_from_coset_amps({SEL[a]: GAUGE[a] for a in range(len(SEL))})


PSI0 = {"ground": st_ground(), "pair01": st_pair(0, 1), "unif28": st_uniform()}
assert np.max(np.abs(H896 @ PSI0["ground"] + 4.0 * PSI0["ground"])) < 1e-9


# ------------------------------------------------------------------ pattern statistics
def born_patterns(psi):
    """Odds over the 28-pattern dictionary carried by a sector state."""
    return np.bincount(PATZ, weights=np.abs(psi) ** 2, minlength=28)


def dephased_patterns(psi):
    """Exact diagonal, in the 28-pattern dictionary, of  sum_E P_E |psi><psi| P_E."""
    c = np.conj(VC896.T @ np.conj(psi))
    grp = np.cumsum(np.concatenate(([0], (np.diff(EV896) > 1e-8).astype(np.int64))))
    out = np.zeros(28)
    for g in range(grp[-1] + 1):
        sl = grp == g
        x = VC896[:, sl] @ c[sl]
        out += np.bincount(PATZ, weights=np.abs(x) ** 2, minlength=28)
    return out


UNIF28 = np.full(28, 1.0 / 28.0)
GS_BORN = born_patterns(PSI0["ground"])
ZERO12 = np.flatnonzero(GS_BORN < 1e-12)          # the discriminator's forbidden corner pairs
assert len(ZERO12) == 12


# ------------------------------------------------------------------ conditioned blocks
CACHE = {}
CACHE_LEVEL = 3          # cache the eigendecomposition for |R| <= this (memory bound)


def get_block(Rmask, wbits):
    """(I, eigenvalues, eigenvectors, degeneracy labels) for H_R restricted to
    {z in the N=2 sector : z|_R = wbits}.  H_R = sum of hop terms on unrecorded sites."""
    key = (Rmask, wbits)
    v = CACHE.get(key)
    if v is not None:
        return v
    I = np.flatnonzero((ZL & Rmask) == wbits)
    d = len(I)
    if d == 0:
        raise RuntimeError("empty block")
    if d == 1:
        res = (I, np.zeros(1), np.ones((1, 1), dtype=np.complex128), np.zeros(1, dtype=np.int64))
    else:
        _LOC[I] = np.arange(d)
        Hb = np.zeros((d, d), dtype=np.complex128)
        cols = np.arange(d)
        for q in FREEQ[Rmask]:
            a = AMP[q][I]
            m = a != 0
            if not m.any():
                continue
            Hb[_LOC[TGT[q][I][m]], cols[m]] = a[m]
        _LOC[I] = -1
        Ev, Vc = np.linalg.eigh(Hb)
        grp = np.cumsum(np.concatenate(([0], (np.diff(Ev) > 1e-9).astype(np.int64))))
        res = (I, Ev, Vc, grp)
    if bin(Rmask).count("1") <= CACHE_LEVEL:
        CACHE[key] = res
    return res


def evolve(psi, Ev, Vc, t):
    if psi.shape[0] == 1:
        return psi
    c = np.conj(Vc.T @ np.conj(psi))
    return Vc @ (np.exp(-1j * t * Ev) * c)


def dephase(psi, Vc, grp, rng):
    """One draw of the unravelling whose average is  sum_E P_E rho P_E  (the t -> infinity limit)."""
    if psi.shape[0] == 1:
        return psi
    c = np.conj(Vc.T @ np.conj(psi))
    ph = np.exp(2j * np.pi * rng.random(int(grp[-1]) + 1))
    return Vc @ (ph[grp] * c)


def form_records(psi, I, sites, rng):
    """Sequential Lueders conditioning on the given sites (Z's commute, so the order
    inside the group does not matter).  Returns (locked bits, restricted index set)."""
    zI = ZL[I]
    Smask = 0
    for q in sites:
        Smask |= (1 << q)
    pr = np.abs(psi) ** 2
    if len(sites) == 1:
        q = sites[0]
        b = ((zI >> q) & 1).astype(np.int64)
        p1 = pr[b == 1].sum()
        val = (1 << q) if rng.random() * pr.sum() < p1 else 0
    else:
        keys = zI & Smask
        uk, inv = np.unique(keys, return_inverse=True)
        w = np.bincount(inv, weights=pr)
        w = w / w.sum()
        val = int(uk[np.searchsorted(np.cumsum(w), rng.random(), side="right").clip(0, len(uk) - 1)])
    return Smask, val


def l1(a, b):
    return float(np.abs(np.asarray(a) - np.asarray(b)).sum())
