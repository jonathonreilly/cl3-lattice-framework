"""Synthetic single-pole budget only; no actual pole or full ledger fixture."""
from pathlib import Path
from fractions import Fraction as F
import types,json
P=Path(__file__).resolve().parent;s=types.ModuleType('schema');exec(compile((P/'schema.py').read_bytes(),str(P/'schema.py'),'exec'),s.__dict__)
for pole in(F(1),F(2)):
 low,high,w=s.budgets(pole,('1','1'),('-1','-1'),(F(0),F(0)));assert high==(0,0) and min(low)>0 and min(w)>0
 low2,high2,w2=s.budgets(pole,('1','1.00000000000000000001'),('-1','-1'),(F(0),F(0)));assert min(high2)>0 and all(b>a for a,b in zip(w,w2))
print(json.dumps({'status':'PASS_TINY_WIDTH_BUDGET','checks':4,'actual_pole_scans':0,'node_evaluations':0}))
