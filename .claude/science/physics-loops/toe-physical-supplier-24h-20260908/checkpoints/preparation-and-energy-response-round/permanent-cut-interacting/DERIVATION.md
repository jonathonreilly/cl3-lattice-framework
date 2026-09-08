# Permanent cuts: valid state invariant, invalid unrestricted encoded inference

2026-09-08. Conditional exploratory result. Root's original PREREGISTRATION.md is preserved. The two counterexample/extension preregistrations precede their calculations. No canonical claim, axiom, gate admission or audit verdict is assigned.

## Verdict

The terminal-refinement argument is valid as a one-component convex-Gaussian state invariant for initially Gaussian states (and their classical mixtures) in the declared permanent-cut class. It does NOT justify the proposed unrestricted conclusion about every encoded all-input density-density filter. A concrete six-physical-qubit native apparatus supplies an encoded two-mode density filter, and also a hopping-plus-density filter, on its entire four-dimensional ready domain. Its apparent interaction is quadratic on that parity-constrained physical domain. This is a useful special construction, not a generic interacting matter preparation algorithm.

## The part of terminal refinement that works

Fix a finite resolved classical history. Its scheduled number-conserving quadratic unitaries are then definite operators, even if the program was adaptive. Every earlier bridge projector is a component-parity projector. All subsequent componentwise quadratic controls and later component-parity projectors commute with it. Moving that projector to the END is legitimate; replacing it by early individual occupations is not.

An ancestor component is a union of final components. Choose one final surviving component C. Refine all other physical components by complete occupation measurements at the terminal time, then discard their results if desired. Their occupation configurations fix every parity not involving C. On a fixed global parity input sector, C's parity is also fixed by those occupations. Therefore each product of terminal bridge projectors becomes either zero or the identity on each refined branch. What remains is the fixed Gaussian unitary sequence, followed by individual occupation projections on the discarded modes. Each refined retained state is Gaussian (or zero). Summing the refined outcomes gives a convex mixture of Gaussian states on C. An initial classical Gaussian mixture is resolved first. Nonbridge source events are the fair surviving-CAR isometries and contribute their scalar factors/dictionary changes, not a new non-Gaussian projector.

This argument is in the source's conditional CAR dictionaries, retaining original boundary signs. It assumes subsequent controls never cross a severed component and that the target is recovered into ONE final component. It is not a statement that a multi-component post-measurement pure state is Gaussian. References outside C cannot simply be annexed to C to turn a reduced-state invariant into a joint-state invariant. Nor does an arbitrary ready/reference input satisfy the initial Gaussian hypothesis merely because the ready ancillas are product states in physical edge coordinates.

The finite stress test retains the odd-discard-parity branch of the six-mode Slater (c0†+c4†)(c1†+c5†)|vac>/2. It is (|05>-|14>)/2 and globally non-Gaussian. After a discarded45 rotation with c=3/5,s=4/5, the terminal refined retained columns are C=[[s,c],[-c,s]]/2. Their sum of outer products is I2/4, exactly the direct retained marginal. Each column is a one-particle Gaussian state. Premature discarded occupation dephasing removes the conditional off-diagonal -3/25 in the first refined state. It preserves its probability and the unrefined marginal. Thus early refinement fails at the conditional-state level; no false adverse claim is made about the unrefined marginal.

The pure-output version of the invariant is sound: if a protocol starts with a Gaussian state and produces a pure state on one retained component, that state is Gaussian. But to rule out a proposed instrument with this argument one must exhibit an allowed Gaussian initial state whose intended pure NON-Gaussian output lies in that one component, using the ACTUAL encoding/recovery map. A formal logical quartic symbol is not sufficient.

## Actual native six-edge counterexample to the broad encoded corollary

Use active path0--1--2, leaves3,4,5 attached respectively to0,1,2, and an inert anchor6 attached0. Virtual coordinates are (0,0,0),(1,0,0),(2,0,0),(0,1,0),(1,1,0),(2,1,0),(0,0,1). Physical edge qubits lie at doubled-coordinate midpoints. There are six distinct M2 factors, maximum degree3, no cycle constraints, and the native global even seven-mode CAR representation.

Fix the three sacrificial physical leaf Z values to + and anchor Z to -. These are supplied UNRECORDED ready preparations. The remaining two physical qubits may carry arbitrary state. The ready projector is

 P=(I-n3)(I-n4)(I-n5)n6,

of rank4. Its active parity is odd. Define logical labels by occupations n0,n1; the compatible third occupation is

 n2=1-[(n0+n1) mod2].

The physical code isometry E maps all four logical basis vectors to these actual ready basis vectors (up to the fixed source dictionary phases). It is not a tensor-product embedding of logical matter with an independent fermionic parity ancilla. On this domain the exact operator identity is

 n0 n1 P = (n0+n1+n2-I)P/2.

The identity fails on the full ambient Hilbert space; the finite checker explicitly rejects that extension.

Apply the ordinary native hopping pulse to each vacant leaf, with cosine r=3/5 and sine4/5. Record that leaf's physical Z, delete its incident hopping, and accept the three unchanged contents. No matter bond is cut. The full success map is

 K=P_success U25 U14 U03 P
  =r^(n0+n1+n2)P
  =r exp[-g n0 n1]P,   g=2log(5/3).

In logical00,01,10,11 order its amplitudes are r,r,r,r^3. It is full rank on the whole ready domain, and therefore the operator equality extends to an arbitrary external reference. All eight branch maps are evaluated; their effects sum to P. Each output has exactly its recorded leaf values and unchanged anchor. Old Records are preserved by subsequent pulses; leaves are never reactivated. The surviving active path remains connected.

The rank4 ready state P/4 is a literal product state in physical edge coordinates, but its active fermionic interpretation is the uniform odd-parity three-mode state. Its parity mode is correlated with logical labels. It is a classical mixture of Gaussian occupation states, not an independent fermionic Gaussian ancilla appended to arbitrary two-mode input. Hence neither the original strict Gaussian independent-ancilla filter obstruction nor the valid convex-Gaussian permanent-cut invariant forbids this construction.

## Nonzero hopping plus density, still with exact outcomes

On the same odd active code, for real t,u,

 H_log=t T01+u n0 n1
      =[t T01+(u/2)(n0+n1+n2)]-u I/2.

The physical bracket is quadratic. Its one-particle eigenvalues are u/2+t,u/2-t,u/2. The already supplied phase/hopping rotation on01 diagonalizes it. Vacant or filled leaf filters for these three energies therefore give

 K=c_phys exp(-beta u/4) exp(-beta H_log/2)P,
 c_phys=exp[-beta sum_negative|epsilon|/2].

If some leaves are initially filled, choose the inert anchor occupation so that the active parity is still odd: anchor parity equals1 plus the sum of leaf occupations modulo2. The anchor is an inert supplied physical ready site, not a free change of fermion parity. Zero eigenvalues use r=1 and deterministic leaf outcomes. The final successful leaf values return to the initial ones, so the same encoded relation remains valid.

The executed nontrivial fixture is t=1,u=2,beta=2log(5/3). Put D=n0-n1 and W=exp(-i*pi*D/4)exp(-i*pi*T01/4); WDW†=T01. Then W(2n0+n2)W†=T01+n0+n1+n2. Use the three vacant cosines r^2,1,r. The complete operator check gives

 K=r exp[-log(5/3)(T01+2n0n1)]P.

On T eigenvalues -1,+1 the target amplitudes are1,r^2; on logical00,11 they are r,r^3. Success probability on P/4 is6001/15625, conditional H is -6071/12002, and conditional hopping is -200/353. All eight branches, including zero-weight outcomes at the r=1 leaf, remain in the computation. This is an actual native physical Kraus identity, not a fitted trace or a classical reassignment of Record labels. The successful logical even-algebra functional is the Gibbs functional of H_log, with partition function 1+2cosh(beta t)+exp(-beta u).

## Scope, failure controls and next question

check.py reports58 exact assertions; hopping_check.py reports51. They use complete physical64-by4 Kraus columns, source A/B/T matrices, actual leaf projectors, all effects, geometry, rank and Record support. The two totals are separate overlapping fixtures, not109 independent scientific obligations. A mutant exchanges the actual hopping pulse cosine and sine, preserving unitarity but changing the attenuation; it fails the fixed full-Kraus target predicate. The prior early-dephasing issue is preserved as a discriminating conditional-state test.

The needed controls, occupation initialization, ordinary tensor composition, Born/Lueders events, pulse schedule and energy/work supply remain explicit. No interacting primitive was added. The density term ceases to be a genuine physical quartic on this restricted three-active-mode parity code; calling this a generic interacting Hamiltonian realization would be misleading. In particular arbitrary three-or-more logical modes, independent fermionic reference/ancilla extensions, or a quartic whose restriction cannot be rewritten quadratically require a separate proof or counterexample.

The prior interacting-preparation DERIVATION.md has been archived verbatim and prefixed with a domain correction. Its Gaussian/independent-ancilla witness remains correct in its stated domain; its no-construction sentence is now historical. The positive encoded extension and the valid permanent-cut state invariant coexist.

## Three logical modes: the exceptional shortcut ends

A prospective five-check supplement tests the root's next discriminator without changing the earlier fixtures. With three logical modes and one parity reservoir, the active code is the even four-mode sector. In its fixed-N=2 subspace, any diagonal one-body energy satisfies

 E01+E23=E02+E13=E03+E12.

For n0n1 these sums are1,0,0. On the whole eight-dimensional even code the affine occupation design has rank5, and adjoining the n0n1 column raises rank to6. Off-diagonal one-body hopping cannot rescue an equality with this diagonal operator: each hopping has observable off-diagonal matrix entries between legal N2 configurations, forcing its coefficient to vanish. Thus there is no quadratic rewriting of this interaction on that code.

More strongly, the four-mode Slater (|01>+|03>-|12>+|23>)/2 is a legal native even-code state, now with three logical modes and the fourth parity reservoir. exp(-log2*n0n1) gives Pluecker value -1/8. If an all-ready-input protocol in the permanent-cut class returns ALL FOUR active modes, including this reservoir, into one final connected component with the original target dictionary, its desired output on that Gaussian input is pure non-Gaussian. The proven terminal-refinement invariant excludes that exact successful map with nonzero probability, assuming additional ancillas begin in occupation-product Gaussian states or their classical mixtures. The witness may be prepared by the supplied quadratic controls before the protocol; it does not require an initially non-Gaussian state.

This is a conditional recovery-domain obstruction. It does not exclude distributed output, changed encodings, a reservoir left outside the recovered component, initially non-Gaussian resources, reconnecting old cuts, or nonquadratic controls. The two-logical-mode encoded counterexample and this three-logical-mode single-component discriminator are therefore consistent. A parity-reservoir label is not an independent Gaussian ancilla; its exact placement and recovery must be part of each theorem's input/output contract.
