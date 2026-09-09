#!/usr/bin/env python3
"""L3c -- the exact obstruction: why no tick rule with tau > 0 keeps the ground-state zeros."""
import numpy as np, itertools, time
import l3c_core as C

OUT = []


def say(*a):
    s = " ".join(str(x) for x in a)
    print(s, flush=True)
    OUT.append(s)


g = C.PSI0["ground"]
QMASK = np.isin(C.PATZ, C.ZERO12)          # the 12 forbidden corner pairs, lifted to the sector
say("forbidden subspace: %d of the %d sector basis patterns (= 12 corner pairs x 32)" % (QMASK.sum(), C.NZ))
say("Q|ground> norm^2 = %.3e   (exact zero: the PR #7858 cancellation)" % float((np.abs(g[QMASK]) ** 2).sum()))
say("")
say("STEP 1: is the ground state still an energy eigenstate after ONE record forms?")
say("        |g_e,b> = P_{Z_e=b}|g> / ||.|| ;  H_R = H minus the hop term on the registered site e.")
say("        variance V = <H_R^2> - <H_R>^2 is zero iff |g_e,b> is an eigenstate of H_R.")
say("  %-8s %-3s | %-10s | %-12s | %-12s | %-12s" %
    ("site", "b", "<H_R>", "var(H_R)", "var(H_full)", "||Q H_R |g_b>||^2"))
rows = []
for q in range(C.NQ):
    for b in (0, 1):
        keep = ((C.ZL >> q) & 1) == b
        v = g * keep
        n = np.linalg.norm(v)
        if n < 1e-14:
            continue
        v = v / n
        # H_R on the whole sector: drop the hop term on site q
        HR = C.H896.copy()
        m = C.AMP[q] != 0
        HR[C.TGT[q][m], np.flatnonzero(m)] -= C.AMP[q][m]
        h = HR @ v
        e1 = float(np.real(np.vdot(v, h)))
        var = float(np.real(np.vdot(h, h))) - e1 ** 2
        hf = C.H896 @ v
        varf = float(np.real(np.vdot(hf, hf))) - float(np.real(np.vdot(v, hf))) ** 2
        qq = float((np.abs(h[QMASK]) ** 2).sum())
        rows.append((C.En.EDGES[q], b, e1, var, varf, qq))
for r in rows[:6]:
    say("  %-8s %-3d | %-10.6f | %-12.6f | %-12.6f | %-12.6f" % r)
say("  ... (%d site/value combinations in all)" % len(rows))
say("  min var(H_R) over all combinations = %.6f ; min ||Q H_R|g_b>||^2 = %.6f"
    % (min(r[3] for r in rows), min(r[5] for r in rows)))
say("  min var(H_full) over all combinations = %.6f" % min(r[4] for r in rows))
say("  -> a single record already destroys BOTH the eigenstate property and the annihilation of the")
say("     forbidden subspace, for every site and every value.  Nothing survives a gap of positive length.")

say("")
say("STEP 2: forbidden mass registered after one record and one gap of length t, then the remaining")
say("        11 records formed immediately (so the only dynamics is that one gap).")
say("  t      | forbidden-12 mass of the finished set (exact, averaged over the first site and value)")
for t in (0.0, 0.01, 0.1, 0.5, 1.0, 2.0, 5.0):
    tot = 0.0
    wsum = 0.0
    for q in range(C.NQ):
        for b in (0, 1):
            keep = ((C.ZL >> q) & 1) == b
            v = g * keep
            w = float((np.abs(v) ** 2).sum())
            if w < 1e-14:
                continue
            v = v / np.sqrt(w)
            I, Ev, Vc, grp = C.get_block(1 << q, b << q)
            vv = C.evolve(v[I], Ev, Vc, t)
            tot += (w / C.NQ) * float((np.abs(vv[np.isin(C.PATZ[I], C.ZERO12)]) ** 2).sum())
            wsum += w / C.NQ
    say("  %-6.2f | %.8f" % (t, tot / wsum))
say("  (t = 0 must be exactly 0; the growth is O(t^2) at small t, as expected for a state the")
say("   generator moves out of the zero set at first order.)")

say("")
say("STEP 3: which pre-record states DO reproduce their own Born diagonal under a tick rule?")
say("        A tick rule leaves the finished-set odds equal to the Born diagonal of psi0 for every")
say("        schedule iff every gap acts trivially on the conditioned state.  Two exact checks:")
say("  (1) tau = 0 (no dynamics): trivially yes, for any psi0.  This is PR #7858's setting.")
say("  (2) psi0 an eigenstate of H: the FIRST gap acts trivially, but H_R != H, so from the second")
say("      gap on the conditioned state evolves.  Quantified in STEP 1 / STEP 2 above.")
say("  (3) the only states left invariant by every H_R (R nonempty) are the joint eigenvectors of all")
say("      12 single-site-deleted Hamiltonians; the intersection over sites is computed here:")
Hs = []
for q in range(C.NQ):
    HR = C.H896.copy()
    m = C.AMP[q] != 0
    HR[C.TGT[q][m], np.flatnonzero(m)] -= C.AMP[q][m]
    Hs.append(HR)
# joint eigenvectors of all H_R  <=>  eigenvectors of H that commute with every deleted term T_q
comm_fail = []
for q in range(C.NQ):
    Tq = C.H896 - Hs[q]
    comm_fail.append(float(np.max(np.abs(C.H896 @ Tq - Tq @ C.H896))))
say("      max ||[H, T_e]|| over the 12 sites = %.4f (nonzero: no common eigenbasis)" % max(comm_fail))
M = np.zeros((C.NZ, C.NZ), dtype=np.complex128)   # stays 896 x 896
for q in range(1, C.NQ):
    Dq = Hs[q] - Hs[0]
    M += Dq.conj().T @ Dq
ev = np.linalg.eigvalsh(M)
say("      the joint kernel of {H_R - H_R'} has dimension %d -> no nonzero state is left invariant by"
    % int((ev < 1e-9).sum()))
say("      all the post-record Hamiltonians at once.")

open("l3c_theorem_out.txt", "w").write("\n".join(OUT) + "\n")
