# Independent review: exact local Record relay cost

2026-09-07. Root proposed the Steiner-cost route before this independent derivation. This is a conditional classical process theorem and an exact small check, not a derivation of primitive Admissibility or a native quantum implementation. Main source read at47da12268436ee1843e822386477aa2c829d95a9: `docs/NATIVE_EDGE_RECORD_MATTER_INSTRUMENT_AND_ENERGY_LEDGER_BOUNDED_THEOREM_NOTE_2026-09-05.md`, carrier paragraph and Theorem2.

## Exact domain and theorem

Let T be a nonempty finite set of physical Z3 sites. Choose a finite event set V containing T, all initially blank, and a deterministic order listing each site of V once. No other sites form Records. At event i the site x_i permanently records a binary value Z_i. The LOAD-BEARING Markov contract is the full-history identity

    Pr(Z_i=z | Z_1,...,Z_(i-1)) = k_i(z | (Z_j : j<i, x_j adjacent x_i)).

The kernels are normalized on every reachable history. There is no additional shared seed, unrecorded interacting state, future conditioning, postselection, or outcome-dependent order. It is insufficient merely to specify the marginal conditional probability given neighboring Records while allowing residual correlations with the rest of the past. Independent local sampling is one realization of the displayed full-history contract.

The target marginal is exactly 1/2 on all-plus and 1/2 on all-minus, with zero mass elsewhere. Minimize the number |V\T| over finite event sets and permitted fixed orders/kernels. Then its minimum equals

    s(T) = min{|S\T| : finite S contains T and its induced nearest-neighbor graph is connected}.

This equality concerns the full target probability law only. Auxiliary Records are additional readable output; the whole transcript is not the original native target-only instrument or its coherent postmeasurement channel.

### Lower bound

The chain rule writes the joint law as the product of the displayed kernels. Each factor refers only to earlier vertices in its own connected component of the induced graph on V. Grouping factors by components gives a product of normalized component laws; interleaving component events in the fixed order changes nothing. Thus target variables belonging to distinct components are independent. Two independent fair signs have joint-plus probability1/4, whereas the required common-bit law gives1/2. Therefore all targets lie in a single component S. That component is a connected set containing T and |V\T| >= |S\T| >= s(T). Other components cannot improve the cost.

This is stronger than an informal causal-cone argument because it specifies the exact factorization assumption. Arbitrary initial shared randomness or hidden quantum correlations are excluded by that assumption, not disproved by this theorem.

### Upper bound with one rule

Choose a minimizing connected S and a rooted spanning tree. Order vertices so each nonroot has an earlier tree parent. Use the SAME translation- and proper-cubic-covariant rule everywhere: with no previously recorded nearest neighbors draw a fair sign; otherwise choose plus with probability the fraction of previously recorded neighbors equal to plus. This also defines a normalized rule on mixed-sign neighborhoods.

The root draws one fair bit. Inductively all previously formed Records have that bit; every next site has at least its parent recorded and all its recorded neighbors agree, so it copies the bit deterministically. Hence all S Records, and in particular all targets, have the exact required law. The rule genuinely varies with neighboring conditions. Formation order and initially blank roles remain supplied; covariance of the kernel does not make a chosen finite rooted schedule a covariant autonomous process.

The upper bound needs the initially blank background, or a separately declared way to mask old fixed Records. With an arbitrary fixed pre-existing plus neighbor, the unmodified rule can turn the first draw deterministic. Lower factorization still holds for deterministic background, but the stated upper construction cannot be silently reused there.

## Actual native square target

The source places virtual vertices at2v and physical edge qubits at2v+e_a. Thus the square's edge sites are

    T={(1,0,0),(2,1,0),(1,2,0),(0,1,0)}.

They are pairwise nonadjacent physical sites, despite sharing virtual graph vertices. In the encoded Fock vacuum every vertex parity B_v is+1. On this cycle B_v is the product of the two incident edge Z operators, so the joint Z law is supported on all-plus/all-minus. The first edge is a nonbridge, and Theorem2 gives its two signs probability1/2. Commuting edge-Z measurements with no incoming dwell therefore give precisely the common fair-bit target law. This uses the supplied code, vacuum, physical placement and Born/Lueders instrument. It does not identify that instrument with the primitive nearest-neighbor law.

No auxiliaries leaves four separate event components, so zero is impossible under the classical local-kernel contract. The center c=(1,1,0) is adjacent to all four targets, so s(T)=1. One center Record first, followed by any target order, suffices. Equally one target first, then center, then the remaining targets suffices; this preserves any prescribed relative target order if auxiliary insertion is allowed.

An arbitrary prescribed FULL order need not attain this minimum: if center is last, all four target draws have already occurred independently. The minimization over orders is essential. For two targets at lattice distance L, every connected containing set has at least L+1 vertices, and a shortest path attains that number. The auxiliary cost is exactly L-1.

## Independent finite controls and adverse cases

The prospective finite-check contract was written before execution, after the analytical route had been discussed. `check.py` uses exact Fraction arithmetic and preserves every complete four-target distribution in `result.json`:

-15 named assertions passed.
-All24 no-relay orders give the uniform16-string product distribution, at TV distance7/8 from the target common-bit law.
-All120 one-center orders were evaluated; exactly48 give the target law. These are center-first and first-target-then-center orders. The72 failed orders are retained, not discarded.
-Distances1..6 on a straight path reproduce the two-target law with L-1 intermediates.
-A shared-seed zero-relay construction reproduces the target law but violates component factorization. This pins the hidden-randomness exclusion.
-A fixed old plus Record at(1,1,1) biases the center-first copy rule to all-plus. This pins the blank-background condition.

The checks do not prove the native code theorem, all-size Steiner theorem, or a physical law selector; those are respectively an explicit source import, the argument above, and an unclosed bridge.

## Prior coverage and actual value

The bounded read/search covered the main native source, complete PR6358/7047 notes previously downloaded at their verified live heads, and keyword searches across main Record/formation notes for Steiner/relay/common-bit/shared-bit/component phrases. No exact vertex-Steiner overhead statement was found in that scope. This is not a complete literature or open-PR novelty claim. The lower proof is elementary graphical-model component factorization, and the upper proof is ordinary copying along a tree; neither should be marketed as new general probability theory.

PR6358 already gives a Record-generated controller/root/metadata positive law and a same-current-map prepared-input obstruction. PR7047 already separates physical marginal identification from diagonal Record coupling and global process resources. The present possible increment is the exact physical midpoint geometry and one auxiliary-site price for this specific native target law. It supplies a local classical emulator after changing the readable transcript; it does not derive the actual formation process or retire its physical identification. If the campaign needs import retirement rather than a conditional implementation cost, the next missing premise is why this auxiliary registration and schedule are the framework's actual native process, not merely an available construction.
