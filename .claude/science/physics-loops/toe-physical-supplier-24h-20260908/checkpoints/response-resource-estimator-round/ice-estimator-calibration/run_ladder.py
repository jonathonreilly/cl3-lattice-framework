from pathlib import Path
import subprocess,sys,time,json
p=Path(__file__).resolve().parent;records=[];start=time.monotonic()
for vi in [0,1]:
 for pop in [512,1024,2048]:
  for burn in [20,40]:
   if time.monotonic()-start>720:raise RuntimeError('insufficient aggregate budget for next capped cell')
   name=f'cell_v{vi}_p{pop}_b{burn}'
   with (p/(name+'.json')).open('w') as out,(p/(name+'.stderr')).open('w') as err:
    t=time.monotonic();r=subprocess.run([sys.executable,str(p/'calibrate.py'),'--vi',str(vi),'--population',str(pop),'--burn',str(burn)],stdout=out,stderr=err,timeout=185)
   records.append({'cell':name,'exit':r.returncode,'wall_seconds':time.monotonic()-t})
   (p/'ladder_status.json').write_text(json.dumps(records,indent=2)+'\n');print(records[-1],flush=True)
   if r.returncode:raise RuntimeError('failed cell preserved; stopping')
