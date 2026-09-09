"""UNLAUNCHED worker library. No CLI: contract/readiness must be reviewed first."""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib
import envelope as en
import real_kernel as kernel
import transport
import formats
import fp_guard
from validate_coefficients import validate
from norms import scan
from cg_candidate import solve

def execute(output):
 raise RuntimeError('UNLAUNCHED: real scan/transport cost, independent integration review and root contract required')

def planned_worker(np,out):
 # Not called by any shipped CLI; retained to make complete dataflow reviewable.
 out=Path(out)
 if out.exists():raise ValueError('fresh output')
 out.mkdir();fp_before=fp_guard.check();P=Path(__file__).parent;coeff=json.loads((P/'COEFFICIENTS.json').read_text());ledger=json.loads((P/'LEDGER.json').read_text());validation=validate(coeff,json.loads((P/'ADAPTED.json').read_text()),hashlib.sha256((P/'ADAPTED.json').read_bytes()).hexdigest());center=[(r['mode'],float.fromhex(r['candidate_hex'])) for r in coeff['center']];neighbors={int(v):[(r['mode'],float.fromhex(r['candidate_hex'])) for r in rows] for v,rows in coeff['neighbors'].items()};frequencies=[float.fromhex(r['candidate_hex']) for r in coeff['frequencies']];vertices=[36,180,6,30,1,5]
 def finite(x):
  if not np.isfinite(x).all():raise ValueError('nonfinite boundary')
 def pair_for(label):return [(vertices[v],-2) for v in ledger['representatives'][label]]
 def apply(label,p,x):
  finite(x);y=kernel.action(x,p,center,neighbors,pair_for(label),frequencies);finite(y);return y
 def write(name,x):
  finite(x);path=out/(name+'.npy');np.save(path,x,allow_pickle=False)
  h=hashlib.sha256(path.read_bytes()).hexdigest();raw=None
  if name in ('firstP','firstO','secondP','secondO','sourceP','sourceO','chi_real'):
   phase='real' if name.startswith('first') else 'i';rawpath=out/(name+'.bin');raw=formats.export(np,path,rawpath,phase,len(x));formats.verify(np,path,rawpath,phase,len(x))
  partial=out/'PARTIAL.json';old=json.loads(partial.read_text()) if partial.exists() else []
  old.append({'file':path.name,'sha256':h,'raw':raw});partial.write_text(json.dumps(old,indent=2));return h
 # Conservative same envelope for all Eg blocks, derived independently from exact table entries.
 def trenv(index,X):
  E,_,_=transport.blocks(index);errs=[];vals=[]
  for row in E:
   for a,b in row:
    # sqrt3 bracket exact100-bit roots. Signed b handled by interval sorting.
    hi=en.root_upper(F(3));lo=hi-F(1,1<<100);end=sorted((a+b*lo,a+b*hi));v=F(float(a)+float(b)*__import__('math').sqrt(3));errs.append(max(abs(v-end[0]),abs(v-end[1])));vals.append(v)
  eta=en.root_upper(sum(e*e for e in errs));L=en.root_upper(sum(v*v for v in vals));return en.transport_error(eta,L,X)
 def transported(x,index,p,X):
  # Magnitude ceiling excludes overflow in unguarded local transport operations.
  if X>F(1<<900):raise ValueError('transport magnitude ceiling')
  y=transport.apply(x,index,p);finite(y);err=trenv(index,X);return y,X+err,err
 first={};second={};certs={};sources={}
 def one(label,stage,b,Bhat,Berr):
  parity=int(stage=='second')
  def certify(x):
   fp_guard.check();X,_=scan(np,x,parity);y=apply(label,parity,x);r=np.subtract(b,y);finite(r);R,_=scan(np,r,parity);z=en.residual(coeff,pair_for(label),X,R,Bhat,Berr);z['X']=X;fp_guard.check();return z
  def save(i,x,c):
   h=write(stage+label+'_'+str(i),x);(out/(stage+label+'_'+str(i)+'.json')).write_text(json.dumps({'hash':h,'certificate':{k:str(v) for k,v in c.items()}},indent=2))
  x,c,i=solve(np,lambda z:apply(label,parity,z),b,certify,save,stage);write(stage+label,x);certs[stage+label]=dict(c,iteration=i);return x,c
 vacuum=np.zeros(1<<20);vacuum[0]=1
 for label in ('P','O'):first[label],_=one(label,'first',vacuum,F(1),F(0))
 for label in ('P','O'):
  norms=[];inherited=[];summed=None
  for entry in ledger['predecessors'][label]:
   c=certs['first'+entry['class']];y,X,e=transported(first[entry['class']],entry['transport'],0,c['X']);norms.append(X);inherited.append(c['solution_error']+e);summed=y if summed is None else np.add(summed,y);finite(summed)
  se=en.sum_error(norms);SX=sum(norms)+se;be=en.enderror(coeff['center'],SX);b=kernel.linear(summed,0,center,'B');finite(b);Berr=sum(inherited)+se+be;Bhat=SX+be;write('source'+label,b);sources[label]={'Berr':str(Berr),'Bhat':str(Bhat)};second[label],_=one(label,'second',b,Bhat,Berr)
 norms=[];errs=[];trs=[];summed=None
 for entry in ledger['entries']:
  c=certs['second'+entry['class']];y,X,e=transported(second[entry['class']],entry['transport'],1,c['X']);norms.append(X);errs.append(c['solution_error']);trs.append(e);summed=y if summed is None else np.add(summed,y);finite(summed)
 chi=np.divide(summed,8);finite(chi);E=en.final_error(errs,trs,norms);write('chi_real',chi);X,buckets=scan(np,chi,1);weights={}
 for k in range(1,22,2):
  a=en.root_upper(F(buckets[k],1<<2148));lo=max(F(0),a-F(1,1<<100));weights[k]=[str(max(F(0),lo-E)**2),str((a+E)**2)]
 a=en.root_upper(F(sum(buckets[3:]),1<<2148));lo=max(F(0),a-F(1,1<<100));weights['all_ge3']=[str(max(F(0),lo-E)**2),str((a+E)**2)]
 fp_after=fp_guard.check();result={'Echi':str(E),'passes_Echi':E<=F(1,10**6),'particle_intervals':weights,'sources':sources,'representative_certificates':{key:{k:str(v) for k,v in value.items()} for key,value in certs.items()},'vector_manifest':json.loads((out/'PARTIAL.json').read_text()),'physical_global_phase':'i','fp_before':fp_before,'fp_after':fp_after};(out/'RESULT.json').write_text(json.dumps(result,indent=2))
 if not result['passes_Echi']:raise RuntimeError('diagnostic failure: Echi threshold')
 return result
