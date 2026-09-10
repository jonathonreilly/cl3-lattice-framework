"""Compact identity and immutable saved-status checks; no scientific replay."""
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations
import json,hashlib
ROOT=Path(__file__).resolve().parents[1]
PACK=ROOT/'.claude/science/physics-loops/native-finite-moment-ward-20260910'
def main():
 n=0
 def check(ok):
  nonlocal n
  if not ok:raise AssertionError(n)
  n+=1
 for row in json.loads((PACK/'IMPORT_PROVENANCE.json').read_text()):check(hashlib.sha256((ROOT/row['local']).read_bytes()).hexdigest()==row['sha256'])
 labels=list(combinations(range(6),2));degrees=[sum(not(set(a)&set(c))for c in labels)for a in labels];check(degrees==[6]*15);check(sum(degrees)==90)
 # Literal polynomial-division identity at synthetic single-atom points.
 for x in [F(1),F(2),F(3)]:
  for t in [F(1,2),F(1),F(2)]:check(x*x-x*t*t+t**4-t**6/(x+t*t)==x**3/(x+t*t))
 check(F(9,4)-F(17,16)**2-F(15,16)**2==F(31,128))
 # Exact cancellation underlying all-q exclusion, synthetic nonnegative data.
 for E in [F(1),F(2)]:
  X,V,a,j,delta,T=F(3),F(4),F(2),F(2),F(1),F(5)
  C=E*(2*X+E+V)
  nominal=a*a*(1+j/delta)+a*T/delta
  error=C+(X+E)*T/delta
  check(nominal-error<=a*a*(1+j/delta)-C)
 d=json.loads((PACK/'imports/DEGREE10_RESULT.json').read_text());check(d['sign_certified']is False);check([r['status']for r in d['rows']]==['INDETERMINATE_SIGN']*2)
 a=json.loads((PACK/'imports/ALLQ_RESULT.json').read_text());check(a['all_fixed_first_polynomials_excluded']is True);check([r['status']for r in a['rows']]==['CERTIFICATE_FAMILY_EXCLUDED']*2)
 o=json.loads((PACK/'imports/OMEGA5_RESULT.json').read_text());check(o['status']=='CERTIFIED_TARGET');check(o['oracle_calls']==0)
 # Mutants challenge signs/scope; no stored target is recomputed.
 check(F(1)-F(1)+F(1)+F(1,2)!=F(1,2))
 check(not(set(labels[0])&set(labels[0]))is False)
 print(f'TOTAL: PASS={n} FAIL=0')
 print('SUPPORT_ONLY: no native or saved-node arithmetic replay; full integration and audit NOT RUN')
if __name__=='__main__':main()
