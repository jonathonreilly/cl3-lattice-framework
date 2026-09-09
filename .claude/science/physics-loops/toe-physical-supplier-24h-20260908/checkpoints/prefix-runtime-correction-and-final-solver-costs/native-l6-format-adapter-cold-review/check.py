from pathlib import Path
import runpy,tempfile,struct,json
import numpy as np
b=Path('/private/tmp/toe-24h-probes-20260908');a=runpy.run_path(str(b/'native-l6-four-solve-implementation/formats.py'));native=runpy.run_path(str(b/'native-l6-exact-norm-scanner/scanner.py'));ind=runpy.run_path(str(b/'native-independent-dyadic-norm-replay/replay.py'));checks=0
bits=[0,1,0x8000000000000000,0x000fffffffffffff,0x0010000000000000,0x7fefffffffffffff,0xbff8000000000000,0x3ff0000000000001]*2
with tempfile.TemporaryDirectory() as d:
 p=Path(d);source=p/'x.npy';np.save(source,np.array(bits,dtype=np.uint64).view(np.float64),allow_pickle=False)
 for phase in ('real','i'):
  raw=p/(phase+'.bin');receipt=a['export'](np,source,raw,phase,16);a['verify'](np,source,raw,phase,16);data=raw.read_bytes();expected=b''.join(struct.pack('<QQ',v,0) if phase=='real' else struct.pack('<QQ',0,v) for v in bits)
  if data!=expected:raise ValueError('literal endian/phase bytes')
  checks+=1
  for parity in (0,1):
   x=native['scan'](raw,5,parity);y=ind['scan'](raw,5,parity)
   if any(x[k]!=y[k] for k in x):raise ValueError('all buckets')
   checks+=1
  # Corrupt inactive zero channel, retaining length and selected data.
  altered=bytearray(data);position=8 if phase=='real' else 0;altered[position]=1;raw.write_bytes(altered)
  try:a['verify'](np,source,raw,phase,16)
  except ValueError:checks+=1
  else:raise ValueError('inactive channel mutant')
print(json.dumps({'status':'PASS','predicates':checks,'maximum_entries':16,'both_parities':True,'full_scans':0,'independent_helper_authorship_disclosed':True}))
