# Independent proof check: capped finite-time localization for the complete head law

Verdict: the proposed bound is valid with constant3. Source-block normalization needs explicit bookkeeping, but it gives exactly the stated final factor D. The proof avoids assuming Fourier translation for the approximate capped flow and does not reset the retained battery. This review applies to the COMPLETE fixed-head native Record law; it does not extend its positive rate-defect argument to occupation-feedback jumps.

## Common spaces and assumptions

Use one common direct sum of legal source/history/head/Record code sectors, with the same positive battery cap P and the same original free Hamiltonian H_total in both generators. Include the exact generator's absorbing refusal copies in this space if needed, with zero additional approximate jumps into those copies. This makes comparison of the two CPTP semigroups literal. Changing the approximate free Hamiltonian would add a separate commutator error not bounded below.

For each eligible source/edge pair i=(s,e), let V_i be the exact full-line two-sign column and W_i the coherently truncated full-line column. Both are isometries on that source code. Whole-hopping-term truncation ensures input/output code preservation; the same physical output Hamiltonian acts on both signs. Put C_i=P_out W_i P_in. The source identity below is the capped source-sector identity, not the identity over all histories. Embed each compressed branch as an ordinary GKSL jump sqrt(gamma) C_iz, with its actual anticommutator. This yields a bounded trace-preserving CP semigroup even though C_i^*C_i may be smaller than identity. No invented refusal is needed for the approximate generator.

The exact source has its original completion, but on Q_safe every refusal amplitude is zero and P_out V_i Q_safe=V_i Q_safe. Q_safe is invariant under the exact capped generator, so its flow agrees with the corresponding full-line flow from the prepared state. All statements below may be tensored with an arbitrary reference identity.

## Single-source, single-edge estimate

Let rho_s>=0 be the exact source block, p_s=Tr rho_s, and define

alpha_i²=Tr[(V_i-W_i)^*(V_i-W_i) rho_s].

Because rho_s is cap-supported and V_i rho_s^(1/2) lands inside the cap,

||(V_i-C_i)rho_s^(1/2)||_2
 =||P_out(V_i-W_i)rho_s^(1/2)||_2 <= alpha_i.

Both columns are contractions. The Hilbert-Schmidt product inequality and telescoping give

||V_i rho_s V_i^* - C_i rho_s C_i^*||_1
 <= (||V_i rho_s^(1/2)||_2+||C_i rho_s^(1/2)||_2) alpha_i
 <= 2 sqrt(p_s) alpha_i.

For separate GKSL sign jumps, the physical recycling sum has no cross-sign coherences. Apply the same sign-dephasing map to both displayed coherent columns; trace-norm contraction preserves the bound. One must not silently identify a coherent-sign isometry channel with that recycling sum, although the inequality is unchanged.

The rate defect is

E_i=I_s-C_i^*C_i
 =P_in W_i^*(I-P_out)W_i P_in.

Thus 0<=E_i<=I_s, and

Tr(E_i rho_s)=||(I-P_out)W_i rho_s^(1/2)||_2²
 =||(I-P_out)(W_i-V_i)rho_s^(1/2)||_2² <=alpha_i².

Using E_i²<=E_i,

||{E_i,rho_s}/2||_1
 <=||E_i rho_s||_1
 <=sqrt(p_s Tr(E_i² rho_s))
 <=sqrt(p_s) alpha_i.

The exact safe-domain anticommutator uses identity, whereas the approximate one uses C_i^*C_i. Consequently the one-edge generator difference is bounded by

3 gamma sqrt(p_s) alpha_i.

For normalized rho_s this reduces to3 gamma alpha_i as proposed. For a subnormalized block, omitting sqrt(p_s) would lose the clean degree bound when summing many histories. Zero-mass blocks contribute zero without defining a conditional state.

## Summing histories and controlling alpha from the exact flow

The initial head/history is definite. The original free Hamiltonian is block diagonal, and each specified exact jump maps into a definite orthogonal history/sign sector, so the exact state remains a classical mixture rho=direct_sum_s rho_s, possibly with arbitrary matter/battery/reference coherences inside each block. Let d_s<=D be its live incident degree.

Suppose the same uniform fiber bound delta(tau) applies to every eligible i. Then

sum_i alpha_i² <= D integral delta(tau)² p_t(tau) d tau,
sum_i p_s = sum_s d_s p_s <=D.

Cauchy-Schwarz therefore gives

sum_i sqrt(p_s) alpha_i
 <=sqrt[(sum_i p_s)(sum_i alpha_i²)]
 <=D sqrt(integral delta² p_t).

There is no factor equal to the number of histories or sign branches. Any radius-dependent constants and boundary norms in delta must be bounded uniformly across those source/edge choices; the maximum over the finite graph is sufficient. This is where the common whole-term LR bound and maximum boundary prefactor enter.

For the exact full-line evolution, let p_t(tau) be the trace over all sector/matter/reference factors of its Fourier-diagonal density. The Hamiltonian A_s-i partial_tau gives the transport term -partial_tau p. At each tau the trace of the complete jumping/recycling terms cancels their anticommutator trace after summing sources and outputs. Hence

p_t(tau)=p_0(tau-t).

This identity concerns only the exact flow. Its identification with the exact capped flow is justified by invariant Q_safe, not by pretending that a cap is a local Fourier multiplier. Initially p_0=|beta_hat|² for every matter-reference input because the fixed battery is prepared independently. Full-line Fourier kernels are a convenient representation of the cap-supported physical states; no periodic Fourier battery or finite Fourier box is introduced.

Let the reference Fourier variable be tau_0=tau-t. On |tau_0|<=T_cut and0<=t<=T_lab, |tau|<=T_cut+T_lab. Therefore, for the stated LR estimate,

epsilon=C_R exp[-mu(R-a-v(T_cut+T_lab))],
int delta² p_t <=epsilon²+4 eta,
eta=int_{|tau_0|>T_cut}p_0(tau_0)d tau_0.

The inequality uses delta<=2 in the tail; it does not truncate beta_hat or modify the initial energy-compact sine packet. If T_cut>=sqrt(2)pi/w, eta<=min(1,32pi/[3(w T_cut)^3]). Keep C_R, v and their geometry hypotheses explicit. For a bound useful below2, the chosen radius/cut/time must actually make these quantities small; validity alone does not imply numerical sharpness.

## Duhamel and fixed-input diamond distance

Write S_t for the exact capped semigroup and S_tilde_t for the compressed approximate one. Both are CPTP on the common capped direct sum. For the fixed initial product-preparation map J_beta,

(S_tilde_t-S_t)J_beta(rho)
 =integral_0^t S_tilde_(t-u)(G_tilde-G)S_u J_beta(rho)du.

The integrand generator difference is Hermitian; complete positivity and trace preservation make S_tilde trace-norm contractive on it, including an arbitrary reference. The generator difference is evaluated ONLY on the exact invariant-safe flow. Applying the previous bounds yields, uniformly for0<=t<=T_lab,

||(S_tilde_t-S_t)J_beta||_diamond
 <=min{2,3 gamma D T_lab sqrt(epsilon²+4 eta)}.

This is the diamond norm of maps whose input is matter in the specified initial legal sector, with battery and head/history fixed by J_beta. It is not the unrestricted diamond norm on arbitrary initial matter-battery states. It retains the battery in the output. It compares full laboratory-time channels, including all histories/traps, rather than a normalized selected-event channel. The usual channel-difference diamond characterization by matter-reference density inputs supplies the stated interpretation; no reference-dimension prefactor is introduced.

The proof does not need the approximate flow to preserve Q_safe, have Fourier density p_0(tau-t), preserve identity edge rate, or restart with a product battery. Approximate cap leakage is encoded precisely in E_i and its actual anticommutator. Earlier one-shot cap safety may be true but is not required at later times in this argument.

## Observables and scope

Under Delta>=t, all legal original sector energies lie in[0,M], M=L(Delta+t). On the common cap[0,C], 0<=H_total<=C+M, including same-H refusal copies. Both compared final states have trace one. Centering H_total therefore gives

|Tr H_total(rho_tilde-rho_exact)|
 <=(C+M)/2 * ||rho_tilde-rho_exact||_1.

Since the exact evolution conserves the initial global energy mean, this bounds the approximate law's energy-account deviation for that preparation. It does not prove exact conservation by the truncated jumps. A history/event indicator is an effect in[0,I], so its probability discrepancy is at most half the trace-norm error. Conditional states normalized by a rare event probability need an additional normalization/error analysis.

The complete-column premise is load bearing: E_i>=0 with E_i=I-C_i^*C_i and leakage expectation bounded by alpha_i² uses W_i^*W_i=V_i^*V_i=I. For occupation-feedback columns the full/truncated effects are different conjugates of M_e, and the displayed positive-defect argument cannot be imported. A distinct rate/no-jump estimate would be required. This review asserts no such extension.

Conclusion: the stated capped finite-time approximation theorem is mathematically supported under its explicit native local-extension/LR assumptions, with the subnormalized-source factor and sign-dephasing clarification above. It neither changes the frozen packet nor produces a local finite-qubit battery, a closed physical reservoir, exact global-energy conservation by the approximation, or renewal.
