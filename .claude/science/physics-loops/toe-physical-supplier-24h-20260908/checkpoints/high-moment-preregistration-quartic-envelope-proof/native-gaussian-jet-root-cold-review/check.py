# Independent integer endpoint extremum checks, no native/table evaluation.
import pathlib,importlib.util,json
from fractions import Fraction as F
P=pathlib.Path('/private/tmp/toe-24h-probes-20260908/native-gaussian-jet-root-review/independent.py');sp=importlib.util.spec_from_file_location('I',P);I=importlib.util.module_from_spec(sp);sp.loader.exec_module(I);n=0
boxes=[(-7,-2),(-3,0),(-2,5),(0,4),(2,9),(I.Q+1,2*I.Q+3)]
for a in boxes:
 for b in boxes:
  raw=[x*y for x in a for y in b];lo=min(raw)//I.Q;hi=-((-max(raw))//I.Q);assert I.times(a,b)==(lo,hi);n+=1
for x in [-7,-1,0,1,7]:
 for d in [2,3,7]:assert I.ceildiv(x,d)==-((-x)//d);n+=1
try:I.compare({'x':True},{'x':1},'typed')
except ValueError:n+=1
else:raise AssertionError('bool masquerade')
print(json.dumps({'checks':n,'native_calls':0,'new_jet_calls':0}))
