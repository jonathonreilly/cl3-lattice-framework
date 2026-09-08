import time,os,sys,json,subprocess,hashlib
from pathlib import Path
p=Path(__file__).resolve().parent;out=p/'COEFFICIENT_OUTPUT'
if out.exists():raise RuntimeError('one attempt only')
out.mkdir();start=time.monotonic();charged=5.0;rows=[];env=dict(os.environ,OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',PYTHONDONTWRITEBYTECODE='1')
for bridge in (0,3,9,12,36,96):
 if 600-charged-(time.monotonic()-start)<180:raise RuntimeError('insufficient reserved cell budget')
 t=time.monotonic()
 try:r=subprocess.run([sys.executable,str(p/'run_bridge.py'),'--bridge',str(bridge),'--output',str(out/('bridge_'+str(bridge)+'.json'))],capture_output=True,text=True,timeout=180,env=env)
 except subprocess.TimeoutExpired as e:
  (out/'FAILURE.json').write_text(json.dumps({'bridge':bridge,'timeout':180,'elapsed':time.monotonic()-start,'prior_charge':charged}));raise
 (out/('bridge_'+str(bridge)+'.stdout')).write_text(r.stdout);(out/('bridge_'+str(bridge)+'.stderr')).write_text(r.stderr);rows.append({'bridge':bridge,'wall_seconds':time.monotonic()-t,'returncode':r.returncode});(out/'LEDGER.json').write_text(json.dumps({'rows':rows,'prior_charge':charged,'total_seconds':charged+time.monotonic()-start},indent=2))
 if r.returncode:raise RuntimeError('failed bridge '+str(bridge))
# No fresh physics execution here. Sum certified interval endpoints outward.
from math import nextafter,inf
lower=upper=0.0
for row in rows:
 f=out/('bridge_'+str(row['bridge'])+'.json');z=json.loads(f.read_text());lower=nextafter(lower+z['interval'][0],-inf);upper=nextafter(upper+z['interval'][1],inf);row['sha256']=hashlib.sha256(f.read_bytes()).hexdigest()
(out/'SUMMARY.json').write_text(json.dumps({'interval':[lower,upper],'excludes_zero':lower>0 or upper<0,'rows':rows,'seconds_including_prior_charge':charged+time.monotonic()-start,'scope':'Adjacent ordered spectator bilinear only, t=1; IEEE754 certificate assumptions, no full leading operator claim'},indent=2)+'\n')
print((out/'SUMMARY.json').read_text())
