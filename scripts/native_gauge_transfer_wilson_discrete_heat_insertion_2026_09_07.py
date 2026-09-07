#!/usr/bin/env python3
"""Exact rational certificate for native Wilson discrete-heat insertion."""
import os
for key in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS","VECLIB_MAXIMUM_THREADS"):os.environ[key]="1"
import signal,time,resource,sys
signal.alarm(180);started=time.monotonic()
"""Exact scalar certificate accompanying an analytical operator proof.

Does not compute spectra or certify infinite-dimensional lemmas numerically.
"""
from fractions import Fraction as F
import json,hashlib
from pathlib import Path
checks=[]
def ck(name,statement):
 if name in checks:raise AssertionError('duplicate check '+name)
 if not statement:raise AssertionError(name)
 checks.append(name)
beta0=2048
ck('exponential geometric remainder domain',F(3,beta0)<1)
extra=F(9,24)/(1-F(3,beta0))
ck('exact saddle exponential remainder coefficient',extra==F(768,2045))
c=29+extra
ck('same-lattice shifted saddle remainder below30',c<30)
insert=(F(1,2)+7*F(1,6))/4
ck('global insertion multiplier norm ceiling',insert==F(5,12))
ratio=F(1000,999)*(F(171,14)+F(2,3)+F(2618,14)*(F(1,12)+F(2,3*beta0)))
ck('imported refined ratio arithmetic',ratio==F(76675625,2685312) and ratio<29)
ck('denominator strictly positive fraction',1-F(1,beta0)-F(2618,14*beta0**2)>F(999,1000))
factor=lambda q:q*(q-7)/4
ck('negative multiplier factor at Q3',factor(F(3))==-3)
ck('positive multiplier factor at Q12',factor(F(12))==15)
ck('two multiplier factors not constant',factor(F(3))!=factor(F(12)))
result=dict(checks=checks,beta0=beta0,global_multiplier_C=29,shifted_saddle_remainder_C=str(c),insertion_norm_ceiling=str(insert),ratio_scalar=str(ratio),source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),scope='Exact rational margins only; contraction, dense range, compact sandwich and isolated-eigenvalue perturbation are proved analytically, not inferred from this certificate.')
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024);elapsed=time.monotonic()-started
if not(0<rss<180 and 0<=elapsed<180):raise AssertionError('resources')
result.update(dependencies={},seconds=elapsed,rss_MiB=rss,resources=dict(timeout_seconds=180,rss_limit_MiB=180,blas_threads=1))
if '--json' in sys.argv:print(json.dumps(result,indent=2,allow_nan=False))
else:
 print('PASS native Wilson exact discrete-heat insertion rational certificate')
 print('per_element: nine exact rational checks; no sampled spectral value is a proof input.')
 print('per_site: global dominant labels; unchanged exact recurrence and sampled shifted saddle.')
 print('per_mode: 29+768/2045<30 remainder and5/12 insertion ceiling.')
 print('per_block: compact signed insertion and top-Perron comparison are analytic proofs, not numerical checks.')
 print('lattice_wide: no full saddle expansion, Perron sign or physical mass-gap conclusion.')
 print('SOURCE_SHA256',result['source_sha256']);print('DEPENDENCIES {}')
 print('RESOURCES',elapsed,rss,'seconds/MiB;180 limits, BLAS1')
 print('TOTAL: PASS FAIL=0')
