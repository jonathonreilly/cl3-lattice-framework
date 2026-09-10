# Exact witness contraction reassociation

Source-only independent algebra review; no selected IDs, T, scalar values, catalog, or native matrices were loaded. This is not a runtime/binder acceptance.

Let S contain the original 48 selected seed columns, V=ST, and L=Z* S (7 by 48). The exact saved dyadic T defines the original frame. Put U=LT and R=T U* (48 by 7). For each four-column rational source F, set X=F* S, A=Z*F and K to the accepted coefficient block, in the common minus-i convention. Then

    (A K)(X T) U* = (A K)(X R).

Consequently the full seven-site block with Y=I is exactly

    sum_nodes A K (A* - X R) + H (I_7 - U U*).

This changes only multiplication association. It does not replace Y by the true inverse metric, alter the original selected frame, change a sign, or remove the separately charged metric error. The high correction H U U* must remain. In the real rephased representation the stars are transposes; complex implementations require adjoints.

The formerly repeated 4 by 48 times 48 by 48 multiplication costs 9,216 summands per node. Its replacement costs 1,344. Across 378 nodes, two impurities, five orbits, this is 5,080,320 rather than 34,836,480 summands. Computing U and R once per orbit costs another 161,280 summands total. The displayed implementation currently invokes evaluate once per impurity and may recompute these: that doubles this small preprocessing term to 322,560 unless explicitly cached. These counts exclude cross-entry construction, A K, 7 by 7 contractions, interval parsing, retention and high correction; they are not a wall-time forecast.

## Arithmetic certificate

The exact 256-grid T must be enclosed outward on the 192 grid, never silently replaced by a new point. Outward interval products and sums then contain the same exact expression regardless of association. Scalar uncertainty, T mapping width and accumulated rounding all remain in the final block enclosure. A small final radius is a gate, not a consequence of the operation count.

A computable rounding-only ledger can be propagated without assuming small condition numbers. For a matrix product C=AB, with entry bounds |A|<=a, |B|<=b, inner dimension n, and input rounding errors e_A,e_B, use

    e_C <= n (a e_B + b e_A + e_A e_B) + 2 n 2^-192.

This follows termwise from perturbing a product and allowing one outward-grid unit for each product and addition per endpoint. Use the actual certified endpoint maxima and propagate separately through U=LT, R=TU*, P=AK, Q=XR, PQ, and HUU*. Sum node errors and multiply the maximum final entry error by 7 for a Frobenius bound. It is legitimate to require this rounding-only certificate below 1e-5; no unconditional such bound is asserted here. The final combined interval-radius gate remains mandatory and may honestly be indeterminate.

## Gamma correction

The full local Gamma resolvent is -L-mu O/6 when L denotes the reduced projected kernel. The constant cancels in the unequal-pole divided difference, which therefore correctly retains reduced L. A one-atom synthetic measure X=4, s=1, mu=2 has B=2/5: the relevant full entry is 2/15 whereas using reduced L alone gives 7/15, differing by mu/6. Thus the explicit correction in raw_local repairs a genuine local insertion error; it must not also be inserted into the already-cancelled divided difference.

The source algebra above is accepted. Updated binder/resource/retention changes in successor30c require their own affected review; this note does not approve them or authorize execution.
