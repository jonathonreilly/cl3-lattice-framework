# Independent review: robust one-shot native high-bit bound

The proposed inequality is valid. This review grounds it in the actual nine-mode even-CAR encoding and one native bridge sign instrument from orbital native-flux-compiler/DERIVATION.md. It does not review or imply an adaptive/multiple-event protocol obstruction.

## Native observable and compression

After a supplied number-conserving Gaussian unitary V, native component parity has observable Gamma(R), R=V*DV, with D=I-2P_component. A fixed known old-Record sign and outcome naming can be combined into eta in {+1,-1}. On the vacuum Gamma(R)=1 exactly. On the actual occupation pair |ij>, its expectation is the principal two-by-two determinant Rii Rjj-Rij Rji. This follows from the exterior-square action; no assumption that the pair state is an eigenstate is made.

For the three modes0,1,2, A=R[{0,1,2},{0,1,2}] is a Hermitian contraction. The corresponding three-by-three pair compression is exactly Lambda² A: exterior-power matrix elements are minors, and all their row/column indices lie inside this principal block. It is not claimed that Lambda² of a generic compression equals compression on arbitrary subspaces; here the coordinate-wedge subspace makes the identity exact.

The encoded pairs01,02,12 have actual high-bit target signs (-,+,+). For eta=+1 define B=Lambda²A and T=diag(-,+,+) in that ordered pair basis. Their summed correct-sign score is S=Tr(TB). Since T=I-2|01><01|,

    S=Tr B-2 <01|B|01> <= Tr B-2 lambda_min(B).

## Spectral bound

The eigenvalues of B are the pair products of the real eigenvalues of A, each lying in[-1,1]. If all three eigenvalues have the same sign, write their absolute values0<=a<=b<=c<=1. The bound on the right is ac+bc-ab <= a+b-ab <=1.

If the eigenvalues have mixed signs, global sign reversal of A does not change B. Thus write them -a,b,c with0<=a<=1 and0<=b<=c<=1. The right side is a(c-b)+bc <= c-b+bc = c+b(c-1) <= c <=1. Zero eigenvalues are included by these formulas or continuity. Hence S<=1 in every case.

For a binary native sign, wrong probability on target t is (1-t expectation)/2. Therefore the sum of wrong probabilities over the three pair inputs is (3-S)/2>=1, and their mean is at least1/3. This is a probability bound for arbitrary Gaussian preprocessing, without a determinism premise.

## Orientations and mixtures

For eta=-1 the vacuum is wrong with probability one, regardless of R. For eta=+1 the three-pair wrong-probability sum is at least one and the vacuum is correct. Thus every fixed oriented Gaussian parity rule has total wrong probability at least one over the four tests {vacuum,01,02,12}. Convexity preserves this total for any input-independent mixture of R and eta, including correlated choices of R and eta. Consequently at least one of these four input errors is at least1/4.

If eta stays physically fixed at +1, convexity preserves the stronger three-pair average bound1/3. The mixture measure must be the same for every tested input; allowing the choice to depend on the unknown input is not covered. Conditioning on a selective event can also destroy this premise and is not silently permitted.

## Standard battery lift

For an independent ready battery, the full-line native bridge effect is a positive Fourier-density mixture of conjugated parity effects. Incoming native Hamiltonian evolution on the fixed source code is number-conserving quadratic plus a scalar fuel term; the scalar drops out of the effect. Thus each Fourier fiber lies in the same Gaussian-parity class and uses the same input-independent battery density. The1/3 fixed-positive-orientation bound survives. A cap-safe realization that exactly agrees with this lift on all tested inputs also inherits it. Reading battery energy, using cap refusals as an answer, input-correlated apparatus or additional non-Gaussian control changes the contract.

## Scope and sharpness caution

No factor-of-two or exterior-compression correction is needed. The finite four-test lower bound can be saturated on that subset by mixing four diagonal reflection/outcome rules, one wrong on each test; this does not establish the global minimax error across all256 encoded inputs. The proposed statement correctly avoids such a claim. A preceding low-bit measurement, adaptive Gaussian feedback, extra readouts and multiple Record events remain outside this one-shot all-input contract.
