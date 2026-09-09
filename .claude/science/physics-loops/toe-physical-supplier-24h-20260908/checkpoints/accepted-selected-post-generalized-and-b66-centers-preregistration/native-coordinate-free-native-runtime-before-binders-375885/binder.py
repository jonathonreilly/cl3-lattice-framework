"""Source-only interface. No accepted scientific file is read at import."""
from fractions import Fraction as F
import adapter

def selected_record(record,expected_orbit):
 """Validate a future extracted record; this does not authenticate its provenance."""
 if type(record.get('orbit'))is not int or record['orbit']!=expected_orbit:raise ValueError('orbit')
 indices=record['indices'];adapter.seeds(indices)
 if record.get('pairs')!=24 or type(record['pairs'])is not int:raise ValueError('fixed24')
 if record.get('candidate_bits')!=256 or type(record['candidate_bits'])is not int:raise ValueError('exact candidate scale')
 T=record['T']
 if len(T)!=48 or any(len(r)!=48 for r in T):raise ValueError('T48')
 if any(type(x)is not int or abs(x).bit_length()>4096 for r in T for x in r):raise ValueError('T endpoint cap')
 if any(T[i][j] for i in range(48)for j in range(i)):raise ValueError('ordered upper T')
 if any(T[i][i]<=0 for i in range(48)):raise ValueError('positive T diagonal')
 # C-width false is explicitly not a rejection. Provenance and T exactness are required.
 return indices,[[(x,x)for x in row]for row in T]

def load(plan):
 # Intentionally unconditional: accepting future metadata requires a reviewed
 # successor source which pins the actual selected producer schema/acceptance.
 raise ValueError('NOTREADY: selected root acceptance and no-history DATA-only loader not implemented')
