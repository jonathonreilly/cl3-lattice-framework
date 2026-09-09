---
claim_type: bounded_theorem
runner: scripts/frontier_cycle937_spider_extension_2026_07_28.py
independent_checker: scripts/frontier_cycle937_spider_extension_independent_check_2026_07_28.py
actual_current_surface_status: conditional-support
---
# Identical-arm symmetry reduction and finite comparisons — Cycle937

Date: 2026-08-05; corrected 2026-09-09

Type: bounded_theorem

Status: supplied finite mathematics; independent correction confirmation pending.

Primary runner: [frontier_cycle937_spider_extension_2026_07_28.py](../scripts/frontier_cycle937_spider_extension_2026_07_28.py)

Companion: [frontier_cycle937_spider_extension_independent_check_2026_07_28.py](../scripts/frontier_cycle937_spider_extension_independent_check_2026_07_28.py)

The [current governing memo](MINIMAL_AXIOMS_2026-06-29.md) supplies the authority
boundary. This note does not reinstate historical scalar Record/additivity
wording. Every Hamiltonian, tensor factor, preparation, arm partition, time,
field and entropy observable below is a supplied mathematical definition.
The exact original sources, outputs, intermediate versions and historical
premise material remain in [correction history](../.claude/science/physics-loops/spider-6008-correction-20260909/HISTORY.md).

## Exact conditional reduction

Take a pointer qubit and d identical arms, each with L qubits and a distinguished
root. Let D=2^L, R=Z_root and

    h = -sum_{(u,v) in E_arm} Z_u Z_v - lambda_arm sum_u X_u,
    H = -lambda_pointer X_S - Z_S sum_{j=1}^d R_j + sum_{j=1}^d h_j.

Fields are real, couplings are the displayed unit couplings, and the arm graph
is finite and simple. Arm graphs may have internal loops. There are no inter-arm
couplings except through the pointer. All arms carry the same h and R under
specified root-preserving identifications. Prepare

    psi_0 = |+>_S tensor v^{tensor d},
    v = |+>_root tensor |0>^{tensor(L-1)}.

Here |0> has Z=+1. The nonuniform preparation along an arm is identical across
arms. Permuting whole arms commutes with H and fixes psi_0. Consequently all
exp(-itH)psi_0 lie in C^2 tensor Sym^d(C^D), for every real t. Its dimension is
2 binomial(d+D-1,d). These are sufficient hypotheses, not necessary conditions
for every possible reduction. A nonisomorphic-arm example violates the stated
identical-arm construction but proves no impossibility of a different reduction.
Internal loops in otherwise identical arms preserve this construction.

Let n=(n_0,...,n_{D-1}) have sum d. The normalized occupation vector is the sum
of all distinct arm words with occupation n divided by sqrt(M_d(n)), where
M_d(n)=d!/prod_a n_a!. For a one-arm operator O, summing O over arms gives

    Gamma(O) = sum_{a,b} O_ab a_a^dagger a_b,
    H_red = -lambda_pointer X tensor I - Z tensor Gamma(R)
            + I tensor Gamma(h).

The matrix element moving b to a differs from zero by
O_ab sqrt(n_b(n_a+1)) for a!=b, while diagonal terms are sum_a n_a O_aa.
Counting the words and the ways to change one letter gives this factor.
Thus, for the normalized orbit isometry P, HP=P H_red and P*P=I. Initial
occupation coefficients are sqrt(M_d(n)) prod_a v_a^{n_a}, with the pointer
|+> factor. These identities prove the exact reduction; numerical checks below
exercise its implementation and do not replace the argument.

For L=1 the occupations reduce to the number n of flipped roots. Gamma(R)=d-2n
and the transverse coefficient is -lambda_arm sqrt((n+1)(d-n)), recovering the
ordinary collective star matrix. No elementary-function or Galois no-go from
historical Cycle933 is used. The displayed symmetric space is not asserted
minimal: in a three-site claw arm, exchanging the two leaves preserves the
preparation and h, and the invariant one-arm space has dimension
2 dim Sym^2(C^2)=6 rather than 8. A global X-parity shortcut is not used;
for L>1 it does not fix the deep |0> preparation.

## Occupation Hankel matrix and conditional entropy

Condition on pointer Z=z with probability p_z>0, and normalize that pure arm
branch. If c_n is its coefficient in the normalized occupation basis, put
f(n)=c_n/sqrt(M_d(n)). Splitting the arms into k and d-k, the coefficient between
normalized occupation vectors p and q is

    T^(k)_(p,q) = sqrt(M_k(p) M_(d-k)(q)) f(p+q).

Indeed the left and right word sums contribute M_k(p)M_(d-k)(q) equal
computational amplitudes, with their two normalization factors. Hence the
squared singular values of T are precisely the normalized Schmidt spectrum.
Transposition exchanges k and d-k. The entropy s_z(k) equals s_z(d-k), and
s_z(0)=s_z(d)=0. Define s(k)=sum_z p_z s_z(k), omitting zero-probability
branches. With two selected identical arms A,B, the conditional mutual
information is C_pair=sum_z p_z[S(A|z)+S(B|z)-S(AB|z)]=2s(1)-s(2).
These identities concern a supplied tensor factorization and pointer
conditioning; they do not identify a physical Record or its formation rule.

## L-ZERO lemma and its hypotheses

Set lambda_arm=0, retaining arbitrary real lambda_pointer and time. Every arm Z
commutes with H, so each deep site stays |0>. Separate H=H_star+D_arm, where
H_star acts only on the pointer and roots, and D_arm sums the internal arm ZZ
terms. D_arm commutes with H_star: its factors are arm Z operators, and the
only transverse term remaining acts on the pointer. Therefore
exp(-itH)=exp(-itD_arm)exp(-itH_star). The first factor is a product of local
arm unitaries. It commutes with pointer conditioning and changes no arm-cut
Schmidt spectrum in either branch. The inert deep product sites add no
Schmidt values. Thus every such conditional cut spectrum is the corresponding
star spectrum, exactly for every real time, under this preparation and zero
arm field. Arms may differ or contain internal loops for this lemma; all root
couplings must still equal those of the compared star, and cross-arm bonds are
outside the hypothesis. In the identical-arm occupation representation the
same local phases factor into left/right diagonal unitaries on T.

Turning on the arm field removes the commutation argument. A positive finite
field-on difference is evidence of that distinction, not a universal scaling
law. Neither the lemma nor its numerical examples derive a propagation speed,
a formation threshold, a physical clock, mass or dynamics supplier.

## Fresh bounded calculations and consequential controls

The primary independently compares the occupation matrix with a full-spin
matrix and normalized arm-orbit projection on five supplied cells: d2/L1,
d2/L2, d3/L2, d2/claw3 and d2/triangle3. The triangle verifies that internal
loops do not invalidate identical-arm permutation symmetry. Fields and times
are printed in full. It checks P*P, P*HP, HP-PH_red, the initial state, evolved
state, direct tensor Schmidt entropies and complement equality.

G1 is the nine-site open chain viewed from its centre: d=2 path arms of L=4.
Five full-versus-reduced comparisons use exactly the historical field/time
pairs (.05,.6), (.10,.7), (.075,.7), (.125,.7), (.15,.7). The original pinned
C_pair comparators are respectively .0033684430810797987,
.021681410144321338, .013109585337640053, .03187770547059022,
.04351050921593025. Their exact source is the archived original receipt,
which is an explicit input. This establishes only a finite conditional
comparator calculation. The historical first-commit comparison used the wrong
time row for .05; that incident is preserved. No physical exception is closed,
no six-cell status promotion is granted, and the old .02-bit comparison threshold
is not adopted as a physical criterion.

The fresh L-ZERO controls compare d2 triangle arms and mixed L1/L3 path arms
against their star at times .7,12,50 with pointer field .35 and arm field zero.
The same L1/L2 pair with arm field .1 and time .7 exhibits a nonzero C_pair
difference. Maximum dense dimension is512; maximum occupation dimension272
in these producer fixtures. Matrix/state/spectrum discrepancies are required
below1e-10, a declared finite numerical tolerance rather than a rigorous error
bound for an asymptotic coefficient.

The symmetry control changes only the first arm root field by .2 in d2/L2.
It computes leakage F P-P(P*FP) and the difference between full evolution and
the lifted projected evolution at t=.7. Both must exceed1e-3. The projected
lift remains normalized: for any isometry P and Hermitian F,
P exp(-itP*FP)c has norm ||c||. Thus normalization loss was an invalid symmetry
test; the corrected experiment tests the actual intertwining and trajectory.
K5's old method declaration is not counted as an adversarial experiment.

Every retained required scientific check and every refutation enters the actual
terminal decision. A nonempty refutation list, an empty check set or a failed
required result prevents success. The companion exercises that rule on a clean
baseline and failed/refuted cases, and calls the actual input guard with a
wrong expected hash. The primary separately challenges the immutable vendor
script's expected hash. No historical producer's exit status is reinterpreted
as evidence that all its scientific claims passed.

## Finite historical tables, not asymptotic or holdout authority

The complete original table bodies and rival scores are retained. The primary
reads their exact input-bound receipt and freshly recomputes only the original
finite scoring routine on the saved delta values. It labels those underlying
simulations historical. The grid is lambda=.30,.25,.20,.15,.12,.10,.08,.06,.05,
.04,.03,.025,.02,.015,.01 at time .7, masking |delta|<=1e-13. Rival integer
powers2..12 with log shape b in {0,.02,...,3}, integer pure powers and half-integer
pure powers are scored by their logarithmic residual spread. All original
path_d2, path_d3, path_d4 and claw_d2 steps, including the weak depth4 step,
remain inspectable with their full values and scores.

Five above-floor points are a sample-count property, not an error estimate or
proof of lambda^(2m) log(lambda) behavior. For any finite positive grid {l_i},
adding epsilon lambda prod_i(lambda-l_i) leaves every sampled value unchanged
while potentially changing the leading behavior at zero. Thus finite ranking
alone cannot establish the claimed general depth law or logarithmic term.
No step is certified asymptotically resolved by this correction.

The saved equal-lambda*t table tests only the supplied one-variable collapse
ansatz for delta_2/C_pair. The coupling sets an independent scale; failure of
that ansatz refutes neither a general light cone nor bounded propagation.
Saved long-time and flatness-threshold rows remain finite observations under
their declared protocol. The historical saturation-length column is a
threshold-based table comparison, not a derived universal arm-length law.

The six saved prediction cells remain historical comparisons. S5 uses field
.10, already present in parent grids; only the other declared new fields
.0825 and .1125 were tested by the old new-field guard. The old source recorded
reduced predictions before full-space evaluations in its own process. This
is in-process ordering, not an independently preregistered unseen holdout.
No fresh holdout experiment is claimed or replayed here.

## Source and premise boundary

The two recovered Cycle932 vendor blobs are fixed at script blob
a885eb79fd9a196b1fb4c96039ea6cb2e97c2b10 (SHA256
6975d2215149116c26392039b04b8b5a6d91236d023a1a37e8dfa602d6abce40)
and receipt blob75875bc27d2013897b3accdc347f165a68d8accd (SHA256
a82b93d79b8b4f5b768b94ff5376abc4f6c28cda43dde7d7d7b263c4bb1d6f14).
The primary reads the recovered receipt's three G1 window rows only as
historical comparison data and pins both blobs for custody. It never resolves
a moving branch or executes the932 controller. Window-edge and original
Chebyshev restriction campaigns are not replayed. Their original outputs,
including two distinct accumulation orders, remain recovery only; no new
bitwise cross-campaign identity is asserted.

The full original eight endpoints, three prior versions and recovered parent
material remain outside note discovery. Current science is preserved. No
historical parent no-go, status flag, quote scan, supplier promotion, or
Record/clock/geometry selection is accepted from that custody. Physical
realization and its connecting premises remain open. Formal audit is deferred;
this correction applies no audit verdict or retained grade.
