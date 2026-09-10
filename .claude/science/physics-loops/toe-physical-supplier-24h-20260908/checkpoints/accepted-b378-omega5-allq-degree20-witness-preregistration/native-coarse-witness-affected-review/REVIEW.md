# Affected witness root timing review

PASS. Root897b606e7201945dfe87877d0ac40dafe0d445d676e041856d7a9302e9bb0ac5 binds unchanged worker30c200e9. Compared with preserved a7f977ca, the sole schema-code change adds worker.seconds<299 while preserving result<=worker<=root<299.5. The monitor bytes are unchanged. Literal numeric finite positive timing checks exclude booleans and non-finite values; worker RSS remains a literal positive integer under384MiB. Root file pins were checked.

One affected-only synthetic adversary copied the parent’s fabricated205-event fixture and assigned worker299.1/root299.2. It now rejects specifically at time ordering. Unchanged parent fixture tests were not rerun. Actual strict root CLI source-only readiness passed with zero accepted loads and zero witness certificates.

This confirmation inherits parent full binder/factoring/49-entry gate review and the earlier independent Gamma/factorization proof. It is not an independent replay of adapter contractions or a scientific result. No native T, IDs, B values or geometry was parsed. Execution remains disabled until parent activation and separate preregistration.
