import json,time,resource,tempfile,hashlib
from pathlib import Path
from fractions import Fraction as F
import numpy as np
import core,postcheck
P=postcheck.P;start=time.monotonic();n=0
def ck(c):
 global n;n+=1
 if not c:raise ValueError(n)
frame=json.loads((P/'FRAME_RESULT.json').read_text());prefix=json.loads((P/'PREFIXES.json').read_text());m=core.ExactModel(frame,prefix);A=m.matrix(3)
x=([i%5-2 for i in range(512)],16);parts=[([1]+[0]*511,1),([i%3-1 for i in range(512)],8)]
b,db=core.incoming(parts);literal=[-F(z,db) for z in b]
for (i,j),a in A.items():literal[i]-=F(a,m.den)*F(x[0][j],x[1])
sq=sum(w*r*r for w,r in zip(m.W,literal));bound=core.residual(m,A,x,parts)
ck(bound*bound>=sq);ck((bound-F(1,10**50))**2<sq)
ck(core.gap(m,3)==F(999997540876869429,1446265625000000000))
for q in (F(0),F(1,3),F(10**100,7)):
 u=core.upper_sqrt(q);ck(u*u>=q)
# Synthetic metadata is solely a decoder fixture, not a solution.
row=prefix['rows'][0];rs=row['prefixes'];vectors=np.zeros((len(rs),512));vectors[0,0]=1
with tempfile.TemporaryDirectory() as temp:
 d=Path(temp);vf=d/'v.npz';jf=d/'bridge.json'
 def save(v):
  np.savez(vf,vectors=v,k=np.array([r['k'] for r in rs],dtype=np.uint8),boundary_used_hex=np.array([hex(int(r['boundary_used_mask'])) for r in rs]),bridge_count=np.array([r['bridge_count'] for r in rs],dtype=np.uint8),toggle_hex=np.array([hex(int(r['full_toggle_mask'])) for r in rs]),word_count=np.ones(len(rs),dtype=np.uint64))
  jf.write_text(json.dumps(dict(bridge=row['bridge_edge'],vector_artifact={'filename':'v.npz','sha256':postcheck.sha(vf)})))
 save(vectors);postcheck.load(jf,prefix);ck(True)
 save(vectors[:-1])
 try:postcheck.load(jf,prefix)
 except ValueError:ck(True)
 else:raise ValueError('missing row accepted')
 vectors[1,0]=np.nan;save(vectors)
 try:postcheck.load(jf,prefix)
 except ValueError:ck(True)
 else:raise ValueError('NaN accepted')
print(json.dumps(dict(checks=n,matrix_denominator=m.den,metric_denominator=m.Wden,sparse_entries=len(A),seconds=time.monotonic()-start,rss_mib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1048576,scope='bounded deterministic harness controls; no saved physical DP or full residual scan'),indent=2))
