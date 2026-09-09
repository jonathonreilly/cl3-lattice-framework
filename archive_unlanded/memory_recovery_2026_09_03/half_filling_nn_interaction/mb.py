#!/usr/bin/env python3
"""Many-body machinery for the record-conserving family
   H = -t sum_bonds eta_ij (c_i^dag c_j + h.c.) + V sum_bonds n_i n_j.
Sector/link-sign machinery reused from L1f/common.py (unmodified import)."""
from __future__ import annotations
import sys, itertools
sys.path.insert(0, "/private/tmp/claude-501/-Users-jonreilly/c26e73d8-5c00-4f5e-8060-c64e52ce77bc/scratchpad/L1f")
import numpy as np
from common import (Lat, EX, eta_ks, sector_eta, face_holonomy_list, one_particle,
                    f2_relations, f2_pivots, bits, qprod, transport, wrap)

POP = np.array([bin(i).count("1") for i in range(1 << 16)], dtype=np.int64)

def popc(x):
    return bin(x).count("1")

def basis(nv, N):
    """All nv-bit ints with N bits set, sorted; plus index map."""
    st = []
    for occ in itertools.combinations(range(nv), N):
        s = 0
        for o in occ:
            s |= 1 << o
        st.append(s)
    st.sort()
    return st, {s: k for k, s in enumerate(st)}

def bond_list(L):
    """[(iv, jv)] site-index pairs for each coarse bond, plus eta lookup key."""
    idx = {v: i for i, v in enumerate(L.V)}
    out = []
    for (v, ax) in L.E:
        w = L.step(v, EX[ax])
        out.append((idx[v], idx[w], (v, ax)))
    return out

def hop_apply(state, i, j):
    """c_i^dag c_j |state>.  Returns (newstate, sign) or None."""
    if not (state >> j) & 1:
        return None
    s1 = popc(state & ((1 << j) - 1))
    s = state ^ (1 << j)
    if (s >> i) & 1:
        return None
    s2 = popc(s & ((1 << i) - 1))
    return (s | (1 << i)), (1 if (s1 + s2) % 2 == 0 else -1)

def build_H(L, eta, N, g, t=1.0, dtype=float):
    """Dense many-body H in the N-particle sector.  t=1; g = V/t."""
    bl = bond_list(L)
    st, ix = basis(L.nv, N)
    D = len(st)
    H = np.zeros((D, D), dtype=dtype)
    for k, s in enumerate(st):
        # diagonal interaction
        d = 0
        for (i, j, key) in bl:
            if ((s >> i) & 1) and ((s >> j) & 1):
                d += 1
        H[k, k] += g * d
        # hopping
        for (i, j, key) in bl:
            e = eta[key]
            for (a, b) in ((i, j), (j, i)):
                r = hop_apply(s, a, b)
                if r is None:
                    continue
                ns, sg = r
                H[ix[ns], k] += -t * e * sg
    return H, st, ix

def build_H_int(L, eta, N, g_int, t_int=1):
    """Integer many-body H (g_int integer)."""
    return build_H(L, eta, N, g_int, t=t_int, dtype=np.int64)

def gs(H, k=6):
    """Full eigvalsh; return sorted levels."""
    return np.sort(np.linalg.eigvalsh(np.asarray(H, dtype=float)))
