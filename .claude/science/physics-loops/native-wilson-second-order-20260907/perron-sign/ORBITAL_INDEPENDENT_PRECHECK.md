# Independent Perron sign precheck

Before receiving the finalized native analytic draft, I reconstructed the radial normalization without using the diagnostic output. Put Q=r² and use a Euclidean polar coordinate after the linear metric transformation. The positive quadrant becomes a pi/3 wedge. Its Jacobian is 2/sqrt(3), and H=r³ sin(3theta)/(3sqrt(3)). Therefore

integral_C H F(Q) dxdy = (2/27) integral_0^infinity q^(3/2) F(q) dq.

The heat diagonal reflection factor at t=1 is
1-exp(-3x²)-exp(-3y²)-exp(-3(x+y)²)+2exp(-3Q).
Its leading degree-six term is 54H². This is a local Taylor check, not by itself a global inequality.

For B positive compact, a normalized top eigenvector u and its eigenvalue mu satisfy B>=mu|u><u|. For the nonnegative multiplier g=(1+Q(Q-7)/4)_+, the trace inequality implies mu integral g|u|² <= Tr(M_g B), provided this trace is defined (it is finite if bounded by the integrable heat diagonal). Since Q(Q-7)/4 <= -1+g pointwise, a trace upper bound 7/1944 together with mu>2/243 gives r<-1+7/16=-9/16. This is a valid strategy independent of the numerical diagnostic. The substantive obligations are the trace estimate and trial lower bound.
