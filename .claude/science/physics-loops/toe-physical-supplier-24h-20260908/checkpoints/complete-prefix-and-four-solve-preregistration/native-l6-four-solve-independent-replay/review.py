"""Unlaunched full evidence replay. No CG or candidate generation."""
import json, hashlib, math, struct
from pathlib import Path
from fractions import Fraction as F
import numpy as np
import envelope as en
import transport, fp_guard
from validate_coefficients import validate
P=Path(__file__).resolve().parent

def finite(x):
 if not np.isfinite(x).all():raise ValueError('nonfinite')

def norm(x,p):
 # Independent as_integer_ratio arithmetic, not the producer bitfield decoder.
 buckets=[0]*22
 for i,v in enumerate(x):
  a,b=float(v).as_integer_ratio();shift=2148-2*(b.bit_length()-1)
  if shift<0:raise ValueError('binary64 denominator')
  k=i.bit_count();buckets[k+((k&1)^p)]+=(a*a)<<shift
 return en.root_upper(F(sum(buckets),1<<2148)),buckets

def parity(a):
 # Independent bit-by-bit parity, restricted to 21 bits.
 out=np.zeros(len(a),dtype=np.uint32)
 for j in range(21):out^=(a>>j)&1
 return out

def linear(x,p,rows,kind,chunk=32768):
 # Output gather: reconstruct each source, rather than scattering input terms.
 n=len(x);top=n.bit_length()-1;out=np.zeros(n)
 if chunk<1 or chunk&(chunk-1):raise ValueError('power-two chunk')
 for start in range(0,n,chunk):
  dst=np.arange(start,min(start+chunk,n),dtype=np.uint32)
  z=np.zeros(len(dst))
  # Scatter chronology is input chunk, then original coefficient row.
  order=sorted(enumerate(rows),key=lambda item:(((start^(1<<item[1][0])) if item[1][0]<top else start)//chunk,item[0]))
  for _,(j,c) in order:
   src=dst^(1<<j) if j<top else dst
   bits=src|((parity(src)^p)<<top)
   sg=1-2*parity(bits&((1<<j)-1)).astype(np.int8)
   if kind=='B':sg*=2*((bits>>j)&1).astype(np.int8)-1
   t=np.multiply(np.multiply(x[src],c),sg);finite(t)
   z=np.add(z,t);finite(z)
  out[start:start+len(dst)]=z
 return out

def action(x,p,center,neighbors,pair,freq):
 n=len(x);top=n.bit_length()-1;out=np.empty(n)
 for start in range(0,n,32768):
  ids=np.arange(start,min(start+32768,n),dtype=np.uint32);bits=ids|((parity(ids)^p)<<top);d=np.zeros(len(ids))
  for j,w in enumerate(freq):d=np.add(d,np.multiply((bits>>j)&1,w))
  out[start:start+len(ids)]=np.multiply(d,x[start:start+len(ids)])
 finite(out)
 for v,k in pair:
  t=linear(linear(x,p,neighbors[v],'A'),1-p,center,'B')
  out=np.add(out,np.multiply(t,k));finite(out)
 return out

def trerr(index,X):
 E,_,_=transport.blocks(index);es=[];vs=[];hi=en.root_upper(F(3));lo=hi-F(1,1<<100)
 for row in E:
  for a,b in row:
   ends=sorted([a+b*lo,a+b*hi]);v=F(float(a)+float(b)*math.sqrt(3));vs.append(v);es.append(max(abs(v-ends[0]),abs(v-ends[1])))
 return en.transport_error(en.root_upper(sum(e*e for e in es)),en.root_upper(sum(v*v for v in vs)),X)

def same(a,b):
 if not np.array_equal(a.view(np.uint64),b.view(np.uint64)):raise ValueError('full vector reconstruction mismatch')

def contract_certificate(name, old, rho):
 iteration=old['iteration']
 if not isinstance(iteration,str) or not iteration.isdecimal() or int(iteration) not in range(16,257,16):raise ValueError('checkpoint contract '+name)
 threshold=F(1,10**10) if name.startswith('first') else F(1,10**9)
 if rho<0 or rho>threshold:raise ValueError('stage rho threshold '+name)

def replay(folder, progress=lambda stage, **detail:None):
 folder=Path(folder);fp_guard.check();result=json.loads((folder/'RESULT.json').read_text());c=json.loads((P/'COEFFICIENTS.json').read_text());l=json.loads((P/'LEDGER.json').read_text());validate(c,json.loads((P/'ADAPTED.json').read_text()),hashlib.sha256((P/'ADAPTED.json').read_bytes()).hexdigest())
 
 if result.get('physical_global_phase')!='i':raise ValueError('physical phase')
 vectors={};names=['firstP','firstO','secondP','secondO','sourceP','sourceO','chi_real']
 for name in names:
  progress('vector_bridge',vector=name)
  rows=[r for r in result['vector_manifest'] if r['file']==name+'.npy']
  if len(rows)!=1:raise ValueError('manifest coverage')
  row=rows[0];path=folder/row['file']
  if hashlib.sha256(path.read_bytes()).hexdigest()!=row['sha256']:raise ValueError('NPY hash')
  x=np.load(path,allow_pickle=False)
  if x.dtype!=np.float64 or x.shape!=(1<<20,):raise ValueError('vector domain')
  finite(x);raw=folder/(name+'.bin');meta=row['raw'];phase='real' if name.startswith('first') else 'i'
  if meta['phase']!=phase or raw.stat().st_size!=16*len(x):raise ValueError('raw domain')
  if hashlib.sha256(raw.read_bytes()).hexdigest()!=meta['sha256']:raise ValueError('raw hash')
  with raw.open('rb') as f:
   for start in range(0,len(x),4096):
    data=f.read(16*min(4096,len(x)-start));pairs=list(struct.iter_unpack('<QQ',data));bits=x[start:start+len(pairs)].view(np.uint64)
    for j,(a,b) in enumerate(pairs):
     if (a,b)!=((int(bits[j]),0) if phase=='real' else (0,int(bits[j]))):raise ValueError('raw bit bridge')
  vectors[name]=x;progress('vector_bridge_complete',vector=name,sha256=row['sha256'])
 center=[(r['mode'],float.fromhex(r['candidate_hex'])) for r in c['center']];neighbors={int(v):[(r['mode'],float.fromhex(r['candidate_hex'])) for r in rs] for v,rs in c['neighbors'].items()};freq=[float.fromhex(r['candidate_hex']) for r in c['frequencies']];vertices=[36,180,6,30,1,5];cert={}
 def certify(name,b,Bhat,Berr):
  progress('fresh_residual',vector=name)
  p=int(name.startswith('second'));label=name[-1];pair=[(vertices[v],-2) for v in l['representatives'][label]];x=vectors[name];X,_=norm(x,p);r=np.subtract(b,action(x,p,center,neighbors,pair,freq));finite(r);R,_=norm(r,p);z=en.residual(c,pair,X,R,Bhat,Berr);z['X']=X
  old=result['representative_certificates'][name]
  for key,value in z.items():
   if value!=F(old[key]):raise ValueError('fresh certificate mismatch '+name+key)
  contract_certificate(name,old,z['rho'])
  cert[name]=z;progress('fresh_residual_complete',vector=name,certificate={k:str(v) for k,v in z.items()})
 vacuum=np.zeros(1<<20);vacuum[0]=1
 for label in ('P','O'):certify('first'+label,vacuum,F(1),F(0))
 for label in ('P','O'):
  progress('source_assembly',vector='source'+label)
  ns=[];errs=[];total=None
  for e in l['predecessors'][label]:
   name='first'+e['class'];z=cert[name];te=trerr(e['transport'],z['X']);y=transport.apply(vectors[name],e['transport'],0);finite(y);total=y if total is None else np.add(total,y);finite(total);ns.append(z['X']+te);errs.append(z['solution_error']+te)
  se=en.sum_error(ns);SX=sum(ns)+se;be=en.enderror(c['center'],SX);b=linear(total,0,center,'B');same(b,vectors['source'+label]);Bhat=SX+be;Berr=sum(errs)+se+be
  if F(result['sources'][label]['Bhat'])!=Bhat or F(result['sources'][label]['Berr'])!=Berr:raise ValueError('source bound')
  certify('second'+label,b,Bhat,Berr)
 progress('final_chi_assembly')
 ns=[];errs=[];tes=[];total=None
 for e in l['entries']:
  name='second'+e['class'];z=cert[name];te=trerr(e['transport'],z['X']);y=transport.apply(vectors[name],e['transport'],1);total=y if total is None else np.add(total,y);finite(total);ns.append(z['X']+te);errs.append(z['solution_error']);tes.append(te)
 chi=np.divide(total,8);same(chi,vectors['chi_real']);E=en.final_error(errs,tes,ns);_,buckets=norm(chi,1);weights={}
 for key in list(range(1,22,2))+['all_ge3']:
  sq=buckets[key] if isinstance(key,int) else sum(buckets[3:]);a=en.root_upper(F(sq,1<<2148));lo=max(F(0),a-F(1,1<<100));weights[str(key)]=[str(max(F(0),lo-E)**2),str((a+E)**2)]
 if weights!=result['particle_intervals'] or E!=F(result['Echi']) or result['passes_Echi']!=(E<=F(1,10**6)):raise ValueError('final certificate')
 progress('final_weights_complete',Echi=str(E),particle_intervals=weights)
 fp_guard.check()
 return {'status':'PASS','scientific_pass':E<=F(1,10**6),'Echi':str(E),'particle_intervals':weights,'full_vectors':7,'fresh_residuals':4,'transports':27,'exact_norm_scans':9}
