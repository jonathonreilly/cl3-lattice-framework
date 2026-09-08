import cmath,math

def measure(obj):
 g=obj.g;states=obj.states;n=len(states)-1;mid=states[n//2];volume=g.L**3
 S=[]
 for h in ((1,) if g.L==2 else (1,2)):
  amplitudes=[]
  for a in range(3):
   for b in range(3):
    if a!=b:
     amplitudes.append(sum((-1)**sum(r)*(((mid>>e)&1)-.5)*cmath.exp(2j*math.pi*h*r[a]/g.L)/math.sqrt(volume) for e,(r,c) in enumerate(g.links) if c==b))
  S.append(sum(abs(z)**2 for z in amplitudes))
 result=dict(mid_nf=obj.nf[n//2],endpoint_nf=(obj.nf[0]+obj.nf[-1])/2,average_nf=sum(obj.nf)/(n+1),endpoint_overlap=1-2*(states[0]^states[-1]).bit_count()/g.E,temporal_activity=sum((a^b).bit_count() for a,b in zip(states,states[1:]))/(g.E*n),S=S,total_nf=sum(obj.nf))
 if any(not math.isfinite(float(z)) for z in [result[k] for k in result if k!='S']+S):raise ValueError('measurement finite')
 return result
