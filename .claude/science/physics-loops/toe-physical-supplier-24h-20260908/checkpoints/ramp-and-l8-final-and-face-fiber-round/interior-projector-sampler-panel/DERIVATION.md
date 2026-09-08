# Exact finite-projector interior alternatives

This independent derivation follows the frozen preregistration and precedes reading root's bridge derivation. No new numerical production, micro, or performance result is claimed. The completed .95 L8 study and its failed memory diagnostics remain immutable; the V0 memory pilot is held unlaunched.

## Target and assumptions

On one finite connected component of the actual legal plaquette-flip graph, let N(x) be flippable-face count, M the geometric face count, and H=V N-A, with 0<=V<1. Count geometric labels with multiplicity in A. Then G=I-H/M is symmetric, nonnegative, and Gxx=1-V N(x)/M>0. Uniform trial endpoints give the exact discrete path law pi(x_0,...,x_n)=Z^-1 product_i G(x_i,x_{i+1}). This is not the continuous-time projector at finite M,n. The even-n midpoint law is proportional to (G^(n/2)1)^2. All proposed states remain in the declared component, hence preserve its Gauss and winding constraints. This is not a sampler of all components.

## Single-slice Gibbs baseline and its obstruction

For interior neighbors a,c, the conditional is G(a,z)G(z,c)/(G^2)(a,c). Endpoint conditionals are G(z,c)/b(c), b(c)=sum_z G(c,z). Random scan with state-independent positive scan probabilities is reversible. Each update is the literal conditional; multiplying pi by its transition probability makes the old and new conditional factors symmetric.

With free endpoints and positive self weights the support is connected: update slices 0 through n-1 successively to the old next slice. At each update the new left neighbor is the old current slice and the right neighbor is the candidate itself, so both bonds are allowed. Repetition collapses any path to its last constant state. A constant state x can be changed to a neighboring constant y by changing the right endpoint and copying y right-to-left. Connectivity of the configuration component completes the proof. Every no-change update has positive probability, giving aperiodicity. This proves no useful mixing bound. Fixed-endpoint-only updates are not covered.

On an L>=4 constant triple a,a,a, distinct flippable faces have distinct endpoints. The probability of leaving a in this single-slice heatbath is

    N(a) / [M^2 (1-V N(a)/M)^2 + N(a)].

At V=0 it is N/(M^2+N), at most 1/(M+1). At fixed V<1 it is O(1/M). Thus acceptance-one heatbath does not imply effective physical updates. At L2 use aggregated multiplicities squared instead; replacing them by label count is wrong. Imaginary-time diffusion is an additional possible cost, not a proved rate here. Erasing provenance tags by interior overwrites cannot itself certify decorrelation.

## Recommended finite-G candidate: whole-time single-face orbit Gibbs

Choose a geometric face p with a state-independent positive probability. On legal configurations define an involution F_p: flip p when flippable, otherwise fix the configuration. Flipping a flippable face leaves it flippable and reverses the move, so this is indeed an involution. At time i form the distinct-state orbit O_i={x_i,F_p x_i}; it has size one or two. Do NOT retain two copies of a fixed state.

Condition on these time-indexed orbits. For s in O_i,t in O_(i+1), set T_i(s,t)=G(s,t). Sum and sample the resulting inhomogeneous binary chain by forward/backward messages. For example h_n(s)=1, h_i(s)=sum_t T_i(s,t)h_(i+1)(t). Draw x_0 with weight h_0, then x_(i+1) with weight T_i(x_i,t)h_(i+1)(t). Arbitrary positive rescaling of each message prevents overflow and cancels from conditionals. The old path has positive weight, so the conditional normalization is nonzero. Zero-weight alternatives must remain excluded.

Every output y has exactly the same orbit O_i because F_p is an involution. Therefore this construction is a true partition of path space, not a state-dependent proposal set requiring an omitted Metropolis correction. The product-G conditional is sampled exactly in ideal arithmetic. Each face-block heatbath is reversible; their state-independent mixture is reversible and has pi stationary.

The block has positive probability to realize any allowed modification at a single slice by face p while leaving other slices unchanged. Every copy move used in the preceding connectivity proof either changes nothing or is one legal geometric-face flip. Hence the face-block mixture is irreducible on the same free-endpoint path support, and its positive no-change probability gives aperiodicity. This remains a finite support result, not polynomial mixing. It does not require sign-free native microscopic A operators: it applies to the explicitly supplied positive ice G, with its declared sign convention.

The block can insert, delete, and move arbitrarily separated pairs of p flips in one exact conditional draw. Consequently it is not constrained to the single-slice pair-insertion probability above. That is an algorithmic mechanism, not a measured improvement or a general lower bound on useful-change probability. Other-face vertices can pin the column; collective spatial rearrangements and flux limitations remain.

Each block uses at most four local G entries per bond and O(n) messages, plus output state updates. G includes the actual aggregated self and actual geometric multiplicity. A valid implementation must distinguish equality, legal single-face difference, and zero entries; it must not infer G merely from the old stored label. If output labels are retained, resample an allowed label conditional on the new endpoints using its g_label/G weight. Self has the one aggregated label. State-only paths suffice for the mathematical target.

Cost is O(n) local tests only after proving constant-size affected-face and state-difference logic. A naive full-state comparison or N recount adds volume factors. A full packed L8 tau36 path occupies about 21.2 MB for 1536 bits times 110593 slices, before messages and caches; uint8 storage is about 170 MB. This is a design calculation, not a measured RSS result. The old three-configuration ring cannot support arbitrary interior access without reconstruction or extra storage. A practical implementation must include packing, checkpoint, cache rebuild and measurement cost. Choosing one face uniformly does not mean one block is a full spatial sweep; M blocks is the corresponding nominal sweep.

## Continuous-time alternative, separately typed

Let L=A-N be the actual continuous-time RK generator (rate one for every legal geometric face). H=-L-(1-V)N. Feynman-Kac gives exp(-tH) as the RK trajectory measure tilted by exp[(1-V)integral N ds]. Relative to ordered jump times and face labels, the unnormalized trajectory density is exp[-V integral N ds] times the product of unit jump rates. At V=0 the holding exponential disappears, but ordered-time volume, endpoints and event-count measure do not. This can motivate event/loop updates without artificial discrete self slots. It changes the target from finite G^n, so requires a new exact exp(-tH) L2 reference and explicit projector-time convention. No cubic-ice loop scattering rules have been established here.

Primary abstract-level source checks only: Syljuasen and Sandvik, https://arxiv.org/abs/cond-mat/0202316, formulate directed-loop detailed balance and demonstrate an XXZ spin model; Yan et al., https://arxiv.org/abs/1809.05792, describe constrained sweeping clusters with a quantum-dimer benchmark. These motivate a route, not an imported ready-made cubic-ice implementation. Full-paper implementation hypotheses were not reviewed in this bounded panel. No novelty claim is made for Gibbs or dynamic programming.

## Prospective gate before any sampling

Recommend the face-orbit block as the next deterministic implementation target because it retains the existing finite-G oracle and changes path interiors nonlocally in time. First independently enumerate small nonconstant-row path examples, verify exact partition-class normalization and detailed balance, and kill a duplicated-singleton-orbit mutant. Then use the actual 864-state L2 component: compute all local G entries with multiplicities, compare dynamic-programming marginals to explicit restricted-path sums on short n, and verify old/new full path weights. Include a fixed-endpoint exclusion control and a floating-message underflow/zero-normalizer guard. General-L bit/cache logic needs independent literal tests before a cost micro. No production is authorized by this recommendation. Mixing and finite projection must be tested separately; lower tag survival is not a substitute for physical autocorrelation and independent-chain uncertainty.
