# L2 forward estimator calibration: full-curve precision fails

## Outcome

The fixed population/forward estimator passes the deterministic kernel, native observable and instrumentation checks, but **does not pass the preregistered full-curve calibration**. All12 cells fail usable precision over tau1..16. One cell also fails the declared four-replica-SE consistency tolerance at tau3. The late window8..14 is not resolved, even at the largest population. No larger-volume or larger-population job was launched.

This concerns the supplied L2 zero-flux mobile component of H=V N_f-A, not a photon/phase inference. It neither validates nor falsifies a thermodynamic Coulomb phase. It does not promote a stable fitted decay to an isolated pole.

## Frozen protocol and executed resources

V=.95 and1; F6; tau0..16; populations512,1024,2048; classical warmup20 sweeps; projector burn20 or40 sweeps;8 independently seeded replicas per cell;4 correlated origins per replica separated by3 sweeps. All six transverse modes are retained. The primary mode is(harmonic1,momentum x,polarization y), matching the exact target. Four origins and six modes are never counted as independent replicas for uncertainty. Each seed is exposed in the raw cell receipt.

All12 cells completed:96 independent replicas and384 origin blocks. Total measured cell time26.5492seconds; maximum cell RSS154.109MiB. The initial fixed-seed/JIT verification used212.781MiB and3.24seconds. Both are inside the prospectively stated180second/384MiB per-job cap and900second aggregate initial allowance. The larger NumPy/Numba runtime cap was declared before execution; there was no failed resource run or silent reduced cell.

## Actual producer and minimal derivative

The fetched transverse producer imports the native stiffness geometry/count implementation and the RK state/constraint helpers. Its measure_correlation_block returns each raw descendant-product mean divided by its own C(0) mean, losing the raw denominator. It also averages normalized origin blocks. I preserved producer_original.py byte-for-byte and made measurement_derivative.py by changing only the function name and terminal `correlation / correlation[0].real` to `correlation`.

Root independently read the complete derivative and checked AST equality under precisely those two substitutions: derivative SHA69fe53bbb5201c28f1be67b5919d2304341925d8639bac2ad9fef12d7eafc175 against producer SHA5bb190ef328d095d83eacf927e2c3964499f178e6f41254368047957a893227d. That review is an instrumentation review, not certification of the original estimator. A fixed-seed64-walker comparison then gives exact equality of final states, counts, original normalized correlations, ESS and every genealogy field. Used geometry/count function ASTs match fetched versus current main; current main has unrelated run_population_core burn-boundary repairs which are not invoked by this transverse prepare_population route.

The stochastic kernel is unchanged. For a state with n_f flippable geometric plaquettes and M24, its branch weight is b=1-(V-1)n_f/M. A uniformly proposed plaquette flips with probability1/b when flippable. Therefore bP_xy equals geometric move multiplicity/M off diagonal and bP_xx=1-V n_f/M, exactly G=I-H/M. All864 states and6912 directed flip updates independently pass this equality and count-update verification. Duplicate geometric moves are counted, not collapsed to a simple graph. All final walkers pass number/Gauss/zero-flux and count checks.

The raw product means and sums are unnormalized with respect to C(0), as required to inspect numerator/denominator and ratio effects. They are **not absolute unnormalized Feynman-Kac partition numerators**: fixed-population resampling discards its growth normalizers. This distinction is retained rather than inventing unrecorded growth data. No claim about those absolute normalizers is made.

## Independent finite-forward and finite-burn target

An independent bit-graph implementation constructs the same864-state component and6912 directed moves, then constructs H and the full floating eigensystem. It does not import the provisional target's geometry or eigensystem. Direct sparse-matrix propagation yields the stationary finite-forward functional below. All864 evaluations of the actual producer's primary observable match this independent observable within1e-14.

Let psi>0 be the ground amplitude, g=1-E0/24, R=G/g, and O the real diagonal primary mode. Summing the transition/branch path weights gives the forward suffix l_F=(R^T)^(24F)1. The stationary population distribution is psi/(1^T psi), not psi². The raw descendant-product denominator and normalized curve are

    D_F = l_F^T O² psi / (1^T psi),
    C_F(tau) = l_F^T O R^(24tau) O psi / (l_F^T O² psi).

The transition Green matrix is symmetric here, so l_F=R^(24F)1. This independently reconstructs the requested finite-F functional; it is not assumed from the provisional report. The stochastic population-control and ratio biases remain separate from this infinite-population limit.

For a nonstationary normalized right amplitude r at the origin, endpoint population normalization cannot be dropped. With L=G^(24F), the exact finite-time raw numerator is

    N_r(tau) = 1^T L O G^(24tau) O r / [1^T L G^(24tau) r],
    D_r = 1^T L O² r / [1^T L r],
    C_r(tau)=N_r(tau)/D_r.

I evolve the specified common initial state through20 classical RK sweeps and20/40 projector sweeps to compute this separate burn-in target. Its difference from stationary C_F is about6.1e-16 at V.95 and4.4e-16 at RK in floating arithmetic. These are numerical residuals, not interval-certified upper bounds on exact bias. They show that deterministic infinite-population transient burn-in is far below the observed stochastic errors on this fixture; they do not remove finite-population steady-state bias.

At V.95, E0=-.4027365059097269 and D_F=.4058736920412003; maximum F6-versus-pure curve difference1.47962e-9. At RK, E0 is numerically zero, D_F=5/12 to roundoff, and F independence holds to roundoff. No exponential-time replacement was made: fits use (24-E0)[1-exp(slope/24)].

## Quantitative failures and uncertainties

Primary analysis follows the existing producer: normalize each origin block, average four origins inside each replica, then compute means and standard errors across8 independent replicas. The simultaneous consistency diagnostic is |mean-exact| <=4 SE+1e-8 for each tau1..16. This is a predeclared diagnostic, not a rigorously calibrated simultaneous confidence band with only8 replicas. Precision separately requires4 SE <=.2 C_F at every tau1..16; a wide error bar cannot earn a precision pass.

All12 cells fail full precision. Eleven fail at every tau2..16; RK2048/burn20 first fails at tau3. The only primary consistency failure is V.95,2048,burn40,tau3:

    exact C_F(3) = .0176171228539501,
    estimate = .0104084142751935,
    replica SE = .00136630255103767.

The difference is about5.28 SE. This remains a failure under the frozen diagnostic. Eight replicas, correlated times and a noisy SE do not identify whether it is finite-population bias or an unlucky fluctuation; no extra seeds were added after seeing it. The correlated six-mode average at the same point is .0177349861318572 with replica SE .00184239497014376, which is useful contextual evidence but does not replace the preregistered primary mode or erase its failure.

At the largest population and burn40:

|V|exact C_F(16)|primary estimate|replica SE|minimum distinct tau16 origins|
|---|---:|---:|---:|---:|
|.95|1.85485e-9|.00243665|.00546813|1326 of2048|
|1|3.79807e-9|-.00619806|.00382941|2048 of2048|

Thus retained ancestry is not sufficient for useful late-time precision. In the RK control, b1 gives identity resampling and no ancestry loss, yet signed product fluctuations overwhelm the positive signal. At detuning the genealogy is reduced but not nearly collapsed; neither a large ESS nor hundreds of distinct origins supplies a tiny-correlation relative-error guarantee.

For V.95,2048,burn40 the RMS primary errors in windows1–4,5–8,9–16 are .0042562,.0028780,.0031914. At RK they are .0042710,.0036412,.0030570. Complete curves, pointwise SE, signed errors and all other cells are in SUMMARY.json. Population doubling lowers some aggregate error scales but not monotonically in each window; no population extrapolation is fitted. No burn or adjacent-population difference exceeds the predeclared4 combined-SE+1e-8 test, which is lack of resolution of such differences, not proof of zero bias.

## Ratio, energy and fit diagnostics

Both average-of-block-ratios and pooled-raw ratio are reported. For pooled ratios the SE uses independent-replica numerator-minus-ratio-times-denominator fluctuations divided by the mean denominator. At V.95,2048,burn40 the maximum difference of the two curve estimators is .000278638; at RK it is .000244649. These observed differences are smaller than the late noise, but are not asserted to bound all ratio bias. The corresponding raw C0 means are .40377045 versus exact .40587369, and .41986847 versus exact .41666667. Raw block denominators and sums are preserved for every origin/mode.

The detuned mixed-energy estimate at2048/burn40 is -.40269638 with replica SE .000133933, compared with exact -.40273651. A good energy estimate does not imply a good small transverse correlator. RK energy is exactly zero by its estimator definition.

At2048/burn40 neither mean primary curve supports a positive fit on either2–6 or8–14: negative points make the logarithm inadmissible. Only1 of8 primary replicas supports the early fit and0 supports the late fit, for both V values. No negative point was dropped, absolute-valued, or replaced by a fit prior. The exact F6 comparison gaps in those windows are1.22881906/1.22445492 at V.95 and1.16581387/1.16086648 at RK; these are reference diagnostics, not estimates rescued from the failed noisy curves.

## Classification and next obligation

- Finite F: independently tiny on this specific L2 fixture; not the observed error scale.
- Infinite-population deterministic burn-in: numerically negligible for the frozen20/40 protocols; finite-population bias remains unresolved.
- Kernel/observable mismatch: no discrepancy found in exhaustive L2 transition/count and observable checks.
- Ratio choice: measured and exposed, not silently pooled; no unbiasedness theorem claimed.
- Genealogy: directly reported; RK proves that good genealogy alone does not control the dominant late-product noise.
- Population/statistical error: fails the full-curve precision requirement and has one primary consistency outlier. There is no license here to fit a late gap or scale to a larger volume.

A useful next design would need variance reduction or an independently validated spectral/moment estimator, with its own prospective comparison to this exact target. Merely doubling the same population once more is not supported as a remedy for a roughly1e-9 signal under1e-3 noise. No quantitative extrapolated population budget or phase conclusion is asserted.
