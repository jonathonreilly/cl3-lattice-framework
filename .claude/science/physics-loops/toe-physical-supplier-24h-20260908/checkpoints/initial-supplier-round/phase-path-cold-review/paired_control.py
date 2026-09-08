# Separate prescribed-control check; does not pretend original QR invoked residual pairs.
import numpy as np,itertools,json
masks=[a for a in range(512) if a.bit_count()%2==0]
n=[np.array([(a>>j)&1 for a in masks]) for j in range(4)]
rows=[]
for a,b in itertools.combinations(range(4),2):
 diagonal=np.ones(256)
 for j in range(a,b):diagonal*=1-2*(n[j]-n[j+1])**2
 expected=(1-2*n[a])*(1-2*n[b]);assert np.array_equal(diagonal,expected)
 wrong=np.ones(256);assert not np.array_equal(wrong,expected)
 rows.append({'pair':[a,b],'correct_identity':True,'identity_gate_mutation_rejected':True})
print(json.dumps({'status':'PASS','all6_prescribed_pairs':rows,'scope':'Independent occupation-representation phase identity; original QR sign branch is empty'},indent=2))
