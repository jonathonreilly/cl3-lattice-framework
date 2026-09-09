"""Fixed sixteen vector-update groups, one conversion, one realnorm; noCG/H."""
def run(np,out,formats,scan,fp):
 import time,json,hashlib
 from pathlib import Path
 out=Path(out)
 if out.exists():raise ValueError('fresh output')
 out.mkdir();start=time.monotonic();record={'stage':'initialization','vector_pass_seconds':[]}
 def save():
  record['seconds']=time.monotonic()-start;(out/'PARTIAL.json').write_text(json.dumps(record,indent=2)+'\n')
 try:
  save();fp.check();ids=np.arange(1<<20);x=((ids%17)-8).astype(float)/16;r=((ids%13)-6).astype(float)/32;p=((ids%11)-5).astype(float)/64;del ids
  record['stage']='sixteen_updates'
  for i in range(16):
   t=time.monotonic();a=np.dot(r,r);b=np.dot(p,p);x=np.add(x,np.multiply(0.125,p));r=np.subtract(r,np.multiply(0.0625,p));p=np.add(r,np.multiply(0.25,p))
   if not all(np.isfinite(v).all() for v in (x,r,p)) or not np.isfinite(a+b):raise ValueError('finite')
   record['vector_pass_seconds'].append(time.monotonic()-t);save()
  record['stage']='conversion';save();t=time.monotonic();source=out/'fixed.npy';np.save(source,x,allow_pickle=False);record['source_npy_sha256']=hashlib.sha256(source.read_bytes()).hexdigest();record['export']=formats.export(np,source,out/'fixed.bin');formats.verify(np,source,out/'fixed.bin');record['conversion_seconds']=time.monotonic()-t;record['stage']='realnorm';save()
  t=time.monotonic();norm,buckets=scan(np,x,0);record['real_norm_seconds']=time.monotonic()-t;record['exact_norm_upper']=str(norm);record['particle_numerators']=list(map(str,buckets));record['squared_norm_numerator']=str(sum(buckets));record['denominator_exponent']=2148;record['stage']='final_fp';save();fp.check();record.update(status='COMPLETE',stage='complete',scope='fixedvectorpasscost; noCG/operator');save();(out/'RESULT.json').write_text(json.dumps(record,indent=2)+'\n')
 except BaseException as e:
  record.update(status='FAILED',error=repr(e));save();(out/'FAILURE.json').write_text(json.dumps(record,indent=2)+'\n');raise
