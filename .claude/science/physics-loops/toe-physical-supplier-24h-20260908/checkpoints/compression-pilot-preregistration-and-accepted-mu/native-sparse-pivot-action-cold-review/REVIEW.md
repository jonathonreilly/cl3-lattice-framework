# Independent sparse support review — PASS

Reviewed complete root proof37360d8b3eeaa19fb0839125a806f036ff3ae2611bc4d78dc2bc6e9f4fbc7fd8 and all four imported source/review pins. I authored the imported coefficient and three-source proofs; this is an independent review of root's new sparse support reduction, with that reuse disclosed.

Each raw selected half seed has at most2 coordinates; adjoining Gamma gives at most4 per accepted pair. The triangular recurrence introduces only previous seed/Gamma support, proving |R|≤4k without relying on small interval values. Every free first action adds only the stated four source types and Gamma partners. The actual rank-two impurity correction has range x0,qA (or qC) even on Gamma input, so no illicit commutation assumption is made. U contains both C and its entire FIRST action, making the principal Gram restriction exact. No second action is used.

The Hermitian factor i is correct: B represents K_A V, H_A V=i Z B, so compressed H=i C*MB while action norm is B*MB. Squaring the Hermitian compressed matrix and subtracting from action Gram yields the true PSD leakage. Complex C requires adjoints and a rigorous complex modulus for a row-sum bound; this is an implementation obligation, not a contradiction in the source proof. Coordinate symbols qA/x0 inside coefficient contractions mean their unit coordinate selectors in U, consistent with the imported formula.

At k≤4, U≤24 and at most300 upper-triangle real principal-Gram requests per orbit follow. The source correctly does not identify these with raw cache reads or wall time. Certified physical entry inflation, coefficient conditioning and accepted input identity remain explicit. No attained leakage or native isometry midpoint claim appears.

3565 exact source-pin and synthetic support predicates passed. They enumerate selected subsets of a small synthetic label family and check free-action support, Gamma closure and the count; they do not evaluate native entries or histories. No source correction requested.
