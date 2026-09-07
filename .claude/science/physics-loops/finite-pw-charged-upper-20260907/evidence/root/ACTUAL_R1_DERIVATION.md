# Exact actual one-plaquette R1 charged-energy fixture

2026-09-07. This fixture was fixed prospectively before the exact Haar-contraction checker ran. All22 checks passed on the first execution. It corroborates a particular finite case of42; it does not prove the general volume-uniform bound by sampling.

## Actual neutral full-carrier ground

Take four independent Haar SU3 links around one elementary plaquette, complete PW cutoff R=1, and a=1. Write U for the path link and M for the oriented product of the other three links, so the loop is UM. U and M are independent Haar matrices, but the latter still consists of three distinct kinetic links. Exact Gauss invariance at each bivalent vertex forces all four loop representation labels to agree, with a unique intertwiner at each vertex. The neutral physical space therefore has orthonormal basis1, chi=Tr(UM), bar chi. It has electric energies0,16,16.

Actual fundamental fusion or direct Haar moments gives J=(chi+bar chi)/6 with zero diagonal and every off-diagonal entry1/6 on this basis. The source term is V=v(1-J). Set t=1/100 and v=96t/(1+t-2t^2), with N=1+2t^2. Then

 Omega=[1+t(chi+bar chi)]/sqrt(N), E0=v-vt/3

is an exact eigenvector of the3-by3 neutral Hamiltonian. The remaining eigenvalues are16+11v/6-E0 and16+7v/6, both larger. Further0<E0<v<4. Any nontrivial gauge representation is orthogonal to the global Haar vacuum and has K>=4, while PVP>=0. Thus no nonneutral representation can beat this neutral vector: it is an actual full tensor-carrier ground. This establishes the ground premise directly for the fixture, without assigning a numerical threshold to the separate weak-coupling theorem.

## Literal projected charged state

Use W=U along the single path link and define A=U, B=P(U chi), C=P(U bar chi). Complete-irrep projection of two fundamental coefficients is their antisymmetric part, while fundamental times antifundamental retains its scalar part. In indices0,1,2 this gives

 B_ij=(1/2)sum_(k,l,a,b)epsilon_ika epsilon_jlb bar U_ab M_lk,
 C_ij=bar M_ji/3.

A, B, C occupy distinct electric representation patterns and are orthogonal: respectively one fundamental path link, four nontrivial links with the path conjugated, and the three-link alternative path with the direct link in vacuum. Their electric eigenvalues are4,16,12. Their squared norms in the actual source convention integral Tr(F^*F)/3 are1,1/3,1/9.

The checker constructs these polynomials and evaluates every Gram and magnetic matrix entry by independent U and M Haar integration. It uses only

 integral U_ij bar U_kl=delta_ik delta_jl/3,
 integral U_i1j1 U_i2j2 U_i3j3=epsilon_i1i2i3 epsilon_j1j2j3/6,

the conjugate rule, and exact center-charge zeros. Unsupported moments raise an error rather than guessing zero. The resulting unnormalized J matrix is

 [[0,1/18,1/54],[1/18,0,1/54],[1/54,1/54,0]].

For example the B-J-C contraction contains36 nonzero epsilon products divided by1944, giving1/54. This is an actual SU3 projection calculation, not a freely chosen three-state Hamiltonian. Since A,B,C are already retained, their compressed magnetic matrix equals their full multiplication matrix elements.

## Exact trial energy and the sufficient-bound limitation

The projected charged state is (A+tB+tC)/sqrt(N). Put Qn=1+4t^2/9. Its accepted norm q=Qn/N and its unnormalized J numerator is(4t+t^2)/27. Its normalized energy is exactly

 Etrial=[4+(20/3)t^2+v(Qn-(4t+t^2)/27)]/Qn.

The exact excess Etrial-E0 is strictly greater than4 but less than4.01. This supplies an adverse example to simply copying the full-unitary exact4 energy identity into the finite carrier. It does not imply that this trial minimizes the full charged sector.

The actual local kinetic budgets are E_path=8t^2/N and E_face=32t^2/N, with e_R=4. The norm loss is14t^2/(9N), bounded by theta=E_path/e_R. The checker verifies the42 estimate using rational upper enclosures sqrt(theta)<=1/50, sqrt(E_path)<=3/100, and sqrt(E_face/e_R)<=3/100, each certified by squaring positive rational numbers. There is one touching face. Thus the exact trial excess is below the certified rational bound

 [4+(1/50)(4+4(3/100))+2v(3/100+1/50)]/(1-theta).

For this fixed prospective v, the cruder geometry-independent theta_bar=8v/e_R is GREATER than1. The fully explicit sufficient estimate based only on v therefore does not apply to this particular R1 fixture, while the sharper actual-energy version does. The fixture was not retuned to hide this limitation. It validates the useful local-energy theorem and demonstrates the conservatism of its optional worst-case replacement budget.
