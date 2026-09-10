"""192-bit outward arithmetic around exact input midpoints. h=1, omega=1/4."""
from fractions import Fraction as F
import interval as iv
ORBITS=((1,1,0),(1,0,0),(0,1,0),(0,0,2),(0,0,1))
def geometry(orbit):
 if tuple(orbit) not in ORBITS:raise ValueError('orbit')
 oa,oc,k=orbit
 I=((1,0,0),(0,2,0),(0,0,2));O=((0,0,0),(0,-2*oa,-k),(0,-k,-2*oc));T=((0,-2,-2),(2,0,0),(2,0,0))
 return I,O,T,tuple(tuple(I[i][j]+O[i][j] for j in range(3)) for i in range(3))
def cross(kind,v,s,sigma,A,B,c,orbit,balance):
 if kind not in (0,1,2) or v not in (0,1,2) or sigma not in(-1,1) or F(s)<=0:raise ValueError('label')
 I,O,T,N=geometry(orbit);s=iv.rational(s);A=iv.rational(A);B=iv.rational(B);c=iv.rational(c)
 if balance[0]<=0:raise ValueError('balance')
 D=iv.scale(iv.sub(iv.ONE,iv.mul(iv.mul(s,s),A)),F(1,6))
 if kind==0:
  g=iv.add(iv.scale(iv.mul(s,A),sigma*I[0][v]),iv.scale(D,T[0][v]))
  j=iv.sub(iv.scale(B,I[0][v]),iv.scale(iv.mul(s,B),F(sigma*T[0][v],6)))
 else:
  g=iv.add(iv.neg(iv.sub(iv.scale(A,N[kind][v]),iv.scale(D,O[kind][v]))),iv.scale(iv.mul(s,A),F(sigma*T[kind][v],6)))
  j=iv.add(iv.scale(B,F(T[kind][v],6)),iv.scale(iv.sub(iv.scale(iv.div(iv.sub(c,B),s),N[kind][v]),iv.scale(iv.mul(s,B),F(O[kind][v],6))),sigma))
 factor=iv.scale(balance,F(1,2))
 return iv.mul(factor,g),iv.mul(factor,j)
def self_entry(i,j,a0,orbit):
 if i not in(0,1,2) or j not in(0,1,2):raise ValueError('label')
 I,O,T,N=geometry(orbit)
 if i==j==0:g=iv.ONE
 elif i==0 or j==0:g=iv.rational(F(1,3))
 else:g=iv.sub(iv.scale(iv.rational(a0),N[i][j]),iv.rational(F(O[i][j],6)))
 return iv.scale(g,F(1,4)),iv.ZERO

def stream(poles,values,alpha,a0,c,emit,before=None):
 """No I/O or loader. emit called BEFORE the width gate for each completed row."""
 if len(poles)!=66 or len(values)!=66 or len(alpha)!=66:raise ValueError('fixed66')
 balances=[iv.sqrt(iv.rational(a)) for a in alpha]
 max_width=0;entries=0;rows=0;traces=[]
 for oi,orbit in enumerate(ORBITS):
  for kind in range(3):
   for ni,s in enumerate(poles):
    for sigma in(-1,1):
     if before:before({'orbit_id':oi,'type':'append_to_pole','append_index':396+kind,'pole_id':ni,'sigma':sigma})
     es=[]
     for v in range(3):
      g,j=cross(kind,v,s,sigma,values[ni][0],values[ni][2],c,orbit,balances[ni]);es.append([ni*6+(0 if sigma==-1 else 3)+v,*g,*j])
     row={'orbit_id':oi,'type':'append_to_pole','append_index':396+kind,'pole_id':ni,'sigma':sigma,'entries':es}
     emit(row);rows+=1;entries+=3
     max_width=max(max_width,max(max(e[2]-e[1],e[4]-e[3]) for e in es))
     if 4*798*max_width>iv.S//2**60:raise ValueError('append arithmetic width')
  trace=iv.ZERO
  for i in range(3):
   if before:before({'orbit_id':oi,'type':'append_self','append_index':396+i})
   es=[]
   for j in range(i,3):
    g,z=self_entry(i,j,a0,orbit);es.append([396+j,*g,*z])
    if i==j:trace=iv.add(trace,g)
   emit({'orbit_id':oi,'type':'append_self','append_index':396+i,'entries':es});rows+=1;entries+=len(es)
   max_width=max(max_width,max(max(e[2]-e[1],e[4]-e[3]) for e in es))
   if 4*798*max_width>iv.S//2**60:raise ValueError('self arithmetic width')
  traces.append(iv.scale(trace,2))
 return {'entries':entries,'rows':rows,'maximum_width':max_width,'append_closed_traces':traces,'denominator':iv.S,'append_arithmetic_radius':4*798*max_width,'radius_denominator':iv.S}
