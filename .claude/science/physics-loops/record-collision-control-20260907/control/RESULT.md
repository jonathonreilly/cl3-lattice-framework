# Frozen control-family result

Both attempts end in scoped obstructions. The first is the workspace/Hamming obstruction in ENCODING_OBSTRUCTION.md. The separately preregistered supplement removes that projector constraint and still fails, now through an exact energy/control invariant.

Exact rational Pauli-dictionary row reduction returned:

| Family | Columns | Rank | Nullity | Fuel-noncommuting basis vectors |
|---|---:|---:|---:|---:|
| Complete graph, weight at most2 |352|258|94|4|
| Fixed NN path, weight at most2 |100|60|40|4|
| Complete graph, exactly weight2 |324|248|76|2|
| Fixed NN path, exactly weight2 |72|50|22|2|

Every returned basis vector has exactly zero commutators with K, old Z_r and N_head. Every vector also commutes exactly with Qactive=q(I+Y_x). Since nullspace bases span all permitted Hamiltonians, this establishes [H,Qactive]=0 for every allowed H. The same holds under commutators, real linear combinations, arbitrary time-dependent schedules and concatenated exponentials. Source Qactive=2 and target Qactive=0 are orthogonal invariant sectors. Consequently this particular accepted transition is unreachable under either allowed graph family, even though total source/target energy is the same5/2. No direct-matrix-element inference or exhaustive Lie closure is needed once this common invariant is established.

Fuel alone is not conserved: X_f(I-Y_x) passes all declared constraints through cancellation between its Pauli summands. Its individual X_f summand fails energy conservation. This actual control distinguishes the result from the erroneous ansatz requiring each Pauli word to commute separately. Old-Record X_r is rejected, identity/K commute, and all NN basis vectors satisfy the complete-graph equations. Full bases and exact rational coefficients appear in result.json. Runtime0.034861seconds,17.703125MiB, below frozen180second/180MiB limits; no dense ambient matrices were allocated.

The exact elimination uses real rational commutators [P,Q]/(2i), keyed by full Pauli words. Sparse echelon pivots and back substitution enumerate one basis vector per free column; each output basis is independently substituted into every original commutator equation. The raw source and output hashes accompany this memo. This is exact arithmetic rather than a tolerance-based nullspace claim.

The native reviewer independently supplied an analytic battery-charge argument after this execution: in the local Y_x energy eigenbasis, flipping the low battery bit cannot be resonant with the sole possible second site, while a high-bit flip paired with x or f would require a spectator-dependent coefficient on the third site. The latter is unavailable to two-site terms; the nonresonant spectator sector forces its amplitude to vanish. This is consistent with the computed Qactive invariant and is separate corroboration, not an input to the nullspace calculation.

Scope: reduced odd-sector carrier with explicit square boundary embedding, supplied tensor/energy/control typing, original fixed nine-qubit encoding and graph. This does not rule out additional ancillas, other encodings, genuinely higher-support interactions, externally work-driven controls, other energy functions or an axiomatic dynamics construction. It does not demonstrate a general nearest-neighbor impossibility. Nothing in this result changes the earlier finite-collision theorem or frozen transport observations.
