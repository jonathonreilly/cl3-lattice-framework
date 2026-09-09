from pathlib import Path
from fractions import Fraction as F
import json,tempfile,types,hashlib,copy
import numpy as np
import validate_coefficients as vc
import formats,envelope
P=Path(__file__).parent;c=json.loads((P/'COEFFICIENTS.json').read_text());a=json.loads((P/'ADAPTED.json').read_text());sha=hashlib.sha256((P/'ADAPTED.json').read_bytes()).hexdigest();vc.validate(c,a,sha);mutants=[]
for name in ('mode','radius','norm','pair'):
 bad=copy.deepcopy(c)
 if name=='mode':bad['center'][0]['mode']=1
 elif name=='radius':bad['center'][0]['candidate_radius']='0'
 elif name=='norm':bad['frequencies'][0]['norm']='0'
 else:bad['pairs'][0][0][1]=2
 try:vc.validate(bad,a,sha)
 except ValueError:mutants.append(name)
 else:raise ValueError('coefficient mutant '+name)
# Execute actual worker function body on16 entries with injected synthetic identity
# operators/solves. This tests dataflow and certificate paths, not native physics.
source=(P/'worker.py').read_text().replace('1<<20','16');ns={'__file__':str(P/'worker.py')};exec(compile(source,'tiny_actual_worker','exec'),ns)
ns['kernel']=types.SimpleNamespace(action=lambda x,*args:None)
ns['kernel'].action=lambda x,p,center,neighbors,pair,freq:x.copy()
ns['kernel'].linear=lambda x,p,center,kind:x.copy()
ns['transport']=types.SimpleNamespace(apply=lambda x,index,p:x.copy(),blocks=lambda index:([[(F(1),F(0)),(F(0),F(0))],[(F(0),F(0)),(F(1),F(0))]],None,1))
ns['fp_guard']=types.SimpleNamespace(check=lambda:{'synthetic':True})
calls=[];scans=[]
def scan(np,x,p):
 scans.append(p);b=[0]*22
 for i,v in enumerate(x):
  sq=F(float(v))**2;num=sq*(1<<2148)
  if num.denominator!=1:raise ValueError('dyadic')
  k=i.bit_count();k+=p^(k&1);b[k]+=num.numerator
 return envelope.root_upper(F(sum(b),1<<2148)),b
ns['scan']=scan
def solve(np,apply,b,certify,save,stage):
 calls.append(stage);x=b.copy();cert=certify(x);save(16,x,cert);return x,cert,16
ns['solve']=solve
with tempfile.TemporaryDirectory() as tmp:
 out=Path(tmp)/'pass';result=ns['planned_worker'](np,out);chi=np.load(out/'chi_real.npy')
 if calls!=['first','first','second','second'] or scans!=[0,0,0,0,1,1,1,1,1]:raise ValueError('stage/scan parity')
 if chi[0]!=F(90,8) or np.any(chi[1:]):raise ValueError('six/fifteen/oneeighth')
 if not result['passes_Echi'] or 'all_ge3' not in result['particle_intervals'] or not(out/'PARTIAL.json').exists():raise ValueError('final coverage')
 original=ns['en'].final_error;ns['en'].final_error=lambda *args:F(1)
 try:ns['planned_worker'](np,Path(tmp)/'fail')
 except RuntimeError as e:
  if 'Echi' not in str(e):raise
 else:raise ValueError('Echi false accepted')
 ns['en'].final_error=original
 try:formats.verify(np,out/'chi_real.npy',out/'absent','wrong',16)
 except ValueError:pass
 else:raise ValueError('bad phase')
print(json.dumps({'coefficient_reconstruction':'PASS','coefficient_mutants':mutants,'actual_worker_synthetic_pass_and_failure':True,'synthetic_dimension':16,'physical_calls':0}))
