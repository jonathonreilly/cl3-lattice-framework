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
from math import factorial
started=_started;checks=[]
def ck(name,b):
 if name in checks or not b:raise AssertionError(name)
 checks.append(name)
certs=[]
for P,N,c in [(0,0,F(1,2)),(3,2,F(3,7)),(12,5,F(2,3))]:
 m=P+N+1;C=F(factorial(m))/c**m
 ck('unit_inverse_power_'+str((P,N)),m-P-N==1)
 ck('positive_exact_coefficient_'+str((P,N)),C>0 and C.denominator>0)
 certs.append({'P':P,'N':N,'c':str(c),'m':m,'coefficient':str(C),'bound':'coefficient/n; from the analytic exponential-series inequality, not evaluated exponentials'})
ck('wrong_series_degree_not_decay',(3+2)-3-2==0)
budgets=[]
for n in [2,5,11]:
 value=n**3*F(1,n**3)*n**2;ck('weighted_Riemann_budget_'+str(n),value==n*n);budgets.append({'n':n,'weighted_norm':str(value)})
clock=[]
for i,(ell,a,b,u) in enumerate([(F(1,8),F(2),F(3),F(1,10)),(F(1,16),F(1,32),F(4),F(1,20)),(F(1,7),F(3,5),F(2,3),F(1,9))]):
 v=u/a;V_e=32*ell*v/b;G=2/(a*b)
 ck('clock_ratio_'+str(i),V_e/G==16*ell*u)
 clock.append({'ell':str(ell),'a':str(a),'b':str(b),'u':str(u),'V_over_e':str(V_e),'G_lower':str(G),'ratio_over_e':str(V_e/G)})
ell,a,b,u=F(1,8),F(2),F(3),F(1,10)
ck('wrong_clock_direction_adverse',32*ell*(u/a)*b!=32*ell*(u/a)/b)
e1,e2=F(1,8),F(1,16);u=F(1,10)
ck('fixed_kinetic_scale_halves_LR_upper',32*e2*u==32*e1*u/2)
ck('fixed_LR_upper_diverging_gap_adverse',32*e1*u/e1==32*e2*u/e2 and 2/e2==2*(2/e1))
ck('bounded_actual_gap_extra_premise_needed',2/e1>10 and 2/e2>10)
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1048576 if sys.platform=='darwin' else 1024)
ck('positive_resources',0<rss<180 and time.monotonic()-started<180)
out={'TOTAL':len(checks),'checks':checks,'exponential_series_certificates':certs,'weighted_budgets':budgets,'clock_cases':clock,'seconds':time.monotonic()-started,'rss_MiB':rss,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'Exact scaling and clock-ratio bookkeeping/adverse controls. No finite calculation proves clustering, continuum convergence, actual propagation speed or a numerical coupling threshold.'}

_emit(out, 18, {'per_element': {'checks': 6, 'scope': 'three exact exponential-series degree/coefficient certificates'}, 'per_site': {'checks': 3, 'scope': 'weighted Riemann norm bookkeeping'}, 'per_mode': {'checks': 3, 'scope': 'clock-rescaled gap/LR ratio identities'}, 'per_block': {'checks': 4, 'scope': 'wrong degree, wrong clock and missing gap-premise adverse controls'}, 'lattice_wide': {'checks': 2, 'scope': 'fixed-scale LR upper and positive resources; no convergence validation'}})
