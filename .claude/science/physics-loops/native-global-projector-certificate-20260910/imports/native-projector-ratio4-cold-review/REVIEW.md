# Independent ratio-four operator quadrature review

Mathematical PASS for the global operator quadrature in e6f88b1d. Complete source read; no nodes or physical evaluations. The two resolvent transport factors bound the trace-class function throughout the right-half-plane ellipse. c-d>0 and1+|z-c|/Re z<=c/(c-d) are valid. Banach-valued Chebyshev truncation, Gauss positivity/exactness and the Hermitian projector prefactor give the displayed factor4rho(b-1)/(pi(rho-1)). The panel length3a is retained. The two geometric sums give389/25; multiplication yields155600/169 and final3112000/507<6139. No dimension factor or scalar-to-operator transfer is hidden.

The interval[2^-32,16] contains18 ratio4 panels, so p21 uses378 new positive nodes. Low correction and N15 high bound combine with the new quadrature constant below2e-13. Rank378*4+2+58=1572 is a valid upper bound per pair, not a measured rank. The separate8e-13 input/operator allowance remains unproved numerically.

Narrow non-quadrature wording fix requested: the example E[1/sqrt(X)-1/sqrt(X+s²)] is not the relevant c-B(s) cancellation. Its replacement should be the exact c-B(s)=s² E[1/(sqrt(X)(X+s²))]. This does not change the quadrature proof but prevents a wrong scalar supplier inference. Await author source delta for a final full-source binding.

Affected author correction97688daf verified: exact positive scalar identity replaces only misleading example, with original source preserved. Final mathematical source PASS; no repeated controls or scientific computation.
