"""Unlaunched fixed vector-pass cost body; no H action or CG solve."""
def run(np,out,formats,scan,fp):
 import time,json
 from pathlib import Path
 out=Path(out)
 if out.exists():raise ValueError('fresh output')
 out.mkdir();fp.check();ids=np.arange(1<<20);x=((ids%17)-8).astype(float)/16;r=((ids%13)-6).astype(float)/32;p=((ids%11)-5).astype(float)/64;del ids;times=[]
 for i in range(16):
  t=time.monotonic();a=np.dot(r,r);b=np.dot(p,p);x=np.add(x,np.multiply(0.125,p));r=np.subtract(r,np.multiply(0.0625,p));p=np.add(r,np.multiply(0.25,p))
  if not all(np.isfinite(v).all() for v in (x,r,p)) or not np.isfinite(a+b):raise ValueError('finite')
  times.append(time.monotonic()-t);(out/'PARTIAL.json').write_text(json.dumps({'vector_pass_seconds':times}))
 source=out/'fixed.npy';np.save(source,x,allow_pickle=False);t=time.monotonic();formats.export(np,source,out/'fixed.bin');formats.verify(np,source,out/'fixed.bin');conversion=time.monotonic()-t;t=time.monotonic();norm,_=scan(np,x,0);elapsed=time.monotonic()-t;fp.check();(out/'RESULT.json').write_text(json.dumps({'vector_pass_seconds':times,'conversion_seconds':conversion,'real_norm_seconds':elapsed,'exact_norm_upper':str(norm),'scope':'vector-pass cost only; no CG/operator'}))
