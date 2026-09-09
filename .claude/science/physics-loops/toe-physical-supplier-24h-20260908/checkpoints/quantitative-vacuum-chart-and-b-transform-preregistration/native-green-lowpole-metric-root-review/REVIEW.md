# Root independent low-pole metric review

PASS at source c9fc5fdc3661a1ed86bd04f98961b544a4a2e1f708a12fe1571cf1ffac23831f, conditional on the reviewed actual native density. No physical values or computation.

For same-sign resolvents the spectral theorem gives squared difference (s-t)² times the stated positive M; the real spectral denominator product is (X+s²)(X+t²). Constant-density radial integration over all space gives1/[4pi(s+t)]. The removed tail is bounded by1/(2pi²), density correction by1/(12pi²), and actual exterior by1. These yield the stated two-sided remainder including exactly one zero parameter. Opposite signs replace (s-t)² by(s+t)².

In square-root coordinates, (u+v)²/(s+t)<=2 and (u+v)²<=4epsilon establish L²=2c+4Kepsilon. Nearest point on n equal sqrt-parameter intervals is at most sqrt(epsilon)/(2n), including boundaries. The generator count7(2n+1) accounts for the shared zero pole; it is an upper bound with no covariance-invariance claim.

For individually weighted columns, trace residual<=W E_n and total norm<=W A0. The Schatten product bound gives2W sqrt(A0 E_n). This step requires the actually supplied coefficient contraction and factor weights, as explicitly stated; trace norm of the summed projector cannot replace W. The test coefficient(1,-1)/sqrt2 yields an UPPER bound for the smallest Gram eigenvalue and consequently a LOWER condition-number bound, as correctly labeled. The dimensionful scaling h^-4 M(s/h,t/h) yields the leading1/[4pi h³(s+t)]. No missing inverse factor or extra cone multiplicity appears.

This supports a pole-grid design and quantifies genuine near-dependence. It neither supplies a positive many-column conditioning bound nor certifies an actual compressed impurity projector, alpha or runtime.
