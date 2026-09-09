import sys,json,tempfile,hashlib,copy
from pathlib import Path
sys.path.insert(0,'/private/tmp/toe-24h-probes-20260908/native-coordinate-free-root-review')
import schema
ids=list(range(24));R=sorted({(6*(i//6)+(i%6)//2+off,g)for i in ids for off in(0,3)for g in(0,1)});U=sorted(set(R)|{(r,g)for r in(396,399,400,401)for g in(0,1)});raw=sorted({r for r,g in U});u=len(U);nr=len(R)
def matrix(n,m):return [[[0,0]for _ in range(m)]for _ in range(n)]
def make(oi):
 e=[];terms=0
 def emit(s,d):e.append((s,d))
 T=[[int(i==j)*2**256 for j in range(48)]for i in range(48)]
 emit('selected_candidate',dict(orbit=oi,pairs=24,candidate_bits=256,indices=ids,T=T))
 count=0
 for j,r in enumerate(raw):
  for s in raw[j:]:
   emit('acquisition_current',dict(raw_i=r,raw_j=s,completed=count));count+=1;emit('acquired_raw',dict(i=r,j=s,G=[0,0],J=[0,0],count=count))
 emit('physical_principal',dict(U=U,M=matrix(u,u),raw_pairs=count))
 def product(n,k,m):
  nonlocal terms
  emit('matrix_product_start',dict(rows=n,inner=k,columns=m,completed_terms=terms));terms+=n*k*m;emit('matrix_product_raw',dict(matrix=matrix(n,m),completed_terms=terms))
 product(nr,48,48);emit('embedding',dict(R=R,U=U,E=matrix(nr,48),C_U=matrix(u,48)));product(u,u,48);product(48,u,48);emit('H_raw',matrix(48,48));results=[]
 for imp in (399,400):
  emit('action_columns',dict(impurity=imp,B_U=matrix(u,48)));product(u,u,48);product(48,u,48);product(48,u,48);emit('A_Z_raw',dict(impurity=imp,A=matrix(48,48),Z=matrix(48,48)));product(48,48,48);product(48,48,48);emit('inverse_candidate',dict(impurity=imp,X=matrix(48,48),terms=4))
  def wrap(s,d):emit(s,dict(impurity=imp,data=d))
  wrap('frame_residual',dict(e='0'));wrap('inverse_residual',dict(r='0',a='1',epsilon='0',A_norm='0'));wrap('AXA',matrix(48,48));wrap('N_raw',matrix(48,48))
  sch=dict(N0=[['0']*48 for _ in range(48)],N_radius='0');wrap('Schur_center',dict(**sch,upper_numerator='0'));wrap('Schur_center',sch)
  v=dict(status='CERTIFIED_GENERALIZED_LEAKAGE_BOUND',delta_squared_lower='0',delta_squared_upper='0',target_squared='1/1000000000000',leakage_pass=True,target_excluded=False,e='0',entrywise_C_claim=False);wrap('result',v);results.append(v)
 return e,dict(status='COMPLETE_SOURCE_ONLY_ALGEBRA',results=results)
with tempfile.TemporaryDirectory()as td:
 p=Path(td);o=p/'out';o.mkdir();src=p/'src';src.mkdir();rf=dict(worker_freeze='toy',selected_output=str(src))
 def save(p,x):p.write_text(json.dumps(x))
 def setup(change=None):
  rows=[]
  for i in range(5):
   od=o/f'ORBIT_{i}';od.mkdir(exist_ok=True)
   for f in od.iterdir():f.unlink()
   sd=src/f'ORBIT_{i}';sd.mkdir(exist_ok=True);save(sd/'SELECTED.json',ids);save(sd/'CANDIDATE.json',[[str(int(a==b))for b in range(48)]for a in range(48)])
   e,ans=make(i)
   if i==4 and change:change(e,ans)
   for j,(s,d)in enumerate(e):save(od/f'{j:05d}_{s}.json',d)
   save(od/'RESULT.json',ans);rows.append(dict(orbit=i,status=ans['status'],stage_files=len(e)))
  result=dict(status='COMPLETE_SAME_SPAN_LEAKAGE_ATTEMPT',orbits=rows,target_squared='1/1000000000000',C_width_gate_required=False,h=1,new_scalar_recenter=False,seconds=1)
  save(o/'RESULT.json',result);save(o/'PARTIAL.json',dict(stage='complete',completed_orbits=rows));save(o/'WORKER_COMPLETE.json',dict(status='COMPLETE_GENERALIZED_LEAKAGE_ATTEMPT',runtime_sha256='toy',result_sha256=hashlib.sha256((o/'RESULT.json').read_bytes()).hexdigest(),seconds=2,rss_bytes=100))
 outcomes=[]
 def test(name,fn=None,expected=False):
  setup(fn)
  try:schema.check(o,rf,3);ok=True
  except (ValueError,KeyError,IndexError):ok=False
  assert ok==expected,name;outcomes.append(dict(name=name,accepted=ok))
 test('full five orbit retained stages',expected=True)
 for stage in ('physical_principal','H_raw'):
  test('missing '+stage,lambda e,a,s=stage:e.pop(next(i for i,x in enumerate(e)if x[0]==s)))
 test('wrong impurity',lambda e,a:next(x[1]for x in e if x[0]=='action_columns').update(impurity=400))
 test('invalid e',lambda e,a:a['results'][0].update(e='1'))
 def refused(e,a):
  k=next(i for i,x in enumerate(e)if x[0]=='H_raw');del e[k+1:];a.clear();a.update(status='INDETERMINATE_CERTIFICATE',error="Refused('synthetic')",leakage_pass=False,current=dict(orbit=4,stage=e[-1][0],serial=len(e)-1));e.append(('indeterminate',copy.deepcopy(a)))
 test('honest Refused prefix',refused,True)
 print(json.dumps({'status':'PASS','scope':'fabricated complete schema, no scientific computation','cases':outcomes},indent=2))
