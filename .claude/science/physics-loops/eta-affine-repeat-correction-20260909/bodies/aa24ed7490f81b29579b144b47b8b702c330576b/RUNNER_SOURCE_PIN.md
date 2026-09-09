# Block 35 runner source pin

source_sha256: `a6a0c0c297d090bec925d9895568083bbf159e4713e8a33e9b19f261c37bdb08`
theorem_sha256: `ba5d5f026ffd5ef882c7eef401d3c5aac9db7cb60f89efa79132bd6e06ee71f7`
no_go_sidecar_sha256: `c1aaa0c54ea0ecfa2d207ca8afa499b90201810017cd2ab2bc26b5a1841c06d0`
postexecution_state_sha256: `4ddabf05fd542593148de6fd79091af4614e80a1f802f0667a2da763db81f4f9`
toe_update_sha256: `155961ed6d1e9de78c37f30c6cefe6e686994ab93b42bab81b0fca77d94a8c22`
independent_attack_sha256: `5bea9c0c042295cf1f6afaf255a19c877afd4d382da569706f5becd959dcf57f`
canonical_cache_sha256: `0b3110720e0c98582b1be2bb8f2516519007a1f06ce751495554c73ac95e9979`
canonical_cache: `logs/runner-cache/admissibility_opus_affine_born_public_evidence_gate_2026_09_01.txt`
state: `final_packet_content_pinned_reproduced`

The cache envelope directly pins the final runner source. The runner in turn
fails closed over seven exact content identities: two canonical authority
objects, the public PR evidence blob, two canonical predecessor objects, and
the result-state and TOE-disposition files. Fourteen one-character digest
mutants and all twenty-one computed science/scope/governance promotions are
rejected. The AST control finds no literal Boolean verdict in the mutation
dictionary.

This manual packet pin deliberately avoids making the runner depend on this
file or on its own digest. Any change to a hash-named artifact requires a fresh
execution, cache, independent attack, and source pin.
