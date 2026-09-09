"""Source-only shared native kernel candidate; no automatic physical driver."""
from fractions import Fraction as F
import interval as iv
import core
TYPES=('cc','cd','P','O','cross')
ORBITS=((1,1,0),(1,0,0),(0,1,0),(0,0,2),(0,0,1))
def endpoint(s,sig,values,typ):
 if typ not in TYPES:raise ValueError('type')
 if typ!='cross':
  C,Cp,L,Lp=core.coefficients(s,sig,values,'O' if typ=='O' else 'P')
  a,b=(0,0) if typ=='cc' else ((0,1) if typ=='cd' else (1,1))
  return C[a][b],Cp[a][b],L[a][b],Lp[a][b]
 A,Ap,B,Bp=map(iv.rational,values);z=iv.rational(s);zz=iv.mul(z,z)
 D=iv.scale(iv.sub(iv.ONE,iv.mul(zz,A)),F(1,6));Dp=iv.scale(iv.neg(iv.add(iv.scale(iv.mul(z,A),2),iv.mul(zz,Ap))),F(1,6))
 d=iv.sub(D,A);dp=iv.sub(Dp,Ap);fac=iv.add(iv.ONE,iv.scale(zz,F(1,6)))
 return iv.scale(iv.mul(z,d),sig),iv.scale(iv.add(d,iv.mul(z,dp)),sig),iv.mul(B,fac),iv.add(iv.mul(Bp,fac),iv.scale(iv.mul(z,B),F(1,3)))
def pair(i,j,labels,ends,typ):
 ni,s,sig=labels[i];nj,t,tau=labels[j];den=sig*s+tau*t
 a=ends[ni,-sig,typ];b=ends[nj,tau,typ]
 if den:g=iv.div(iv.sub(b[0],a[0]),iv.rational(den));z=iv.neg(iv.div(iv.sub(b[2],a[2]),iv.rational(den)))
 else:g=iv.scale(b[1],tau);z=iv.scale(b[3],-tau)
 if typ!='cd' and i==j:z=iv.ZERO
 return g,z

def key(i,j,typ):
 if typ not in TYPES:raise ValueError('type')
 if typ=='cd' or i<=j:return (typ,i,j),False
 return (typ,j,i),True

def reconstruct(fetch,i,j,a,b,orbit):
 """fetch(type,i,j) returns stored canonical G/J; source a,b in0..2."""
 if orbit not in ORBITS or a not in range(3) or b not in range(3):raise ValueError('selector')
 oa,oc,k=orbit;factor=1;transpose=False
 if a==b:typ='cc' if a==0 else ('O' if (oa if a==1 else oc) else 'P')
 elif a==0:typ='cd'
 elif b==0:typ='cd';i,j=j,i;transpose=True
 else:
  if not k:return iv.ZERO,iv.ZERO
  typ='cross';factor=k
 token,swapped=key(i,j,typ);g,z=fetch(*token)
 if transpose!=swapped:z=iv.neg(z)
 return iv.scale(g,factor),iv.scale(z,factor)

def stream(poles,values,alpha,write):
 """Explicit caller only. Arithmetic midpoint inputs, not physical error enclosures.
 write receives each completed row immediately; caller owns failure retention/caps.
 """
 if len(poles)!=len(values) or len(alpha)!=len(poles) or not poles:raise ValueError('length')
 if any(s<=0 for s in poles) or len(set(poles))!=len(poles):raise ValueError('poles')
 if any(x<=0 for x in alpha):raise ValueError('balance')
 labels=[(n,s,sig) for n,s in enumerate(poles) for sig in (-1,1)]
 ends={(n,sig,t):endpoint(s,sig,values[n],t) for n,s in enumerate(poles) for sig in(-1,1) for t in TYPES}
 roots=[iv.sqrt(iv.rational(x)) for x in alpha];count=0;maxwidth=0
 for typ in TYPES:
  for i in range(len(labels)):
   entries=[]
   for j in range(0 if typ=='cd' else i,len(labels)):
    g,z=pair(i,j,labels,ends,typ);bal=iv.mul(roots[labels[i][0]],roots[labels[j][0]])
    g,z=iv.mul(g,bal),iv.mul(z,bal);maxwidth=max(maxwidth,iv.width(g),iv.width(z));entries.append([j,*g,*z]);count+=1
   write({'type':typ,'i':i,'entries':entries,'count':count,'max_width':maxwidth})
 # k=2 reconstruction doubles widths; complete396-row G/J block bound is conservative.
 radius=F(2*792*maxwidth,iv.S)
 if radius>F(1,2**60):raise ValueError('common matrix arithmetic radius')
 return {'entries':count,'raw_rows':3*len(labels),'closed_rows':6*len(labels),'arithmetic_radius':str(radius),'physical_error_ledger':'separate and required'}
