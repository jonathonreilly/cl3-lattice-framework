"""Source-only exact midpoint append formulas, h=1; no native data loader."""
from fractions import Fraction as F
SCALE=F(1,2) # sqrt(omega), omega=1/4

def geometry(oA,oC,k):
    if (oA,oC,k) not in ((1,1,0),(1,0,0),(0,1,0),(0,0,2),(0,0,1)):
        raise ValueError('unsupported ordered orbit')
    I=((1,0,0),(0,2,0),(0,0,2))
    O=((0,0,0),(0,-2*oA,-k),(0,-k,-2*oC))
    T=((0,-2,-2),(2,0,0),(2,0,0))
    N=tuple(tuple(I[i][j]+O[i][j] for j in range(3)) for i in range(3))
    return I,O,T,N

def appended_to_pole(kind,v,s,sigma,A,B,c,orbit,balance=F(1)):
    """Return <x,y>,<x,Gamma y>; x=(e0,wA,wC)/2, y=balance*(-iR)v.
    Caller supplies certified scalar intervals in a future interval adapter.
    Here inputs are exact rational midpoints; returned values are NOT intervals.
    """
    if kind not in (0,1,2) or v not in (0,1,2) or sigma not in (-1,1):
        raise ValueError('label')
    s,A,B,c,balance=map(F,(s,A,B,c,balance))
    if s<=0 or balance<=0: raise ValueError('positive pole/balance')
    I,O,T,N=geometry(*orbit);D=(1-s*s*A)/6
    if kind==0:
        g=sigma*s*A*I[0][v]+D*T[0][v]
        j=B*I[0][v]-sigma*s*B*T[0][v]/6
    else:
        g=-(A*N[kind][v]-D*O[kind][v])+sigma*s*A*T[kind][v]/6
        j=B*T[kind][v]/6+sigma*((c-B)*N[kind][v]/s-s*B*O[kind][v]/6)
    return SCALE*balance*g,SCALE*balance*j

def appended_pair(i,j,a0,orbit):
    if i not in (0,1,2) or j not in (0,1,2):raise ValueError('label')
    I,O,T,N=geometry(*orbit)
    g=F(1) if i==j==0 else F(1,3) if (i==0 or j==0) else F(a0)*N[i][j]-F(1,6)*O[i][j]
    return SCALE*SCALE*g,F(0)

def native_append(*args,**kwargs):
    raise RuntimeError('UNLAUNCHED: no native append or interval adapter authorized')
