# Energy-bin result independent scalar review

**PASS.** Independently authored standard-library Fraction reconstruction checks all 686 saved occupation bins, all 14 reported summary groups and every interval/error field (5,366 explicit predicates). It imports no author arithmetic. Exact root brackets, energy denominators, reciprocal bounds, quadratic error, and outward rounding were reconstructed; all fields agree exactly. Particle-bin sums reproduce the accepted chi certificate's exact unrounded particle intervals, including all-ge3. This checks scalar reduction of the saved bins, not a second raw-vector scan.

The higher-particle singleton susceptibility is certified within approximately [0.0001427327701821816, 0.00014273277099632474]; the one-particle interval is [8.599715889441283, 8.599715889780029]. These are energy-weighted quantities, distinct from the previously accepted particle weights. The finite-L6 singleton contribution does not determine the full sixth-order coefficient.

All 1,888 source/runtime pins, accepted production/completion/replay/acceptance bindings, input digest, and final result digest agree. Root acceptance matches the actual external shell: 1.71 seconds, 34,979,840-byte root RSS and 69,435,392-byte sampled tree peak, within 30 seconds/384 MiB. Coverage is 1,048,576 entries. Reuse the earlier primary mathematical source review 12281695 and our wrapper review d79f4a83 explicitly; no physical scan, inverse or vector action was rerun here. Runtime/FP and supplied-model assumptions of the accepted chi certificate remain.

RESULT.json records concise values; READ_HASHES.json pins read inputs and standalone replay.py. No retuning or data replacement occurred.
