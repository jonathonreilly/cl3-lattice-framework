# Independent finite CAR-chain boundary commutant proof

Reviewed frozen primary boundary-commutant/PREREGISTRATION.md SHA256 f3f8977ff90dad5d865402c5fcf96b3cbb60d06f2578c116f63641730a2f7be5. The candidate theorem is valid as stated. No numerical nullspace result is used in this proof.

Let A={1,...,m} be a proper initial segment of a finite open CAR chain, all connecting hopping coefficients nonzero. Use the full Fock representation, an ordinary finite battery tensor factor, and an even operator O in the CAR algebra of A tensored with arbitrary battery operators. Assume the full identity [O,H+HB]=0. The operator may be non-Hermitian. Claim: O=I_matter tensor B and [B,HB]=0.

Write P_A for local fermion parity. The JW tensor decomposition across A and its exterior gives c_(m+1)=P_A tensor a_(m+1), whereas c_m acts on A alone. The crossing bond is
 t_m(c_m^dagger P_A tensor a_(m+1)+P_A c_m tensor a_(m+1)^dagger).
The exterior hopping Hamiltonian is even and acts as identity on A in this decomposition, hence commutes with O. Internal matter and battery commutators multiply the exterior identity. The exterior matrices I,a,a^dagger are linearly independent (as are their tensor products with the remaining exterior identity). Therefore the full zero commutator separately forces
 [O,c_m^dagger P_A]=[O,P_A c_m]=0.
Evenness gives [O,P_A]=0 and P_A is invertible, so [O,c_m]=[O,c_m^dagger]=0. No battery commutator can cancel these exterior nonidentity coefficients.

The factor-stripping step requires care: c_m includes a JW prefix parity string, so one should not simply identify its ordinary matrix commutant with identity on the last qubit without using evenness. First [O,n_m]=0 makes O diagonal in the last occupation, O=O0 tensor|0><0|+O1 tensor|1><1|, with battery factors included in O0/O1. Evenness implies each block commutes with parity P_(m-1). Since c_m=P_(m-1) tensor a_m, its commutator equates O0 and O1. Hence O=O' tensor I_m, with O' even on the shorter prefix. Repeat at the preceding nonzero bond. After all m modes are stripped, only B remains and the original equation becomes [B,HB]=0. This proves the statement for arbitrary finite battery dimension and degeneracies. The surviving battery algebra has dimension sum_E multiplicity(E)^2; for four distinct energies it is4.

The full-Fock premise is load-bearing. Compressing individual c_m operators to a fixed-N sector makes them zero and destroys the exterior-coefficient argument; it is not a legitimate proof shortcut or numerical implementation of this theorem. Conversely, this proof does not identify a fuel-changing map between different native Hamiltonian sectors with an endomorphism commuting with one fixed H+HB. The native Record/fuel instrument uses such sector structure, so applying this result to it would require a new explicit embedding and hypotheses.

The initial-segment geometry and single crossing bond are explicit. No arbitrary graph statement is proved: multiple exterior couplings can require a separate linear-independence analysis. If the boundary bond is severed, local even operators commuting with the isolated prefix energy survive. For m=1 the prefix hopping itself is zero; n1 is a nontrivial severed control, while the 'nonzero local hopping' diagnostic applies only to m>=2. With full-chain support H itself is a nontrivial commuting matter operator, outside the proper-prefix hypothesis.

## Relation to localization bounds

The theorem excludes simultaneous STRICT prefix support and EXACT global commutation within this fixed connected-chain class. It does not exclude exponentially small tails, approximate commutation, a finite-time state-specific comparison, or a supplied globally supported apparatus. Thus it is compatible with a finite-radius quench/Lieb-Robinson estimate: a truncated approximation can have a controlled nonzero error while no nontrivial strictly supported exact commuting operator exists.

No radius/error lower bound follows just from this qualitative commutant proof. Such a bound would require a quantitative inverse estimate and its dependence on bond strengths, region size and battery spectrum; nonzero hoppings may be arbitrarily small. On a genuinely bounded finite capped space, if a globally commuting V is approximated in OPERATOR norm by V_R, the elementary bound ||[K,V_R]||<=2||K|| ||V_R-V|| is available. A state-dependent localization bound cannot be silently substituted for that operator-norm premise, and an unbounded full-line battery cannot be silently treated as bounded. The prior retained-state/semigroup localization estimates should keep their own exact domains and constants.

Verdict: a valid conditional finite-chain exact-support theorem, with no fuel-transfer, axiomatic-admissibility, universal-locality or native-general-graph extension. Communicated the full proof and the m=1 contrast detail directly to primary before receiving its numerical outcome.
