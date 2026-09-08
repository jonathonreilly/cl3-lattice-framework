from pathlib import Path
import subprocess,sys,time,json
p=Path(__file__).resolve().parent;start=time.monotonic();rows=[]
for pop in [1024,2048]:
 for case in range(7):
  if 600-(time.monotonic()-start)<180:raise RuntimeError('insufficient budget for next frozen job')
  name=f'production_p{pop}_c{case}';t=time.monotonic()
  with(p/(name+'.json')).open('w')as out,(p/(name+'.stderr')).open('w')as err:
   try:r=subprocess.run([sys.executable,str(p/'production.py'),'--population',str(pop),'--case',str(case)],stdout=out,stderr=err,timeout=180)
   except subprocess.TimeoutExpired:
    rows.append({'cell':name,'timeout':True,'seconds':time.monotonic()-t});(p/'PRODUCTION_STATUS.json').write_text(json.dumps(rows,indent=2)+'\n');raise
  rows.append({'cell':name,'exit':r.returncode,'seconds':time.monotonic()-t});(p/'PRODUCTION_STATUS.json').write_text(json.dumps(rows,indent=2)+'\n');print(rows[-1],flush=True)
  if r.returncode:raise RuntimeError('failed fixed job; no replacement')
