"""Strict decoder for the six frozen candidate NPZ files; standard library only."""
import ast,hashlib,json,math,re,struct,zipfile
from pathlib import Path
NAMES={'vectors','k','boundary_used_hex','bridge_count','toggle_hex','word_count'}
def npy(data,name):
 if len(data)<10 or data[:6]!=b'\x93NUMPY':raise ValueError('NPY magic')
 version=tuple(data[6:8])
 if version==(1,0):size=2;fmt='<H';encoding='latin1'
 elif version in ((2,0),(3,0)):size=4;fmt='<I';encoding='utf8' if version==(3,0) else 'latin1'
 else:raise ValueError('NPY version')
 if len(data)<8+size:raise ValueError('truncated header')
 hlen=struct.unpack(fmt,data[8:8+size])[0]
 if not 0<hlen<=65536 or 8+size+hlen>len(data):raise ValueError('header length')
 raw=data[8+size:8+size+hlen]
 if not raw.endswith(b'\n'):raise ValueError('header terminator')
 tree=ast.parse(raw.decode(encoding).strip(),mode='eval')
 if not isinstance(tree.body,ast.Dict) or len(tree.body.keys)!=3:raise ValueError('header keys')
 keys=[ast.literal_eval(k) for k in tree.body.keys]
 if len(set(keys))!=3 or set(keys)!={'descr','fortran_order','shape'}:raise ValueError('header keys')
 h=ast.literal_eval(tree)
 if h['fortran_order'] is not False:raise ValueError('Fortran order')
 shape=h['shape'];desc=h['descr']
 if type(shape) is not tuple or any(type(x) is not int or x<=0 for x in shape):raise ValueError('shape')
 if name=='vectors':
  if len(shape)!=2 or shape[1]!=512 or shape[0]>2048 or desc!='<f8':raise ValueError('vector type/shape')
  width=8;fmt='<d'
 else:
  if len(shape)!=1 or shape[0]>2048:raise ValueError('metadata shape')
  if name in ('k','bridge_count'):
   if desc!='|u1':raise ValueError('uint8 dtype')
   width=1;fmt='<B'
  elif name=='word_count':
   if desc!='<u8':raise ValueError('uint64 dtype')
   width=8;fmt='<Q'
  else:
   if type(desc) is not str or not re.fullmatch(r'<U[1-9][0-9]*',desc):raise ValueError('unicode dtype')
   width=4*int(desc[2:]);fmt=None
   if width>1024:raise ValueError('unicode width')
 count=math.prod(shape);payload=data[8+size+hlen:]
 if len(payload)!=count*width:raise ValueError('payload length')
 if fmt:
  values=[v[0] for v in struct.iter_unpack(fmt,payload)]
  if name=='vectors' and not all(math.isfinite(v) for v in values):raise ValueError('nonfinite candidate')
 else:
  values=[]
  for off in range(0,len(payload),width):
   s=payload[off:off+width].decode('utf-32-le').rstrip('\0')
   if not re.fullmatch(r'0x(?:0|[1-9a-f][0-9a-f]*)',s):raise ValueError('canonical hex')
   values.append(s)
 return shape,values

def arrays(file):
 with zipfile.ZipFile(file) as z:
  infos=z.infolist()
  if len(infos)!=6 or {i.filename for i in infos}!={n+'.npy' for n in NAMES}:raise ValueError('ZIP membership/duplicates')
  out={}
  for i in infos:
   if i.flag_bits&1 or i.file_size>12*1024*1024 or i.compress_type not in (zipfile.ZIP_STORED,zipfile.ZIP_DEFLATED):raise ValueError('ZIP domain')
   name=i.filename[:-4];out[name]=npy(z.read(i),name)
 count=out['vectors'][0][0]
 if any(shape!=(count,) for n,(shape,v) in out.items() if n!='vectors'):raise ValueError('metadata row count')
 return out

def load(file,prefix):
 file=Path(file);z=json.loads(file.read_text());a=z['vector_artifact'];vf=file.parent/a['filename']
 if Path(a['filename']).name!=a['filename'] or hashlib.sha256(vf.read_bytes()).hexdigest()!=a['sha256'] or vf.stat().st_size!=a['bytes']:raise ValueError('artifact binding')
 data=arrays(vf);count=data['vectors'][0][0]
 if a['shape']!=[count,512] or a['dtype']!='float64':raise ValueError('artifact shape')
 val={n:v for n,(s,v) in data.items()};rows={}
 for i in range(count):
  key=(int(val['boundary_used_hex'][i],16),val['bridge_count'][i]);row=(val['k'][i],int(val['toggle_hex'][i],16),val['word_count'][i],val['vectors'][512*i:512*(i+1)])
  if key in rows:raise ValueError('duplicate key')
  rows[key]=row
 r=next(r for r in prefix['rows'] if r['bridge_edge']==z['bridge']);expected={(int(x['boundary_used_mask']),x['bridge_count']):x for x in r['prefixes']}
 if set(rows)!={(0,0),*expected}:raise ValueError('prefix coverage')
 if rows[(0,0)][:3]!=(0,0,1) or rows[(0,0)][3]!=[1.]+[0.]*511:raise ValueError('vacuum')
 for key,x in expected.items():
  if rows[key][:2]!=(x['k'],int(x['full_toggle_mask'])):raise ValueError('prefix identity')
 return z,r,rows
