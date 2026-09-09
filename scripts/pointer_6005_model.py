"""Supplied finite star and sampled interval definitions from Cycles934/932.
Copied computational definitions do not grant original physical/corpus claims.
"""
import math
import numpy as np
import scipy.optimize as sopt
HEADLINE_DELTA=.1
CONTENT_H_MIN=.05
EXCESS_MIN=.02
INDEP_MAX=.02
EDGE_TOL=1e-13
SIG_X=np.array([[0.,1.],[1.,0.]])
SIG_Z=np.diag([1.,-1.])


def h2(p):
    if p <= 0.0 or p >= 1.0:
        return 0.0
    return float(-p * math.log2(p) - (1.0 - p) * math.log2(1.0 - p))

def ent_of_spectrum(w):
    w = np.asarray(w, dtype=float)
    w = w[w > 1e-16]
    if w.size == 0:
        return 0.0
    w = w / w.sum()
    return float(-(w * np.log2(w)).sum())

def binom(n, k):
    return float(math.comb(n, k))

class StarCollective:
    """ROUTE S: the derived 2(d+1) reduction of a star K_{1,d}.

    Basis |z> (x) |D^d_m>, z in {0,1} with Z_0 = +1 / -1, and |D^d_m> the Dicke
    state with m arms in |1>.  The frozen Hamiltonian restricted to this space is

        H = - Z_0 (d - 2m)  - lambda X_0  - lambda * (raising + lowering)

    with <D_{m+1}|sum_j X_j|D_m> = sqrt((m+1)(d-m)).  The frozen preparation
    |+>^(x)(d+1) is symmetric, so the evolution never leaves the subspace
    The present note proves invariance; original leakage figures remain historical.
    """

    def __init__(self, d, lam, lam_pointer=None, lam_arm=None):
        self.d = d
        self.lam = lam
        self.lp = lam if lam_pointer is None else lam_pointer
        self.la = lam if lam_arm is None else lam_arm
        D = d + 1
        N = 2 * D
        H = np.zeros((N, N))

        def ix(z, m):
            return z * D + m

        for z in (0, 1):
            zs = 1.0 if z == 0 else -1.0
            for m in range(D):
                H[ix(z, m), ix(z, m)] += -zs * (d - 2 * m)
                if m + 1 < D:
                    v = -self.la * math.sqrt((m + 1) * (d - m))
                    H[ix(z, m + 1), ix(z, m)] += v
                    H[ix(z, m), ix(z, m + 1)] += v
            for m in range(D):
                H[ix(1 - z, m), ix(z, m)] += -self.lp
        self.H = H
        self.w, self.V = np.linalg.eigh(H)
        a = np.array([math.sqrt(binom(d, m)) for m in range(D)]) / math.sqrt(2.0 ** d)
        psi0 = np.zeros(N, dtype=complex)
        psi0[0:D] = a / math.sqrt(2.0)
        psi0[D:2 * D] = a / math.sqrt(2.0)
        self.c = self.V.conj().T @ psi0
        self._sqrtC = np.array([math.sqrt(binom(d, m)) for m in range(D)])
        self._cache = {}

    # ---- amplitudes -------------------------------------------------------
    def amplitudes(self, t):
        """Return (p, x) with p the pointer Z-distribution and x[z] the (d+1)-term
        SYMMETRIC-TENSOR amplitude sequence x_m = a_m / sqrt(C(d,m)) of branch z."""
        D = self.d + 1
        psi = self.V @ (np.exp(-1j * self.w * t) * self.c)
        ps, xs = [], []
        for z in (0, 1):
            a = psi[z * D:(z + 1) * D]
            p = float(np.vdot(a, a).real)
            ps.append(p)
            an = a / math.sqrt(p) if p > 1e-300 else a
            xs.append(an / self._sqrtC)
        tot = sum(ps)
        return [q / tot for q in ps], xs

    # ---- the Hankel block (933's object) ----------------------------------
    def hankel(self, x, k):
        d = self.d
        M = np.empty((k + 1, d - k + 1), dtype=complex)
        for m in range(k + 1):
            cm = math.sqrt(binom(k, m))
            for q in range(d - k + 1):
                M[m, q] = cm * math.sqrt(binom(d - k, q)) * x[m + q]
        return M

    def branch_rho(self, x, k):
        M = self.hankel(x, k)
        R = M @ M.conj().T
        tr = float(np.trace(R).real)
        return R / tr if tr > 0 else R

    # ---- the pointer-side statistics, derived -----------------------------
    def stats(self, t, kmax=2):
        key = (round(float(t), 15), kmax)
        if key in self._cache:
            return self._cache[key]
        p, xs = self.amplitudes(t)
        out = {"p_z": p, "H_Z": h2(p[0])}
        s = {}
        chi = {}
        for k in range(1, min(kmax, self.d) + 1):
            rzs = [self.branch_rho(xs[z], k) for z in (0, 1)]
            sv = [ent_of_spectrum(np.linalg.eigvalsh(r)) for r in rzs]
            s[k] = float(sum(pz * e for pz, e in zip(p, sv)))
            mix = p[0] * rzs[0] + p[1] * rzs[1]
            chi[k] = float(ent_of_spectrum(np.linalg.eigvalsh(mix)) - s[k])
        out["s"] = s
        out["chi"] = chi
        out["chi1"] = chi.get(1)
        out["s1"] = s.get(1)
        out["s2"] = s.get(2)
        out["C_ab"] = (2.0 * s[1] - s[2]) if (1 in s and 2 in s) else None
        self._cache[key] = out
        return out

    # ---- the frozen gate conjunction, evaluated in the reduction ----------
    def gates(self, t, delta=HEADLINE_DELTA):
        st = self.stats(t)
        H = st["H_Z"]
        c1 = st["chi1"]
        exc = c1 - self.chi0
        content = (H >= CONTENT_H_MIN and c1 >= (1.0 - delta) * H and exc >= EXCESS_MIN)
        cab = st["C_ab"]
        indep = (cab is not None and cab <= INDEP_MAX)
        # R_ind >= 2 needs TWO content-passing fragments whose own pair is under
        # the gate.  On a star every arm is a singleton fragment and all arms are
        # exchangeable, so this is (d >= 2) and content and independence.
        cert = bool(self.d >= 2 and content and indep)
        return {"t": t, "H_Z": H, "chi1": c1, "excess": exc, "C_ab": cab,
                "m_H": H - CONTENT_H_MIN,
                "m_content": c1 - (1.0 - delta) * H,
                "m_excess": exc - EXCESS_MIN,
                "m_indep": (None if cab is None else INDEP_MAX - cab),
                "content": bool(content), "indep": bool(indep), "cert": cert}

    @property
    def chi0(self):
        if not hasattr(self, "_chi0"):
            self._chi0 = self.stats(0.0)["chi1"]
        return self._chi0

    def cert(self, t, delta=HEADLINE_DELTA):
        return self.gates(t, delta)["cert"]

def chi1_single_arm_closed(t, lam_arm):
    """With the pointer's own transverse term switched off, Z_0 is conserved, each
    branch is a PRODUCT of d identical single-qubit states, and the single-arm
    Holevo information is a two-level formula with NO d in it at all."""
    v = []
    for s in (+1.0, -1.0):
        H = -s * SIG_Z - lam_arm * SIG_X
        w, V = np.linalg.eigh(H)
        c = V.conj().T @ (np.array([1.0, 1.0], dtype=complex) / math.sqrt(2.0))
        v.append(V @ (np.exp(-1j * w * t) * c))
    ov = abs(complex(np.vdot(v[0], v[1])))
    return h2(0.5 * (1.0 + min(1.0, ov)))

def content_threshold_overlap(delta=HEADLINE_DELTA):
    """c* in (0,1) with h2((1+c*)/2) = 1 - delta -- the ZERO-FIELD content edge."""
    lo, hi = 0.0, 1.0 - 1e-15
    for _ in range(300):
        mid = 0.5 * (lo + hi)
        if h2(0.5 * (1.0 + mid)) > (1.0 - delta):
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)

def zero_field_window(delta=HEADLINE_DELTA):
    c = content_threshold_overlap(delta)
    t0 = 0.5 * math.acos(c)
    return {"c_star": c, "t_open": t0, "t_close": math.pi / 2.0 - t0,
            "width": math.pi / 2.0 - 2.0 * t0}

def bisect_scalar(f, a, b, tol=EDGE_TOL):
    fa, fb = f(a), f(b)
    if fa == 0.0:
        return a
    if fb == 0.0:
        return b
    if (fa > 0) == (fb > 0):
        return None
    for _ in range(400):
        m = 0.5 * (a + b)
        fm = f(m)
        if (fm > 0) == (fa > 0):
            a, fa = m, fm
        else:
            b, fb = m, fm
        if abs(b - a) < tol:
            break
    return 0.5 * (a + b)

def edges_by_brentq(cell, dt, lo=0.0, hi=1.3):
    """Locate the certifiable interval by scanning and then BRENTQ on the binding
    margin -- a different root finder acting on a different function."""
    ts = [lo + k * dt for k in range(int(round((hi - lo) / dt)) + 1)]
    flags = [cell.cert(t) for t in ts]
    blocks, cur = [], None
    for i, f in enumerate(flags):
        if f and cur is None:
            cur = i
        elif not f and cur is not None:
            blocks.append((cur, i - 1))
            cur = None
    if cur is not None:
        blocks.append((cur, len(flags) - 1))
    out = []
    for (i, j) in blocks:
        def binding_margin(t):
            m = cell.margins(t)
            c = [m["m_H"], m["m_chi"], m["m_exc"]]
            if m["m_ind"] is not None:
                c.append(m["m_ind"])
            if len(m["passes"]) < 2:
                return min(m["m_H"], m["m_chi"], m["m_exc"])
            return min(c)
        a = (ts[i - 1] if i > 0 else None)
        b = (ts[j + 1] if j + 1 < len(ts) else None)
        lo_e = (lo if a is None else sopt.brentq(binding_margin, a, ts[i],
                                                 xtol=1e-14, rtol=8.9e-16, maxiter=300))
        hi_e = (ts[j] if b is None else sopt.brentq(binding_margin, ts[j], b,
                                                    xtol=1e-14, rtol=8.9e-16, maxiter=300))
        out.append({"lo": float(lo_e), "hi": float(hi_e), "width": float(hi_e - lo_e)})
    return out


class SampledCell:
    """Adapter for the actual932 counter, at one supplied delta."""
    def __init__(self, collective, delta=.1):
        self.collective=collective;self.delta=delta
    def cert(self,t):return self.collective.cert(t,self.delta)
    def margins(self,t):
        g=self.collective.gates(t,self.delta)
        return {'m_H':g['m_H'],'m_chi':g['m_content'],'m_exc':g['m_excess'],
                'm_ind':g['m_indep'],'passes':list(range(self.collective.d)) if g['content'] else []}


class PlantedIntervals:
    """The original C5 advertised two-interval predicate, now executable."""
    intervals=((.6,.9),(1.8,2.1))
    def margin(self,t):return max(min(t-a,b-t) for a,b in self.intervals)
    def cert(self,t):return self.margin(t)>=0
    def margins(self,t):
        v=self.margin(t)
        return {'m_H':v,'m_chi':v,'m_exc':v,'m_ind':v,'passes':[0,1]}


def revival_control(counter):
    blocks=counter(PlantedIntervals(),.05,lo=0.,hi=3.)
    expected=PlantedIntervals.intervals
    ok=len(blocks)==2 and all(abs(b['lo']-a)<1e-10 and abs(b['hi']-z)<1e-10 for b,(a,z) in zip(blocks,expected))
    return bool(ok),blocks


def sampled_verdict(flags,times,*,x_control_ok,commutator_ordering_ok,drift_ok):
    """Exact first-event discrete rule with explicitly supplied control clauses."""
    if len(flags)!=len(times) or any(b<=a for a,b in zip(times,times[1:])):
        raise ValueError('ordered grid and one flag per sample required')
    if not all(type(x) is bool for x in [x_control_ok,commutator_ordering_ok,drift_ok]):
        raise ValueError('full protocol control clauses must be explicitly supplied booleans')
    first=next((i for i,flag in enumerate(flags) if flag),None);run=0
    if first is not None:
        for flag in flags[first:]:
            if not flag:break
            run+=1
    yes=first is not None and times[first]<=1.+1e-12 and run>=3 and x_control_ok and commutator_ordering_ok and drift_ok
    return {'first_time':None if first is None else times[first],'run':run,'verdict':'YES' if yes else 'NO'}


def sampled_union(windows,times):
    """Use union membership before counting consecutive discrete samples."""
    return [any(w['lo']-1e-12<=t<=w['hi']+1e-12 for w in windows) for t in times]


def one_interval_count(a,b,phase,h):
    """Infinite-grid integer count; finite-horizon clipping must occur first."""
    if h<=0 or b<a:raise ValueError('positive spacing and ordered interval required')
    return max(0,math.floor((b-phase)/h+1e-12)-math.ceil((a-phase)/h-1e-12)+1)


def accepted(checks,refutations):
    return bool(checks) and all(x is True for x in checks.values()) and not refutations
