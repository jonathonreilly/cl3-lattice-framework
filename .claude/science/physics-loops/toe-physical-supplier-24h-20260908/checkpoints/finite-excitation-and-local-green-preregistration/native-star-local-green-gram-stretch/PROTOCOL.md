# Fixed local Green certification-cost pilot

Status: UNLAUNCHED. Source/cold review, remote preregistration and a root external monitor are required before the physical integral code is called.

Exactly four jobs run in one worker: s=1 A/A', s=1 B/B', s=2 A/A', s=2 B/B', in h=1 units. The 2D jobs have leaf cap1024; the 3D jobs cap4096. Maximum depth12, interval output precision40 binary fractional bits, sine endpoints64 bits, internal square roots80 bits. The exact dimensionless target width is1/32 for both coordinates of each job. Refinement stops at the target or the fixed cap/depth. INDETERMINATE_AT_CAP is a preserved result, not an error to repair by widening the target. Every completed row and each32-split checkpoint is saved before moving on.

The external topology must be one root monitor and one standard-library worker. Total budget30 seconds including startup, streaming pin verification, arithmetic, I/O and teardown; root kill29.5 seconds; worker alarm29 seconds. Sample the whole tree against384MiB. No retries or parallel integrators. All four fixed cases must remain in the final record even if their requested widths are not reached; a resource failure preserves completed rows and current stage.

The proposal is deliberately a small cost and enclosure study, not a forecast of final Gram precision. At most10240 leaf cells are live across the jobs sequentially; the largest individual heap has4096 leaves. Exact dyadic rounding prevents coprime denominator growth. Trig values are cached only at dyadic coordinates through depth12. The 30-second cap is prospective; no physical integration timing has been measured. Future high precision needs a new source-bound contract based on these actual costs and widths.

run.py requires -I -B -S, a fresh external output path, exact local executable/directory membership, verified-byte module loading, interpreter and broad standard-library/dylib pins. OS libraries outside that runtime inventory are explicitly outside the hash boundary. Readiness uses the real parser and loaded-module check without calling integrate or constructing a physical enclosure.

The only preparation execution consists of28 exact non-integrating checks (roots, directed rounding, Machin identity, sine normalization, rational function special values and divided differences), plus two actual source mutants rejected. They are not physical Green values. The actual physical pilot has not run.
