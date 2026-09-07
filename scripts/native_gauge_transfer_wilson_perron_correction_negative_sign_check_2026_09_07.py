#!/usr/bin/env python3
"""Independent exact arithmetic for the analytic native Wilson Perron sign proof."""
import time,signal,resource,sys,math,argparse
START=time.monotonic();signal.alarm(180)
from fractions import Fraction as F
from math import factorial
import json,hashlib
from pathlib import Path
checks=[]
def ck(name,ok):
 if name in checks or not ok:raise AssertionError(name)
 checks.append(name)
low2=F(4,35)**2*F(2,3)**5
ck('low radial integral ceiling squared',low2<F(1,24)**2)
ck('sqrt6 ceiling squared',6<F(5,2)**2)
ck('sqrt3 ceiling squared',3<F(7,4)**2)
exp6=sum(F(6)**j/factorial(j) for j in range(17))
ck('positive Taylor lower bound exp6',exp6>400)
moment=36*factorial(1)+15*factorial(2)+2*factorial(3)+F(1,12)*factorial(4)
ck('high polynomial moment',moment==80)
ck('high radial ceiling',F(20)*F(5,2)/400==F(1,8))
J=F(7,324)*(F(1,24)+F(1,8));mu=F(2,243)
ck('weighted trace ceiling',J==F(7,1944))
ck('Perron moment upper bound',-1+J/mu==F(-9,16))
ck('absolute insertion upper bound',F(-9,16)*mu==F(-1,216))
ck('pointwise polynomial minimum',F(7,2)*(F(7,2)-7)/4==F(-49,16))
ck('radial H normalization rational factor',F(2,27)*F(3,4)==F(1,18))
ck('heat trial quotient rational factor',F(1,16)*F(1,27)*F(2,3)**4/F(1,18)==F(2,243))
R=lambda q:q*(q-7)/4
ck('middle interval low endpoint negative',R(F(2,3))+1<0)
ck('middle interval high endpoint negative',R(F(6))+1<0)
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024);elapsed=time.monotonic()-START
if not math.isfinite(rss) or not math.isfinite(elapsed) or rss>=180 or elapsed>=180:raise AssertionError(('resources',rss,elapsed))
result=dict(checks=checks,assertion_count=len(checks),relative_lower_bound='-49/16',relative_upper_bound='-9/16',absolute_upper_bound='-1/216',exp6_partial_sum=str(exp6),source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),scope='Exact scalar arithmetic supporting the analytical positive-operator/heat-kernel proof; no floating Perron data used',seconds=elapsed,rss_MiB=rss,resources=dict(timeout_seconds=180,rss_limit_MiB=180),runtime_input_files=[])
parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--json',action='store_true');args=parser.parse_args()
if args.json:print(json.dumps(result,indent=2,allow_nan=False))
else:
 print('PASS exact native Wilson Perron negative-sign arithmetic certificate')
 print('RESULT '+json.dumps(result,sort_keys=True,allow_nan=False))
 print('per_element: exact rational bounds and positive exponential-series lower bound checked.')
 print('per_site: chamber radial normalization and nonempty positive/negative multiplier regions are analytical source premises.')
 print('per_mode: actual normalized Perron correction bounded; no fitted eigenvector or eigenvalue input.')
 print('per_block: bounded multiplier truncation, positive-operator trace and Rayleigh trial are proved in the source, not numerically inferred.')
 print('lattice_wide: checked and not executed -- no explicit finite-beta onset, excited/ground ratio sign or physical mass-gap claim.')
 print('TOTAL: PASS FAIL=0 ASSERTIONS='+str(len(checks)))
