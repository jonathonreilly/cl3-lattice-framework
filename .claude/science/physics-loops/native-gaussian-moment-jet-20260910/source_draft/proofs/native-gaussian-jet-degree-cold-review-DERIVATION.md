# Cumulant degree audit and native projected moment table

Source-only conditional PASS of the degree bound. The relative determinant/GNS identification remains the separate bridge under review; the algebra below neither assumes its native validity from a finite toy nor computes any actual moment, scalar, array or supplier.

## Analytic cancellation before acquisition

Introduce a formal coupling z in V. In the jet U(t)=exp(th)exp(-t(h+zV)), every U_n is homogeneous of total h/V degree n and has no zero-V term for n>=1. Its part linear in z satisfies

 U_n^[1]=-ad_h^(n-1)(V)/n!.

This follows from U1=-zV and (n+1)U_(n+1)=[h,U_n]-zU_n V. For n>=2,

 Tr(P U_n^[1])=0,

since [P,h]=0 and Tr(P[h,X])=Tr([P,h]X)=0. In the infinite setting the cyclic step is valid for bounded h,P and trace-class X; iterated commutators of finite-rank V are finite rank. No cyclicity of an unregularized infinite free trace is used.

Now use the formal log expansion

 ell_n=(1/2) sum_(m=1..n) (-1)^(m+1)/m
       sum_(k1+...+km=n,ki>=1) Tr(P U_k1 ... P U_km).

For m>=2 every factor U_ki has at least one V, hence every word has at least two V in total. For m=1 the only one-V term cancels as above. Thus every surviving cumulant monomial of order n>=2 has at most n-2 free h letters. This is a bound on the TOTAL degree of a trace monomial, not n-2 on each factor followed by uncharged multiplication.

After writing V=F J F*, F=(a,d), J=2i[[0,1],[-1,0]], break each cyclic trace at its V factors. A segment of h and P collapses, because [P,h]=0 and P²=P, to h^j or P h^j. Its exponent cannot exceed the total number of h letters. This produces cyclic traces/products of2x2 ordinary or projected source moments with powers j<=n-2. Trace cyclicity can merge the end segments but cannot increase their total exponent. Log products create additional P separators, not extra h letters.

The reconstruction Z'=ell' Z multiplies scalar cumulants with total order n. Each cumulant entering m_n has order<=n, so it introduces no higher one-particle power. The mean is separately ell1=-Tr(PV)/2=-c. Therefore cumulants and reconstructed moments through N>=2 have the sufficient source table j<=N-2. A naive implementation constructing the full2N-column jet Gram first could still request powers2N-2 unnecessarily. The cancellation and degree filtering must be implemented symbolically BEFORE that acquisition; numerical cancellation of high-power enclosures is not a justification to omit them.

## Native sign conventions and general measures

Here h=h0=iK, P=1_(h<0)=(I-sign h)/2, h=1 units for energy scales. K is real skew, Ka is the signed sum of the six neighbor basis vectors, and a^T Kd=-2. Define M_j=<a,|h|^j a>, M0=1, M1=mu=3c, M3=nu, M5=omega5, M7=omega7, M9=omega9.

The reviewed pair spectral measures give, for every function in this finite calculation,

 <d_P,f(|h|)d_P>=2<a,f(|h|)a>,
 <d_O,f(|h|)d_O>=(1/3)<a,|h|² f(|h|)a>.

The signed center-edge symmetry gives

 a^T K f(|h|)d=-(1/3)<a,|h|² f(|h|)a>.

Indeed the six signed edge contributions are equal; a pair is one third of k=Ka, and a^T K f K a=-<a,|h|²f a>. This fixes the negative imaginary odd cross entry below. It is not obtained by treating K as positive adjacency. The relation also applies to f=|h|^-1 on the stated local vectors; the bounded sign operator is the actual expression at j=0. No globally bounded |h|^-1 is assumed.

Define D_j=F* h^j F and B_j=F* P h^j F in order(a,d). These matrices are Hermitian; lower off-diagonal entries conjugate upper ones. Let T_j=2M_j for P-pair and T_j=M_(j+2)/3 for O-pair. For r>=0:

 D_(2r)=[[M_(2r),0],[0,T_(2r)]],
 D_(2r+1)=[[0,-i M_(2r+2)/3],[+i M_(2r+2)/3,0]],

 B_(2r)=[[M_(2r)/2,+i M_(2r+1)/6],
          [-i M_(2r+1)/6,T_(2r)/2]],
 B_(2r+1)=[[-M_(2r+1)/2,-i M_(2r+2)/6],
            [+i M_(2r+2)/6,-T_(2r+1)/2]].

Proof: h^(2r)=|h|^(2r); h^(2r+1)=iK|h|^(2r); h^j sign(h) equals iK|h|^(j-1) for even j, and |h|^j for odd j. Substitute into B_j=(D_j-F*h^j sign(h)F)/2. In particular B0[a,d]=+ic/2, whereas the physical ordered Majorana contraction <gamma(a)gamma(d)>=-ic. The latter is2P transposed in these real coordinates; substituting it directly for B0 would reverse the determinant convention. Tr(PV)=2c and ell1=-c check this factor and sign independently.

## Sufficient scalar requirements through moment10

The bound does not assert each highest scalar necessarily survives further exact cancellation. It is a sufficient acquisition boundary.

| New target moment | Maximum segment power | P-pair largest odd absolute index | O-pair largest odd index | Largest even index over both |
| --- | --- | --- | --- | --- |
| m7 | 5 | 5 | 7 | 6 |
| m8 | 6 | 7 | 7 | 8 |
| m9 | 7 | 7 | 9 | 8 |
| m10 | 8 | 9 | 9 | 10 |

Thus the combined P/O route to m7,m8 needs prospective omega7 beyond c,nu,omega5; m9,m10 additionally needs omega9. It does not need omega11 under this degree-filtered representation. Ordinary projected-even O entries at j8 require the exact even M10/3, which must not be silently dropped just because the free power bound is8.

Even M_(2r) for r<=5 are elementary native dispersion moments. An exact unevaluated formula is

 M_(2r)=sum_(a+b+c=r) r!/(a!b!c!) binom(2a,a)binom(2b,b)binom(2c,c).

These are finite integer identities from the native sum of three independent4sin² coordinates. Existing lower exact values may be imported; any new M8/M10 combinatorial evaluation must be included in the future source/protocol and not confused with a numerical scalar oracle. No new even or odd moment value was computed here.

## Finite cost representation and unresolved work

A table through8 has nine ordinary and nine projected2x2 blocks per pair class, at most72 complex slots/class before Hermitian/parity reuse. There are only the two new real interval suppliers omega7/omega9 plus the finite exact even-moment identities. Multiplication uses source Gram entries, not a raw-bank inverse or fictitious independent modes. The coefficients of the rank-two V carry the physical factor2i.

A constructive implementation can represent U_n as noncommutative words tagged by total order, V-count and projected-segment powers. Remove the pure-h and traced one-V sectors analytically, expand log compositions with their1/(2m) coefficient, contract cyclic2x2 source blocks, then use the scalar exponential recurrence. Alternatively a filtered finite-rank series can retain those tags. Neither a dense2N bank without degree filtering nor an unproved cancellation of interval widths earns the reduced supplier count.

Literal formal expansion remains finite but may be expensive: U_k has at most2^k-1 distinct nonempty-V words after collecting their rational coefficients, and an upper combinatorial log-word count is sum over compositions of n of product(2^ki-1). Cancellations and identical-word caching can lower this count. This is an operation representation, not a runtime/precision forecast; source coefficient growth, directed arithmetic, cumulant cancellation widths and output retention need their own bounded implementation review.

The infinite determinant identity, cumulant-to-native-moment identification, authenticated omega7/omega9, exact even moments, and numerical width/cost certificate remain missing obligations. Reusing accepted lower scalar moments in the final scalar recurrence must be distinguished from recomputing them as new native comparison targets.
