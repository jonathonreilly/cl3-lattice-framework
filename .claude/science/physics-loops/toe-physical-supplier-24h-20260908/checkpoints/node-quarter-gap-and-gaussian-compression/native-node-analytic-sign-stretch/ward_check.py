from fractions import Fraction as F
import json
from pathlib import Path
def add(a,b):return [[a[i][j]+b[i][j] for j in range(2)]for i in range(2)]
def scale(a,s):return [[s*x for x in r]for r in a]
def mul(*args):
 a=args[0]
 for b in args[1:]:a=[[sum(a[i][k]*b[k][j] for k in range(2))for j in range(2)]for i in range(2)]
 return a
def comm(a,b):return add(mul(a,b),scale(mul(b,a),-1))
g=[[F(1),F(0)],[F(0),F(-1)]]
n=0
for a in range(-3,4):
 for c in range(-3,4):
  wa=[[F(2),F(a)],[F(a),F(-2)]];wc=[[F(2),F(c)],[F(c),F(-2)]]
  ra=[[F(-2),F(1,3)],[F(1,3),F(-1)]];rc=[[F(-1),F(1,5)],[F(1,5),F(-3)]]
  old=add(add(mul(rc,ra),scale(mul(comm(wc,rc),g,ra),F(-1,2))),scale(mul(rc,g,comm(wa,ra)),F(1,2)))
  new=add(add(add(scale(mul(rc,ra),3),scale(mul(rc,g,add(wa,scale(wc,-1)),ra),F(1,2))),scale(mul(wc,rc,g,ra),F(-1,2))),scale(mul(rc,g,ra,wa),F(-1,2)))
  if old!=new:raise ValueError('Ward expansion')
  n+=4
out={'status':'PASS','exact_entry_checks':n,'scope':'noncommutative Ward expansion only; no native spectra','physical_runs':0}
Path(__file__).with_name('WARD_RESULT.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
