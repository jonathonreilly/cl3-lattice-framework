import runpy,contextlib,io,json
from pathlib import Path
with contextlib.redirect_stdout(io.StringIO()):d=runpy.run_path(str(Path(__file__).with_name('check.py')))
np=d['np'];sp=d['sparse'];A=d['A'];N=d['N'];nf=d['nf'];rows=[]
r0=np.zeros(864);r0[0]=1;RK=sp.eye(864)-N/24+A/24
for _ in range(480):r0=RK@r0
for V in [.93,.94,.95,.96,.97]:
 G=sp.eye(864)-(V*N-A)/24;r=r0.copy();samples=[]
 for sweep in range(80):
  for _ in range(24):r=G@r;r/=sum(r)
  if sweep>=40:samples.append(float(r@nf))
 ew=(V-1)*np.mean(samples);E=d['values'][V]
 rows.append({'V':V,'window_energy':float(ew),'exact_energy':E,'window_bias':float(ew-E),'endpoint_right_l1':float(sum(abs(r-d['psis'][V]/sum(d['psis'][V]))))})
print(json.dumps({'rows':rows,'scope':'Infinite-population deterministic window only; reused exact graph input, no finite-population claim.'},indent=2))
