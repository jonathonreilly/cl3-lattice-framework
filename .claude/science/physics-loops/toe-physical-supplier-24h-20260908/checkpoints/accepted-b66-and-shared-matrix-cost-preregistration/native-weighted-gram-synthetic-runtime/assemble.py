"""Unlaunched scalar-balanced native Gram assembly. No import-time work."""
from fractions import Fraction as F
from pathlib import Path
import json,time,hashlib
import interval as iv
from core import coefficients,woodbury,entry

def write(p,x):p.write_text(json.dumps(x,indent=2)+'\n')
def assemble_class(rows,pi,kind,out):
 out.mkdir();start=time.monotonic();cache={};labels=[];roots=[];coeff=[];stage='initial';trace=iv.ZERO;maxwidth=0;coefficient_width=0;residual_abs=0;completed=0
 def partial():write(out/'PARTIAL.json',{'stage':stage,'completed_triangle_rows':completed,'completed_coefficients':len(coeff),'raw_dimension':len(labels),'max_entry_width_scaled':str(maxwidth),'trace_closed':iv.bounds(iv.scale(trace,2)),'seconds':time.monotonic()-start})
 partial()
 try:
  for n,row in enumerate(rows):
   stage='coefficient_'+str(n);partial()
   s=F(row['s']);w=F(row['weight']);values=[F(row[k]) for k in ('A','Aprime','B','Bprime')]
   if s<=0 or w<=0:raise ValueError('positive pole/weight')
   alpha=iv.div(iv.rational(35*w),iv.rational(2*pi));root=iv.sqrt(alpha);roots.append(root)
   for sig in(1,-1):
    cache[n,sig]=coefficients(s,sig,values,kind)
    for a in range(2):labels.append((n,s,sig,a))
   signed,det,res=woodbury(s,values,kind)
   coefficient_width=max(coefficient_width,max(iv.width(x) for r in signed for x in r));residual_abs=max(residual_abs,max(max(abs(x[0]),abs(x[1])) for r in res for x in r))
   coeff.append({'id':n,'alpha':iv.bounds(alpha),'sqrt_alpha':iv.bounds(root),'T_over_35_equals_i_times':[[iv.bounds(x) for x in r] for r in signed],'determinant':iv.bounds(det),'inverse_residual_qt_plus_I':[[iv.bounds(x) for x in r] for r in res]})
   write(out/'COEFFICIENTS.json',{'class':kind,'nodes':coeff,'scaled_denominator':str(iv.S),'physical_input_errors_included':False});partial()
  write(out/'COEFFICIENTS.json',{'class':kind,'nodes':coeff,'scaled_denominator':str(iv.S),'physical_input_errors_included':False})
  stage='coefficient_gate';partial()
  if coefficient_width>iv.S//(1<<40) or 2*residual_abs>iv.S//(1<<40):raise ValueError('coefficient arithmetic gate')
  digest=hashlib.sha256();path=out/'UPPER_TRIANGLE.ndjson'
  with path.open('xb') as f:
   for i in range(len(labels)):
    stage='triangle_'+str(i);line=[]
    for j in range(i,len(labels)):
     g,z=entry(i,j,labels,cache);balance=iv.mul(roots[labels[i][0]],roots[labels[j][0]]);g=iv.mul(g,balance);z=iv.mul(z,balance)
     maxwidth=max(maxwidth,iv.width(g),iv.width(z))
     if i==j:trace=iv.add(trace,g)
     line.append([j,str(g[0]),str(g[1]),str(z[0]),str(z[1])])
    b=(json.dumps({'i':i,'entries':line},separators=(',',':'))+'\n').encode();f.write(b);f.flush();digest.update(b);completed=i+1;partial()
  closed=2*len(labels);stage='final_gate';partial()
  result={'status':'CANDIDATE_MIDPOINT_ARITHMETIC','class':kind,'raw_dimension':len(labels),'implicit_closed_dimension':closed,'nodes':len(rows),'triangle_rows':completed,'triangle_entries':len(labels)*(len(labels)+1)//2,'triangle_sha256':digest.hexdigest(),'triangle_bytes':path.stat().st_size,'denominator':str(iv.S),'trace_closed':iv.bounds(iv.scale(trace,2)),'max_entry_width_scaled':str(maxwidth),'Gram_operator_rounding_radius':str(F(closed*maxwidth,2*iv.S)),'coefficient_operator_rounding_radius':str(F(coefficient_width,iv.S)),'coefficient_inverse_residual_operator_bound':str(F(2*residual_abs,iv.S)),'physical_input_error_charged_separately':True,'purification_performed':False,'seconds':time.monotonic()-start}
  write(out/'RESULT.json',result)
  if F(closed*maxwidth,2*iv.S)>F(1,2**60):raise ValueError('Gram rounding gate')
  if iv.scale(trace,2)[1]>=318*iv.S:raise ValueError('trace bound gate')
  result['status']='CERTIFIED_MIDPOINT_ARITHMETIC_ONLY';write(out/'RESULT.json',result);return result
 except BaseException as e:
  write(out/'FAILURE.json',{'stage':stage,'completed_triangle_rows':completed,'error':repr(e),'seconds':time.monotonic()-start});raise

def run_bound_inputs(*args,**kwargs):
 raise RuntimeError('UNLAUNCHED: accepted B66 binder, source/runtime/cost contract and root preregistration are absent')
