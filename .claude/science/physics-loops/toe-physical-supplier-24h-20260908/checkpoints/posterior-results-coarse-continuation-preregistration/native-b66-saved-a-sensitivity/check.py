"""Saved accepted A66 widths only; no oracle, B contraction or physical solve."""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json
p=Path('/private/tmp/toe-24h-probes-20260908/native-stationary-pole-scalar-run-9845c/RESULT.json');raw=p.read_bytes();data=json.loads(raw)
acc=Path('/private/tmp/toe-24h-probes-20260908/native-stationary-pole-scalar-root-review/ROOT_ACCEPTANCE.json');a=json.loads(acc.read_text())
if hashlib.sha256(raw).hexdigest()!=a['result_sha256']:raise ValueError('acceptance binding')
rows=[]
for row in data['rows']:
 s=F(row['oracle']['s']);wa,wd=map(F,row['oracle']['widths'])
 ra=sum((s**(2*n+2)/((2*n+1)*8**(2*n+1)) for n in range(26)),F(0))
 dra=sum(((2*n+2)*s**(2*n+1)/((2*n+1)*8**(2*n+1)) for n in range(26)),F(0))
 g=F(2,3)*ra*wa;h=F(2,3)*(dra*wa+ra*wd)
 rows.append({'id':row['id'],'R_A_decimal':float(ra),'R_Aprime_decimal':float(dra),'B_tail_input_width_bound':str(g),'Bprime_tail_input_width_bound':str(h),'status':'PASS_1E-30' if max(g,h)<F(1,10**30) else 'INDETERMINATE'})
if len(rows)!=66:raise ValueError('census')
result={'scope':'saved A66 high-tail sensitivity only; not full B widths','accepted_result_sha256':hashlib.sha256(raw).hexdigest(),'acceptance_sha256':hashlib.sha256(acc.read_bytes()).hexdigest(),'rows':rows,'all_tail_input_widths_below_1e30':all(r['status']=='PASS_1E-30' for r in rows),'max_B_width_decimal':max(float(F(r['B_tail_input_width_bound'])) for r in rows),'max_Bprime_width_decimal':max(float(F(r['Bprime_tail_input_width_bound'])) for r in rows),'max_R_A':max(r['R_A_decimal'] for r in rows)}
print(json.dumps(result,indent=2))
