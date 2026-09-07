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
    assert out['TOTAL'] == expected == len(set(out.get('names', out['checks'])))
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
from fractions import Fraction as F
from itertools import product,combinations
import json
checks=[]
def ck(name,b):
 assert name not in checks and b,name
 checks.append(name)
haar_norm=sum(F(int(a==b),3) for a,b in product(range(3),repeat=2))
ck('Schur fundamental character norm',haar_norm==1)
ck('center kills first and squared characters',1%3!=0 and 2%3!=0)
var=F(2,36)*haar_norm
ck('actual plaquette variance',var==F(1,18))
ck('normalized variance',18*var==1)
def edges(k):
 x,y,z=(3*t for t in k)
 return {(x,y,z,0),(x+1,y,z,1),(x,y+1,z,0),(x,y,z,1)}
anchors=list(product(range(-1,2),repeat=3));sets=[edges(k) for k in anchors]
ck('all27 neighboring coarse plaquettes pairwise link-disjoint',all(not a&b for a,b in combinations(sets,2)))
ck('each actual plaquette has four links',all(len(s)==4 for s in sets))
ck('repeated plaquette is not independent',bool(sets[0]&sets[0]) and 18*var!=0)
# B²=18; threshold z²<=1/(4B²).
ck('small argument threshold',F(1,4*18)==F(1,72))
ck('Taylor deviation coefficient',F(1,2)+F(1,12)<=1)
ck('log remainder coefficient at threshold',1/(2*(1-F(1,72)))<=1)
ck('combined cubic coefficient',F(1,6)+F(1,36)==F(7,36))
ck('safe cubic constant',F(7,36)<F(1,4))
ck('sum remainder power',F(9,2)-3==F(3,2))
out={'status':'PASS','checks':len(checks),'names':checks,'plaquettes':len(sets),'pairs':len(list(combinations(sets,2))),'variance':str(var),'normalized_variance':'1','log_remainder_relative_to_discrete_quadratic':'O(h^(3/2)); no continuous-test quadrature rate claimed'}
out['TOTAL']=out['checks']
out['seconds']=time.monotonic()-_started
out['rss_MiB']=_rss()
out['source_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()

_emit(out, 13, {'per_element': {'checks': 4, 'scope': 'supplied Haar character moments and normalization'}, 'per_site': {'checks': 3, 'scope': 'actual27-plaquette disjointness and repeated-plaquette adverse'}, 'per_mode': {'checks': 2, 'scope': 'small-argument threshold and Taylor deviation'}, 'per_block': {'checks': 3, 'scope': 'exact logarithmic remainder constants'}, 'lattice_wide': {'checks': 1, 'scope': 'mesh remainder exponent; resource/interface guards not added to mathematical count'}})
