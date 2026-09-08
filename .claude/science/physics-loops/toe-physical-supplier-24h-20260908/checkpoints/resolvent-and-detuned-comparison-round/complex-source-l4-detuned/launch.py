import subprocess,sys,time,json
from pathlib import Path
p=Path(__file__).resolve().parent;start=time.monotonic();rows=[]
def save():
 (p/'STATUS.json').write_text(json.dumps(dict(cells=rows,charged_total_seconds=time.monotonic()-start,budget_seconds=900),indent=2))
for group in range(3):
 for case in range(7):
  if time.monotonic()-start>720:save();raise RuntimeError('insufficient remaining180seconds')
  name=f'cell_g{group}_c{case}';t=time.monotonic()
  if (p/(name+'.json')).exists():save();raise RuntimeError('existing cell; refuse overwrite')
  with (p/(name+'.json')).open('w') as out,(p/(name+'.stderr')).open('w') as err:
   try:r=subprocess.run([sys.executable,'-O',str(p/'driver.py'),'--group',str(group),'--case',str(case)],stdout=out,stderr=err,timeout=180)
   except subprocess.TimeoutExpired:rows.append(dict(cell=name,timeout=True,seconds=time.monotonic()-t));save();raise
  rows.append(dict(cell=name,exit=r.returncode,seconds=time.monotonic()-t));save();print(rows[-1],flush=True)
  if r.returncode:raise RuntimeError('failed fixed cell; no replacement')
