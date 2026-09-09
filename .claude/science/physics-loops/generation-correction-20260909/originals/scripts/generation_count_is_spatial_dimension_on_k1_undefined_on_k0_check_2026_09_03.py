#!/usr/bin/env python3
"""The generation count is the spatial dimension on the K1 branch and undefined on K0.

One-particle nearest-neighbour operators on the periodic L^d torus (dense numpy,
exact integer and half-integer entries, no seeds, no fitted constants):

  T_mu   = sum_x |x+mu><x|                     plain translation, T_mu|p> = e^{-i p_mu}|p>
  H_K0   = sum_mu (T_mu + T_mu^+)              K0 class: flux +1, hopping t = 1
  H_K1r  = sum_mu eta_mu (T_mu + T_mu^+)       K1 class, real frame t = eta
  H_K1   = i sum_mu eta_mu (T_mu - T_mu^+)     K1 class, staggered frame t = i eta
  M_W    = sum_mu (1 - (T_mu + T_mu^+)/2)      the Wilson operator, M_W(p) = sum_mu (1 - cos p_mu)
  eta_mu(x) = (-1)^(x_1 + ... + x_{mu-1})      Kawamoto-Smit signs

Every number printed is recomputed from these operators. One PASS/FAIL line per
check; the last line is the TOTAL line.
"""

from __future__ import annotations

import functools
import itertools
import math

import numpy as np

AUDIT_TIMEOUT_SEC = 120

LAM = 0.1
LAM_SWEEP = (0.1, 0.25, 0.5, 1.0, 2.0)
D3_SIZES = (4, 6, 8)


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, statement: str, condition: bool) -> None:
        result = bool(condition)
        self.passed += int(result)
        self.failed += int(not result)
        print(f"{'PASS' if result else 'FAIL'}: {label} {statement}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


# ----------------------------------------------------------------------------- operators
@functools.lru_cache(maxsize=None)
def sites(L: int, d: int) -> np.ndarray:
    return np.array(list(itertools.product(range(L), repeat=d)), dtype=np.int64)


def ravel(Y: np.ndarray, L: int) -> np.ndarray:
    d = Y.shape[1]
    return (Y % L) @ (L ** np.arange(d - 1, -1, -1))


def permutation_matrix(L: int, d: int, Y: np.ndarray, sign=None) -> np.ndarray:
    N = L ** d
    M = np.zeros((N, N))
    M[ravel(Y, L), np.arange(N)] = 1.0 if sign is None else sign
    return M


def shift(L: int, d: int, mu: int, apbc: bool = False) -> np.ndarray:
    Y = sites(L, d).copy()
    Y[:, mu] += 1
    wrap = Y[:, mu] == L
    sign = np.where(wrap, -1.0 if apbc else 1.0, 1.0)
    return permutation_matrix(L, d, Y, sign)


def eta(L: int, d: int, mu: int) -> np.ndarray:
    return (-1.0) ** (sites(L, d)[:, :mu].sum(axis=1) % 2)


def operators(L: int, d: int, apbc: bool = False):
    T = [shift(L, d, mu, apbc) for mu in range(d)]
    N = L ** d
    H0 = sum(t + t.T for t in T)
    H1r = sum(eta(L, d, mu)[:, None] * (T[mu] + T[mu].T) for mu in range(d))
    H1 = sum(1j * eta(L, d, mu)[:, None] * (T[mu] - T[mu].T) for mu in range(d))
    MW = sum(np.eye(N) - 0.5 * (t + t.T) for t in T)
    return T, H0, H1r, H1, MW


def plane_wave(L: int, d: int, n) -> np.ndarray:
    return np.exp(2j * np.pi * (sites(L, d) @ np.asarray(n)) / L) / L ** (d / 2)


def corners(L: int, d: int):
    return list(itertools.product([0, L // 2], repeat=d))


def hamming(n, L: int) -> int:
    return sum(1 for c in n if c == L // 2)


def cyc_rot(L: int, d: int) -> np.ndarray:
    """Proper rotation cycling the axes: x -> (x_d, x_1, ..., x_{d-1}) for odd d,
    x -> (-x_d, x_1, ..., x_{d-1}) for even d (the sign keeps det = +1)."""
    X = sites(L, d)
    last = X[:, -1] if d % 2 else (-X[:, -1]) % L
    return permutation_matrix(L, d, np.column_stack([last, X[:, :-1]]))


def proper_rotations(d: int):
    mats = []
    for perm in itertools.permutations(range(d)):
        for signs in itertools.product([1, -1], repeat=d):
            M = np.zeros((d, d), dtype=int)
            for i, j in enumerate(perm):
                M[i, j] = signs[i]
            if round(np.linalg.det(M)) == 1:
                mats.append(M)
    return mats


def orbit_sizes(points, L: int, group):
    pts, seen, sizes = set(points), set(), []
    for p in points:
        if p in seen:
            continue
        orb = {tuple(int(v) % L for v in M @ np.array(p)) for M in group}
        if not orb <= pts:
            return None
        seen |= orb
        sizes.append(len(orb))
    return sorted(sizes)


def momenta_with_cos_sum(L: int, d: int, value: float):
    return [n for n in itertools.product(range(L), repeat=d)
            if abs(sum(math.cos(2 * math.pi * c / L) for c in n) - value) < 1e-9]


def mult_at(ev: np.ndarray, value: float, tol: float = 1e-7) -> int:
    return int(np.sum(np.abs(ev - value) < tol))


def flux_set(tfun, L: int, d: int):
    """Normalised plaquette flux t_mu(x) t_nu(x+mu) conj(t_mu(x+nu)) conj(t_nu(x))."""
    vals = set()
    for x in map(tuple, sites(L, d)):
        for mu in range(d):
            for nu in range(mu + 1, d):
                xm = list(x); xm[mu] = (xm[mu] + 1) % L
                xn = list(x); xn[nu] = (xn[nu] + 1) % L
                f = tfun(x, mu) * tfun(tuple(xm), nu) * np.conj(tfun(tuple(xn), mu)) * np.conj(tfun(x, nu))
                f = f / abs(f)
                vals.add((round(float(np.real(f)), 6), round(float(np.imag(f)), 6)))
    return sorted(vals)


def eta_fun(x, mu: int) -> float:
    return (-1.0) ** (sum(x[:mu]) % 2)


# ----------------------------------------------------------------------------- algebra on a level
def perm_orbits(sigma):
    seen, orbs = set(), []
    for k in range(len(sigma)):
        if k in seen:
            continue
        o, j = [], k
        while j not in seen:
            o.append(j)
            seen.add(j)
            j = sigma[j]
        orbs.append(o)
    return orbs


def block_algebra(Rt: np.ndarray) -> dict:
    """Algebra generated by the rank-1 diagonal projectors E_ii and a phased permutation
    matrix Rt on C^n.  The nonzero words E_i Rt^k E_j are matrix units up to phase; the
    span is  (+)_orbits M_|O|(C).  Returns its dimension (from the rank of the stacked
    words), closure, orbit sizes and the commutant dimension (diagonal D with [Rt, D] = 0)."""
    n = Rt.shape[0]
    mags = np.abs(Rt)
    is_perm = bool(np.allclose(mags.sum(axis=0), 1.0, atol=1e-9)
                   and np.allclose(mags.max(axis=0), 1.0, atol=1e-9))
    sigma = [int(np.argmax(mags[:, j])) for j in range(n)]
    orbs = perm_orbits(sigma)
    orbit_of = {i: k for k, o in enumerate(orbs) for i in o}
    order = math.lcm(*[len(o) for o in orbs])
    words, pairs, unit_ok = [], set(), True
    Rk = np.eye(n, dtype=complex)
    for _ in range(order):
        for j in range(n):
            col = Rk[:, j]
            i = int(np.argmax(np.abs(col)))
            rest = np.linalg.norm(np.delete(col, i))
            unit_ok &= rest < 1e-9 and abs(abs(col[i]) - 1) < 1e-9
            w = np.zeros((n, n), dtype=complex)
            w[i, j] = col[i]                      # = E_i Rt^k E_j exactly
            words.append(w.reshape(-1))
            pairs.add((i, j))
        Rk = Rk @ Rt
    rank = int(np.linalg.matrix_rank(np.array(words), tol=1e-8))
    all_pairs = {(i, j) for i in range(n) for j in range(n) if orbit_of[i] == orbit_of[j]}
    closed = unit_ok and pairs == all_pairs          # matrix units within an orbit multiply to matrix units
    # commutant: diagonal D with Rt D - D Rt = 0
    A = np.array([(Rt @ np.diag(e) - np.diag(e) @ Rt).reshape(-1) for e in np.eye(n)]).T
    commutant = n - int(np.linalg.matrix_rank(A, tol=1e-8))
    return {"dim": rank, "closed": closed, "is_perm": is_perm,
            "orbits": orbs, "sizes": sorted(len(o) for o in orbs), "commutant": commutant}


def k1_level(L: int, d: int, T, H1, MW, R, lam: float) -> dict:
    """The eigenspace of H_K1 + lam M_W at E = 2 lam (the hw = 1 corner level)."""
    w, V = np.linalg.eigh(H1 + lam * MW)
    B = V[:, np.abs(w - 2 * lam) < 1e-7]
    n = B.shape[1]
    Tt = [B.conj().T @ t @ B for t in T]
    comm = max(np.linalg.norm(a @ b - b @ a) for a in Tt for b in Tt)
    herm = max(np.linalg.norm(t - t.conj().T) for t in Tt)
    combo = sum((mu + 1) * Tt[mu] for mu in range(d))
    _, W = np.linalg.eigh(0.5 * (combo + combo.conj().T))
    C = B @ W
    chars = sorted(tuple(int(round((C[:, k].conj() @ t @ C[:, k]).real)) for t in T) for k in range(n))
    char_res = max(np.linalg.norm(t @ C[:, k] - (C[:, k].conj() @ t @ C[:, k]) * C[:, k])
                   for t in T for k in range(n))
    Rt = C.conj().T @ R @ C
    unitary = bool(np.allclose(Rt.conj().T @ Rt, np.eye(n), atol=1e-9))
    power = bool(np.allclose(np.linalg.matrix_power(Rt, d), np.eye(n), atol=1e-9))
    alg = block_algebra(Rt)
    return {"dim": n, "comm": max(comm, herm, char_res), "chars": chars, "unitary": unitary,
            "power": power, "trace": complex(np.trace(Rt)), "alg": alg}


def k0_level(L: int, d: int, H0, MW, R, lam: float) -> dict:
    """The eigenspace of H_K0 + lam M_W containing the hw = 1 corners (sum cos p = d - 2)."""
    E1 = 2 * d - 4 + 2 * lam
    n = mult_at(np.linalg.eigvalsh(H0 + lam * MW), E1)
    mom = momenta_with_cos_sum(L, d, d - 2)
    PW = np.array([plane_wave(L, d, m) for m in mom]).T
    res = float(np.linalg.norm((H0 + lam * MW) @ PW - E1 * PW))
    alg = block_algebra(PW.conj().T @ R @ PW)
    hw1 = {k for k, m in enumerate(mom) if all(c in (0, L // 2) for c in m) and hamming(m, L) == 1}
    corner_orbit = any(set(o) == hw1 for o in alg["orbits"])
    return {"dim": n, "nmom": len(mom), "res": res, "alg": alg, "corner_orbit": corner_orbit}


def bulk_clearance(ev: np.ndarray, corner_levels) -> float:
    mask = np.ones(len(ev), dtype=bool)
    for v in corner_levels:
        mask &= np.abs(ev - v) >= 1e-7
    bulk = ev[mask]
    return float(min(np.min(np.abs(bulk - v)) for v in corner_levels))


# ----------------------------------------------------------------------------- main
def fmt(x: float) -> str:
    return f"{x:.1e}"


def main() -> int:
    checks = Checks()
    print("external_scientific_inputs: none; every operator is declared in this runner (dense numpy, no seeds)")
    print("surface: one-particle nearest-neighbour operators on the periodic L^d torus; K0 t=1, K1 t=i*eta (Kawamoto-Smit), "
          "M_W = sum_mu (1 - (T_mu + T_mu^+)/2); lam = 0.1 unless stated")

    # ---- d = 3 block ------------------------------------------------------------------
    t1_diff, t1_ok = 0.0, True
    k1_zero, k1_kernel_res, corner_res, eig_res = [], 0.0, 0.0, 0.0
    mult01, clear01, sweep = [], [], {lam: [] for lam in LAM_SWEEP}
    floor, lev1, lev0, zero0, zero0_corners, zero0_orbits, mw_const, id_diff, extrema = [], [], [], [], [], [], 0.0, 0.0, []
    apbc_rows, frame_rows = [], []
    comm0, comm1, flux = None, None, None
    G3 = proper_rotations(3)
    for L in D3_SIZES:
        d = 3
        T, H0, H1r, H1, MW = operators(L, d)
        N = L ** d
        R = cyc_rot(L, d)
        t1_diff = max(t1_diff, float(np.max(np.abs(MW - (d * np.eye(N) - 0.5 * H0)))))
        if L == 4:
            comm0 = float(np.linalg.norm(H0 @ MW - MW @ H0))
            comm1 = float(np.linalg.norm(H1 @ MW - MW @ H1))
            flux = {
                "K0": flux_set(lambda x, mu: 1.0, L, d),
                "K1r": flux_set(eta_fun, L, d),
                "K1": flux_set(lambda x, mu: 1j * eta_fun(x, mu), L, d),
                "mix": flux_set(lambda x, mu: 1j * eta_fun(x, mu) - LAM / 2, L, d),
            }
        # K1: zero modes and corner identities
        w1, V1 = np.linalg.eigh(H1)
        k1_zero.append(mult_at(w1, 0.0))
        Z = V1[:, np.abs(w1) < 1e-7]
        Cw = np.array([plane_wave(L, d, c) for c in corners(L, d)]).T
        k1_kernel_res = max(k1_kernel_res, float(np.linalg.norm(Cw - Z @ (Z.conj().T @ Cw))))
        for c in corners(L, d):
            v, h = plane_wave(L, d, c), hamming(c, L)
            corner_res = max(corner_res, float(np.linalg.norm(H1 @ v)), float(np.linalg.norm(MW @ v - 2 * h * v)))
            for lam in LAM_SWEEP:
                eig_res = max(eig_res, float(np.linalg.norm((H1 + lam * MW) @ v - 2 * lam * h * v)))
        nz = np.sort(np.abs(w1))[2 ** d]
        floor.append((nz, 2 * math.sin(2 * math.pi / L)))
        for lam in LAM_SWEEP:
            ev = np.linalg.eigvalsh(H1 + lam * MW)
            sweep[lam].append(tuple(mult_at(ev, 2 * lam * k) for k in range(d + 1)))
            if lam == LAM:
                mult01.append(sweep[lam][-1])
                clear01.append(bulk_clearance(ev, [2 * lam * k for k in range(d + 1)]))
        lev1.append(k1_level(L, d, T, H1, MW, R, LAM))
        # K0: zero set, Wilson constancy, band extrema, hw=1 level
        e0 = np.linalg.eigvalsh(H0)
        mom0 = momenta_with_cos_sum(L, d, 0.0)
        zero0.append((mult_at(e0, 0.0), len(mom0)))
        zero0_corners.append(sum(1 for m in mom0 if all(c in (0, L // 2) for c in m)))
        zero0_orbits.append(orbit_sizes(mom0, L, G3))
        Z0 = np.array([plane_wave(L, d, m) for m in mom0]).T
        mw_const = max(mw_const, float(np.linalg.norm(MW @ Z0 - d * Z0)), float(np.linalg.norm(H0 @ Z0)))
        id_diff = max(id_diff, float(np.max(np.abs((H0 + LAM * MW) - (d * LAM * np.eye(N) + (1 - LAM / 2) * H0)))))
        extrema.append((mult_at(e0, 2 * d), mult_at(e0, -2 * d)))
        lev0.append(k0_level(L, d, H0, MW, R, LAM))
        # boundary witnesses
        _, H0a, _, H1a, _ = operators(L, d, apbc=True)
        ea, e0a = np.linalg.eigvalsh(H1a), np.linalg.eigvalsh(H0a)
        apbc_rows.append((mult_at(ea, 0.0), float(np.min(np.abs(ea))), 2 * math.sqrt(d) * math.sin(math.pi / L),
                          mult_at(np.abs(ea), float(np.min(np.abs(ea)))), mult_at(e0a, 0.0)))
        U = np.diag([1j ** (int(s) % 4) for s in sites(L, d).sum(axis=1)])
        conj = bool(np.allclose(U.conj().T @ H1r @ U, -H1, atol=1e-9))
        frame_rows.append((mult_at(np.linalg.eigvalsh(H1r), 0.0), conj))

    # ---- d = 2 and d = 4 blocks -----------------------------------------------------------
    tab = {}
    for d, Ls in ((2, (4, 6, 8)), (4, (4, 6))):
        rows = []
        for L in Ls:
            T, H0, H1r, H1, MW = operators(L, d)
            N = L ** d
            R = cyc_rot(L, d)
            t1_diff = max(t1_diff, float(np.max(np.abs(MW - (d * np.eye(N) - 0.5 * H0)))))
            w1 = np.linalg.eigvalsh(H1)
            ev = np.linalg.eigvalsh(H1 + LAM * MW)
            pattern = tuple(mult_at(ev, 2 * LAM * k) for k in range(d + 1))
            for c in corners(L, d):
                v, h = plane_wave(L, d, c), hamming(c, L)
                eig_res = max(eig_res, float(np.linalg.norm((H1 + LAM * MW) @ v - 2 * LAM * h * v)))
            e0 = np.linalg.eigvalsh(H0)
            mom0 = momenta_with_cos_sum(L, d, 0.0)
            rows.append({"L": L, "zero1": mult_at(w1, 0.0), "pattern": pattern,
                         "lev1": k1_level(L, d, T, H1, MW, R, LAM),
                         "zero0": (mult_at(e0, 0.0), len(mom0)),
                         "zero0_corners": sum(1 for m in mom0 if all(c in (0, L // 2) for c in m)),
                         "lev0": k0_level(L, d, H0, MW, R, LAM)})
            del T, H0, H1r, H1, MW, R
        tab[d] = rows

    # ---- checks ---------------------------------------------------------------------------
    checks.check("T1-wilson-is-k0",
                 f"M_W = d*I - H_K0/2 with max entry difference {t1_diff:.1f} for d=2,3,4 at every L used "
                 "(the Wilson operator is the K0 hopping up to an affine map)", t1_diff == 0.0)
    checks.check("T1-commutators",
                 f"[H_K0, M_W] = 0 exactly (norm {comm0:.1f}); ||[H_K1, M_W]|| = {comm1:.2f} (d=3, L=4): "
                 "the Wilson operator is a K0 term, not a K1 term", comm0 == 0.0 and comm1 > 1.0)
    mix = flux["mix"]
    mix_txt = ", ".join(f"{a:+.6f}{b:+.6f}i" for a, b in mix)
    checks.check("T4-flux",
                 f"plaquette flux sets (d=3, L=4): K0 {[a for a, _ in flux['K0']]}, K1 t=eta {[a for a, _ in flux['K1r']]}, "
                 f"K1 t=i*eta {[a for a, _ in flux['K1']]}; H_K1 + lam M_W read as one hopping t = i*eta - lam/2 has "
                 f"{len(mix)} flux values {{{mix_txt}}}: non-uniform, outside the two-class family",
                 flux["K0"] == [(1.0, 0.0)] and flux["K1r"] == [(-1.0, 0.0)] and flux["K1"] == [(-1.0, 0.0)]
                 and len(mix) == 2 and all(abs(b) > 0.01 for _, b in mix))
    checks.check("T2-zero-modes",
                 f"d=3: H_K1 zero modes {k1_zero} = 2^3 at L=4,6,8; kernel = span of the 8 corner plane waves "
                 f"(max residual {fmt(k1_kernel_res)})", k1_zero == [8, 8, 8] and k1_kernel_res < 1e-9)
    checks.check("T2-corner-identities",
                 f"d=3: H_K1|c> = 0 and M_W|c> = 2hw|c> for all 8 corners at L=4,6,8 (max residual {fmt(corner_res)}), so "
                 f"(H_K1 + lam M_W)|c> = 2 lam hw |c> for every lam; checked at lam in {LAM_SWEEP} and d=2,4 (max residual {fmt(eig_res)})", corner_res < 1e-9 and eig_res < 1e-9)
    checks.check("T2-multiplicities",
                 f"d=3 lam=0.1: levels 0, 0.2, 0.4, 0.6 have multiplicities {mult01[0]} = C(3,k) at L=4,6,8; "
                 f"nearest bulk eigenvalue to any corner level at distance {'/'.join(f'{c:.3f}' for c in clear01)} (L=4/6/8)",
                 all(m == (1, 3, 3, 1) for m in mult01) and all(c > 0.1 for c in clear01))
    sw = {lam: sweep[lam] for lam in LAM_SWEEP}
    small_ok = all(sw[lam][i] == (1, 3, 3, 1) for lam in (0.1, 0.25, 0.5) for i in range(3))
    checks.check("T2-isolation-window",
                 f"d=3: (1,3,3,1) exact for lam in (0.1, 0.25, 0.5) at L=4,6,8; lam=1: {sw[1.0]}; lam=2: {sw[2.0]} "
                 "(L=4,6,8): singlets cross bulk states at lam=1 and triplets at lam=2 for L=4,8; the hw=1 triplet is "
                 "exactly threefold through lam=1 at every L",
                 small_ok and sw[1.0] == [(5, 3, 3, 5), (1, 3, 3, 1), (5, 3, 3, 5)]
                 and sw[2.0] == [(2, 10, 10, 2), (1, 3, 3, 1), (2, 18, 18, 2)])
    checks.check("T2-bulk-floor",
                 "d=3: smallest nonzero |E| of H_K1 = 2 sin(2 pi/L) = "
                 + "/".join(f"{a:.4f}" for a, _ in floor) + " at L=4/6/8 (the finite-volume separation of bulk from corners)",
                 all(abs(a - b) < 1e-9 for a, b in floor))
    checks.check("T2-hw1-level",
                 f"d=3 lam=0.1: eigenspace at E=0.2 has dim {[x['dim'] for x in lev1]} at L=4,6,8; plain translations "
                 f"restricted to it are Hermitian and commute (max residual {fmt(max(x['comm'] for x in lev1))})",
                 all(x["dim"] == 3 for x in lev1) and all(x["comm"] < 1e-9 for x in lev1))
    chars3 = [(-1, 1, 1), (1, -1, 1), (1, 1, -1)]
    checks.check("T2-characters",
                 f"d=3: joint translation characters on the hw=1 level are {chars3} at L=4,6,8 (-1 in exactly one slot)",
                 all(x["chars"] == chars3 for x in lev1))
    checks.check("T2-rotation",
                 "d=3: the axis 3-cycle R restricted to the hw=1 level is unitary, R^3 = I, trace "
                 + "/".join(f"{abs(x['trace'].real):.1f}" for x in lev1)
                 + ": a fixed-point-free 3-cycle, one orbit on the 3 characters",
                 all(x["unitary"] and x["power"] and abs(x["trace"]) < 1e-9 and len(x["alg"]["orbits"]) == 1 for x in lev1))
    checks.check("T2-algebra",
                 f"d=3: the algebra generated by the 3 character projectors and R has dim {[x['alg']['dim'] for x in lev1]} "
                 f"= dim M_3(C), closed, commutant dim {[x['alg']['commutant'] for x in lev1]}: irreducible, "
                 "no proper invariant subspace (no proper quotient) at L=4,6,8",
                 all(x["alg"]["dim"] == 9 and x["alg"]["closed"] and x["alg"]["commutant"] == 1 for x in lev1))
    checks.check("T3-k0-zero-set",
                 f"d=3: H_K0 zero modes {'/'.join(str(a) for a, _ in zero0)} at L=4/6/8 = #{{p : sum_mu cos p_mu = 0}} "
                 f"({'/'.join(str(b) for _, b in zero0)}); corners on the zero set: {zero0_corners}; "
                 f"proper-rotation orbit sizes {zero0_orbits}",
                 [a for a, _ in zero0] == [20, 24, 68] and all(a == b for a, b in zero0) and zero0_corners == [0, 0, 0]
                 and zero0_orbits == [[8, 12], [12, 12], [8, 12, 24, 24]])
    checks.check("T3-wilson-constant",
                 f"d=3: M_W = 3 on ker H_K0 (max residual {fmt(mw_const)}); H_K0 + lam M_W = 3 lam + (1 - lam/2) H_K0 "
                 f"(max entry difference {fmt(id_diff)}): the Wilson term lifts nothing on K0",
                 mw_const < 1e-9 and id_diff < 1e-12)
    checks.check("T3-band-extrema",
                 f"d=3: the extremal K0 levels E = +6 (p = 0) and E = -6 (p = (pi,pi,pi)) have multiplicities {extrema} "
                 "at L=4,6,8: one species at each band extremum",
                 extrema == [(1, 1), (1, 1), (1, 1)])
    checks.check("T3-hw1-level",
                 f"d=3 lam=0.1: the level containing the hw=1 corners (E = 2.2, sum cos p = 1) has dim "
                 f"{'/'.join(str(x['dim']) for x in lev0)} at L=4/6/8 (plane-wave residual {fmt(max(x['res'] for x in lev0))}); "
                 f"R-orbits {'/'.join(str(len(x['alg']['orbits'])) for x in lev0)}, all of size 3; the hw=1 corners form one orbit",
                 [x["dim"] for x in lev0] == [15, 27, 39] and all(x["dim"] == x["nmom"] and x["res"] < 1e-9 for x in lev0)
                 and all(set(x["alg"]["sizes"]) == {3} and x["corner_orbit"] for x in lev0)
                 and [len(x["alg"]["orbits"]) for x in lev0] == [5, 9, 13])
    checks.check("T3-algebra",
                 f"d=3: the algebra generated by the momentum projectors and R on that level has dim "
                 f"{'/'.join(str(x['alg']['dim']) for x in lev0)} = 9 x orbits (full M_n: "
                 f"{'/'.join(str(x['dim'] ** 2) for x in lev0)}), closed, commutant dim "
                 f"{'/'.join(str(x['alg']['commutant']) for x in lev0)}: M_3(C)^(+5/9/13), reducible; "
                 "the corner triplet is one summand among equals",
                 [x["alg"]["dim"] for x in lev0] == [45, 81, 117] and all(x["alg"]["closed"] for x in lev0)
                 and [x["alg"]["commutant"] for x in lev0] == [5, 9, 13])
    checks.check("T5-apbc",
                 f"d=3 antiperiodic: H_K1 zero modes {[r[0] for r in apbc_rows]} at L=4,6,8; min |E| = 2 sqrt(3) sin(pi/L) = "
                 f"{'/'.join(f'{r[1]:.4f}' for r in apbc_rows)} on {[r[3] for r in apbc_rows]} = 4^3 momenta; "
                 f"H_K0 zero modes {[r[4] for r in apbc_rows]}",
                 all(r[0] == 0 and abs(r[1] - r[2]) < 1e-9 and r[3] == 64 for r in apbc_rows)
                 and [r[4] for r in apbc_rows] == [0, 56, 0])
    checks.check("T5-frame",
                 f"d=3 periodic: the real frame t = eta has {[r[0] for r in frame_rows]} zero modes at L=4,6,8; "
                 f"U = diag(i^|x|) conjugates it to -H_K1: {[r[1] for r in frame_rows]} (single-valued iff L = 0 mod 4)",
                 [r[0] for r in frame_rows] == [8, 0, 8] and [r[1] for r in frame_rows] == [True, False, True])
    for d, want_pat in ((2, (1, 2, 1)), (4, (1, 4, 6, 4, 1))):
        rows = tab[d]
        chars = sorted(tuple(-1 if k == m else 1 for k in range(d)) for m in range(d))
        ok = all(r["zero1"] == 2 ** d and r["pattern"] == want_pat and r["lev1"]["dim"] == d
                 and r["lev1"]["chars"] == chars and r["lev1"]["comm"] < 1e-9 and r["lev1"]["unitary"]
                 and r["lev1"]["alg"]["dim"] == d * d and r["lev1"]["alg"]["closed"]
                 and r["lev1"]["alg"]["commutant"] == 1 for r in rows)
        checks.check(f"T6-k1-d{d}",
                     f"d={d} (L={','.join(str(r['L']) for r in rows)}): H_K1 zero modes {rows[0]['zero1']} = 2^{d}; corner "
                     f"multiplicities {want_pat} at lam=0.1; hw=1 level dim {d} with characters -1 in exactly one slot; "
                     f"algebra dim {d * d} = dim M_{d}(C), commutant dim 1: irreducible", ok)
    for d, want0, wantc, wantn, wanta in ((2, [6, 10, 14], 2, [6, 10, 14], [20, 36, 52]),
                                          (4, [70, 198], 6, [28, 68], [208, 528])):
        rows = tab[d]
        ok = ([r["zero0"][0] for r in rows] == want0 and all(r["zero0"][0] == r["zero0"][1] for r in rows)
              and all(r["zero0_corners"] == wantc for r in rows) and [r["lev0"]["dim"] for r in rows] == wantn
              and all(r["lev0"]["dim"] == r["lev0"]["nmom"] and r["lev0"]["res"] < 1e-9 and r["lev0"]["alg"]["closed"]
                      and r["lev0"]["corner_orbit"] and r["lev0"]["alg"]["dim"] < r["lev0"]["dim"] ** 2 for r in rows)
              and [r["lev0"]["alg"]["dim"] for r in rows] == wanta)
        checks.check(f"T6-k0-d{d}",
                     f"d={d}: H_K0 zero modes {[r['zero0'][0] for r in rows]} (extensive); corners on the zero set "
                     f"{wantc} (those with hw = d/2); the level holding the hw=1 corners has dim {wantn} with algebra dim "
                     f"{wanta} < n^2, orbit sizes {rows[-1]['lev0']['alg']['sizes']} at L={rows[-1]['L']}: reducible", ok)
    counts = {2: tab[2][0]["lev1"]["dim"], 3: lev1[0]["dim"], 4: tab[4][0]["lev1"]["dim"]}
    checks.check("T6-count-table",
                 f"lightest nonzero corner multiplet on K1 has size C(d,1) = d: {counts}; on K0 no corner level is "
                 "isolated in d=2,3,4: no count is defined there",
                 counts == {2: 2, 3: 3, 4: 4})
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
