# Separate isotropic result: exact fifth-order mixing

The preregistered exact center-flux enumeration tested973017 signed subsets of the22actual action faces through size5. There are no successful subsets at sizes0,1,2,3,4 and exactly one at size5: the five spatial cap faces on the INPUT slice, with their consistent oriented signs. Runtime0.267seconds,28.985MiB. Raw graph,24link incidence vectors, all counts and the unique signed solution are retained in isotropic_center_selection.json. This is necessary center selection, not a claim that any flux-balanced graph automatically has nonzero Haar integral.

Why repeated factors are covered: a degree n monomial of the Wilson exponential is a product of n fundamental or antifundamental plaquette traces. For each face reduce its signed count modulo3 to0,±1. The number of nonzero residues is at most n. Independent center multiplication of each of the24Haar links forces the resulting signed face incidence to cancel the input source loop modulo3. Therefore no degree below5 survives. At degree5 every surviving residue support must have size5, forcing exactly one trace factor on each of those five faces. There are no repeated insertions, neutral pairs, triple insertions or temporal insertions at that degree.

The unique cap is evaluated by actual Schur disk gluing, rather than by its center condition. Its four1/3gluing factors give1/81. Every spatial halfweight contributes b/12. The other slice contributes its constant term. Hence, with s=t=b in the exact frozen source operator,

<χ0,D_(b,b)χ3> = b^5/(12^5·81) + O(b^6).

The finite compact-group integral is entire in b, so this strictly positive leading coefficient proves nonzero mixing for all sufficiently small positive ISOTROPIC b. This result is distinct from the previously frozen anisotropic proof and does not establish anything at beta6.

An optional explicit derived positive point requires no fitted remainder. Write the two-slice integrand as χ3(Winput)exp[b A(U,V)]. There are ten spatial halfweights and twelve temporal weights, so |A|≤5+12=17 and |χ3|≤3. Its degree≥6 Taylor remainder is bounded by

3 e^(17b)(17b)^6/6!.

At b=10^-14, e^(17b)<2, so remainder≤17^6 b^6/120. This is strictly smaller than b^5/(12^5·81), as verified by an exact rational comparison. Thus a fully positive isotropic parameter exists explicitly, with the extreme small value disclosed. The parameter is a derived corollary, not part of the original pre-computation fixture.

This refutes character diagonality for the specified actual cube-slab Wilson/Haar compression and source map even at isotropic coupling. It does not identify a dressed-environment source map or claim the historical multi-link physical target has supplied this exact map. The graph geometry was already known in the distinct-shell exact-core note; the new ingredient is the actual two-slice off-diagonal, including the24link SU3 center rule and its coefficient.
