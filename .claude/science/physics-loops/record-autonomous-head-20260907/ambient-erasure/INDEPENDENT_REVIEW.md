# Independent ambient/history-erasure review

Reviewed the orbital agent's ambient-generator-review.md, against the native algebra and an independently assembled finite matrix witness. No fatal algebraic obstruction found. One timing statement needs a clear distinction between conditional physical states and complete timed trajectory Kraus amplitudes.

## Native seed, cap and code

J_vw=T_e n_v(1-n_w) is correct on the ambient native edge algebra, with T_e the unit-normalized hopping generator, not a_e T_e. T_e maps the active occupancy projector into the reverse occupancy projector and squares to the one-particle endpoint projector. Thus J*J=n_v(1-n_w), [J,N]=0, and Z_e J=-J Z_e. These are ambient identities; the code restriction identifies their CAR meaning. The head factor has M_vw*M_vw=n_v^head(1-n_w^head) on the full head tensor space and reduces to n_v^head on the invariant one-head sector, as the memo explicitly specifies.

For a source code P_alpha, both ambient source H and target H-h_e-Delta commute with it termwise. This does not mean Q_ez preserves the OLD source code; it generally does not. In the capped sign-summed loss, the two outgoing energy projectors are adjacent in each product and collapse to the same b. Because target H commutes Z_e, sum_z Q_z Pi_out(b) Q_z=Pi_out(b). The battery factor depends on a,a',b but not sign, so this cancellation is valid with the cap retained. The remaining native factors commute P_alpha. Forward images enter the correct NEW code and the summed loss preserves the source. Both halves are necessary for GKSL code invariance.

The actual witness detects individual capped-loss source-code leakage0.35355339059327395 while the sign-summed leakage is4.21e-16. Thus this is a nontrivial source-code cancellation, not merely a forward-isometry assertion. For Record-only refusal the eligibility effect E_vw replaces the full identity. Since it commutes H and the full-line column has effect E_vw, the one combined-sign complement is positive; functional calculus preserves code and total energy. Absorbing-flag completion matches the old sector complement. Feedback uses the actual compressed loss with no such identity completion.

## CPTP erasure and merged histories

The channel C(rho)=sum_s W_s rho_ss W_s* is CPTP even when some W_s have overlapping or identical ranges: each Kraus has an orthogonal input history block, so their squared norms sum to identity. Orthogonality of OUTPUT embeddings is not required. The branch restrictions, the summed-loss restriction and H W_s=W_s H_s imply the generator identity. For the old generator with separate source-history jumps, off-diagonal history blocks do not contribute to any recycling diagonal and are killed by C, so the intertwining also holds as a channel identity on its whole declared history space, not only on the initial classical history mixture.

After histories merge, the ambient generator acts on the SUM of their physical density matrices. It does not add their amplitudes. Its jump instruments preserve the same environmentally recorded edge/sign/time history when old source labels are summed, but C cannot make an arbitrary order-register observable into a system observable. No counterexample to these claims was found. Code basis phase choices are harmless only when the W_s and sector matrices are transformed consistently; the fixed physical ambient construction supplies that consistency.

## Section5 timing clarification

On the full line, or on the invariant safe domain with no cap truncation at any prefix, products of lifted bare seeds telescope because the same ambient Hamiltonian defines every lift. For a Record-only path with k events and dwell vector t,

K_p(t)=gamma^(k/2) exp[-gamma sum_l d_l t_l/2]
       exp[-i H_total T] V_(bare product),    T=sum_l t_l.

The entire accumulated free phase remains. It does not disappear under the total-energy coordinate change; in Q fibers it is exp(-iQT). For two orders with the same final head/fuel/Record data, the physical Record-only bare Q products commute and the head/fuel products agree on the eligible initial sector. Their retained lift and final free factor therefore agree when T agrees. Their NORMALIZED conditional physical states agree as claimed.

However the full timed no-jump Kraus operators also contain the scalar exp[-gamma sum d_l t_l/2]. Equal T alone does not fix it. On the cube four-step prefixes d=(3,2,2,2), so sum d_l t_l=2T+t_1. Two dwell vectors with equal T but different first dwell have different unnormalized path amplitudes/probability densities. On the square witness d=(2,1,1,1), the corresponding expression is T+t_1. Thus section5 is correct if read literally as equality of the retained lift plus final free evolution, or of normalized states; do not strengthen it to equality of complete timed path operators unless the degree-weighted dwell sums also agree.

Cap compression inserted between arbitrary unsafe paths need not telescope. The section5 counterexample can explicitly choose the declared invariant safe preparation, which is sufficient to establish noninvertibility of erasure. No general unsafe path-order equivalence is needed. Feedback products and no-jump operators are noncommuting/state dependent and do not inherit this Record-only state-equality argument.

## Actual finite witness

check.py compares independent grouped-projector ambient lift assembly (literal battery index writes) with the preexisting independent native code-sector lift routines. It uses16-dimensional ambient edge matrices and an actual34-level ladder. Head/fuel blocks are identified by their actual routing labels rather than allocating illegal full tensor states. All columns of independent total-H matrix intertwiners are checked in blocks. Eight branch restrictions include Record-only and directed-feedback initial/nonbridge and old-Record/bridge sectors. Recycling amplitudes, summed loss, anticommutator, free term and refusal-effect restrictions are checked on the full legal capped source columns.

Two actual square trails [0,1,2,3] and [3,2,1,0] merge at head0 with all four fuels spent and common signs(+,-,+,+). On a native N2 input the witness superposes SAFE total energies19 and20, so a real relative retained-battery phase can be detected. Each timed path is applied stage by stage with its actual system-plus-battery free matrix, scalar no-jump factor and lifted jump. Results:

- Equal totalT=1 for dwell vectors(.1,.2,.3,.4) and(.4,.3,.2,.1) gives identical normalized physical outputs.
- Their timed probability ratio is exp(-.3)=0.7408182206817174, exposing the extra scalar normalization condition.
- Changing accumulated time by1 gives retained-state trace distance2sin(.5)=0.9588510772084062, demonstrating that the full free phase survives.
- Incorrect coherent addition of merging histories changes the density by Frobenius norm0.28650479686018987.
-417 new checks plus72 on-demand carrier checks passed; maximum residual3.5531e-15, final runtime0.347s, peakRSS146.9MiB.

The current scratch script SHA256 is19ed1d441a27e916b92e088e2d568307f7344f0a06e94e427cd8e6febeaa1011. Final result.json is the execution receipt. The carrier's full main/census is not rerun; its on-demand assertion count is reported separately. This witness is a commensurate square/dimer calculation, not a full-cube or local physical bath realization.

## Remaining implementation scope

The displayed ambient controlled whole-hop Hamiltonian supplies a finite-range interaction without a global chronological or code projector in its seed. An LR estimate is therefore applicable with the explicit enlarged geometry, bounds and Fourier-tail domain stated by the memo. This does not by itself localize the exact energy lift, cap or refusal, implement a finite local battery, or account for reservoir record entropy/renewal. Those caveats are correctly retained.
