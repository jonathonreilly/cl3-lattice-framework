import ast,json
from fractions import Fraction
from itertools import product
from pathlib import Path
p=Path(__file__).parents[1]/'originals/6009/scripts/frontier_cycle900_harmonic_repair_2026_07_28.py'
t=ast.parse(p.read_text())
names={'ptrim','padd','pmul','pscale','mq_primes','mq_norm'}
ns={'Fraction':Fraction,'product':product}
exec(compile(ast.Module(body=[n for n in t.body if isinstance(n,ast.FunctionDef) and n.name in names],type_ignores=[]),str(p),'exec'),ns)
a={frozenset():(Fraction(1),),frozenset({2}):(Fraction(1),)}
actual=ns['mq_norm'](a)
assert actual==()
print(json.dumps({'actual_original_norm_of_1_plus_sqrt2':list(actual),'actual_means':'zero polynomial','correct_norm':'-1','identity':'(1+sqrt(2))(1-sqrt(2))=1-2=-1','functions':sorted(names)},indent=2))
