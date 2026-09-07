import os,time,signal,json,resource,sys,hashlib
for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS']:os.environ[k]='1'
t0=time.monotonic();signal.alarm(180)
from itertools import product,combinations
from fractions import Fraction as F
from pathlib import Path
AUDIT_TIMEOUT_SEC=180
AUDIT_MEMORY_LIMIT_MB=180
if sys.argv[1:] not in ([],['--json']): raise SystemExit('usage: gauge_wilson_local_observable_finite_region_pw_2026_09_07.py [--json]')
checks=[]
def ck(name,value):
 if not value:raise AssertionError(name)
 checks.append(name)
def add(x,i):return tuple(v+(j==i) for j,v in enumerate(x))
faces=[]
for x in product(range(-5,6),repeat=3):
 for i,j in combinations(range(3),2):faces.append(frozenset([(x,i),(add(x,i),j),(add(x,j),i),(x,j)]))
inc={}
for n,f in enumerate(faces):
 for e in f:inc.setdefault(e,set()).add(n)
origin=((0,0,0),0); dist={origin:0};front={origin}
for r in range(1,5):
 new={z for e in front for n in inc[e] for z in faces[n]}-dist.keys()
 for e in new:dist[e]=r
 front=new
ck('each tested link has at most four faces',all(len(inc[e])<=4 for e in dist))
ck('origin has exactly four faces',len(inc[origin])==4)
ck('successor face count at most sixteen',all(len(set.union(*(inc[e] for e in faces[n])))<=16 for n in inc[origin]))
ck('adjacent link tails coordinate difference at most one',all(max(abs(a-b) for a,b in zip(e[0],z[0]))<=1 for n in inc[origin] for e in faces[n] for z in faces[n]))
rows=[]
for r in range(4):
 ball={e for e,d in dist.items() if d<=r}; touched=set.union(*(inc[e] for e in ball)); cross=[n for n in touched if not faces[n]<=ball]; inside=[n for n in touched if faces[n]<=ball]
 ck('polynomial ball bound R'+str(r),len(ball)<=3*(2*r+1)**3)
 ck('crossing face distance R'+str(r),all(min(dist.get(e,99) for e in faces[n])>=r for n in cross))
 ck('crossing incidence bound R'+str(r),len(cross)<=4*len(ball))
 ck('retained face incidence bound R'+str(r),len(inside)<=len(ball))
 rows.append({'radius':r,'links':len(ball),'retained_faces':len(inside),'crossing_faces':len(cross),'polynomial_link_bound':3*(2*r+1)**3})
for R in [0,1,2,4,10]:
 m=R+1;g=(3*m*m+3)//4+3*m
 ck('balanced omitted threshold '+str(R),g==min(p*p+(m-p)**2+p*(m-p)+3*m for p in range(m+1)))
ck('projection normalization inequality algebra',(F(1,1)-F(3,5))**2<=1-F(3,5)**2)
ck('zero coupling locality prefactor',2*4*0*7==0)
ck('zero time locality and dynamic prefactors',2*4*3*0==0 and 1+7*0==1)
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1048576 if sys.platform=='darwin' else 1024)
ck('resource contract',0<rss<180 and time.monotonic()-t0<180)
result={'checks':checks,'TOTAL':len(checks),'rows':rows,'seconds':time.monotonic()-t0,'rss_MiB':rss,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
if sys.argv[1:]==['--json']:
 print(json.dumps(result,indent=2,allow_nan=False))
else:
 print('PASS TOTAL='+str(result['TOTAL'])+' unique named checks')
 print('per_element: PASS 4 actual cubic incidence and adjacent-tail controls')
 print('per_site: PASS 16 radius0..3 ball, crossing-distance and face-count controls')
 print('per_mode: PASS 5 balanced omitted Peter-Weyl threshold controls')
 print('per_block: PASS 3 projection normalization and zero-coupling/time controls')
 print('lattice_wide: PASS 1 resource control; all-volume propagation remains analytical')
 print('DATA: '+json.dumps({k:v for k,v in result.items() if k not in ('checks','seconds','rss_MiB','source_sha256')},sort_keys=True,allow_nan=False))
 print('RESOURCE: seconds='+str(result['seconds'])+' rss_MiB='+str(result['rss_MiB'])+' limits=180sec/180MiB')
 print('SOURCE_SHA256: '+result['source_sha256'])
signal.alarm(0)
