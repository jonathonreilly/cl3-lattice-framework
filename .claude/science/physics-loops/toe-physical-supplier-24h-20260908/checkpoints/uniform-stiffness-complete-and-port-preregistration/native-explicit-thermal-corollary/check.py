from fractions import Fraction as F
from math import factorial
import json
from pathlib import Path
B=Path(__file__).resolve().parent
# These are exact parameter implications, conditional on delta_infty >= 3/50.
pi_upper=F(22,7)
if not pi_upper*pi_upper<10:raise ValueError('pi-square comparator')
exp_point=F(7,10);exp_lower=sum((exp_point**j/factorial(j) for j in range(6)),F(0))
if not exp_lower>2:raise ValueError('log2 upper comparator')
delta=F(3,50)-F(30,2*32**2)-4*F(7,10)/200
if not delta>F(3,100):raise ValueError('thermal coefficient')
large_exp_lower=sum((F(105)**j/factorial(j) for j in range(211)),F(0));target=48**24*31*4096
if not large_exp_lower>target:raise ValueError('connected-set contraction')
r=dict(status='PASS conditional exact parameter implications',predicates=4,delta_thermal_rational_lower=str(delta),claimed_delta='3/100',native_kappa_over_h='3/800',minimum_M=32,thermal_stiffness_beta_h=200,connected_bound_beta_h=14000,connected_contraction='3/4',scope='No density-input acceptance, spectral evaluation, or phase assertion')
(B/'RESULT.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r))
