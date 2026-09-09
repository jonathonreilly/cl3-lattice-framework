# Before-data local bytecode correction

Root found that -B suppresses writing but does not prevent SourceFileLoader from reading timestamp-valid cached bytecode. The04ad source/freeze/readiness and local bytecode are preserved in history_before_cache_fix_04ad. Only disposable active local __pycache__ was removed. The actual wrapper now reads each local source once, verifies those bytes, and compiles/executes the identical bytes into the prepared module namespace. No local SourceFileLoader execution remains.

The actual loader AST control creates a same-size/same-timestamp stale pyc. Ordinary loader returns2; verified-source loader returns1; wrong hash rejects. No physical calls. Mathematical helpers, thresholds and contract unchanged. Installed runtime/cache assumptions remain separately declared; this does not purport to disable all installed Python caches.
