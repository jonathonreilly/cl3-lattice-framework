import json,time,hashlib
from fractions import Fraction as F
from pathlib import Path
from core import Iv,assemble,compress
P=Path(__file__).resolve().parent
def validate_inputs():
 manifest=json.loads((P/'ACCEPTED_INPUTS.json').read_text())
 if manifest['status']!='BOUND_ACCEPTED_SCALARS':raise ValueError('unaccepted input manifest')
 data={s:[] for s in (1,2)}
 for kind,keys,target in [('A',('A','Aprime'),F(1,10**12)),('B',('B','Bprime'),F(1,10**6))]:
  spec=manifest[kind];path=Path(spec['result']);raw=path.read_bytes();h=hashlib.sha256(raw).hexdigest()
  if h!=spec['result_sha256']:raise ValueError('result pin')
  acceptance=Path(spec['acceptance']);worker=Path(spec['worker'])
  if hashlib.sha256(acceptance.read_bytes()).hexdigest()!=spec['acceptance_sha256'] or hashlib.sha256(worker.read_bytes()).hexdigest()!=spec['worker_sha256']:raise ValueError('receipt pin')
  a=json.loads(acceptance.read_text());w=json.loads(worker.read_text());d=json.loads(raw)
  if a['status']!=spec['accepted_status'] or a['result_sha256']!=h or w['result_sha256']!=h or w['status']!='COMPLETE':raise ValueError('accepted binding')
  if d['alpha_computed'] is not False:raise ValueError('input scope')
  for s in (1,2):
   rows=[r for r in d['rows'] if r['s']==str(s)]
   if len(rows)!=1:raise ValueError('pole membership')
   row=rows[0]
   if row['status']!='CERTIFIED_TARGET':raise ValueError('uncertified scalar')
   for key in keys:
    if len(row[key])!=2:raise ValueError('interval shape')
    v=Iv(*row[key])
    if v.hi-v.lo>target:raise ValueError('scalar width')
    if row[key]!=spec['intervals'][str(s)][key]:raise ValueError('explicit interval binding')
    data[s].append(v)
 return {s:tuple(v) for s,v in data.items()}

def run(out):
 out.mkdir();start=time.monotonic();stage='validate';rows=[]
 def save(name,obj):(out/name).write_text(json.dumps(obj,indent=2)+'\n')
 def progress(r):
  nonlocal rows
  rows=r;save('PARTIAL.json',{'stage':stage,'rows':rows,'seconds':time.monotonic()-start})
 progress(rows)
 try:
  data=validate_inputs();stage='assemble_28';progress(rows);G,J=assemble(data)
  save('GRAM_INTERVALS.json',{'order':'s1+,s1-,s2+,s2-; each center,+x,-x,+y,-y,+z,-z','G':[[v.json() for v in r] for r in G],'J':[[v.json() for v in r] for r in J],'projected_gram':'(G+iJ)/2','physical_scalar_recomputation':False})
  # Exact bare-column relations, independently derived from (K-sigma*s)y=-e.
  def rel(label):
   v=[0]*28;s,sig=((1,1),(1,-1),(2,1),(2,-1))[label];v[7*label]=-sig*s
   for a in range(3):v[7*label+1+2*a]=1;v[7*label+2+2*a]=-1
   return v
  first=rel(0);nulls=[];checks=0
  for label in (1,2,3):
   v=[a-b for a,b in zip(rel(label),first)];nulls.append(v)
   for M in (G,J):
    for row in M:
     z=sum((x*c for x,c in zip(row,v)),Iv(0));checks+=1
     if not z.lo<=0<=z.hi:raise ValueError('null relation excluded')
  save('ALGEBRA.json',{'null_relations':nulls,'interval_null_containment_checks':checks,'covariance_closure':'[[G,J],[-J,G]]; implied by actual pure Gamma0^2=-I','PH':'real Y, real skew J; projected complement (G-iJ)/2','warning':'No interval PSD eigenvalue certification is claimed; positivity uses the source Green theorem.'})
  stage='paired_pivots';progress(rows);status,rows,initial=compress(G,J,progress)
  stage='complete';save('RESULT.json',{'status':status,'execution_complete':True,'initial_trace':initial.json(),'rows':rows,'null_containment_checks':checks,'seconds':time.monotonic()-start,'physical_integrals':0,'physical_gram_assembled':True,'alpha_computed':False,'stationary_projector_computed':False,'error_scope':'for Y C Y^dagger with any ||C||<=1, not an assembled physical impurity projector'})
 except BaseException as e:save('FAILURE.json',{'stage':stage,'rows':rows,'error':repr(e),'seconds':time.monotonic()-start});raise
