# Local entropy export gives a conditional probability supplier, but fails native-code preservation

Status: bounded exploratory result, not a physical Record closure. Main pin2b42ebe4b6b4ee76b0fa1b8e668ad7775e946307. The current June29 axioms, landed6358 corrected prepared-family source, live7047 at2babab5976e69488a318b1c822fecdc25a68895e, native edge-instrument placement/definitions, and the controlled-copy source were consulted. This result does not identify a density operator with the framework's complete Record state. All density inputs below are explicit operational preparation data in a conditional model.

## 1. Why this candidate and what it adds

PR7047 already constructs an absorbing finite cq channel but leaves its physical Record calibration and local admissibility marginal equality supplied. Landed6358 already proves a current-Record condition cannot distinguish arbitrary prepared inputs. Merely specifying a Born-shaped kernel, a controlled copy, or the previous square's classical mediator would repeat those results. The candidate here physically exports target memory to a nearest-neighbor sink, derives the resulting local effect, and tests whether that preparation operation remains inside the actual BKSF carrier. The last test fails decisively.

Active reset is standard causal-break machinery, not claimed as new quantum Markov theory. Pollock et al., Operational Markov condition for quantum processes, arXiv1801.09811, pp2–3 and Appendix B, define an output-independent preparation and explain that later coupling to an environment can restore old dependence. The primary paper was read directly. Its two-SWAP counterexample is acknowledged as prior art, not a new discovery in the controls here. The native code obstruction is the application-specific discriminator.

## 2. Physical geometry and operational domain

Place target x at an actual native edge midpoint, for example(1,0,0). Its program site c=x+e_y, entropy sink a=x-e_y, and witness fragment w=x+e_z are three distinct actual physical nearest neighbors. In the original native fixture these are spectators, not adjacent BKSF edge qubits. Activating them is an additional apparatus, not a reinterpretation of graph incidence. The other three neighbors are fixed spectators. The program site has a definite supplied binary Record content r represented operationally by|r><r|. The sink and witness are unrecorded, supplied fresh in|0>. Their absence is a tagged condition, not a readable zero Record.

A declared preparation history h may carry ANY target/reference density rho_xE^h, entangled or classically correlated with arbitrary external history data. For each h the sink and witness must be fresh product factors; the program is a definite classical r. This freshness and the representation of the program Record are imports. The complete six-neighbor condition includes r, these supplied roles, and the fixed absence pattern. It does not include rho_xE^h. A rotated/translated apparatus has the corresponding transformed roles and axes; this gives a covariant family of supplied apparatuses, not an autonomously selected homogeneous lattice law or an axiom-derived common frame.

No interaction with the exported sink or external reference is allowed between preparation and readout. Later permanence is only asserted under operations commuting with the recorded pointer projectors; no irreversible absorption is obtained from a finite closed unitary merely by naming a fragment a Record.

## 3. Actual local preparation and sharp history dependence

Use the two-qubit exchange U_t on target,sink, with0<=t<=1 and a=sqrt(1-t²):

U_t|00>=|00>, U_t|10>=t|10>+a|01>,
U_t|01>=t|01>-a|10>, U_t|11>=|11>.

This is a nearest-neighbor unitary. With fresh sink|0>, its reduced channel has Kraus operators K0=diag(1,t), K1=a|0><1|. It is not assumed as a probability table: these matrices are extracted from the actual unitary. Then apply a program-controlled target rotation R_r=[[c_r,-s_r],[s_r,c_r]], with(c0,s0)=(3/5,4/5) and(c1,s1)=(4/5,3/5). The control acts on the physical neighboring program and commutes with its content projectors, so it leaves every definite old program Record unchanged. The chosen coupling/angle and time of application are supplied.

For the native target sign outcome represented by P1=|1><1|, the complete incoming effect is

E_r,t = sum_i K_i^* R_r^* P1 R_r K_i
      = [[s_r², c_r s_r t],
         [c_r s_r t, s_r²+(c_r²-s_r²)t²]].

Thus the Born instrument probability is Tr(E_r,t rho_x^h). The Born probability principle is an explicit input, but the equality and its history dependence are derived from the actual local operations, not postulated separately for each preparation.

At t=0, E_r,0=s_r² I and the full replacement channel satisfies

(R_r ∘ reset ⊗ id_E)(rho_xE^h)=|psi_r><psi_r| tensor rho_E^h,
|psi_r>=c_r|0>+s_r|1>.

The identity holds on all operator matrix units and hence with arbitrary reference. Consequently every complete earlier history in the declared domain gives p(1|h)=16/25 for r0 or9/25 for r1. This is a nonconstant two-condition operational family with exact history-independent target odds. The exterior state remains history dependent; only decoupling/no-return prevents that information returning.

For partial reset the full range of probabilities over arbitrary incoming target densities is the eigenvalue interval of E_r,t. Its exact diameter is

D_r(t)=sqrt(4c_r²s_r² t²+(c_r²-s_r²)²t⁴).

The best constant approximation over all these preparations has worst-case error D_r(t)/2, attained at the interval midpoint s_r²+(c_r²-s_r²)t²/2. For the two frozen programs and t=3/5, D=9sqrt(1649)/625; at t1 it is1. Every t>0 has positive D for these programs, so exact full-domain local-history sufficiency fails. This is sharp by eigenvector inputs, not a finite-sample bound. It quantifies the preparation task instead of assuming away hidden history.

## 4. Actual joint pointer support, and the still-open Record step

Apply nearest-neighbor CNOT from target to fresh witness, giving V|psi>=P0|psi>|0>+P1|psi>|1>. Then

(P0 tensor P1+P1 tensor P0)V=0.

This zero-mismatch operator identity holds on every input and reference, not just equal marginals. Reading/dephasing the witness in the supplied Z instrument gives exactly sum_z P_z rho P_z tensor|z><z|. The target outcome and witness pointer have a derived diagonal joint law. Under later pointer-nondemolition operations those quantum pointer labels persist.

This does NOT establish that either pointer is the framework's permanent Record. A physical calibration declaring the target pointer outcome to be its supported Record content, actual target formation, and a future dynamics preserving that content remain separate inputs. In particular the witness is not first made into an unrelated Record with inaccessible preparation data: doing that would create another local-condition obligation at its site. The calculation supplies a quantum writer candidate with actual joint support, not an unlicensed semantic quantum-to-Record map. PR7047's equation(4)/(5) interface is narrowed operationally on this domain but not retired.

There is no hidden blank-plus-two-outcomes embedding in one ordinary qubit. Absence is external status in the declared condition; the witness ready vector equals one possible final quantum label. A repeated total absorbing channel would require a guard/freshness structure or an irreversible resource process. None is inferred here.

## 5. Decisive failure on the actual native code

The actual square BKSF vacuum is GHZplus on its four edge qubits, with cycle S=-X0Y1X2Y3 and cycle projector P=(I+S)/2. Apply the exact t0 replacement to edge0, leaving the other three edge qubits untouched. The output is

rho' = |0><0| tensor (|000><000|+|111><111|)/2.

Directly Tr(P rho')=1/2, whereas the original N0 vacuum projector has expectation1/4. The circuit has exported coherence required by the code. It is therefore NOT an admissible native-code-preserving preparation operation on this original square, even though it is a perfectly valid local M2 channel. Subsequent native CAR statements cannot be imported on rho'. A programmed rotation afterward does not restore the lost code correlations.

There is a general local restriction. For a stabilizer S=sigma_x tensor R with sigma_x a nontrivial one-qubit Pauli and R having both signs, consider a target-only CPTP map preserving the entire +1 code. For every Kraus K, positivity of the leaked weight implies P_minus(K tensor I)P_plus=0. In the sigma eigenbasis, input code vectors include |+> tensor Ran(R+) and|-> tensor Ran(R-). Any off-diagonal element of K takes one into the wrong S sector. Hence every K commutes with sigma. Trace preservation then preserves the populations of sigma's two eigenstates. Such a channel cannot replace all code inputs by one fixed local state. The conclusion is restricted to a channel supported on that single edge and this entire code domain; multisite corrections, code changes and restricted preparations are not excluded.

Even more narrowly, if a target-only channel preserves the pure square vacuum itself, each Kraus maps GHZplus to a scalar multiple of itself. Its Schmidt rank across the target/rest cut is2, so every Kraus is scalar I on the target. Thus the channel is identity. A nontrivial local reset cannot preserve that fixed vacuum, not merely its entire code. This is an exact obstruction to this candidate route, not a universal Record-writing no-go.

## 6. Evidence and remaining obligation

The executable checks51 exact assertions: extracted exchange Kraus operators, completeness, symbolic effect and diameter, all16 target/reference matrix units, both programs and three frozen reset amplitudes, zero-mismatch joint pointer support, actual native code/vacuum leakage, and wrong freshness/returned-memory/wrong-label controls. The first symbolic attempt failed because SymPy was not told0<=t<=1 when conjugating sqrt(1-t²); a real exchange amplitude and algebraic substitution repaired domain handling. A subsequent matrix-times-bool TypeError was replaced by an integer Kronecker delta. Both sources/errors are preserved; neither changed the physical parameters or target. No failure was reclassified as a theorem PASS.

The hardest remaining task is a native-code-compatible, spatially local preparation/export mechanism which registers enough lawful nearby Record information to determine the instrument effect on its full history domain, while retaining the claimed CAR/code physics. It must also provide the semantic formation/calibration and a no-return/permanence resource law. Pure local reset solves the operational probability problem by changing precisely the native structure one wants to preserve. The next useful route is explicitly multisite code-preserving preparation or a physically justified smaller code domain, not a relabeling of this failed reset as the desired supplier.
