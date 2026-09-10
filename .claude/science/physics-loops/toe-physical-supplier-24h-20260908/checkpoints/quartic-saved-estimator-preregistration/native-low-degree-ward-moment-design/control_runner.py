import subprocess,time,sys,json
from pathlib import Path
start=time.monotonic();peak=0
with open('CONTROLS.json','w') as out,open('CONTROL_STDERR.txt','w') as err:
 p=subprocess.Popen([sys.executable,'-B','-c','import signal,runpy; signal.alarm(29); runpy.run_path("controls.py",run_name="__main__")'],stdout=out,stderr=err)
 while p.poll() is None:
  v=subprocess.run(['ps','-o','rss=','-p',str(p.pid)],capture_output=True,text=True).stdout.strip()
  if v:peak=max(peak,int(v)*1024)
  if peak>384*1024**2 or time.monotonic()-start>29.5:
   p.kill();p.wait();raise RuntimeError('synthetic resource guard')
  time.sleep(.01)
Path('CONTROL_RECEIPT.json').write_text(json.dumps({'exit_code':p.returncode,'seconds':time.monotonic()-start,'sampled_child_rss':peak,'cap_bytes':384*1024**2,'scope':'tiny synthetic only'})+'\n')
if p.returncode:raise SystemExit(p.returncode)
