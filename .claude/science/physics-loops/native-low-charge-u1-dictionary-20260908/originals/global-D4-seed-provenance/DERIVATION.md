# A globally supported same-sign exchange loop on the actual cubic carrier

This finite witness discharges the global low-charge extendibility qualification for the local three-hop example in PR8038, head86e03ef9a8eaafb9106304bf54cc0a991c758001. It does not assert that every locally admissible boundary template extends, and it does not supply a deconfined particle or continuum-statistics interpretation.

Use the actual periodic4x4x4 graph with64 lexicographically ordered vertices and192 sorted undirected edges. Each native neighbor order is ascending. The source helper was read completely; its local exterior vertices are replaced here by the full periodic degree constraints. The common-carrier low-charge hypothesis retains relaxed cycle constraints.

Choose i=(0,0,0), j=(1,0,0), k=(0,1,0), l=(0,0,1). Put Qj=Ql=+1 and Q=-1 at(2,2,0),(2,0,2), zero elsewhere. Since epsilon is odd atj,l and even at the compensating charges, all four defects require degree2; every other vertex requires degree3. Fix n_ij=0,n_ik=1,n_il=0. The bipartite integral flow network assigns remaining edge occupations: source capacities are the residual even-vertex degree demands, every free even-to-odd edge has capacity1, and odd-vertex-to-sink capacities are their residual demands. The exact flow93 saturates every demand. The resulting bitstring is then checked directly, independently of trusting the solver's degree feasibility conclusion.

RESULT.json contains the full vertex/edge dictionary,192-bit initial configuration and every intermediate192-bit state and64-entry charge vector. Bitstrings are conventional binary strings with edge0 at the RIGHT; the edge list fixes the interpretation. The first signed witness has positive charges at vertex IDs16 and1 and negative charges at40 and34. Complementing all192bits negates every Q, giving the opposite-signed active template without a second optimization.

For both signs, the routes

 A: i<-j, k<-i, i<-l,
 B: i<-l, k<-i, i<-j

are nonzero at every step, stay globally in |Gv|<=1, and retain exactly two positive and two negative charges. Both finish in the identical full link configuration, not merely the same charge vector. Each directed hop is computed literally from the source native Pauli dictionary: the endpoint Z strings give A_ab's sign, the antisymmetric orientation supplies A_ba=-A_ab, and the neutral-target/charged-source parity factor gives T_ab=-i A_ab. All amplitudes have modulus1. The exact route phases are -i and+i. Following A and then the reverse ofB therefore closes a six-hop path with product phase-1.

A diagonal change of basis multiplies each edge amplitude by an endpoint phase ratio; these ratios cancel around a closed path. The product-1 therefore excludes a diagonal rephasing making every hopping edge nonnegative real on the containing configuration component. It also excludes making every edge negative real, since a six-edge product of negative entries is positive. This is a narrow phase-frustration statement for this actual connected subgraph. It does not exclude a general non-diagonal unitary, extra resources or another state domain. It explains why the ordered one-positive/one-negative-hole frame used in the D2 variational theorem does not extend automatically to this D4 sector with identical signed charges.

The maxflow is a construction aid, while the delivered bitstrings, charges and native phase tapes are a directly checkable finite witness.102 explicit guards pass under -O in0.0047s18.46MiB. The full global Hilbert space is not enumerated. No physical exchange protocol or preparation is claimed, and no branch/source/GitHub mutation was performed.
