# Independent endpoint-residual result

All proposed identities are correct under the explicit real-symmetric finite-H, uniform endpoint trial and stationary finite-path hypotheses. The correction sign is plus. The bound sharpens to sqrt(Var_psi H Var_psi X)/<X>. G only needs entrywise nonnegativity for the path law, not positive-semidefinite spectrum. Proof SHA f0b6e01a4e9ef881f3455c19870804f588d782e3b80a7fa5c73b63d979effed9 is frozen with source/results in HASHES.json.

Nineteen checks pass: exact rational three-state four-bond path sums with a genuinely complex diagonal source; wrong midpoint-as-endpoint, wrong endpoint square and omitted covariance discrepancies; independently constructed literal864-state L2 graph with6912 directed face moves, all pooled source increments; and finite-G oracle checks at n2,48,192. No author module or stored energy target is imported. Final run records88.797MiB and0.091seconds after imports; the command had a180second alarm and completed in under one second. No stochastic samples were generated.

Tiny exact correction is10788/26460835, demonstrating that omission is not an identity. For actual L2,V=.95:

| n | D | covariance correction | source Rayleigh relative E_psi | sharper bound |
|---|---:|---:|---:|---:|
|2|1.610801192904|0.039512151074|1.650313343978|0.045672005483|
|48|1.660993329986|0.001748362046|1.662741692031|0.002441122825|
|192|1.664329088659|0.000002018155|1.664331106814|0.000003008895|

These are finite-oracle checks, not noise-free reinterpretations of current L4 production. The required statistics are the same-time midpoint X times endpoint-average h, the cross-endpoint h_left h_right and midpoint X². Existing separate batch means cannot reconstruct these products. No fields were added to the running production. Relative to E0 there remains an unknown additive E_psi-E0; energy variance alone is not a general certified ground-error bound, and no pole or supported-gap inference is made here.
