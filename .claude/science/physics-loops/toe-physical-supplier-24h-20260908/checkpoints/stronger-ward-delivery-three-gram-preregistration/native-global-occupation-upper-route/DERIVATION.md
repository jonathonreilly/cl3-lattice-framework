# A finite global occupation-tail upper certificate

Source-only route, no new Gram, scalar, moments, selected IDs or transforms evaluated. It is a possible consumer-directed replacement for the inconclusive seven-row lower witness, not a numerical conclusion or a recommendation to rerun that witness.

## Exact quantity and imports

Use RAW_BANK_OCCUPATION.md and POLAR_OCCUPATION_INTERFACE.md in their supplied doubled-CAR positive-polarization convention. Write R=P0+, A=PA+, C=(I-R)A, Q=|C|=(A(I-R)A)^(1/2). Then M=Tr Q<87/2 and, for the EXACT selected orthogonal projection P, the required quantity is

 tau=Tr((I-P)Q).

It is NOT Tr((I-P)C²), Tr((I-P)C*C), or the unweighted projector leakage. C need not be self-adjoint. Right support Q⊂A H is essential for the physical Fock interpretation. The supplied polar trace identity gives tau<=||C(I-P)||1 without any S1-Lipschitz claim for absolute values.

If ||Dhat-(A-R)||1<=eta, put Chat=(I-R)Dhat. Then ||C-Chat||1<=eta, hence

 tau <= eta + ||Chat(I-P)||1.                                  (1)

The existing global378-node operator descriptor, including its TWO inverse columns and FULL fifteen-term high polynomial correction, supplies a sufficiently fine eta as an imported certificate (the accepted conservative bound is2e-13). The older66-node or leading-high-only coarse approximation must not silently substitute for that descriptor. The latter's approximately.019 analytic charge already exceeds a1e-9 occupation target.

## Exact physical finite Gram identity

Write Dhat=F K F*, with actual physical descriptor columns F, coefficient K, and the exact physical preconditioned selected48-column frame S. The raw selected seed matrix alone does not have the near-identity metric used below. Set

 H=S*S>0, P=S H^-1 S*, M_F=F*F,
 A_F=F*(I-R)F, B_F=F*S,
 G_tail=M_F-B_F H^-1 B_F* >=0.

Then Chat(I-P)=[(I-R)F] K [(I-P)F]*. Its nonzero singular values equal those of A_F^(1/2) K G_tail^(1/2), including multiplicity. This follows from the polar decompositions of the two finite column maps; kernels contribute only zeros. No inverse of M_F, ghost-mode orthonormalization or natural occupation eigenbasis is needed.

A square-root-free matrix sufficient bound is

 ||Chat(I-P)||1 <= sqrt(r Tr(K* A_F K G_tail)),                 (2)

where r<=number of descriptor columns is an explicit rank upper bound. The trace is a physical Hilbert–Schmidt norm squared. A negative computed upper enclosure is a failure, not permission to clip it. Equation(2) needs only finite Gram contractions and a directed scalar square root. A certified finite PSD spectral calculation could improve it, but that would be an additional numerical procedure, not a hidden import.

For any factor split K=L N*, a second bound is

 ||Chat(I-P)||1 <= sqrt(Tr(L* A_F L) Tr(N* G_tail N)).          (3)

It may avoid dense cross-block products at the price of triangle/Cauchy loss. There is no claim either bound is sharp enough for the actual24-pair frame.

## The selected metric cannot be replaced without a charge

The accepted selected-frame certificate bounds ||H-I||<=e<8e-6; it does not make S an exact isometry. Replacing H^-1 by I gives SS* rather than P and costs

 ||P-SS*||<=e,
 extra tau charge <= ||Chat||1 e <= (43.5+eta)e.

That source-only upper allowance is about3.5e-4, far too large for1e-9. This is not evidence of an actual large error; it means this particular coarse bound is insufficient.

A certified point inverse candidate J with ||I-HJ||<=d satisfies

 ||P-SJS*|| <= (1+e)d/(1-e).

Its contribution to(1) is bounded by (43.5+eta)(1+e)d/(1-e). It must fit the allocation alongside all physical Gram/coefficient and arithmetic errors. Merely having e<8e-6 does not certify a sufficiently small d for an arbitrary point J.

Alternatively use the finite polynomial J_n(H)=sum_{k=0}^n(I-H)^k inside the exact Gram expression. Its deterministic inverse remainder is <=e^(n+1)/(1-e); n=2 makes the projector-induced nuclear charge below3e-14 under the stated e and M. This is an identity in the EXACT H. A computation on interval H still needs outward propagation of every physical input width and coefficient dependency; the small truncation remainder does not erase those widths or guarantee a narrow final enclosure. A3-term Neumann expression avoids an uncontrolled inverse algorithm while keeping the exact metric error explicit.

## A bounded streaming alternative and its costs

Per one impurity, the existing physical descriptor has a safe column bound

 n=4*378+2+58=1572.

The first term is the node blocks, the second the zero-frequency inverse block, and58 is the bare-Krylov high correction of degree28. Their exact coefficient representation must be supplied, not merely the polynomial's name. Processing each impurity separately avoids inventing a common numerical eigenbasis. Selected H has48 columns in each pair-orbit frame.

A full upper-triangular acquisition of M_F and A_F plus B_F and H would have at most

 n(n+1)+48n+48*49/2 =2,549,388 scalar Gram requests per case.

This is a structural upper count, not a proposed job. Two dense full complex interval matrices at256-bit endpoints alone require about633MB of packed endpoint storage, excluding indexing and arithmetic; Python Fractions cost substantially more. It is not a384MiB plan.

Instead split Dhat into378 rank<=4 node terms, a rank<=2 inverse term and a rank<=58 high term. Triangle inequality in(1) permits a sum of separate nuclear upper bounds. For each node only its4x4 ordinary/projected Grams and4x48 selected cross block are needed. A literal upper count, without sharing/reusing entries, is

 378*(2*10+4*48) + (2*3+2*48) + (2*1711+58*48) +1176
 =87,620 scalar requests per case.

This can be streamed with small matrix storage, with the58-column high block the largest extra block. The resulting bound loses inter-node cancellation and may be useless; no timing, width or threshold success is predicted. Ten cases multiply this count by10 before sharing. Current seven-local-row contractions do not constitute these global Grams.

## New scientific evaluations still required

- Actual ordinary and negative-reference-band self/cross Grams of new rational columns, and their selected-frame cross Grams. Existing A/B data define much of the scalar reduction but coarse B widths and divided-difference/confluent sensitivity must be certified for THIS nuclear target; the old witness radius allowance is not automatically sufficient.
- Exact inverse-column self/cross quantities at zero and their projected counterparts, with explicit one-sided/confluent limits and existing zero-frequency inputs. No singular division by a nominal zero pole is allowed.
- A finite coefficient factorization of the COMPLETE high polynomial in its physical bare-Krylov columns. Its Gram entries involve powers through K0^56 and corresponding reference-covariance insertions on the local source family. Existing c,nu,omega5 alone do not provide these higher-order entries. Finite lattice polynomial identities and certified absolute-moment/covariance reductions must be derived and costed; no high-moment calculation was made here.
- H and its certified inverse/residual or Neumann evaluation in the same frame, retaining physical input widths. The selected certificate authenticates the frame but is not an automatic fine inverse or fine global Gram certificate.
- A final positive upper enclosure for the finite nuclear objective including arithmetic and interval errors, with all signed coefficients and source normalization preserved.

Thus a new87,620-request streaming gate is only an architecture, not yet a source-reviewed executable protocol. The highest-value early check would be a source-derived finite block error/cost budget, especially whether the high term and metric uncertainty can fit the occupation allocation. No new acquisition should be launched solely because the lower witness was small.

## Consumer thresholds and remaining propagation obligation

The supplied occupation-consumer target ledger requires tau<=1e-9 AND rho²=Tr(QY)<=1e-16 h² for a positive commuting time-uniform residual majorant Y. With M<43.5, cutoff S=1e8/h and t<=100/h these suffice for the propagation component error<1/3000. Additional finite-state/projector/scalar/arithmetic contributions must total<=2/3000 to reach the stated unnormalized1e-3 map accuracy. They do not automatically control inserted Ward words or normalized/mixed Gaussian kernels.

A workable tail allocation is eta plus the finite objective and metric/input errors <=1e-9. Fine eta alone is insufficient. For the residual objective the exact analogous route is

 rho² <= ||Chat Y||1 + eta||Y||,
 Y=S H^-1 W H^-1 S*, W>=0 with the required commuting relation.

Here Chat Y has finite factors (I-R)F [K B_F H^-1 W H^-1] S*, so the same finite Gram bounds apply. With eta<=2e-13 and a half-budget5e-17h² for eta||Y||, one additionally needs ||Y||<=2.5e-4h², or a sharper eta. An instantaneous leakage value is insufficient; W must dominate the evolved residual for both time signs over the Poisson range. No such actual W or small nuclear term is supplied by the failed lower witness.

The seven-row witness measured Z*D(I-P), which can be small while the global residual remains large. Its smallness cannot certify any of these upper objectives. The polar upper route is legitimate and already anticipated by reviewed source lemmas; the new content here is the exact fine-descriptor/metric obligation and concrete streaming versus dense acquisition boundary. Consumer sufficiency remains open.

The full-space projection and Gram identities above do not establish an impurity-positive-band Fock map. Positive-band projection/transport and its contraction property remain exactly the separate interface obligations in POLAR_OCCUPATION_INTERFACE.md.
