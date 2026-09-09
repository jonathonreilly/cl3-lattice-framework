# Exact target contract

| field | contract |
|---|---|
| Target statement | Decide whether the assumptions stated in PR #7814's landed summary, when read with the current minimal axioms, entail an affine pure-qubit nearest-neighbor kernel; if not, exhibit an exact countermodel and identify a sufficient missing property. |
| Quantifiers/domain | Bloch vectors `n,m in S^2`; fixed nearest-neighbor rules on triangle-free bipartite lattice graphs and the actual `Z^3` local conditional specification; all real nonzero nonlinear-kernel parameters in the declared safe domain. |
| Allowed premises | Current `minimal_axioms` source; elementary probability normalization; exact finite graph factorization; simultaneous `SO(3)` invariance; public PR #7814 summary only as conditional prior art. |
| Forbidden weakenings | No hidden archive premise; no old Record additivity; no identification of event additivity with preparation affinity; no identification of Block 34 lambda with PR #7814 lambda; no use of a numeric fit as a selector. |
| Required edge cases | Constant kernel; strict-positive versus endpoint-zero kernels; arbitrary common kernel scaling; `lambda -> -lambda` on bipartite graphs; pure versus mixed-state wording; finite and local-`Z^3` scope. |
| Completion witness | Exact nonlinear counterkernel or proof excluding it; exact affinity-to-affine representation lemma; exact Born/anti-Born stagger map; source-pinned public evidence census; independently recomputed displayed gravity arithmetic. |
| Outcomes not counting as closure | Equal partition functions alone; opposite correlation alone; arithmetic agreement with displayed formulas; absence of the archive; a finite Monte Carlo match; a proposed axiom clause not adopted or audited. |

The neutral outcomes are: `AFFINE_FORCED_PUBLICLY`,
`PUBLIC_ASSUMPTIONS_ALLOW_NONLINEAR`, or `UNDECIDABLE_WITHOUT_FORMAL_RECORD_CONSISTENCY`.
The last two may coexist: a countermodel can refute the ordinary reading while
an unspecified stronger archive definition remains unavailable.
