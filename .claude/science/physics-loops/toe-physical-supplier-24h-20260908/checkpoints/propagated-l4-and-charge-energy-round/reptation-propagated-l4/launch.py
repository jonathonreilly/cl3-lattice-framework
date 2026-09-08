import pathlib,json,hashlib,time,subprocess,sys
p=pathlib.Path(__file__).resolve().parent
for n,h in json.loads((p/'PRODUCTION_FREEZE.json').read_text()).items():
 if hashlib.sha256((p/n).read_bytes()).hexdigest()!=h:raise RuntimeError('freeze '+n)
f=json.loads((p/'FORECAST.json').read_text());t=time.monotonic();rows=[]
for arm in range(4):
 for sh in range(8):
  if 3600-f['micro']-(time.monotonic()-t)<180:raise RuntimeError('full shard reserve')
  name=f'arm{arm}_shard{sh}';out=p/(name+'.json')
  if out.exists():raise RuntimeError('no overwrite/replacement')
  st=time.monotonic()
  with out.open('w') as o,(p/(name+'.stderr')).open('w') as e:
   try:r=subprocess.run([sys.executable,str(p/'production.py'),'--cell',str(arm),'--shard',str(sh)],stdout=o,stderr=e,timeout=180)
   except subprocess.TimeoutExpired:
    rows.append(dict(name=name,timeout=True));(p/'STATUS.json').write_text(json.dumps(rows));raise
  rows.append(dict(name=name,exit=r.returncode,seconds=time.monotonic()-st));(p/'STATUS.json').write_text(json.dumps(rows,indent=2))
  if r.returncode:raise RuntimeError('failed fixed shard')
