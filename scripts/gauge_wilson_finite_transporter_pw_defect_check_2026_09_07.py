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
started=_started
import sympy as s
checks=[]
def ck(name,b):
 if name in checks or not b:raise AssertionError(name)
 checks.append(name)
def zero(M):return all(s.simplify(x)==0 for x in M)
def eps(a,b,c):return s.LeviCivita(a,b,c)
def F(k,l):return 1+3*k+l
def A(k,l):return 10+3*k+l
def ix(basis,color):return 3*basis+color
U=s.zeros(57)
for i in range(3):
 for j in range(3):
  U[ix(F(i,j),i),ix(0,j)]=1/s.sqrt(3)
  for k in range(3):
   for l in range(3):
    if i==k and j==l:U[ix(0,i),ix(A(k,l),j)]=1/s.sqrt(3)
    for a in range(3):
     for b in range(3):
      z=eps(a,i,k)*eps(b,j,l)/2
      if z:U[ix(A(a,b),i),ix(F(k,l),j)]=z
T=s.diag(1,-1,0);q=[0]+[-T[k,k] for k in range(3) for l in range(3)]+[T[k,k] for k in range(3) for l in range(3)]
Q=s.kronecker_product(s.diag(*q),s.eye(3));Tc=s.kronecker_product(s.eye(19),T)
G=s.simplify(U.H*U);D=s.eye(57)-G
Pv=s.diag(*([1]*3+[0]*54));shell=s.eye(57)-Pv
v=s.eye(57)[:,ix(F(0,0),0)]
ck('actual_R1_dimension57',U.shape==(57,57))
ck('Cartan_covariance_literal_matrix',zero(Q*U-U*Q+Tc*U))
ck('wrong_Cartan_sign_adverse',not zero(Q*U-U*Q-Tc*U))
ck('Gram_hermitian',G==G.H)
ck('Gram_idempotent_contraction',zero(G*G-G))
ck('Gram_rank15_by_projector_trace',s.trace(G)==15)
ck('defect_projector',zero(D*D-D))
ck('defect_rank42_by_projector_trace',s.trace(D)==42)
ck('defect_shell_support',zero(D-shell*D*shell))
ck('vacuum_color_interior_isometry',zero(Pv*G*Pv-Pv))
ck('highest_weight_kernel',zero(U*v))
ck('defect_norm1_witness',D*v==v and (v.H*v)[0]==1)
ck('energy_shell_bound',zero((shell-D)*(shell-D)-(shell-D)) and s.trace(shell-D)>=0)
ck('finite_trace_square_offset38',s.trace((Q+Tc)**2)-s.trace(Q**2)==38)
ck('fake_identity_unitary_breaks_covariance',not zero(Q-Q+Tc))
ck('R0_transporter_zero_from_Haar_first_moment',zero(Pv*U*Pv))
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1048576 if sys.platform=='darwin' else 1024)
ck('positive_resources',0<rss<180 and time.monotonic()-started<180)
entries=[[i,j,str(U[i,j])] for i in range(57) for j in range(57) if U[i,j]!=0]
out={'TOTAL':len(checks),'checks':checks,'dimension':57,'basis':'vacuum, fundamental(k,l), antifundamental(k,l), each followed by color0..2','nonzero_U_entries':entries,'Gram_trace':str(s.trace(G)),'defect_trace':str(s.trace(D)),'Cartan_link_generator':list(map(str,q)),'highest_weight_index':ix(F(0,0),0),'seconds':time.monotonic()-started,'rss_MiB':rss,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'Actual R1 full-irrep Haar multiplication compression; analytic Haar coefficients supplied. Finite matrices do not replace the all-R fusion, trace obstruction or energy/path proof.'}

_emit(out, 17, {'per_element': {'checks': 3, 'scope': 'actual57 dimension, trace-square offset and R0 block'}, 'per_site': {'checks': 2, 'scope': 'literal Cartan covariance and wrong-sign adverse'}, 'per_mode': {'checks': 4, 'scope': 'exact Gram Hermiticity/projection/rank and defect projection'}, 'per_block': {'checks': 4, 'scope': 'defect rank/shell, interior isometry and highest-weight kernel'}, 'lattice_wide': {'checks': 4, 'scope': 'norm-one witness, energy-shell control, fake-unitary adverse and resources; no all-R proof by finite test'}})
