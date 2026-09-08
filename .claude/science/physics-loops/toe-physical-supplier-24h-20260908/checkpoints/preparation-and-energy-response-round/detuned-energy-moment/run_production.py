from pathlib import Path
import subprocess,sys,time,json
p=Path(__file__).resolve().parent;start=time.monotonic();rows=[]
for pop in [1024,2048]:
 for vi in range(5):
  remaining=600-(time.monotonic()-start)
  if remaining<180:raise RuntimeError('insufficient remaining budget for next frozen job')
  name=f'production_p{pop}_v{vi}';t=time.monotonic()
  with (p/(name+'.json')).open('w') as out,(p/(name+'.stderr')).open('w') as err:
   try:r=subprocess.run([sys.executable,str(p/'production.py'),'--population',str(pop),'--vi',str(vi)],stdout=out,stderr=err,timeout=180)
   except subprocess.TimeoutExpired:
    rows.append({'name':name,'status':'TIMEOUT','wall':time.monotonic()-t});(p/'PRODUCTION_STATUS.json').write_text(json.dumps(rows,indent=2));raise
  rows.append({'name':name,'exit':r.returncode,'wall':time.monotonic()-t});(p/'PRODUCTION_STATUS.json').write_text(json.dumps(rows,indent=2)+'\n');print(rows[-1],flush=True)
  if r.returncode:raise RuntimeError('failed frozen job; no replacement')
