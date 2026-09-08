# Exact64-to16 Bloch-square reduction and degree-eight algebra

This derivation was completed without reading the pending96-matrix pilot or its output. It applies to every one of the32 supplied cube-link representatives, hence the six reviewed density classes. Unit hopping and the reviewed real period-four tiling are retained. No new eigenvalue or integral computation is performed.

## Folded coordinates

Write r_a=2b_a+v_a with b_a,v_a in{0,1}, and y_a=f(r_a)=v_a xor b_a. Use cube coordinate y and block coordinate b, each an8-dimensional space. Let a_a(y_other) be the internal cube bond sign, diagonal and independent of y_a. Set

C=sum_a a_a(y_other) X_{y,a},
A_a=a_a(y_other) Y_{y,a},
Z_b=Z_{b,0}Z_{b,1}Z_{b,2}.

Internal hopping is C tensor Z_b. A crossing hop flips b_a while keeping y fixed. Its b_a matrix is X when y_a=1, and cos(k_a)X+sin(k_a)Y when y_a=0, multiplied by product_{c>a}Z_{b,c}. This follows directly from the positive-wrap exp(+ik) convention: for y_a=0 the b=1 to0 matrix entry is exp(+ik).

Call the crossing operators Q_a. They square to identity and anticommute pairwise, since their block Jordan-Wigner strings supply one minus sign; their y-dependent projectors commute across different axes. Hence (sum Q_a)^2=3I. In the mixed anticommutator only the same-axis internal term contributes. Using [X,Z]=-2iY gives the exact identity

h(k)^2=(C²+3I_8) tensor I_8 + sum_a A_a tensor Gamma_a(k),
Gamma_a=product_{c<a}Z_{b,c}[(cos k_a-1)Y_{b,a}-sin k_a X_{b,a}].

The Gamma matrices are Hermitian, mutually anticommute and satisfy Gamma_a²=q_a²I, q_a=2sin(k_a/2) on the zone[0,2pi]^3. For nonzero q_a, independent block-spin Z rotations turn the three normalized Gamma into the standard three Jordan-Wigner Clifford generators. Their8-dimensional representation contains the two inequivalent2-dimensional complex Clifford irreducibles, each twice: the central chirality has trace zero and eigenvalues plus/minus1 with multiplicity4.

Consequently h² is two copies each of D_plus and D_minus, where

D_plus(q)=(C²+3I_8) tensor I_2 + sum_a q_a A_a tensor sigma_a,
D_minus(q)=(C²+3I_8) tensor I_2 - sum_a q_a A_a tensor sigma_a,

and sigma_a=(X,Y,Z). Cube parity P_y=product Z_{y,a} commutes with C² and anticommutes with every A_a, so conjugation by P_y exchanges D_plus and D_minus. Thus h² has precisely FOUR copies of the16-dimensional D=D_plus. Degenerate q_a=0 cases follow by continuity of the characteristic polynomial, without dividing by zero. D is positive semidefinite for q in[0,2]^3 because every such q comes from a Bloch momentum.

## Kramers doubling and exact polynomial degree

Every A_a is purely imaginary, while C² is real. The antiunitary Theta=(I_8 tensor iY) complex conjugation satisfies Theta²=-I and Theta D Theta^{-1}=D: both A and the spin Pauli vector reverse sign. Therefore each eigenvalue of D has even multiplicity. Its characteristic polynomial is the square of a monic degree-eight polynomial p(z;q). This is a finite algebraic degeneracy, not physical species or time-reversal identification.

One can compute p exactly without choosing square-root branches of a determinant. Its power sums are s_j=Tr(D^j)/2; Newton recursion c_0=1 and j*c_j+sum_{i=1}^j c_{j-i}s_i=0 constructs its eight coefficients. They are polynomials in q. Spin pi rotations flip any two q signs, and P_y flips all three; hence each coefficient is even in each q_a. In x_a=q_a², coefficient c_j has total degree at most floor(j/2). This gives a small exact polynomial representation with at most35 monomials per coefficient, rather than a64-degree Laurent determinant. Explicit coefficient extraction is a next deterministic task, not asserted completed here.

For the canonical cube C²=3I. Its A_a anticommute. Therefore the three A_a tensor sigma_a commute, square toI and have all eight joint sign assignments with multiplicity2. The canonical D roots are

6 + epsilon_0 q_0 + epsilon_1 q_1 + epsilon_2 q_2,

one for each epsilon in{+1,-1}³, each twice. These are nonnegative on the physical cube and reproduce the seam-aware finite pi dispersion after grouping the four-cell momenta. In particular k=0 gives6I; k=(pi,pi,pi) includes zero. No smoothness through that zero is presumed.

## Density normalization and certification route

Tr_64|h|=4 Tr_16 sqrt(D). Thus

e_aux=-(1/32) average_k Tr_16 sqrt(D)
      =-(1/16) average_k sum_{j=1}^8 sqrt(lambda_j(D)).

The original native half-factor and restored hopping amplitude remain unchanged. Setting q_a=2sin(theta_a), theta in[0,pi/2]^3, replaces the normalized k integral by the uniform normalized theta integral. It avoids introducing an endpoint-singular arcsine weight into a numerical implementation.

A concrete rigorous route is now degree-eight real-root isolation at rational q or certified interval evaluation of D16, coupled to sine intervals and a fixed/admissibly refined box enclosure for the trace square roots. The canonical eight roots are explicit. Zero neighborhoods need interval/Holder treatment, not a falsely smooth quadrature remainder. Exact Newton coefficients can permit cheaper certified root enclosures than repeated64-matrix diagonalization. This reduces an actual algebraic cost; it does not establish positive density differences or that the resulting enclosure will be sharp enough. Correlated comparison bounds and finite-size/winding corrections are still independent obligations. No pointwise ordering against the canonical background is assumed.

## Deterministic controls

The preregistered control compares the literal64-site Laurent square with the tensor identity for all32 backgrounds at all eight k_a in{0,pi}. It also checks the reduced Hermitian block and exact fourfold trace moments through degree3:1,281 predicates,0.36seconds external,21,528,576bytes high water. Omitting the entire cross term changes224 of256 cases; it is a genuine adverse matrix check, not a claimed coefficient mutant.

A second exact control uses the nontrivial rational unit phase(3+4i)/5 in all three axes. After multiplying h by5, the square identity is verified entirely in Gaussian integers for all32 backgrounds, so the sine terms absent at0/pi are actually exercised. The same control verifies Theta invariance and Theta²=-I at the algebraic test vector q=(1,2,3); q=3 is explicitly only an algebraic test, not a physical momentum.96 additional predicates pass. Python complex values here contain small exactly represented integers; there are no floating eigenvalues, tolerances or integrations.

The analytical Clifford and antiunitary arguments, rather than finitely many trace moments, establish the full all-k multiplicities. All inputs, source and outputs are hash-bound. No pilot result was read before this freeze.
