import json,math,copy,time,resource
import analyze,config
from runtime import Runtime,NAMES
n=0
def ck(c):
 global n;n+=1
 if not c:raise ValueError(n)
def reject(f):
 try:f()
 except (ValueError,KeyError):ck(True)
 else:raise ValueError('bad fixture accepted')
start=time.monotonic();r=Runtime();a=config.ARMS[0];m=r.measure(r.seed(a['T']));row=[m[k] for k in NAMES];count=24*(a['burn']+128)
z=dict(chain=0,seed=config.seed(0,0),arm=a,raw_names=list(NAMES),rows=[row[:] for _ in range(128)],batch_means=[row[:] for _ in range(16)],face_histogram=[count]+[0]*23,completed_blocks=count,selected_events_sum=0,tape_used_sum=count,bracket_width_sum=0.,max_path_events=0,bit_calls=count,numerical_failures=0)
analyze.validate(z,a,0);ck(True)
for key,value in [('rows',z['rows'][:-1]),('completed_blocks',count-1)]:
 bad=copy.deepcopy(z);bad[key]=value;reject(lambda:analyze.validate(bad,a,0))
bad=copy.deepcopy(z);bad['arm']['T']=2.;reject(lambda:analyze.validate(bad,a,0))
bad=copy.deepcopy(z);bad['rows'][0][0]=float('nan');reject(lambda:analyze.validate(bad,a,0))
T=analyze.targets()
for t in T.values():
 st=analyze.stats([t['raw'][:] for _ in range(16)]);ck(analyze.assess(st,t)['pass_all'])
 m=t['raw'];g=analyze.gradients(m)
 for j in range(12):
  eps=1e-5;x=m[:];y=m[:];x[j]+=eps;y[j]-=eps
  fd=[(u-v)/(2*eps) for u,v in zip(analyze.derived(x),analyze.derived(y))]
  for k in range(5):ck(abs(fd[k]-g[k][j])<1e-8)
 # Deterministic symmetric perturbations, not synthetic physics observations.
 vectors=[[v+(i-7.5)*.0001*(j+1) for j,v in enumerate(m)] for i in range(16)]
 st=analyze.stats(vectors)
 for j in range(5):ck(abs(st['derived_se'][j]**2-st['derived_covariance'][j][j])<1e-18)
 ck(len(st['joint_raw_derived_mean_covariance'])==17)
m=[0.]*12;ck(analyze.stats([m[:] for _ in range(16)])['denominator_positive'] is False)
print(json.dumps(dict(checks=n,seconds=time.monotonic()-start,rss_mib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1048576,scope='deterministic controls only'),indent=2))
