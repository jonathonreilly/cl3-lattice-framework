from pathlib import Path
import subprocess,sys,time,json
p=Path(__file__).resolve().parent;micro=json.loads((p/'MICRO.json').read_text())['elapsed_seconds'];start=time.monotonic();rows=[]
for g in range(3):
 for vi in range(3):
  if 600-micro-(time.monotonic()-start)<180:raise RuntimeError('insufficient remaining full cell budget; stop without shrinking')
  name=f'cell_g{g}_v{vi}';t=time.monotonic()
  with (p/(name+'.json')).open('w') as out,(p/(name+'.stderr')).open('w') as err:
   r=subprocess.run([sys.executable,str(p/'pilot.py'),'--group',str(g),'--vi',str(vi)],stdout=out,stderr=err,timeout=180)
  rows.append({'cell':name,'exit':r.returncode,'wall_seconds':time.monotonic()-t});(p/'STATUS.json').write_text(json.dumps(rows,indent=2)+'\n');print(rows[-1],flush=True)
  if r.returncode:raise RuntimeError('frozen cell failed; no replacement')
