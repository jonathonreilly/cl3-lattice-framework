#!/usr/bin/env python3
"""Matter above the chosen half-filled sea: finite real source comparisons.
A: three supplied staggered/twist free seas, finite gaps and chiral projector identity.
B: real fixed-number particle-hole projectors, number and row-energy densities.
C: real chiral conjugation and bulk holonomy identities, no APS boundary map.
D: original finite FFT boxes, star averages, actual log fit, chosen amplitude
band0.02 and Richardson diagnostic; zero-total does not exclude higher multipoles.
E: candidate-specific readout failures; old gauge rows omit the twist seam.
F: imposed two-component span, not a physical orientation theorem.
R: charged-even alternative, fixed-Z energy witness, complex-row restriction,
and full actual edge-equation translation covariance. All physical preparation,
readout, response and clock choices remain supplied. Standalone; no parent run."""

from __future__ import annotations

import itertools
import sys

import numpy as np

AUDIT_TIMEOUT_SEC = 300

# Mutable proof/interpretation inputs are part of this runner's source identity.
AUDIT_INPUT_PATHS = ['docs/MATTER_ABOVE_THE_HALF_FILLED_SEA_ODD_AND_EVEN_DENSITIES_AND_THE_VACUUM_QUESTION_CONDITIONAL_BOUNDED_THEOREM_NOTE_2026-09-03.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/GRAVITY_WEAK_FIELD_SOURCE_RESPONSE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-11.md']
SOURCE_INPUT_SHA256 = {'docs/MATTER_ABOVE_THE_HALF_FILLED_SEA_ODD_AND_EVEN_DENSITIES_AND_THE_VACUUM_QUESTION_CONDITIONAL_BOUNDED_THEOREM_NOTE_2026-09-03.md': '5fd4d2f12542b11716dfdfe8dfecc523b714af38e6102d324b3ea716891ec771', 'docs/MINIMAL_AXIOMS_2026-06-29.md': '93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753', 'docs/GRAVITY_WEAK_FIELD_SOURCE_RESPONSE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-11.md': '71023af5e313037d74eb3efb56b0515c913e66947981950e1871b3acc398fdbf'}

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

# Historical amplitude reference;0.02 is the explicitly chosen amplitude band.
# The distinct historical exponent tolerance does not supply this criterion.
NOTE_STABLE = 0.3267
NOTE_BAND = 0.02
NOTE_FIXED_ROW = {32: 0.190, 48: 0.432, 64: 0.568}


# ============================================ the coarse lattice and its sea

def eta_ks(v, a):
    """Kawamoto-Smit link sign of the coarse bond (v, v + e_a), axes 0/1/2."""
    if a == 0:
        return 1
    if a == 1:
        return -1 if (v[0] & 1) else 1
    return -1 if ((v[0] + v[1]) & 1) else 1


def build(L, twist=(0, 0, 0)):
    """Coarse torus L^3 with the KS staggered sign field; twist[a] = 1 flips
    the bonds crossing the cut v_a = L-1 -> 0, changing one Wilson line and no
    face. Returns the symmetric integer hopping matrix and the site list."""
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


def best_twist(L):
    """The twist minimising the half-filling energy, and its energy ladder."""
    N = L ** 3 // 2
    rows = []
    for tw in itertools.product((0, 1), repeat=3):
        M, _, _ = build(L, tw)
        rows.append((tw, float(np.sum(np.linalg.eigvalsh(M)[:N]))))
    return min(rows, key=lambda r: r[1]), rows


SEA = {}


def sea(L):
    if L in SEA:
        return SEA[L]
    (tw, E), rows = best_twist(L)
    M, sites, idx = build(L, tw)
    w, U = np.linalg.eigh(M)
    N = L ** 3 // 2
    P = U[:, :N] @ U[:, :N].T
    eps = np.array([(-1.0) ** sum(v) for v in sites])
    SEA[L] = dict(M=M, w=w, U=U, P=P, sites=sites, idx=idx, tw=tw, E=E,
                  N=N, eps=eps, rows=rows)
    return SEA[L]


def group_A():
    got = {L: sea(L)["E"] for L in (4, 6, 8)}
    quoted = {4: -78.383672, 6: -258.857540, 8: -611.811768}
    dev = max(abs(got[L] - quoted[L]) for L in got)
    check("A1 [numerical, 1e-6] the half-filled staggered sea at its optimal twist on "
          "4^3/6^3/8^3 has E_sea = %.6f/%.6f/%.6f, the first two being the supplied "
          "filling datum's own values"
          % (got[4], got[6], got[8]), dev < 1e-6)

    S4 = sea(4)
    flat = float(np.max(np.abs(S4["M"] @ S4["M"] - 6 * np.eye(64))))
    perE = S4["E"] / 64.0
    check("A2 [exact] at L = 4 the optimal-twist field satisfies M^2 = 6 I as a 64x64 "
          "integer identity (residual %.0f), so every level is +-sqrt6 and E_sea/V is "
          "exactly -sqrt6/2 = %.9f (residual %.0e)"
          % (flat, -np.sqrt(6) / 2, abs(perE + np.sqrt(6) / 2)),
          flat == 0.0 and abs(perE + np.sqrt(6) / 2) < 1e-12)

    gaps, bl = {}, {}
    for L in (4, 6, 8):
        S = sea(L)
        gaps[L] = S["w"][S["N"]] - S["w"][S["N"] - 1]
        n = L // 2
        smin = min(3 * np.cos(2 * PI * (m + (0.5 if S["tw"][0] else 0.0)) / n)
                   for m in range(n))
        bl[L] = 2 * np.sqrt(max(6 + 2 * smin, 0.0))
    closed = {4: 2 * np.sqrt(6), 6: 2 * np.sqrt(3),
              8: 2 * np.sqrt(6 - 3 * np.sqrt(2))}
    dev_b = max(abs(gaps[L] - bl[L]) for L in gaps)
    dev_c = max(abs(gaps[L] - closed[L]) for L in gaps)
    check('A3 [numerical, 1e-13] the three finite gaps are 2 sqrt6 / 2 sqrt3 / 2 sqrt(6 - 3 sqrt2) = %.6f/%.6f/%.6f, matching the supplied reduced-zone formula 2 sqrt(6 + 2 min_q sum_a cos q_a) (%.0e); no continuum convergence estimate from three sizes'
          % (gaps[4], gaps[6], gaps[8], max(dev_b, dev_c)),
          dev_b < 1e-13 and dev_c < 1e-13
          and gaps[4] > gaps[6] > gaps[8] > 0)

    par = all((L ** 3 // 2) % 2 == 0 for L in (4, 6, 8))
    check('A4 [exact] V/2 = 32/108/256 is even; fixed-number neutrality and response P0 are separate choices', par)

    worst_n, worst_chi, worst_ph = 0.0, 0.0, 0.0
    for L in (4, 6, 8):
        S = sea(L)
        M, P, e = S["M"], S["P"], S["eps"]
        worst_n = max(worst_n, float(np.max(np.abs(np.diag(P) - 0.5))))
        worst_chi = max(worst_chi,
                        float(np.max(np.abs(e[:, None] * M * e[None, :] + M))))
        conj = e[:, None] * P * e[None, :]
        worst_ph = max(worst_ph,
                       float(np.max(np.abs(np.diag(P) + np.diag(conj) - 1.0))))
    check("A5 [exact/numerical, 1e-12] <n_v> = 1/2 at EVERY site of all three tori "
          "(%.0e), and its exact reason: the bipartite grading eps_v = (-1)^{v1+v2+v3} "
          "gives eps M eps = -M as an integer identity (%.0f), so P_vv + (eps P eps)_vv "
          "= 1 (%.0e) and P_vv = 1/2" % (worst_n, worst_chi, worst_ph),
          worst_n < 1e-12 and worst_chi == 0.0 and worst_ph < 1e-12)


# ================================================== B -- pairs above the sea

def wavepacket(L, S, v0, which, width=1.0):
    """Normalised Gaussian at v0 projected into the empty ('p') or the
    occupied ('h') orbitals of the half-filled sea."""
    g = np.zeros(L ** 3)
    for i, v in enumerate(S["sites"]):
        d2 = 0
        for a in range(3):
            dd = (v[a] - v0[a]) % L
            d2 += min(dd, L - dd) ** 2
        g[i] = np.exp(-d2 / (2 * width * width))
    sub = S["U"][:, S["N"]:] if which == "p" else S["U"][:, :S["N"]]
    psi = sub @ (sub.T @ g)
    return psi / np.linalg.norm(psi)


def excite(L, S, pk, hk):
    """One particle-hole pair above the sea: the one-body projector P', the
    number-density deviation rho, the local energy density eps_v, and E_exc."""
    P = S["P"]
    Pp = P - np.outer(hk, hk) + np.outer(pk, pk)
    D = Pp - P
    rho = np.diag(Pp) - 0.5
    epsv = np.sum(S["M"] * D, axis=1)
    Ee = float(pk @ S["M"] @ pk - hk @ S["M"] @ hk)
    return Pp, rho, epsv, Ee


def spread(prof, sites, L):
    """Periodic rms radius and inverse participation ratio of a profile."""
    p = prof / prof.sum()
    cen = []
    for a in range(3):
        ang = np.array([2 * PI * v[a] / L for v in sites])
        cen.append((np.arctan2(float((p * np.sin(ang)).sum()),
                               float((p * np.cos(ang)).sum())) % (2 * PI))
                   * L / (2 * PI))
    r2 = 0.0
    for a in range(3):
        d = np.array([(v[a] - cen[a]) % L for v in sites])
        r2 += float((p * np.minimum(d, L - d) ** 2).sum())
    return np.sqrt(r2), 1.0 / float((p ** 2).sum())


PAIRS = {}


def pairs8():
    if PAIRS:
        return PAIRS
    L = 8
    S = sea(L)
    U, N = S["U"], S["N"]
    PAIRS["orb"] = excite(L, S, U[:, N], U[:, N - 1]) + (U[:, N] ** 2,
                                                         U[:, N - 1] ** 2)
    for d in (1, 2, 3, 4):
        pk = wavepacket(L, S, (0, 0, 0), "p")
        hk = wavepacket(L, S, (d, 0, 0), "h")
        PAIRS[d] = excite(L, S, pk, hk) + (pk ** 2, hk ** 2)
    return PAIRS


def group_B():
    L = 8
    S = sea(L)
    R = pairs8()

    _, rho_o, eps_o, Ee_o, pp, hp = R["orb"]
    rp, ip = spread(pp, S["sites"], L)
    rh, ih = spread(hp, S["sites"], L)
    check("B1 [numerical, 1e-12] the band-edge orbital pair on 8^3 has E_exc = %.6f, "
          "the sea gap, and is DELOCALISED: IPR %.0f and %.0f of 512 sites, rms %.2f "
          "and %.2f" % (Ee_o, ip, ih, rp, rh),
          abs(Ee_o - (S["w"][S["N"]] - S["w"][S["N"] - 1])) < 1e-12
          and ip > 150 and ih > 150)

    sums, rmss = [], []
    for d in (1, 2, 3, 4):
        _, rho, epsv, Ee, pp, hp = R[d]
        sums.append(abs(float(rho.sum())))
        rmss += [spread(pp, S["sites"], L)[0], spread(hp, S["sites"], L)[0]]
    check("B2 [numerical, 1e-13] localised wavepackets on 8^3 -- particle from the "
          "empty orbitals, hole from the occupied ones, d = 1/2/3/4 -- have sum_v rho "
          "= 0 to %.0e for rho = <n_v> - 1/2, with rms %.2f to %.2f"
          % (max(sums + [abs(float(rho_o.sum()))]), min(rmss), max(rmss)),
          max(sums) < 1e-13 and abs(float(rho_o.sum())) < 1e-13
          and 1.5 < min(rmss) and max(rmss) < 1.9)

    devs, Es = [], []
    for k in ("orb", 1, 2, 3, 4):
        _, rho, epsv, Ee, _, _ = R[k]
        devs.append(abs(float(epsv.sum()) - Ee))
        Es.append(Ee)
    check("B3 [numerical, 1e-14] the local energy density eps_v = sum_{j~v} M_vj "
          "(P' - P)_vj carries the whole excitation: sum_v eps_v = E_exc to %.0e over "
          "all five pairs, E_exc %.4f to %.4f"
          % (max(devs), min(Es), max(Es)), max(devs) < 1e-14)

    neg_o = float(np.sum(eps_o[eps_o < 0]))
    neg4 = []
    for d in (1, 2, 3, 4):
        _, _, epsv, Ee, _, _ = R[d]
        neg4.append(100 * abs(float(np.sum(epsv[epsv < 0]))) / Ee)
    S4 = sea(4)
    p4 = wavepacket(4, S4, (0, 0, 0), "p")
    h4 = wavepacket(4, S4, (2, 0, 0), "h")
    _, _, eps4, _, = excite(4, S4, p4, h4)
    neg_4 = float(np.sum(eps4[eps4 < 0]))
    check('B4 [numerical, 1e-15] real row-energy negative part: exactly 0 for the orbital pair (%.0e) and on 4^3 (%.0e), and %.1f%% to %.1f%% of E_exc for the selected wavepackets; no general positivity'
          % (abs(neg_o), abs(neg_4), min(neg4), max(neg4)),
          abs(neg_o) < 1e-15 and abs(neg_4) < 1e-15 and max(neg4) < 0.4)

    abs_sums = [float(np.abs(R[k][1]).sum()) for k in ("orb", 1, 2, 3, 4)]
    check("B5 [numerical] the clouds OVERLAP: sum_v |rho| runs %.2f to %.2f, under "
          "the 2 a disjoint unit particle and hole would give"
          % (min(abs_sums), max(abs_sums)), max(abs_sums) < 2.0)


# ================================================== C -- conjugation and flux

def group_C():
    L = 8
    S = sea(L)
    M, P, e = S["M"], S["P"], S["eps"]
    R = pairs8()
    dr, de = 0.0, 0.0
    for k in ("orb", 1, 2, 3, 4):
        Pp, rho, epsv, _, _, _ = R[k]
        Pc = e[:, None] * (np.eye(L ** 3) - Pp) * e[None, :]
        dr = max(dr, float(np.max(np.abs((np.diag(Pc) - 0.5) + rho))))
        de = max(de, float(np.max(np.abs(np.sum(M * (Pc - P), axis=1) - epsv))))
    check("C1 [exact] conjugation P' -> eps (I - P') eps sends rho -> -rho (%.0e) and "
          "eps_v -> +eps_v (%.0e) over all five pairs: the number-density deviation is "
          "the ODD datum, the energy density the EVEN one"
          % (dr, de), dr < 1e-15 and de < 1e-15)

    tw, sites = S["tw"], S["sites"]

    def base(v, a):
        s = eta_ks(v, a)
        return -s if (tw[a] and v[a] == L - 1) else s

    def gauged(v, a):
        w = tuple((v[i] + EX[a][i]) % L for i in range(3))
        return base(v, a) * ((-1) ** sum(v)) * ((-1) ** sum(w))

    def holonomies(sign):
        out = []
        for v in sites:
            for (a, b) in ((0, 1), (0, 2), (1, 2)):
                v1 = tuple((v[i] + EX[a][i]) % L for i in range(3))
                v2 = tuple((v[i] + EX[b][i]) % L for i in range(3))
                out.append(sign(v, a) * sign(v1, b) * sign(v2, a) * sign(v, b))
        return np.array(out)

    h0, h1 = holonomies(base), holonomies(gauged)
    flips = all(gauged(v, a) == -base(v, a) for v in sites for a in range(3))
    wl = []
    for a in range(3):
        for sgn in (base, gauged):
            pr = 1
            for t in range(L):
                v = tuple(t * EX[a][i] for i in range(3))
                pr *= sgn(v, a)
            wl.append(pr)
    same_wl = all(wl[2 * a] == wl[2 * a + 1] for a in range(3))
    check("C2 [exact] eps is a diagonal +-1 gauge map: it flips all %d link signs, yet "
          "all %d faces of 8^3 keep their holonomy (%d) and every even Wilson line is "
          "fixed (%s) -- a state and its conjugate lie in the SAME flux sector"
          % (3 * L ** 3, len(h0), int(np.max(np.abs(h0 - h1))), same_wl),
          flips and int(np.max(np.abs(h0 - h1))) == 0 and same_wl)


# =============================================================== D -- response

_GC = {}


def ghat(Lb):
    k = 2 * PI * np.fft.fftfreq(Lb)
    lam = 6 - 2 * (np.cos(k)[:, None, None] + np.cos(k)[None, :, None]
                   + np.cos(k)[None, None, :])
    G = np.zeros_like(lam)
    nz = lam > 1e-12
    G[nz] = 1.0 / lam[nz]
    G[0, 0, 0] = 0.0
    return G


def green(Lb):
    if Lb not in _GC:
        _GC[Lb] = np.real(np.fft.ifftn(ghat(Lb)))
    return _GC[Lb]


def solve(rho, Gh):
    """phi = G0 P0 rho; P0 is automatic because Ghat[0] = 0."""
    return np.real(np.fft.ifftn(np.fft.fftn(rho) * Gh))


def star(phi, r):
    """Cubic-star average over the six +-r offsets: kills l = 1 and l = 3."""
    return float(phi[r, 0, 0] + phi[-r, 0, 0] + phi[0, r, 0] + phi[0, -r, 0]
                 + phi[0, 0, r] + phi[0, 0, -r]) / 6.0


def antix(phi, r):
    """x-antisymmetric part: kills l = 0 and l = 2."""
    return float(phi[r, 0, 0] - phi[-r, 0, 0]) / 2.0


def unwrapped(vec, sites, L, about):
    """Offsets from `about`, unwrapped through the physical torus seam."""
    out = []
    for i, v in enumerate(sites):
        q = []
        for a in range(3):
            t = (v[a] - about[a]) % L
            q.append(t - L if t > L // 2 else t)
        out.append((tuple(q), vec[i]))
    return out


def recentre(pairs):
    """Shift to the charge centroid (rounded); returns pairs, total, dipole."""
    q = sum(w for _, w in pairs)
    if abs(q) > 1e-9:
        c = np.round(np.array([sum(w * o[a] for o, w in pairs)
                               for a in range(3)]) / q).astype(int)
        pairs = [(tuple(o[a] - c[a] for a in range(3)), w) for o, w in pairs]
        q = sum(w for _, w in pairs)
    p = np.array([sum(w * o[a] for o, w in pairs) for a in range(3)])
    return pairs, q, p


def place(pairs, Lb):
    A = np.zeros((Lb, Lb, Lb))
    for o, w in pairs:
        A[o[0] % Lb, o[1] % Lb, o[2] % Lb] += w
    return A


SRC = {}


def sources():
    """The four candidate sources built from the d = 4 wavepacket pair on the
    physical 8^3 torus, unwrapped about the pair midpoint and re-centred."""
    if SRC:
        return SRC
    L = 8
    S = sea(L)
    _, rho, epsv, Ee, _, _ = pairs8()[4]
    mid = (2, 0, 0)
    for tag, vec in (("a", rho), ("b", epsv / Ee), ("c", np.abs(rho)),
                     ("d", np.maximum(rho, 0.0))):
        pr, q, p = recentre(unwrapped(vec, S["sites"], L, mid))
        SRC[tag] = (pr, q, p)
    SRC["Ee"] = Ee
    return SRC


def group_D():
    row = {N: 4 * PI * 10 * green(N)[10, 0, 0] for N in sorted(NOTE_FIXED_ROW)}
    ok_row = all(round(row[N], 3) == NOTE_FIXED_ROW[N] for N in row)
    check('D1 [numerical, 1e-3] finite historical reference comparison: 4 pi r G(r) at r = 10 rounds to %s at N = 32/48/64'
          % "/".join("%.3f" % row[N] for N in sorted(row)), ok_row)

    PT = {Lb: 4 * PI * (Lb // 4) * green(Lb)[Lb // 4, 0, 0]
          for Lb in (8, 16, 32, 64)}
    quoted = {8: 0.4065, 16: 0.3468, 32: 0.3307, 64: 0.3275}
    devp = max(abs(PT[Lb] - quoted[Lb]) for Lb in PT)
    check('D2 [numerical, 1e-4] finite point control: 4 pi r G at r = Lb/4 is %s at Lb = 8/16/32/64, against historical rows (%.0e)'
          % ("/".join("%.4f" % PT[Lb] for Lb in (8, 16, 32, 64)), devp),
          devp < 1e-4)

    SS = sources()
    pr_a, q_a, p_a = SS["a"]
    Gh = ghat(64)
    phi_a = solve(place(pr_a, 64), Gh)
    mono16 = 4 * PI * 16 * star(phi_a, 16)
    lg = np.array([[np.log(r), np.log(abs(antix(phi_a, r)))]
                   for r in (4, 5, 6, 8, 10, 12)])
    slope = float(np.polyfit(lg[:, 0], lg[:, 1], 1)[0])
    rats = {r: 4 * PI * r * r * antix(phi_a, r) / p_a[0] for r in (5, 8, 10)}
    check('D3 [numerical] fixed-N number source: total %.0e, star monopole %.0e at r = 16, dipole |p| = %.3f at d = 4, actual fitted log-log slope %.2f, 4 pi r^2 antisym_x phi / p_x = %s at r = 5/8/10; higher multipoles not excluded'
          % (abs(q_a), abs(mono16), float(np.linalg.norm(p_a)), slope,
             "/".join("%.4f" % rats[r] for r in (5, 8, 10))),
          abs(q_a) < 1e-12 and abs(mono16) < 1e-3
          and abs(slope + 2.0) < 0.05
          and all(abs(rats[r] - 1.0) < 0.01 for r in rats))
    del phi_a, Gh

    mono = {}
    for tag in ("b", "c", "d"):
        pr, q, _ = SS[tag]
        mono[tag] = {}
        for Lb in (8, 16, 32, 64):
            Gh = ghat(Lb)
            r = Lb // 4
            mono[tag][Lb] = 4 * PI * r * star(solve(place(pr, Lb), Gh), r) / q
            del Gh
    b = mono["b"]
    check('D4 [numerical, chosen amplitude band0.02] real energy source: 4 pi r phi at r = Lb/4 is %s at Lb = 8/16/32/64, outside the chosen band about0.3267 at8,16 and inside at32,64; the historical exponent tolerance is a distinct quantity'
          % "/".join("%.4f" % b[Lb] for Lb in (8, 16, 32, 64)),
          abs(b[8] - NOTE_STABLE) > NOTE_BAND
          and abs(b[16] - NOTE_STABLE) > NOTE_BAND
          and abs(b[32] - NOTE_STABLE) <= NOTE_BAND
          and abs(b[64] - NOTE_STABLE) <= NOTE_BAND)

    st = {}
    for Lb in (32, 64):
        Gh = ghat(Lb)
        pr, q, _ = SS["b"]
        st[Lb] = (solve(place(pr, Lb), Gh), q)
        del Gh
    rich = {}
    ctrl = {}
    for dd in (4, 6, 8, 10):
        f64, q64 = st[64]
        f32, q32 = st[32]
        rich[dd] = 4 * PI * dd * (2 * star(f64, dd) / q64 - star(f32, dd) / q32)
        ctrl[dd] = 4 * PI * dd * (2 * star(green(64), dd) - star(green(32), dd))
    check('D5 [numerical, finite Richardson protocol] 2 f_64 - f_32 gives coefficients %s at dd = 4/6/8/10 against the matched point control %s, agreeing to0.01 on these points only'
          % ("/".join("%.4f" % rich[dd] for dd in (4, 6, 8, 10)),
             "/".join("%.4f" % ctrl[dd] for dd in (4, 6, 8, 10))),
          all(abs(rich[dd] - ctrl[dd]) < 0.01 for dd in rich))

    check("D6 [numerical, band 0.02] the two non-linear positive candidates do the "
          "same: (c) |rho| and (d) rho_+ = max(rho, 0) read %.4f and %.4f at Lb = 64, "
          "inside the band and beside the point control %.4f"
          % (mono["c"][64], mono["d"][64], PT[64]),
          abs(mono["c"][64] - NOTE_STABLE) <= NOTE_BAND
          and abs(mono["d"][64] - NOTE_STABLE) <= NOTE_BAND)


# ========================================== E -- the five-clause source check

def encoding_masks(nblk=3):
    """F2 x-mask and z-mask of B_v and of one A_ij on an open nblk^3 coarse
    block, code qubits exactly the coarse edge sites, direction order
    -x < -y < -z < +x < +y < +z at every coarse vertex."""
    verts = list(itertools.product(range(nblk), repeat=3))
    edges = []
    for v in verts:
        for a in range(3):
            w = tuple(v[i] + EX[a][i] for i in range(3))
            if w in set(verts):
                edges.append((v, w))
    eid = {frozenset(e): i for i, e in enumerate(edges)}

    def order_at(u):
        """Incident edges of u in the declared direction order."""
        out = []
        for k, d in enumerate([(-1, 0, 0), (0, -1, 0), (0, 0, -1),
                               (1, 0, 0), (0, 1, 0), (0, 0, 1)]):
            w = tuple(u[i] + d[i] for i in range(3))
            if frozenset((u, w)) in eid:
                out.append((k, eid[frozenset((u, w))]))
        return [i for _, i in sorted(out)]

    def B(u):
        z = 0
        for i in order_at(u):
            z ^= 1 << i
        return 0, z

    def A(i, j):
        e = eid[frozenset((i, j))]
        z = 0
        for u in (i, j):
            for f in order_at(u):
                if f == e:
                    break
                z ^= 1 << f
        return 1 << e, z

    return verts, edges, B, A


def group_E():
    verts, edges, B, A = encoding_masks(3)
    ctr = (1, 1, 1)
    bx, bz = B(ctr)
    ax, az = A(ctr, (2, 1, 1))
    nsupp = bin(bz).count("1")
    # -B_v/2 is diagonal (no X), an involution times -1/2, and both signs are
    # attained on the six-qubit support: spectrum {-1/2, +1/2}.
    bits = [i for i in range(bz.bit_length()) if (bz >> i) & 1]
    diagvals = [(-1.0) ** bin(m).count("1") for m in range(1 << len(bits))]
    spec = sorted({round(-x / 2, 12) for x in diagvals})
    L6 = sea(6)
    M6, sites6, idx6 = L6["M"], L6["sites"], L6["idx"]
    perm = np.array([idx6[((v[0] + 1) % 6, v[1], v[2])] for v in sites6])
    sgn = np.array([(-1.0) ** (v[1] + v[2]) for v in sites6])
    Mp = np.zeros_like(M6)
    Mp[np.ix_(perm, perm)] = M6
    gauge_res = float(np.max(np.abs(Mp - sgn[:, None] * M6 * sgn[None, :])))
    p6 = wavepacket(6, L6, (0, 0, 0), "p")
    h6 = wavepacket(6, L6, (3, 0, 0), "h")
    _, rho6, eps6, _, = excite(6, L6, p6, h6)
    D6 = (np.outer(p6, p6) - np.outer(h6, h6))
    Dt = np.zeros_like(D6)
    Dt[np.ix_(perm, perm)] = D6
    Dg = sgn[:, None] * Dt * sgn[None, :]
    rho_sh = np.zeros(216)
    rho_sh[perm] = rho6
    eps_sh = np.zeros(216)
    eps_sh[perm] = eps6
    tr_rho = float(np.max(np.abs(np.diag(Dg) - rho_sh)))
    tr_eps = float(np.max(np.abs(np.sum(M6 * Dg, axis=1) - eps_sh)))
    tot = abs(float(sources()["a"][1]))
    check("E1 [exact] candidate (a) is the NAMED operator rho_v = <n_v> - 1/2 = "
          "-B_v/2: diagonal (x-mask %d), local on exactly %d coarse edge sites, phase "
          "invariant, covariant on the untwisted 6^3 (%.0f, %.0e); spectrum "
          "{%+.1f, %+.1f}, so NOT positive; total %.0e"
          % (bx, nsupp, gauge_res, tr_rho, spec[0], spec[1], tot),
          bx == 0 and nsupp == 6 and gauge_res == 0.0 and tr_rho < 1e-13
          and spec == [-0.5, 0.5] and tot < 1e-12)

    S8 = sea(8)
    sites8, idx8 = S8["sites"], S8["idx"]
    perm8 = np.array([idx8[((v[0] + 1) % 8, v[1], v[2])] for v in sites8])
    sgn8 = np.array([(-1.0) ** (v[1] + v[2]) for v in sites8])
    M8 = S8["M"]
    Mp8 = np.zeros_like(M8)
    Mp8[np.ix_(perm8, perm8)] = M8
    d8 = np.abs(Mp8 - sgn8[:, None] * M8 * sgn8[None, :])
    cutx = sorted({sites8[i][0] for i, _ in np.argwhere(d8 > 1e-9)})
    Pp8, _, eps8, _, _, _ = pairs8()[4]
    D8 = Pp8 - S8["P"]
    Dt8 = np.zeros_like(D8)
    Dt8[np.ix_(perm8, perm8)] = D8
    Dg8 = sgn8[:, None] * Dt8 * sgn8[None, :]
    eps8_sh = np.zeros(512)
    eps8_sh[perm8] = eps8
    cut_res = float(np.max(np.abs(np.sum(M8 * Dg8, axis=1) - eps8_sh)))
    check('E2 [finite real source] energy is offdiagonal: hop carries X on %d code qubit with %d trailing Zs; old KS-bulk-only translation omits twist seam and leaves residual %.1e on v_x %s, not an obstruction to full covariance'
          % (bin(ax).count("1"), bin(az).count("1"), cut_res, cutx),
          ax != 0 and cut_res > 1e-9 and cutx == [0, 1, 7])

    _, rho, _, _, _, _ = pairs8()[4]
    Pc = S8["eps"][:, None] * (np.eye(512) - Pp8) * S8["eps"][None, :]
    mixed = 0.5 * (Pp8 + Pc)
    rho_mix = np.diag(mixed) - 0.5
    lin = 0.5 * (np.abs(rho) + np.abs(np.diag(Pc) - 0.5))
    gapl = float(np.max(np.abs(np.abs(rho_mix) - lin)))
    check("E3 [exact] candidates (c) |rho| and (d) rho_+ are the expectation of NO "
          "operator, being non-linear in the state: on the equal mixture of a pair and "
          "its conjugate |rho| reads 0 where a linear functional reads the average, "
          "%.4f apart" % gapl,
          gapl > 1e-3 and float(np.max(np.abs(rho_mix))) < 1e-12)

    check("E4 [stated] so NEITHER linear-in-the-state candidate meets all five bridge "
          "clauses above this sea: (a) fails positivity, total zero; (b) fails "
          "diagonality; (c), (d) are positive with non-zero total but no operator "
          "expresses them", True)


# =========================================================== F -- signed sector

def group_F():
    basis = np.array([[1.0], [1.0]])
    target = np.array([1.0, -1.0])
    coef, *_ = np.linalg.lstsq(basis, target, rcond=None)
    resid = float(np.linalg.norm(basis @ coef - target))
    check('F1 [finite imposed-label span] manually supplied [+1,+1] has least-squares residual %.6f = sqrt2 to [+1,-1]; no APS boundary/operator/orientation map constructed' % resid,
          abs(resid - np.sqrt(2)) < 1e-12)

    S = sea(8)
    U, N, e, M = S["U"], S["N"], S["eps"], S["M"]
    conj = e * U[:, N]
    occ = float(np.linalg.norm(S["P"] @ conj))
    flip = abs(float(conj @ M @ conj) + float(U[:, N] @ M @ U[:, N]))
    check('F2 [finite chiral identity] conjugated empty orbital is in occupied shell (%.12f), energy negated (%.0e); bulk holonomies stay fixed, while an independently defined APS label remains untested'
          % (occ, flip), abs(occ - 1.0) < 1e-12 and flip < 1e-12)



def group_R():
    # Actual even charged projector, distinct from every fixed-N original pair.
    s=sea(4); v=s["U"][:,s["N"]:s["N"]+2]; charged=s["P"]+v@v.T
    charge=float(np.trace(charged-s["P"])); residue=float(np.max(abs(charged@charged-charged)))
    check("R1 [actual even alternative] adding two empty orbitals gives deltaN=%.12f, even total N34, projector residual %.1e" % (charge,residue), abs(charge-2)<1e-12 and residue<1e-12 and (s["N"]+2)%2==0)
    a=np.array([1.,1.])/np.sqrt(2);b=np.array([1.,-1.])/np.sqrt(2);m=np.array([[0.,1.],[1.,0.]])
    es=(float(a@m@a),float(b@m@b))
    check("R2 [readout counterexample] identical fixed-Z probabilities, offdiagonal energies %.12f / %.12f" % es, np.array_equal(a*a,b*b) and abs(es[0]-1)<1e-12 and abs(es[1]+1)<1e-12)
    m=np.array([[0.,1,0,0],[1,0,2,0],[0,2,0,3],[0,0,3,0]]);_,u=np.linalg.eigh(m);p=(u[:,2]+1j*u[:,3])/np.sqrt(2);h=u[:,1];delta=np.outer(p,p.conj())-np.outer(h,h);row=np.sum(m*delta,axis=1)
    check("R3 [domain counterexample] complex pair gives max imaginary row %.6f while total imaginary %.1e; original source restricted to real states" % (np.max(abs(row.imag)),abs(row.sum().imag)), np.max(abs(row.imag))>.1 and abs(row.sum().imag)<1e-14)
    s=sea(8);m=s["M"];perm=np.array([s["idx"][((v[0]+1)%8,v[1],v[2])] for v in s["sites"]]);mp=np.zeros_like(m);mp[np.ix_(perm,perm)]=m
    gauge=np.zeros(512);gauge[0]=1;todo=[0];consistent=True;edges=0
    while todo:
        i=todo.pop()
        for j in np.flatnonzero(m[i]):
            z=gauge[i]*mp[i,j]/m[i,j];edges+=1
            if gauge[j]==0:gauge[j]=z;todo.append(int(j))
            elif gauge[j]!=z:consistent=False
    mr=float(np.max(abs(mp-gauge[:,None]*m*gauge[None,:])))
    p=wavepacket(8,s,(0,0,0),'p');h=wavepacket(8,s,(4,0,0),'h');delta=np.outer(p,p)-np.outer(h,h);dt=np.zeros_like(delta);dt[np.ix_(perm,perm)]=delta;dg=gauge[:,None]*dt*gauge[None,:]
    old=np.sum(m*delta,axis=1);target=np.empty(512);target[perm]=old;er=float(np.max(abs(np.sum(m*dg,axis=1)-target)))
    check("R4 [actual full gauge] all %d directed edge equations, matrix residual %.0e and real energy translation %.1e; twist seam included" % (edges,mr,er), edges==3072 and consistent and np.all(abs(gauge)==1) and mr==0 and er<1e-14)

def main():
    for g in (group_A, group_B, group_C, group_D, group_E, group_F, group_R):
        g()
    print("SUMMARY: supplied real fixed-N source comparisons; charged even and full-covariance alternatives remain. No physical readout, gravity or APS theorem.")
    print("per_element: checked finite source sums and exact stated scalar identities; physical interpretation is not supplied")
    print("per_site: checked declared coordinate/record/source dictionaries on finite sites; no fine-site formation mechanism follows")
    print("per_mode: checked the stated one-particle or Fourier modes only; no unexecuted interacting or APS boundary spectrum")
    print("per_block: checked named finite preparations, response boxes or sign-field families at their stated tolerances")
    print("lattice_wide: checked and not executed — no physical infinite-volume formation law or numerical limit error bound is certified")
    print("TOTAL: PASS=%d FAIL=%d" % (PASS, FAIL))
    return 1 if FAIL else 0


if __name__ == "__main__":
    sys.exit(main())
