# Post-execution mutation amendment

The baseline runner returns `PASS=13 FAIL=0`.  All 21 preregistered mutations
are killed.  One postexecution mutation was added after exact index inspection:

- `conflate_Gram_with_transfer`

It forces the false reading that the two-slice coefficient array closes a
nontrivial OS time-translation target.  The fifth certificate kills it because
the exact identities are `C=G`, `G^-1 C=I`, `C != I`, and
`target_closed=False`.

Final result: 22 mutations killed, zero survived.  Mutation execution now
stops immediately after the first failed certificate.  This fail-fast change
prevents already-killed perturbed kernels from consuming minutes in irrelevant
symbolic reconstruction; it does not skip any baseline check, weaken a
threshold, or change a target event.
