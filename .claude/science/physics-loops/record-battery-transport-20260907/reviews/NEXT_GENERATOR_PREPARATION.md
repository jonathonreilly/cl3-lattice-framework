# Independent preparation review: fixed head/fuel/shared-battery GKSL route

Reviewed 2026-09-07. Read-only review of AUTONOMOUS_SHARED_APPARATUS_ROUTE.md, NEXT_FORMATION_ROUTE.md, ROOT_DERIVATION.md, and the native Record instrument/energy apparatus and local-cycle parent notes. No source or campaign-tree files were modified. This is algebraic preparation, not a transport computation or a reproduced trail census.

## Verdict

No fatal algebraic obstruction found in the shared-apparatus construction when formulated on the direct sum of legal history/head/live-mask/code sectors. Several definitions should be made explicit before claiming a complete fixed generator. In particular, the sentence saying every branch has amplitude 1/sqrt(2) must be restricted to nonbridges; bridge Kraus maps are parity projections with state-dependent probabilities. The stated four-event calculation is within the nonbridge domain.

## Complete jump definition

Let s label a legal history, head v, recorded/deleted mask R and compatible Record code, with L initial edges. Put H_s = H_R + Delta (L-|R|) I, counting the live fuel units. For an incident live edge e=(v,w), let K_{s,e,z}: H_s -> H_{s'} be the native branch map, including head move, fuel lowering and history append. Require sum_z K_z^* K_z = I_s, preserving total N and old Records. Nonbridges have K_z=J_z/sqrt(2), J_z^*J_z=I. Bridges instead have K_z=(I+z s_C parity_C)/2 in the appropriate input/output dictionaries; their sum is complete without inserting another 1/sqrt(2).

Correction from the 2026-09-07 backlog review: the initial preparation memo wrote `Delta |R|` in this equation while using a positive `Delta` battery shift below. That combination would increase total energy by `2 Delta` per event. Counting live fuel as `L-|R|` restores the intended fuel lowering and agrees with AUTONOMOUS_SHARED_APPARATUS_ROUTE.md. The three current source theorems and their runners do not use this future-route fuel term.

On a full-line battery define A_z=sum_{a,b} Pi_out(b) K_z Pi_in(a) tensor T_{a-b}, using FULL system energies including fuel. Equivalently, if a,b name matter energies, the shift is a-b+Delta. Do not include Delta twice. With T_u|E>=|E+u>, (H_out+E_B)A_z=A_z(H_in+E_B). Fourier fibers are exp(-i tau H_out)K_z exp(i tau H_in), hence sum_z A_z^*A_z=I_s even for bridge instruments. This is the exact justification of rate gamma per legal edge.

Embed these maps in the common sector direct sum and set L_{s,e,z}=sqrt(gamma)A_z. One may combine compatible source sectors into L_{v,w,z}, provided the appended history makes distinct outgoing sectors orthogonal. A single initial definite history/head sector remains a classical mixture over these sectors under the jump unraveling. All legality projectors and head/history Hamiltonians must be specified; choosing degenerate head/history energies is an explicit resource choice.

## Cap and refusal

Let P cap the battery to [0,97]. Define the combined column S=(P_out A_+ P_in, P_out A_- P_in), so S^*S=sum_z S_z^*S_z <= I. Add one refusal F=(I-S^*S)^(1/2), multiplied by sqrt(gamma) in the generator. Because caps commute with energy, S_z intertwine total energy, S^*S commutes with input energy, and F does also. Embed refusal in a copy carrying the same Hamiltonian. A concrete completion is an absorbing refusal sector with no outgoing jumps; this prevents unspecified repeated history growth off the safe domain. Alternatively specify a same-sector refusal channel. Neither choice affects the safe fixture. Completing each sign independently would yield twice the intended rate.

For |R|<=12 and Delta=t=1, ||H_s||<=24, so initial beta support [48,49] implies total support [24,73] and battery support [0,97] at every prefix. This remains valid through bridges and trapping sectors. Fuel positivity actually permits a sharper bound, but optimization is unnecessary. The cap is continuous and therefore infinite dimensional. On the bounded capped Hilbert space all stated spectral functions should mean bounded Borel functions (or functions integrable in the state), avoiding gratuitous domain claims.

Each completed jump commutes with the common H_total. Therefore D_L^*(f(H_total))=L^*f(H_total)L-1/2{L^*L,f(H_total)}=0. Adding -i[H_total,rho] preserves this statement. This proves modeled total-energy distribution conservation, not a closed-unitary implementation or a local reservoir construction.

## Waiting law and averaging

On safe sector s, sum_{e,z} L^*L=gamma d_R(v) I_s. Thus the no-jump propagator is exp(-gamma d_R(v)t/2) exp(-iH_total t), edge probability is 1/d_R(v), and total wait is exponential with rate gamma d_R(v). On four-event nonbridge histories signs are fair. Later signs need not be fair, but their sum leaves the edge waiting law unchanged. Traps d=0 have no next event and must retain their probability mass.

Intertwining pushes every free dwell to the final side of a conditioned branch: A_k exp(-iH_{k-1,total}t_k)...A_1 exp(-iH_{0,total}t_1)=exp(-iH_{k,total}T)A_k...A_1. Tracing battery gives exp(-iH_R T)sigma_path exp(iH_R T), since final fuel is scalar. At the kth event epoch, for a FIXED path and rates r_l, averaging yields matrix factor product_l r_l/(r_l+i(E_b-E_b')). This includes the wait BEFORE each event and excludes any post-k wait. It is not a fixed laboratory-time ensemble: at fixed time path length and survival factors differ. It is not a guarantee for every realized waiting sequence. The path must be conditioned before using its rates; do not average the rates first.

The shared lift telescopes. Within the common nonbridge CAR gauge its matter reduction depends only on the final mask and initial state; fuel contributes a common k Delta shift. The overlap kernel is unchanged, and the battery mean must be contracted with [E0+w/2+(u+v)/2]K(u-v), u=a-b+k Delta. The resulting mean has the additive k Delta contribution, but energy conservation alone is not an independent battery calculation.

## Recommended finite independently checkable tests

1. Enumerate all trails from the declared initial head using exact rational branching probabilities; verify every prefix up to four is connected, path counts and rates, and sum of weights. Reproduce rather than assume the claimed 24 paths and (3,2,2,2) degree sequence. Separately census five-step disconnects and terminal counts without postselection.
2. On at least one reachable bridge and one nonbridge, use the native code/CAR dictionaries to test sum K_z^*K_z=I, old Record persistence and N intertwining. Include a bridge input with deterministic parity outcome, which detects illicit fair-sign continuation.
3. On a small commensurate finite battery witness, test every matrix entry of [H_total,L], combined completeness including refusal, safe zero-refusal, and a deliberately cap-unsafe input with nonzero refusal. A finite witness supports the implementation check; the continuous cap theorem remains analytical.
4. Verify no-jump total rate gamma d and the rational Laplace factors independently, including zero energy gap and conjugation under reversed gap. Compare a small direct deterministic integration to the product formula without using Monte Carlo as the proof.
5. Compute all four-event path/sign conditional density matrices, direct battery moments, sharp N, energy and current diagnostics. Preserve unfavorable paths. Check Hermiticity, positivity tolerance, trace, total weights and total-energy conservation. Use the actual joint moment as the primary battery value.
6. Mutation controls: omit Delta, double it, reset battery each event, force fair bridge signs, complete signs separately, replace pathwise rate product with a mean rate, and reverse the Laplace gap. Each should fail a targeted invariant or comparison.

Remaining imports are the carrier and CAR encoding, initial matter pulse/state, definite head and live fuel preparation, energy gap, battery coherence and continuous spectrum, degenerate history storage, the spectral global implementation, gamma and external time parameter, supplied jump unraveling/Markov law and irreversible entropy sink. Removing prescribed edge order and dwell durations removes those schedules only. No locality, one-site admissibility, closed autonomous finite unitary realization, replenishment, renewal or indefinite transport is established.
