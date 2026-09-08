"""No top-level random execution. Supplied CT model and finite readouts."""
from pathlib import Path
from fractions import Fraction
import json,math
from geometry import FrozenGeometry
from verified_path import Trajectory
from conditional import Conditional,draw
NAMES=('mid_NF','mid_X1','mid_X2','mid_X1_square','mid_X2_square','endpoint_h','hL_hR','mid_X1_endpoint_h','mid_X2_endpoint_h','time_average_NF','endpoint_overlap','physical_event_count','hamming_activity_per_time','electric_corner_intensity','plane_anisotropy')

class Adapter:
 def __init__(self,L,V=.95):
  if isinstance(V,bool) or not math.isfinite(float(V)):raise ValueError('finite V')
  self.V=Fraction(str(V))
  if not 0<=self.V<=1 or L not in (2,4):raise ValueError('declared adapter domain')
  self.g=FrozenGeometry(L);self.harmonics=(1,) if L==2 else (1,2)
 def seed(self,T):return Trajectory(self.g,self.g.seed,[],float(T),[])
 def propagated(self,T,face_choices,clock_values,burn_sweeps=128,max_clock_events=4096):
  if type(burn_sweeps) is not int or burn_sweeps<0 or type(max_clock_events) is not int or max_clock_events<=0:raise ValueError('initializer caps')
  T=float(T)
  if not math.isfinite(T) or T<=0:raise ValueError('initializer time')
  faces=iter(face_choices);clocks=iter(clock_values);g=self.g;x=g.seed;witness=[]
  def face():
   try:p=next(faces)
   except StopIteration:raise ValueError('initializer face tape exhausted') from None
   if type(p) is not int or not 0<=p<g.M:raise ValueError('initializer face label')
   return p
  for _ in range(burn_sweeps*g.M):
   p=face()
   if g.legal(x,p):x^=g.masks[p];witness.append(p)
  initial=x;events=[];elapsed=0.;clock_count=0
  while True:
   if clock_count>=max_clock_events:raise ValueError('whole initializer clock cap')
   try:u=next(clocks)
   except StopIteration:raise ValueError('initializer clock tape exhausted') from None
   if not math.isfinite(u) or not 0<u<1:raise ValueError('initializer clock domain')
   dt=-math.log(u)/g.M;clock_count+=1;nxt=elapsed+dt
   if not elapsed<nxt:raise ValueError('initializer positive clock')
   if nxt==T:raise ValueError('initializer boundary clock')
   if nxt>T:break
   p=face()
   if g.legal(x,p):events.append((nxt,p));x^=g.masks[p]
   elapsed=nxt
  path=Trajectory(g,initial,events,T,witness)
  return path,{'rk_sweeps':burn_sweeps,'rk_proposals':burn_sweeps*g.M,'clock_draws':clock_count,'physical_events':len(events),'scope':'finite RK preparation followed by RK CT path; not detuned stationary initialization'}
 def block(self,path,p,values,maxevents=4096,tol=1e-12):
  if path.g is not self.g:raise ValueError('geometry owner')
  return draw(Conditional(path,p,float(self.V)),values,maxevents=maxevents,tol=tol)
 def sources(self,x):
  g=self.g;v=g.L**3;result=[]
  for h in self.harmonics:
   total=0
   for a in range(3):
    for b in range(3):
     if a==b:continue
     re=im=0
     for e,(r,c) in enumerate(g.links):
      if c!=b:continue
      # L2/L4 phases are exact fourth roots of unity.
      phase=(2*h*r[a]//g.L)%4;sgn=(-1)**sum(r)*(2*((x>>e)&1)-1)
      re+=sgn*(1,0,-1,0)[phase];im+=sgn*(0,1,0,-1)[phase]
     total+=re*re+im*im
   result.append(Fraction(total,4*v))
  return result
 def measure(self,path):
  if path.g is not self.g:raise ValueError('geometry owner')
  g=self.g;x=path.initial;mid=x;integral=0.;last=0.;T=path.T
  for t,p in path.events:
   integral+=(t-last)*g.nf(x);x^=g.masks[p]
   if t<=T/2:mid=x
   last=t
  integral+=(T-last)*g.nf(x);NF=g.nf(mid);hL=float((self.V-1)*g.nf(path.initial));hR=float((self.V-1)*g.nf(x));E=(hL+hR)/2
  source=self.sources(mid);X1=float(source[0]);X2=float(source[1]) if len(source)==2 else X1
  v=g.L**3;overlap=sum((2*((path.initial>>e)&1)-1)*(2*((x>>e)&1)-1) for e in range(g.E))/g.E
  corner=sum(sum(2*((mid>>e)&1)-1 for e,(r,c) in enumerate(g.links) if c==a)**2 for a in range(3))/(4*v*v)
  planes=[sum(g.legal(mid,p) for p in range(a*v,(a+1)*v)) for a in range(3)];aniso=(3*sum(n*n for n in planes)-NF*NF)/(3*v*v)
  values=[NF,X1,X2,X1*X1,X2*X2,E,hL*hR,X1*E,X2*E,integral/T,overlap,len(path.events),4*len(path.events)/(3*v*T),corner,aniso]
  if not all(math.isfinite(z) for z in values):raise ValueError('finite measurement')
  if g.L==2:
   names=('mid_NF','mid_X','mid_X2','endpoint_h','hL_hR','mid_X_endpoint_h','time_average_NF','endpoint_overlap','physical_event_count','hamming_activity_per_time','electric_corner_intensity','plane_anisotropy')
   return dict(zip(names,[values[i] for i in (0,1,3,5,6,7,9,10,11,12,13,14)]))
  return dict(zip(NAMES,values))
 def balance(self,values,T):return float(self.V)*values['time_average_NF']-values['physical_event_count']/T-values['endpoint_h']
 def save(self,path,file):
  path.full_check();z={'L':self.g.L,'V':str(self.V),'T':path.T.hex(),'initial':hex(path.initial),'events':[[t.hex(),p] for t,p in path.events],'witness':path.witness}
  f=Path(file)
  if f.exists():raise ValueError('no overwrite')
  f.write_text(json.dumps(z,separators=(',',':'))+'\n')
 def load(self,file):
  z=json.loads(Path(file).read_text())
  if set(z)!={'L','V','T','initial','events','witness'} or z['L']!=self.g.L or z['V']!=str(self.V):raise ValueError('checkpoint domain')
  return Trajectory(self.g,int(z['initial'],16),[(float.fromhex(t),p) for t,p in z['events']],float.fromhex(z['T']),z['witness'])
