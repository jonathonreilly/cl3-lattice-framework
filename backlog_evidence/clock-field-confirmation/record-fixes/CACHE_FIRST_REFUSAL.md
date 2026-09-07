# Preserved first cache-refresh refusal

The first author refresh executed the clock primary successfully, then the
cache writer refused the helper receipt with `RunnerIdentityChangedError`.
The source and input content identities were unchanged before and after:
source `15c25d533b55c3d2067af563371cc9fe1f7dec489d99a18050effb4be86c5e22`,
input fingerprint `9ea7f727f20c1bf720647f93e76b8c0f97bc9b5685656ebf16b488b87568e758`.
The observed change was the scripts directory metadata (size 186912 to
186944); the helper's ordinary imports created `scripts/__pycache__`.
The author's `sys.dont_write_bytecode=True` did not propagate to the child
interpreter. Set `PYTHONDONTWRITEBYTECODE=1` in the actual child environment
and rerun the bounded refresh. No cache guard was weakened, no scientific
source was changed for this repair, and the refused execution is not a cache
PASS or a full integration-gate attempt.
