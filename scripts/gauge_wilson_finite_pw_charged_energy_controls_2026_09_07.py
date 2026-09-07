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
import time,resource,json,hashlib,itertools
from pathlib import Path
from fractions import Fraction as F
import sympy as s
t0=_started;checks=[];details={}
def ck(n,b):
 if not bool(b):raise AssertionError(n)
 checks.append(n)
for n in [2,3,4]:
 verts=list(itertools.product(range(n),repeat=3));edges={}
 for x in verts:
  for a in range(3):
   if x[a]+1<n:
    y=list(x);y[a]+=1;edges[(x,tuple(y))]=0
 faces=[]
 for x in verts:
  for a,b in itertools.combinations(range(3),2):
   if x[a]+1<n and x[b]+1<n:
    xa=list(x);xa[a]+=1;xb=list(x);xb[b]+=1;xab=xa.copy();xab[b]+=1
    xa,xb,xab=map(tuple,[xa,xb,xab]);f=[(x,xa),(x,xb),(xa,xab),(xb,xab)];f=[tuple(sorted(e)) for e in f];faces.append(set(f))
    for e in f:edges[e]+=1
 path=[];x=(0,0,0)
 for a in range(3):
  for step in range(n-1):
   y=list(x);y[a]+=1;y=tuple(y);path.append((x,y));x=y
 touch=sum(bool(f.intersection(path)) for f in faces)
 ck(f'box{n}_maximum_four_faces',max(edges.values())<=4)
 ck(f'box{n}_touch_budget',touch<=4*len(path))
 ck(f'box{n}_distinct_path',len(set(path))==3*(n-1))
 details[str(n)]={'links':len(edges),'faces':len(faces),'path':len(path),'touching':touch,'max_incidence':max(edges.values())}
energies=[]
for R in range(1,21):
 h=R*R-(R*R//4)+3*R
 vals=[p*p+p*(R-p)+(R-p)**2+3*R for p in range(R+1)]
 energies.append(h);ck(f'shell_R{R}',min(vals)==h)
P=s.eye(3)-s.ones(3)/3;Q=s.eye(3)-P;V=s.diag(0,1,2);W=s.diag(1,-1,1)
comm=P*V*P*W*P-P*W*P*V*P
rhs=P*W*Q*V*P-P*V*Q*W*P
ck('full_multiplications_commute',V*W==W*V)
ck('compression_commutator_identity',comm==rhs)
ck('naive_compressed_commutation_rejected',comm!=s.zeros(3))
ck('wrong_compression_sign_rejected',comm!=-rhs)
ck('projection_and_unitary',P*P==P and W.T*W==s.eye(3))
ck('positive_face_norm_bound',V.is_positive_semidefinite and (2*s.eye(3)-V).is_positive_semidefinite)
h=energies[9];theta=F(8,h)
ck('R10_normalization_budget',theta<1)
ck('R1_insufficient_budget_rejected',F(8,energies[0])>=1)
ck('denominator_positive',1-theta>0)
K=s.diag(0,4); excited=s.Matrix([0,1]);vac=s.Matrix([1,0])
ck('restricted_ground_replacement_adverse',(excited.T*K*excited)[0]==4 and (vac.T*K*vac)[0]==0 and min(K.eigenvals())==0)
ck('generator_normalization_discriminator',8*1==3*F(8,3) and 8*2!=3*F(8,3))
result={'TOTAL':len(checks),'checks':checks,'geometry':details,'shell_energies_R1_to20':energies,'compression_commutator':[[str(x) for x in comm.row(i)] for i in range(3)],'theta_R10_a_v_d1':str(theta),'scope':'Exact geometry, shell, budget and abstract compression controls; not a SU3 spectral trial or proof of the analytical bound.','source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'seconds':time.monotonic()-t0,'rss_MiB':_rss()}

_emit(result,40,{'per_element': {'checks': 20, 'scope': 'exact shell minimum for each R=1..20'}, 'per_site': {'checks': 9, 'scope': 'actual three cubic boxes: incidence, touching faces and distinct paths'}, 'per_mode': {'checks': 6, 'scope': 'exact nonzero compression commutator and sign/naive commutation adverse'}, 'per_block': {'checks': 3, 'scope': 'sufficient and insufficient normalization budgets, positive denominator'}, 'lattice_wide': {'checks': 2, 'scope': 'restricted-ground premise adverse and generator convention discriminator; no numerical SU3 spectral validation'}})
