from pathlib import Path
import json,hashlib,shutil,math
p=Path('/private/tmp/toe-24h-probes-20260908/detuned-reptation-local');r=p.parent/'detuned-reptation-local-cold-review/synthetic'
for name in ['core.py','production.py','analyze.py']:shutil.copyfile(p/name,r/name)
for cell,(tau,burn) in enumerate([(4,8),(4,32),(12,8),(12,32),(36,8),(36,32)]):
 n=384*tau
 for sh in range(16):
  rows=[]
  for rep in range(2):
   cid=32*cell+2*sh+rep;z=cid%32-15.5;vec=[64+.02*z,12+.01*z+math.sin(cid)*.01,13-.02*z,-3+.002*z]
   rows.append(dict(cid=cid,seed=202609160000+cid,mean=vec,batch_means=[vec]*16,counters={'accepted':64*n-10,'rejections':10,'accepted_self':10,'self_proposals':15}))
  x=dict(micro=False,cell=cell,shard=sh,L=4,V=.95,harmonics=[1,2],n=n,tau=tau,burn_multiplier=burn,updates=64*n,chains=2,rows=rows,seconds=1.,rss_mib=50.,source_sha=hashlib.sha256((p/'production.py').read_bytes()).hexdigest(),core_sha=hashlib.sha256((p/'core.py').read_bytes()).hexdigest())
  (r/f'cell{cell}_shard{sh}.json').write_text(json.dumps(x))
