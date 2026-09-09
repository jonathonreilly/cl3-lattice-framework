#!/usr/bin/env python3
"""L3c -- what a tick does when record formation is interleaved with pre-record hopping."""
import sys, time, math, itertools
import numpy as np
import l3c_core as C
import l3c_run as R

T0 = time.time()
OUT = []


def say(*a):
    s = " ".join(str(x) for x in a)
    print(s, flush=True)
    OUT.append(s)


def hdr(s):
    say("")
    say("#" * 108)
    say(s)
    say("#" * 108)


NT = 20000
TAUS = (0.1, 0.5, 2.0)
PS = (0.5, 0.2, 0.05, 0.01)
STATES = ("ground", "pair01", "unif28")
LAB = {"ground": "(a) hopping ground state E=-4",
       "pair01": "(b) localised A-string pair (0,1)",
       "unif28": "(c) uniform over the 28 pair states"}

# ================================================================= 0  the model
hdr("SECTION 0  the declared model")
say("cluster            : 2x2x2 cube, 8 corners, 12 edge sites -> 12 qubits, dim 4096 (BKSF, L3/L3b verified)")
say("stabilizers        : %d independent face operators; code space 2^7 = 128" % C.KSTAB)
say("state space used   : the N=2 record sector = span{|z> : corner-parity pattern has weight 2}, dim %d = 28 x 32."
    % C.NZ)
say("                     every hop term preserves it exactly, so nothing above %dx%d is ever formed." % (C.NZ, C.NZ))
say("pre-record H       : H = sum_edges T_e, T_e = (i/2) A_e (B_i - B_j); code-sector spectrum {-4,-2,0,2,4},")
say("                     ground level -4.  On the whole %d-dim sector (32 flux copies) the extreme level is -(2+2sqrt2)." % C.NZ)
say("TICK               : (i) every unrecorded edge site forms a record with probability p, independently;")
say("                         each locks a value with the odds carried by the current state (Lueders conditioning,")
say("                         sequential in a random order inside the tick);")
say("                     (ii) the pre-record state then evolves by exp(-i tau H_R).")
say("MODEL CHOICE A     : H_R = sum of hop terms on UNRECORDED sites (exactly the terms commuting with every")
say("                     registered Z_e, since T_e is the only term with X support on site e).  Primary model.")
say("MODEL CHOICE B     : keep the full H each step and re-condition on the registered values afterwards. Tested.")
say("clock              : site e's formation tick is Geometric(p); the finished set is complete at tick max_e T_e.")
say("dictionary         : the finished set of 12 locked values fixes one of the 28 corner pairs (vertex pattern).")

# ================================================================= 1  sanity
hdr("SECTION 1  sanity: p = 1 (every record forms at the first tick)")
say("At p = 1 no evolution precedes any record, so the finished set must reproduce the Born diagonal of the")
say("initial state exactly.  Exact facts first:")
say("  ground state Born diagonal: %d patterns at 1/16 = %.6f, %d patterns at exactly 0."
    % (int((C.GS_BORN > 1e-12).sum()), 1 / 16, len(C.ZERO12)))
say("  the %d zeros are the discriminator's forbidden corner pairs: %s"
    % (len(C.ZERO12), [C.PAIRS[i] for i in C.ZERO12]))
say("  they are the pairs whose two corners lie on the SAME x-face {0,1,2,3} or {4,5,6,7}.")
say("  in the 4096-dim edge-pattern space that is %d x 32 = %d cancellation zeros (PR #7858)."
    % (len(C.ZERO12), 32 * len(C.ZERO12)))
for nm in STATES:
    b = C.born_patterns(C.PSI0[nm])
    c, tk = R.run(nm, 1.0, 0.5, NT, seed=101, mode="drop")
    st = R.stats(c, b)
    say("  MC p=1 %-8s n=%d : L1 to its own Born diagonal = %.4f +- %.4f ; ticks to completion = %d (exact 1)"
        % (nm, NT, st["d_rf"], st["b_rf"], tk.max()))
    if nm == "ground":
        say("           forbidden-12 registered mass = %.5f (exact 0), max over the 12 = %.5f"
            % (st["fmass"], st["p"][C.ZERO12].max()))

say("")
say("tau = 0 control (dynamics switched off): the finished set must be the Born diagonal for every p.")
for p in (0.2, 0.01):
    c, tk = R.run("ground", p, 0.0, 4000, seed=77)
    say("  tau=0 p=%.2f : L1 to ground Born = %.4f ; forbidden-12 mass = %.5f"
        % (p, C.l1(c / c.sum(), C.GS_BORN), c[C.ZERO12].sum() / c.sum()))

say("")
say("order independence INSIDE one tick (all Z_e commute, so Lueders projections commute):")
bad = 0
tests = 0
for nm in STATES:
    psi = C.evolve(C.PSI0[nm], *C.get_block(0, 0)[1:3], 0.37)   # a generic non-stabilizer pre-record state
    I0 = C.get_block(0, 0)[0]
    for trio in ((0, 1, 2), (3, 7, 11), (2, 5, 9)):
        for vals in itertools.product((0, 1), repeat=3):
            ref = None
            for perm in itertools.permutations(range(3)):
                v = psi
                I = I0
                for t in perm:
                    keep = ((C.ZL[I] >> trio[t]) & 1) == vals[t]
                    v = v[keep]
                    I = I[keep]
                if ref is None:
                    ref = (v, I)
                else:
                    tests += 1
                    if len(I) != len(ref[1]) or not np.array_equal(I, ref[1]) or np.max(np.abs(v - ref[0])) > 1e-13:
                        bad += 1
say("  %d ordered comparisons over 3-site groups on evolved states of all three initial states: mismatches %d"
    % (tests, bad))

# ================================================================= 2  main grid
hdr("SECTION 2  the finished-set statistics, tick model, %d trajectories per point" % NT)
say("columns: mean ticks to completion | # of the 28 patterns with odds < 1e-3 | # with zero registrations |")
say("         L1 to the ground-state Born diagonal | L1 to uniform-on-28 | mass on the 12 forbidden pairs")
GRID = {}
for nm in STATES:
    say("")
    say("initial state %s" % LAB[nm])
    born = C.born_patterns(C.PSI0[nm])
    say("  %-5s %-5s | %8s | %5s %5s | %-16s | %-16s | %-18s" %
        ("p", "tau", "E[ticks]", "<1e-3", "zero", "L1 to GS Born", "L1 to uniform", "forbidden-12 mass"))
    for p in PS:
        for tau in TAUS:
            t0 = time.time()
            c, tk = R.run(nm, p, tau, NT, seed=hash((nm, p, tau)) % (2 ** 31), mode="drop")
            st = R.stats(c, born)
            GRID[(nm, p, tau)] = (c, st, tk)
            say("  %-5.2f %-5.1f | %8.1f | %5d %5d | %.4f +- %.4f | %.4f +- %.4f | %.5f +- %.5f   [%.0fs]"
                % (p, tau, tk.mean(), st["below"], st["zeros"], st["d_gs"], st["b_gs"],
                   st["d_un"], st["b_un"], st["fmass"], st["fse"], time.time() - t0))

np.save("grid_counts.npy", np.array([GRID[k][0] for k in sorted(GRID, key=str)]))

# ================================================================= 3  regimes
hdr("SECTION 3  the three regimes")
say("(i)  fast-formation limit p -> 1 : the finished set is the Born diagonal of the initial state (Section 1).")
say("")
say("(ii) slow-formation limit p -> 0 at fixed tau.  The gap before each record diverges, so the pre-record")
say("     state fully dephases in the energy basis of the CURRENT H_R, and records form one at a time in a")
say("     uniformly random site order.  That limiting process is simulated exactly (random-phase unravelling")
say("     of  rho -> sum_E P_E rho P_E  at every gap).")
say("")
say("     Exact single-dephasing comparison  sum_E P_E |psi0><psi0| P_E  (dephasing w.r.t. the FULL H only):")
DEPH_EX = {}
for nm in STATES:
    d = C.dephased_patterns(C.PSI0[nm])
    DEPH_EX[nm] = d
    say("       %-8s : L1(dephased(psi0), Born(psi0)) = %.4f ; L1(dephased, uniform) = %.4f ; forbidden-12 mass = %.6f"
        % (nm, C.l1(d, C.born_patterns(C.PSI0[nm])), C.l1(d, C.UNIF28), d[C.ZERO12].sum()))
say("     (for the ground state this is the identity map: an energy eigenstate is invariant under the dephasing.)")
say("")
say("     Simulated p -> 0 limit (sequential dephasing, %d trajectories):" % NT)
DEPH = {}
for nm in STATES:
    t0 = time.time()
    c = R.run_deph(nm, NT, seed=4242)
    st = R.stats(c, DEPH_EX[nm])
    DEPH[nm] = (c, st)
    say("       %-8s : <1e-3 %2d | zero %2d | L1 to GS Born %.4f | L1 to uniform %.4f | L1 to single-dephased(psi0) %.4f"
        " | forbidden-12 %.5f +- %.5f  [%.0fs]"
        % (nm, st["below"], st["zeros"], st["d_gs"], st["d_un"], st["d_rf"], st["fmass"], st["fse"], time.time() - t0))
say("")
say("     convergence check: L1 between the finished-set odds at p and the simulated p -> 0 limit")
for nm in STATES:
    row = []
    for p in PS:
        pp = GRID[(nm, p, 0.5)][0] / NT
        row.append("p=%.2f: %.4f" % (p, C.l1(pp, DEPH[nm][0] / NT)))
    say("       %-8s (tau=0.5)  %s" % (nm, "   ".join(row)))
say("")
say("(iii) survival of the discriminator's 12 zeros, by regime (mass registered on the 12 forbidden pairs):")
say("      %-8s | %-12s | %s | %-12s" % ("state", "p=1 (exact)", " ".join("p=%-6.2f" % p for p in PS), "p->0 limit"))
for nm in STATES:
    b = C.born_patterns(C.PSI0[nm])
    say("      %-8s | %-12.5f | %s | %-12.5f"
        % (nm, b[C.ZERO12].sum(),
           " ".join("%-8.5f" % (GRID[(nm, p, 0.5)][0][C.ZERO12].sum() / NT) for p in PS),
           DEPH[nm][0][C.ZERO12].sum() / NT))
say("      (tau = 0.5 column; the other taus are in Section 2.)")

# ================================================================= 4  alternative dynamics
hdr("SECTION 4  model choice B -- keep the full H, re-condition on the registered values every step")
NB = 5000
say("%d trajectories per point (this model cannot use the gap-accumulation shortcut, so it is run smaller)." % NB)
say("  %-8s %-5s %-5s | %-22s | %-22s | %s" % ("state", "p", "tau", "L1 to GS Born (A / B)", "forbidden-12 (A / B)", "L1(A,B)"))
for nm in STATES:
    for p in (0.5, 0.2, 0.05):
        for tau in TAUS:
            Uf = C.VC896 @ (np.exp(-1j * tau * C.EV896)[:, None] * C.VC896.conj().T)
            sd = hash((nm, p, tau, "AB")) % (2 ** 31)
            ca, _ = R.run(nm, p, tau, NB, seed=sd, mode="drop")
            cb, _ = R.run(nm, p, tau, NB, seed=sd, mode="proj", Uf=Uf)
            pa, pb = ca / NB, cb / NB
            say("  %-8s %-5.2f %-5.1f | %.4f / %.4f          | %.5f / %.5f      | %.4f"
                % (nm, p, tau, C.l1(pa, C.GS_BORN), C.l1(pb, C.GS_BORN),
                   pa[C.ZERO12].sum(), pb[C.ZERO12].sum(), C.l1(pa, pb)))
say("  (MC noise floor on L1(A,B) at n=%d is about %.4f for a 28-cell distribution.)"
    % (NB, 2 * 28 * math.sqrt(2 / (math.pi * NB)) * math.sqrt((1 / 28) * (27 / 28))))

# ================================================================= 5  order dependence
hdr("SECTION 5  order of formation: exact fixed schedules, same finished recorded set")
say("All schedules register all 12 sites; they differ only in WHEN.  Odds computed exactly by enumerating")
say("the whole record tree (no Monte Carlo).")
SCHED = {
    "A all 12 at tick 1": [(0, list(range(12)))],
    "B one per tick, site order 0..11": [(0, [0])] + [(1, [q]) for q in range(1, 12)],
    "C one per tick, site order 11..0": [(0, [11])] + [(1, [q]) for q in range(10, -1, -1)],
    "D one per tick, star of corner 0 first": None,
    "E one every 5 ticks, order 0..11": [(0, [0])] + [(5, [q]) for q in range(1, 12)],
    "F two per tick, 6 ticks": [(0, [0, 1])] + [(1, [2 * i, 2 * i + 1]) for i in range(1, 6)],
}
star0 = list(C.En.STAR[0])
rest = [q for q in range(12) if q not in star0]
SCHED["D one per tick, star of corner 0 first"] = [(0, [star0[0]])] + [(1, [q]) for q in star0[1:] + rest]
for tau in (0.5, 2.0):
    say("")
    say("  tau = %.1f" % tau)
    for nm in STATES:
        res = {}
        for k, s in SCHED.items():
            res[k] = R.exact_schedule(C.PSI0[nm], s, tau)
        keys = list(SCHED)
        say("    %s" % LAB[nm])
        for k in keys:
            say("      %-38s  L1 to GS Born %.4f | L1 to uniform %.4f | forbidden-12 %.6f | #<1e-3 %d"
                % (k, C.l1(res[k], C.GS_BORN), C.l1(res[k], C.UNIF28), res[k][C.ZERO12].sum(),
                   int((res[k] < 1e-3).sum())))
        say("      pairwise L1 between schedules (exact, no sampling error):")
        for a, b in itertools.combinations(keys, 2):
            say("        %-38s vs %-38s  L1 = %.4f" % (a[:38], b[:38], C.l1(res[a], res[b])))

# ================================================================= 6  clock
hdr("SECTION 6  record count as a clock")
say("Each site's formation tick is Geometric(p): mean 1/p per site.  Completion tick T = max of 12 i.i.d.")
say("Geometric(p), so P(T <= t) = (1-(1-p)^t)^12 and E[T] = sum_{j=1..12} (-1)^{j+1} C(12,j) / (1-(1-p)^j).")
say("  %-6s | %-10s | %-10s | %-10s | %-22s" % ("p", "1/p", "E[T] exact", "E[T] MC", "MC quantiles 10/50/90"))
for p in (1.0,) + PS:
    ex = sum((-1) ** (j + 1) * math.comb(12, j) / (1 - (1 - p) ** j) for j in range(1, 13))
    tk = np.random.default_rng(9).geometric(p, size=(40000, 12)).max(1)
    say("  %-6.2f | %-10.2f | %-10.3f | %-10.3f | %d / %d / %d"
        % (p, 1 / p, ex, tk.mean(), np.quantile(tk, .1), np.quantile(tk, .5), np.quantile(tk, .9)))
say("")
say("Is the finished set a function of the product p*tau only?  Points with equal p*tau, same initial state:")
say("  %-8s | %-16s | %-16s | %-8s | %s" % ("state", "point 1", "point 2", "p*tau", "L1 between them"))
EXTRA = {}
for nm in STATES:
    for (p1, t1, p2, t2) in ((0.2, 0.5, 0.05, 2.0), (0.5, 0.1, 0.05, 1.0), (0.2, 0.1, 0.01, 2.0)):
        for (pp, tt) in ((p1, t1), (p2, t2)):
            if (nm, pp, tt) not in GRID and (nm, pp, tt) not in EXTRA:
                c, _ = R.run(nm, pp, tt, NT, seed=hash((nm, pp, tt, "x")) % (2 ** 31), mode="drop")
                EXTRA[(nm, pp, tt)] = c
        g1 = GRID[(nm, p1, t1)][0] if (nm, p1, t1) in GRID else EXTRA[(nm, p1, t1)]
        g2 = GRID[(nm, p2, t2)][0] if (nm, p2, t2) in GRID else EXTRA[(nm, p2, t2)]
        say("  %-8s | p=%.2f tau=%.1f | p=%.2f tau=%.1f | %-8.3f | %.4f"
            % (nm, p1, t1, p2, t2, p1 * t1, C.l1(g1 / NT, g2 / NT)))
say("  (MC noise floor on L1 at n=%d is about %.4f.)"
    % (NT, 2 * 28 * math.sqrt(2 / (math.pi * NT)) * math.sqrt((1 / 28) * (27 / 28))))
say("")
say("Same p, different tau (does tau matter at all beyond the product?):")
for nm in STATES:
    for p in (0.2, 0.05):
        say("  %-8s p=%.2f : L1(tau=0.1, tau=0.5) = %.4f ; L1(tau=0.5, tau=2.0) = %.4f ; L1(tau=0.1, tau=2.0) = %.4f"
            % (nm, p, C.l1(GRID[(nm, p, 0.1)][0] / NT, GRID[(nm, p, 0.5)][0] / NT),
               C.l1(GRID[(nm, p, 0.5)][0] / NT, GRID[(nm, p, 2.0)][0] / NT),
               C.l1(GRID[(nm, p, 0.1)][0] / NT, GRID[(nm, p, 2.0)][0] / NT)))

say("")
say("[total runtime] %.1f s" % (time.time() - T0))
open("l3c_out.txt", "w").write("\n".join(OUT) + "\n")
