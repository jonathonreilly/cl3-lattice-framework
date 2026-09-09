# Source review findings and disposition

Initial proof43f0 read completely. Core invariant and inverse-error proof is sound. Three source corrections identified:

1. Historical full coefficient-width gate is2^-39, not2^-40. Corrected in cff1.
2. Reduced selected-G/source acquisition count was insufficiently justified for full action J,D. Corrected in cff1 to safe full principal U count5460 and explicit need for extra identities before a reduced action plan. This is not a physical impossibility claim: skewness and resolvent identities might allow further reductions, but they were not provided.
3. Literal B0 definition omitted free source terms if read as Lambda E plus impurity alone. Requested explicit padded Lambda E+QYE, with Y both free-source and actual rank-two terms. The earlier sparse identity already includes these terms.

No native inputs or actual selected data were read. Tiny independent rational 3D skew-generator/2D nonorthogonal-frame controls passed. No caller runtime or upcoming implementation is covered by this proof review.
