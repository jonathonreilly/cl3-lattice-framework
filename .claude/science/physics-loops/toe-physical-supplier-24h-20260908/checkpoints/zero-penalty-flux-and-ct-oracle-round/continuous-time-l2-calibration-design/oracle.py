"""Exact integer/rational truncated-uniformization oracle; no RNG."""
from fractions import Fraction as F
import math,json,pathlib,time,resource,sys,signal
from geometry_reference import Geometry
BPATH=pathlib.Path(__file__).resolve().parent
NTEST=0
def need(c,msg):
 global NTEST
 NTEST+=1
 if not c:raise ValueError(msg)
def frac(x):return dict(numerator=str(x.numerator),denominator=str(x.denominator),float=float(x))
def cap(T):
 x=24*T;lam=x*F(21,20);J=math.ceil(x)+64
 lower=sum((x**j/F(math.factorial(j)) for j in range(J+1)),F(0))
 k=math.floor(lam)
 while True:
  tail=lam**(k+1)/F(math.factorial(k+1))/(1-lam/F(k+2))/lower
  if tail<=F(1,10**14):break
  k+=1
 moment=lam*lam**k/F(math.factorial(k))/(1-lam/F(k+1))/lower
 return k,tail,moment,dict(x=str(x),lambda_bound=str(lam),exp_lower_degree=J,exp_lower=frac(lower))
def component():
 g=Geometry(2);need(g.M==24 and len(g.by_mask)==24,'unique native masks');states=[g.seed];seen={g.seed:0};parent=[None];label=[None]
 for x in states:
  for p in range(g.M):
   if g.legal(x,p):
    y=x^g.masks[p]
    if y not in seen:seen[y]=len(states);states.append(y);parent.append(seen[x]);label.append(p)
 need(len(states)==864,'component864')
 nf=[g.nf(x) for x in states];neighbors=[[seen[x^g.masks[p]] for p in range(g.M) if g.legal(x,p)] for x in states]
 diag=[480-19*k for k in nf]
 for i,ns in enumerate(neighbors):
  need(all(i in neighbors[j] for j in ns),'symmetric adjacency');need(480<=diag[i]+20*len(ns)<=504,'row bounds');g.validate(states[i])
 xs=[];signs=[]
 for x in states:
  total=0
  for a in range(3):
   for b in range(3):
    if a!=b:
     z=sum((-1)**(sum(r)+r[a])*(2*((x>>e)&1)-1) for e,(r,c) in enumerate(g.links) if c==b);total+=z*z
  xs.append(total);signs.append([2*((x>>e)&1)-1 for e in range(g.E)])
 need(all(0<=z<=384 for z in xs),'X<=12')
 return g,states,nf,neighbors,diag,xs,signs,parent,label

def apply(v,neighbors,diag):return [d*v[i]+20*sum(v[j] for j in ns) for i,(d,ns) in enumerate(zip(diag,neighbors))]
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def main():
 g,states,nf,ns,diag,xs,signs,parent,label=component();caps={str(T):cap(T) for T in (F(1,2),F(2))};K=max(z[0] for z in caps.values())
 h=[[1]*864];hn=[nf.copy()]
 for k in range(K):h.append(apply(h[-1],ns,diag));hn.append(apply(hn[-1],ns,diag))
 sums=[sum(v) for v in h]
 # Exact all-time insertion coefficients and binomial midpoint coefficients.
 Fn=[];midNF=[];midX=[];midX2=[];midXN=[]
 for k in range(K+1):
  f=a=b=c=d=0
  for j in range(k+1):
   left=h[j];right=h[k-j];weighted=math.comb(k,j)
   nn=xx=xx2=xn=0
   for i,(u,v) in enumerate(zip(left,right)):
    uv=u*v;nn+=uv*nf[i];xx+=uv*xs[i];xx2+=uv*xs[i]*xs[i];xn+=hn[j][i]*v*xs[i]
   f+=nn;a+=weighted*nn;b+=weighted*xx;c+=weighted*xx2;d+=weighted*xn
   need(dot(left,right)==sums[k],'exact midpoint normalization per split')
  Fn.append(f);midNF.append(a);midX.append(b);midX2.append(c);midXN.append(d)
 # All24 endpoint spin-pair insertions, no symmetry import.
 overlap=[0]*(K+1)
 for e in range(g.E):
  z=[row[e] for row in signs];v=z.copy()
  for k in range(K+1):
   overlap[k]+=dot(z,v)
   if k<K:v=apply(v,ns,diag)
 results=[]
 for T in (F(1,2),F(2)):
  kmax,tv,tailmoment,info=caps[str(T)];Dden=20/T;need(Dden.denominator==1,'rational uniformization scale');Dden=int(Dden)
  coeff=[Dden**(kmax-k)*math.factorial(kmax)//math.factorial(k) for k in range(kmax+1)]
  weights=[c*sums[k] for k,c in enumerate(coeff)];Z=sum(weights);two=2**kmax
  common=two*Z
  calc=lambda vec:F(sum(coeff[k]*2**(kmax-k)*vec[k] for k in range(kmax+1)),common)
  moments={
   'mid_NF':calc(midNF), 'mid_X':calc(midX)/32, 'mid_X2':calc(midX2)/1024,
   'endpoint_h':-F(sum(coeff[k]*dot(nf,h[k]) for k in range(kmax+1)),20*Z),
   'hL_hR':F(sum(coeff[k]*dot(nf,hn[k]) for k in range(kmax+1)),400*Z),
   'mid_X_endpoint_h':-calc(midXN)/640,
   'time_average_NF':sum((F(coeff[k]*Fn[k],k+1) for k in range(kmax+1)),F(0))/Z,
   'endpoint_overlap':F(sum(coeff[k]*overlap[k] for k in range(kmax+1)),24*Z)}
  eventcoeff=[0]+[k*sums[k]-480*k*sums[k-1]+19*Fn[k-1] for k in range(1,kmax+1)]
  need(all(z>=0 for z in eventcoeff),'nonnegative event coefficient')
  mean_events=F(sum(coeff[k]*eventcoeff[k] for k in range(kmax+1)),Z)
  moments['physical_event_count']=mean_events;moments['hamming_activity_per_time']=mean_events/(6*T)
  ranges={'mid_NF':F(24),'mid_X':F(12),'mid_X2':F(144),'endpoint_h':F(6,5),'hL_hR':F(36,25),'mid_X_endpoint_h':F(72,5),'time_average_NF':F(24),'endpoint_overlap':F(2)}
  errors={name:tv*span for name,span in ranges.items()};errors['physical_event_count']=tailmoment+tv*mean_events;errors['hamming_activity_per_time']=errors['physical_event_count']/(6*T)
  need(sum(F(w,Z) for w in weights)==1,'count law normalizes')
  need(moments['mid_X']>0,'nonzero source norm')
  results.append(dict(T_total=str(T),midpoint_projection_time=str(T/2),K=kmax,TV_upper=frac(tv),count_tail_moment_upper=frac(tailmoment),cap_derivation=info,moments={name:frac(z) for name,z in moments.items()},absolute_CT_truncation_error_upper={name:frac(z) for name,z in errors.items()},count_weights_integer=[str(w) for w in weights],count_normalizer_integer=str(Z)))
 # Retain exact backward columns and deterministic BFS witnesses for future initializer review.
 (BPATH/'BACKWARD_POWERS.json').write_text(json.dumps(dict(states=states,parents=parent,parent_face=label,h=h,h_NF=hn,diag=diag,neighbors=ns),separators=(',',':')))
 return dict(checks=NTEST,dimension=864,geometric_faces=24,Kmax=K,V='19/20',targets=results,scope='exact rational finite-cutoff targets with analytic CT tail bounds; no stochastic execution')
if __name__=='__main__':
 signal.signal(signal.SIGALRM,lambda *_:(_ for _ in ()).throw(TimeoutError('180s')));signal.alarm(180);t=time.monotonic();r=main();r['seconds']=time.monotonic()-t;r['rss_mib']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024);need(r['rss_mib']<=384,'RSS');r['checks']=NTEST;print(json.dumps(r,indent=2))
