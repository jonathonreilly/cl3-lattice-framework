from pathlib import Path
import subprocess,sys,time,json
p=Path(__file__).resolve().parent;start=time.monotonic();status=[]
for pop in[512,2048]:
 for batch in range(4):
  if time.monotonic()-start>180:raise RuntimeError('insufficient remaining aggregate cap for next180second job')
  n=f'p{pop}_batch{batch}';t=time.monotonic()
  with(p/(n+'.json')).open('w')as out,(p/(n+'.stderr')).open('w')as err:r=subprocess.run([sys.executable,str(p/'run_batch.py'),'--population',str(pop),'--batch',str(batch)],stdout=out,stderr=err,timeout=185)
  status.append({'batch':n,'exit':r.returncode,'seconds':time.monotonic()-t});(p/'STATUS.json').write_text(json.dumps(status,indent=2));print(status[-1],flush=True)
  if r.returncode:raise RuntimeError('failed batch preserved')
