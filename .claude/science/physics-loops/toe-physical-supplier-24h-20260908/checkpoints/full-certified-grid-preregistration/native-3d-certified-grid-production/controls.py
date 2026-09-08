"""Predata exact aggregation controls; no spectra."""
from fractions import Fraction as F
from itertools import product
from collections import Counter
from pathlib import Path
import json,copy
from aggregate import comparison,node_interval
from exact_certificate import certificate
p=Path(__file__).resolve().parent;trig=json.loads((p/'TRIG_INPUTS.json').read_text());cubes=json.loads((p/'CUBE_INPUTS.json').read_text())
coverage=Counter()
for job in range(24):
 for j in product(range(4*(job%4),4*(job%4)+4),range(16),range(16)):coverage[(job//4,j)]+=1
if len(coverage)!=24576 or set(coverage.values())!={1}:raise ValueError('24job partition')
D=[[0j]*16 for _ in range(16)];Q=[[0j]*16 for _ in range(16)]
for i in range(16):D[i][i]=i;Q[i][i]=1
index=(0,0,0);g=trig['rows'][0];q=F(float.fromhex(g['q_hex']));inp=3*max(abs(q-F(g['lower_numerator'],g['denominator'])),abs(q-F(g['upper_numerator'],g['denominator'])))
c=certificate(D,Q,list(range(16)),inp);row=dict(job=0,rep=0,index=index,eigenvalues_hex=[float(i).hex() for i in range(16)],vectors_hex=[[[complex(z).real.hex(),complex(z).imag.hex()] for z in line] for line in Q],certificate=c)
node_interval(row,0,index,trig)
for kind in ('index','radius','normalization','roots'):
 z=copy.deepcopy(row)
 if kind=='index':z['index']=(1,0,0)
 if kind=='radius':z['certificate']['input_radius']='0'
 if kind=='normalization':z['certificate']['density_lower']=str(F(c['density_lower'])/2)
 if kind=='roots':z['certificate']['root_intervals'][0]=['1','1']
 try:node_interval(z,0,index,trig)
 except ValueError:pass
 else:raise ValueError('corruption accepted '+kind)
densities={r:(F(-2),F(-2)) if r==15 else (F(-1),F(-1)) for r in (0,1,3,5,10,15)}
z=comparison(densities,cubes,trig);err=3*F(trig['pi_upper_numerator'],trig['pi_denominator'])**2/(8*32**2)
for c in z['costs']:
 if F(c['density_lower'])!=1-err or F(c['limiting_delta_lower'])!=8*(1-err)/c['defects'] or F(c['native_half_objective_defect_coefficient_lower'])!=(1-err)/c['defects']:raise ValueError('exact normalization/quadrature')
print(json.dumps(dict(controls=12,unique_nodes=len(coverage),original_nodes=8*len(coverage),scope='synthetic aggregation and exact coverage; no physical eigenvalues')))
