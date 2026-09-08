from pathlib import Path
import subprocess,sys,time,json
p=Path(__file__).resolve().parent;micro=json.loads((p/'MICRO.json').read_text())['seconds'];start=time.monotonic();rows=[]
for L in [2,4]:
 for burn in [32,128]:
  if 510-micro-(time.monotonic()-start)<120:raise RuntimeError('insufficient remaining full cell budget')
  name=f'L{L}_b{burn}';t=time.monotonic()
  with(p/(name+'.json')).open('w')as out,(p/(name+'.stderr')).open('w')as err:
   try:r=subprocess.run([sys.executable,str(p/'run.py'),'--L',str(L),'--burn',str(burn)],stdout=out,stderr=err,timeout=120)
   except subprocess.TimeoutExpired:
    rows.append({'cell':name,'timeout':True,'seconds':time.monotonic()-t});(p/'STATUS.json').write_text(json.dumps(rows,indent=2)+'\n');raise
  rows.append({'cell':name,'exit':r.returncode,'seconds':time.monotonic()-t});(p/'STATUS.json').write_text(json.dumps(rows,indent=2)+'\n');print(rows[-1],flush=True)
  if r.returncode:raise RuntimeError('failed fixed cell, no replacement')
