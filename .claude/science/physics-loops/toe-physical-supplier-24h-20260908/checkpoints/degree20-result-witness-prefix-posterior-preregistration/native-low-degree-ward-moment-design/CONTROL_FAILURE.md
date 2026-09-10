The first control invocation failed before importing core or executing any control: macOS rejected setrlimit(RLIMIT_AS, (384MiB,384MiB)) with ValueError current limit exceeds maximum limit. No mathematical result produced. Replaced unsupported AS guard with DATA limit and a parent sampled process RSS/time guard; this is a synthetic-only invocation.

The DATA limit also failed before imports. That failed runner/stderr/receipt are preserved. Final runner uses external sampled RSS and29.5s wall guard plus child29s alarm; no claim of OS hard memory reservation.
