# Portable native witness

Original scratch source19ed1d441a27e916b92e088e2d568307f7344f0a06e94e427cd8e6febeaa1011
is preserved in the worker scratch directory. Port changes only source docstring,
AUDIT_INPUT_PATHS, repository-relative dependency hashing and stdout/JSON packaging.
Scientific matrix assembly, cases, tolerances and180second/180MiB limits are unchanged.
A live raw-to-port result comparison and independent cold port review are pending.

The derivation timing claim is read as equality of normalized physical states
on safe support, not complete timed probability densities. The independent
review provides the nontrivial unequal waiting-weight counterexample.

Raw-to-port scientific JSON is exactly equal, excluding source/resources metadata.
Root then added an explicit finite-error guard to the comparison helper, closing
NaN/Inf acceptance without changing matrix mathematics; final replay is pending.

Cold review corrected terminology: the computed2sin(0.5) quantity is the
trace norm of the state difference, twice conventional trace distance. The
portable JSON field is renamed distinct_time_state_trace_norm; its numerical
value and all scientific calculations are unchanged.
