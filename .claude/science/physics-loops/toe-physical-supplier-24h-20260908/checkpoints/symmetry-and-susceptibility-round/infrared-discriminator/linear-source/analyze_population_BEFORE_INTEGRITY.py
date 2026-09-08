import json,hashlib
from pathlib import Path
import numpy as np
p=Path(__file__).resolve().parent;grid=[0.,-.01,.01,-.005,.005,-.0025,.0025];out={};vectors={}
for pop in [128,256]:
 cells=[json.loads((p/f'population_p{pop}_c{c}.json').read_text()) for c in range(7)]
 for c,r in enumerate(cells):
  if r['population']!=pop or r['case']!=c or r['xi']!=grid[c] or len(r['rows'])!=16:raise ValueError('cell schema')
  for j,row in enumerate(r['rows']):
   if row['replica']!=j or row['seed']!=5700000+10000*(pop==256)+j or row['postconditions'] is not True:raise ValueError('seed/postcondition')
   if abs(row['shifted_energy']-(row['physical_energy']-r['shift']))>1e-12:raise ValueError('algebraic shifted energy')
 X=np.array([[cells[c]['rows'][j]['physical_energy'] for c in range(7)] for j in range(16)])
 if not np.isfinite(X).all():raise ValueError('nonfinite')
 cov=np.cov(X,rowvar=False,ddof=1);mcov=cov/16;means=X.mean(0);rows=[];cs=[]
 for h,mi,pi in [(.01,1,2),(.005,3,4),(.0025,5,6)]:
  w=np.zeros(7);w[0]=2/h**2;w[mi]=w[pi]=-1/h**2;z=X@w;value=float(z.mean());se=float(z.std(ddof=1)/4);cs.append(z)
  odd=(X[:,pi]-X[:,mi])/(2*h)
  rows.append(dict(h=h,primary=h==.01,chi=value,SE=se,positive=value>0,precision_pass=bool(value>0 and 4*se<=.1*value),odd_response=float(odd.mean()),odd_SE=float(odd.std(ddof=1)/4),replica_curvatures=z.tolist(),covariance_SE=float(np.sqrt(max(0,w@mcov@w)))))
 differences=[]
 for j in [1,2]:
  z=cs[j]-cs[0];v=float(z.mean());se=float(z.std(ddof=1)/4)
  differences.append(dict(secondary_h=rows[j]['h'],difference=v,SE=se,nominal_4SE_compatible=abs(v)<=4*se+2e-5))
 out[str(pop)]=dict(energy_means=means.tolist(),replica_energy_vectors=X.tolist(),sample_covariance=cov.tolist(),mean_covariance=mcov.tolist(),curvatures=rows,paired_step_differences=differences);vectors[pop]=cs
comparisons=[]
for j,h in enumerate([.01,.005,.0025]):
 x=vectors[256][j];y=vectors[128][j];v=float(x.mean()-y.mean());se=float(np.sqrt(x.var(ddof=1)/16+y.var(ddof=1)/16));comparisons.append(dict(h=h,difference=v,SE=se,nominal_4SE_compatible=abs(v)<=4*se))
print(json.dumps(dict(scope='nominal finite replica diagnostics, not certified bounds',shifted_energy_semantics='algebraic local-energy transform; no measured growth history',populations=out,population_comparisons=comparisons,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()),indent=2,allow_nan=False))
