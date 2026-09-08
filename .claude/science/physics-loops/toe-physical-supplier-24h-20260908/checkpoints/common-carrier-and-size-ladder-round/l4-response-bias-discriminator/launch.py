from pathlib import Path
import subprocess,sys,json,time
p=Path(__file__).resolve().parent;charged=json.loads((p/'MICRO.json').read_text())['seconds'];rows=[]
for g in [0,1]:
 for c in range(11):
  if 2400-charged<180:raise RuntimeError('reserve exhausted')
  q=p/f'g{g}_c{c}.json'
  if q.exists():raise RuntimeError('refuse overwrite')
  t=time.monotonic()
  try:
   with q.open('w') as out,(p/f'g{g}_c{c}.stderr').open('w') as err:r=subprocess.run([sys.executable,str(p/'driver.py'),'--group',str(g),'--case',str(c)],stdout=out,stderr=err,timeout=180)
   code=r.returncode
  except subprocess.TimeoutExpired:code=-999
  wall=time.monotonic()-t;charged+=wall;rows.append(dict(group=g,case=c,wall_seconds=wall,returncode=code,charged_seconds=charged));(p/'STATUS.json').write_text(json.dumps(rows,indent=2)+'\n')
  if code:raise RuntimeError('fixed cell failure, no replacement')
  a=json.loads(q.read_text())
  if not 0<a['rss_mib']<384 or a['seconds']>=180:raise RuntimeError('resources')
print(json.dumps(dict(complete=True,cells=22,charged_seconds=charged)))
