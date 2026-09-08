import pathlib,json,hashlib,time,subprocess,sys
p=pathlib.Path(__file__).resolve().parent
for n,h in json.loads((p/'PRODUCTION_FREEZE.json').read_text()).items():
 if hashlib.sha256((p/n).read_bytes()).hexdigest()!=h:raise RuntimeError('freeze '+n)
t=time.monotonic();rows=[];micro=json.loads((p/'MICRO.json').read_text())['seconds']
for sh in range(4):
 if 300-micro-(time.monotonic()-t)<180:raise RuntimeError('full shard reserve')
 f=p/f'shard{sh}.json'
 if f.exists():raise RuntimeError('no overwrite/replacement')
 st=time.monotonic()
 with f.open('w') as o,(p/f'shard{sh}.stderr').open('w') as e:
  try:r=subprocess.run([sys.executable,str(p/'production.py'),'--shard',str(sh)],stdout=o,stderr=e,timeout=180)
  except subprocess.TimeoutExpired:
   rows.append(dict(shard=sh,timeout=True));(p/'STATUS.json').write_text(json.dumps(rows));raise
 rows.append(dict(shard=sh,exit=r.returncode,seconds=time.monotonic()-st));(p/'STATUS.json').write_text(json.dumps(rows,indent=2))
 if r.returncode:raise RuntimeError('failed fixed shard')
