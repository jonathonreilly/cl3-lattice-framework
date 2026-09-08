import os
for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS']:os.environ[k]='1'
from pathlib import Path
import json,hashlib,time,resource,signal,sys
signal.alarm(180);t=time.monotonic()
import numpy as np
from initialize import initialize
from checkpoint import save,load
p=Path(__file__).parent;checks=0;events=0;timings=[]
for L,n in [(2,48),(4,384),(8,110592)]:
 # Deterministic finite replay control, not a new timing/physics micro.
 a,_=initialize(L,n,np.random.default_rng(702+L),0);rng=np.random.default_rng(902+L)
 for _ in range(19):a.step(rng)
 acc={'step':19,'batch':[[1.25,-2.5]],'runs':[0,3],'unfinished':2,'u':4,'lo':-1,'hi':8}
 file=p/f'CONTROL_L{L}.npz';st=time.monotonic();save(file,a,rng,L,acc);b,s,rest=load(file);timings.append(time.monotonic()-st)
 assert rest==acc
 for k in range(128):
  assert a.step(rng)==b.step(s)
  assert a.head==b.head and a.direction==b.direction and a.nf==b.nf and np.array_equal(a.labels,b.labels)
  assert all(np.array_equal(x,y) for x,y in zip(a.states,b.states))
  assert all(np.array_equal(x,y) for x,y in zip(a.O,b.O))
  events+=1
 checks+=1
 # Genuine wrong-direction checkpoint adverse replay: this must separate states.
 b.direction=-b.direction
 diverged=False
 for _ in range(16):
  a.step(rng);b.step(s)
  diverged |= a.head!=b.head or not np.array_equal(a.labels,b.labels)
 assert diverged;checks+=1
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024)
if time.monotonic()-t>180 or rss>=384:raise RuntimeError('resources')
(p/'CHECKPOINT_CONTROLS.json').write_text(json.dumps(dict(roundtrip_graphs=3,exact_replayed_events=events,checks=checks,wrong_direction_mutants_killed=3,roundtrip_seconds=timings,total_seconds=time.monotonic()-t,rss_mib=rss,not_production=True),indent=2)+'\n')
print((p/'CHECKPOINT_CONTROLS.json').read_text())
