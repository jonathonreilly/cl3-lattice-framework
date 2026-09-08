# Sixth-order sign obstruction inside the coordinate-seed component

This is a constructive refinement of the existing full-carrier H6 sign witness. It does not use flux equality as a proxy for connectedness. The actual L6 coordinate seed has edge bit n_(r,a)=r_a mod2, with edges ordered by lexicographic vertex then positive axis, exactly the declared seed convention. Faces are ordered by axis pair (xy,xz,yz), then root vertex.

## Legal preparation and loop

Starting at that seed, perform face6 then face258. Their edge lists are

[18,127,36,19], [126,236,129,128].

Both flips are explicitly alternating and preserve degree three. This reaches the first loop state. From there perform faces6,438,222 with edge lists

[18,127,36,19], [19,38,22,20], [18,128,21,20].

Every intermediate is ice. Their combined toggle is the simple six-cycle [21,128,127,36,38,22]; toggling it closes exactly to the first loop state. The active cube root is(0,1,0); all coordinates of the local moves lie strictly within the periodic cell, with no seam or winding contribution.

RESULT.json stores the complete648-bit coordinate seed and all four648-bit loop states, preparation face/edge tape, loop face lists and closing cycle. The checker independently verifies the preparation endpoint, all full vertex degrees and actual native endpoints. The native sequential-product phases are(−1,−1,+1,+1). Including three positive fourth coefficients and the negative sixth coefficient gives effective signs(−1,−1,+1,−1), with closed product−1.

Hence the same diagonal-phase obstruction already proved for the H6 coefficient occurs in the actual plaquette-connected component containing this numerical coordinate seed. This is a literal finite path certificate; it assumes neither global plaquette ergodicity nor equality of flux sectors with components. It makes no claim about how often an equilibrated simulation visits these particular states or the severity of a numerical sign problem.

## Search record and limits

All216 elementary cubes,8corners and6orders were tested at the zero-preparation seed and failed. All324 legal single preparatory flips were then tested, scanning every cube touching a changed edge. Other cubes retain their initial unsuccessful pattern, so this is complete for the specified one-flip preparation/cube-loop template. That stage failed and its exact original source and failure are preserved.

The prospectively permitted two-flip stage scanned legal pairs in deterministic face order; the127th pair examined succeeded. It only needs cubes touching the second flip because every other cube is unchanged from an exhaustively unsuccessful single-flip state. Total attempted corner/order tuples226421; no RNG, sampling, discarded production or timeout retuning. This is not a theorem that two flips are minimal among every conceivable route or sign witness, only the successful route and the bounded template failures stated above.

Sixteen aggregate explicit predicates passed in0.241s at16.5MiB. The search loop also contains concrete conditional legality checks, but those are not inflated into the predicate total. Full H6 coefficients and analytic sign-persistence window remain separate reviewed prerequisites. Canonical H6 source c265 and all previous witness bytes are unchanged.
