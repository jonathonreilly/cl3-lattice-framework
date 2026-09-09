# Independent root review of native infrared coefficients

PASS at DERIVATION source 08471be1b681fd65680b7d41e004430995abc16a73db948d7b86b8de18d98d19. No numerical lattice integral, elliptic formula or observed value was used.

I independently checked theta-to-x Jacobian and folded multiplicity: x=2sin(theta/2), dx/dtheta=cos(theta/2), so the density and one-cone normalization are correct. Product(1-a_i)>=1-sum a_i and the convex secant bound give the stated c=1/6 upper density correction on the unit ball.

Direct radial integration yields the displayed A-difference term and A-derivative term with coefficient4pi/(2pi)^3=1/(2pi²). The low-s arctangent gives1/(4pi). The derivative correction has bound c s/pi² and outside-ball bound2s, giving2+7/(6pi²). This directly controls the derivative rather than differentiating a generic remainder.

For B, radial integrands are s²r/(r²+s²) for the difference and2s r³/(r²+s²)² for the derivative, with the same radial density normalization. Their elementary primitives give the stated logarithms and signs. The density correction uses integrals of r³/(r²+s²) and r5/(r²+s²)², both bounded by1/2. The resulting constants1+7/(24pi²) and2+7/(12pi²) are conservative and valid on0<s<=1.

All outer kernels used are bounded by1 after removing the explicit s² or2s factor because r>=1. The h scaling follows directly from X_h=h²X and is dimensionally consistent, including B's s²/h³ remainder. A0 and B0 remain unevaluated and conditional inputs for finite enclosures; the derivative limit of A is an independent native exact coefficient without the elliptic import. No Gram conditioning, alpha or final cost is claimed.
