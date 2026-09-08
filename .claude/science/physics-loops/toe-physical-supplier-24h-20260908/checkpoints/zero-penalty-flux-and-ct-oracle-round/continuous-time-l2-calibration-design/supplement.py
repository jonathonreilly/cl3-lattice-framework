import json,pathlib,math
from fractions import Fraction as F
from geometry_reference import Geometry
B=pathlib.Path(__file__).resolve().parent
r=json.loads((B/'ORACLE.json').read_text());raw=json.loads((B/'BACKWARD_POWERS.json').read_text());g=Geometry(2);h=raw['h'];nf=raw['h_NF'][0];states=raw['states'];N=0
parse=lambda z:F(int(z['numerator']),int(z['denominator']))
def need(c,msg):
 global N
 N+=1
 if not c:raise ValueError(msg)
xs=[]
for x in states:
 xs.append(sum(sum((-1)**(sum(q)+q[a])*(2*((x>>e)&1)-1) for e,(q,c) in enumerate(g.links) if c==b)**2 for a in range(3) for b in range(3) if a!=b))
corner=[];aniso=[]
for x in states:
 corner.append(sum(sum(2*((x>>e)&1)-1 for e,(r,c) in enumerate(g.links) if c==a)**2 for a in range(3)))
 counts=[sum(g.legal(x,p) for p in range(a*8,(a+1)*8)) for a in range(3)]
 aniso.append(3*sum(k*k for k in counts)-sum(counts)**2)
 need(0<=corner[-1]<=192 and 0<=aniso[-1]<=128,'bounded order readouts')
outputs=[]
for row in r['targets']:
 T=F(row['T_total']);K=row['K'];delta=parse(row['TV_upper']);Dden=int(40/T)
 coeff=[Dden**(K-k)*math.factorial(K)//math.factorial(k) for k in range(K+1)]
 psi=[sum(c*h[k][i] for k,c in enumerate(coeff)) for i in range(864)];norm=sum(x*x for x in psi)
 midNF=F(sum(x*x*n for x,n in zip(psi,nf)),norm);midX=F(sum(x*x*s for x,s in zip(psi,xs)),32*norm)
 target={k:parse(v) for k,v in row['moments'].items()};err={k:parse(v) for k,v in row['absolute_CT_truncation_error_upper'].items()}
 need(abs(midNF-target['mid_NF'])<=48*delta,'half-time NF independent truncation');need(abs(midX-target['mid_X'])<=24*delta,'half-time X independent truncation')
 residual=target['physical_event_count']-T*(F(19,20)*target['time_average_NF']-target['endpoint_h'])
 need(abs(residual)<=err['physical_event_count']+T*(F(19,20)*err['time_average_NF']+err['endpoint_h']),'CT energy/count identity bounded truncation')
 # Exact ratio intervals, no fitted numerical threshold.
 def box(k):return (target[k]-err[k],target[k]+err[k])
 def add(a,b):return (a[0]+b[0],a[1]+b[1])
 def neg(a):return (-a[1],-a[0])
 def scale(a,c):return (min(c*a[0],c*a[1]),max(c*a[0],c*a[1]))
 def divide(a,b):
  need(b[0]>0,'positive denominator bound');z=[x/y for x in a for y in b];return(min(z),max(z))
 S=target['mid_X'];E=target['endpoint_h'];D=(F(19,20)*target['mid_NF']-E)/(2*S);C=target['mid_X_endpoint_h']/S-E;R=D+C
 Db=scale(divide(add(scale(box('mid_NF'),F(19,20)),neg(box('endpoint_h'))),box('mid_X')),F(1,2))
 Cb=add(divide(box('mid_X_endpoint_h'),box('mid_X')),neg(box('endpoint_h')));Rb=add(Db,Cb)
 outputs.append(dict(T_total=str(T),D=float(D),correction=float(C),R=float(R),D_interval=[float(z) for z in Db],correction_interval=[float(z) for z in Cb],R_interval=[float(z) for z in Rb],D_interval_rational=[str(z) for z in Db],correction_interval_rational=[str(z) for z in Cb],R_interval_rational=[str(z) for z in Rb],half_polynomial_order_reference={'electric_corner_intensity':str(F(sum(z*z*v for z,v in zip(psi,corner)),256*norm)),'plane_anisotropy':str(F(sum(z*z*v for z,v in zip(psi,aniso)),192*norm))},order_CT_error_upper={'electric_corner_intensity':str(F(3,4)*delta),'plane_anisotropy':str(F(2,3)*delta)},scope='bounds account uniformization truncation only; displayed floats are rounded'))
# Literal conditional k2 path: initial probability and two label transitions telescope.
i=0;p=next(p for p in range(g.M) if g.legal(states[i],p));j=states.index(states[i]^g.masks[p]);Z2=sum(h[2])
prob=F(h[2][i],Z2)*F(20*h[1][j],h[2][i])*F(raw['diag'][j],h[1][j])
need(prob==F(20*raw['diag'][j],Z2),'stationary integer path telescopes')
print(json.dumps(dict(checks=N,derived_targets=outputs,scope='deterministic independent-half-vector and exact interval controls'),indent=2))
