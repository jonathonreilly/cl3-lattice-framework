from fractions import Fraction as F
from math import factorial
from pathlib import Path
import json,signal
signal.alarm(30)
r=Path('/private/tmp/toe-24h-probes-20260908/native-infinite-pair-gap-quarter-stretch');a=json.loads((r/'RESULT.json').read_text())
# Independently simplify each lower rectangle to a single integer rational.
tail=sum((F(7168*(24*j*j-2048),11*j*j*((j+1)**2+1792)**2) for j in range(16,320)),F(0))
if tail!=F(a['perpendicular_tail']):raise ValueError('rectangle equality')
old=json.loads(Path('/private/tmp/toe-24h-probes-20260908/native-infinite-pair-gap-cold-review/RESULT.json').read_text())
low=F(old['gap_lower'])
if low!=F(a['perpendicular_low']) or low+tail<=F(1,4):raise ValueError('perpendicular')
op=F(3,8)*(F(4,7)+F(40,343))
if op!=F(a['opposite_lower']) or op<=F(1,4):raise ValueError('opposite')
# Integral recursion independently gives integral(s²+7)^-4 / pi =5/(32*7^(7/2)).
# The rational coefficient of1/sqrt7 from g²/2 is512/2*5/(32*7**3).
if F(512,2)*F(5,32*7**3)!=F(40,343):raise ValueError('normalization')
err=F(90,8)*(32+4800+384)/sum(F(25)**n/factorial(n) for n in range(161))
if err!=F(a['laplace_tail_upper']) or err>=F(1,10**6):raise ValueError('tail')
print(json.dumps({'status':'PASS','perpendicular_lower_decimal':float(low+tail),'opposite_lower':str(op),'tail_upper_decimal':float(err),'predicate_groups':5,'physical_runs':0},indent=2))
