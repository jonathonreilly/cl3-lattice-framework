# Preregistered smallest native-cell control attempt

2026-09-07. Frozen before control-nullspace or Lie-algebra computation. No repository edits. This is a new conditional fixture, not a retuning or claim about the previously frozen square/cube. The target is a real complete native Z event with hopping, fuel lowering, head motion, battery transfer and accepted label. The permitted controls are an explicitly supplied ansatz, not consequences of M2(C) or an approved gate primitive.

## Inputs read

The orbital PHYSICAL_COMPILATION_PREMISE_MAP.md and native collision PREREGISTRATION.md and REVIEW.md. Their conditional-composition/control/clock/role and fresh-label gaps remain. The square collision witness is a motivation, not imported numerical evidence for this smaller fixture.

## Minimal carrier and exact target

Use the connected two-vertex, one-edge graph, in its supplied odd-parity native representation. One edge qubit x represents B_v=Z_x, B_w=-Z_x, A_vw=X_x. Thus N=(1-B_v)/2+(1-B_w)/2=1 identically, and the whole real hopping is h=-i A_vw(B_w-B_v)/2=Y_x. The minus sign on B_w is a supplied odd-parity boundary convention. No cycle stabilizer is needed on this tree. This is the smallest nonzero hopping carrier; deleting its only edge is a bridge deletion and retains both component parity sectors through the physical edge-Z signs.

A fuel qubit f has q=(I-Z_f)/2, so charged means |1>. The original and conserved energy for this integer-spectrum fixture is

    K = q (I+Y_x) + E_B,
    E_B = (1/2)I + n_b0 + 2 n_b1.

The battery uses four positive levels 1/2,3/2,5/2,7/2, delta=1 and cap4. No rounding error exists here. The surviving matter Hamiltonian after q=0 is zero. Heads h_v,h_w use one-hot computational encoding; source is |10>, destination |01>. Two zero-energy collision-label qubits l0,l1 encode vacuum00, accepted+01, accepted-10, refusal11. Add an old Record sentinel r with Z_r fixed, making permanence a nonvacuous control constraint. Nine physical qubits in total.

The native complete sign effects are P_z=(I+z Z_x)/2. Let Pi_+=(I+Y_x)/2 and Pi_-=(I-Y_x)/2. The accepted finite battery operator for sign z is

    J_z = |01><10|_head tensor |0><1|_f
          tensor [P_z Pi_+ tensor T_2 + P_z Pi_- tensor I_B],

where T_2 raises the battery by two cells and is zero at its upper boundary. Its accompanying collision factor is |label z><00|. The complement is one combined-sign refusal on the eligible source, not one refusal per sign. This defines an actual native event column and its star interaction, although this first test asks only whether a selected accepted transition is accessible.

Freeze source |s> = |Y+>_x |1>_f |10>_head |00>_battery |00>_label |0>_r.
Freeze target |t> = |Z+>_x |0>_f |01>_head |10>_battery |01>_label |0>_r, where battery notation here is high-bit-first (b1 b0).
Both have total energy 5/2. The exact accepted-plus star matrix element has modulus 1/sqrt(2), not zero: P_+|Y+> has that norm and the battery really rises from1/2 to5/2. This target is not an unrelated qubit swap. Testing its reachability is only a necessary small part of implementing the full coherent event instrument.

## Embedding and allowed Hamiltonians

Place the nine qubits on the Z3 nearest-neighbor line, coordinates (j,0,0), j=0,...,8, in this order:

    r, h_v, h_w, x, f, b0, b1, l0, l1.

The only nontrivial matter-energy term qY_x has adjacent support. Battery energy is on-site. The frozen NN graph is this path. No auxiliary sites, variable placements, detunings, supplied SWAPs or post-result additional couplings are allowed in this attempt.

A real control Hamiltonian is a real linear combination of Hermitian Pauli words of weight at most two, with a weight-two word supported on an allowed graph edge. Including one-body words makes the ansatz more generous than strictly two-nonidentity-site terms; report both the exactly-weight-two subspace and the at-most-two subspace. Require exact [H,K]=0, [H,Z_r]=0, and [H,N_head]=0, where N_head=n_hv+n_hw. Also require [H,P_legal]=0 for the COMBINED legal subspace: (f=1,head=10,label=00) OR (f=0,head=01,label=01 or10) OR (f=1,head=10,label=11), tensored with the full edge/battery space and r=0. This is a diagonal projector with an exact Pauli expansion. Do not require preservation of its separate source, accepted or refusal summands: their mixing is the target. No further commutation with fuel, battery, new-label or edge Z is assumed. The old Record remains untouched as content; the selected edge is not an old Record initially. Intermediate workspace states need not already be accepted events. Label locking after a completed collision would require an additional formation/dynamics rule and is not silently supplied by this coherent reachability test.

First compute the complete-graph at-most-two-site commutant as a generous diagnostic. This cannot establish NN success; failure to find a direct source-target matrix element cannot establish failure of its generated Lie algebra. Then perform the fixed NN calculation. Both ansatzes are preregistered, not substitutions selected by results.

## Exact computation and proof plan

Represent Pauli words by binary x/z masks and exact Gaussian-rational coefficients; use the phase convention making each basis word Hermitian. Expand K exactly (quarters/halves only). Form coefficient dictionaries for commutators with K, Z_r, N_head and P_legal and solve the real rational homogeneous system. Record every basis vector and its exact residual. Avoid a dense 512x512 matrix or dense 4^9 operator basis.

Evaluate direct <t|H|s> only as a diagnostic. For reachability, first search for exact conserved projectors/charges commuting with every allowed control, particularly fuel or energy-degeneracy components. An exact invariant separating s and t proves failure for this frozen control family, including all concatenations and time-dependent schedules. If none separates them, compute the smallest invariant state space generated from s by the control basis inside the fixed energy5/2, head-number1 and r=0 subspace, using exact sparse amplitudes over Q(i,sqrt2). Intersect that space with the combined P_legal subspace. A target outside that cyclic space is a valid obstruction. A target inside it is not sufficient for controllability: then calculate the restricted dynamical Lie algebra or provide an explicit sequence of admissible exponentials taking s to t with verified phase. No endpoint-only argument will be called a Lie-algebra no-go. Constraints apply to the SUM of each Hamiltonian, not separately to each Pauli word; cancellation such as XY exchange must survive. Each allowed control commutes with K; externally work-driven nonconserving pulses are outside this particular ansatz.

The energy5/2 eigenspace is explicitly enumerable: q=1,Y+=+1 requires battery1/2; q=1,Y-=-1 requires battery5/2; q=0 allows both edge states at battery5/2. Heads and labels multiply these small degeneracies. Transform to a Y-eigenbasis only for small restricted exact calculations; this is a mathematical basis change, not an assumed physically available rotation.

Controls: perturb a returned commutant coefficient to fail conservation; test a known forbidden one-site fuel flip; test a known allowed diagonal Hamiltonian; verify target matrix element and energy directly; compare NN basis inclusion in complete-graph commutant; distinguish a deliberately disconnected endpoint from direct-matrix-element-zero but multistep-connected examples in the algebra routine. All resource runners use one BLAS thread,180 seconds and180 MiB, and report exact ranks plus hashes. Resource failure is unresolved, never evidence of a physical obstruction.

## Frozen interpretation

Success would be a conditional state-transfer construction under the declared controls, not synthesis of the complete collision, permanence of newly formed Records, a covariant rule, an axiomatic interaction primitive or universal compilation. Failure would concern this explicit carrier/encoding/control support and energy model only. No controls, energy levels, target, graph, parity convention or auxiliary count will be changed after the first result; any later fixture must receive a separate preregistration.
