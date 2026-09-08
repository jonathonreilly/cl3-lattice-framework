from analyze import replay,validate_history
import copy,json
from pathlib import Path
n=12;burn=24;updates=48;runs=[5,2,8];last=54
mem,rej=replay(n,runs,last,burn,updates)
c=dict(run_lengths_including_burn=runs,unfinished_run=last,rejections=rej,accepted=updates-rej,self_proposals=0,accepted_self=0,window_traversals_including_burn=sum(z//n for z in runs+[last]))
r=dict(memory=mem,counters=c,initializer=dict(rk_sweeps=128,rk_proposals=128*192,Q_steps=n,nonself_Q_steps=2,law='finite RK start followed by productQ; not equilibrium productG path law'))
validate_history(r,n,128,burn,updates)
kills=[]
for group in r:
 for key in r[group]:
  z=copy.deepcopy(r);v=z[group][key]
  if isinstance(v,list):z[group][key]=[-1]+v[1:]
  elif isinstance(v,str):z[group][key]='wrong'
  elif v is None:z[group][key]=1
  elif key=='nonself_Q_steps':z[group][key]=n+1
  elif key in ['self_proposals','accepted_self']:z[group][key]=updates+1
  else:z[group][key]=v+1
  try:validate_history(z,n,128,burn,updates)
  except ValueError:kills.append(group+'.'+key)
  else:raise RuntimeError('mutation survived '+group+'.'+key)
Path('MALFORMED_CONTROLS.json').write_text(json.dumps(dict(killed=kills,production_executed=False),indent=2)+'\n')
print(len(kills))
