"""Source-only finite Clifford/Wick Ward engine; no native data or driver."""
from fractions import Fraction as F
from functools import lru_cache

MAX_TERMS=262144
MAX_PRODUCTS=2000000
MAX_WICK_STATES=65536
MAX_BITS=16384
COUNT={'products':0,'wick_states':0}

def reset():
    COUNT.update(products=0,wick_states=0)
def guard(x):
    if len(x)>MAX_TERMS: raise ValueError('term cap')
    for (m,p),v in x.items():
        if type(m) is not int or m<0 or p not in (0,1): raise ValueError('Clifford label')
        if max(v.numerator.bit_length(),v.denominator.bit_length())>MAX_BITS: raise ValueError('rational cap')
    return x
def add(*xs):
    z={}
    for x in xs:
        for k,v in x.items(): z[k]=z.get(k,F(0))+v
    return guard({k:v for k,v in z.items() if v})
def scale(x,c): return guard({k:v*F(c) for k,v in x.items() if v*c})
def mul(x,y):
    z={}
    for (a,p),v in x.items():
        for (b,q),w in y.items():
            COUNT['products']+=1
            if COUNT['products']>MAX_PRODUCTS: raise ValueError('product cap')
            aa=a; swaps=0
            while aa:
                bit=aa&-aa; swaps+=(b&(bit-1)).bit_count(); aa-=bit
            k=(a^b,(p+q)%2)
            z[k]=z.get(k,F(0))+(-1)**(swaps+(p+q)//2)*v*w
    return guard({k:v for k,v in z.items() if v})
def dagger(x):
    return {(m,p):v*(-1)**(p+m.bit_count()*(m.bit_count()-1)//2) for (m,p),v in x.items()}
def imag(x): return {(m,1-p):(-1)**p*v for (m,p),v in x.items()}
ONE={(0,0):F(1)}
def gamma(i):
    if type(i) is not int or not 0<=i<4096: raise ValueError('site cap')
    return {(1<<i,0):F(1)}
def advance(x,K,B):
    """D O Omega=([H0,O]+B O)Omega; [H0,gamma_j]=i sum_k K[k,j] gamma_k."""
    z=mul(B,x)
    for (mask,phase),coef in x.items():
        ids=[j for j in range(mask.bit_length()) if mask>>j&1]
        for pos,j in enumerate(ids):
            left=sum(1<<i for i in ids[:pos]);right=sum(1<<i for i in ids[pos+1:])
            for k,val in K.get(j,{}).items():
                word=mul(mul({(left,phase):coef},gamma(k)),{(right,0):F(1)})
                z=add(z,scale(imag(word),val))
    return z

def polynomial(coeff,source,K,B):
    if not 1<=len(coeff)<=7: raise ValueError('fixed degree cap6')
    out={};state=source
    for n,c in enumerate(coeff):
        out=add(out,scale(state,c))
        if n+1<len(coeff): state=advance(state,K,B)
    return out

def wick_expectation(kappa):
    """kappa(i,j)=<gamma_i gamma_j>/i for distinct ordered i<j.
    Exact reference covariance is an external scientific premise, not supplied here.
    """
    @lru_cache(maxsize=MAX_WICK_STATES)
    def pf(mask):
        COUNT['wick_states']+=1
        if COUNT['wick_states']>MAX_WICK_STATES: raise ValueError('Wick state cap')
        if not mask:return F(1)
        ids=[i for i in range(mask.bit_length()) if mask>>i&1]
        if len(ids)%2:return F(0)
        i=ids[0];ans=F(0)
        for pos,j in enumerate(ids[1:]):
            ans+=(-1)**pos*F(kappa(i,j))*pf(mask^(1<<i)^(1<<j))
        return ans
    def expect(x):
        ans=[F(0),F(0)]
        for (mask,p),v in x.items():
            if mask.bit_count()%2:continue
            r=mask.bit_count()//2;p+=r
            ans[p%2]+=(-1)**(p//2)*v*pf(mask)
        return tuple(ans)
    return expect

def inner(x,y,expect):return expect(mul(dagger(x),y))
def norm2(x,expect):
    re,im=inner(x,x,expect)
    if im or re<0:raise ValueError('invalid covariance/norm certificate')
    return re

def pair_vectors(K,B,J,p,q):
    u=polynomial(p,ONE,K,B)
    source=mul(J,u)
    v=polynomial(q,source,K,B)
    r=add(ONE,scale(advance(u,K,B),-1))
    t=add(source,scale(advance(v,K,B),-1))
    return {'x':scale(u,-1),'v':v,'r':r,'t':t}

def nominal(rows,ordered_edges,g,expect):
    value=F(0)
    for c,a in ordered_edges:
        value+=inner(rows[c]['x'],rows[a]['x'],expect)[0]
        value-=inner(rows[c]['x'],mul(g,rows[a]['v']),expect)[0]
    return value
