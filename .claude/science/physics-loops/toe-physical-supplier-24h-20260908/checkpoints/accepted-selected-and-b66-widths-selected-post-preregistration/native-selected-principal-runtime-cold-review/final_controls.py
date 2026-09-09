import json,hashlib,sys,tempfile,copy,time
from pathlib import Path
BASE=Path('/private/tmp/toe-24h-probes-20260908'); ROOT=BASE/'native-selected-principal-root-review'
sys.path.insert(0,str(ROOT)); import schema
Q=1<<256
I=[[int(i==j) for j in range(48)]for i in range(48)]
Z=[[0]*48 for _ in range(48)]
D=lambda n:[[n*int(i==j)for j in range(48)]for i in range(48)]
S=[[str(x)for x in r]for r in I]
ev=[]
def add(stage,data):ev.append(dict(sequence=len(ev),stage=stage,data=data))
for a in range(24):
 for b in range(a,24):add('selected_entry',dict(a=a,b=b,g=[int(a==b)]*2,j=[0,0]))
add('selected_gram',dict(center=I,radii=Z,E=I,labels=[[i,0]for i in range(48)]))
for i in range(48):
 for j in range(i+1):add('candidate_pivot',dict(i=i,j=j,radicand=Q*Q*int(i==j)))
 add('candidate_factor_row',dict(row=i,values=D(Q)[i]))
for j in range(48):
 for i in range(j,-1,-1):add('candidate_inverse_entry',dict(i=i,j=j,value=Q*int(i==j)))
add('dyadic_inputs',dict(Gcenter=D(Q),radius=Z,T=D(Q),E=D(Q),scale=Q))
add('H_integer',dict(H=D(Q**3),denominator=Q**3))
add('error',dict(e='0',eta='0',Tnorm_upper='7'))
add('coefficient_box',dict(center=S,radius='0'))
assert len(ev)==2705
start=time.monotonic(); outcomes=[]
with tempfile.TemporaryDirectory(prefix='selected-schema-tiny-') as tmp:
 p=Path(tmp);out=p/'out';out.mkdir()
 def put(p,x):p.write_text(json.dumps(x))
 def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
 hist=[];pins={}
 for i in range(5):
  h=p/f'h{i}.json';put(h,{'history':[{'index':j}for j in range(24)]});hist.append(str(h));pins[str(h)]=sha(h)
 bp=p/'binding.json';put(bp,dict(histories=hist,inputs=pins))
 rf=dict(authorization={'binding_sha256':'synthetic'},worker_freeze='synthetic',binding_path=str(bp))
 def setup():
  for i in range(5):
   d=out/f'ORBIT_{i}';d.mkdir(exist_ok=True)
   for f in d.iterdir():f.unlink()
   put(d/'SELECTED.json',list(range(24)));put(d/'CANDIDATE.json',S)
   (d/'EVENTS.ndjson').write_text(''.join(json.dumps(e)+'\n'for e in ev))
   put(d/'RESULT.json',dict(status='CERTIFIED_ENCLOSURE',center=S,radius='0',e='0',width_pass=True,l1_pass=True))
  finish()
 def finish(seconds=.5):
  rows=[dict(orbit=i,status=json.loads((out/f'ORBIT_{i}'/'RESULT.json').read_text())['status'])for i in range(5)]
  put(out/'STARTED.json',rf['authorization']);put(out/'RESULT.json',dict(status='COMPLETE_SELECTED_PRINCIPAL_ATTEMPT',seconds=seconds,orbits=rows))
  put(out/'PARTIAL.json',dict(current={'stage':'complete'},rows=rows))
  put(out/'WORKER_COMPLETE.json',dict(status='COMPLETE_SELECTED_PRINCIPAL',runtime_sha256='synthetic',binding_sha256='synthetic',result_sha256=sha(out/'RESULT.json'),seconds=1,rss_bytes=100))
 def test(name,change=None,ok=False):
  setup()
  if change:change()
  try:r=schema.check(out,rf,2);accepted=True;detail=r
  except Exception as e:accepted=False;detail=repr(e)
  outcomes.append(dict(name=name,accepted=accepted,expected=ok,detail=detail));assert accepted==ok,(name,detail)
 d=out/'ORBIT_4'
 def result(**kw):
  a=json.loads((d/'RESULT.json').read_text());a.update(kw);put(d/'RESULT.json',a);finish()
 def eventchange(fn):
  ee=copy.deepcopy(ev);fn(ee);(d/'EVENTS.ndjson').write_text(''.join(json.dumps(e)+'\n'for e in ee))
 test('five certified real validator',ok=True)
 test('terminal 2705 Limit',lambda:result(status='INDETERMINATE_LIMIT_OR_CANDIDATE',failure_kind='Limit',error="Limit('integer bit cap')",current={'stage':'coefficient_box','orbit':4}),True)
 def residual(e):
  eventchange(lambda ee:(ee.pop(),ee[-1]['data'].update(e=str(e))))
  result(status='INDETERMINATE_RESIDUAL',e=str(e))
 test('2704 residual e1',lambda:residual(1),True)
 test('empty events',lambda:(d/'EVENTS.ndjson').write_text(''))
 test('wrong result time',lambda:finish('not-a-time'))
 test('residual e0',lambda:residual(0))
 test('wrong selected labels',lambda:put(d/'SELECTED.json',list(range(1,25))))
 test('retained box mismatch',lambda:eventchange(lambda ee:ee[-1]['data'].update(radius='1')))
 test('retained error mismatch',lambda:eventchange(lambda ee:ee[-2]['data'].update(e='1/2')))
 test('inverse candidate mismatch',lambda:eventchange(lambda ee:next(e for e in ee if e['stage']=='candidate_inverse_entry')['data'].update(value=0)))
 test('wrong failure stage',lambda:result(status='INDETERMINATE_LIMIT_OR_CANDIDATE',failure_kind='Limit',error="Limit('cap')",current={'stage':'error','orbit':4}))
report=dict(status='PASS',scope='Synthetic schema fixtures only; real events_schema, no native data or arithmetic replay.',seconds=time.monotonic()-start,tests=outcomes)
print(json.dumps(report,indent=2))
