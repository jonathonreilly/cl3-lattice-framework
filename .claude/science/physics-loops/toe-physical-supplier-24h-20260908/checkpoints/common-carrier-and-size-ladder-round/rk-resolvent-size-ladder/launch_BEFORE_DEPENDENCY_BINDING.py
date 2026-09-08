import pathlib,subprocess,sys,time,json,hashlib
p=pathlib.Path(__file__).resolve().parent
freeze=json.loads((p/'PRODUCTION_FREEZE.json').read_text())
for n,h in freeze.items():
 if hashlib.sha256((p/n).read_bytes()).hexdigest()!=h:raise RuntimeError('freeze changed: '+n)
f=json.loads((p/'FORECAST_PRODUCTION.json').read_text())
if not f['gate']:raise RuntimeError('forecast gate')
start=time.monotonic();rows=[]
for L,b in [(8,32),(8,128),(8,512),(16,32),(16,128),(16,2048)]:
 for sh in range(4):
  if 2700-f['micros']-(time.monotonic()-start)<180:raise RuntimeError('insufficient whole shard reserve')
  name=f'L{L}_b{b}_shard{sh}'
  if (p/(name+'.json')).exists() or (p/name).exists():raise RuntimeError('refuse overwrite/replacement')
  t=time.monotonic()
  with (p/(name+'.json')).open('w') as out,(p/(name+'.stderr')).open('w') as err:
   try:r=subprocess.run([sys.executable,str(p/'stream.py'),'--L',str(L),'--burn',str(b),'--shard',str(sh)],stdout=out,stderr=err,timeout=180)
   except subprocess.TimeoutExpired:
    rows.append(dict(name=name,timeout=True,seconds=time.monotonic()-t));(p/'STATUS.json').write_text(json.dumps(rows,indent=2));raise
  rows.append(dict(name=name,exit=r.returncode,seconds=time.monotonic()-t));(p/'STATUS.json').write_text(json.dumps(rows,indent=2));print(rows[-1],flush=True)
  if r.returncode:raise RuntimeError('failed fixed shard, no replacement')
