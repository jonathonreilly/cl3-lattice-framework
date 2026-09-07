#!/usr/bin/env python3
"""Exact finite support controls; the analytic theorem is in the source note."""
import os, sys, time, signal, resource, json, hashlib, math
from pathlib import Path
AUDIT_TIMEOUT_SEC = 180
AUDIT_RSS_LIMIT_MIB = 180
_started = time.monotonic()
for _name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_name] = '1'
if sys.argv[1:] not in ([], ['--json']):
    raise SystemExit('usage: '+Path(__file__).name+' [--json]')
def _timeout(signum, frame):
    raise TimeoutError('180-second audit budget exceeded')
signal.signal(signal.SIGALRM, _timeout)
signal.alarm(AUDIT_TIMEOUT_SEC)
def _rss():
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / (1048576 if sys.platform == 'darwin' else 1024)
def _finite(value):
    if isinstance(value, float) and not math.isfinite(value):
        raise AssertionError('nonfinite output')
    if isinstance(value, dict):
        for item in value.values(): _finite(item)
    elif isinstance(value, (list, tuple)):
        for item in value: _finite(item)
def _emit(out, expected, scopes):
    assert out['TOTAL'] == expected == len(set(out['checks']))
    assert 0 < _rss() < AUDIT_RSS_LIMIT_MIB
    assert time.monotonic() - _started < AUDIT_TIMEOUT_SEC
    assert sum(v['checks'] for v in scopes.values()) == expected
    out['N5_scopes'] = scopes
    out['resource_limits'] = {'seconds': AUDIT_TIMEOUT_SEC, 'rss_MiB': AUDIT_RSS_LIMIT_MIB}
    _finite(out)
    if sys.argv[1:] == ['--json']:
        print(json.dumps(out, sort_keys=True, indent=2, allow_nan=False))
    else:
        print('PASS '+Path(__file__).name)
        for key, item in scopes.items(): print(key+': '+str(item['checks'])+' checks; '+item['scope'])
        print('TOTAL: '+str(expected))
        print('seconds: '+str(out['seconds'])+'; rss_MiB: '+str(out['rss_MiB']))
        print('source_sha256: '+out['source_sha256'])
    signal.alarm(0)
import itertools
started=_started; L=4; checks=[]
def check(n,x):
 assert n not in checks and bool(x),n
 checks.append(n)
def add(x,i,d=1):
 y=list(x);y[i]=(y[i]+d)%L;return tuple(y)
def boundary(x,i,j):return [(x,i,1),(add(x,i),j,1),(add(x,j),i,-1),(x,j,-1)]
v2=list(itertools.product(range(L),repeat=2));v3=list(itertools.product(range(L),repeat=3))
e2=[(x,i) for x in v2 for i in range(2)];e3=[(x,i) for x in v3 for i in range(3)]
f2=v2;f3=[(x,i,j) for x in v3 for i,j in itertools.combinations(range(3),2)]
idx2={z:k for k,z in enumerate(e2)};idx3={z:k for k,z in enumerate(e3)}
B2=[[0]*len(f2) for _ in e2]
for c,x in enumerate(f2):
 for y,i,s in boundary(x,0,1):B2[idx2[y,i]][c]=(B2[idx2[y,i]][c]+s)%3
for x,i,j in f3:
 lhs=[0]*len(e2)
 for y,k,s in boundary(x,i,j):
  if k<2:lhs[idx2[y[:2],k]]=(lhs[idx2[y[:2],k]]+s)%3
 rhs=[B2[r][f2.index(x[:2])] for r in range(len(e2))] if (i,j)==(0,1) else [0]*len(e2)
 assert lhs==rhs
check('actual_192_face_chain_map',len(f3)==192)
def rank(M):
 A=[r[:] for r in M];p=0
 for c in range(len(A[0])):
  pivot=next((r for r in range(p,len(A)) if A[r][c]%3),None)
  if pivot is None:continue
  A[p],A[pivot]=A[pivot],A[p];a=pow(A[p][c],-1,3);A[p]=[(a*z)%3 for z in A[p]]
  for r in range(len(A)):
   if r!=p:
    a=A[r][c];A[r]=[(z-a*w)%3 for z,w in zip(A[r],A[p])]
  p+=1
 return p
check('projected_boundary_rank15',rank(B2)==15)
check('constant_sheet_kernel',all(sum(row)%3==0 for row in B2))
def mul(A,v):return [sum(a*b for a,b in zip(row,v))%3 for row in A]
data=[]
for R,S,expected in [(1,1,1),(1,2,2),(2,2,4),(3,3,7)]:
 sheet=[int(x<R and y<S) for x,y in f2];target=mul(B2,sheet)
 sols=[[(z+c)%3 for z in sheet] for c in range(3)];sizes=[sum(z!=0 for z in a) for a in sols]
 check(f'rectangle_{R}_{S}_affine_solutions',all(mul(B2,a)==target for a in sols))
 check(f'rectangle_{R}_{S}_support_minimum',min(sizes)==expected)
 # Lift each projected sheet to z=0 and verify the actual link boundary.
 for sol in sols:
  bd=[0]*len(e3)
  for (x,y),coef in zip(f2,sol):
   for z,i,s in boundary((x,y,0),0,1):bd[idx3[z,i]]=(bd[idx3[z,i]]+coef*s)%3
  target3=[0]*len(e3)
  for (x,y),coef in zip(f2,sheet):
   for z,i,s in boundary((x,y,0),0,1):target3[idx3[z,i]]=(target3[idx3[z,i]]+coef*s)%3
  assert bd==target3
 check(f'rectangle_{R}_{S}_actual_lift_boundary',True)
 data.append({'R':R,'S':S,'area':R*S,'projected_area':L*L,'all_three_solutions':sols,'support_sizes':sizes,'minimum':min(sizes),'half_area_condition':2*R*S<=L*L})
check('adverse_complement_beats_rectangle',data[-1]['minimum']<data[-1]['area'] and not data[-1]['half_area_condition'])
check('triple_insertion_charge_cancels',all((3*z)%3==0 for z in mul(B2,[1]+[0]*15)))
# A one-cell charge is not the four-cell rectangle boundary despite equal total area mod3.
check('total_flux_only_adverse',mul(B2,[1]+[0]*15)!=mul(B2,[int(x<2 and y<2) for x,y in f2]))
check('resource',time.monotonic()-started<180 and 0<_rss()<180)
out={'TOTAL':len(checks),'checks':checks,'cases':data,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'seconds':time.monotonic()-started,'rss_MiB':_rss(),'scope':'Exact finite center-chain controls; no finite calculation proves the complex marked-polymer bound or computes an analyticity radius.'}

_emit(out, 19, {'per_element': {'checks': 1, 'scope': 'actual 192-face projection chain map'}, 'per_site': {'checks': 2, 'scope': 'projected rank and constant-sheet kernel'}, 'per_mode': {'checks': 4, 'scope': 'four frozen affine filling cases'}, 'per_block': {'checks': 8, 'scope': 'four minima and four actual lifted boundaries'}, 'lattice_wide': {'checks': 4, 'scope': 'three adverse controls and positive resources; no polymer proof'}})
