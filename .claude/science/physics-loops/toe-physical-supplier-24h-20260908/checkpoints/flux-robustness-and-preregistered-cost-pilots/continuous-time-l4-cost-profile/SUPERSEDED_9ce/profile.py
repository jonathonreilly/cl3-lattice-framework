"""Four fixed cost observations only; imported without executing them."""
import json,random,time,math
from pathlib import Path
from adapter import Adapter,NAMES
from preflight import sha

def face_stream(r):
 while True:
  x=r.getrandbits(8)
  if x<192:yield x

def uniform_stream(r):
 while True:yield r.getrandbits(53)/2**53

def main(out):
 out=Path(out);cases=[]
 for cid,(T,start) in enumerate(((.5,'constant'),(.5,'propagated'),(2.,'constant'),(2.,'propagated'))):
  begin=time.monotonic();seed=202609420000+cid;r=random.Random(seed);b=random.Random(seed+10000)
  t=time.monotonic();a=Adapter(4,.95)
  if start=='constant':p=a.seed(T);init={'rk_sweeps':0,'rk_proposals':0,'clock_draws':0,'physical_events':0}
  else:p,init=a.propagated(T,face_stream(r),uniform_stream(r),128,4096)
  init_seconds=time.monotonic()-t;blocks=[];measurements=[];mt=[]
  for face in (0,64,128,191):
   t=time.monotonic();p,receipt=a.block(p,face,uniform_stream(b),4096);seconds=time.monotonic()-t
   blocks.append({'face':face,'seconds':seconds,'receipt':receipt})
   t=time.monotonic();measurements.append(a.measure(p));mt.append(time.monotonic()-t)
  t=time.monotonic();path=out/f'path{cid}.json';a.save(p,path);loaded=a.load(path)
  if a.measure(loaded)!=measurements[-1] or loaded.events!=p.events or loaded.witness!=p.witness:raise ValueError('lossless full path roundtrip')
  io=time.monotonic()-t
  t=time.monotonic();rows=[[v[k] for k in NAMES] for v in measurements]*32
  batches=[[sum(rows[j][k] for j in range(i,i+8))/8 for k in range(15)] for i in range(0,128,8)]
  syn={'scope':'SYNTHETIC repeated serialization fixture, not physical observations','rows':rows,'batches':batches,'face_histogram':[128]*192,'numerical_failures':0,'path_sha':sha(path)}
  sf=out/f'synthetic{cid}.json';sf.write_text(json.dumps(syn,allow_nan=False));back=json.loads(sf.read_text())
  if back!=syn or len(back['rows'])!=128 or len(back['batches'])!=16:raise ValueError('synthetic serialization')
  synthetic=time.monotonic()-t
  cases.append(dict(cid=cid,T=T,start=start,seed=seed,initialization=init,initialization_seconds=init_seconds,blocks=blocks,measurements=measurements,measurement_seconds=mt,io_seconds=io,synthetic_output_seconds=synthetic,synthetic_rows=128,synthetic_batches=16,events=len(p.events),witness_length=len(p.witness),case_seconds=time.monotonic()-begin))
 return {'cases':cases,'names':NAMES,'scope':'cost only; no mixing or physics acceptance'}
