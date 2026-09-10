"""Frozen nonnative noncommuting interval interaction fixture, 30s/384MiB."""
import time,signal,resource,sys,importlib.util,json
from pathlib import Path
from fractions import Fraction as F
import independent as I
import tables as T
P=Path('/private/tmp/toe-24h-probes-20260908/native-degree21-masked-jet-prototype')
start=time.monotonic();signal.signal(signal.SIGALRM,lambda *_:(_ for _ in()).throw(TimeoutError('30s synthetic cap')));signal.alarm(30)
# Only frozen prototype interval/core modules, never loader or scientific input.
for name in ['arithmetic','core']:
 spec=importlib.util.spec_from_file_location(name,P/(name+'.py'));m=importlib.util.module_from_spec(spec);sys.modules[name]=m;spec.loader.exec_module(m)
C=sys.modules['core'];events=[];checks=0
for kind,rank in [('nominal',4),('inner',3)]:
 # h=0, source bank I; nontrivial rank-one projection with offdiagonal1/2.
 # Both defect sets are Hermitian and noncommute with this P.
 def D(n,i,j):return I.c(int(n==0 and i==j))
 def B(n,i,j):
  if n:return I.ZERO
  v=F(1,2)if i<2 and j<2 else F(0);z=I.c(v)
  return((z[0][0]-1,z[0][1]+1),(0,0))
 mask,factors=T.factors(kind);J=T.defects(kind);got=[];want=[]
 root=I.reconstruct(mask,factors,J,D,B,lambda s,d:got.append((s,d)))
 prod,cnt=C.jet(kind+'21',J,D,B,lambda s,d:want.append((s,d)))
 def converted(stage,data):
  d=dict(data)
  for key in ['A','Q','matrix']:
   if key in d and isinstance(d[key],dict):d[key]=[[rank*p+i,rank*q+j,v]for(p,i,q,j),v in sorted(d[key].items(),key=lambda x:(rank*x[0][0]+x[0][1],rank*x[0][2]+x[0][3]))]
  return stage,d
 got=[converted(s,d)for s,d in got]
 assert len(got)==len(want),(kind,len(got),len(want))
 for j,(a,b)in enumerate(zip(got,want)):
  if a!=b:raise AssertionError((kind,j,a[0],str(a)[:200],str(b)[:200]))
  checks+=1
 assert root==prod;checks+=1
 events.append({'kind':kind,'events':len(got),'coefficients':len(root)})
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss;assert rss<384*1048576;signal.alarm(0)
print(json.dumps({'status':'PASS_NONCOMMUTING_SYNTHETIC','checks':checks,'records':events,'seconds':time.monotonic()-start,'rss_bytes':rss,'native_calls':0,'producer_loader_calls':0}))
