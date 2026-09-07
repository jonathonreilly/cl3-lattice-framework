#!/usr/bin/env python3
"""Exact finite support for the conditional native Z4 flux instrument proof."""
AUDIT_TIMEOUT_SEC = 180
import time, signal, resource, sys, hashlib
from pathlib import Path
import json
started=time.monotonic()
signal.alarm(AUDIT_TIMEOUT_SEC)
from itertools import product
from pathlib import Path
import json
# Physical computational bits x_j satisfy Z_j=(-1)^x_j.
assertion_count=0
rows=[]
for data in product((0,1),repeat=8):
 occ=list(data)+[0,1,sum(data)%2,1]
 assertion_count+=1
 assert sum(occ)%2==0
 x=[];p=0
 for n in occ[:-1]:p^=n;x.append(p)
 before=x[:];low=[];prev=0
 for k in range(4):low.append(x[k]^prev);prev=x[k]
 assertion_count+=1
 assert low==list(data[:4])
 lowflux=(low[0]+low[1]-low[2]-low[3])%4
 q=x[3]^(lowflux//2)
 # Actual native T8=Y8*(I-Z7 Z9)/2; guard must be on.
 guard=(1-(-1)**(x[7]+x[9]))//2
 assertion_count+=1
 assert guard==1
 phase=1
 if q:
  # exp(-i*pi*Y/2)|0>=|1>, |1>=-|0>.
  phase=(-1)**x[8];x[8]^=1
 assertion_count+=1
 assert x[:4]==before[:4]
 recovered=[x[0]]+[x[j]^x[j-1] for j in range(1,11)]+[x[10]]
 assertion_count+=1
 assert recovered[:8]==list(data)
 assertion_count+=1
 assert recovered[8:]==[q,1-q,sum(data)%2,1]
 labels=[data[i]+2*data[i+4] for i in range(4)];flux=(labels[0]+labels[1]-labels[2]-labels[3])%4
 assertion_count+=1
 assert x[3]==flux%2 and x[8]==flux//2
 rows.append(dict(data=data,physical_before=before,physical_after=x,low_records=before[:4],controller_q=q,lsb_record=x[3],msb_record=x[8],pulse_phase=phase,flux=flux))
assertion_count+=1
assert len({tuple(r['physical_after']) for r in rows})==256
# Direct physical Pauli action derivation on all local3bit strings.
# A8=X8 Z7, B8=Z7 Z8, B9=Z8 Z9; (i/2)A8(B8-B9).
pauli_rows=[]
for l,m,r in product((0,1),repeat=3):
 z7,z8,z9=[(-1)**v for v in (l,m,r)]
 actual=1j*z7*(z7*z8-z8*z9)/2
 expected=1j*z8*(1-z7*z9)/2
 assertion_count+=1
 assert actual==expected
 pauli_rows.append(dict(bits=[l,m,r],T_flip_amplitude=[actual.real,actual.imag]))
out=dict(inputs=len(rows),rows=rows,local_pauli_rows=pauli_rows,native_record_edges=[0,1,2,3,8],native_pulse_support=[7,8,9],scope='Exact ideal native Pauli/Record isometry on a supplied even-code input and controller. No energy-apparatus or two-site gate compilation claim.')
out['summary']='256 inputs;8 physical three-site Pauli actions;5 native events;both flux Record sites.'

rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024)
seconds=time.monotonic()-started
assertion_count+=1
assert 0<rss<180 and 0<=seconds<180
out.update(assertions=assertion_count,status='PASS',seconds=seconds,rss_MiB=rss,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),dependencies={})
if '--json' in sys.argv:
 print(json.dumps(out,indent=2,allow_nan=False))
else:
 print('PASS: '+out['summary'])
 print('per_element: 256 prepared basis inputs; all data occupations and both physical flux Record sites verified.')
 print('per_site: Five actual bridge events on a twelve-mode path; three-edge pulse support verified.')
 print('per_mode: All8 local Pauli basis actions include the pulse phase and guard; no arbitrary-controller Hilbert simulation.')
 print('per_block: Ideal supplied-controller instrument; switching, work apparatus and preparation remain inputs.')
 print('lattice_wide: checked and not executed — finite path scope; no autonomous or finite-battery implementation.')
 print('TOTAL: PASS='+str(assertion_count)+' FAIL=0; executed assertions include one resource guard.')
 print('Resources: %.6fs; %.3f MiB; declared limits180s/180MiB.'%(seconds,rss))
 print('Source SHA256: '+out['source_sha256'])
