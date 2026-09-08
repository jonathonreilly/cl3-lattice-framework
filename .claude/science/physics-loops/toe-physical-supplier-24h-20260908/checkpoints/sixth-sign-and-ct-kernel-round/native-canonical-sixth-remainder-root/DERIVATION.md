# A coarse exact finite-volume canonical remainder after sixth order

Research proof. Supplied H(g)=UD+gV, with full native D>=0, P=1_{D=0}, D|Q>=2, U>0. Let L=sum_e |lambda_e|, so ||V||<=L. If L=0 the claim is exact. This is a GLOBAL finite-volume norm estimate, not the volume-independent local theorem. No physical coupling selection is implied.

## Analytic canonical Hamiltonian on the fixed ice carrier

Set r=U/(4L). For complex |g|<=r and z on the counterclockwise circle |z|=U, the unperturbed resolvent has norm at most1/U and the perturbed resolvent at most1/(U-|g|L). The Riesz projection

 Pi(g)=(1/(2 pi i)) integral_(|z|=U) (z-H(g))^-1 dz

is analytic and has fixed rank. Resolvent identity gives

 ||Pi(g)-P|| <= |g|L/(U-|g|L) <=1/3.

On the P carrier let A(g)=P Pi(g) P and B(g)=P H(g) Pi(g) P. Thus ||A-I_P||<=1/3 and the principal binomial A^-1/2 is analytic, with norm at mostsqrt(3/2). The exact compressed contour identity H Pi=(1/(2 pi i)) integral z(z-H)^-1 dz bounds ||B||<=U²/(U-|g|L)<=4U/3. Consequently

 K_can(g)=A(g)^-1/2 B(g) A(g)^-1/2

is analytic for |g|<=r and ||K_can(g)||<=2U there. For real g, Pi is orthogonal and Pi P A^-1/2 is an isometry with positive P overlap. This is precisely the canonical direct-rotation column. Therefore K_can is the actual Hermitian canonical effective Hamiltonian for the whole finite ice-descended cluster. Complex g is only an analytic bounding device; no physical nonunitary dynamics is asserted.

The global bit parity F=product_e Z_e conjugates H(g) to H(-g) and is scalar on ice (every ice state has3N/2 occupied edges). Hence A(-g)=A(g), B(-g)=B(g), and K_can(-g)=K_can(g). This supplies evenness of the complete canonical operator, not just its diagonal. K_can(0)=0.

## Sixth-order truncation

Let K_6(g) contain the exact degree2,4,6 Taylor coefficients in this canonical convention. Cauchy's coefficient bound and evenness give, for |g|<r,

 ||K_can(g)-K_6(g)|| <= 2U (|g|/r)^8 / [1-(|g|/r)^2].

In particular, for a=|g|L<=U/8,

 ||K_can-K_6|| <= (2^19/3) a^8/U^7.

The constant is coarse. The volume dependence is explicit in L, and this statement does not provide a volume-uniform isolated band or useful coupling threshold. It is a norm remainder for the canonical operator, separate from the earlier one-sided fourth-order eigenvalue bound.

## A sufficient sign window for the supplied uniform model

For uniform magnitude lambda>0 write epsilon=|g|lambda/U and E=|edges|=3N, so a=UEepsilon. In the legal four-transition witness, three C4 entries of K_6 have coefficient U[epsilon^4/2-(43/6)epsilon^6] times the native B phase. The closing C6 entry has coefficient -(3/8)Uepsilon^6 times its B phase. Distinct transition supports ensure no other C4/C6 term contributes to these entries.

For a strict sufficient window impose

 0<epsilon<min[1/(8E), sqrt(3/86), 3/(2^(23/2) E^4)].

The second bound leaves each C4 magnitude greater than Uepsilon^4/4. The last bound makes the global remainder smaller than (3/16)Uepsilon^6, half the magnitude of the C6 entry; it also is smaller than the retained C4 margin. Therefore all four nonzero signs survive in the exact finite-volume canonical Hamiltonian. The negative closed product obstructs making every entry real nonpositive by diagonal phases in this explicit sufficient window.

This is an extremely conservative existence bound, not evidence of a practical sign threshold, thermodynamic phase or hardness of every simulation method. Arbitrary nondiagonal basis changes are outside the obstruction. The complete H6 coefficients and delivered legal sign witness are separate prerequisites; the analytic norm proof itself does not determine them.
