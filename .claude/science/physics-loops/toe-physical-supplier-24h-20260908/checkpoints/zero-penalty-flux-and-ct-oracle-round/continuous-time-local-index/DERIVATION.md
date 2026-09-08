# Local event indexing for the CT selected-face conditional

This is a source-bound design and deterministic reference data structure, not a new sampler, timing result or mixing theorem. It imports the complete30391 CT quotient proof and the2ddd integrated conditional implementation, with the explicit native alias erratum. Actual L2/L4 geometric masks are unique. The target remains the supplied CT exp(-TH) ensemble on one seed-reachable component, with free endpoints and total path time T.

## State representation and invariants

Maintain one immutable event record(time,id,geometric_label) for each actual nonself flip. Times are globally distinct and lie strictly between0 andT. Keep a global ordered tree, one ordered tree per face label, and one ordered tree per physical edge containing exactly events whose face toggles that edge. Tree keys are(time,id); subtree sizes support prefix parity. The initial bit configuration and a legal seed-to-initial witness are retained.

An edge bit immediately before t equals its initial bit XOR the parity of events on that edge with time<t. This defines a consistent left-limit convention on deterministic fixtures. Generic CT random event equality at a fixed measurement time is measure zero, but the implementation does not leave that convention ambiguous. Each global event occurs in exactly four edge trees and one face tree. The global trajectory remains legal; a selected-face replacement must prove local legality before root commit. Persistent AVL roots permit atomic updates and preserve prior roots when requested.

Initial construction is NOT free: all events and component provenance must be validated and indexed. The current reference constructor calls the full existing trajectory checker, including repeated global ice checks; this costs more than the optimal legal-flip-induction constructor. Building balanced indexes costs at least linear work in total events (the present insertion implementation costs O(N logN)). This is setup, not falsely included in a claimed constant per-face update.

## Exactly which events matter to face p

Let A_p be the set of plaquettes touching any edge of p, and U_p the union of all edges in A_p. Delta_p Nf=sum_(r in A_p)[legal_r(x XOR p)-legal_r(x)] depends only on bits in U_p. For the L4 fixture |A_p|=13 and|U_p|=32; only bounded-range geometry, not these exact numbers, is needed.

Merge the edge-tree iterators for edges in U_p and deduplicate event IDs. These are precisely events with support intersecting U_p. Let K_U count them, including old p events. Each contributes at most four iterator entries, so the query visits at most4K_U event entries. The merge costs O(K_U log|U_p|), with no traversal of strict-distant events. Old p events must still be read to reconstruct the baseline local orientation and to delete their records, even though they are absent from the new conditional skeleton.

Track the baseline bits on U_p, applying every queried event restricted to U_p. Remove old p events only from the transfer skeleton. At every retained local event, record the distinct p orbit and canonical ordering; the ordering of x and x XOR p depends only on the highest p bit, so remote bit changes cannot swap this ordering. Diagonal differences require only A_p legality checks, not global Nf. For a retained q touching p, all q edges lie in U_p and its full0/1 compatibility is checked there. For q disjoint from p but intersecting U_p, q legality is unchanged by the candidate p flip and is guaranteed by the valid baseline; its restricted XOR map is a bijection, though it may change Delta_p Nf and therefore still supplies a message breakpoint.

A strict-distant q has no edge in U_p. It changes neither p legality nor Delta_p Nf; it is legal on exactly the same p alternatives, commutes with the p flip, and has identity transport in the canonical local coordinates. Its possible change to the absolute global Nf is a common holding scalar across the face conditional. Therefore all such events can be omitted from the TRANSFER calculation and adjacent local intervals merged. They remain in every physical trajectory/index. The full30391 orbit skeleton is reconstructed by carrying its outside bits along those unchanged events; no outside degree of freedom is resampled or discarded.

Thus local transfer matrices and initial/end conditional messages depend on K_U, not the number of strict-distant events. They still depend on relevant near events even when those events appear unimportant on one baseline configuration. Overlapping gated plaquette maps can be noncommuting: the other order can encounter an illegal flip. Such events are handled by partial/singleton compatibility, never by a generic commuting-X argument.

## Persistent splice and locality of legality checks

Remove all old p event records and insert the new p times. Only the selected face tree and the four p-edge trees change, together with the global tree. Each deletion/insertion copies O(logN) AVL nodes. Updating those five roots plus the global root is atomic after checks; there is no full copy of every edge/face root map. Retained event IDs, labels and times are unchanged. If the first state flips, update the four initial p bits and append p to the witness.

For candidate legality, replay only the new p events and retained U_p events on local bits. Check every p flip and every retained q touching p explicitly. A retained q disjoint from p has the same bits on its own support as before and therefore keeps its baseline legality. Strict-distant events need no replay. This proves global legality by induction from the valid baseline. The prototype performs these local checks before mutation.

Floating event-time collisions require an additional GLOBAL logarithmic lookup: a new p event could coincide with an ignored distant event. The global ordered tree detects this without scanning the trajectory. A collision or local incompatibility rejects the entire proposed splice; no retry, deletion of the other event, or silent reordering occurs. Persistent roots ensure failures leave the previous index unchanged.

The resulting update cost includes O(K_U log|U_p|) local extraction, local-message/bridge work, and O((N_p_old+N_p_new) logN) tree splicing/collision checks. It is not literally O(K_U) with all logarithmic/global bookkeeping suppressed. Event generation can itself be expensive; no bound on N_p_new or physical mixing is supplied. The small Python prototype also uses packed arbitrary-size integers, whose bit-operation cost grows with word count; an actual large-volume implementation would need chunked random-access initial bits rather than pretending big integers are constant-time at arbitrary volume.

## Observable reconstruction and unavoidable global costs

At any fixed t, the new and old full configurations differ by either zero or the entire p mask. The common flip flag is initial_flip XOR parity(old p events<t) XOR parity(new p events<t). Hence a cached midpoint/end Nf updates through A_p only, and a fixed finite Fourier-source menu updates from four link changes. Endpoint overlap changes on those four links only. These caches require a full correct initial construction and checked update formulas; arbitrary global observables do not automatically have this property.

The all-time Nf integral also updates locally. On the union of old U_p events and new p times, maintain the baseline local state x and that flip flag delta. Integrate Delta_p Nf(x) whenever delta=1, zero otherwise. This exactly gives the new-minus-old integral; distant events do not change its integrand. The prototype uses a sorted local union O((K_U+N_p_new)log(K_U+N_p_new)); a merge iterator can reduce this without changing the formula. Total physical event count changes by N_p_new-N_p_old. These are mathematical update identities, not a implemented complete12-observable production cache.

Reconstructing an arbitrary full configuration from edge prefixes costs O(E logN) in the reference representation. Serializing the entire path or performing a global audit costs O(N) or more. Persistent delta checkpoints can amortize this, but need reviewed replay/compaction and retention policies; keeping every historical root forever grows memory. No claim is made that arbitrary measurements, startup, checkpoint compaction, full output, or independent validation is local for free.

## Deterministic controls

185 explicit predicates passed in0.041831s,19.296875MiB. A legal L4 path with3 relevant events is expanded by20 strict-distant events; the local query still visits exactly the same relevant records while all23 global events remain stored. Local normalized transfer matrices agree with complete original conditional products before and after expansion. An actual overlapping pair exhibits gated noncommutativity.

Six deterministic supplied-tape outputs from the existing full conditional are spliced through the index. Every reconstructed physical trajectory, seed witness, all-edge prefix query, AVL count/balance invariant, fixed-time Nf difference and local integral-Nf change agrees with a literal full replay. Old persistent roots remain unchanged. A new event at an ignored distant time fails through the global collision check, and a near gated incompatibility fails local validation; both failures are atomic.

These are source/data-structure controls only. They do not validate an efficient indexed bridge generator, future observable cache code, a runtime forecast, stationarity, equilibration, a ground-state limit or a phase. The reference full conditional is used in the fixtures to generate deterministic proposals, not claimed to have already acquired the local complexity of this design.
