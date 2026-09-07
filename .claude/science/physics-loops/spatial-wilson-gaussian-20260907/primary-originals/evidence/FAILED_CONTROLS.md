# Preserved control failures

1. The reversed-axis iterator was consumed after the first BFS vertex in the second-tree control. This produced an incomplete tree and a singular inverse. The frozen primary tree was correct. check-before-iterator-fix.py and ITERATOR_FAILURE.txt preserve the failure; materializing the axis order and asserting the second tree size fixed it without changing the fixture.
2. The initial absolute Gaussian prefactor candidate in GAUSSIAN_NORMALIZATION_PREREGISTRATION.md used the false simplification omega²/(2a+omega)=2a−omega. normalization_check_before_prefactor_fix.py preserves the rejected assertion. The identity on the right instead has numerator b². Direct Gaussian integration gives the corrected lambda0 in DERIVATION.md; no covariance or ratio was changed.
