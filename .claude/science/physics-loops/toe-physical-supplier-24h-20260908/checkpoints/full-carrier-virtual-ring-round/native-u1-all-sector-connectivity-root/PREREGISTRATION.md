# All-sector connectivity proof stretch

Root candidate: graph of all low-charge bit configurations on an even cubic torus (extent>=4), edges given by nonzero single native A edge moves, including pair creation/annihilation. Prove every configuration connects to an ice state by reducing D, then connect ice states by directed-cycle reversal using an ephemeral pair. No sign-free, ground uniqueness or physical occurrence claim.

Start from orientation with outdegree3+Q. Seek a directed path from positive to negative; use last positive and first following negative to make interior neutral. Every cut containing positive but no reachable negative would have positive net divergence and no outgoing edge, a contradiction. Along path move positive through neutral vertices then annihilate adjacent opposite charges. This reduces D by2. For two ice states, directed difference cycles can be reversed by creating one pair at an edge and moving along the rest of the directed cycle to annihilation.

Controls, if needed: deterministic fullL4 configurations containing several charges, implement actual edgebit/degree dynamics and signed native Pauli amplitudes. No exhaustiveclaim from finite fixtures; analytical proof supplies universal quantifiers. Any bound must count actual graph path/cycle lengths. No stochastic production. Target≤180s384MiB.
