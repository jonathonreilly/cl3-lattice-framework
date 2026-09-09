import json,time,hashlib
from fractions import Fraction as F
from pathlib import Path
from core import Iv,assemble,compress
P=Path(__file__).resolve().parent
BASE=P.parents[1]
INPUT=BASE/'native-star-local-green-gram-run-41ebe'/'RESULT.json'
ACCEPTANCE=BASE/'native-star-local-green-gram-root-review'/'ROOT_ACCEPTANCE.json'
WORKER=BASE/'native-star-local-green-gram-run-41ebe'/'WORKER_COMPLETE.json'
def validate_inputs():
 d=json.loads(INPUT.read_text());a=json.loads(ACCEPTANCE.read_text());w=json.loads(WORKER.read_text());h=hashlib.sha256(INPUT.read_bytes()).hexdigest()
 if a['status']!='ACCEPTED_COMPLETE_FIXED_PILOT' or w['status']!='COMPLETE' or a['result_sha256']!=h or w['result_sha256']!=h:raise ValueError('accepted scalar binding')
 if not d['all_width_targets_met'] or d['gram_matrix_computed'] or d['alpha_computed']:raise ValueError('input scope')
 if [(r['s'],r['kind']) for r in d['rows']]!=[('1','A'),('1','B'),('2','A'),('2','B')]:raise ValueError('fixed rows')
 data={}
 for s in (1,2):
  rr=d['rows'][2*(s-1):2*s];values=[]
  for r in rr:
   if r['status']!='CERTIFIED_TARGET':raise ValueError('scalar status')
   for lo,hi in r['bounds']:
    v=Iv(lo,hi)
    if v.hi-v.lo>F(1,32):raise ValueError('scalar width')
    values.append(v)
  data[s]=tuple(values)
 return data

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
