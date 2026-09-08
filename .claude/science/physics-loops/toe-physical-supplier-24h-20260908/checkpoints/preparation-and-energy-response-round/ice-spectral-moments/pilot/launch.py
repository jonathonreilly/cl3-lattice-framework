from pathlib import Path
import subprocess,sys,time,json
p=Path(__file__).resolve().parent;status=[];start=time.monotonic()
for L in[2,4]:
 for burn in[32,128]:
  if time.monotonic()-start>360:raise RuntimeError('not enough of480-second production budget for next120-second cell')
  name=f'L{L}_b{burn}';t=time.monotonic()
  with(p/(name+'.json')).open('w')as out,(p/(name+'.stderr')).open('w')as err:r=subprocess.run([sys.executable,str(p/'pilot.py'),'--L',str(L),'--burn',str(burn)],stdout=out,stderr=err,timeout=125)
  status.append({'cell':name,'exit':r.returncode,'seconds':time.monotonic()-t});(p/'STATUS.json').write_text(json.dumps(status,indent=2)+'\n');print(status[-1],flush=True)
  if r.returncode:raise RuntimeError('failed cell retained; no coverage reduction')
