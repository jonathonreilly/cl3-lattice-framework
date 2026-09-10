import sys,json
sys.dont_write_bytecode=True
from fractions import Fraction as F
sys.path.insert(0,'/private/tmp/toe-24h-probes-20260908/native-gaussian-jet-native-runtime-proposal')
import core as C,adapter
n=0;M={str(j):[[C.S*(j+1)]*2,[0,0]]for j in range(11)}
for kind in ['P','O']:
 D,B=adapter.tables(M,kind)
 for j in range(9):
  # Independent negative-band identities for a point radial table, outward grid.
  t=F(2*(j+1))if kind=='P'else F(j+3,3)
  expected=F(j+1,2)if j%2==0 else-F(j+1,2)
  z=B[str(j)][0][0][0];assert F(z[0],C.S)<=expected<=F(z[1],C.S);n+=1
  expected=t/2 if j%2==0 else-t/2;z=B[str(j)][1][1][0];assert F(z[0],C.S)<=expected<=F(z[1],C.S);n+=1
  expected=F(j+2,6)*(1 if j%2==0 else-1);z=B[str(j)][0][1][1];assert F(z[0],C.S)<=expected<=F(z[1],C.S);n+=1
print(json.dumps({'status':'PASS','independent_table_predicates':n,'native_values':0,'full_jet_calls':0}))
