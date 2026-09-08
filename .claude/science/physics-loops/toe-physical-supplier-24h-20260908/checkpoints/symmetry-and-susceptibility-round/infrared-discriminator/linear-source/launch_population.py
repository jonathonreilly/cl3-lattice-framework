import time,subprocess,json,sys,os,hashlib
from pathlib import Path
p=Path(__file__).resolve().parent;budget=1800.;charged=3.5605325830110814;status=[]
# Calling this file is a production action; frozen pending root review.
for pop in [128,256]:
 for case in range(7):
  if budget-charged<180:raise RuntimeError('insufficient reserved cell budget')
  target=p/f'population_p{pop}_c{case}.json'
  if target.exists():raise RuntimeError('refuse overwrite or implicit rerun')
  t=time.monotonic()
  try:
   with target.open('w') as out,(p/f'population_p{pop}_c{case}.stderr').open('w') as err:
    result=subprocess.run([sys.executable,str(p/'producer.py'),'--population',str(pop),'--case',str(case)],stdout=out,stderr=err,timeout=180,env={**os.environ,'OPENBLAS_NUM_THREADS':'1','OMP_NUM_THREADS':'1','MKL_NUM_THREADS':'1'})
   code=result.returncode
  except subprocess.TimeoutExpired:code=-999
  wall=time.monotonic()-t;charged+=wall;status.append(dict(population=pop,case=case,wall_seconds=wall,returncode=code,charged_total=charged))
  (p/'POPULATION_STATUS.json').write_text(json.dumps(status,indent=2)+'\n')
  if code!=0:raise RuntimeError('cell failure preserved; stop')
  r=json.loads(target.read_text())
  if not 0<r['rss_mib']<384 or r['seconds']>=180 or charged>budget or any(x['postconditions'] is not True for x in r['rows']):raise RuntimeError('resource/postcondition failure')
print(json.dumps(dict(complete=True,charged_seconds=charged,cells=len(status))))
