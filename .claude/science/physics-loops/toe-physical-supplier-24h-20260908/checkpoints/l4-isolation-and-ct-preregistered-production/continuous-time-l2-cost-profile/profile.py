import json,time,random,math,resource
from pathlib import Path
from runtime import Runtime,Variates
CASES=[(.5,'constant',202609340001),(.5,'bounded',202609340002),(2.,'constant',202609340003),(2.,'bounded',202609340004)]
def main(out):
 start=time.monotonic();r=Runtime();load=time.monotonic()-start;rows=[]
 for cid,(T,kind,seed) in enumerate(CASES):
  cr=time.monotonic();rng=random.Random(seed);v=Variates(rng.getrandbits);z=time.monotonic()
  path=r.seed(T) if kind=='constant' else r.stationary_truncated(T,v)[0]
  init=time.monotonic()-z;blocks=[];intervals=[];values=[];measurement_times=[]
  for interval in range(4):
   tick=time.monotonic()
   for _ in range(96):
    p=v.randbelow(24);bt=time.monotonic();path,rec=r.block(path,p,v)
    blocks.append(dict(face=p,seconds=time.monotonic()-bt,receipt=rec))
   mt=time.monotonic();values.append(r.measure(path));measurement_times.append(time.monotonic()-mt);intervals.append(time.monotonic()-tick)
  z=time.monotonic();file=out/f'path{cid}.json';r.save(path,file);copy=r.load(file)
  if copy.events!=path.events or copy.initial!=path.initial or r.measure(copy)!=values[-1]:raise ValueError('roundtrip')
  io=time.monotonic()-z
  z=time.monotonic()
  synthetic_rows=[dict(values[j%4]) for j in range(128)]
  batch_means=[{k:sum(row[k] for row in synthetic_rows[j:j+8])/8 for k in values[0]} for j in range(0,128,8)]
  synthetic=dict(scope='SYNTHETIC repeated fixture vectors; no additional physical data',rows=synthetic_rows,batch_means=batch_means,face_histogram=[sum(b['face']==p for b in blocks) for p in range(24)])
  synthetic_file=out/f'synthetic{cid}.json';synthetic_file.write_text(json.dumps(synthetic))
  if json.loads(synthetic_file.read_text())!=synthetic:raise ValueError('synthetic representative output roundtrip')
  synthetic_io=time.monotonic()-z
  rows.append(dict(cid=cid,T=T,start=kind,seed=seed,initialization_seconds=init,io_seconds=io,synthetic_output_seconds=synthetic_io,synthetic_rows=128,synthetic_batches=16,measurement_seconds=measurement_times,interval_seconds=intervals,blocks=blocks,measurements=values,bit_calls=v.bit_calls,case_seconds=time.monotonic()-cr))
 return dict(runtime_load_seconds=load,cases=rows,seconds=time.monotonic()-start,rss_mib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1048576)
