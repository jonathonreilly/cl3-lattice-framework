"""Unexecuted full-size synthetic cost body; no native A or B input."""
from pathlib import Path
from fractions import Fraction as F
import json,time,hashlib
from assemble import assemble_class
P=Path(__file__).resolve().parent

def run(out):
 plan=json.loads((P/'FIXTURE.json').read_text());geometry=json.loads(Path(plan['geometry_path']).read_text())['rows'];rows=[]
 for row in geometry:
  s=F(row['s_midpoint']);wl,wu=map(F,row['weight']);w=(wl+wu)/2;A=1/(9+s*s);Ap=-2*s/(9+s*s)**2
  rows.append({'s':str(s),'weight':str(w),'A':str(A),'Aprime':str(Ap),'B':str(3*A),'Bprime':str(3*Ap)})
 if len(rows)!=66:raise ValueError('fixed66')
 # Synthetic pi22/7 is fixed exactly; this is a cost fixture, not native data.
 start=time.monotonic();results=[];stage='initial'
 try:
  for kind in ('P','O'):
   stage=kind;(out/'PARTIAL.json').write_text(json.dumps({'stage':stage,'completed_classes':results,'synthetic_only':True})+'\n')
   result=assemble_class(rows,F(22,7),kind,out/kind)
   if result['raw_dimension']!=264 or result['implicit_closed_dimension']!=528 or result['triangle_entries']!=34980:raise ValueError('full synthetic shape')
   results.append({'class':kind,'result_sha256':hashlib.sha256((out/kind/'RESULT.json').read_bytes()).hexdigest(),'seconds':result['seconds'],'triangle_sha256':result['triangle_sha256']})
   (out/'PARTIAL.json').write_text(json.dumps({'stage':kind+'_complete','completed_classes':results,'synthetic_only':True})+'\n')
  (out/'RESULT.json').write_text(json.dumps({'status':'COMPLETE_FIXED_SYNTHETIC_COST','classes':results,'seconds':time.monotonic()-start,'synthetic_only':True,'physical_scalar_calls':0,'native_gram_computed':False,'physical_error_ledger_certified':False,'pairings_or_states_computed':False},indent=2)+'\n')
 except BaseException as e:
  (out/'FAILURE.json').write_text(json.dumps({'stage':stage,'completed_classes':results,'error':repr(e),'seconds':time.monotonic()-start,'synthetic_only':True},indent=2)+'\n');raise
