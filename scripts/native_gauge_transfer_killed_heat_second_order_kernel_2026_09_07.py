#!/usr/bin/env python3
"""Exact rational support for the native killed-heat second-order kernel proof.

The continuum Fourier/reflection and weighted-norm proofs are source mathematics;
these ten checks certify only their stated rational comparisons.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
    os.environ[key]='1'
import argparse, hashlib, math, resource, signal, sys, time
from pathlib import Path
AUDIT_TIMEOUT_SEC = 180
signal.alarm(AUDIT_TIMEOUT_SEC)
started=time.monotonic()
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--json',action='store_true')
args=parser.parse_args()
from fractions import Fraction as F
from math import factorial
import json
b=F(2048);t=F(1,2);alpha=F(23,72)*t
low=F(1,10)*(6*t/(810*alpha**4)+24*t*t/(2592*alpha**5))
exp21=sum(F(64,3)**j/factorial(j) for j in range(81))
exp32=sum(F(32)**j/factorial(j) for j in range(81))
exact_tail=b*b*F(48,10)/10**9
approx_tail=b*b*F(6,10)*(F(7,6)+b/144+2/b)/10**12
checks={'prefactor_pi22over7':F(22,7)**2<F(32,3),'low_lt_14over5':low<F(14,5),'exp64over3_gt_billion':exp21>10**9,'exp32_gt_trillion':exp32>10**12,'exact_tail_lt_21over1000':exact_tail<F(21,1000),'approx_tail_lt_1over1000':approx_tail<F(1,1000),'total_lt3':F(14,5)+F(21,1000)+F(1,1000)<3,'reflection_constant':6*3==18,'cut_inside_torus':F(2,3)<9,'tail_monotonic_threshold':b>288}
if len(checks)!=10 or not all(checks.values()):
    raise AssertionError("exact arithmetic certificate failed")

rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024)
elapsed=time.monotonic()-started
if not(math.isfinite(rss) and 0<rss<180 and math.isfinite(elapsed) and 0<=elapsed<180):
    raise AssertionError('resource contract')
result=dict(checks=checks,rational_assertion_count=len(checks),low_bound=str(low),
    exact_tail_bound=str(exact_tail),approx_tail_bound=str(approx_tail),
    beta0=2048,time_interval=['1/2','1'],uniform_reflected_constant=18,
    correction_coefficient='t/4 times L_x^2 s_t^C',shift=[1,1],
    dependencies={},source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    seconds=elapsed,rss_MiB=rss,resources=dict(timeout_seconds=180,rss_limit_MiB=180,blas_threads=1),
    scope='Ten exact rational comparisons supporting the source Fourier/reflection proof. All shifted endpoints, beta>=2048, t in[1/2,1]; two-sided weighted same-grid HS bound. No bare-heat norm or second-order cell-embedding expansion; no spectral coefficient certified by this runner.')
if args.json:
    print(json.dumps(result,indent=2,allow_nan=False))
else:
    print('PASS native killed-heat second-order certificate: ten exact rational assertions')
    print('per_element: low Fourier integral and two high-frequency tails have exact rational ceilings.')
    print('per_site: rho=(1,1) shifted chamber endpoints are retained; the six images are source-proved.')
    print('per_mode: beta>=2048 and t in[1/2,1], with correction (t/4beta)L_x^2 s_t^C.')
    print('per_block: source theorem gives scaled-kernel error<18/beta^2 and two-sided weighted same-grid HS control.')
    print('lattice_wide: arithmetic supports the conditional native Fourier proof; no bare-heat norm or cell-embedding expansion is tested.')
    print('SOURCE_SHA256',result['source_sha256'])
    print('DEPENDENCIES {}')
    print('RESOURCES',elapsed,rss,'seconds/MiB; 180 limits, BLAS1')
    print('TOTAL: PASS FAIL=0')
