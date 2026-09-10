"""Source-only rational coefficient assembly. No acquisition or physical loaders."""
from fractions import Fraction as F

BITS = 84
MAX_BITS = 32768

def need(ok, message):
    if not ok:
        raise ValueError(message)

def bounded(x):
    need(type(x) is F, 'literal Fraction required')
    need(max(abs(x.numerator).bit_length(), x.denominator.bit_length()) <= MAX_BITS,
         'stored rational bit cap')
    return x

def interval(x):
    need(type(x) in (tuple, list) and len(x) == 2, 'interval shape')
    lo, hi = map(bounded, x)
    need(lo <= hi, 'ordered interval')
    return lo, hi

def midpoint(x):
    lo, hi = interval(x)
    return bounded((lo + hi) / 2)

def mul(a, b):
    return [[bounded(sum((a[i][k] * b[k][j] for k in range(len(b))), F(0)))
             for j in range(len(b[0]))] for i in range(len(a))]

def quantize(x):
    bounded(x)
    # Exact nearest dyadic; upward tie. Both signs have absolute error <= half ulp.
    y = x * 2**BITS
    return bounded(F((2*y.numerator+y.denominator)//(2*y.denominator), 2**BITS))

def coefficient(s, A_box, kind, retain):
    """Return Qhat for T+=i Qhat at exact midpoint s, in unnormalized U=[e0,d]."""
    bounded(s)
    need(F(1, 2**32) <= s <= 16, 'pole range')
    need(kind in ('P', 'O'), 'impurity class')
    alo, ahi = interval(A_box)
    need(alo >= 0 and ahi-alo <= F(1,10**30), 'A acquisition width')
    # Intersect with the proved spectral range for the positive probability measure.
    # Empty intersection is inconsistent input; never silently clip it into success.
    clipped = (max(F(0),alo), min(1/(s*s),ahi))
    need(clipped[0] <= clipped[1], 'A spectral range intersection empty')
    A = midpoint(clipped)
    D = bounded((1-s*s*A)/6)
    B = A if kind == 'P' else D
    a = bounded(1-4*D)
    det = bounded(a*a+8*s*s*A*B)
    retain('coefficient_inputs', dict(s=s, A=A, A_box=(alo,ahi), D=D,
                                    Bgeo=B, a=a, determinant=det, kind=kind))
    need(det > 0, 'nonpositive midpoint determinant')
    Q = [[bounded(-8*s*B/det), bounded(2*a/det)],
         [bounded(-2*a/det), bounded(-4*s*A/det)]]
    # Independent exact inverse residual: (I-N M) Q = N, V=iN, G=iM.
    K = [[a, -4*s*B], [2*s*A, a]]
    N = [[F(0), F(2)], [F(-2), F(0)]]
    need(mul(K,Q) == N, 'Woodbury residual')
    Qhat = [[quantize(t) for t in row] for row in Q]
    error = bounded(2*max(abs(Q[i][j]-Qhat[i][j]) for i in range(2) for j in range(2)))
    retain('coefficient_exact_and_rounded', dict(Q=Q, Qhat=Qhat, operator_rounding=error))
    need(error <= F(1,2**80), 'coefficient operator rounding gate')
    return Qhat, error

def reciprocal_pi_box():
    """Machin identity; alternating remainders for40 and12 terms, exact rationals."""
    def atan_box(q,n):
        value=sum((F((-1)**k,(2*k+1)*q**(2*k+1)) for k in range(n)),F(0))
        next_term=F((-1)**n,(2*n+1)*q**(2*n+1))
        return min(value,value+next_term),max(value,value+next_term)
    a,b=atan_box(5,40),atan_box(239,12)
    lo,hi=16*a[0]-4*b[1],16*a[1]-4*b[0]
    need(F(3)<lo<=hi<F(4), 'Machin positive pi enclosure')
    out=(bounded(1/hi),bounded(1/lo))
    need((out[1]-out[0])/2<=F(1,2**180), 'Machin reciprocal radius')
    return out

def block_imaginary(Q, weight, reciprocal_pi, polarization):
    """Physical coefficient is i times this real skew 4x4 matrix, columns [X+,X-]."""
    need(polarization in ('positive','negative'), 'polarization')
    bounded(weight); bounded(reciprocal_pi)
    need(weight > 0 and reciprocal_pi > 0, 'positive weight and reciprocal pi')
    factor = weight*reciprocal_pi/2 * (-1 if polarization == 'positive' else 1)
    C = [[F(0) for _ in range(4)] for _ in range(4)]
    for i in range(2):
        for j in range(2):
            C[i][j+2] = bounded(factor*Q[i][j])
            C[j+2][i] = -C[i][j+2]
    return C

def analytic_budget():
    low = F(2,9)*F(5439,160)*F(1,2**48)+F(867,192)*F(1,2**64)
    high = F(1,8)*F(9,64)**15*(1+F(18,64*33))
    quadrature = F(6139)*F(4,25)**21
    return dict(low=low, high=high, quadrature=quadrature)

def assemble(rows, pi_box, retain):
    """Future interface only. rows contain authenticated roots/weights/A(midpoint) boxes.

    The caller must authenticate the Gauss21/18-panel source and the pi enclosure.
    This pure function does not establish those provenance or analytic premises.
    """
    need(type(rows) is list and len(rows)==378, 'exactly378 authenticated nodes')
    plo, phi = interval(pi_box)
    need(0 < plo <= phi < F(1,3) and (phi-plo)/2 <= F(1,2**180), 'reciprocal pi radius')
    pmid = midpoint(pi_box)
    epsA = rhos = rhow = epsT = F(0)
    totalw = F(0)
    last = F(0)
    for index, row in enumerate(rows):
        need(type(row) is dict and set(row)=={'id','root','weight','A'}, 'row fields')
        need(type(row['id']) is int and row['id']==index, 'literal sequential id')
        sl, sh = interval(row['root']); wl, wh = interval(row['weight'])
        s, w = midpoint((sl,sh)), midpoint((wl,wh))
        need(F(1,2**32) <= sl <= sh <= 16 and sl > last, 'root order and domain')
        last = sh
        need(wl > 0, 'weight positive')
        need((sh-sl)/2 <= F(1,2**160) and (wh-wl)/2 <= F(1,2**160), 'geometry radii')
        rhos=max(rhos,(sh-sl)/2); rhow=max(rhow,(wh-wl)/2)
        alo,ahi=interval(row['A']); epsA=max(epsA,(ahi-alo)/2)
        totalw=bounded(totalw+w)
        retain('node_start', dict(index=index, row=row))
        for kind in ('P','O'):
            Q, err=coefficient(s, row['A'], kind, retain)
            epsT=max(epsT,err)
            retain('node_operator', dict(index=index,kind=kind,
                columns='R0(+is)[e0,d], R0(-is)[e0,d]',
                positive_imaginary=block_imaginary(Q,w,pmid,'positive')))
    need(totalw <= 17, 'midpoint weight sum')
    input_error=bounded(2**27*epsA+2**42*rhos+2**13*rhow+5*epsT+2**12*(phi-plo)/2)
    analytic=analytic_budget()
    total=bounded(input_error+sum(analytic.values(),F(0)))
    # Positive-band low correction -3 epsilon/pi X0 V X0*, X0=H0^-1U.
    low_imaginary=[[F(0),bounded(-6*F(1,2**32)*pmid)],
                   [bounded(6*F(1,2**32)*pmid),F(0)]]
    high=[dict(n=n,power=2*n+1,coefficient=bounded(pmid*F((-1)**n,(2*n+1)*16**(2*n+1)))) for n in range(15)]
    result=dict(analytic=analytic,input_error=input_error,total_error=total,
                low_columns='H0^-1 [e0,d]',low_imaginary=low_imaginary,
                high_operator='sum coefficient*(HA^power-H0^power)',high=high,
                physical_columns_exact=True,gram_or_consumer_certified=False)
    retain('ledger_before_gate',result)
    need(total < F(1,10**12), 'total nuclear error target')
    return result
