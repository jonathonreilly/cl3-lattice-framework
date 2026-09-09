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
 import json
 from pathlib import Path
 import data_binder,selected_binder,old_reader,data_adapter
 if plan.get('status')!='ROOT_REVIEWED_GENERALIZED_LEAKAGE':raise ValueError('NOTREADY')
 def read(path):
  if data_binder.sha(path)!=plan['inputs'].get(path):raise ValueError('plan pin')
  return json.loads(Path(path).read_text())
 for path,h in plan['inputs'].items():
  if data_binder.sha(path)!=h:raise ValueError('full plan closure')
 dp=read(plan['data_binding']);sp=read(plan['selected_binding'])
 for child in(dp,sp):
  for path,h in child['inputs'].items():
   if plan['inputs'].get(path)!=h:raise ValueError('child closure')
 if dp['original_family_binding']!=sp['original_family_binding']:raise ValueError('same original family')
 records=selected_binder.load(sp)
 cp,ap,np,radii,poles,alpha,emu=data_binder.load(dp)
 opened=[]
 try:
  opened.append(old_reader.Indexed(cp,plan['inputs'][cp],'cache'))
  opened.append(old_reader.Indexed(ap,plan['inputs'][ap],'append'))
  opened.append(data_adapter.NewIndex(np,plan['inputs'][np]))
  entries=[data_adapter.Entries(old_reader.Entries(*opened[:2],old_reader.ORBITS[i],**radii),opened[2],i,etaA=radii['etaA'],etaB=radii['etaB'],etac=radii['etac'],etamu=emu)for i in range(5)]
  # Exact rational family enclosed on256 grid; T remains exact dyadic point.
  return dict(records=records,entries=entries,poles=[adapter.rounded(x)for x in poles],alpha=[adapter.rounded(x)for x in alpha],descriptors=opened)
 except BaseException as original:
  errors=[]
  for d in opened:
   try:d.verify()
   except BaseException as e:errors.append('verify '+repr(e))
   try:d.close()
   except BaseException as e:errors.append('close '+repr(e))
  if errors:original.add_note(repr(errors))
  raise
