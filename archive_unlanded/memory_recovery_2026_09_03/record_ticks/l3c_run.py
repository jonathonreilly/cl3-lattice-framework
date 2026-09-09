#!/usr/bin/env python3
"""L3c -- the tick model.  Monte Carlo over record-formation schedules and record values."""
import sys, time, itertools
import numpy as np
import l3c_core as C

FULL = C.FULLMASK
IC = {}


def get_I(Rmask, wbits):
    key = (Rmask, wbits)
    v = IC.get(key)
    if v is None:
        v = np.flatnonzero((C.ZL & Rmask) == wbits)
        if len(IC) < 400000:
            IC[key] = v
    return v


# ---------------------------------------------------------------- one trajectory
def traj_drop(psi0, Tsite, tau, rng):
    """Model choice A: after a record forms at site e, the hop term on e is dropped.
    H_R = sum of hop terms on unrecorded sites; it commutes with every recorded Z."""
    Rmask = 0
    wbits = 0
    I, Ev, Vc, grp = C.get_block(0, 0)
    psi = psi0
    prev = 1
    for tk in np.unique(Tsite):
        m = int(tk) - prev
        if m > 0:
            psi = C.evolve(psi, Ev, Vc, m * tau)
        sites = np.flatnonzero(Tsite == tk)
        Smask, val = C.form_records(psi, I, sites, rng)
        Rmask |= Smask
        wbits |= val
        I2, Ev, Vc, grp = C.get_block(Rmask, wbits)
        psi = psi[np.searchsorted(I, I2)]
        psi = psi / np.linalg.norm(psi)
        I = I2
        prev = int(tk)
    assert len(I) == 1
    return C.PATZ[I[0]]


def traj_proj(psi0, Tsite, Uf, rng):
    """Model choice B: keep the full H each tick and re-condition on the already
    registered values after every step."""
    Rmask = 0
    wbits = 0
    I = get_I(0, 0)
    psi = psi0
    prev = 1
    for tk in np.unique(Tsite):
        m = int(tk) - prev
        if m > 0 and len(I) > 1:
            M = Uf[np.ix_(I, I)]
            for _ in range(m):
                psi = M @ psi
                n = np.linalg.norm(psi)
                if n < 1e-13:
                    return -1
                psi = psi / n
        sites = np.flatnonzero(Tsite == tk)
        Smask, val = C.form_records(psi, I, sites, rng)
        Rmask |= Smask
        wbits |= val
        I2 = get_I(Rmask, wbits)
        psi = psi[np.searchsorted(I, I2)]
        psi = psi / np.linalg.norm(psi)
        I = I2
        prev = int(tk)
    assert len(I) == 1
    return C.PATZ[I[0]]


def traj_deph(psi0, rng):
    """The exact slow-formation limit p -> 0 at fixed tau: the gap before each record
    diverges, so the pre-record state is fully dephased in the H_R energy basis, and
    records form one at a time in a uniformly random site order."""
    Rmask = 0
    wbits = 0
    I, Ev, Vc, grp = C.get_block(0, 0)
    psi = psi0
    for q in rng.permutation(12):
        psi = C.dephase(psi, Vc, grp, rng)
        Smask, val = C.form_records(psi, I, [int(q)], rng)
        Rmask |= Smask
        wbits |= val
        I2, Ev, Vc, grp = C.get_block(Rmask, wbits)
        psi = psi[np.searchsorted(I, I2)]
        psi = psi / np.linalg.norm(psi)
        I = I2
    assert len(I) == 1
    return C.PATZ[I[0]]


# ---------------------------------------------------------------- drivers
def run(name, p, tau, ntraj, seed=12345, mode="drop", Uf=None):
    psi0 = C.PSI0[name]
    rng = np.random.default_rng(seed)
    Ts = rng.geometric(p, size=(ntraj, 12))
    counts = np.zeros(28, dtype=np.int64)
    for t in range(ntraj):
        if mode == "drop":
            k = traj_drop(psi0, Ts[t], tau, rng)
        elif mode == "proj":
            k = traj_proj(psi0, Ts[t], Uf, rng)
        else:
            k = traj_deph(psi0, rng)
        counts[k] += 1
    return counts, Ts.max(1)


def run_deph(name, ntraj, seed=999):
    psi0 = C.PSI0[name]
    rng = np.random.default_rng(seed)
    counts = np.zeros(28, dtype=np.int64)
    for t in range(ntraj):
        counts[traj_deph(psi0, rng)] += 1
    return counts


# ---------------------------------------------------------------- statistics
def stats(counts, ref_born):
    n = counts.sum()
    p = counts / n
    se = np.sqrt(p * (1 - p) / n)
    d_gs = C.l1(p, C.GS_BORN)
    d_un = C.l1(p, C.UNIF28)
    d_rf = C.l1(p, ref_born)
    # bootstrap standard errors on the L1 distances
    rng = np.random.default_rng(7)
    B = rng.multinomial(n, p, size=300) / n
    b_gs = np.abs(B - C.GS_BORN).sum(1).std()
    b_un = np.abs(B - C.UNIF28).sum(1).std()
    b_rf = np.abs(B - ref_born).sum(1).std()
    below = int((p < 1e-3).sum())
    zeros = int((counts == 0).sum())
    fmass = float(p[C.ZERO12].sum())
    fse = float(np.sqrt(fmass * (1 - fmass) / n))
    return dict(p=p, se=se, d_gs=d_gs, b_gs=b_gs, d_un=d_un, b_un=b_un,
                d_rf=d_rf, b_rf=b_rf, below=below, zeros=zeros,
                fmass=fmass, fse=fse, pmin=float(p.min()))


# ---------------------------------------------------------------- exact fixed schedules
def exact_schedule(psi0, stages, tau):
    """stages = list of (gap, [sites]); gap = number of tau-steps taken before this group
    forms.  Returns the exact 28-pattern odds of the finished set."""
    nodes = [(0, 0, C.get_block(0, 0), psi0, 1.0)]
    for gap, sites in stages:
        out = []
        Smask = 0
        for q in sites:
            Smask |= 1 << q
        for Rmask, wbits, blk, psi, pr in nodes:
            I, Ev, Vc, grp = blk
            if gap > 0:
                psi = C.evolve(psi, Ev, Vc, gap * tau)
            zI = C.ZL[I]
            keys = zI & Smask
            w = np.abs(psi) ** 2
            uk, inv = np.unique(keys, return_inverse=True)
            wk = np.bincount(inv, weights=w)
            for a in range(len(uk)):
                if wk[a] < 1e-14:
                    continue
                nR = Rmask | Smask
                nw = wbits | int(uk[a])
                blk2 = C.get_block(nR, nw)
                sub = psi[np.searchsorted(I, blk2[0])]
                out.append((nR, nw, blk2, sub / np.linalg.norm(sub), pr * wk[a]))
        nodes = out
    res = np.zeros(28)
    for Rmask, wbits, blk, psi, pr in nodes:
        assert len(blk[0]) == 1
        res[C.PATZ[blk[0][0]]] += pr
    assert abs(res.sum() - 1.0) < 1e-9, res.sum()
    return res
