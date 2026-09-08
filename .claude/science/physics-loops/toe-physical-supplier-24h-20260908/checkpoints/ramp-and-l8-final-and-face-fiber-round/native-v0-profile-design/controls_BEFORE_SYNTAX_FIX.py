import pathlib,json,time,signal,resource,sys,copy
import numpy as np
from initialize import initialize
from checkpoint import save,load
from core import count,legal,flip,Path
from observables import OrderMenu
from profile import advance,accumulator
signal.alarm(180);start=time.monotonic();P=pathlib.Path(__file__).parent;checks=0
def req(c,m):
 global checks
 checks+=1
 if not c:raise RuntimeError(m)
for L in (2,4):
 for V in (.95,0.,1.):
  a,meta=initialize(L,24,np.random.default_rng(8101),V,2);r=np.random.default_rng(8101);x=Path(L,24,V).states[0];M=len(a.faces)
  for t in range(2*M):
   f=int(r.integers(M))
   if legal(x,a.faces[f]):x=flip(x,f,a.faces)
  literal=[x.copy()];labels=[]
  for t in range(24):
   u=r.random()*(M+(1-V)*count(x,a.faces));f=int(u) if u<M else -1;label=f if f>=0 and legal(x,a.faces[f]) else -1;labels.append(label);x=flip(x,label,a.faces);literal.append(x.copy())
  req(np.array_equal(a.labels,labels),'initializer labels')
  for k,j in enumerate((0,12,24)):req(np.array_equal(a.states[k],literal[j]),'initializer states');req(a.nf[k]==count(literal[j],a.faces),'initializer NF');req(np.max(abs(a.O[k]-a.coeff@(literal[j]-.5)))<1e-12,'initializer O')
# Full accumulated deterministic replay, split inside warmup, inside batch, and final short segment.
rows=[]
for V in (.95,0.):
 L=2;n=24;warm=17;measured=384;menu=OrderMenu(L);a,_=initialize(L,n,np.random.default_rng(9001),V,2);r=np.random.default_rng(9002);s=accumulator();aa=copy.deepcopy(a);rr=copy.deepcopy(r);ss=copy.deepcopy(s);advance(aa,rr,ss,menu,warm+measured,warm,measured)
 for k,stop in enumerate((7,149,300,warm+measured)):
  advance(a,r,s,menu,stop,warm,measured);file=P/f'CONTROL_V{V}_split{k}.npz';save(file,a,r,L,s);a,r,s=load(file,expected=dict(L=L,n=n,V=V))
 req(s==ss and r.bit_generator.state==rr.bit_generator.state,'full accumulator/RNG');req(a.head==aa.head and a.direction==aa.direction and np.array_equal(a.labels,aa.labels),'full ring')
 for k in range(3):req(np.array_equal(a.states[k],aa.states[k]) and a.nf[k]==aa.nf[k] and np.array_equal(a.O[k],aa.O[k]),'full caches')
 req(s['snapshots']==16 and np.array(s['raw']).shape==(16,154),'same-time complete vector');rows.append(dict(V=V,attempts=s['step'],rejections=s['rejections'],snapshots=s['snapshots']))
 # Updated metadata mutant must fail before constructing the path.
 with np.load(file,allow_pickle=False) as z:data={k:z[k].copy() for k in z.files}
 meta=json.loads(str(data['metadata']));meta['V']=.5;data['metadata']=np.array(json.dumps(meta));bad=P/f'WRONG_V_{V}.npz';np.savez_compressed(bad,**data)
 try:load(bad,expected=dict(L=L,n=n,V=V))
 except ValueError as e:req(str(e)=='checkpoint V mismatch','wrongV reason')
 else:raise RuntimeError('wrongV accepted')
# Pure cadence arithmetic on the ACTUAL profile lengths, no profile execution.
steps=[t+1-4096 for t in range(4096,4096+24576) if (t+1-4096)%1536==0];req(steps==list(range(1536,24577,1536)),'actual half-open cadence');req(sum(t<=8192 for t in steps)==5 and8192-steps[4]==512,'partial batch one snapshot')
req(any(r['rejections'] for r in rows),'rejection coverage')
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1048576 if sys.platform=='darwin' else 1024);req(rss<384 and time.monotonic()-start<180,'resources');out=dict(predicates=checks,rows=rows,seconds=time.monotonic()-start,rss_mib=rss,scope='deterministic reduced fixture continuation; no cost profile or stationary sampling');(P/'CONTROLS.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
