# Independent elliptic oracle source review

PASS for final source freeze6d85facf780f73e1dbaea0f98d2ef02e670eee0344ead6a5e9219e8234da4770, subject to the separately required root monitor and preregistration before the one physical run. No physical oracle, integral or Gram call was executed by this reviewer.

## Imported identity and mathematical scope

Read both full derivations, all core/dispatcher/pilot/toy/protocol files, supplied toy/readiness receipts, and the final retention delta. Independently opened the primary-source exposition [Guttmann, section1.2, printed page5](https://arxiv.org/pdf/1004.1435). Its simple-cubic defining integral, prefactor and xi formula agree with the imported statement; the displayed elliptic argument is a modulus whose square is the implementation's parameter m. This is a source-checked mathematical import attributed there to Joyce, not a reproof of that identity. No paper values enter the controls.

The native substitution q=s²+6 and z=6/q is correct for X=6-2sum cos(2k). Rationalizing the numerator and denominator gives exactly the supplied xi². The replacement sqrt(q²-36)=s sqrt(s²+12) is valid for s>=0 and fixes the right-hand branch at0. All radicals and denominators in the rationalized expression stay away from zero in a neighborhood of0. Consequently differentiating that right-hand expression is legitimate; differentiating the original integrand under an unjustified limit at0 is neither required nor performed. The code reports a right derivative at0, not a derivative of an even analytic function of s.

The inequalities xi<1/4 and m<16/27 are conservative and correct. The normalized elliptic coefficients are binom(2n,n)^2/16^n. Terms0..95 are retained. The omitted value and m-derivative are bounded by the two explicit geometric tails starting at96. Multiplication of the nonnegative derivative-tail interval by the signed interval m' correctly encloses either derivative sign. Differentiation of the truncated series and all prefactors uses the same dual arithmetic; the derivative-tail term is not omitted.

## Arithmetic and independent controls

160-bit dyadic floor/ceiling rounding is outward for signed values. Four-product multiplication, reciprocal away from zero, and integer-squared root brackets enclose the exact inputs. The root derivative uses reciprocal of twice the positive root interval. Every operation in the oracle has these bounds; no libm accuracy assumption enters. The high powers in the exact rational tail are rounded when added to the interval accumulator. An extreme untested s can legitimately fail a parameter/divisor/width guard; this pilot promises only its five fixed points.

Independent53 exact synthetic predicates test nonsquare root brackets, signed reciprocal intervals, and omitted value/derivative subseries against the geometric bounds for two truncation lengths and three non-native parameters, with positive and negative derivative slopes. The full infinite-tail conclusion is analytical, not inferred from a finite subseries test. The tests compile the pinned arithmetic core but never call oracle. All1884 current source/runtime pins and exact local executable membership match. The copied return baseline is byte-identical to the completed original result.

The author's13 toy checks are correctly scoped to arithmetic primitives and elliptic parameter convention; they do not claim physical normalization validation. The future fixed comparisons at1/2,1,2 require both A and A' interval intersection with independent return-series intervals. Intersection is a useful falsifier, not a proof of the special-function identity or an additional high-precision containment claim.

## Failure retention, readiness and execution boundary

Initial6d806 source had one concrete issue: it checked return-series overlap before saving the just-computed oracle row. A disagreement would discard the offending interval and timing. Author preserved that freeze and repaired the pilot. Final code appends and persists each computed row with PENDING overlap before comparison; an exception keeps that row, stage and previous rows. No arithmetic or case selection changed. This closes the finding.

The strict actual -I -B -S CLI was independently exercised against the final freeze in readiness mode only; it passed without calling the oracle. Source modules execute only from hash-verified bytes, local executable/directory membership is fixed, and loaded modules are rechecked after the body. The pinned broad standard-library/runtime includes the interpreter and relevant dylibs, while OS behavior remains an explicit outside boundary. Fresh output is required. A worker alarm is secondary to the proposed external30-second,384MiB whole-tree monitor; no such physical launch was performed here.

All five rows must be retained in fixed order0,1e-9,1/2,1,2. COMPLETE_FIXED_CASES is execution completion; all_targets_met separately records precision. INDETERMINATE does not authorize tuning or retry. This review establishes source readiness, not measured cost, achieved enclosure widths, alpha, or a Gram result.

Reviewer disclosure: I authored earlier local Green/common-Gram work. I did not author this elliptic identity implementation; this review independently checked its source and arithmetic and reused the already completed return-series baseline only as a source-bound comparator.
