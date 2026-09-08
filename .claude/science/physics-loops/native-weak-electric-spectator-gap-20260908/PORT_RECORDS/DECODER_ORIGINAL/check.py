import json,hashlib,io,zipfile,struct,warnings,time,resource,signal
from pathlib import Path
import numpy as np
import decoder
signal.alarm(180);start=time.monotonic();B=Path(__file__).parent;P=B.parent/'native-zero-penalty-sixth-spectator-coefficient';out=P/'COEFFICIENT_OUTPUT';prefix=json.loads((P/'PREFIXES.json').read_text());n=0;pins={}
def ck(x):
 global n;n+=1
 if not x:raise ValueError(n)
def reject(f):
 try:f()
 except (ValueError,UnicodeError,SyntaxError):ck(True)
 else:raise ValueError('mutant survived')
for bridge in (0,3,9,12,36,96):
 f=out/f'bridge_{bridge}.npz';pins[str(f)]=hashlib.sha256(f.read_bytes()).hexdigest();a=decoder.arrays(f);z,r,rows=decoder.load(f.with_suffix('.json'),prefix)
 with np.load(f,allow_pickle=False) as original:
  for name,(shape,values) in a.items():
   ck(tuple(original[name].shape)==shape)
   flat=original[name].ravel()
   if name=='vectors':ck(b''.join(struct.pack('<d',v) for v in values)==flat.tobytes())
   else:ck(values==flat.tolist())
  ck(len(rows)==len(original['k']))
# Actual candidate NPY mutations with altered headers/payload, bypassing hash gates.
with zipfile.ZipFile(out/'bridge_0.npz') as z:raw={i.filename:z.read(i) for i in z.infolist()}
v=raw['vectors.npy'];hlen=struct.unpack('<H',v[8:10])[0];head=v[10:10+hlen];payload=v[10+hlen:]
def replace_header(old,new):
 h=head.replace(old,new)
 return v[:8]+struct.pack('<H',len(h))+h+payload
reject(lambda:decoder.npy(replace_header(b'512',b'511'),'vectors'))
reject(lambda:decoder.npy(replace_header(b"'<f8'",b"'|O8'"),'vectors'))
reject(lambda:decoder.npy(v[:10+hlen]+struct.pack('<d',float('nan'))+payload[8:],'vectors'))
reject(lambda:decoder.npy(v[:-1],'vectors'))
mem=io.BytesIO()
with warnings.catch_warnings():
 warnings.simplefilter('ignore')
 with zipfile.ZipFile(mem,'w') as z:
  for name,data in raw.items():z.writestr(name,data)
  z.writestr('k.npy',raw['k.npy'])
mem.seek(0);reject(lambda:decoder.arrays(mem))
result=dict(checks=n,seconds=time.monotonic()-start,rss_mib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1048576,npz_sha256=pins,scope='all six array decodings bit-equal; no coefficient replay')
(B/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
