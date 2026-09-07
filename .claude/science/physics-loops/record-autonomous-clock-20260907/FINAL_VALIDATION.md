# Shared current-main validation

Integrated full pipeline0497df333725 passes against current main a8f84aaad7, including all nine changed science claims in the stacked record apparatus unit. Separate strict lint passes. The nonempty pre-cleanup readiness capture has exactly9rows,0failures and0control failures. Source provenance includes PR8004 head5bd7f234bd and PR8005 headfb81c52351, whose scientific source/runners remain unchanged after current-main integration. Three new canonical clock/chain runners pass unchanged180-second/180-MiB limits; exact hashes are in CANONICAL_RUNNERS.json.

The first pipeline stopped at the graph-manifest acknowledgement guard because the graph build itself does not refresh that separate manifest. The full refusal log is retained. Explicit manifest regeneration/staging fixed the acknowledgement; the repeated complete pipeline passed. No scientific assertion or evidence threshold changed.

The independent source-port review passes. Generated audit outputs are restored to this branch's own HEAD only after saving this nonempty readiness evidence; controlled manifest, sources, runner caches and proof/review history remain. No audit verdict or source merge is assigned.
