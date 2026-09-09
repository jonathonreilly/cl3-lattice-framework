from pathlib import Path
import subprocess,os,time,json,signal,hashlib,sys,resource
E=Path(__file__).resolve().parent
cmd=[sys.executable,str(E/'decisive_controls.py')]
env=dict(os.environ);env.update({k:'1' for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS']});env['PYTHONDONTWRITEBYTECODE']='1'
pre={'command':cmd,'cost':'Read finite L5 runner: two 75-edge Hessians, batch75 x5 x15; ten simplex symbolic gradient functions plus50 hinge stars at import. No parent mains or large period campaigns. Independent metric/gauge and Schur controls.','wall_cap_s':30,'rss_cap_bytes':2*1024**3,'env_overrides':{k:env[k] for k in env if k.endswith('NUM_THREADS') or k in ['VECLIB_MAXIMUM_THREADS','PYTHONDONTWRITEBYTECODE']}}
(E/'CONTROL_PREFLIGHT.json').write_text(json.dumps(pre,indent=2)+'\n')
t0=time.monotonic(); peak=0; killed=None
with (E/'controls.stdout').open('wb') as out,(E/'controls.stderr').open('wb') as err:
 p=subprocess.Popen(cmd,cwd=E,env=env,stdout=out,stderr=err,start_new_session=True)
 while p.poll() is None:
  s=subprocess.run(['ps','-o','rss=','-p',str(p.pid)],capture_output=True,text=True)
  rss=sum(int(x) for x in s.stdout.split())*1024;peak=max(peak,rss)
  if time.monotonic()-t0>30:killed='wall'
  if rss>2*1024**3:killed='rss'
  if killed:os.killpg(p.pid,signal.SIGKILL);break
  time.sleep(.005)
 code=p.wait()
r={'command':cmd,'exit_code':code,'elapsed_s':time.monotonic()-t0,'sampled_peak_rss_bytes':peak,'limit_kill':killed,'limits':pre,'script_sha256':hashlib.sha256((E/'decisive_controls.py').read_bytes()).hexdigest(),'scope':'independent tiny controls and final finite L5 primary; no cache mutation'}
(E/'CONTROL_EXECUTION.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r));print((E/'controls.stdout').read_text());print((E/'controls.stderr').read_text())
