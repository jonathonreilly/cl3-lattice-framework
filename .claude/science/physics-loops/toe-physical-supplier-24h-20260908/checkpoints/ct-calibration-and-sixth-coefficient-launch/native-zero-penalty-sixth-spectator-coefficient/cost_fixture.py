from pathlib import Path
import time,signal,contextlib,io,runpy,json,resource,os,hashlib
start=time.monotonic();signal.alarm(30)
p=Path(__file__).resolve().parent
# Imported own deterministic frame controls must not reset the outer alarm.
src=(p/'frame_control.py').read_text();src=src.replace('signal.alarm(180);start=time.monotonic();count=0','start=time.monotonic();count=0')
d={'__name__':'cost_frame'}
with contextlib.redirect_stdout(io.StringIO()):exec(compile(src,str(p/'frame_control.py'),'exec'),d)
np=d['np'];kf=d['kf'].copy()
for e in (0,1):
 i,j=d['edges'][e];kf[i,j]*=-1;kf[j,i]*=-1
s=time.monotonic();H=d['fock'](d['B'].T@kf@d['C']);A=H+5*d['math'].sqrt(24)*np.eye(512);build=time.monotonic()-s
rhs=np.zeros(512);rhs[0]=1;s=time.monotonic();x=np.linalg.solve(A,rhs);solve=time.monotonic()-s
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1048576 if os.uname().sysname=='Darwin' else 1024)
out={'scope':'one deterministic cost-only solve; NOT a coefficient or certified interval','seconds':time.monotonic()-start,'build_seconds':build,'solve_seconds':solve,'rss_mib':rss,'residual_norm':float(np.linalg.norm(A@x-rhs)),'frame_sha256':hashlib.sha256((p/'frame_control.py').read_bytes()).hexdigest()}
if out['seconds']>=30 or rss>=384:raise RuntimeError(out)
print(json.dumps(out,indent=2))
