# Block 212 corrected bounded ledger

**Repair date:** 2026-09-10

**Status:** preserved finite exact calculation; broader readings rejected or open

## Preserved finite calculation

- One fixed `12 x 4` cover, one x-graded carrier, joint slots `(2,4)`, read level `5`, and the proposed W9 profile reading.
- Both 16-entry sequential arrays are exactly nonnegative, normalize to exactly one, and differ in `16/16` entries.
- Reversing simultaneous dictionary insertion changes `0/16` structural matrices.
- Both two-pin residuals are exactly nonzero in `4/4` components and sum exactly to zero.
- Comparisons marked `10x`, `100x`, strict, or narrow are exact **l1-norm** comparisons. Against slot 4, both joint l1 norms are strictly larger and their excess is below `1/200` of the slot-4 norm. Component-magnitude counts are forward `3/4` and reverse `4/4` at that slot.
- The `5 x 16` single-readout system is real-affine consistent because `rank(A)=rank([A|b])=4`. Nonnegative restoring weights were not tested.
- The nested `(25 x 4, 25 x 12, 25 x 20)` stacks have rank pairs `(4,5)`, `(8,9)`, `(12,13)` and are affine inconsistent.
- `A^T A` is invertible at the `25 x 4` rung and singular at the 12- and 20-column rungs. The implemented pivot basis `C` has full column rank and `C^T C` is invertible at every rung.
- The three chosen fixed-coordinate Riesz residuals are pairwise nonproportional. The largest-rung residual remains a common certificate for all nested stacks.

## Rejected inference or open obligation

- More unknowns than equations does not prove consistency; rank equality does so here.
- The l1 comparisons are not componentwise inequalities.
- There is no all-rungs singular-Gram claim.
- Sequential-factorization order dependence is not a universal dependency-order theorem or nonclassicality result.
- The profile-as-probability and pinned-profile-as-conditional readings remain proposed.
- Simplex membership, a multi-context joint stack, richer alphabets, other fixtures, and other parameter choices remain open.
- No classical no-go, violated bound, generic theorem, continuum result, dynamics, gravity, axiom, premise, or primitive is supplied or adopted.

## Provenance disposition

The old 42-module Python closure is absent on current main. The repaired runtime uses a reviewed helper containing only the fixed construction actually needed and imports current Block 105 for `EX`, `ET`, and `shift_lifts()`. Historical parent theorem prose and unused closure objects are archive context only. The historical healing weights cancel on the selected self edge and are not a live input.

All four original Block 212 bodies and the relevant old helper bodies are preserved exactly in `.claude/science/physics-loops/released7753-recovery-20260910/`. The old cache and its printed fingerprints are historical evidence. No matching standalone independent-check artifact was found among the original four bodies.
