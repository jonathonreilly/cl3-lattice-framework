# Conditional physical preparation and permanent-history locality

This is a small constructive discrimination result, not a proposed second canonical block or an axiom-selected formation law. It continues the charged-history supplier proof. Exact source comparison is below. No physical simulation was run.

## Supplied physical family and actual preparation

On a finite nearest-neighbor bipartite qubit graph H=A union B (or the checkerboard Z3 graph), supply A qubits in |+>, B qubits in |0>, a common pointer basis, and real rotation R(theta)=exp(-i theta Y). Apply R(theta0) to each B and the actual two-site nearest-neighbor gates

 U_ab = |0><0|_a tensor I_b + |1><1|_a tensor R(theta)_b.

All these gates commute: controls occur only in A and Y targets only in B. Their product gives the normalized state

 Psi = 2^(-|A|/2) sum_a |a> tensor product_b R(theta0+theta sum_(a neighbor b) a)|0>.

This is a preparation from one fixed two-body interaction family, not synthesis of an arbitrary conditional probability table. Edge coloring schedules its gates in bounded depth (six layers on the cubic lattice), independently of volume. The commuting product defines a quasi-local automorphism in infinite volume: for a local observable only gates incident to its original support contribute. No extra pointer/ancilla factor is introduced in preparing this state. Ordinary Born/Lueders measurement and the Record interpretation are still premises.

## Exact state-action closure on eligible prefixes

Allow an unrecorded A to form at any time. Allow a B only when ALL its A neighbors already have Records. Use raw pointer contraction at each formation, preserving its outcome permanently. For a prefix (R,a_R), every recorded B has only recorded A neighbors. In the displayed wavefunction its scalar factor is therefore independent of all unrecorded A values. Removing all recorded coordinates leaves, up to one scalar,

 sum_(a on A minus R) |a> tensor product_(b in B minus R) R(theta0+theta sum_(a neighbor b) a)|0>.

Recorded root values in the angle are fixed. Every remaining B factor has norm one, so the squared norm of this vector is 2^|A minus R|. It follows directly from the actual contracted quantum vector that:

* every eligible A has conditional outcome probability 1/2;
* every eligible B has probability sin²(theta0+theta k) for outcome one, with k its number of recorded-one A neighbors;
* the normalized residual vector retains the same family after either branch.

These statements hold after arbitrary earlier eligible B outcomes, not merely after an all-A-first sweep. They concern every positive-probability prefix, not a favorable postselection. Stopped prefixes are precisely order ideals for the depth-two dependency graph. Classical order-ideal factorization alone is prior material; the displayed native-qubit preparation and quantum residual closure are the narrower contribution.

If these qubits are the supplied edge factors of the charged-history dictionary, its raw deletion maps give the same contractions exactly. Passing to its standardized positive-Gauss frame inserts known diagonal Z dressings and coherent history phases, which preserve all pointer probabilities. This is algebraic compatibility, not authorization of those frame changes as physical pulses. Further, an abstract edge-label adjacency is NOT automatically physical nearest-neighbor adjacency in the cubic link embedding. The strict-nearest-neighbor preparation claim is for H's declared physical qubit adjacency. A native link encoding with separated edge centers needs its own routing/resource proof before inheriting that claim. No matter-hopping dwell is inserted after preparation; a generic such dwell would not preserve this family.

## Outcome-independent local clocks and infinite construction

Supply independent rate-lambda exponential clocks, independent of the quantum preparation and outcomes. Set T_a=E_a on A and T_b=max_(a neighbor b) T_a + E_b on B, with all E independent. This is equivalently a rate-lambda local Poisson clock accepted at B only after readiness, by memorylessness. Clock history depends on site/Record membership only, not their values, so conditioning on the entire realized clock history does not reweight any quantum branch beyond its observed outcomes. In particular there is no hidden event-selection bias in the fair-root claim.

Every site time depends on at most seven independent clocks. This defines the infinite process directly, without a first global event. Each site records once; bounded spatial windows have finitely many events on bounded time intervals. Every site forms at finite time almost surely. For a B of degree at most six,

 P(T_b>t) <= 7 exp(-lambda t/2),
 E T_b <= (H_6+1)/lambda,

by splitting at t/2 and by the mean maximum of six exponentials. There is no finite total number of events on the entire infinite lattice, and no such claim is required. The birth generator is local with root rate lambda and target rate lambda times readiness. Its outcome rates are exactly the quantum conditional probabilities above.

The checkerboard role pattern, start slice, clock scale, preparation, pointer axis and irreversible Record interpretation remain supplied. This is covariant under symmetries preserving the supplied role field, not an axiom-selected translation-invariant empty-lattice law. Randomly hiding the role field is not a repair: it can create extra conditional information and requires its own proof.

A role-free restricted corollary starts instead with an already recorded set whose complement is an independent set of isolated holes. At each hole prepare the same rotation using its recorded nearest neighbors, and allow a rate-lambda append only when all six neighbors are recorded. Roles are then Record-visible, and the rule is translation/proper-cubic covariant with the supplied pointer basis. This fills the isolated holes but does not propagate from a finite seed, generate calibration/preparation, or solve the original empty-lattice formation problem. It is not claimed to surpass the prior Record-visible controller construction in physical selection.

## Exact discriminatory control

locality_check.py uses the physical five-site path A0-B0-A1-B1-A2 and rational rotation cos(theta)=3/5, sin(theta)=4/5, theta0=theta. It applies the actual two-site gates to a 32-entry vector (the common sqrt(8) normalization omitted), then checks its equality with the claimed state. It enumerates 107 distinct eligible partial histories, checks every eligible next probability, and verifies the full remaining amplitude vector is proportional to the claimed residual family. 831 exact Fraction predicates pass.

Dropping eligibility fails locality itself, not only fair-root labeling. Given B0=0, conditioning additionally on the distant B1=0 or B1=1 changes P(A0=1) from 53137249/67337474 to 7922297/12836722. The nearest neighbor of A0, namely B0, has the same Record content in both cases. This is a precise remote-evidence counterexample to unrestricted formation from the same prepared state. Boundary neighbors can be fixed identically in both fixtures; no infinite-volume conclusion is inferred from the test.

## Actual prior comparison and decision

Source snapshots/pins are in locality_sources/PINS.json. Read #8011 at11395e60: its entire priority-formation proof already gives local marked infinite birth laws, permanence, all-or-none eligibility as an odds-preserving option, and the order-ideal/mark-independence criterion. Its explicit residual is the quantum/Born bridge. I do not claim a new probabilistic process theorem here. #8012 at910fb7 is a concentration/profile variational theorem, unrelated to this quantum preparation mechanism.

Current main0c52 finite-law note: read its contract, three partial-condition readings, formation/static definitions and theorem statements. It already warns that static marginals generally have nonlocal evidence. The monotone-law note's displayed DAG factorization and non-Markov corner examples are likewise prior; no rebranding as a new law is justified. The August14 Record-visible integrated-instrument note's controller, sections1–7 and resource boundary already supply finite compatible instruments plus a live-M2 comparator. The June18 controlled-copy theorem already supplies a fresh-fragment write isometry under a chosen kick and calibration. The open7326 at59439913 result/contract/first-mark sections already supply indexed marked-Poisson semantics under an explicitly selected action and clock; no source-current selection is obtained here.

The remaining distinct calculation is an explicit ancilla-free nearest-neighbor quantum state family with exact all-eligible-prefix closure, compatible with permanent contraction histories, and a sharp counterexample when eligibility is removed. It replaces an arbitrary joint table by a small fixed interaction family but does not derive the physical choice of that interaction or the irreversible readout. This is useful as a supplier test fixture; it is not yet a high-value standalone physics PR. The genuine next obligation is to obtain preparation and eligibility from the same native physical dynamics without imported checkerboard roles or external clocks. Nothing in this calculation claims that obligation is discharged.
