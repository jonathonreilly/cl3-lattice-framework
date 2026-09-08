import pathlib,json,hashlib,struct,math
from factory import reconstruct,valid_parameters

def sha(p):return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
def save(obj,folder):
 folder=pathlib.Path(folder);folder.mkdir(exist_ok=False)
 width=(obj.g.E+7)//8
 with (folder/'states.bin').open('wb') as f:
  for x in obj.states:f.write(x.to_bytes(width,'little'))
 for name,values in [('nf.bin',obj.nf),('witness.bin',obj.witness)]:
  with (folder/name).open('wb') as f:
   for k in values:f.write(struct.pack('<H',k))
 meta=dict(L=obj.g.L,n=len(obj.states)-1,V=float(obj.V),width=width,total_nf=sum(obj.nf),witness_count=len(obj.witness),files={n:sha(folder/n) for n in ('states.bin','nf.bin','witness.bin')})
 (folder/'meta.json').write_text(json.dumps(meta,sort_keys=True,indent=2));return meta

def load(g,folder,expected):
 folder=pathlib.Path(folder);m=json.loads((folder/'meta.json').read_text())
 valid_parameters(m['L'],m['n'],m['V'],0)
 if (m['L'],m['n'],m['V'])!=expected or m['L']!=g.L:raise ValueError('expected metadata')
 if type(m['width']) is not int or m['width']!=(g.E+7)//8 or type(m['witness_count']) is not int or m['witness_count']<0:raise ValueError('layout')
 names=('states.bin','nf.bin','witness.bin')
 if set(m['files'])!=set(names):raise ValueError('file menu')
 for name in names:
  if sha(folder/name)!=m['files'][name]:raise ValueError('hash '+name)
 raw=(folder/'states.bin').read_bytes();counts=(folder/'nf.bin').read_bytes();wit=(folder/'witness.bin').read_bytes()
 if len(raw)!=(m['n']+1)*m['width'] or len(counts)!=2*(m['n']+1) or len(wit)!=2*m['witness_count']:raise ValueError('binary length')
 states=[int.from_bytes(raw[i:i+m['width']],'little') for i in range(0,len(raw),m['width'])]
 counts=[z[0] for z in struct.iter_unpack('<H',counts)];witness=[z[0] for z in struct.iter_unpack('<H',wit)]
 return reconstruct(g,states,counts,m['V'],witness,m['total_nf'])
