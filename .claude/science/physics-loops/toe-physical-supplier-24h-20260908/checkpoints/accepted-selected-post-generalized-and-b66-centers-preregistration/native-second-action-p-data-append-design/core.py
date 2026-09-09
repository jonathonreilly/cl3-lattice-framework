"""New p DATA only. No loader, index, oracle or full old-entry builder."""
from fractions import Fraction as F
from math import isqrt
S=1<<192;CAP=4096
ORBITS=((1,1,0),(1,0,0),(0,1,0),(0,0,2),(0,0,1))
PAIRS=(((1,2),(3,4)),((1,2),(3,5)),((1,3),(5,6)),((1,3),(2,4)),((1,3),(2,5)))
def box(x):
 if len(x)!=2 or any(type(v)is not int or abs(v).bit_length()>CAP for v in x)or x[0]>x[1]:raise ValueError('endpoint cap/order')
 return tuple(x)
def rational(x):
 x=F(x)
 if max(abs(x.numerator).bit_length(),x.denominator.bit_length())>512:raise ValueError('rational input cap')
 a=x.numerator*S;b=x.denominator;return box((a//b,-((-a)//b)))
def add(a,b):return box((a[0]+b[0],a[1]+b[1]))
def neg(a):return(-a[1],-a[0])
def mul(a,b):
 a=box(a);b=box(b);z=[x*y for x in a for y in b];return box((min(z)//S,-((-max(z))//S)))
def scale(a,x):return mul(a,rational(x))
def sqrt(x):
 x=box(x)
 if x[0]<=0:raise ValueError('positive alpha')
 a=isqrt(x[0]*S);b=isqrt(x[1]*S);return box((a,b+(b*b<x[1]*S)))
def geometry(orbit):
 a,c=PAIRS[ORBITS.index(tuple(orbit))]
 def d(ids):return(0,)+tuple((1 if j%2 else-1)if j in ids else 0 for j in range(1,7))
 return ((1,0,0,0,0,0,0),d(a),d(c)),(d(a),d(c),d(range(1,7)))
def form(u,v):
 I=sum(a*b for a,b in zip(u,v));O=sum(u[j]*v[j+1 if j%2 else j-1]for j in range(1,7));T=sum((1 if j%2 else-1)*(u[j]*v[0]-u[0]*v[j])for j in range(1,7));return I,O,T,I+O

def pole(u,v,s,sigma,balance,mu,qentry,orbit):
 if type(u)is not int or type(v)is not int or u not in range(3)or v not in range(3)or type(sigma)is not int or sigma not in(-1,1)or F(s)<=0:raise ValueError('label')
 old,new=geometry(orbit);I,O,T,N=form(new[u],old[v]);g,j=map(box,qentry)
 G=add(scale(g,-sigma*F(s)),scale(balance,F(I,2)))
 J=add(scale(j,-sigma*F(s)),scale(mul(balance,rational(mu)),F(-T,12)))
 return G,J

def ward(u,v,orbit):
 _,new=geometry(orbit);f=(2,0,1)[v];I,*_=form(new[u],new[f]);return rational(F(-I,4)),(0,0)
def qpair(u,v,mu,nu,orbit):
 _,new=geometry(orbit);I,O,T,N=form(new[u],new[v]);return(0,0),add(scale(rational(mu),F(-N,4)),scale(rational(nu),F(O,24)))
def selfpair(u,v,orbit):
 _,new=geometry(orbit);I,O,T,N=form(new[u],new[v]);return rational(F(6*I-O,4)),(0,0)

def stream(poles,alpha,mu,nu,q_saved,emit,before,old_maximum_width):
 """q_saved reads authenticated saved ARITHMETIC q-to-pole rows; no reevaluation.
 Old mu midpoint must exactly match those rows. emit serializes before return.
 """
 if len(poles)!=66 or len(alpha)!=66 or type(old_maximum_width)is not int or old_maximum_width<0:raise ValueError('fixed family')
 if any(F(x)<=0 for x in poles)or len(set(map(F,poles)))!=66:raise ValueError('pole family')
 balances=[sqrt(rational(a))for a in alpha];maximum=old_maximum_width;rows=entries=reads=0;traces=[]
 def retain(tag,es):
  nonlocal rows,entries,maximum
  emit({**tag,'entries':es});rows+=1;entries+=len(es)
  maximum=max(maximum,max(max(e[2]-e[1],e[4]-e[3])for e in es))
  if 4*810*maximum>S//2**60:raise ValueError('combined810 arithmetic bound')
 for oi,orbit in enumerate(ORBITS):
  for u in range(3):
   for n,s in enumerate(poles):
    for sigma in(-1,1):
     tag={'orbit_id':oi,'type':'p_to_pole','append_index':402+u,'pole_id':n,'sigma':sigma};before(tag);es=[]
     for v in range(3):
      saved=q_saved(oi,u,n,sigma,v);reads+=1
      g,j=pole(u,v,s,sigma,balances[n],mu,saved,orbit);es.append([6*n+(0 if sigma==-1 else 3)+v,*g,*j])
     retain(tag,es)
   for kind,offset,func in [('p_to_ward',396,lambda v:ward(u,v,orbit)),('p_to_q',399,lambda v:qpair(u,v,mu,nu,orbit))]:
    tag={'orbit_id':oi,'type':kind,'append_index':402+u};before(tag);es=[]
    for v in range(3):g,j=func(v);es.append([offset+v,*g,*j])
    retain(tag,es)
  trace=(0,0)
  for u in range(3):
   tag={'orbit_id':oi,'type':'p_self','append_index':402+u};before(tag);es=[]
   for v in range(u,3):
    g,j=selfpair(u,v,orbit);es.append([402+v,*g,*j])
    if u==v:trace=add(trace,scale(g,2))
   retain(tag,es)
  if trace[1]>35*S:raise ValueError('new closed trace35')
  traces.append(trace)
 if(rows,entries,reads)!=(2025,6060,5940):raise ValueError('fixed census')
 return {'status':'COMPLETE_P_DATA_ARITHMETIC_ONLY','rows':rows,'entries':entries,'saved_q_reads':reads,'closed_rows':810,'raw_rows':405,'trial_unchanged':True,'original_trial_raw_rows':399,'append_closed_traces':traces,'prior_trace_strict_upper':536,'combined_trace_strict_upper':571,'maximum_integer_width':maximum,'combined_arithmetic_radius_numerator':4*810*maximum,'denominator':S,'oracle_calls':0,'old_entry_reevaluations':0}

def physical_radius(kind,u,v,orbit,*,etaA,etaB,eta_mu,eta_nu,s=F(1),balance_upper=F(1)):
 """Independent physical inflation; no old arithmetic-width subtraction."""
 vals=list(map(F,(etaA,etaB,eta_mu,eta_nu,s,balance_upper)))
 if any(x<0 for x in vals)or vals[4]<=0 or vals[5]<=0:raise ValueError('physical radius input')
 if vals[0]>F(1,10**30)or any(x>F(1,10**19)for x in vals[1:4]):raise ValueError('inherited scalar precision')
 etaA,etaB,eta_mu,eta_nu,s,balance_upper=vals
 old,new=geometry(orbit)
 if kind=='pole':
  I,O,T,N=form(new[u],old[v]);ans=(s*2800*etaA,s*(176*etaB+eta_mu)+balance_upper*abs(T)*eta_mu/12)
 elif kind=='q':
  I,O,T,N=form(new[u],new[v]);ans=(F(0),abs(N)*eta_mu/4+abs(O)*eta_nu/24)
 elif kind in('ward','self'):ans=(F(0),F(0))
 else:raise ValueError('radius kind')
 for x in ans:
  if max(abs(x.numerator).bit_length(),x.denominator.bit_length())>4096:raise ValueError('physical radius bit cap')
 return ans
