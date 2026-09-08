import os
for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS']:os.environ[k]='1'
import signal,time,json,copy
from pathlib import Path
signal.alarm(180);start=time.monotonic()
import numpy as np
from producer import initial,advance,finalrow,config,req
from checkpoint import save,load
p=Path(__file__).parent;c=config(0,0,True);c.update(burn=19,updates=160,n=48,rk=0)
a,r,s=initial(c);a,r,s=advance(a,r,s,c,179)
b,t,z=initial(c)
for stop in [7,23,58,101,179]:
 b,t,z=advance(b,t,z,c,stop);save(p/'ROUNDTRIP.npz',b,t,c['L'],z);b,t,z=load(p/'ROUNDTRIP.npz')
req(s==z and finalrow(s,c)==finalrow(z,c),'complete accumulator')
req(np.array_equal(a.labels,b.labels) and a.head==b.head and a.direction==b.direction and a.nf==b.nf and all(np.array_equal(x,y) for x,y in zip(a.O,b.O)) and r.bit_generator.state==t.bit_generator.state,'path and rng')
# Select deterministic tape continuation with actual rejections, without tuning physics.
rejections=len(s['runs']);req(rejections>0,'actual rejection exercised')
with np.load(p/'ROUNDTRIP.npz',allow_pickle=False) as f:raw={k:f[k].copy() for k in f.files}
bad=dict(raw);bad['nf']=raw['nf']+1;np.savez_compressed(p/'MUTANT_NF.npz',**bad)
try:load(p/'MUTANT_NF.npz')
except ValueError:nfkill=True
else:raise RuntimeError('NF corruption passed')
bad=dict(raw);meta=json.loads(str(raw['metadata']));meta['direction']=0;bad['metadata']=np.array(json.dumps(meta));np.savez_compressed(p/'MUTANT_DIRECTION.npz',**bad)
try:load(p/'MUTANT_DIRECTION.npz')
except ValueError:dkill=True
else:raise RuntimeError('direction corruption passed')
(p/'PRODUCER_CONTROLS.json').write_text(json.dumps(dict(total_seconds=time.monotonic()-start,exact_split_stops=[7,23,58,101,179],burn=19,batch_width=10,rejections=rejections,nf_mutant_killed=nfkill,direction_mutant_killed=dkill,not_production=True),indent=2)+'\n')
print((p/'PRODUCER_CONTROLS.json').read_text())
