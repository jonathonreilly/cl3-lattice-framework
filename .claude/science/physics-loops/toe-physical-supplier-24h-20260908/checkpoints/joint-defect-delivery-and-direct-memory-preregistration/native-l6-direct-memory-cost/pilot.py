"""Fixed memory and pass cost; no solver, SVD or resolvent."""
import json,time,hashlib,resource
from pathlib import Path

def run(np,out,plane,kernel,norms,formats,fp,validate,root):
 out=Path(out)
 if out.exists():raise ValueError('fresh pilot output')
 out.mkdir();start=time.monotonic();record={'stage':'start','planes':[]}
 def save():
  record['seconds']=time.monotonic()-start;record['rss_bytes']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
  (out/'PARTIAL.json').write_text(json.dumps(record,indent=2)+'\n')
 def guard():
  save()
  if record['rss_bytes']>384*1048576:raise MemoryError('384MiB supplementary guard')
 try:
  save();fp.check();c=json.loads((root/'COEFFICIENTS.json').read_text());adapt=(root/'ADAPTED.json').read_bytes();validate(c,json.loads(adapt),hashlib.sha256(adapt).hexdigest())
  center=[(r['mode'],float.fromhex(r['candidate_hex'])) for r in c['center']];neighbors={int(v):[(r['mode'],float.fromhex(r['candidate_hex'])) for r in rows] for v,rows in c['neighbors'].items()};freq=[float.fromhex(r['candidate_hex']) for r in c['frequencies']]
  record['stage']='committed banks';save();t=time.monotonic();banks=[np.full(1<<20,(j+1)/16,dtype=np.float64) for j in range(9)];x=np.empty(1<<20,dtype=np.float64);record['bank_allocation_seconds']=time.monotonic()-t;guard()
  def restore():
   for lo in range(0,len(x),4096):
    ids=np.arange(lo,min(lo+4096,len(x)),dtype=np.int64);x[lo:lo+len(ids)]=(ids%17-8)/16
  for p,q in [(0,1),(0,20),(18,19)]:
   for kind in ['AA','BB']:
    for sector in [0,1]:
     record['stage']='restore';record['current']={'p':p,'q':q,'kind':kind,'sector':sector};save();t=time.monotonic();restore();rest=time.monotonic()-t
     record['stage']='plane';save();t=time.monotonic();plane.apply(x,21,sector,p,q,0.37,kind,chunk=4096);elapsed=time.monotonic()-t
     record['planes'].append(dict(record['current'],restore_seconds=rest,plane_seconds=elapsed));guard()
  # Restore fixed input once more; action is on declared P even sector.
  record['stage']='action input restore';save();t=time.monotonic();restore();record['action_restore_seconds']=time.monotonic()-t
  record['stage']='original P even action';save();t=time.monotonic();y=kernel.action(x,0,center,neighbors,[(36,-2),(6,-2)],freq);record['action_seconds']=time.monotonic()-t;guard()
  record['stage']='exact real norm';save();t=time.monotonic();norm,buckets=norms.scan(np,y,0);record['norm_seconds']=time.monotonic()-t;record['norm_upper']=str(norm);record['particle_numerators']=list(map(str,buckets));record['squared_norm_numerator']=str(sum(buckets));record['denominator_exponent']=2148;guard()
  record['stage']='save and bridge';save();t=time.monotonic();source=out/'action.npy';np.save(source,y,allow_pickle=False);record['npy_sha256']=hashlib.sha256(source.read_bytes()).hexdigest();record['raw']=formats.export(np,source,out/'action.bin');formats.verify(np,source,out/'action.bin');record['save_bridge_seconds']=time.monotonic()-t;guard()
  # Keep every bank live through all phases; np.full committed nonzero pages.
  record['bank_endpoints']=[[float(a[0]),float(a[-1])] for a in banks]
  if len(banks)!=9 or any(pair!=[(j+1)/16]*2 for j,pair in enumerate(record['bank_endpoints'])):raise ValueError('bank retention')
  fp.check();record.update(status='COMPLETE',stage='complete',scope='memory/pass cost only; no solver/resolvent/SVD');guard();(out/'RESULT.json').write_text(json.dumps(record,indent=2)+'\n')
 except BaseException as e:
  record.update(status='FAILED',error=repr(e));save();(out/'FAILURE.json').write_text(json.dumps(record,indent=2)+'\n');raise
