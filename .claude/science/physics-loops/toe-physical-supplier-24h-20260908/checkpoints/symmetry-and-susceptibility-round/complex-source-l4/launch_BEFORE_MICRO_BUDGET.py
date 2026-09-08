import subprocess,sys,time,json
from pathlib import Path
p=Path(__file__).resolve().parent;start=time.monotonic();rows=[]
for pop in (512,1024):
 for case in range(8):
  if time.monotonic()-start>420:raise RuntimeError('insufficient remaining180seconds in600second envelope')
  name=f'production_p{pop}_c{case}';t=time.monotonic()
  with (p/(name+'.json')).open('w') as out,(p/(name+'.stderr')).open('w') as err:
   try:r=subprocess.run([sys.executable,'-O',str(p/'driver.py'),'--population',str(pop),'--case',str(case)],stdout=out,stderr=err,timeout=180)
   except subprocess.TimeoutExpired:
    rows.append(dict(cell=name,timeout=True,seconds=time.monotonic()-t));(p/'STATUS.json').write_text(json.dumps(rows,indent=2));raise
  rows.append(dict(cell=name,exit=r.returncode,seconds=time.monotonic()-t));(p/'STATUS.json').write_text(json.dumps(rows,indent=2));print(rows[-1],flush=True)
  if r.returncode:raise RuntimeError('fixed cell failed; no replacement')
