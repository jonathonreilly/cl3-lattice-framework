# Verified source loader delta

PASS at production RUNTIME_FREEZE f9bdb802ea9ab651979432e5edc52fb966b811febb248b461f739821f38db41b. Read full changed run.py, actual-loader AST control source, control receipt and import-readiness receipt. Every pinned input currently matches. Worker, recurrence, envelope and validator remain byte-identical to cb13 review; no physical execution or test rerun.

load_verified reads source bytes once, verifies exactly those bytes, and compiles/executes that buffer in the created module namespace. It does not call SourceFileLoader.exec_module, so a timestamp-valid stale pyc cannot replace verified local source. Modules are registered in dependency order before dependent imports. The exact control constructs a same-size/same-timestamp pyc with VALUE2 against current VALUE1, demonstrates default loader consumption, verifies the actual extracted function returns1, and rejects wrong hash. This is a genuinely discriminating cache control rather than merely a hash change. The runtime/import boundary for external modules remains the separately pinned runtime; the repair specifically closes the reviewed local-module cache gap.

No remaining blocker in this narrow delta. Independent replay input/threshold/progress guards are a separate pending review, and the external complete production/replay contract remains required.
