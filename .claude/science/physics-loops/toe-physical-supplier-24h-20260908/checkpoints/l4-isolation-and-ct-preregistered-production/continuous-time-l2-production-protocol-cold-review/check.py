from pathlib import Path
from fractions import Fraction as F
import json,hashlib,sys,copy,math
src=Path('/private/tmp/toe-24h-probes-20260908/continuous-time-l2-calibration');sys.path.insert(0,str(src))
import analyze as a,launch,config
n=0
def need(c,m):
 global n
 n+=1
 if not c:raise RuntimeError(m)
freeze=json.loads((src/'FINAL_FREEZE.json').read_text())
for name,h in freeze['files'].items():need(hashlib.sha256((src/name).read_bytes()).hexdigest()==h,'sourcehash')
for name,h in json.loads((src/'RUNTIME.json').read_text())['files'].items():need(hashlib.sha256(Path(name).read_bytes()).hexdigest()==h,'runtimehash')
need(len({config.seed(i,j) for i in range(8) for j in range(16)})==128,'seed independence namespace')
base=[F(8),F(2),F(5),F(-1,2),F(1,3),F(-3,4),F(8),F(0),F(5),F(5,3),F(1,8),F(1,4)]
rows=[[v+F((i-7)*(j%3-1),100) for j,v in enumerate(base)] for i in range(16)];m=[sum(r[j] for r in rows)/16 for j in range(12)]
nf,x,x2,e,hh,xh=m[:6];D=(F(19,20)*nf-e)/(2*x)
g=[[F(0)]*12 for _ in range(5)];g[0][0]=F(19,20)/(2*x);g[0][1]=-D/x;g[0][3]=-1/(2*x);g[1][1]=-xh/x**2;g[1][3]=-1;g[1][5]=1/x;g[2]=[u+v for u,v in zip(g[0],g[1])];g[3][3]=-2*e;g[3][4]=1;g[4][1]=-2*x;g[4][2]=1
joint=[]
for r in rows:
 d=[v-u for u,v in zip(m,r)];joint.append(d+[sum(q*v for q,v in zip(gg,d)) for gg in g])
C=[[sum(r[i]*r[j] for r in joint)/F(15*16) for j in range(17)] for i in range(17)]
s=a.stats([[float(v) for v in r] for r in rows])
for i in range(17):
 for j in range(17):need(abs(float(C[i][j])-s['joint_raw_derived_mean_covariance'][i][j])<1e-14,'independent joint covariance')
need(a.stats([[0.]*12 for _ in range(16)])['denominator_positive'] is False,'invalid pooledX')
need('derived' not in a.raw_stats([[1.,0.]+[0.]*10 for _ in range(16)]),'raw half no ratio')
arms=[dict(gates={'pass_all':True},half_flags=[False]*12,measured_face_coverage=[True]*16) for _ in range(8)];contr=[dict(arms=p,flags=[False]*12,derived_flags=[False]*5) for p in ([1,3],[5,7])]
need(a.acceptance(arms,contr),'base acceptance')
for i in range(8):
 z=copy.deepcopy(arms);z[i]['gates']['pass_all']=False;need(a.acceptance(z,contr)==(i%2==0),'fixedprimary gates')
 z=copy.deepcopy(arms);z[i]['half_flags'][0]=True;need(a.acceptance(z,contr)==(i%2==0),'fixedprimary halves')
 z=copy.deepcopy(arms);z[i]['measured_face_coverage'][0]=False;need(not a.acceptance(z,contr),'allarm measuredcoverage')
for j in range(2):
 for key,length in [('flags',12),('derived_flags',5)]:
  for k in range(length):
   z=copy.deepcopy(contr);z[j][key][k]=True;need(not a.acceptance(arms,z),'all longstart flags')
for rss,elapsed,real in [(1,1,1),(384*1048576,180,180)]:need(launch.resource_receipt(f'real {real}\n{rss} maximum resident set size',elapsed)['outer_rss_bytes']==rss,'boundaryresources')
for text,elapsed in [('real 1\n402653185 maximum resident set size',1),('real 1\n1 maximum resident set size',180.001),('real nan\n1 maximum resident set size',1)]:
 try:launch.resource_receipt(text,elapsed)
 except ValueError:need(True,'badexternal rejected')
 else:need(False,'badexternal accepted')
Path(__file__).with_name('RESULT.json').write_text(json.dumps({'checks':n,'freeze':hashlib.sha256((src/'FINAL_FREEZE.json').read_bytes()).hexdigest(),'scope':'deterministic covariance/gates/resources only; no oracle-trained data or stochastic launch'},indent=2)+'\n')
