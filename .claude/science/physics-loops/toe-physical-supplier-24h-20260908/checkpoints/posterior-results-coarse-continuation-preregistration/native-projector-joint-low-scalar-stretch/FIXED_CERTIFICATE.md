# Concrete fixed C certificate candidate

Unexecuted source proposal for 2^-32<=s<=16, h=1. It supplements the direct positive identity in DERIVATION.md. The target here is absolute scalar width 10^-20, not an automatic operator-input allocation. No Joyce oracle is called. Import A0<=17/60 from the frozen native-infinite-star-node-stretch/UNIFORM_PAIR_GAP.md (h=1). In particular14A0<=119/30<4 and24A0<=34/5<7; the premise source hash is included in FIXED_FREEZE.

Use low cutoff d=2^-80, upper cutoff T=16, 84 dyadic panels, and p=32 Gauss nodes per panel:2688 outer nodes per pole. Integrate the low cusp term exactly as ell log(1+d/s). The earlier infrared low remainder applies only s<=1; for s>1 use the positive bound K(s,t)<=A0/s², so the entire low interval lies in [0,d A0/s²]. In either case the low error radius is <d (using pi>3,k<3). Certified logarithm/pi rounding is separately charged.

On a dyadic panel [a,2a], use ellipse rho=5, center1.5a, semiaxes1.3a and1.2a. Re z>=.2a, |z|<=2.8a, hence sec(arg z)<=14. For X>=0,

 |X+z²| >= cos(arg z)(X+|z|²).

Therefore the analytic kernel K(s,z)=E[1/((X+s²)(X+z²))] has modulus at most14 A0/s²<4/s². Nuclear arguments are unnecessary here: this is scalar holomorphy with an integrable dominating function A0/s² on each compact ellipse. Summing the positive Gauss/Chebyshev bound gives

 E_quad <=(2/pi)*5*(T-d)*(4/s²)*25^-32
         <(640/3)*2^64*25^-32.

For the high tail use N=20 terms from the finite expansion in the predecessor. Its error is <=(2/3)*12^19/(41*16^41). Coefficients Qj=E[X^j/(X+s²)] must be evaluated with interval recurrence, not rounded cancellation silently. The exact positive definition permits intersection with nonnegative bounds. These are new finite moments/coefficient computations, not an old integral rerun.

## Certified node arithmetic with no nested Gauss

Let g=|t²-s²| and m=(t+s)/2. All comparisons use certified node brackets, and a branch is selected only after its stated inequality is established. Ambiguous threshold brackets can use the more conservative branch.

1. If g>=2^-80, independent A enclosures of radius<=10^-49 give K radius<=2*10^-49*2^80<3*10^-25, apart from node-location error.
2. If 2^-144<=g<2^-80, request A enclosures of radius<=10^-80. The corresponding K radius is <=2*10^-80*2^144<5*10^-37.
3. If g<2^-144, evaluate L(m)=-A'(m), with radius<=10^-80, and approximate K by L(m)/(s+t). The midpoint-average error is bounded below. No subtraction of A values occurs in this branch.

An actual oracle must return certified radii; a bit setting alone is not a guarantee. Existing 160-bit certificates may serve branch1 where their actual radius meets10^-49; branch2/3 require newly certified higher precision (nominal320 bits is not itself a proof). This is a NEW proposed oracle protocol.

For the midpoint error, direct differentiation of A gives

 |A'''(r)| <=24r E[(X+r²)^-3]+48r³ E[(X+r²)^-4]
            <=72 A0/r³.

This uses E[(X+r²)^-k]<=A0/r^(2k-2), requiring no Joyce analytic continuation. Near branch3, t>=s/2 since g<s²/2. Hence r>=s/2 on the segment and |L''(r)|<=576 A0/s³. The integral-average midpoint bound is |average L-L(m)|<=sup|L''| (t-s)²/24. Dividing by s+t and using |t-s|=g/(s+t) gives

 error_K <=24 A0 g²/[s³(s+t)³] <=24 A0 g²/s^6
          <7*2^-288*2^192=7*2^-96<10^-27.

The derivative oracle contribution <=10^-80/s is negligible. Thus all branches can conservatively allocate K radius10^-24. Positive weights of total length<16 and2/pi<2/3 make the integrated node-arithmetic radius< (32/3)*10^-24. This does not yet include node or weight enclosure widths.

Node/weight perturbations must be bounded by direct interval evaluation over their brackets, including branch selection and midpoint derivative remainder. A sufficient additional total weighted-radius allowance is10^-23. Analytic low, middle, high errors plus these allocations give radius<10^-21, hence width<2*10^-21<10^-20, as checked by exact rational controls. The logarithm/pi/moment recurrence must fit that additional allowance as well; it is a condition, not an achieved certificate.

For378 poles the unshared count is1,016,064 outer nodes. Branch2/3 counts cannot be stated before exact separation analysis. No need for A'' from Joyce is assumed: the elementary A''' estimate proves the midpoint remainder. Joyce's explicit expression may improve precision/cost, but every radical/root branch and returned interval remains an implementation obligation. The proof therefore supplies a finite method and budget, not an execution-ready million-oracle contract or runtime forecast. Sharing nodes and analytic low expansions may reduce work, without changing completed protocols.
