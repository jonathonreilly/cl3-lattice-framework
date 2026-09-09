# Four-representative L6 vertex: prospective certified algorithm

No CG, full-vector transport, spectrum, or residual has been run for this design. It uses the exact adapted21-mode frame and vacuum-fixed48-element transports (candidate freeze194b07b7), the declared proper-prefix gap delta=|t|/3, and the fullvector arithmetic-envelope proof9e489. The latter is a conditional arithmetic theorem; current floating candidate code is not already its certified implementation. The gap is applied only to actual two-edge star masks, which belong to the reviewed complete prefix domain. The bath vacuum offset and unequal positive frequencies must be retained.

## Four positive-denominator solves

Use A_C=H_C-E0>0. Both negative Feshbach inverse signs cancel, so define x_A=A_A^-1 Omega and y_C=A_C^-1 gamma0 sum_(A disjoint C)x_A, then chi=(1/8)sum_C y_C. No extra1/48 or flat-frequency scaling is allowed at L6. Physical electric1/8 is retained. At |t|=1, delta=1/3; x scales as|t|^-1 and y,chi as|t|^-2.

Choose first representatives (+x,+y) and(+x,-x), denoted P and O. Solve the two even systems. Reconstruct all15 first vectors with the exact selected magnetic transports from the fixed ledger. Form the two complete odd right-hand sides for last pairs P,O, then solve those two odd systems. Reconstruct the15 second vectors and sum with1/8. Each last perpendicular pair has five perpendicular and one opposite predecessor; each last opposite pair has four perpendicular and two opposite predecessors. These are all six disjoint pairs, not a weighted scalar substitution for their vectors.

The stabilizer of A permutes H_A and fixes Omega, so uniqueness of the positive inverse makes x_A stabilizer invariant. Similarly the stabilizer of C permutes its full six-predecessor set and fixes gamma0, making its exact odd source and inverse invariant. Thus chosen transports are unambiguous for exact solutions. Approximate representatives need not be invariant: fix one transport per target before data, and certify each transport's discrepancy through its norm-error envelope. Do not silently average away a stabilizer discrepancy. The full vertex is group invariant, but this does not establish one-particle linearity.

## Complete residual propagation

All norms below are certified upper bounds for stored dyadic candidates. A first representative residual certificate rho_1a bounds ||Omega-A_a xhat_a|| and includes the full arithmetic error of A's actual two independent two-Gamma chains, diagonal and vector additions. Then e_1a=rho_1a/delta bounds its solution error. For any transported first vector add its certified transport error tau_1A to the corresponding e_1a. The exact symmetry has norm1, so it does not amplify the inherited error.

For representative last pair C, let eta_C bound all arithmetic in summing its six stored first vectors and applying gamma0. Then the approximate source bhat_C differs from the exact source by

B_C <= sum_(A disjoint C)(e_1class(A)+tau_1A)+eta_C.

Certify rho_2C >= ||bhat_C-A_C yhat_C|| against that actual stored source, including full action and residual-subtraction error. Its solution error is e_2C=(rho_2C+B_C)/delta. The source uncertainty is added before division, not treated as a solver residual against an exact source. For each transported second candidate add tau_2C. If eta_sum bounds the final15-vector sum and exact1/8 scaling, the full vertex error is

E_chi <= (12 e_2P+3 e_2O+sum_C tau_2C)/8 + eta_sum.

With no transport/source/sum roundoff, the first-residual contribution is delta^-2(9rho_1P+9rho_1O/4); the second-residual contribution is delta^-1(3rho_2P/2+3rho_2O/8). At |t|=1 these weights are81,81/4,9/2,9/8, respectively. This independently checks both the two resolvents and electric1/8. No factor30 or missing predecessor multiplicity is hidden.

A coarse physical upper norm is ||chi|| <=(15*6/8)delta^-2=405/(4|t|²). It is only an envelope, not a predicted value. It can bound intermediate magnitudes when a sharper measured certified norm is unavailable.

## Fixed iteration and stopping proposal

Propose zero-start, unpreconditioned CG with a fixed maximum256 iterations for each of the four systems, no restarts or representative substitution. Exact-arithmetic positivity follows from the supplied gap. An upper operator bound is Lambda=|t|[6sqrt12+6sqrt24+6sqrt36+3sqrt48+8], since each of two flipped edges changes the Hamiltonian by a norm2|t| term and the triangle inequality even permits the conservative8|t| allowance. The sharper total perturbation allowance is4|t|;8 is intentionally conservative. This upper bound licenses the usual exact-CG condition-number envelope, but does not guarantee finite-precision stopping. The actual action implementation, transport rounding and exact-norm scanner must first receive independent source review and cost profiling.

For a concrete prospective precision rule, require certified first residuals <=10^-10, second residuals <=10^-9/|t|, and final E_chi<=10^-6/|t|² including every transport/source/sum term. Check the full certified residual at fixed iterations16,32,...,256 and stop a system only at its first passing checkpoint. These thresholds and cap are to be frozen before physical data; failure is retained, not followed by more iterations. The final chi certificate, not an ordinary recursive CG residual or small update norm, determines success. This proposal changes no already frozen pilot.

The computation is authorized only if measured action, transport, dot-product and certified norm costs support the entire fixed worst-case schedule. The maximum iteration cost includes four systems times256 pair actions, CG dot/axpy work and memory. The16 checkpoints per system add64 fresh action certificates; each action certificate requires norms of all intermediate chain/diagonal/addition vectors as specified by9e489. Either stream these exact accumulators during the action or charge their full extra passes explicitly. Price all first/second orbit transports, twelve-vector source assembly, fifteen-vector final assembly, file serialization and independent replay. Four representative vectors alone use32MiB real or64MiB complex, but solver workspaces and all intermediates must be included under a measured peak cap. Do not retain thirty physical vectors by default; stream transport contributions into two sources/final sum, preserving deterministic accumulation order.

## Particle-weight inference

For each desired odd particle number k, compute the exact dyadic squared norm of the projected candidate (count the implicit top bit). Obtain outward roots to enclose a_k=||P_k chihat||. Then

[max(0,a_k_lower-E_chi)^2,(a_k_upper+E_chi)^2]

contains the true w_k. A strictly positive lower endpoint certifies a nonzero component. An upper endpoint below a predeclared tolerance certifies smallness only; numerical finite tolerance cannot establish exact zero. For a concrete optional diagnostic tolerance choose w_k<=10^-12/|t|^4. Claiming that all multiparticle weight is small requires the full k>=3 projector, not only k3 andk5; modes7 through21 remain possible on L6. The same single streaming norm pass can collect all odd particle counts and total norm with integer accumulators, so price it once, including bit-count classification and output hashes. Tiny toy tests or selected coordinates cannot replace that full pass.

No Gaussian rank is guessed. If the fixed fullvector cost or arithmetic-certification prerequisites fail, this design stops without asserting a vertex result or silently replacing it with a low-rank ansatz.
