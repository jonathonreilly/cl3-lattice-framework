# Streaming finite occupation objectives and correlated low-frequency kernels

Source-only conditional construction. No native input, node, scalar or matrix has been evaluated. This resolves the full-cache storage obstruction at the level of an explicit finite objective; it does not assert that the resulting conservative bound is small.

## 1. Local factor objectives require no global Gram

Write the exact new projector candidate as Dhat=sum_j F_j C_j F_j*, C_j=C_j*, with one block per quadrature node and separate low/high corrections. A rational node uses r<=4 columns for a single impurity. Let the exact selected projection be P=S G^-1 S*, G=S*S>0, m=48 for the current24-pair trial. Define only

 M_j=F_j*F_j, D_j=S*F_j,
 K_j=F_j*(I-P)F_j=M_j-D_j*G^-1D_j >=0.

Then

 ||Dhat(I-P)||1 <=sum_j sqrt(Tr(|C_j| M_j) Tr(|C_j| K_j)).       (1)

Proof: C_j=|C_j|^(1/2) sign(C_j)|C_j|^(1/2). Factor F_j|C_j|^(1/2) and (I-P)F_j|C_j|^(1/2), inserting the contraction sign(C_j). Schatten Holder gives the product of HS norms. All matrices per block are at most r by r, apart from the m by r cross block. Exact null directions cause no inverse in M_j or K_j. The only inverse is the already required selected G inverse (or its preconditioned residual certificate). Interval arithmetic must certify upper traces using genuine PSD premises; it must not silently clip an inconsistent negative upper bound.

A sharper exact block quantity is Tr sqrt(M_j^(1/2) C_j K_j C_j M_j^(1/2)). It equals ||F_j C_j F_j*(I-P)||1 by the nonzero singular-value identity. It too is only r-dimensional; a validated PSD square-root trace enclosure must handle zero eigenvalues. Formula(1) is a conservative fallback that avoids that numerical subproblem.

For a positive majorant Y=S Z S* (Z=Z*, Y>=0), put B_j=F_j*Y²F_j=D_j* Z G Z D_j. Then

 ||Dhat Y||1 <=sum_j sqrt(Tr(|C_j|M_j) Tr(|C_j|B_j)).            (2)

This follows by the same factorization. The actual polar occupation inequalities add eta for the projection-tail objective and eta||Y|| for the majorant objective. Contracting P0^- on the left can only lower these nuclear norms, so no higher half-moment supplier is needed for that left projection. Cross data D_j may still require J kernels because the chosen S includes reference-Gamma partners.

The triangle inequality may lose cancellations between nodes. That is a performance/strength limitation, not a validity gap. It yields an actual implementable conservative test; if it is too large, a more correlated multi-block compression must be a separate source-bound improvement.

## 2. Concrete streaming layout and operation counts

Retain the certified m by m selected metric/inverse or preconditioner and the fixed majorant ZGZ. Stream one F_j block: its C_j,M_j,D_j, then compute K_j/B_j and two scalar upper traces. Persist each block's inputs, residual/inverse allowance and resulting trace bounds before discarding it. Never store cross-Grams between distinct quadrature nodes.

For m48,r4, storage is O(m²+mr+r²):2304+192+16 scalar intervals per operator matrix set, not millions of raw pairs. Several copies and fixed192/256 endpoints remain well below384MiB under a compiled packed or modest object representation; the future implementation must measure actual Python/object RSS rather than assume this mathematical count. Even a handful of48² matrices at conservative1KiB/interval consumes only tens ofMiB. The high correction rank at N14 is at most54 per impurity, still small enough for a separate block; it need not be split into an enormous full raw cache.

A dense G^-1D_j costs m²r=9216 multiply-add terms, followed by r²m=768 for D_j* product. A second majorant product costs another9216+768 terms if no structure is exploited. Thus a safe arithmetic count is19968 terms per node/impurity before coefficient, square-root and error-ledger work. At a prospective378-node family, two impurity classes in each of five orbits require at most75,479,040 such terms. Each orbit/class can be processed sequentially; shared literal source kernels can be cached in a bounded small block. This is an operation count, not an asserted wall time or a120-second fit. A new bounded synthetic profile is necessary before any native launch.

Only m*r=192 cross scalar entries plus at most16 self entries per node are needed, rather than a global O(nodes²) Gram. For two classes/five orbits/378nodes the loose count is786240 entries. Symmetry can lower this count but must not be silently assumed in a fixed runtime. The ratio4/378-node plan remains conditional on its separate operator quadrature proof review.

## 3. Why old independent scalar boxes are inadequate at low poles

The exact identities

 c=B(0)=E X^-1/2,
 B(s)=c-s² C(s),  C(s)=E[1/(sqrt(X)(X+s²))]

show that dividing independently rounded c-B(s) by s² amplifies absolute scalar uncertainty by s^-2. At s=2^-32, a1e-29 uncertainty becomes order1e-10. It is therefore invalid to claim a1e-12 operator/input budget using those boxes without a new correlated calculation. The fact that the physical difference is small does not make independent interval subtraction correlated.

Similarly divided differences of A or B at nearby poles require a joint enclosure. They must not inherit the old final scalar intervals as though the common A0/c contribution cancels exactly. All exact scalar values remain valid; it is the derived width that may be insufficient.

## 4. Cancellation-preserving alternative scalar interfaces

Instead of forming c-B(s), directly certify the positive kernel C(s). A legitimate integral identity is

 C(s)=(2/pi) integral_0^infinity [A(s)-A(t)]/(t²-s²) dt,

with the confluent value -A'(s)/(2s). It follows from the positive Stieltjes representation of1/sqrt(X) and Tonelli. This integral is finite for every s>0. It does not subtract independently certified c and B values. Its evaluation still needs correlated A divided differences and tail/rounding bounds; this note does not declare it an existing supplier.

For two positive poles define directly

 K_B(s,t)=E[sqrt(X)/((X+s²)(X+t²))]
          =(B(s)-B(t))/(t²-s²).

The exact Feynman-parameter representation is

 K_B(s,t)=integral_0^1 E[sqrt(X)/(X+r(theta)²)²] dtheta,
 r(theta)²=theta s²+(1-theta)t².

This preserves positivity and avoids a c subtraction. Likewise K_A(s,t)=integral_0^1[-A'(r(theta))/(2r(theta))]dtheta. The B kernel uses -B'(r)/(2r). These are exact definitions for a new jointly certified kernel interface; evaluating a poorly resolved old derivative and dividing by r is not a proof of sufficient precision.

A potentially efficient small-s branch extracts the known cusp A(s)=A0-s/(4pi)+R(s). Then

 [A(s)-A(t)]/(t²-s²)=1/[4pi(s+t)]+[R(s)-R(t)]/(t²-s²).

The logarithmic low contribution to C(s) is explicit after integration. The remainder must be enclosed by a proved joint Taylor/divided-difference bound from the exact elliptic formula, not by independently rounded A0 and A(s). A rigorous bound on R and its divided differences is still a scientific supplier gate. The scalar closed form alone does not certify that bound or its cost.

## 5. Required new input ledger

Before runtime, specify whether each cross entry uses a direct positive kernel, a common analytic expression evaluated jointly at all poles, or an independent box with an explicitly adequate propagated width. Propagate through C_j, K_j and the trace objective, including G^-1 error and possible cancellation in the residual. A trace norm budget must follow from these actual objective errors; a uniform entry-width target alone is not a substitute.

Existing unchanged current24 Gram/action evidence may be reused only with its original scalar family. A precision update requires the affine recentering proof or rebuilding the particular cross entries with new coherent scalar centers. There is no permission to shrink radii around old centers. A new larger rational bank and its projected cross-Grams are new work, not a replay of completed cache assembly.

The positive result here is a finite streaming objective with m48/r4 blocks, avoiding the832MiB full-cache construction. The unresolved questions are the strength of the block triangle bound, the low-frequency correlated kernel supplier, the actual arithmetic width propagation and measured runtime. No native probe or numerical outcome is authorized by this source plan.
