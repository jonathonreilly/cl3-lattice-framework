from itertools import product
from pathlib import Path
import json
# Physical computational bits x_j satisfy Z_j=(-1)^x_j.
rows=[]
for data in product((0,1),repeat=8):
 occ=list(data)+[0,1,sum(data)%2,1]
 assert sum(occ)%2==0
 x=[];p=0
 for n in occ[:-1]:p^=n;x.append(p)
 before=x[:];low=[];prev=0
 for k in range(4):low.append(x[k]^prev);prev=x[k]
 assert low==list(data[:4])
 lowflux=(low[0]+low[1]-low[2]-low[3])%4
 q=x[3]^(lowflux//2)
 # Actual native T8=Y8*(I-Z7 Z9)/2; guard must be on.
 guard=(1-(-1)**(x[7]+x[9]))//2
 assert guard==1
 phase=1
 if q:
  # exp(-i*pi*Y/2)|0>=|1>, |1>=-|0>.
  phase=(-1)**x[8];x[8]^=1
 assert x[:4]==before[:4]
 recovered=[x[0]]+[x[j]^x[j-1] for j in range(1,11)]+[x[10]]
 assert recovered[:8]==list(data)
 assert recovered[8:]==[q,1-q,sum(data)%2,1]
 labels=[data[i]+2*data[i+4] for i in range(4)];flux=(labels[0]+labels[1]-labels[2]-labels[3])%4
 assert x[3]==flux%2 and x[8]==flux//2
 rows.append(dict(data=data,physical_before=before,physical_after=x,low_records=before[:4],controller_q=q,lsb_record=x[3],msb_record=x[8],pulse_phase=phase,flux=flux))
assert len({tuple(r['physical_after']) for r in rows})==256
# Direct physical Pauli action derivation on all local3bit strings.
# A8=X8 Z7, B8=Z7 Z8, B9=Z8 Z9; (i/2)A8(B8-B9).
pauli_rows=[]
for l,m,r in product((0,1),repeat=3):
 z7,z8,z9=[(-1)**v for v in (l,m,r)]
 actual=1j*z7*(z7*z8-z8*z9)/2
 expected=1j*z8*(1-z7*z9)/2
 assert actual==expected
 pauli_rows.append(dict(bits=[l,m,r],T_flip_amplitude=[actual.real,actual.imag]))
out=dict(inputs=len(rows),rows=rows,local_pauli_rows=pauli_rows,native_record_edges=[0,1,2,3,8],native_pulse_support=[7,8,9],scope='Exact ideal native Pauli/Record isometry on a supplied even-code input and controller. No energy-apparatus or two-site gate compilation claim.')
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS256physical-code inputs;8actual localPauli actions; twoactualfluxRecordsites; oldRecords/data preserved')
