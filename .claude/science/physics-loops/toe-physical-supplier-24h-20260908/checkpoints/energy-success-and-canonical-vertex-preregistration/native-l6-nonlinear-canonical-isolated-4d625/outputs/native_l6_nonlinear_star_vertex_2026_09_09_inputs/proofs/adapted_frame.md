# Exact octahedral-adapted L6 one-star transports

This is a new computational basis design, not a modification of any frozen physical pilot. It uses the same canonical K and the previously verified48 signed site maps fixing gamma0. No spectrum, resolvent, Gaussian evaluation or full Fock vector was computed.

Order neighbors +x,-x,+y,-y,+z,-z and absorb eta_j=K_0j/2 into their unit vectors. The site maps then act by the ordinary six-neighbor permutation representation. Its orthogonal real basis is

A=(1,1,1,1,1,1), E1=(1,1,-1,-1,0,0), E2=(1,1,1,1,-2,-2),
T1=(1,-1,0,0,0,0), T2=(0,0,1,-1,0,0), T3=(0,0,0,0,1,-1).

For lambda in12,24,36,48, apply the exact polynomial projector product_(mu!=lambda)(-K²-mu)/(lambda-mu) to these neighbor vectors. The projected Gram is diagonal in this basis. Dividing squared norms by the original basis squared norms gives:

|lambda|A1g|Eg (each)|T1u (each)|
|---|---|---|---|
|12|4/27|4/27|4/9|
|24|4/9|4/9|4/9|
|36|1/3|1/3|1/9|
|48|2/27|2/27|0|

Thus the lambda48 rank3 is exactly A1g+Eg. The others have rank6. Pair each nonzero projected white vector r with Kr: this yields21 complex modes and the same42-real carrier. Orthogonality between white vectors and their black partners is automatic by bipartiteness. Exact sector eigen-identities and norms verify closure. The projected center is contained in the paired A1g direction because K e0 is proportional to the absorbed-neighbor sum. Therefore no endpoint is lost.

Whiten each irrep using its displayed scalar Gram eigenvalue and the fixed original vector norm. This preserves its representation. Every signed symmetry then acts as identity on each A1g, the same real orthogonal2x2 Eg matrix on four Eg pairs, and signed permutation on each of three T1u triplets. The two Eg norms differ by3, so the whitened entries belong to Q(sqrt3); the recorded unnormalized matrices are rational. The exact helper verifies all48 actual site transforms on every projected vector, not just an abstract character match. ADAPTED.json stores all matrices and vectors.

Because the same transform applies to r and Kr, the resulting complex annihilator matrix has these same real blocks. It preserves number and has the vacuum-fixed exterior lift from the prior transport proof. No dense21-mode mixing or arbitrary ground phase is needed.

A literal implementation can precompute the signed permutation of the nine T modes and its exterior sign table on512 occupation patterns, then stream a parity vector once. Each Eg block acts on states with pair occupation01/10 by its2x2 matrix;00 is unchanged and11 receives det(Eg). With21 modes and a fixed parity there are2^18 two-state mixing pairs per block and2^18 doubly occupied amplitudes. Four such blocks and one signed permutation require O(4*2^20) scalar work and O(2^20) storage. This is an arithmetic operation count, not a measured runtime or an implemented million-component transport. It excludes the cost of converting an old arbitrary paired basis into this new adapted basis. A solver must be defined directly in the adapted frame, or separately certify that conversion.

For first sources x_A=R_A Omega, the two pair orbits12 perpendicular/3 opposite give x_(gA)=Gamma(g)x_A. For the complete second source b_C=gamma0 sum_(A disjoint C)x_A, the same action sends b_C to b_(gC), since gamma0 and Omega are fixed and the six-predecessor set is permuted bijectively. Consequently y_C=R_C b_C also has two orbit representatives. In exact arithmetic the full vertex is reconstructed from two first solves and two second solves, with their actual exterior transports and1/8 final sum. Stabilizer choices do not change exact vectors. With approximate candidates, different representative transports can disagree within certified errors; this must be propagated rather than silently symmetrized without accounting.

This reduction does not prove vacuum linearity, a small Gaussian rank, residual accuracy, or a practical solve cost. Unequal frequencies remain. No native coupling, observable or physical protocol has changed.
