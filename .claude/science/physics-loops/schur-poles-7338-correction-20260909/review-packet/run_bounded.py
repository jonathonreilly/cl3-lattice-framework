import os,sys,time,subprocess,signal,pathlib,json
O=pathlib.Path(__file__).parent
env=os.environ.copy();env.update({x:'1' for x in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS']});env['PYTHONDONTWRITEBYTECODE']='1'
start=time.monotonic();peak=0;reason=None
with (O/'independent_check.log').open('w') as out:
 p=subprocess.Popen([sys.executable,'-u',str(O/'independent_check.py')],stdout=out,stderr=subprocess.STDOUT,env=env,start_new_session=True)
 while p.poll() is None:
  rows=subprocess.check_output(['ps','-axo','pgid=,rss='],text=True).splitlines();rss=sum(int(x.split()[1])*1024 for x in rows if x.split() and int(x.split()[0])==p.pid);peak=max(peak,rss)
  if time.monotonic()-start>30 or rss>2*1024**3:
   reason='wall' if time.monotonic()-start>30 else 'rss';os.killpg(p.pid,signal.SIGKILL);break
  time.sleep(.1)
 p.wait()
r={'returncode':p.returncode,'elapsed':time.monotonic()-start,'process_group_peak_rss_bytes':peak,'limit_seconds':30,'limit_rss_bytes':2*1024**3,'termination':reason,'blas_threads':1};(O/'bounded_receipt.json').write_text(json.dumps(r,indent=2));print(r)
