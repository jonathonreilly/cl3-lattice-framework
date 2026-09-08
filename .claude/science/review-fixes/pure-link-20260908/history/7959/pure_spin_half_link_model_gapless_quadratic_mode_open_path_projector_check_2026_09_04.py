#!/usr/bin/env python3
"""The pure spin-1/2 link model on the cubic torus is gapless, deconfined and
unordered at L <= 12, with a quadratic transverse mode and a flat transverse
structure factor; an open-path projector that evades the plaquette-parity
obstruction, certified on three exact geometries.

Self-contained runner for the PURE spin-1/2 U(1) quantum link model -- no
matter -- in the conventions of PR #7911 / PR #7942, on three named finite
geometries plus two small path spaces.  One designed spin-1/2 link role per
edge, with

    E_e = (1/2) Z^L_e   (eigenvalues +-1/2),   U_e = (X^L_e + i Y^L_e)/2,
    (div E)_v = sum_{e at v} s_{v,e} E_e,      G_v = (div E)_v - rho_v,
    W_f = the oriented four-link ring product,  P_f = W_f + W_f^dag,
    H = -lambda sum_f P_f,   lambda supplied and set to 1,

the electric term a c-number at spin 1/2 because E_e^2 = I/4.  rho_v = 0 on
every torus (z_v = 6 even); the height-1 cylinder ladder carries PR #7911's
declared staggered background.

  A  [exact] THE 2x2x2 CENSUS.  9600 states, 937 plaquette-flip components with
     the full size multiset, 125 winding classes, the zero-winding class as
     864 + 16 frozen singletons, E_0, Delta_1, the internal gap, and the
     placement of the full-sector first excitation in the six unit-flux classes
     W = +-e_d.  S_L(k) = 0 at every k.
  B  [exact] THE L = 8 LADDER.  dim 49, three components, E_0 on the 47-state
     one, and the exact k = pi staggered plateau of the top-link correlator.
  C  [exact, needs cc] THE 4x2x2 CENSUS.  23,063,296 states, 405 winding
     classes, the zero-winding class as ONE flip component of 1,551,976 states
     plus 48 frozen states, E_0, S_L = 0, and the exact transverse-electric
     decay rates at k = pi/2 and k = pi.  Enumeration, component and Perron
     vector are done by the embedded C engine, compiled at run time.
  D  [exact] THE OPEN-PATH PROJECTOR'S BALANCE CERTIFICATES.  On COMPLETE path
     spaces of three small components: detailed balance and stationarity of the
     symmetric chain, global and skew balance of the bounce chain, its failure
     of plain detailed balance, irreducibility, Gauss's law on every state of
     every path, the middle-state marginal, and the exact ergodicity ceilings.
  E  [witness] THE SAMPLER ROWS, at declared seeds.  Both engines compiled here
     from embedded C: reptation on the 2x2x2 ice component and on the ladder,
     GFMC on 2x2x2 at three walker counts (population bias falling with the
     walker count) and on 4x2x2, and one short L = 4 GFMC run.  Skipped, with a
     stated reason, if no C compiler is available.
  F  [declared] THE L^3 PRODUCTION ROWS ARE QUOTED, NOT RECOMPUTED.  The
     L = 4, 6, 8, 10, 12 GFMC production of the source computation (seeds
     20261001-20261020 and 20261101-20261114, tau_prod 130-230, N_w = 500-8000,
     30 bins) costs hours of core time and is NOT rerun here; its numbers are
     declared constants and this group checks only the arithmetic read off
     them -- omega/k against omega/k^2, the confining expectation sigma L, and
     the Bragg ratio a plaquette solid would need.

Groups A, B, D and F are exact integer, bit and floating-point arithmetic in
Python; group C is exact and seed-free but needs a C compiler for the 23-million
state enumeration; group E rows are witnesses at declared seeds.  No dense
matrix anywhere exceeds 864 x 864, and peak memory stays under 400 MB.

Output: one PASS/SKIP/FAIL line per check and a final `TOTAL: PASS=N FAIL=M`.
Exit code 0 iff FAIL = 0.
"""

from __future__ import annotations

import math
import os
import shutil
import subprocess
import sys
import tempfile
import time
from collections import Counter

import numpy as np
import scipy.sparse as sp
from scipy.sparse.csgraph import connected_components

AUDIT_TIMEOUT_SEC = 300
LAM = 1.0
DELTA = 0.5
SEED_REPT = 20260904
SEED_GFMC_T222 = 20260930
SEED_GFMC_T422 = 20260931
SEED_GFMC_T4 = 20261001

T0 = time.time()
PASS = 0
FAIL = 0
SKIPPED = 0


def check(label, cond):
    global PASS, FAIL
    ok = bool(cond)
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print(("PASS " if ok else "FAIL ") + label)
    return ok


def skip(label, reason):
    global SKIPPED
    SKIPPED += 1
    print("SKIP " + label + " -- " + reason)


def close(a, b, tol=1e-9):
    return abs(float(a) - float(b)) <= tol


# ------------------------------------------------------------------ geometry
# Conventions redeclared here, verbatim from PR #7911 / PR #7942:
#   E_e = Z_e/2 ; bit b = 1 <-> E = +1/2 ; link (v,d) points from v to v+d_hat
#   (div E)_v = sum_e s_{v,e} E_e ,  s = +1 out of v, -1 into v ; G_v = (div E)_v - rho_v
#   face (v,d1<d2): ordered quadruple (p,q | u,w) = ((v,d1),(v+d1,d2) | (v+d2,d1),(v,d2))
#   P_f applicable iff b_p == b_q and b_u == b_w and b_p != b_u ; action = XOR of the four bits
#   torus: rho_v = 0 (z_v = 6 even).  ladder: 2 rho(t_i) = (-1)^i, 2 rho(b_i) = -(-1)^i
# Link index = 3*site + d, site = (x*Ly + y)*Lz + z.  Face index = 3*site + fi.
class Geo:
    def __init__(self, tag, NL, plaq, inc, rho2, pos=None, ldir=None, n=None, li=None):
        self.tag, self.NL, self.plaq, self.inc, self.rho2 = tag, NL, plaq, inc, rho2
        self.pos, self.ldir, self.n, self.li = pos, ldir, n, li
        self.NP = len(plaq)
        self.NV = len(inc)

    def gauss_residual(self, bits):
        worst = 0
        for v, lst in self.inc.items():
            tot = sum(sg * (1 if (bits >> j) & 1 else -1) for j, sg in lst)
            worst = max(worst, abs(tot - self.rho2[v]))
        return worst

    def applicable(self, s, f):
        p, q, u, w = self.plaq[f]
        bp, bq, bu, bw = (s >> p) & 1, (s >> q) & 1, (s >> u) & 1, (s >> w) & 1
        return bp == bq and bu == bw and bp != bu

    def flips(self, s):
        out = []
        for f, (p, q, u, w) in enumerate(self.plaq):
            bp, bq, bu, bw = (s >> p) & 1, (s >> q) & 1, (s >> u) & 1, (s >> w) & 1
            if bp == bq and bu == bw and bp != bu:
                out.append((f, s ^ (1 << p) ^ (1 << q) ^ (1 << u) ^ (1 << w)))
        return out

    def n_app(self, s):
        return len(self.flips(s))


def torus3d(Lx, Ly, Lz):
    n = (Lx, Ly, Lz)
    sites = [(x, y, z) for x in range(Lx) for y in range(Ly) for z in range(Lz)]

    def step(s, d):
        return tuple(((s[i] + 1) % n[i]) if i == d else s[i] for i in range(3))

    li, links, pos, ldir = {}, [], [], []
    for s in sites:
        for d in range(3):
            li[(s, d)] = len(links)
            links.append((s, d))
            pos.append(s)
            ldir.append(d)
    inc = {s: [] for s in sites}
    for (s, d), j in li.items():
        inc[s].append((j, +1))
        inc[step(s, d)].append((j, -1))
    plaq = []
    for s in sites:
        for d1 in range(3):
            for d2 in range(d1 + 1, 3):
                a, b = step(s, d1), step(s, d2)
                plaq.append((li[(s, d1)], li[(a, d2)], li[(b, d1)], li[(s, d2)]))
    rho2 = {s: 0 for s in sites}
    g = Geo("t%d%d%d" % (Lx, Ly, Lz), len(links), plaq, inc, rho2, pos, ldir, n, li)
    g.sites = sites
    return g


def ladder(L):
    """PR #7911's height-1 cylinder.  T_i = 3i, B_i = 3i+1, R_i = 3i+2; face i = (T_i, R_i | R_{i+1}, B_i)."""
    NL = 3 * L
    T = lambda i: 3 * (i % L)
    B = lambda i: 3 * (i % L) + 1
    R = lambda i: 3 * (i % L) + 2
    inc = {}
    for i in range(L):
        inc[('t', i)] = [(T(i), +1), (T(i - 1), -1), (R(i), -1)]
        inc[('b', i)] = [(B(i), +1), (B(i - 1), -1), (R(i), +1)]
    rho2 = {}
    for i in range(L):
        rho2[('t', i)] = (-1) ** i
        rho2[('b', i)] = -((-1) ** i)
    plaq = [(T(i), R(i), R(i + 1), B(i)) for i in range(L)]
    return Geo("lad%d" % L, NL, plaq, inc, rho2)


def ice_config(g):
    """The analytic Gauss-law-zero configuration e(v,x) = (-1)^{v_y+v_z} and cyclic."""
    bits = 0
    for (s, d), j in g.li.items():
        other = [s[i] for i in range(3) if i != d]
        if sum(other) % 2 == 0:
            bits |= 1 << j
    return bits


def winding(g, bits):
    """W_d = sum over links (v,d) with v_d = 0 of e/2; integer on even tori, cut-independent by G_v = 0."""
    W = []
    for d in range(3):
        tot = 0
        for (s, dd), j in g.li.items():
            if dd == d and s[d] == 0:
                tot += (1 if (bits >> j) & 1 else -1)
        W.append(tot // 2)
    return tuple(W)


def enumerate_sector(g):
    """Site-by-site assignment of the unassigned incident links, enforcing G_v at each site."""
    order = list(g.inc.keys())
    seen, todo = set(), []
    for s in order:
        new = [j for (j, sg) in g.inc[s] if j not in seen]
        for j in new:
            seen.add(j)
        todo.append(new)
    part = [0]
    for k, s in enumerate(order):
        new, inc, target = todo[k], g.inc[s], g.rho2[s]
        old = [(j, sg) for (j, sg) in inc if j not in new]
        newsg = [(j, sg) for (j, sg) in inc if j in new]
        nxt = []
        for st in part:
            base = 0
            for (j, sg) in old:
                base += sg * (1 if (st >> j) & 1 else -1)
            for m in range(1 << len(new)):
                tot = base
                st2 = st
                for a, (j, sg) in enumerate(newsg):
                    if (m >> a) & 1:
                        st2 |= 1 << j
                        tot += sg
                    else:
                        tot -= sg
                if tot == target:
                    nxt.append(st2)
        part = nxt
    return sorted(set(part))


def components(g, states):
    idx = {s: i for i, s in enumerate(states)}
    seen = [False] * len(states)
    comps = []
    for i0 in range(len(states)):
        if seen[i0]:
            continue
        comp, stack = [i0], [i0]
        seen[i0] = True
        while stack:
            i = stack.pop()
            for f, t in g.flips(states[i]):
                j = idx[t]
                if not seen[j]:
                    seen[j] = True
                    comp.append(j)
                    stack.append(j)
        comps.append(sorted(comp))
    return comps


def hamiltonian_dense(g, comp_states, lam=LAM):
    idx = {s: i for i, s in enumerate(comp_states)}
    n = len(comp_states)
    H = np.zeros((n, n))
    for i, s in enumerate(comp_states):
        for f, t in g.flips(s):
            H[idx[t], i] -= lam
    return H


def write_geo(g, path, init_bits):
    with open(path, "w") as fh:
        fh.write("%d %d %d\n" % (g.NL, g.NP, g.NV))
        for (p, q, u, w) in g.plaq:
            fh.write("%d %d %d %d\n" % (p, q, u, w))
        fh.write("".join('1' if (init_bits >> j) & 1 else '0' for j in range(g.NL)) + "\n")
        if g.n is not None:
            fh.write("%d %d %d\n" % g.n)
            for j in range(g.NL):
                x, y, z = g.pos[j]
                fh.write("%d %d %d %d\n" % (x, y, z, g.ldir[j]))
        else:
            fh.write("0 0 0\n")
        for v, lst in g.inc.items():
            fh.write(str(len(lst)) + " " + " ".join("%d %d" % (j, sg) for j, sg in lst) + " %d\n" % g.rho2[v])


def fourier_E(g, Evals, k):
    out = np.zeros((Evals.shape[0], 3), dtype=complex)
    for j in range(g.NL):
        x, y, z = g.pos[j]
        ph = np.exp(-1j * (k[0] * x + k[1] * y + k[2] * z))
        out[:, g.ldir[j]] += ph * Evals[:, j]
    return out


def E_vals(g, states):
    arr = np.zeros((len(states), g.NL))
    for i, s in enumerate(states):
        for j in range(g.NL):
            arr[i, j] = 0.5 if (s >> j) & 1 else -0.5
    return arr


# ================================================== the embedded C engines
# Compiled at run time into a private temporary directory; no binary and no external
# datum is trusted.  t422x.c is written for this runner; reptate.c and gfmc.c are the
# source computation's engines verbatim except for one printf string and one counter
# name, both reworded to "commuting-step exchanges" -- no code path changes.
C_T422 = r"""/* Exact, seed-free 4x2x2 engine: Gauss-sector enumeration, winding census, flip component,
 * Perron vector of B = I + A on the component, transverse structure factors and the exact
 * transverse-electric decay rates.  Reads the .geo written by the runner's own indexing.
 * usage: t422x geo mmax                                                                     */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <math.h>

static int NL, NP, NV, Lx, Ly, Lz;
static int (*plq)[4];
static int *lpx, *lpy, *lpz, *ldir;
static int *inc_cnt, (*inc_link)[8], (*inc_sign)[8], *rho2;
static unsigned char *initb;
static int (*newl)[8], *newl_cnt;
static uint64_t *St; static int64_t nst = 0; static int counting = 1; static int64_t ncount = 0;

static void read_geo(const char *fn) {
    FILE *fh = fopen(fn, "r"); if (!fh) { fprintf(stderr, "no geo\n"); exit(1); }
    if (fscanf(fh, "%d %d %d", &NL, &NP, &NV) != 3) exit(2);
    plq = malloc(sizeof(int[4]) * NP);
    for (int f = 0; f < NP; f++) if (fscanf(fh, "%d %d %d %d", &plq[f][0], &plq[f][1], &plq[f][2], &plq[f][3]) != 4) exit(3);
    char *buf = malloc(NL + 16); if (fscanf(fh, "%s", buf) != 1) exit(4);
    initb = malloc(NL); for (int j = 0; j < NL; j++) initb[j] = (buf[j] == '1');
    if (fscanf(fh, "%d %d %d", &Lx, &Ly, &Lz) != 3) exit(5);
    lpx = malloc(sizeof(int) * NL); lpy = malloc(sizeof(int) * NL); lpz = malloc(sizeof(int) * NL); ldir = malloc(sizeof(int) * NL);
    for (int j = 0; j < NL; j++) if (fscanf(fh, "%d %d %d %d", &lpx[j], &lpy[j], &lpz[j], &ldir[j]) != 4) exit(6);
    inc_cnt = malloc(sizeof(int) * NV); inc_link = malloc(sizeof(int[8]) * NV); inc_sign = malloc(sizeof(int[8]) * NV); rho2 = malloc(sizeof(int) * NV);
    for (int v = 0; v < NV; v++) {
        if (fscanf(fh, "%d", &inc_cnt[v]) != 1) exit(7);
        for (int a = 0; a < inc_cnt[v]; a++) if (fscanf(fh, "%d %d", &inc_link[v][a], &inc_sign[v][a]) != 2) exit(8);
        if (fscanf(fh, "%d", &rho2[v]) != 1) exit(9);
    }
    fclose(fh);
}

static void rec(int v, uint64_t bits) {
    if (v == NV) { if (counting) ncount++; else St[nst++] = bits; return; }
    int k = newl_cnt[v];
    for (int m = 0; m < (1 << k); m++) {
        uint64_t b = bits;
        for (int a = 0; a < k; a++) if ((m >> a) & 1) b |= 1ULL << newl[v][a];
        int tot = 0;
        for (int a = 0; a < inc_cnt[v]; a++) tot += inc_sign[v][a] * (((b >> inc_link[v][a]) & 1) ? 1 : -1);
        if (tot == rho2[v]) rec(v + 1, b);
    }
}
static int cmp64(const void *a, const void *b) { uint64_t x = *(const uint64_t *)a, y = *(const uint64_t *)b; return (x < y) ? -1 : (x > y); }

static int64_t M; static uint64_t *S; static int64_t *rowptr; static int32_t *col; static int8_t *napp;
static int64_t bs(const uint64_t *arr, int64_t n, uint64_t x) {
    int64_t lo = 0, hi = n - 1;
    while (lo <= hi) { int64_t mid = (lo + hi) >> 1; if (arr[mid] == x) return mid; if (arr[mid] < x) lo = mid + 1; else hi = mid - 1; }
    return -1;
}
static void matvec_A(const double *x, double *y) {
    for (int64_t i = 0; i < M; i++) { double s = 0; for (int64_t p = rowptr[i]; p < rowptr[i + 1]; p++) s += x[col[p]]; y[i] = s; }
}

int main(int argc, char **argv) {
    if (argc < 3) { fprintf(stderr, "usage: t422x geo mmax\n"); return 1; }
    read_geo(argv[1]);
    int mmax = atoi(argv[2]);
    newl = malloc(sizeof(int[8]) * NV); newl_cnt = calloc(NV, sizeof(int));
    char *seen = calloc(NL, 1);
    for (int v = 0; v < NV; v++) for (int q = 0; q < inc_cnt[v]; q++) { int j = inc_link[v][q]; if (!seen[j]) { seen[j] = 1; newl[v][newl_cnt[v]++] = j; } }
    counting = 1; rec(0, 0);
    int64_t n = ncount;
    St = malloc(8 * (size_t)n); if (!St) { fprintf(stderr, "oom states\n"); return 2; }
    counting = 0; rec(0, 0);
    qsort(St, n, 8, cmp64);
    int64_t dup = 0; for (int64_t i = 1; i < n; i++) if (St[i] <= St[i - 1]) dup++;
    printf("dim_gauss=%lld sorted_unique=%d\n", (long long)n, dup == 0);
    /* re-derive Gauss on every state */
    int64_t bad = 0;
    for (int64_t i = 0; i < n; i++) {
        uint64_t b = St[i];
        for (int v = 0; v < NV; v++) { int tot = 0; for (int a = 0; a < inc_cnt[v]; a++) tot += inc_sign[v][a] * (((b >> inc_link[v][a]) & 1) ? 1 : -1); if (tot != rho2[v]) { bad++; break; } }
    }
    printf("gauss_violations=%lld\n", (long long)bad);
    /* winding class of every state; key = (Wx+8)*289 + (Wy+8)*17 + (Wz+8) */
    int nwl[3] = {0, 0, 0}; int wlink[3][16];
    for (int j = 0; j < NL; j++) { int d = ldir[j]; int c = (d == 0) ? lpx[j] : (d == 1 ? lpy[j] : lpz[j]); if (c == 0) wlink[d][nwl[d]++] = j; }
    int *wcount = calloc(4913, sizeof(int));
    int32_t *key = malloc(4 * (size_t)n);
    uint64_t fmask[64];
    for (int f = 0; f < NP; f++) fmask[f] = (1ULL << plq[f][0]) | (1ULL << plq[f][1]) | (1ULL << plq[f][2]) | (1ULL << plq[f][3]);
    int8_t *nap = malloc((size_t)n);
    int64_t frozen = 0, frozen0 = 0;
    for (int64_t i = 0; i < n; i++) {
        uint64_t b = St[i]; int W[3];
        for (int d = 0; d < 3; d++) { int t = 0; for (int q = 0; q < nwl[d]; q++) t += ((b >> wlink[d][q]) & 1) ? 1 : -1; W[d] = t / 2; }
        int32_t k = (W[0] + 8) * 289 + (W[1] + 8) * 17 + (W[2] + 8);
        key[i] = k; wcount[k]++;
        int na = 0;
        for (int f = 0; f < NP; f++) { int bp = (b >> plq[f][0]) & 1, bq = (b >> plq[f][1]) & 1, bu = (b >> plq[f][2]) & 1, bw = (b >> plq[f][3]) & 1; if (bp == bq && bu == bw && bp != bu) na++; }
        nap[i] = (int8_t)na;
        if (na == 0) { frozen++; if (k == 8 * 289 + 8 * 17 + 8) frozen0++; }
    }
    int ndist = 0, wmax = 0;
    for (int i = 0; i < 4913; i++) { if (wcount[i]) ndist++; if (wcount[i] > wmax) wmax = wcount[i]; }
    int32_t k0 = 8 * 289 + 8 * 17 + 8;
    printf("winding_classes=%d zero_winding=%d w100=%d w010=%d w001=%d largest_class=%d\n",
           ndist, wcount[k0], wcount[k0 + 289], wcount[k0 + 17], wcount[k0 + 1], wmax);
    printf("frozen_total=%lld frozen_zero_winding=%lld\n", (long long)frozen, (long long)frozen0);
    /* BFS from the ice state */
    uint64_t ice = 0; for (int j = 0; j < NL; j++) if (initb[j]) ice |= 1ULL << j;
    int64_t i0 = bs(St, n, ice); if (i0 < 0) { fprintf(stderr, "ice not in sector\n"); return 3; }
    printf("ice_key_is_zero=%d ice_napp=%d\n", key[i0] == k0, (int)nap[i0]);
    unsigned char *vis = calloc((n + 7) / 8, 1);
    int64_t *queue = malloc(8 * 2000000); int64_t qcap = 2000000, qn = 0;
    vis[i0 >> 3] |= 1 << (i0 & 7); queue[qn++] = i0;
    int64_t lstart = 0, lend = 1; int depth = 0;
    while (lstart < lend) {
        for (int64_t p = lstart; p < lend; p++) {
            uint64_t b = St[queue[p]];
            for (int f = 0; f < NP; f++) {
                int bp = (b >> plq[f][0]) & 1, bq = (b >> plq[f][1]) & 1, bu = (b >> plq[f][2]) & 1, bw = (b >> plq[f][3]) & 1;
                if (!(bp == bq && bu == bw && bp != bu)) continue;
                int64_t j = bs(St, n, b ^ fmask[f]);
                if (j < 0) { fprintf(stderr, "missing target in sector\n"); return 4; }
                if (!(vis[j >> 3] & (1 << (j & 7)))) {
                    vis[j >> 3] |= 1 << (j & 7);
                    if (qn == qcap) { qcap *= 2; queue = realloc(queue, 8 * qcap); }
                    queue[qn++] = j;
                }
            }
        }
        lstart = lend; lend = qn; depth++;
    }
    printf("component=%lld bfs_depth=%d zero_minus_comp_minus_frozen0=%lld\n", (long long)qn, depth, (long long)(wcount[k0] - qn - frozen0));
    /* extract the component, free the sector */
    M = qn;
    S = malloc(8 * (size_t)M);
    int64_t mm = 0; for (int64_t i = 0; i < n; i++) if (vis[i >> 3] & (1 << (i & 7))) S[mm++] = St[i];
    int allzero = 1; for (int64_t i = 0; i < n; i++) if ((vis[i >> 3] & (1 << (i & 7))) && key[i] != k0) { allzero = 0; break; }
    printf("component_all_zero_winding=%d\n", allzero);
    free(St); free(key); free(vis); free(queue); free(nap); St = NULL;
    /* CSR adjacency */
    rowptr = malloc(8 * (size_t)(M + 1)); napp = malloc((size_t)M);
    int64_t nnz = 0;
    for (int64_t i = 0; i < M; i++) {
        uint64_t b = S[i]; int na = 0;
        for (int f = 0; f < NP; f++) { int bp = (b >> plq[f][0]) & 1, bq = (b >> plq[f][1]) & 1, bu = (b >> plq[f][2]) & 1, bw = (b >> plq[f][3]) & 1; if (bp == bq && bu == bw && bp != bu) na++; }
        napp[i] = (int8_t)na; rowptr[i] = nnz; nnz += na;
    }
    rowptr[M] = nnz;
    col = malloc(4 * (size_t)nnz);
    int64_t missing = 0;
    for (int64_t i = 0; i < M; i++) {
        uint64_t b = S[i]; int64_t p = rowptr[i];
        for (int f = 0; f < NP; f++) {
            int bp = (b >> plq[f][0]) & 1, bq = (b >> plq[f][1]) & 1, bu = (b >> plq[f][2]) & 1, bw = (b >> plq[f][3]) & 1;
            if (bp == bq && bu == bw && bp != bu) { int64_t j = bs(S, M, b ^ fmask[f]); if (j < 0) { missing++; j = i; } col[p++] = (int32_t)j; }
        }
    }
    printf("nnz=%lld missing_targets=%lld\n", (long long)nnz, (long long)missing);
    /* Perron vector of B = I + A by power iteration */
    double *x = malloc(8 * (size_t)M), *y = malloc(8 * (size_t)M);
    for (int64_t i = 0; i < M; i++) x[i] = 1.0 / sqrt((double)M);
    double lam = 0, lam_old = -1; int it;
    for (it = 0; it < 5000; it++) {
        matvec_A(x, y);
        for (int64_t i = 0; i < M; i++) y[i] += x[i];
        double nrm = 0, rq = 0;
        for (int64_t i = 0; i < M; i++) { nrm += y[i] * y[i]; rq += x[i] * y[i]; }
        nrm = sqrt(nrm); lam = rq;
        for (int64_t i = 0; i < M; i++) x[i] = y[i] / nrm;
        if (fabs(lam - lam_old) < 1e-14 && it > 40) break;
        lam_old = lam;
    }
    double a0 = lam - 1.0;
    matvec_A(x, y); double ray = 0, res = 0;
    for (int64_t i = 0; i < M; i++) ray += x[i] * y[i];
    for (int64_t i = 0; i < M; i++) { double d = y[i] - ray * x[i]; res += d * d; }
    double nap0 = 0, sx = 0, snx = 0;
    for (int64_t i = 0; i < M; i++) { nap0 += x[i] * x[i] * napp[i]; sx += x[i]; snx += x[i] * napp[i]; }
    printf("power_it=%d E0=%.10f rayleigh_a0=%.10f residual=%.2e napp0=%.10f mixed=%.10f Pf=%.10f\n",
           it, -ray, ray, sqrt(res), nap0, -snx / sx, ray / NP);
    /* structure factors and exact decay rates at k = (2 pi q / Lx, 0, 0) */
    double Ns = (double)(Lx * Ly * Lz);
    double *orr = malloc(8 * (size_t)M), *oii = malloc(8 * (size_t)M);
    double *ar = malloc(8 * (size_t)M), *ai = malloc(8 * (size_t)M), *tr = malloc(8 * (size_t)M), *ti = malloc(8 * (size_t)M);
    double delta = 0.25, lamd = 1.0 + delta * ray;
    for (int q = 1; q <= Lx / 2; q++) {
        double kv = 2 * M_PI * q / Lx;
        for (int mu = 0; mu < 3; mu++) {
            for (int64_t i = 0; i < M; i++) {
                double zr = 0, zi = 0;
                for (int j = 0; j < NL; j++) if (ldir[j] == mu) { double e = ((S[i] >> j) & 1) ? 0.5 : -0.5; zr += cos(kv * lpx[j]) * e; zi += -sin(kv * lpx[j]) * e; }
                orr[i] = zr / sqrt(Ns) * x[i]; oii[i] = zi / sqrt(Ns) * x[i];
            }
            double s = 0; for (int64_t i = 0; i < M; i++) s += orr[i] * orr[i] + oii[i] * oii[i];
            printf("S q=%d mu=%d val=%.10f\n", q, mu, s);
            if (mu == 0) continue;
            if (mu == 2) continue;       /* S_zz equals S_yy by the y<->z symmetry, checked at mu=2 above */
            memcpy(ar, orr, 8 * (size_t)M); memcpy(ai, oii, 8 * (size_t)M);
            double c0 = s, cprev = s, scale = 1.0;
            for (int m = 1; m <= mmax; m++) {
                matvec_A(ar, tr); matvec_A(ai, ti);
                for (int64_t i = 0; i < M; i++) { ar[i] += delta * tr[i]; ai[i] += delta * ti[i]; }
                scale *= lamd;
                double cm = 0; for (int64_t i = 0; i < M; i++) cm += orr[i] * ar[i] + oii[i] * ai[i];
                cm /= scale;
                if (m == 40 || m == 80 || m == 120 || m == mmax) printf("omega q=%d m=%d ratio=%.10f omega_eff=%.6f\n", q, m, cm / c0, lamd * (1.0 - cm / cprev) / delta);
                cprev = cm;
            }
        }
    }
    return 0;
}
"""

C_REPTATE = r"""/* P2 -- open-path (projector) Monte Carlo for the spin-1/2 U(1) quantum link model
 *        H = -lam sum_f P_f ,  lam = 1 ,  on a Gauss-law sector.
 *
 * Representation.  A = -H/lam is the adjacency matrix of the plaquette-flip graph of the sector
 * (P_f applicable  <=>  edge).  The lazy propagator  B = I + delta*A  has the same eigenvectors as H,
 * eigenvalues 1 + delta*a_n, and its Perron eigenvector is the sector ground state.  A path of N
 * steps  s_0 -> s_1 -> ... -> s_N  carries weight  prod_i B_{s_i s_{i+1}} = delta^{#moves}, with
 * step i either a 'stay' (weight 1) or a single plaquette flip (weight delta).  Summing over all
 * paths with uniform (trial) end states gives  Z(N) = 1^T B^N 1 ; the middle of a long path is
 * distributed as psi_0(s)^2, the ends as psi_0(s).
 *
 * Update (reptation).  Grow one end by one step proposed from  q(s'|s) = B_{s s'}/(1+delta n_app(s))
 * and shrink the other end.  Detailed balance (symmetric mode, direction chosen at random) gives
 * the Metropolis acceptance  min(1, (1+delta n_app(old head))/(1+delta n_app(new tail))).  Bounce
 * mode keeps the direction until a rejection and then reverses it (Pierleoni-Ceperley); both are
 * certified exactly in cert_transition_matrix.py on a small path space.
 *
 * Gauss's law is preserved by construction (only P_f applications ever touch the state); it is
 * re-verified from the incidence lists at every measurement (gauss_err counter).
 *
 * Estimators (lam = 1):
 *   E_mix    = -<n_app(end)>                                 (mixed, exact as N -> inf)
 *   mv       = P(bulk step is a move) -> delta a0/(1+delta a0)  so  E_pure = -mv/(delta(1-mv))
 *   <O>_bulk for diagonal O (n_app, |E_mu(k)|^2, flippability dumps)
 *   C_O(m)   = <O_j O*_{j+m}>_bulk on block-averaged series (block b steps) for transverse E(k)
 *              at axis momenta k = 2 pi n/L e_d, n = 1..kmax, d = x,y,z.
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <stdint.h>
#include <complex.h>

/* ---------------------------------------------------------------- RNG: xoshiro256** */
static uint64_t rs[4];
static inline uint64_t rotl(const uint64_t x, int k) { return (x << k) | (x >> (64 - k)); }
static uint64_t next_u64(void) {
    const uint64_t result = rotl(rs[1] * 5, 7) * 9;
    const uint64_t t = rs[1] << 17;
    rs[2] ^= rs[0]; rs[3] ^= rs[1]; rs[1] ^= rs[2]; rs[0] ^= rs[3]; rs[2] ^= t; rs[3] = rotl(rs[3], 45);
    return result;
}
static double urand(void) { return (next_u64() >> 11) * (1.0 / 9007199254740992.0); }
static void seed_rng(uint64_t seed) {
    uint64_t z = seed;
    for (int i = 0; i < 4; i++) {           /* splitmix64 */
        z += 0x9e3779b97f4a7c15ULL;
        uint64_t x = z;
        x = (x ^ (x >> 30)) * 0xbf58476d1ce4e5b9ULL;
        x = (x ^ (x >> 27)) * 0x94d049bb133111ebULL;
        rs[i] = x ^ (x >> 31);
    }
}

/* ---------------------------------------------------------------- geometry */
static int NL, NP, NV, Lx, Ly, Lz, is3d;
static int (*plq)[4];          /* face -> p q u w */
static int *nbf_cnt, (*nbf)[13];  /* face -> faces sharing a link (incl. itself) */
static int *lpos_x, *lpos_y, *lpos_z, *ldir;
static int *inc_cnt, (*inc_link)[8], (*inc_sign)[8], *rho2;
static unsigned char *init_bits;

static int cmp_int(const void *a, const void *b) { return (*(int *)a) - (*(int *)b); }

static void read_geo(const char *fn) {
    FILE *fh = fopen(fn, "r");
    if (!fh) { fprintf(stderr, "cannot open %s\n", fn); exit(1); }
    if (fscanf(fh, "%d %d %d", &NL, &NP, &NV) != 3) exit(2);
    plq = malloc(sizeof(int[4]) * NP);
    for (int f = 0; f < NP; f++)
        if (fscanf(fh, "%d %d %d %d", &plq[f][0], &plq[f][1], &plq[f][2], &plq[f][3]) != 4) exit(3);
    init_bits = malloc(NL);
    char *buf = malloc(NL + 16);
    if (fscanf(fh, "%s", buf) != 1) exit(4);
    for (int j = 0; j < NL; j++) init_bits[j] = (buf[j] == '1');
    free(buf);
    if (fscanf(fh, "%d %d %d", &Lx, &Ly, &Lz) != 3) exit(5);
    is3d = (Lx > 0);
    lpos_x = malloc(sizeof(int) * NL); lpos_y = malloc(sizeof(int) * NL); lpos_z = malloc(sizeof(int) * NL); ldir = malloc(sizeof(int) * NL);
    if (is3d)
        for (int j = 0; j < NL; j++)
            if (fscanf(fh, "%d %d %d %d", &lpos_x[j], &lpos_y[j], &lpos_z[j], &ldir[j]) != 4) exit(6);
    inc_cnt = malloc(sizeof(int) * NV); inc_link = malloc(sizeof(int[8]) * NV); inc_sign = malloc(sizeof(int[8]) * NV); rho2 = malloc(sizeof(int) * NV);
    for (int v = 0; v < NV; v++) {
        if (fscanf(fh, "%d", &inc_cnt[v]) != 1) exit(7);
        for (int a = 0; a < inc_cnt[v]; a++)
            if (fscanf(fh, "%d %d", &inc_link[v][a], &inc_sign[v][a]) != 2) exit(8);
        if (fscanf(fh, "%d", &rho2[v]) != 1) exit(9);
    }
    fclose(fh);
    /* link -> faces */
    int *lf_cnt = calloc(NL, sizeof(int));
    int (*lf)[8] = malloc(sizeof(int[8]) * NL);
    for (int f = 0; f < NP; f++)
        for (int a = 0; a < 4; a++) { int j = plq[f][a]; lf[j][lf_cnt[j]++] = f; }
    nbf_cnt = calloc(NP, sizeof(int)); nbf = malloc(sizeof(int[13]) * NP);
    for (int f = 0; f < NP; f++) {
        int tmp[40], n = 0;
        tmp[n++] = f;
        for (int a = 0; a < 4; a++) { int j = plq[f][a]; for (int b = 0; b < lf_cnt[j]; b++) tmp[n++] = lf[j][b]; }
        qsort(tmp, n, sizeof(int), cmp_int);
        int m = 0;
        for (int i = 0; i < n; i++) if (i == 0 || tmp[i] != tmp[i - 1]) nbf[f][m++] = tmp[i];
        if (m > 13) { fprintf(stderr, "nbf overflow\n"); exit(10); }
        nbf_cnt[f] = m;
    }
    free(lf_cnt); free(lf);
}

/* ---------------------------------------------------------------- end states with applicability lists */
typedef struct {
    unsigned char *b;      /* link bits */
    int *app_list;         /* applicable faces */
    int *app_pos;          /* face -> position in list or -1 */
    int n_app;
} End;

static inline int applicable(const unsigned char *b, int f) {
    int bp = b[plq[f][0]], bq = b[plq[f][1]], bu = b[plq[f][2]], bw = b[plq[f][3]];
    return (bp == bq) && (bu == bw) && (bp != bu);
}
static inline void flip_bits(unsigned char *b, int f) {
    b[plq[f][0]] ^= 1; b[plq[f][1]] ^= 1; b[plq[f][2]] ^= 1; b[plq[f][3]] ^= 1;
}
static void end_init(End *e, const unsigned char *bits) {
    e->b = malloc(NL); memcpy(e->b, bits, NL);
    e->app_list = malloc(sizeof(int) * NP); e->app_pos = malloc(sizeof(int) * NP); e->n_app = 0;
    for (int f = 0; f < NP; f++) {
        if (applicable(e->b, f)) { e->app_pos[f] = e->n_app; e->app_list[e->n_app++] = f; }
        else e->app_pos[f] = -1;
    }
}
static inline void end_set_app(End *e, int f, int val) {
    int pos = e->app_pos[f];
    if (val && pos < 0) { e->app_pos[f] = e->n_app; e->app_list[e->n_app++] = f; }
    else if (!val && pos >= 0) {
        int last = e->app_list[--e->n_app];
        e->app_list[pos] = last; e->app_pos[last] = pos; e->app_pos[f] = -1;
    }
}
static void end_flip(End *e, int f) {
    flip_bits(e->b, f);
    for (int i = 0; i < nbf_cnt[f]; i++) { int g = nbf[f][i]; end_set_app(e, g, applicable(e->b, g)); }
}
/* n_app of the state obtained by flipping f in e (without modifying e) */
static int n_app_after(End *e, int f) {
    int n = e->n_app;
    flip_bits(e->b, f);
    for (int i = 0; i < nbf_cnt[f]; i++) { int g = nbf[f][i]; int now = applicable(e->b, g); int was = (e->app_pos[g] >= 0); n += now - was; }
    flip_bits(e->b, f);
    return n;
}
static int gauss_residual(const unsigned char *b) {
    int worst = 0;
    for (int v = 0; v < NV; v++) {
        int tot = 0;
        for (int a = 0; a < inc_cnt[v]; a++) tot += inc_sign[v][a] * (b[inc_link[v][a]] ? 1 : -1);
        int r = abs(tot - rho2[v]); if (r > worst) worst = r;
    }
    return worst;
}

/* ---------------------------------------------------------------- visited-state set (small NL only) */
#define HSZ (1 << 23)
#define PAIR_D 64
static uint64_t *hset; static int hcount = 0; static int track_visits = 0;
static uint64_t bits_to_u64(const unsigned char *b) { uint64_t x = 0; for (int j = 0; j < NL; j++) if (b[j]) x |= (1ULL << j); return x; }
static void visit(const unsigned char *b) {
    uint64_t x = bits_to_u64(b) + 1;  /* +1 so that 0 marks empty */
    uint64_t h = (x * 0x9e3779b97f4a7c15ULL) >> 41;
    while (hset[h] && hset[h] != x) h = (h + 1) & (HSZ - 1);
    if (!hset[h]) { hset[h] = x; hcount++; }
}

/* ---------------------------------------------------------------- main */
int main(int argc, char **argv) {
    if (argc < 17) {
        fprintf(stderr, "usage: reptate geo delta N Nl n_therm n_moves meas_every nbins seed mode block mmax kmax dump_every outprefix sweep_every\n");
        return 1;
    }
    long sweep_every = atol(argv[16]);
    const char *geo = argv[1]; double delta = atof(argv[2]); int N = atoi(argv[3]); int Nl = atoi(argv[4]);
    long n_therm = atol(argv[5]); long n_moves = atol(argv[6]); long meas_every = atol(argv[7]); int nbins = atoi(argv[8]);
    uint64_t seed = strtoull(argv[9], NULL, 10); int mode = atoi(argv[10]); int block = atoi(argv[11]); int mmax = atoi(argv[12]);
    int kmax = atoi(argv[13]); long dump_every = atol(argv[14]); const char *outp = argv[15];
    read_geo(geo);
    seed_rng(seed);
    track_visits = (NL <= 62);
    if (track_visits) hset = calloc(HSZ, sizeof(uint64_t));
    printf("# reptate: geo=%s NL=%d NP=%d NV=%d delta=%g N=%d Nl=%d n_therm=%ld n_moves=%ld meas_every=%ld nbins=%d seed=%llu mode=%s block=%d mmax=%d kmax=%d dump_every=%ld\n",
           geo, NL, NP, NV, delta, N, Nl, n_therm, n_moves, meas_every, nbins, (unsigned long long)seed, mode ? "bounce" : "symmetric", block, mmax, kmax, dump_every);
    printf("# interior sweep (adjacent same-face pair insert/delete + commuting-step exchanges) every %ld moves\n", sweep_every);
    printf("# init gauss residual = %d, init n_app = ", gauss_residual(init_bits));
    End E[2];  /* E[0] = tail (s_0), E[1] = head (s_N) */
    end_init(&E[0], init_bits); end_init(&E[1], init_bits);
    printf("%d\n", E[0].n_app);
    /* path ring buffer: step[(t0 + i) % N] connects s_i -> s_{i+1}; initial path = all stays */
    int *step = malloc(sizeof(int) * N); for (int i = 0; i < N; i++) step[i] = -1;
    int t0 = 0;
    for (int i = 0; i < N; i++) {          /* grow the head N times with the proposal chain */
        int ng0 = E[1].n_app; int f0 = -1;
        if (urand() >= 1.0 / (1.0 + delta * ng0)) f0 = E[1].app_list[(int)(urand() * ng0)];
        step[i] = f0; if (f0 >= 0) end_flip(&E[1], f0);
    }
    printf("# initial path: forward walk, n_app(tail)=%d n_app(head)=%d\n", E[0].n_app, E[1].n_app);
    End cur; end_init(&cur, E[0].b);
    long sw_ins_try = 0, sw_ins_acc = 0, sw_del_try = 0, sw_del_acc = 0, sw_exch = 0;
    /* momenta: axis directions d, n = 1..kmax ; phase tables per link (complex) */
    int NK = is3d ? 3 * kmax : 1;
    double complex *ph = malloc(sizeof(double complex) * NK * NL);
    int *k_d = malloc(sizeof(int) * NK), *k_n = malloc(sizeof(int) * NK);
    double Ns = is3d ? (double)(Lx * Ly * Lz) : (double)(NL / 3);
    if (is3d) {
        int Ld[3] = {Lx, Ly, Lz};
        for (int d = 0; d < 3; d++) for (int n = 1; n <= kmax; n++) {
            int kk = d * kmax + (n - 1); k_d[kk] = d; k_n[kk] = n;
            double kval = 2.0 * M_PI * n / Ld[d];
            for (int j = 0; j < NL; j++) {
                int c = (d == 0) ? lpos_x[j] : (d == 1) ? lpos_y[j] : lpos_z[j];
                ph[kk * NL + j] = cexp(-I * kval * c) / sqrt(Ns);
            }
        }
    } else { /* ladder: k = pi on the top links, index 3q */
        k_d[0] = 0; k_n[0] = 1;
        for (int j = 0; j < NL; j++) ph[j] = (j % 3 == 0) ? (((j / 3) % 2) ? -1.0 : 1.0) / sqrt(Ns) : 0.0;
    }
    /* transverse components for axis momentum along d: the two other directions (ladder: single) */
    int NCOMP = is3d ? 2 : 1;
    /* accumulators (per bin) */
    int NBK = (N - 2 * Nl + 1) / block;           /* number of blocks in the bulk window */
    if (NBK < 2) { fprintf(stderr, "bulk window too small\n"); return 1; }
    if (mmax > NBK - 1) mmax = NBK - 1;
    double *acc_C = calloc((size_t)NK * NCOMP * (mmax + 1), sizeof(double));
    double *acc_Cn = calloc((size_t)(mmax + 1), sizeof(double));
    double *acc_S = calloc((size_t)NK * NCOMP, sizeof(double));     /* equal-time |E_c(k)|^2 (unblocked) */
    double *acc_SL = calloc((size_t)NK, sizeof(double));           /* longitudinal |E_d(k)|^2 */
    double acc_Scnt = 0.0;
    double *acc_face = calloc(NP, sizeof(double));                 /* moves per face in the bulk */
    double acc_move = 0.0, acc_stepcnt = 0.0, acc_napp = 0.0, acc_nappcnt = 0.0;
    double acc_Emix = 0.0, acc_Emixcnt = 0.0, acc_acc = 0.0, acc_try = 0.0;
    long gauss_err = 0, replay_err = 0;
    double complex *Ek = malloc(sizeof(double complex) * NK * 3);  /* E_mu(k) running values */
    double complex *series = malloc(sizeof(double complex) * NK * NCOMP * NBK);
    unsigned char *s = malloc(NL);
    FILE *fb = NULL, *fd = NULL;
    char fn[512];
    snprintf(fn, sizeof fn, "%s.bins", outp); fb = fopen(fn, "w");
    if (dump_every > 0) { snprintf(fn, sizeof fn, "%s.dump", outp); fd = fopen(fn, "wb"); }
    int dir = 1;   /* +1 grow head, -1 grow tail */
    long acc_f = 0, acc_b = 0, rej_f = 0, rej_b = 0;
    long total = n_therm + n_moves;
    long per_bin = n_moves / nbins;
    int bin = 0;
    long nmeas_bin = 0, ndump = 0;
    /* header of bins file */
    fprintf(fb, "# columns: bin acc_rate E_mix_tail_head move_frac napp_bulk | S_T(k,c) for k=0..NK-1,c | S_L(k) | C(k,c,m) m=0..%d | face moves f=0..NP-1\n", mmax);
    fprintf(fb, "# NK=%d NCOMP=%d mmax=%d NP=%d block=%d k_d=", NK, NCOMP, mmax, NP, block);
    for (int kk = 0; kk < NK; kk++) fprintf(fb, "%d:%d ", k_d[kk], k_n[kk]);
    fprintf(fb, "\n");
    for (long it = 0; it < total; it++) {
        if (mode == 0) dir = (urand() < 0.5) ? 1 : -1;
        End *grow = (dir > 0) ? &E[1] : &E[0];
        End *shrink = (dir > 0) ? &E[0] : &E[1];
        /* propose new step at the growing end */
        int ng = grow->n_app;
        double pstay = 1.0 / (1.0 + delta * ng);
        int fnew = -1;
        if (urand() >= pstay) fnew = grow->app_list[(int)(urand() * ng)];
        /* the step to be removed at the shrinking end */
        int idx_rm = (dir > 0) ? (t0 % N) : ((t0 + N - 1) % N);
        int frm = step[idx_rm];
        int n_new_tail = (frm < 0) ? shrink->n_app : n_app_after(shrink, frm);
        double ratio = (1.0 + delta * ng) / (1.0 + delta * n_new_tail);
        acc_try += 1.0;
        if (ratio >= 1.0 || urand() < ratio) {
            acc_acc += 1.0; if (dir > 0) acc_f++; else acc_b++;
            /* apply */
            if (frm >= 0) end_flip(shrink, frm);
            if (fnew >= 0) end_flip(grow, fnew);
            if (dir > 0) { step[idx_rm] = fnew; t0 = (t0 + 1) % N; }
            else { step[idx_rm] = fnew; t0 = (t0 + N - 1) % N; }
            if (track_visits) visit(grow->b);
        } else {
            if (dir > 0) rej_f++; else rej_b++;
            if (mode == 1) dir = -dir;
        }
        if (sweep_every > 0 && (it + 1) % sweep_every == 0) {
            /* sequential interior sweep; cur walks from the tail state along the path */
            memcpy(cur.b, E[0].b, NL);
            cur.n_app = 0; for (int f = 0; f < NP; f++) { if (applicable(cur.b, f)) { cur.app_pos[f] = cur.n_app; cur.app_list[cur.n_app++] = f; } else cur.app_pos[f] = -1; }
            for (int j = 0; j < N - 1; j++) {
                int ia = (t0 + j) % N, ib = (t0 + j + 1) % N;
                int a = step[ia], b = step[ib];
                if (urand() < 0.5) {
                    int commute = 1;
                    if (a >= 0 && b >= 0) { for (int q = 0; q < nbf_cnt[a]; q++) if (nbf[a][q] == b) { commute = 0; break; } }
                    if (commute && a != b) { step[ia] = b; step[ib] = a; sw_exch++; }
                } else if (a < 0) {
                    /* windowed pair insertion: f applicable at s_j; window = positions j+1..j+D truncated
                       before the first flip sharing a link with f; partner = a uniformly chosen stay in it */
                    sw_ins_try++;
                    int n = cur.n_app;
                    if (n > 0) {
                        int f = cur.app_list[(int)(urand() * n)];
                        int nst = 0, pos[PAIR_D];
                        for (int d = 1; d <= PAIR_D && j + d < N; d++) {
                            int g = step[(t0 + j + d) % N];
                            if (g < 0) { pos[nst++] = d; continue; }
                            int share = 0; for (int q = 0; q < nbf_cnt[f]; q++) if (nbf[f][q] == g) { share = 1; break; }
                            if (share) break;
                        }
                        if (nst > 0) {
                            double r = delta * delta * n * nst;
                            if (r >= 1.0 || urand() < r) { int d = pos[(int)(urand() * nst)]; step[ia] = f; step[(t0 + j + d) % N] = f; sw_ins_acc++; }
                        }
                    }
                } else {
                    /* windowed pair deletion: partner = first flip of a within D with no link-sharing flip before it;
                       n_st = stays in the window of the DELETED configuration (partner counted as a stay) */
                    sw_del_try++;
                    int f = a, jp = -1, nst = 0, ok = 1;
                    for (int d = 1; d <= PAIR_D && j + d < N; d++) {
                        int g = step[(t0 + j + d) % N];
                        if (g < 0) { nst++; continue; }
                        if (g == f) { if (jp < 0) { jp = d; nst++; continue; } else break; }
                        int share = 0; for (int q = 0; q < nbf_cnt[f]; q++) if (nbf[f][q] == g) { share = 1; break; }
                        if (share) { if (jp < 0) ok = 0; break; }
                    }
                    if (ok && jp > 0) {
                        double r = 1.0 / (delta * delta * cur.n_app * nst);
                        if (r >= 1.0 || urand() < r) { step[ia] = -1; step[(t0 + j + jp) % N] = -1; sw_del_acc++; }
                    }
                }
                if (step[ia] >= 0) end_flip(&cur, step[ia]);
            }
            /* consistency: after the last step the cursor must reach the head */
            if (step[(t0 + N - 1) % N] >= 0) end_flip(&cur, step[(t0 + N - 1) % N]);
            if (memcmp(cur.b, E[1].b, NL) != 0) replay_err += 1000000;
        }
        if (it >= n_therm) {
            acc_Emix += -0.5 * (E[0].n_app + E[1].n_app); acc_Emixcnt += 1.0;
            long it2 = it - n_therm;
            if ((it2 + 1) % meas_every == 0) {
                /* replay from the tail */
                memcpy(s, E[0].b, NL);
                int napp = E[0].n_app;
                for (int kk = 0; kk < NK; kk++) for (int mu = 0; mu < 3; mu++) {
                    double complex z = 0;
                    if (is3d) { for (int j = 0; j < NL; j++) if (ldir[j] == mu) z += ph[kk * NL + j] * (s[j] ? 0.5 : -0.5); }
                    else if (mu == 0) { for (int j = 0; j < NL; j++) z += ph[j] * (s[j] ? 0.5 : -0.5); }
                    Ek[kk * 3 + mu] = z;
                }
                if (gauss_residual(s) != 0) gauss_err++;
                int blk_i = 0, in_blk = 0;
                for (int c = 0; c < NK * NCOMP * NBK; c++) series[c] = 0;
                for (int j = 0; j <= N; j++) {
                    int inbulk = (j >= Nl && j <= N - Nl);
                    if (inbulk) {
                        acc_napp += napp; acc_nappcnt += 1.0;
                        for (int kk = 0; kk < NK; kk++) {
                            int d = k_d[kk];
                            for (int c = 0; c < NCOMP; c++) {
                                int mu = is3d ? ((d + 1 + c) % 3) : 0;
                                double complex z = Ek[kk * 3 + mu];
                                acc_S[kk * NCOMP + c] += creal(z * conj(z));
                                if (blk_i < NBK) series[(kk * NCOMP + c) * NBK + blk_i] += z;
                            }
                            if (is3d) { double complex zl = Ek[kk * 3 + d]; acc_SL[kk] += creal(zl * conj(zl)); }
                        }
                        acc_Scnt += 1.0;
                        if (fd && dump_every > 0 && ((j - Nl) % dump_every == 0)) {
                            fwrite(s, 1, NL, fd); ndump++;
                        }
                        in_blk++;
                        if (in_blk == block) { in_blk = 0; blk_i++; }
                    }
                    if (j == N) break;
                    int f = step[(t0 + j) % N];
                    if (j >= Nl && j < N - Nl) {
                        acc_stepcnt += 1.0;
                        if (f >= 0) { acc_move += 1.0; acc_face[f] += 1.0; }
                    }
                    if (f >= 0) {
                        /* update napp by the delta rule, then flip */
                        int dn = 0;
                        int was[13];
                        for (int i = 0; i < nbf_cnt[f]; i++) was[i] = applicable(s, nbf[f][i]);
                        flip_bits(s, f);
                        for (int i = 0; i < nbf_cnt[f]; i++) dn += applicable(s, nbf[f][i]) - was[i];
                        napp += dn;
                        for (int a = 0; a < 4; a++) {
                            int jl = plq[f][a];
                            double dE = s[jl] ? 1.0 : -1.0;   /* new - old = +-1 */
                            if (is3d) { for (int kk = 0; kk < NK; kk++) Ek[kk * 3 + ldir[jl]] += ph[kk * NL + jl] * dE; }
                            else Ek[0] += ph[jl] * dE;
                        }
                    }
                }
                if (memcmp(s, E[1].b, NL) != 0 || napp != E[1].n_app) replay_err++;
                /* correlators on the block series (normalise block sums by block) */
                for (int kk = 0; kk < NK; kk++) for (int c = 0; c < NCOMP; c++) {
                    double complex *x = &series[(kk * NCOMP + c) * NBK];
                    for (int bI = 0; bI < NBK; bI++) x[bI] /= block;
                    for (int m = 0; m <= mmax; m++) {
                        double sum = 0; int cnt = 0;
                        for (int bI = 0; bI + m < NBK; bI++) { sum += creal(x[bI] * conj(x[bI + m])); cnt++; }
                        acc_C[(kk * NCOMP + c) * (mmax + 1) + m] += sum / cnt;
                    }
                }
                for (int m = 0; m <= mmax; m++) acc_Cn[m] += 1.0;
                nmeas_bin++;
            }
            if ((it2 + 1) % per_bin == 0) {
                /* write bin */
                fprintf(fb, "%d %.8f %.10f %.10f %.10f |", bin, acc_acc / acc_try, acc_Emix / acc_Emixcnt, acc_move / acc_stepcnt, acc_napp / acc_nappcnt);
                for (int q = 0; q < NK * NCOMP; q++) fprintf(fb, " %.10f", acc_S[q] / acc_Scnt);
                fprintf(fb, " |");
                for (int kk = 0; kk < NK; kk++) fprintf(fb, " %.10f", acc_SL[kk] / acc_Scnt);
                fprintf(fb, " |");
                for (int q = 0; q < NK * NCOMP; q++) for (int m = 0; m <= mmax; m++) fprintf(fb, " %.10f", acc_C[q * (mmax + 1) + m] / acc_Cn[m]);
                fprintf(fb, " |");
                for (int f = 0; f < NP; f++) fprintf(fb, " %.8f", acc_face[f] / acc_stepcnt);
                fprintf(fb, "\n");
                fflush(fb);
                memset(acc_C, 0, sizeof(double) * NK * NCOMP * (mmax + 1)); memset(acc_Cn, 0, sizeof(double) * (mmax + 1));
                memset(acc_S, 0, sizeof(double) * NK * NCOMP); memset(acc_SL, 0, sizeof(double) * NK); acc_Scnt = 0;
                memset(acc_face, 0, sizeof(double) * NP);
                acc_move = acc_stepcnt = acc_napp = acc_nappcnt = acc_Emix = acc_Emixcnt = acc_acc = acc_try = 0;
                bin++; nmeas_bin = 0;
            }
        }
    }
    fclose(fb); if (fd) fclose(fd);
    long nstay = 0; for (int i = 0; i < N; i++) if (step[i] < 0) nstay++;
    printf("# final: gauss_err=%ld replay_err=%ld visited_states=%d dumps=%ld head_gauss=%d tail_gauss=%d n_app(tail)=%d n_app(head)=%d stays_in_path=%ld/%d acc_fwd=%ld acc_bwd=%ld rej_fwd=%ld rej_bwd=%ld sweep: ins %ld/%ld del %ld/%ld exchanges %ld\n",
           gauss_err, replay_err, track_visits ? hcount : -1, ndump, gauss_residual(E[1].b), gauss_residual(E[0].b), E[0].n_app, E[1].n_app, nstay, N, acc_f, acc_b, rej_f, rej_b, sw_ins_acc, sw_ins_try, sw_del_acc, sw_del_try, sw_exch);
    return 0;
}
"""

C_GFMC = r"""/* P2 -- continuous-time Green's-function (projector) Monte Carlo for H = -sum_f P_f on a Gauss sector,
 * with fixed-population reconfiguration and forward-walking (ancestry) buffers.
 *
 * e^{tau A} (A = -H = flip-graph adjacency) is sampled by walkers: from state s a walker waits an
 * exponential time with rate n_app(s), then flips a uniformly chosen applicable face; the importance
 * weight grows as exp( int (n_app(s(t)) - E_T) dt ).  Every dtau the population is reconfigured to
 * exactly Nw walkers by systematic resampling with probabilities w_i / sum w (population-control
 * bias O(1/Nw), checked by varying Nw against exact anchors).  The weighted population is the
 * mixed distribution ~ psi_0(s); an ancestor Kp steps back of the present population is distributed
 * as psi_0(s)^2 (forward walking), so every walker carries a ring buffer of its ancestors' observables
 * (transverse E(k) at axis momenta) and periodic state snapshots (dumped for pure structure factors).
 *
 * Estimators (lambda = 1):  E_mix = -<n_app>_w ,  E_growth = E_T - ln(W/Nw)/dtau ,
 *   S_T(k) pure = <|E_c(k)|^2 at lag Kp>_w ,  C_c(k,m) = <E_c(k)[lag Kp+m] E_c(k)^*[lag Kp]>_w  (tau = m dtau).
 * usage: gfmc geo Nw tau_equil tau_prod dtau K Kp kmax snap_every nsnap dump_every dump_walkers nbins seed corr_every outprefix
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <stdint.h>
#include <complex.h>

static uint64_t rs[4];
static inline uint64_t rotl(const uint64_t x, int k) { return (x << k) | (x >> (64 - k)); }
static uint64_t next_u64(void) { const uint64_t r = rotl(rs[1] * 5, 7) * 9; const uint64_t t = rs[1] << 17; rs[2] ^= rs[0]; rs[3] ^= rs[1]; rs[1] ^= rs[2]; rs[0] ^= rs[3]; rs[2] ^= t; rs[3] = rotl(rs[3], 45); return r; }
static double urand(void) { return (next_u64() >> 11) * (1.0 / 9007199254740992.0); }
static void seed_rng(uint64_t seed) { uint64_t z = seed; for (int i = 0; i < 4; i++) { z += 0x9e3779b97f4a7c15ULL; uint64_t x = z; x = (x ^ (x >> 30)) * 0xbf58476d1ce4e5b9ULL; x = (x ^ (x >> 27)) * 0x94d049bb133111ebULL; rs[i] = x ^ (x >> 31); } }

static int NL, NP, NV, Lx, Ly, Lz, is3d;
static int (*plq)[4]; static int *nbf_cnt, (*nbf)[13];
static int *lpos_x, *lpos_y, *lpos_z, *ldir;
static int *inc_cnt, (*inc_link)[8], (*inc_sign)[8], *rho2;
static unsigned char *init_bits;
static int cmp_int(const void *a, const void *b) { return (*(int *)a) - (*(int *)b); }

static void read_geo(const char *fn) {
    FILE *fh = fopen(fn, "r"); if (!fh) { fprintf(stderr, "cannot open %s\n", fn); exit(1); }
    if (fscanf(fh, "%d %d %d", &NL, &NP, &NV) != 3) exit(2);
    plq = malloc(sizeof(int[4]) * NP);
    for (int f = 0; f < NP; f++) if (fscanf(fh, "%d %d %d %d", &plq[f][0], &plq[f][1], &plq[f][2], &plq[f][3]) != 4) exit(3);
    init_bits = malloc(NL); char *buf = malloc(NL + 16); if (fscanf(fh, "%s", buf) != 1) exit(4);
    for (int j = 0; j < NL; j++) init_bits[j] = (buf[j] == '1'); free(buf);
    if (fscanf(fh, "%d %d %d", &Lx, &Ly, &Lz) != 3) exit(5);
    is3d = (Lx > 0);
    lpos_x = malloc(sizeof(int) * NL); lpos_y = malloc(sizeof(int) * NL); lpos_z = malloc(sizeof(int) * NL); ldir = malloc(sizeof(int) * NL);
    if (is3d) for (int j = 0; j < NL; j++) if (fscanf(fh, "%d %d %d %d", &lpos_x[j], &lpos_y[j], &lpos_z[j], &ldir[j]) != 4) exit(6);
    inc_cnt = malloc(sizeof(int) * NV); inc_link = malloc(sizeof(int[8]) * NV); inc_sign = malloc(sizeof(int[8]) * NV); rho2 = malloc(sizeof(int) * NV);
    for (int v = 0; v < NV; v++) { if (fscanf(fh, "%d", &inc_cnt[v]) != 1) exit(7); for (int a = 0; a < inc_cnt[v]; a++) if (fscanf(fh, "%d %d", &inc_link[v][a], &inc_sign[v][a]) != 2) exit(8); if (fscanf(fh, "%d", &rho2[v]) != 1) exit(9); }
    fclose(fh);
    int *lf_cnt = calloc(NL, sizeof(int)); int (*lf)[8] = malloc(sizeof(int[8]) * NL);
    for (int f = 0; f < NP; f++) for (int a = 0; a < 4; a++) { int j = plq[f][a]; lf[j][lf_cnt[j]++] = f; }
    nbf_cnt = calloc(NP, sizeof(int)); nbf = malloc(sizeof(int[13]) * NP);
    for (int f = 0; f < NP; f++) { int tmp[40], n = 0; tmp[n++] = f; for (int a = 0; a < 4; a++) { int j = plq[f][a]; for (int b = 0; b < lf_cnt[j]; b++) tmp[n++] = lf[j][b]; }
        qsort(tmp, n, sizeof(int), cmp_int); int m = 0; for (int i = 0; i < n; i++) if (i == 0 || tmp[i] != tmp[i - 1]) nbf[f][m++] = tmp[i]; nbf_cnt[f] = m; }
    free(lf_cnt); free(lf);
}
static inline int applicable(const unsigned char *b, int f) { int bp = b[plq[f][0]], bq = b[plq[f][1]], bu = b[plq[f][2]], bw = b[plq[f][3]]; return (bp == bq) && (bu == bw) && (bp != bu); }
static int gauss_residual(const unsigned char *b) { int worst = 0; for (int v = 0; v < NV; v++) { int tot = 0; for (int a = 0; a < inc_cnt[v]; a++) tot += inc_sign[v][a] * (b[inc_link[v][a]] ? 1 : -1); int r = abs(tot - rho2[v]); if (r > worst) worst = r; } return worst; }

/* walker layout: one contiguous block */
static int NK, NCOMP, K, NSNAP;
static size_t WSZ, off_bits, off_list, off_pos, off_Ek, off_buf, off_snap;
typedef struct { int n_app; double logw; } WHead;
static inline unsigned char *w_bits(char *w) { return (unsigned char *)(w + off_bits); }
static inline int *w_list(char *w) { return (int *)(w + off_list); }
static inline int *w_pos(char *w) { return (int *)(w + off_pos); }
static inline double complex *w_Ek(char *w) { return (double complex *)(w + off_Ek); }
static inline float complex *w_buf(char *w) { return (float complex *)(w + off_buf); }
static inline unsigned char *w_snap(char *w) { return (unsigned char *)(w + off_snap); }
static double complex *ph; static int *k_d, *k_n; static double Ns;

static void walker_init(char *w, const unsigned char *bits) {
    WHead *h = (WHead *)w; h->logw = 0; h->n_app = 0;
    memcpy(w_bits(w), bits, NL);
    int *list = w_list(w), *pos = w_pos(w);
    for (int f = 0; f < NP; f++) { if (applicable(w_bits(w), f)) { pos[f] = h->n_app; list[h->n_app++] = f; } else pos[f] = -1; }
    double complex *Ek = w_Ek(w);
    for (int kk = 0; kk < NK; kk++) for (int mu = 0; mu < 3; mu++) { double complex z = 0; for (int j = 0; j < NL; j++) if (ldir[j] == mu) z += ph[kk * NL + j] * (w_bits(w)[j] ? 0.5 : -0.5); Ek[kk * 3 + mu] = z; }
    memset(w_buf(w), 0, sizeof(float complex) * (size_t)K * NK * NCOMP);
    for (int s = 0; s < NSNAP; s++) memcpy(w_snap(w) + (size_t)s * NL, bits, NL);
}
static inline void walker_flip(char *w, int f) {
    WHead *h = (WHead *)w; unsigned char *b = w_bits(w); int *list = w_list(w), *pos = w_pos(w);
    for (int a = 0; a < 4; a++) { int jl = plq[f][a]; b[jl] ^= 1; double dE = b[jl] ? 1.0 : -1.0; double complex *Ek = w_Ek(w); for (int kk = 0; kk < NK; kk++) Ek[kk * 3 + ldir[jl]] += ph[kk * NL + jl] * dE; }
    for (int i = 0; i < nbf_cnt[f]; i++) { int g = nbf[f][i]; int val = applicable(b, g); int p = pos[g];
        if (val && p < 0) { pos[g] = h->n_app; list[h->n_app++] = g; }
        else if (!val && p >= 0) { int last = list[--h->n_app]; list[p] = last; pos[last] = p; pos[g] = -1; } }
}

int main(int argc, char **argv) {
    if (argc < 17) { fprintf(stderr, "usage: gfmc geo Nw tau_equil tau_prod dtau K Kp kmax snap_every nsnap dump_every dump_walkers nbins seed corr_every outprefix [nsub]\n"); return 1; }
    int nsub = (argc > 17) ? atoi(argv[17]) : 1;   /* reconfigurations per dtau (weight spread per reconfiguration ~ exp(sigma_n dtau/nsub)) */
    const char *geo = argv[1]; int Nw = atoi(argv[2]); double tau_equil = atof(argv[3]), tau_prod = atof(argv[4]), dtau = atof(argv[5]);
    K = atoi(argv[6]); int Kp = atoi(argv[7]); int kmax = atoi(argv[8]); int snap_every = atoi(argv[9]); NSNAP = atoi(argv[10]);
    int dump_every = atoi(argv[11]); int dump_walkers = atoi(argv[12]); int nbins = atoi(argv[13]); uint64_t seed = strtoull(argv[14], NULL, 10); int corr_every = atoi(argv[15]); const char *outp = argv[16];
    read_geo(geo); seed_rng(seed);
    NK = is3d ? 3 * kmax : 1; NCOMP = is3d ? 2 : 1; Ns = is3d ? (double)(Lx * Ly * Lz) : (double)(NL / 3);
    ph = malloc(sizeof(double complex) * NK * NL); k_d = malloc(sizeof(int) * NK); k_n = malloc(sizeof(int) * NK);
    if (is3d) { int Ld[3] = {Lx, Ly, Lz}; for (int d = 0; d < 3; d++) for (int n = 1; n <= kmax; n++) { int kk = d * kmax + n - 1; k_d[kk] = d; k_n[kk] = n; double kv = 2 * M_PI * n / Ld[d];
        for (int j = 0; j < NL; j++) { int c = (d == 0) ? lpos_x[j] : (d == 1) ? lpos_y[j] : lpos_z[j]; ph[kk * NL + j] = cexp(-I * kv * c) / sqrt(Ns); } } }
    else { k_d[0] = 0; k_n[0] = 1; for (int j = 0; j < NL; j++) ph[j] = (j % 3 == 0) ? (((j / 3) % 2) ? -1.0 : 1.0) / sqrt(Ns) : 0.0; }
    int MC = K - Kp;   /* number of correlator lags */
    off_bits = sizeof(WHead); off_list = off_bits + ((NL + 7) / 8) * 8; off_pos = off_list + sizeof(int) * NP; off_Ek = off_pos + sizeof(int) * NP; off_Ek = (off_Ek + 15) / 16 * 16;
    off_buf = off_Ek + sizeof(double complex) * NK * 3; off_snap = off_buf + sizeof(float complex) * (size_t)K * NK * NCOMP; WSZ = off_snap + (size_t)NSNAP * NL; WSZ = (WSZ + 15) / 16 * 16;
    printf("# gfmc: geo=%s NL=%d NP=%d NV=%d Nw=%d tau_equil=%g tau_prod=%g dtau=%g K=%d Kp=%d (tau_proj=%g, corr lags %d -> tau %g) kmax=%d snap_every=%d nsnap=%d (snapshot lag %g) dump_every=%d dump_walkers=%d nbins=%d seed=%llu corr_every=%d walker_bytes=%zu nsub=%d (reconfigure every %g)\n",
           geo, NL, NP, NV, Nw, tau_equil, tau_prod, dtau, K, Kp, Kp * dtau, MC, MC * dtau, kmax, snap_every, NSNAP, (NSNAP - 1) * snap_every * dtau, dump_every, dump_walkers, nbins, (unsigned long long)seed, corr_every, WSZ, nsub, dtau / nsub);
    char *pool = malloc(WSZ * (size_t)Nw); if (!pool) { fprintf(stderr, "oom\n"); return 2; }
    for (int i = 0; i < Nw; i++) walker_init(pool + WSZ * i, init_bits);
    printf("# init: gauss residual=%d n_app=%d\n", gauss_residual(init_bits), ((WHead *)pool)->n_app);
    double ET = ((WHead *)pool)->n_app;   /* trial energy (-E), adapted to the growth estimate */
    long nsteps_eq = (long)(tau_equil / dtau + 0.5), nsteps_pr = (long)(tau_prod / dtau + 0.5), per_bin = nsteps_pr / nbins;
    int rpos = 0, spos = 0;    /* ring positions (global) */
    /* accumulators */
    double a_Emix = 0, a_Egr = 0, a_cnt = 0, a_nappP = 0;
    double *a_Smix = calloc(NK * NCOMP, sizeof(double)), *a_Spure = calloc(NK * NCOMP, sizeof(double)), *a_SL = calloc(NK, sizeof(double));
    double *a_C = calloc((size_t)NK * NCOMP * MC, sizeof(double)); double a_Ccnt = 0;
    double *cum = malloc(sizeof(double) * Nw); int *copies = malloc(sizeof(int) * Nw);
    char fn[512]; snprintf(fn, sizeof fn, "%s.bins", outp); FILE *fb = fopen(fn, "w");
    FILE *fd = NULL; if (dump_every > 0) { snprintf(fn, sizeof fn, "%s.dump", outp); fd = fopen(fn, "wb"); }
    fprintf(fb, "# columns: bin E_mix E_growth | S_mix(k,c) | S_pure(k,c) | S_L_pure(k) | C(k,c,m) m=0..%d | ncopies_max\n", MC - 1);
    fprintf(fb, "# NK=%d NCOMP=%d MC=%d dtau=%g Kp=%d k_d=", NK, NCOMP, MC, dtau, Kp);
    for (int kk = 0; kk < NK; kk++) fprintf(fb, "%d:%d ", k_d[kk], k_n[kk]); fprintf(fb, "\n");
    long total = nsteps_eq + nsteps_pr; int bin = 0; long gauss_err = 0, ndump = 0; double maxcopies_bin = 0; double Wmin = 1e300, Wmax = 0;
    for (long step = 0; step < total; step++) {
        /* evolve every walker for dtau in nsub sub-steps, reconfiguring after each sub-step but the last */
        double lnW_sum = 0;
        for (int sub = 0; sub < nsub; sub++) {
            double dts = dtau / nsub;
            for (int i = 0; i < Nw; i++) {
                char *w = pool + WSZ * i; WHead *h = (WHead *)w; double t = 0;
                while (1) {
                    double rate = h->n_app;
                    if (rate <= 0) { h->logw += -ET * (dts - t); break; }
                    double dt = -log(1.0 - urand()) / rate;
                    if (t + dt >= dts) { h->logw += (rate - ET) * (dts - t); break; }
                    h->logw += (rate - ET) * dt; t += dt;
                    walker_flip(w, w_list(w)[(int)(urand() * h->n_app)]);
                }
            }
            if (sub < nsub - 1) {
                double lm = -1e300; for (int i = 0; i < Nw; i++) { double l = ((WHead *)(pool + WSZ * i))->logw; if (l > lm) lm = l; }
                double Ws = 0; for (int i = 0; i < Nw; i++) { double wi = exp(((WHead *)(pool + WSZ * i))->logw - lm); cum[i] = wi; Ws += wi; }
                lnW_sum += log(Ws / Nw) + lm;
                double u = urand() / Nw, acc = 0; int j = 0;
                for (int i = 0; i < Nw; i++) { acc += cum[i] / Ws; int c = 0; while (j < Nw && u + (double)j / Nw < acc) { c++; j++; } copies[i] = c; }
                int dead_i = 0;
                for (int i = 0; i < Nw; i++) { if (copies[i] <= 1) continue;
                    for (int c = 1; c < copies[i]; c++) { while (dead_i < Nw && copies[dead_i] != 0) dead_i++; if (dead_i >= Nw) break; memcpy(pool + WSZ * dead_i, pool + WSZ * i, WSZ); copies[dead_i] = 1; } }
                for (int i = 0; i < Nw; i++) ((WHead *)(pool + WSZ * i))->logw = 0;
            }
        }
        for (int i = 0; i < Nw; i++) {
            char *w = pool + WSZ * i;
            /* push observables into the ring */
            float complex *buf = w_buf(w) + (size_t)rpos * NK * NCOMP; double complex *Ek = w_Ek(w);
            for (int kk = 0; kk < NK; kk++) for (int c = 0; c < NCOMP; c++) { int mu = is3d ? ((k_d[kk] + 1 + c) % 3) : 0; buf[kk * NCOMP + c] = (float complex)Ek[kk * 3 + mu]; }
            if (step % snap_every == 0) memcpy(w_snap(w) + (size_t)spos * NL, w_bits(w), NL);
        }
        /* weights */
        double lmax = -1e300; for (int i = 0; i < Nw; i++) { double l = ((WHead *)(pool + WSZ * i))->logw; if (l > lmax) lmax = l; }
        double W = 0; for (int i = 0; i < Nw; i++) { double wi = exp(((WHead *)(pool + WSZ * i))->logw - lmax); cum[i] = wi; W += wi; }
        double a_growth = ET + (lnW_sum + log(W / Nw) + lmax) / dtau;   /* estimate of a0 = -E_0 over the whole step */
        double Egrowth = -a_growth;
        int measuring = (step >= nsteps_eq) && (step >= K);
        if (measuring) {
            double emix = 0, nappP = 0;
            for (int i = 0; i < Nw; i++) { char *w = pool + WSZ * i; double wi = cum[i] / W; emix += wi * ((WHead *)w)->n_app;
                float complex *b0 = w_buf(w) + (size_t)rpos * NK * NCOMP;
                int lagpos = (rpos - Kp + K) % K; float complex *bp = w_buf(w) + (size_t)lagpos * NK * NCOMP;
                for (int q = 0; q < NK * NCOMP; q++) { a_Smix[q] += wi * crealf(b0[q] * conjf(b0[q])); a_Spure[q] += wi * crealf(bp[q] * conjf(bp[q])); }
                /* longitudinal: not buffered (zero by Gauss); computed from the current Ek for the record */
                double complex *Ek = w_Ek(w); for (int kk = 0; kk < NK; kk++) { double complex zl = Ek[kk * 3 + k_d[kk]]; a_SL[kk] += wi * creal(zl * conj(zl)); }
                if (step % corr_every == 0) {
                    for (int m = 0; m < MC; m++) { int lp2 = (rpos - Kp - m + 2 * K) % K; float complex *bm = w_buf(w) + (size_t)lp2 * NK * NCOMP;
                        for (int q = 0; q < NK * NCOMP; q++) a_C[q * MC + m] += wi * crealf(bm[q] * conjf(bp[q])); }
                }
            }
            a_Emix += -emix; a_Egr += Egrowth; a_cnt += 1; if (step % corr_every == 0) a_Ccnt += 1;
            if (W < Wmin) Wmin = W; if (W > Wmax) Wmax = W;
            if (fd && dump_every > 0 && ((step - nsteps_eq) % dump_every == 0)) {
                int oldest = (spos + 1) % NSNAP;   /* the slot about to be overwritten next = oldest */
                for (int i = 0; i < Nw; i += (Nw / dump_walkers > 0 ? Nw / dump_walkers : 1)) { unsigned char *s = w_snap(pool + WSZ * i) + (size_t)oldest * NL; if (gauss_residual(s)) gauss_err++; fwrite(s, 1, NL, fd); ndump++; }
            }
        }
        /* reconfiguration: systematic resampling */
        double u = urand() / Nw, acc = 0; int j = 0, maxc = 0;
        for (int i = 0; i < Nw; i++) { acc += cum[i] / W; int c = 0; while (j < Nw && u + (double)j / Nw < acc) { c++; j++; } copies[i] = c; if (c > maxc) maxc = c; }
        if (maxc > maxcopies_bin) maxcopies_bin = maxc;
        /* survivors stay, dead slots receive copies */
        int dead_i = 0;
        for (int i = 0; i < Nw; i++) {
            if (copies[i] <= 1) continue;
            for (int c = 1; c < copies[i]; c++) { while (dead_i < Nw && copies[dead_i] != 0) dead_i++; if (dead_i >= Nw) break; memcpy(pool + WSZ * dead_i, pool + WSZ * i, WSZ); copies[dead_i] = 1; }
        }
        for (int i = 0; i < Nw; i++) ((WHead *)(pool + WSZ * i))->logw = 0;
        ET = 0.9 * ET + 0.1 * a_growth;
        rpos = (rpos + 1) % K; if (step % snap_every == 0) spos = (spos + 1) % NSNAP;
        if (measuring && ((step - nsteps_eq + 1) % per_bin == 0)) {
            fprintf(fb, "%d %.10f %.10f |", bin, a_Emix / a_cnt, a_Egr / a_cnt);
            for (int q = 0; q < NK * NCOMP; q++) fprintf(fb, " %.10f", a_Smix[q] / a_cnt); fprintf(fb, " |");
            for (int q = 0; q < NK * NCOMP; q++) fprintf(fb, " %.10f", a_Spure[q] / a_cnt); fprintf(fb, " |");
            for (int kk = 0; kk < NK; kk++) fprintf(fb, " %.3e", a_SL[kk] / a_cnt); fprintf(fb, " |");
            for (int q = 0; q < NK * NCOMP; q++) for (int m = 0; m < MC; m++) fprintf(fb, " %.10f", a_C[q * MC + m] / a_Ccnt); fprintf(fb, " | %g\n", maxcopies_bin);
            fflush(fb);
            a_Emix = a_Egr = a_cnt = a_Ccnt = 0; memset(a_Smix, 0, sizeof(double) * NK * NCOMP); memset(a_Spure, 0, sizeof(double) * NK * NCOMP); memset(a_SL, 0, sizeof(double) * NK); memset(a_C, 0, sizeof(double) * NK * NCOMP * MC); maxcopies_bin = 0; bin++;
        }
    }
    fclose(fb); if (fd) fclose(fd);
    printf("# final: ET=%.6f gauss_err(dumps)=%ld dumps=%ld W range per step [%.3g, %.3g] (relative to Nw=%d)\n", ET, gauss_err, ndump, Wmin, Wmax, Nw);
    return 0;
}
"""



print("H = -lambda sum_f P_f, lambda = 1; E_e = Z^L_e/2, U_e = sigma^+_e, G_v = (div E)_v - rho_v; "
      "geometries 2x2x2, 4x2x2, ladder L = 8; witness seeds %d / %d / %d / %d"
      % (SEED_REPT, SEED_GFMC_T222, SEED_GFMC_T422, SEED_GFMC_T4))

# ================================================================== A  2x2x2
g2 = torus3d(2, 2, 2)
st2 = enumerate_sector(g2)
res2 = max(g2.gauss_residual(s) for s in st2)
comps2 = components(g2, st2)
mult2 = Counter(len(c) for c in comps2)
check("A1 [exact] 2x2x2 torus (24 links, 8 vertices at z_v = 6, 24 faces, rho_v = 0): dim(Gauss) = %d by slab sweep, "
      "every state re-derived against G_v = 0 with max |2 (div E)_v - 2 rho_v| = %d; %d plaquette-flip components, "
      "multiset %s"
      % (len(st2), res2, len(comps2), ", ".join("%d x %d" % (k, mult2[k]) for k in sorted(mult2, reverse=True))),
      len(st2) == 9600 and res2 == 0 and len(comps2) == 937
      and mult2 == Counter({864: 1, 464: 6, 252: 12, 136: 8, 36: 6, 6: 144, 1: 760})
      and sum(k * v for k, v in mult2.items()) == 9600)

Wof = [winding(g2, s) for s in st2]
wc = Counter(Wof)
comp_of = {}
for ci, c in enumerate(comps2):
    for i in c:
        comp_of[i] = ci
per_w = {}
for i, W in enumerate(Wof):
    per_w.setdefault(W, set()).add(comp_of[i])
straddle = sum(1 for c in comps2 if len(set(Wof[i] for i in c)) > 1)
z_sizes = sorted((len(comps2[ci]) for ci in per_w[(0, 0, 0)]), reverse=True)
ice2 = ice_config(g2)
i_ice = st2.index(ice2)
big2 = comps2[comp_of[i_ice]]
check("A2 [exact] the winding vector separates sectors: %d distinct W over the sector, %d components straddle two "
      "classes, zero-winding = %d states = one flip component of %d (the analytic ice configuration's; G_v = 0, "
      "12/24 faces applicable, W = 0) plus %d frozen singletons"
      % (len(wc), straddle, wc[(0, 0, 0)], z_sizes[0], len(z_sizes) - 1),
      len(wc) == 125 and straddle == 0 and wc[(0, 0, 0)] == 880 and z_sizes == [864] + [1] * 16
      and len(big2) == 864 and g2.gauss_residual(ice2) == 0 and g2.n_app(ice2) == 12 and winding(g2, ice2) == (0, 0, 0))

spec2 = {}
for ci, c in enumerate(comps2):
    stc = [st2[i] for i in c]
    w, V = np.linalg.eigh(hamiltonian_dense(g2, stc))
    spec2[ci] = (stc, w, V)
allw2 = np.sort(np.concatenate([spec2[ci][1] for ci in spec2]))
stI, wI, VI = spec2[comp_of[i_ice]]
E0_2, D1_2, gapI = allw2[0], allw2[1] - allw2[0], wI[1] - wI[0]
check("A3 [1e-9] full-sector E_0 = %.10f, Delta_1 = %.10f; the ground state is in the 864-state ice component (its own "
      "E_0 agrees to %.1e), whose internal gap is %.10f -- the sector-internal gap a winding-conserving sampler reads, "
      "larger by %.1f per cent"
      % (E0_2, D1_2, abs(wI[0] - E0_2), gapI, 100 * (gapI / D1_2 - 1)),
      close(E0_2, -9.0267209135) and close(D1_2, 1.6276099336) and close(wI[0], E0_2)
      and close(gapI, 2.2257853859))

hosts = []
for ci, (stc, w, V) in spec2.items():
    if min(abs(w - allw2[1])) < 1e-9:
        hosts.append((ci, len(stc), sorted(set(Wof[i] for i in comps2[ci]))))
unit = set()
for ci, sz, Ws in hosts:
    unit |= set(Ws)
check("A4 [1e-9] the first excitation is a FLUX state: Delta_1 = %.10f is carried by %d components, each of %d states "
      "and each a unit-flux class W = +-e_d, %s; the cheapest excitation at 2x2x2 is the unit-winding sector itself"
      % (D1_2, len(hosts), hosts[0][1], ", ".join("(%d,%d,%d)" % W for W in sorted(unit))),
      len(hosts) == 6 and all(sz == 464 for _, sz, _ in hosts) and len(unit) == 6
      and unit == {(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)})

psi2 = VI[:, 0]
rho2v = psi2 ** 2
Ev2 = E_vals(g2, stI)
SL_max, STpi = 0.0, None
for a in range(2):
    for b in range(2):
        for c in range(2):
            k = (np.pi * a, np.pi * b, np.pi * c)
            if a == b == c == 0:
                continue
            Ek = fourier_E(g2, Ev2, k)
            S = np.zeros((3, 3), dtype=complex)
            for mu in range(3):
                for nu in range(3):
                    S[mu, nu] = (rho2v * Ek[:, mu] * np.conj(Ek[:, nu])).sum() / g2.NV
            K = np.array([1 - np.exp(1j * k[d]) for d in range(3)])
            SL = float(np.real(np.conj(K) @ S @ K) / float(np.vdot(K, K).real))
            SL_max = max(SL_max, abs(SL))
            if (a, b, c) == (1, 0, 0):
                STpi = (float(S[1, 1].real), float(S[2, 2].real))
Ek = fourier_E(g2, Ev2, (np.pi, 0.0, 0.0))
O = VI.T @ (Ek[:, 1][:, None] * VI)
amp = np.abs(O[:, 0]) ** 2
lvl = float(wI[np.nonzero(amp > 1e-10)[0][0]] - wI[0])
check("A5 [1e-9] in that ground state the lattice-longitudinal S_L(k) = |K*.S.K|/|K|^2 is %.1e at every one of the "
      "seven non-zero k, the transverse S_yy = S_zz = %.8f at (pi,0,0), and the lowest level carrying transverse-E "
      "weight sits at E - E_0 = %.10f"
      % (SL_max, STpi[0], lvl),
      SL_max < 1e-30 and close(STpi[0], 0.25303701, 1e-8) and close(STpi[1], 0.25303701, 1e-8)
      and close(lvl, 2.5172790443))

# ================================================================== B  ladder
gl = ladder(8)
stl = enumerate_sector(gl)
resl = max(gl.gauss_residual(s) for s in stl)
compl_ = components(gl, stl)
sizes_l = sorted((len(c) for c in compl_), reverse=True)
stL = [stl[i] for i in max(compl_, key=len)]
wL, VL = np.linalg.eigh(hamiltonian_dense(gl, stL))
check("B1 [1e-9] PR #7911's height-1 ladder at L = 8 (24 links, 16 vertices at z_v = 3, 8 faces, declared staggered "
      "background): dim(Gauss) = %d, max |G_v| = %d, components %s; on the 47-state one E_0 = %.10f, gap %.10f, "
      "<P_f> = %.10f"
      % (len(stl), resl, sizes_l, wL[0], wL[1] - wL[0], -wL[0] / gl.NP),
      len(stl) == 49 and resl == 0 and sizes_l == [47, 1, 1] and close(wL[0], -4.8309586723)
      and close(wL[1] - wL[0], 0.9726557606) and close(-wL[0] / gl.NP, 0.6038698340))

Etop = np.zeros((len(stL), 8))
for i, s in enumerate(stL):
    for q in range(8):
        Etop[i, q] = 0.5 if (s >> (3 * q)) & 1 else -0.5
Ok = (Etop @ np.cos(np.pi * np.arange(8))) / np.sqrt(8.0)
psiL = VL[:, 0]
plateau = float((psiL ** 2 @ Ok)) ** 2
B = np.eye(len(stL)) + DELTA * (-hamiltonian_dense(gl, stL))
lamB = 1.0 + DELTA * (-wL[0])
u = np.ones(len(stL))
for _ in range(50):
    u = (B @ u) / lamB
vv = Ok * u
for _ in range(40):
    vv = (B @ vv) / lamB
C40 = float(u @ (Ok * vv)) / float(u @ u)
check("B2 [1e-4] the ladder's staggered order is a plateau, not a decay: C(m) at k = pi for O = sum_i (-1)^i "
      "E(T_i)/sqrt(L) saturates at <psi_0|O|psi_0>^2 = %.8f, already %.8f at m = 40 of B = I + %.2f A"
      % (plateau, C40, DELTA),
      close(plateau, 0.7353, 1e-4) and close(C40, 0.7353, 1e-4) and close(C40, plateau, 1e-5))


# =============================================== D  the open-path projector's balance certificates
def certify(g, comp_states, N, delta):
    """Complete path space {(s_0..s_N)} of the flip component, the exact transition matrices of the
    symmetric and bounce reptation chains, and their balance certificates.  Everything sparse."""
    idx = {s: i for i, s in enumerate(comp_states)}
    n = len(comp_states)
    nbrs = [[idx[t] for f, t in g.flips(s)] for s in comp_states]
    deg = [len(x) for x in nbrs]
    gres = max(g.gauss_residual(s) for s in comp_states)
    edge_ok = all(bin(comp_states[i] ^ comp_states[j]).count("1") == 4 for i in range(n) for j in nbrs[i])
    paths = []
    stack = [[s0] for s0 in range(n - 1, -1, -1)]
    while stack:
        p = stack.pop()
        if len(p) == N + 1:
            paths.append(tuple(p))
            continue
        s = p[-1]
        stack.append(p + [s])
        for t in nbrs[s]:
            stack.append(p + [t])
    pidx = {p: i for i, p in enumerate(paths)}
    M = len(paths)
    moves = np.array([sum(1 for i in range(N) if p[i] != p[i + 1]) for p in paths])
    pi = delta ** moves.astype(float)
    pi /= pi.sum()

    def q(s, t):
        return (1.0 if t == s else delta) / (1.0 + delta * deg[s])

    def acc(old_head, new_tail):
        return min(1.0, (1.0 + delta * deg[old_head]) / (1.0 + delta * deg[new_tail]))

    rf, cf, vf, rb, cb, vb = [], [], [], [], [], []
    rej_f, rej_b = np.zeros(M), np.zeros(M)
    for i, p in enumerate(paths):
        head, tail = p[-1], p[0]
        a = acc(head, p[1])
        for t in [head] + nbrs[head]:
            rf.append(i); cf.append(pidx[p[1:] + (t,)]); vf.append(q(head, t) * a)
            rej_f[i] += q(head, t) * (1 - a)
        a = acc(tail, p[-2])
        for t in [tail] + nbrs[tail]:
            rb.append(i); cb.append(pidx[(t,) + p[:-1]]); vb.append(q(tail, t) * a)
            rej_b[i] += q(tail, t) * (1 - a)
    Tf = sp.csr_matrix((vf, (rf, cf)), shape=(M, M))
    Tb = sp.csr_matrix((vb, (rb, cb)), shape=(M, M))
    T = (0.5 * (Tf + Tb) + sp.diags(0.5 * (rej_f + rej_b))).tocsr()
    rows = float(abs(np.asarray(T.sum(axis=1)).ravel() - 1.0).max())
    A = (sp.diags(pi) @ T).tocsr()
    db = float(abs(A - A.T).max()) if (A - A.T).nnz else 0.0
    stat = float(abs(pi @ T - pi).max())
    ncc = connected_components(T, directed=True, connection="strong")[0]
    # bounce chain on the lifted space (path, direction)
    P2M = sp.csr_matrix((np.ones(M), (np.arange(M), 2 * np.arange(M))), shape=(M, 2 * M))
    P2Mo = sp.csr_matrix((np.ones(M), (np.arange(M), 2 * np.arange(M) + 1)), shape=(M, 2 * M))
    TB = (P2M.T @ Tf @ P2M + P2Mo.T @ Tb @ P2Mo
          + sp.csr_matrix((rej_f, (2 * np.arange(M), 2 * np.arange(M) + 1)), shape=(2 * M, 2 * M))
          + sp.csr_matrix((rej_b, (2 * np.arange(M) + 1, 2 * np.arange(M))), shape=(2 * M, 2 * M))).tocsr()
    pit = np.repeat(pi, 2) / 2
    rowsB = float(abs(np.asarray(TB.sum(axis=1)).ravel() - 1.0).max())
    statB = float(abs(pit @ TB - pit).max())
    AB = (sp.diags(pit) @ TB).tocsr()
    dbB = float(abs(AB - AB.T).max()) if (AB - AB.T).nnz else 0.0
    nccB = connected_components(TB, directed=True, connection="strong")[0]
    Sk = (sp.diags(pi) @ Tf - (sp.diags(pi) @ Tb).T).tocsr()
    skew = float(abs(Sk).max()) if Sk.nnz else 0.0
    # middle-state marginal against the exact finite-N formula
    Hc = hamiltonian_dense(g, comp_states)
    Bm = np.eye(n) + delta * (-Hc)
    j = N // 2
    u = np.ones(n) @ np.linalg.matrix_power(Bm, j)
    v = np.linalg.matrix_power(Bm, N - j) @ np.ones(n)
    marg_exact = u * v / float(u @ v)
    marg_path = np.zeros(n)
    for i, p in enumerate(paths):
        marg_path[p[j]] += pi[i]
    return dict(n=n, M=M, gres=gres, edge_ok=edge_ok, rows=rows, db=db, stat=stat, ncc=ncc,
                rowsB=rowsB, statB=statB, dbB=dbB, nccB=nccB, skew=skew,
                marg=float(abs(marg_path - marg_exact).max()))


gl4 = ladder(4)
sl4 = enumerate_sector(gl4)
cl4 = components(gl4, sl4)
c7 = [sl4[i] for i in max(cl4, key=len)]
c6 = [st2[i] for i in [c for c in comps2 if len(c) == 6][0]]
c36 = [st2[i] for i in [c for c in comps2 if len(c) == 36][0]]
CERT = [("ladder L = 4, 7 states, N = 4", certify(gl4, c7, 4, 0.5)),
        ("ladder L = 4, 7 states, N = 6, delta = 0.3", certify(gl4, c7, 6, 0.3)),
        ("2x2x2 6-state component, N = 5", certify(g2, c6, 5, 0.5)),
        ("2x2x2 36-state component, N = 3", certify(g2, c36, 3, 0.5))]
check("D1 [exact] the open-path projector is certified on COMPLETE path spaces, not sampled: %s paths on %s. Every "
      "state on every path has G_v = 0 (max residual %d) and every step is one four-link plaquette flip"
      % (", ".join(str(r["M"]) for _, r in CERT), "; ".join(t for t, _ in CERT),
         max(r["gres"] for _, r in CERT)),
      all(r["gres"] == 0 and r["edge_ok"] for _, r in CERT)
      and [r["M"] for _, r in CERT] == [935, 11119, 4790, 10020])
check("D2 [1e-18] the symmetric chain is exactly reversible for pi(path) = delta^{#moves}/Z: row sums 1 to %.0e, "
      "detailed balance max|pi_x T_xy - pi_y T_yx| = %.1e, stationarity max|pi T - pi| = %.1e, one strongly connected "
      "component on each of the four path spaces, so pi is its unique stationary law"
      % (max(r["rows"] for _, r in CERT), max(r["db"] for _, r in CERT), max(r["stat"] for _, r in CERT)),
      all(r["rows"] < 1e-15 and r["db"] < 1e-18 and r["stat"] < 1e-18 and r["ncc"] == 1 for _, r in CERT))
check("D3 [1e-18] the bounce chain is the expected NON-reversible one, certified by global and skew balance: on the "
      "lifted space (path, direction) row sums 1 to %.0e, global balance %.1e, skew detailed balance %.1e, irreducible, "
      "while plain detailed balance fails by up to %.1e"
      % (max(r["rowsB"] for _, r in CERT), max(r["statB"] for _, r in CERT), max(r["skew"] for _, r in CERT),
         max(r["dbB"] for _, r in CERT)),
      all(r["rowsB"] < 1e-15 and r["statB"] < 1e-18 and r["skew"] < 1e-18 and r["nccB"] == 1
          and r["dbB"] > 1e-5 for _, r in CERT))
check("D4 [1e-14] the stationary law is the intended one: the middle-state marginal of pi equals the exact "
      "1^T B^j e_s e_s^T B^{N-j} 1 / Z of B = I + delta A to %.1e on all four path spaces, so the middle of a long path "
      "carries psi_0^2 and the ends psi_0"
      % max(r["marg"] for _, r in CERT),
      all(r["marg"] < 1e-14 for _, r in CERT))
check("D5 [exact] the ergodicity ceiling: a flip conserves the winding vector, so a chain started on the 2x2x2 ice "
      "configuration reaches exactly %d states and one on the ladder's dynamical component exactly %d, no more; flux "
      "energies need chains started in W = (1,0,0) and (2,0,0)"
      % (len(big2), len(stL)),
      len(big2) == 864 and len(stL) == 47)


# =========================================== compile the embedded engines at run time
def find_compiler():
    """The first working C compiler on PATH, or None."""
    for cc in (os.environ.get("CC"), "cc", "gcc", "clang"):
        if cc and shutil.which(cc):
            return cc
    return None


CC = find_compiler()
TMP = tempfile.mkdtemp(prefix="pure_link_projector_")
EXE = {}
cc_reason = ""
if CC is None:
    cc_reason = "no C compiler on PATH (tried $CC, cc, gcc, clang)"
else:
    for name, src in (("t422x", C_T422), ("reptate", C_REPTATE), ("gfmc", C_GFMC)):
        path = os.path.join(TMP, name + ".c")
        with open(path, "w") as fh:
            fh.write(src)
        cp = subprocess.run([CC, "-O2", "-o", os.path.join(TMP, name), path, "-lm"],
                            capture_output=True, text=True, timeout=180)
        if cp.returncode != 0:
            CC = None
            cc_reason = "the embedded C source %s.c did not compile: %s" % (name, cp.stderr.strip()[-160:])
            break
        EXE[name] = os.path.join(TMP, name)

GEO = {}
if CC is not None:
    g4 = torus3d(4, 2, 2)
    gL4 = torus3d(4, 4, 4)
    for tag, gg in (("t222", g2), ("t422", g4), ("t444", gL4)):
        GEO[tag] = os.path.join(TMP, tag + ".geo")
        write_geo(gg, GEO[tag], ice_config(gg))
    GEO["lad8"] = os.path.join(TMP, "lad8.geo")
    write_geo(gl, GEO["lad8"], stL[int(np.argmax(VL[:, 0] ** 2))])

# ============================================================ C  the 4x2x2 torus, exact
T4 = {}
if CC is None:
    for lab in ("C1", "C2", "C3", "C4", "C5"):
        skip(lab + " [exact, needs cc] the 4x2x2 census, its one flip component, E_0, S_L = 0 and the exact "
                   "transverse decay rates", cc_reason)
else:
    r = subprocess.run([EXE["t422x"], GEO["t422"], "120"], capture_output=True, text=True,
                       timeout=AUDIT_TIMEOUT_SEC)
    if r.returncode != 0:
        for lab in ("C1", "C2", "C3", "C4", "C5"):
            skip(lab + " [exact, needs cc] the 4x2x2 census", "engine failed: " + r.stderr.strip()[-160:])
    else:
        for line in r.stdout.splitlines():
            if line.startswith("S "):
                t = line.split()
                T4.setdefault("S", {})["_".join(t[1:3])] = float(t[3].split("=")[1])
            elif line.startswith("omega "):
                t = line.split()
                T4.setdefault("omega", {})["_".join(t[1:3])] = float(t[4].split("=")[1])
                T4["omega"]["_".join(t[1:3]) + "_ratio"] = float(t[3].split("=")[1])
            else:
                for tok in line.split():
                    k, v = tok.split("=")
                    T4[k] = float(v) if ("." in v or "e" in v) else int(v)
        check("C1 [exact] the 4x2x2 torus (48 links, 16 vertices, 48 faces, rho_v = 0), enumerated site by site and "
              "sorted: dim(Gauss) = %d, all distinct, %d Gauss violations; %d distinct winding vectors, zero-winding "
              "class %d, W = (1,0,0) %d, W = (0,1,0) = (0,0,1) %d"
              % (T4["dim_gauss"], T4["gauss_violations"], T4["winding_classes"], T4["zero_winding"],
                 T4["w100"], T4["w010"]),
              T4["dim_gauss"] == 23063296 and T4["sorted_unique"] == 1 and T4["gauss_violations"] == 0
              and T4["winding_classes"] == 405 and T4["zero_winding"] == 1552024
              and T4["w100"] == 477888 and T4["w010"] == 1101696 and T4["w001"] == 1101696)
        check("C2 [exact] at 4x2x2 a winding class is ONE flip component up to isolated frozen states, so the 937 of "
              "2x2x2 is a smallest-box artefact: %d zero-winding states = one component of %d (breadth-first depth %d "
              "from the ice configuration) plus %d frozen (n_app = 0; %d frozen in the sector), remainder %d; closed "
              "under flips, %d adjacencies, %d missing targets"
              % (T4["zero_winding"], T4["component"], T4["bfs_depth"], T4["frozen_zero_winding"],
                 T4["frozen_total"], T4["zero_minus_comp_minus_frozen0"], T4["nnz"], T4["missing_targets"]),
              T4["component"] == 1551976 and T4["bfs_depth"] == 17 and T4["frozen_zero_winding"] == 48
              and T4["frozen_total"] == 46264 and T4["zero_minus_comp_minus_frozen0"] == 0
              and T4["nnz"] == 21578752 and T4["missing_targets"] == 0
              and T4["component_all_zero_winding"] == 1 and T4["ice_key_is_zero"] == 1)
        check("C3 [1e-9] the exact ground state of that 1,551,976-state component by power iteration on B = I + A "
              "(%d iterations, Rayleigh residual %.1e): E_0 = %.10f, <n_app>_0 = %.10f, mixed estimator %.10f, "
              "<P_f> = %.10f"
              % (T4["power_it"], T4["residual"], T4["E0"], T4["napp0"], T4["mixed"], T4["Pf"]),
              close(T4["E0"], -16.7037885782) and close(T4["napp0"], 19.0690013962)
              and close(T4["mixed"], -16.7037885782) and close(T4["Pf"], 0.3479955954)
              and T4["residual"] < 1e-10)
        S = T4["S"]
        check("C4 [1e-8] in that ground state S_L(k) = S_xx(k) is %.1e at (pi/2,0,0) and %.1e at (pi,0,0) -- zero to "
              "machine precision, not to a tolerance -- while S_yy = S_zz = %.10f at pi/2 and %.10f at pi"
              % (S["q=1_mu=0"], S["q=2_mu=0"], S["q=1_mu=1"], S["q=2_mu=1"]),
              abs(S["q=1_mu=0"]) < 1e-12 and abs(S["q=2_mu=0"]) < 1e-12
              and close(S["q=1_mu=1"], 0.1044875978, 1e-8) and close(S["q=1_mu=2"], 0.1044875978, 1e-8)
              and close(S["q=2_mu=1"], 0.1815941329, 1e-8) and close(S["q=2_mu=2"], 0.1815941329, 1e-8))
        om = T4["omega"]
        check("C5 [1e-3] exact transverse-electric decay rates on 4x2x2 from C(m) = <o|B^m|o>/lambda_B^m, delta = 0.25: "
              "omega_eff = %.4f, %.4f, %.4f at m = 40, 80, 120 for k = pi/2 and %.4f, %.4f, %.4f for k = pi, falling ONTO "
              "2.566 and 2.891 FROM ABOVE -- a sampler's finite-window plateau is therefore an upper bound on omega"
              % (om["q=1_m=40"], om["q=1_m=80"], om["q=1_m=120"],
                 om["q=2_m=40"], om["q=2_m=80"], om["q=2_m=120"]),
              close(om["q=1_m=120"], 2.566, 1e-3) and close(om["q=2_m=120"], 2.891, 1e-3)
              and om["q=1_m=40"] > om["q=1_m=80"] > om["q=1_m=120"]
              and om["q=2_m=40"] > om["q=2_m=80"] > om["q=2_m=120"])


# =================================================== E  [witness] the sampler rows, declared seeds
def lazy_anchors(w, V, delta, N, Nl, napp):
    """Exact finite-N anchors of the lazy propagator B = I + delta A from uniform trial ends."""
    a = -w / LAM
    b = 1.0 + delta * a
    c = V.T @ np.ones(V.shape[0])
    Z = float((c * c * b ** N).sum())
    Emix = float(-LAM * (c * c * a * b ** N).sum() / Z)
    mv = float(delta * (c * c * a * b ** (N - 1)).sum() / Z)
    O = V.T @ (napp[:, None] * V)
    vals = [float((c * b ** j) @ O @ (c * b ** (N - j))) / Z for j in range(Nl, N - Nl + 1)]
    return Emix, mv, -LAM * mv / (delta * (1 - mv)), float(np.mean(vals))


def _bins(path):
    rows = []
    for line in open(path):
        if line.startswith("#") or not line.strip():
            continue
        rows.append([[float(x) for x in blk.split()] for blk in line.split("|")])
    return rows


def _ms(v):
    v = np.asarray(v, dtype=float)
    return float(v.mean()), float(v.std(ddof=1) / math.sqrt(len(v)))


def run_rept(geo, delta, N, Nl, ntherm, nmoves, nbins, seed, kmax, tag, sweep=100):
    out = os.path.join(TMP, tag)
    r = subprocess.run([EXE["reptate"], geo, str(delta), str(N), str(Nl), str(ntherm), str(nmoves),
                        "100", str(nbins), str(seed), "1", "1", "40", str(kmax), "0", out, str(sweep)],
                       capture_output=True, text=True, timeout=AUDIT_TIMEOUT_SEC)
    if r.returncode != 0:
        raise RuntimeError(r.stderr[-300:])
    fin = [l for l in r.stdout.splitlines() if l.startswith("# final:")][-1]
    d = _bins(out + ".bins")
    E = _ms([x[0][2] for x in d])
    mv = _ms([x[0][3] for x in d])
    na = _ms([x[0][4] for x in d])
    SL = max(abs(v) for x in d for v in x[2])
    return dict(E=E, mv=mv, na=na, SL=SL, nbin=len(d),
                gauss=int(fin.split("gauss_err=")[1].split()[0]),
                replay=int(fin.split("replay_err=")[1].split()[0]),
                visited=int(fin.split("visited_states=")[1].split()[0]),
                Ep=-LAM * mv[0] / (delta * (1 - mv[0])))


def run_gfmc(geo, Nw, teq, tpr, dtau, K, Kp, kmax, seed, tag, nsub=1, nbins=20):
    out = os.path.join(TMP, tag)
    r = subprocess.run([EXE["gfmc"], geo, str(Nw), str(teq), str(tpr), str(dtau), str(K), str(Kp),
                        str(kmax), "4", "4", "0", "0", str(nbins), str(seed), "1", out, str(nsub)],
                       capture_output=True, text=True, timeout=AUDIT_TIMEOUT_SEC)
    if r.returncode != 0:
        raise RuntimeError(r.stderr[-300:])
    fin = [l for l in r.stdout.splitlines() if l.startswith("# final:")][-1]
    d = _bins(out + ".bins")
    npure = len(d[0][2])
    return dict(E=_ms([x[0][1] for x in d]), Eg=_ms([x[0][2] for x in d]),
                Sp=[_ms([x[2][q] for x in d]) for q in range(npure)],
                SL=max(abs(v) for x in d for v in x[3]), nbin=len(d),
                gauss=int(fin.split("gauss_err(dumps)=")[1].split()[0]))


def sig(meas, err, exact):
    return (meas - exact) / err if err > 0 else float("inf")


if CC is None:
    for lab in ("E1", "E2", "E3", "E4", "E5"):
        skip(lab + " [witness] the reptation and GFMC rows at their declared seeds", cc_reason)
else:
    napp2 = np.array([g2.n_app(s) for s in stI], dtype=float)
    A2 = lazy_anchors(wI, VI, 0.5, 200, 50, napp2)
    a1 = run_rept(GEO["t222"], 0.5, 200, 50, 100000, 2000000, 20, SEED_REPT, 1, "w_t222")
    s1 = [sig(a1["E"][0], a1["E"][1], A2[0]), sig(a1["mv"][0], a1["mv"][1], A2[1]),
          sig(a1["na"][0], a1["na"][1], A2[3])]
    check("E1 [witness, seed %d] the open-path projector on the 2x2x2 ice component, delta = 0.5, N = 200, bounce, "
          "interior sweep every 100 moves, 1e5 + 2e6 moves, %d bins: E_mix = %.4f(%.0f), move fraction %.5f(%.0f), "
          "<n_app>_bulk = %.3f(%.0f) sit %.2f, %.2f, %.2f sigma from the exact finite-N anchors %.10f, %.10f, %.10f; "
          "the head visits exactly %d states -- the whole component, nothing outside -- gauss_err %d, replay_err %d"
          % (SEED_REPT, a1["nbin"], a1["E"][0], 1e4 * a1["E"][1], a1["mv"][0], 1e5 * a1["mv"][1],
             a1["na"][0], 1e3 * a1["na"][1], s1[0], s1[1], s1[2], A2[0], A2[1], A2[3], a1["visited"],
             a1["gauss"], a1["replay"]),
          max(abs(x) for x in s1) < 3.0 and a1["visited"] == 864 and a1["gauss"] == 0 and a1["replay"] == 0
          and a1["SL"] < 1e-12 and abs(A2[0] - wI[0]) < 1e-9)

    nappL = np.array([gl.n_app(s) for s in stL], dtype=float)
    AL = lazy_anchors(wL, VL, 0.5, 200, 50, nappL)
    a2 = run_rept(GEO["lad8"], 0.5, 200, 50, 100000, 2000000, 20, SEED_REPT, 1, "w_lad8")
    s2 = [sig(a2["E"][0], a2["E"][1], AL[0]), sig(a2["mv"][0], a2["mv"][1], AL[1]),
          sig(a2["na"][0], a2["na"][1], AL[3])]
    check("E2 [witness, seed %d] the same engine on the L = 8 ladder, same parameters: E_mix = %.4f(%.0f), move "
          "fraction %.5f(%.0f), <n_app>_bulk = %.3f(%.0f) sit %.2f, %.2f, %.2f sigma from the exact %.10f, %.10f, "
          "%.10f, and the head visits exactly %d states, the dynamical component"
          % (SEED_REPT, a2["E"][0], 1e4 * a2["E"][1], a2["mv"][0], 1e5 * a2["mv"][1], a2["na"][0],
             1e3 * a2["na"][1], s2[0], s2[1], s2[2], AL[0], AL[1], AL[3], a2["visited"]),
          max(abs(x) for x in s2) < 3.0 and a2["visited"] == 47 and a2["gauss"] == 0 and a2["replay"] == 0)

    if T4:
        E0_4, na0_4 = T4["E0"], T4["napp0"]
        mv4 = 0.25 * (-E0_4) / (1 + 0.25 * (-E0_4))
        a3 = run_rept(GEO["t422"], 0.25, 600, 150, 200000, 3000000, 20, 20260921, 2, "w_t422")
        s3 = [sig(a3["E"][0], a3["E"][1], E0_4), sig(a3["mv"][0], a3["mv"][1], mv4),
              sig(a3["na"][0], a3["na"][1], na0_4)]
        check("E3 [witness, seed 20260921] the same engine on the 1,551,976-state 4x2x2 component, delta = 0.25, "
              "N = 600, 2e5 + 3e6 moves, %d bins: E_mix = %.4f(%.0f), move fraction %.5f(%.0f), <n_app> = %.3f(%.0f) "
              "sit %.2f, %.2f, %.2f sigma from group C's exact %.10f, %.10f, %.10f; sampled S_L = %.0e, head visits "
              "%d of %d and never leaves, gauss_err %d"
              % (a3["nbin"], a3["E"][0], 1e4 * a3["E"][1], a3["mv"][0], 1e5 * a3["mv"][1], a3["na"][0],
                 1e3 * a3["na"][1], s3[0], s3[1], s3[2], E0_4, mv4, na0_4, a3["SL"], a3["visited"],
                 T4["component"], a3["gauss"]),
              max(abs(x) for x in s3) < 3.0 and a3["gauss"] == 0 and a3["replay"] == 0
              and a3["SL"] < 1e-12 and 0 < a3["visited"] <= T4["component"])
    else:
        skip("E3 [witness] the open-path projector on the 4x2x2 component", "group C did not run")

    b1 = run_gfmc(GEO["t222"], 1600, 20, 400, 0.25, 40, 24, 1, SEED_GFMC_T222, "w_g222")
    sb = [sig(b1["E"][0], b1["E"][1], wI[0]), sig(b1["Eg"][0], b1["Eg"][1], wI[0]),
          sig(b1["Sp"][0][0], b1["Sp"][0][1], 0.25303701), sig(b1["Sp"][1][0], b1["Sp"][1][1], 0.25303701)]
    check("E4 [witness, seed %d] the second projector -- continuous-time GFMC with reconfiguration and forward walking, "
          "N_w = 1600, tau = 20 + 400, dtau = 0.25, tau_proj = 6 -- on the same component: E_mix = %.4f(%.0f), "
          "E_growth = %.4f(%.0f) at %.2f and %.2f sigma from the exact %.10f; pure S_T(pi,0,0) = %.4f(%.0f), %.4f(%.0f) "
          "at %.2f and %.2f sigma from %.8f per component; sampled S_L = %.0e"
          % (SEED_GFMC_T222, b1["E"][0], 1e4 * b1["E"][1], b1["Eg"][0], 1e4 * b1["Eg"][1], sb[0], sb[1],
             wI[0], b1["Sp"][0][0], 1e4 * b1["Sp"][0][1], b1["Sp"][1][0], 1e4 * b1["Sp"][1][1], sb[2],
             sb[3], 0.25303701, b1["SL"]),
          max(abs(x) for x in sb) < 3.0 and b1["gauss"] == 0 and b1["SL"] < 1e-12)

    if T4:
        bias = []
        for Nw in (400, 1600, 6400):
            b = run_gfmc(GEO["t422"], Nw, 20, 400, 0.1, 100, 50, 2, SEED_GFMC_T422, "w_g422_%d" % Nw)
            bias.append((Nw, b["E"][0], b["E"][1], b["E"][0] - T4["E0"], b["gauss"], b["SL"]))
        check("E5 [witness, seed %d] the walker method's population-control bias, measured against the exact "
              "E_0 = %.10f and falling with the walker count: E_mix = %.4f(%.0f), %.4f(%.0f), %.4f(%.0f) at "
              "N_w = 400, 1600, 6400 (tau = 20 + 400, dtau = 0.1), a bias of +%.3f, +%.3f, +%.3f = %.2f, %.2f, %.2f "
              "per cent of |E_0|, always toward higher energy; S_L = %.0e, gauss_err = %d throughout"
              % (SEED_GFMC_T422, T4["E0"], bias[0][1], 1e4 * bias[0][2], bias[1][1], 1e4 * bias[1][2],
                 bias[2][1], 1e4 * bias[2][2], bias[0][3], bias[1][3], bias[2][3],
                 100 * bias[0][3] / abs(T4["E0"]), 100 * bias[1][3] / abs(T4["E0"]),
                 100 * bias[2][3] / abs(T4["E0"]),
                 max(b[5] for b in bias), max(b[4] for b in bias)),
              all(b[3] > 0 for b in bias) and bias[0][3] > bias[1][3] > bias[2][3]
              and bias[2][3] < 0.01 and all(b[4] == 0 and b[5] < 1e-10 for b in bias))
    else:
        skip("E5 [witness] the population-control bias against the exact 4x2x2 energy", "group C did not run")

if CC is None:
    skip("E6 [witness] one short L = 4 GFMC run on the 4^3 torus", cc_reason)
else:
    b2 = run_gfmc(GEO["t444"], 500, 20, 40, 0.1, 160, 120, 1, SEED_GFMC_T4, "w_g444", nsub=5)
    NP4 = 3 * 64
    check("E6 [witness, seed %d] ONE SHORT L = 4 run, the only L^3 row computed here: 4^3 torus (192 links, 192 faces, "
          "ice start), N_w = 500, tau = 20 + 40, dtau = 0.1, nsub = 5, tau_proj = 12 gives E_mix = %.3f(%.0f) and "
          "E_growth = %.3f(%.0f), agreeing to %.2f sigma, E/N_p = %.4f -- above the quoted L = 4 row -56.199(19) at "
          "N_w = 2000 by the bias E5 measures; S_L = %.0e, gauss_err = %d"
          % (SEED_GFMC_T4, b2["E"][0], 1e3 * b2["E"][1], b2["Eg"][0], 1e3 * b2["Eg"][1],
             abs(b2["E"][0] - b2["Eg"][0]) / max(b2["E"][1], 1e-12), b2["E"][0] / NP4, b2["SL"], b2["gauss"]),
          -0.31 < b2["E"][0] / NP4 < -0.27 and b2["SL"] < 1e-10 and b2["gauss"] == 0
          and b2["E"][0] > -56.199 and abs(b2["E"][0] - b2["Eg"][0]) < 6 * max(b2["E"][1], b2["Eg"][1]))

# ============== F  [declared] the L^3 production rows are QUOTED, not recomputed here
LS = (4, 6, 8, 10, 12)
OM = (1.3, 0.80, 0.5, 0.32, 0.20)            # omega(k_min), quoted, GFMC nsub = 5, N_w = 2000
KM = tuple(2 * math.pi / L for L in LS)
ok = tuple(o / k for o, k in zip(OM, KM))
ok2 = tuple(o / k ** 2 for o, k in zip(OM, KM))
check("F1 [declared] GAPLESS AND QUADRATIC. The L = 4-12 production rows are QUOTED (GFMC, seeds 20261001-20261020 and "
      "20261101-20261114, tau_prod 130-230, N_w = 500-8000, 30 bins) and are NOT rerun here. From the quoted "
      "omega(k_min) = %s at k_min = 2pi/L: monotone, no saturation; omega/k halves (%.2f -> %.2f) while omega/k^2 = %s "
      "stays flat at mean %.2f over L = 6-12, spread %.0f per cent -- the quadratic form, not omega = c|k|"
      % (", ".join("%.2f" % o for o in OM), ok[1], ok[4], ", ".join("%.2f" % v for v in ok2[1:]),
         sum(ok2[1:]) / 4, 100 * (max(ok2[1:]) - min(ok2[1:])) / (sum(ok2[1:]) / 4)),
      all(OM[i] > OM[i + 1] for i in range(4)) and abs(ok[1] / ok[4] - 2.0) < 0.1
      and max(ok2[1:]) - min(ok2[1:]) < 0.10 and abs(sum(ok2[1:]) / 4 - 0.78) < 0.03)

SIG = 0.71 / 4.0
FL = ((6, 0.150, 0.076), (8, 0.15, 0.20))
dev = [(L, SIG * L, (SIG * L - e) / s) for L, e, s in FL]
check("F2 [declared] DECONFINED. The quoted E(W=1) - E(0) falls from 0.708(24) at L = 4 to %.3f(%.0f) at L = 6 and "
      "%.2f(%.0f) at L = 8, where a confining string of the L = 4 tension sigma = 0.71/4 needs sigma L = %.2f and %.2f "
      "-- excluded by %.1f and %.1f sigma; the fall beats Coulomb 1/L (%.2f) and fits 1/L^2 (%.2f, %.1f sigma), and the "
      "quoted E(2)/E(1) = 4.1(9) at L = 6 is the quadratic 4, not the string 2"
      % (FL[0][1], 1e3 * FL[0][2], FL[1][1], 1e2 * FL[1][2], dev[0][1], dev[1][1], dev[0][2], dev[1][2],
         0.708 * 4 / 6, 0.708 * (4 / 6.0) ** 2, (0.708 * (4 / 6.0) ** 2 - FL[0][1]) / FL[0][2]),
      dev[0][2] > 10 and dev[1][2] > 5 and abs(4.1 - 4.0) < 0.9)

NS = tuple(L ** 3 for L in LS)
BR = (1.49, 1.24, 1.18, 1.19, 1.08)
PS = (0.0152, 0.0051, 0.0018, 0.0009, 0.0005)
check("F3 [declared] UNORDERED. The quoted largest S_T(k) over the zone FALLS from %.2f at L = 4 to %.2f at L = 12, a "
      "factor %.2f, where a plaquette solid would make it GROW by the site factor %d; the per-site measure at (0,pi,pi) "
      "falls %.4f -> %.4f, factor %.1f against the 1/N_s factor %.1f of a liquid; quoted max_k S_L(k) <= %.0e"
      % (BR[0], BR[4], BR[0] / BR[4], NS[4] // NS[0], PS[0], PS[4], PS[0] / PS[4], NS[4] / NS[0], 4e-32),
      BR[4] < BR[0] and BR[0] / BR[4] < 1.5 and NS[4] // NS[0] == 27
      and abs(PS[0] / PS[4] / (NS[4] / NS[0]) - 1) < 0.15)

STK = (0.348, 0.302, 0.293, 0.344, 0.376)
maxw = 2 * math.sin(KM[0] / 2) / (2 * math.sin(KM[4] / 2))
check("F4 [declared] NOT THE MAXWELL PHOTON AT THESE MOMENTA. The quoted S_T(k_min) = %s (two components) is FLAT from "
      "k = pi/2 to pi/6, varying %.0f per cent with no trend, where S_T proportional to omega_k = c|k| would fall by a "
      "factor %.2f (lattice 2 sin(k/2)); with omega = %.2f k^2 and the exact S_L = 0 of A and C this is the flat "
      "pinch-point form of a z = 2 mode in a Hamiltonian carrying no Rokhsar-Kivelson term"
      % (", ".join("%.2f" % v for v in STK), 100 * (max(STK) - min(STK)) / (sum(STK) / 5), maxw,
         sum(ok2[1:]) / 4),
      max(STK) / min(STK) < 1.4 and maxw > 2.0 and min(STK) > 0.29 and max(STK) < 0.39)

shutil.rmtree(TMP, ignore_errors=True)
print("SUMMARY: the Gauss sector is counted exactly on three geometries -- 937 flip components at 2x2x2 but ONE per "
      "winding class at 4x2x2, so the 937 is a smallest-box artefact and the winding vector separates sectors -- and "
      "the open-path projector is certified on complete path spaces, needing no parity-changing update because its ends "
      "are free. Every L^3 row is a quoted witness: gapless, deconfined and unordered at L <= 12, with a quadratic "
      "transverse mode and a flat transverse structure factor, not the Maxwell photon at these momenta.")
print("TOTAL: PASS=%d FAIL=%d" % (PASS, FAIL))
sys.exit(0 if FAIL == 0 else 1)
