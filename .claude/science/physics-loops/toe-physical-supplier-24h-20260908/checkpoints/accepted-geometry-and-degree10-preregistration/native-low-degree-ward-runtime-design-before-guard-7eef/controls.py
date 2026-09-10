from fractions import Fraction as F
import json,tempfile
from pathlib import Path
import interval as I,compute,worker
checks=0
def need(x):
 global checks
 if not x:raise AssertionError(checks)
 checks+=1
for v in [F(0),F(1),F(2),F(3,7),F(1000000,3)]:
 a,b=I.root(I.point(v));need(a*a<=v<=b*b and b-a<=F(1,2**128))
for bad in [True,1,'01','1/0','2/4','-0']:
 try:I.parse(bad)
 except (ValueError,ZeroDivisionError):need(True)
 else:need(False)
try:I.nonnegative((F(-2),F(-1)))
except ValueError:need(True)
else:need(False)
need(I.nonnegative((F(-1),F(1)))==(F(0),F(1)))
need(I.mul((F(-2),F(3)),(F(-4),F(5)))==(F(-12),F(15)))
need(compute.solve(I.point(2),I.point(1),I.point(3),I.point(1),I.point(4))[:2]==(F(-1,5),F(7,5)))
# Full worker schedule with explicit mock candidate and loader. Native moment
# formulas are NOT called; four stage payloads imitate interfaces only.
oldc,oldl=compute.candidate,worker.load
calls=[]
def fake(c,nu,kind,mode,emit):
 calls.append((mode,kind))
 for stage in ['moments','polynomial','source_moments','residual_raw']:emit(stage,{'kind':kind,'synthetic':True})
 return dict(p0=F(1),p1=F(0),q=F(0),r2=I.point(0),t2=I.point(0))
try:
 compute.candidate=fake;worker.load=lambda b:(I.point(F(4,5)),I.point(15))
 with tempfile.TemporaryDirectory(prefix='degree10-synthetic-')as d:
  worker.run({'_binding_file_sha256':'synthetic'},Path(d))
  r=json.loads((Path(d)/'RESULT.json').read_text());events=[json.loads(x)for x in (Path(d)/'EVENTS.ndjson').read_text().splitlines()]
  need(r['events']==205 and len(events)==205 and r['choices']==2)
  need(calls==[('residual','P'),('residual','O'),('variational','P'),('variational','O')])
  need(all(x['nominal']==['90','90']and x['status']=='POSITIVE_CERTIFICATE'for x in r['rows']))
  need(all(sorted(y['count']for y in x['orbits'].values())==[6,12,12,12,48]for x in r['rows']))
  need(all(x['sequence']==i+1 for i,x in enumerate(events)))
finally:compute.candidate,worker.load=oldc,oldl
print(json.dumps({'status':'PASS_SYNTHETIC_ONLY','checks':checks,'accepted_scalar_loads':0,'native_candidate_calls':0},indent=2))
