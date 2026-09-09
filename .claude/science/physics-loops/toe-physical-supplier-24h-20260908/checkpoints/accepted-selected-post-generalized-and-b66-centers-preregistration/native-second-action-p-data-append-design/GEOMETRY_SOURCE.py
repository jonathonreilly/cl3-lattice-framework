"""Three bare DATA sources only; exact-midpoint outward192 arithmetic, h=1."""
from fractions import Fraction as F
import interval as iv
ORBITS=((1,1,0),(1,0,0),(0,1,0),(0,0,2),(0,0,1))
PAIRS=(((1,2),(3,4)),((1,2),(3,5)),((1,3),(5,6)),((1,3),(2,4)),((1,3),(2,5)))
def geometry(orbit):
 a,c=PAIRS[ORBITS.index(tuple(orbit))]
 def d(ids):return (0,)+tuple((1 if j%2 else -1) if j in ids else 0 for j in range(1,7))
 return ((1,0,0,0,0,0,0),d(a),d(c)),(d(a),d(c),d(range(1,7)))
def bilinear(u,v):
 eye=sum(x*y for x,y in zip(u,v));opp=sum(u[j]*v[j+1 if j%2 else j-1] for j in range(1,7))
 skew=sum((1 if j%2 else -1)*(u[j]*v[0]-u[0]*v[j]) for j in range(1,7))
 return eye,opp,skew,eye+opp

def cross(kind,v,s,sigma,A,B,mu,orbit,balance):
 if kind not in range(3) or v not in range(3) or sigma not in(-1,1) or F(s)<=0:raise ValueError('labels')
 old,new=geometry(orbit);I,O,T,N=bilinear(new[kind],old[v])
 if balance[0]<=0:raise ValueError('positive balance')
 s,A,B,mu=map(iv.rational,(s,A,B,mu));s2=iv.mul(s,s)
 D=iv.scale(iv.sub(iv.ONE,iv.mul(s2,A)),F(1,6))
 g=iv.add(iv.scale(iv.mul(s,iv.sub(iv.scale(A,N),iv.scale(D,O))),sigma),iv.scale(D,T))
 j=iv.sub(iv.sub(iv.scale(B,N),iv.scale(iv.sub(mu,iv.mul(s2,B)),F(O,6))),iv.scale(iv.mul(s,B),F(sigma*T,6)))
 factor=iv.scale(balance,F(1,2));return iv.mul(factor,g),iv.mul(factor,j)

def insertion(kind,v,c,mu,orbit):
 if kind not in range(3) or v not in range(3):raise ValueError('labels')
 old,new=geometry(orbit);I,O,T,N=bilinear(new[kind],old[v])
 if v==0:j=iv.scale(iv.rational(mu),F(-T,24))
 else:j=iv.add(iv.scale(iv.rational(c),F(-N,4)),iv.scale(iv.rational(mu),F(O,24)))
 return iv.ZERO,j

def self_entry(i,j,orbit):
 if i not in range(3) or j not in range(3):raise ValueError('labels')
 _,new=geometry(orbit);return iv.rational(F(bilinear(new[i],new[j])[0],4)),iv.ZERO

def stream(poles,values,alpha,c,mu,emit,before):
 if len(poles)!=66 or len(values)!=66 or len(alpha)!=66:raise ValueError('fixed66')
 balances=[iv.sqrt(iv.rational(a)) for a in alpha];maximum=0;rows=entries=0;traces=[]
 def retain(row):
  nonlocal maximum,rows,entries
  emit(row);rows+=1;entries+=len(row['entries'])
  maximum=max(maximum,max(max(e[2]-e[1],e[4]-e[3]) for e in row['entries']))
  if 4*804*maximum>iv.S//2**60:raise ValueError('new append arithmetic bound')
 for oi,orbit in enumerate(ORBITS):
  for kind in range(3):
   for ni,s in enumerate(poles):
    for sigma in(-1,1):
     tag={'orbit_id':oi,'type':'bare_to_pole','append_index':399+kind,'pole_id':ni,'sigma':sigma};before(tag)
     es=[]
     for v in range(3):
      g,j=cross(kind,v,s,sigma,values[ni][0],values[ni][2],mu,orbit,balances[ni]);es.append([6*ni+(0 if sigma==-1 else 3)+v,*g,*j])
     retain({**tag,'entries':es})
   tag={'orbit_id':oi,'type':'bare_to_insertion','append_index':399+kind};before(tag)
   es=[]
   for v in range(3):
    g,j=insertion(kind,v,c,mu,orbit);es.append([396+v,*g,*j])
   retain({**tag,'entries':es})
  trace=iv.ZERO
  for i in range(3):
   tag={'orbit_id':oi,'type':'bare_self','append_index':399+i};before(tag);es=[]
   for j in range(i,3):
    g,z=self_entry(i,j,orbit);es.append([399+j,*g,*z])
    if i==j:trace=iv.add(trace,g)
   retain({**tag,'entries':es})
  traces.append(iv.scale(trace,2))
 return {'rows':rows,'entries':entries,'maximum_width':maximum,'append_arithmetic_radius':4*804*maximum,'denominator':iv.S,'append_closed_traces':traces}
