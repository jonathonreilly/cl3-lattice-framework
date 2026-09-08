# Leaving winding checks unfixed does not repair literal same-edge ice

## Scope

Retain the previous same-edge hypotheses on periodic even cubic L>=4, but fix only the canonical contractible elementary-plaquette native BKSF cycle checks, leaving all noncontractible winding-cycle eigenvalues free. Use a consistent local-check sector (the usual native signs suffice). Ice is literally degree3 of edge occupation(1−Z)/2. This is a conditional algebraic compatibility test, not a universal physical no-go or a claim that either model is axiom-selected.

The source native cycle operators are monomial Paulis: their X support toggles exactly the cycle edges. Their phases do not change coefficient moduli. Local plaquette generators span binary contractible cycles; the remaining three independent homology classes are the usual coordinate windings of the cubic3-torus. Equivalently the cellular chain complex of three periodic circles has H1(F2)=F2³. Elementary plaquette deformations exchange successive coordinate steps and cancel reversals, reducing a closed chain to its three winding representatives. Thus local-cycle rank isE−V+1−3=E−V−2. This topological fact is used explicitly; finite checks corroborate it rather than proving it for allL.

## A stronger elementary zero-intersection argument

At ANY ice configuration and ANY vertex, its three outgoing edge bits include an equal pair by the binary pigeonhole principle. Choose the elementary plaquette in those two coordinate directions rooted at that vertex. It toggles both equal outgoing bits there; degree3 changes to1 or5. Hence its toggled partner lies outside ice, regardless of what happens at the other three vertices.

A vector fixed by that local plaquette Pauli has coefficients related by a nonzero phase on the paired basis configurations. If it were supported entirely on ice, its coefficient on the original configuration would have to vanish. Apply this argument to each possible ice basis configuration, choosing its equal outgoing pair. Every coefficient vanishes. Therefore the local-check subspace has zero intersection with ice already; no fixed winding sector, full-cycle transitivity, seed-specific empty face or ergodicity assumption is required. The argument concerns arbitrary superpositions and does not treat a cycle toggle as a legal ice dynamics move.

## Same quantitative overlap bound

Ice imposes allB_v=−1. Within this incidence fiber, local plaquette toggles partition the Z strings into eight affine winding classes. On each class, the fixed local-cycle eigenvector is unique up to normalization and has uniform coefficient modulus. Different winding classes have disjoint computational support. A consistent canonical local-check group has no additional nontrivial diagonal stabilizer on this fiber; it is the restriction of the native cycle-space stabilizer representation, whose cycle X supports label the group faithfully. Consequently coherent combinations of winding sectors cannot interfere on a diagonal ice projection.

Take k=V/8 selected all-even vertices and their disjoint six-edge stars. G\S remains connected as proved in the previous overlap review. It also contains three coordinate-winding cycles avoiding every removed star: for direction a, fix another coordinate at1 and run all the way around direction a. Their seam-cut parity vectors are the three standard basis vectors.

Assign any of32odd six-bit patterns to each selected star. Incidence completion on G\S has constant multiplicity2^(E−V−5k+1), by the residual even-parity condition and connected incidence rank. The three surviving winding cycles change winding independently without altering assigned stars or vertex parity. Thus completions divide equally among all eight global winding sectors: each has2^(E−V−5k−2) completions. Conditional on ANY winding sector, the selected star patterns are therefore still independent uniform odd patterns. Degree3 accepts20/32=5/8 at each star.

Let P_local denote the local-cycle projector. Since Pice selects only allBminus, and the winding components are computationally disjoint,

 ||Pice P_local||² = max_w probability(ice | all-odd incidence,winding w)
                   <= (5/8)^(V/8).

This is the same bound as for the fully fixed native code; freeing topological labels does not help this literal identification. For arbitrary state in the partial code, the projected norm is a convex combination of the winding-sector probabilities. No coherent cancellation produces a better overlap.

## Bounded controls and limitations

check.py independently builds all cubic edges, plaquette binary vectors and seam cuts at L4,6,8. It verifies local ranks126,430,1022 versus full cycle ranks129,433,1025; disjoint selected stars; residual connectivity; and three explicit residual winding loops. Completion exponents per star assignment per sector are86,295,702. Runtime below.1second,16.3MiB; no Hilbert-space matrices or large-state enumeration.

Finite boundaries or deleted edges can remove the three outgoing directions, required plaquette checks or the residual-graph hypotheses. Trees have no cycle checks. Different operator dictionaries/extra carriers are separate escape routes. The conclusion does not automatically transfer to those domains. Leaving only winding checks unfixed on this undeleted torus is the specific escape ruled out here.
