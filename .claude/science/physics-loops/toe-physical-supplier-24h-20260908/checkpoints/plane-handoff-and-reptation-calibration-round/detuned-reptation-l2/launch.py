import pathlib,json,hashlib,subprocess,time,sys
p=pathlib.Path(__file__).resolve().parent
for n,h in json.loads((p/'PRODUCTION_FREEZE.json').read_text()).items():
 if hashlib.sha256((p/n).read_bytes()).hexdigest()!=h:raise RuntimeError('freeze '+n)
micro=json.loads((p/'MICRO.json').read_text())['seconds'];t=time.monotonic();rows=[]
for cell in range(9):
 if 900-micro-(time.monotonic()-t)<180:raise RuntimeError('whole cell reserve')
 f=p/f'cell{cell}.json'
 if f.exists():raise RuntimeError('no overwrite/replacement')
 st=time.monotonic()
 with f.open('w') as out,(p/f'cell{cell}.stderr').open('w') as err:
  try:r=subprocess.run([sys.executable,str(p/'production.py'),'--cell',str(cell)],stdout=out,stderr=err,timeout=180)
  except subprocess.TimeoutExpired:
   rows.append(dict(cell=cell,timeout=True));(p/'STATUS.json').write_text(json.dumps(rows));raise
 rows.append(dict(cell=cell,exit=r.returncode,seconds=time.monotonic()-st));(p/'STATUS.json').write_text(json.dumps(rows,indent=2))
 if r.returncode:raise RuntimeError('failed cell')
