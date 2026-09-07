# Cold review of root occupation-feedback note draft

Reviewed /private/tmp/toe-feedback-note-draft-20260907.md as read at the start of this review, against the separately frozen primary and orbital raw results, comparison.json, their derivation/observation memos, and the reported finite native witness scope. No draft edits. I authored the native witness, so this review checks the note's representation of its output and scope, not independent verification of that witness's internals; root owns that independent code/matrix review.

## Concrete required corrections

### 1. Restrict the coherent monomial path formula to its nonbridge domain

The section states the integrated T_(p,g) formula for a directed edge path without an explicit restriction. As written it omits bridge Record-sign dephasing. After a bridge, two occupation configurations can produce different component-parity outcomes; summing the signs removes their cross term. The displayed epsilon_x epsilon_y F_p X_g formula has no matching-outcome factor and therefore is not an arbitrary-history coherence formula.

Add immediately before the X_g/F_p construction that these coherent state formulas are used for the first four, connected nonbridge prefixes. For a later bridge, retain explicit parity/sign projectors or require matching branch outcomes in each coherence pair. The diagonal exclusion-walk/trap census DOES continue through bridges because sum_z B_z^*B_z=M_e. Distinguish that valid probability continuation from the restricted coherent state computation. This is the only substantive formula-domain gap found; it does not change the reported first-four results.

### 2. Narrow what the independent keyed comparison establishes

The sentence 'The two independent methods agree on all45 post-event path states' suggests comparison of complete70-by70 density matrices. The actual comparison receipt binds probabilities, eight site densities, twelve currents, matter/battery/conditional-total energies, initial q, reach and trap data. Neither raw row format contains a complete density matrix to compare.

Use 'agree on all45 post-event diagnostic rows' or explicitly list the compared observables. Both methods construct states, but agreement of the reported observable set is not full state tomography. The maximum residual below1.3e-12 and the292 exact configuration records are correctly reported at that measured scope.

### 3. State the full-line/safe-domain qualification for fiber formulas

Battery cap compression is introduced before the Fourier-multiplier discussion. A globally cap-compressed operator is not a Fourier multiplication operator, and arbitrary capped total-energy fibers have varying allowed system dimensions. The identities Y_B(tau)=exp(-i tau A_out)B exp(i tau A_s), R_s(tau)=gamma exp(-i tau A_s)M_s exp(i tau A_s), and 'lifted jumps become B' are literal on the full line and on the common invariant safe total-energy support reached by this prepared experiment.

Add that qualification explicitly where the fiber formulas start. The previous paragraph already asserts the needed safe-domain theorem, so this is a precision repair, not a new cap obstruction. The full-line comparison remains valid on that invariant support and the actual compressed generator remains CPTP everywhere.

### 4. Identify the coordinate convention of D_s

The displayed D_s={M_s,A_s}/2-sum B^*A_out B is the battery-drift operator in total-energy coordinates. In the ordinary Fourier representation its fiber is exp(-i tau A_s)D_s exp(i tau A_s). Replace the ambiguous 'drift fiber is gamma times' with 'in total-energy coordinates the drift is gamma D_s', or show the conjugation. The subsequent safe fixed-Q counterexample uses the former convention correctly.

## Checks that support the draft

- The dressed hazard is carefully distinguished from bare physical occupation. q_x is the diagonal of the initial energy-kernel reduction, not |psi_x|². The final statement that the head need not mark a certainly occupied bare physical site is consistent with the global energy lift.
- The no-jump anticommutator is retained. The new rate is non-scalar and may vanish at positive live degree. No identity-refusal completion is added. Cap compression preserves total-energy intertwining and yields a valid GKSL law with its own actual rate operator.
- The path energy account is correctly conditional. Z_0 and Tr T_(p,0)(Z_0) integrate the selected total-Q moment. The draft does not incorrectly equate each selected path's Q with the unconditional initial mean. The separate finite-ladder example Q10 versus Q15 illustrates selection rather than energy nonconservation.
- The negative-drift2-by2 matrix includes the anticommutator, not just recycling. A relative basis phase can make the edge hopping coefficient +t in the displayed matrix; the signed cube's actual edge coefficient does not change its two eigenvalues. For an explicit cube example choose variable occupied site0/1 and fixed occupied sites2,4,5. Other outgoing jumps from head0 vanish on both configurations. Other hopping terms have no matrix element within that two-configuration span; the compressed drift has the stated eigenvalues. The draft appropriately separates this algebraic N4 embedding from the implemented N2 square/dimer ladder witness.
- The native witness output claims match its declared test receipt: safe total-energy20, negative drift approximately-0.207106781187, preserved N/old Records/bridge parity, energy indicators and actual matrix-exponential no-jump comparison. This statement is a scope/output consistency check, not an independent rerun/audit of my own code.
- Reached masses and support ranges/counts match the raw primary summaries and the orbital result. Recomputed from raw primary rows: event4 support-passing unconditional probability0.09447537526773082; conditional on event4,0.7087283971493138. These match the draft's rounded values.
- Recomputed first-event battery range47.39498959522888..48.15097506684822 matches the stated47.395..48.151. Low selected-path battery means alone do not establish negative unconditional instantaneous drift of the frozen cube preparation; the draft only says compatibility with the drift formula, which is appropriate.
- Initial dark mass, reached-event normalization, full terminal mass and finite five-event exhaustion are presented as parts of one probability census. The tiny numerical head-occupied blocked initial weight in the raw runs is not elevated into an exact positivity assertion. The draft neither hides that mass nor calls16/24 a uniform probability.
- The note explicitly declines a pre-event front comparison. That is correct: no new pre-instrument convention was computed. Post-state support is kept distinct from the parent pre-front criterion and from expectations of absolute currents.
- The finite witness is not described as a full-cube continuous-ladder implementation, local physical particle-transfer device, renewal theorem, or independent validation of a universal no-go.

## Evidence read and limits

Read primary occupation-feedback/results.json and OBSERVATIONS.md; orbital occupation-feedback/results.json, MEMO.md and comparison.json; the note draft; and the finite witness reported outputs. Independently recomputed the two weighted event4 probabilities and first-event battery range from raw rows. No new full45-state numerical execution was performed in this review. The report does not approve metadata, helper mapping, audit status or landing structure, which were explicitly outside this task.

Disposition: repair the nonbridge-domain qualifier and the three coordinate/comparison wording points, then the reviewed scientific claims are supported at their stated conditional and finite scope. No source-side scientific calculation change is requested by this review.
