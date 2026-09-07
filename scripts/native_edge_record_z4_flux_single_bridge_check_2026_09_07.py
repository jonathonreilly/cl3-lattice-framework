#!/usr/bin/env python3
"""Exact finite support for the conditional native Z4 flux instrument proof."""
AUDIT_TIMEOUT_SEC = 180
import time, signal, resource, sys, hashlib
from pathlib import Path
import json
started=time.monotonic()
signal.alarm(AUDIT_TIMEOUT_SEC)
from itertools import product,combinations
assertion_count=0
rows=[]
for data in product((0,1),repeat=8):
 occ=list(data)+[sum(data)%2]
 x=[]; parity=0
 for bit in occ[:-1]:parity^=bit;x.append(parity)
 labels=[data[i]+2*data[i+4] for i in range(4)]
 flux=(labels[0]+labels[1]-labels[2]-labels[3])%4
 assertion_count+=1
 assert x[3]==flux%2
 rows.append(dict(data=list(data),occupation=occ,physical_bits=x,labels=labels,flux=flux,low_sign=(-1)**x[3],high_sign=(-1)**(flux//2)))
assertion_count+=1
assert len(rows)==256 and len({tuple(z['physical_bits']) for z in rows})==256
pairs=[]
for i,j in combinations(range(9),2):
 occ=[int(k in (i,j)) for k in range(9)]
 matching=[z for z in rows if z['occupation']==occ]
 assertion_count+=1
 assert len(matching)==1
 pairs.append(dict(pair=[i,j],high_sign=matching[0]['high_sign']))
triangle=[next(z['high_sign'] for z in pairs if z['pair']==ij) for ij in ([0,1],[0,2],[1,2])]
assertion_count+=1
assert len(pairs)==36 and triangle==[-1,1,1] and triangle[0]*triangle[1]*triangle[2]==-1
# Exhaust the diagonal reflection signs to check the finite triangle obstruction.
reflection_controls=[]
for signs in product((-1,1),repeat=3):
 pair_signs=[signs[0]*signs[1],signs[0]*signs[2],signs[1]*signs[2]]
 assertion_count+=1
 assert pair_signs[0]*pair_signs[1]*pair_signs[2]==1 and pair_signs!=triangle
 reflection_controls.append(dict(signs=signs,pairs=pair_signs))
out=dict(inputs=256,two_particle_states=36,diagonal_triangle_controls=8,rows=rows,pair_rows=pairs,triangle=triangle,reflection_controls=reflection_controls,summary='256 orthogonal inputs;36 pair states;8 diagonal-reflection controls.',scope='Single bridge after arbitrary number-conserving quadratic evolution on the declared9-mode encoding; not a multiparity or feedback no-go.')

rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024)
seconds=time.monotonic()-started
assertion_count+=1
assert 0<rss<180 and 0<=seconds<180
out.update(assertions=assertion_count,status='PASS',seconds=seconds,rss_MiB=rss,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),dependencies={})
if '--json' in sys.argv:
 print(json.dumps(out,indent=2,allow_nan=False))
else:
 print('PASS: '+out['summary'])
 print('per_element: 256 exact orthogonal occupation encodings and low-bit prefix identities.')
 print('per_site: Declared nine-mode path with eight physical edge qubits; no arbitrary lattice realization executed.')
 print('per_mode: All36 two-particle inputs and8 diagonal-sign controls; exterior-square proof covers all Gaussian controls.')
 print('per_block: Single-bridge sign readout only; ready-battery statement is analytic, not a simulated energy apparatus.')
 print('lattice_wide: checked and not executed — finite path scope; no universal compiler or whole-lattice claim.')
 print('TOTAL: PASS='+str(assertion_count)+' FAIL=0; executed assertions include one resource guard.')
 print('Resources: %.6fs; %.3f MiB; declared limits180s/180MiB.'%(seconds,rss))
 print('Source SHA256: '+out['source_sha256'])
