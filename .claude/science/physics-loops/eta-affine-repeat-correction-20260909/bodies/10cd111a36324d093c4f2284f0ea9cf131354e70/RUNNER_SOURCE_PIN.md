# Block 36 runner source pin

source_sha256: `d1b0bd04d565dd9d32c758cceb27ca69aa1f069fc7d2e7b4ddba6aded5e4940f`
theorem_sha256: `ac8e6b0902f742d6824deb5ebbae2a14b5b383f18a9a398317de031d03724a17`
postexecution_state_sha256: `6fef185078db3a86f5ae64797d419ecae3e1689be05405cb1144462c44d36fe7`
toe_update_sha256: `c6efd4ccdf2b72f2df140c79b264e2d7f697886ff979f8e4b70372b90c2d8e38`
independent_attack_sha256: `c0d25593d13847a91695afb8c732ec1510ec42545cd05074cf213cfae2bb3b8a`
canonical_cache_sha256: `b0e324ae007c4f282589078503bc88c936309ce5c26b149e20cebff64335e098`
canonical_cache: `logs/runner-cache/admissibility_gaussian_fair_record_affinity_haar_factor_fresh_port_reset_2026_09_01.txt`
no_go_gate: `integrated_in_theorem_section_11`
state: `final_packet_content_pinned_reproduced`

The cache envelope pins the final runner source and six declared-input
fingerprint. The runner then fails closed over 27 exact Git objects, the six
unchanged preregistered worktree inputs, 32 computed science/scope/governance
mutations, and an AST check requiring zero literal Boolean mutation verdicts.

This manual packet pin deliberately avoids making the runner depend on its own
digest or on postexecution prose. Any change to a hash-named artifact requires
a fresh execution, cache, independent attack, and source pin.
