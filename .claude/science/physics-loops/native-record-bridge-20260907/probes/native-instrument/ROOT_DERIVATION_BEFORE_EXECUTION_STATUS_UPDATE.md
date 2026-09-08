# Fixed native vacuum histories and local Record communication

Status: exploratory conditional mathematics, no axiom derivation or audit verdict. Source read completely: main47da12268436ee1843e822386477aa2c829d95a9 native_edge_record_matter_instrument_and_energy_ledger note (2026-09-05). The prior proposed three-consecutive-physical-site witness had a placement error; the source places virtual vertices at2v and edge qubits at2v+e_a. Nothing here changes that source.

## Exact finite physical instrument

Take virtual cycle vertices0,1,2,3 at physical coordinates(0,0,0),(2,0,0),(2,2,0),(0,2,0), with physical edge qubits e0=(01),e1=(12),e2=(23),e3=(03) at(1,0,0),(2,1,0),(1,2,0),(0,1,0). All other sites are fixed unrecorded spectators. Their states do not interact in the supplied instrument. All target edge centers have mutual nearest-neighbor distance at least2; the six actual neighbors of every target are spectators.

With ascending vertex-neighbor orders, the actual generators are A01=X0, A12=Z0 X1, A23=Z1 X2 Z3, A03=Z0 X3, and A30=-A03. Thus the oriented cycle stabilizer S=A01 A12 A23 A30=-X0 Y1 X2 Y3. The B generators are Z0Z3,Z0Z1,Z1Z2,Z2Z3. Their joint +1 subspace is spanned by|0000>,|1111>; imposing S=+1 gives the unique encoded N=0 vacuum |Omega>=(|0000>+|1111>)/sqrt2. The initial code has dimension8; selecting this vacuum is a supplied preparation, not a framework vacuum theorem.

The stipulated ideal event is Q_e,z=(I+z Z_e)/2 with supplied Born probabilities and Lueders update. Every first edge sign is fair. Conditional on a first sign z at any other edge, each remaining edge has sign z with certainty. Full measurement in any fixed edge order has exactly two outcomes, all+ and all−, each probability1/2. Zero hopping/dwell is a supplied allowed case; N=0 is also annihilated by the stated hopping. No arbitrary preparation comparison or sign-dependent schedule is used.

For example record e2 first, then e0. The two histories after the first event differ at e2, physical distance2 from e0, while all six physical neighbor conditions of e0 remain the same fixed spectators. Its second-event probability nevertheless differs by1. This excludes identifying this whole declared event-history instrument with a kernel depending only on those unchanged six-site conditions. It does not refute the axioms: the intended condition semantics and admissible preparation domain, or the identification of this stipulated measurement with primitive formation, may differ. Prior6358 already has a generic current-Record sufficiency obstruction; the new test specializes one fixed actual encoded preparation and actual midpoint geometry. Prior7931 already discusses global recorded-edge conditioning; no general underdetermination novelty is claimed.

## Quantitative two-event comparator

A competitor with fixed outcome-independent two-event order, no changing unrecorded neighbor data and an actual history-conditional local kernel has product output law Ber(p) tensor Ber(q), even allowing different site odds. The target law D assigns1/2 each to++ and−−. Its total variation distance is

  TV(D,P_pq)=1-min(pq,1/2)-min((1-p)(1-q),1/2).

The minimum over[0,1]^2 is sqrt2−1. To prove it, maximize the two-min overlap. If pq>=1/2, overlap=1/2+(1-p)(1-q)<=3/2-2sqrt(pq)+pq<=2-sqrt2, using p+q>=2sqrt(pq) and monotonicity in pq on[1/2,1]. The symmetric argument covers(1-p)(1-q)>=1/2. In the remaining region both products are at most1/2. For fixed p the overlap1-p-q+2pq is affine in q, so its maximum on the allowed interval is at its boundary, either one of the previous product equalities or q=0/1 where overlap<=1/2. Equality occurs p=q=1/sqrt2 or its complemented pair. If the competitor must preserve the native first-event fair marginal p=1/2, every q instead gives TV=1/2. Conditional second-event worst-case error is at least1/2. These are exact statements for this competitor class, not bounds on arbitrary quantum dynamics or an unmodeled formation selector.

## Positive locality-cost target

Let T be a finite nonempty set of target sites of a locally finite connected graph, here Z3. Start with no Records and fixed unchanging unrecorded background. Choose a finite set S containing T and one fixed total event order on S, independent of outcomes. Each site forms once. Its conditional distribution given the entire earlier history is a binary kernel depending only on previously formed nearest-neighbor Record values (plus deterministic fixed data); hidden shared stochastic seeds, invisible quantum evolution and outcome-dependent scheduling are outside this class. The target joint law is the common fair bit: all target signs equal, with either sign having probability1/2.

Claim to independently check: minimizing over S, orders and such kernels, the minimum number of auxiliary Record sites is

  min{|S minus T| : T subset S and the induced nearest-neighbor graph on S is connected}.

This is a graph vertex-Steiner cardinality, not a newly selected physical law. A prescribed incompatible full event order is not included in this minimization.

Necessity: the chain-rule product of local history kernels factors across connected components of the induced event graph. Therefore different components have independent target marginals. Two nondegenerate fair target variables in different components cannot be equal almost surely. All targets must occupy one component; discard irrelevant components. Sufficiency: choose an optimal connected S and a rooted spanning tree. Order its vertices so every nonroot has an earlier tree parent. Use a single translation/rotation-covariant binary rule: no previously recorded neighbors gives a fair bit; otherwise choose a recorded-neighbor sign uniformly (equivalently p+ is the fraction of recorded neighbors with+). The root gives one fair bit and induction makes every subsequent sign equal to it. This constructive law, initial blank state and event order are supplied, not derived from the TOE. Deterministic existing background Records can spoil this particular upper-bound construction and are excluded.

For the actual four target edge centers above, zero auxiliaries leaves four isolated sites, while the center(1,1,0) is adjacent to all four. Thus the minimum is exactly1. First record any target, then the central mediator, then the remaining targets in any order. The four target joint probabilities reproduce the native vacuum Record law. This reproduces classical probabilities on this one preparation only; it is not a compiler preserving arbitrary native CAR states or an identification of Born probabilities with Admissibility.

For two targets separated by graph distanceL, the minimum is L−1. The lower bound follows from every connected S containing a path of at leastL edges; a shortest path attains it. Fixed separated target components require a real connected chain of permanent Records in this restricted process class. An already prepared shared latent bit or invisible interaction would change the class and invalidate that lower-bound argument.

## Review state

The general locality-cost conjecture was sent to a separate Astra-low worker for proof challenge and independent controls before substantial reuse. Their early scope corrections require optimization over chosen fixed orders and an initially blank background; both are incorporated here. This is not a blind derivation after that exchange. Literal Pauli and independent bit-code controls will be executed next; no numerical PASS is asserted in this draft.
