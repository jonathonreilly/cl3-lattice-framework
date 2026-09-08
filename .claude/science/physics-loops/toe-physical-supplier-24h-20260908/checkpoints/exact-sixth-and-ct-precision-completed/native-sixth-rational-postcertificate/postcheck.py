import json,sys,hashlib,time
from pathlib import Path
from itertools import combinations
from fractions import Fraction as F
import numpy as np
from core import ExactModel,candidate,incoming,residual,gap,upper_sqrt
P=Path('/private/tmp/toe-24h-probes-20260908/native-zero-penalty-sixth-spectator-coefficient')
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(file,prefix):
 file=Path(file);z=json.loads(file.read_text());vfile=file.parent/z['vector_artifact']['filename']
 if sha(vfile)!=z['vector_artifact']['sha256']:raise ValueError('vector hash')
 with np.load(vfile,allow_pickle=False) as n:
  if set(n.files)!={'vectors','k','boundary_used_hex','bridge_count','toggle_hex','word_count'}:raise ValueError('NPZ membership')
  if n['vectors'].dtype!=np.dtype('float64') or n['vectors'].ndim!=2 or n['vectors'].shape[1]!=512 or not np.isfinite(n['vectors']).all():raise ValueError('vector dtype/shape/finite')
  count=len(n['vectors'])
  if any(n[k].shape!=(count,) for k in n.files if k!='vectors'):raise ValueError('metadata shape')
  rows={}
  for i in range(count):
   key=(int(n['boundary_used_hex'][i],16),int(n['bridge_count'][i]));row=(int(n['k'][i]),int(n['toggle_hex'][i],16),int(n['word_count'][i]),n['vectors'][i].copy())
   if key in rows:raise ValueError('duplicate key')
   rows[key]=row
 r=next(r for r in prefix['rows'] if r['bridge_edge']==z['bridge'])
 expected={(int(x['boundary_used_mask']),x['bridge_count']):x for x in r['prefixes']}
 if set(rows)!={(0,0),*expected}:raise ValueError('prefix coverage')
 if rows[(0,0)][:3]!=(0,0,1) or list(rows[(0,0)][3])!=[1.]+[0.]*511:raise ValueError('vacuum')
 for key,x in expected.items():
  if rows[key][:2]!=(x['k'],int(x['full_toggle_mask'])):raise ValueError('prefix identity')
 return z,r,rows

def certify(file,frame,prefix):
 model=ExactModel(frame,prefix);z,row,saved=load(file,prefix);bridge=row['bridge_edge'];boundary=prefix['boundary_edges'];terms=[(a,b) for a,b in combinations(sorted(boundary+[bridge]),2) if set(model.edges[a])&set(model.edges[b])]
 target=(sum(1<<e for e in boundary),2);layer={(0,0):(([1]+[0]*511,1),F(0),1)};ledger=[];u6=F(2449489742783179,10**15)
 if u6*u6<=6:raise ValueError('sqrt upper')
 for k in range(1,7):
  inc={}
  for (used,bc),data in layer.items():
   for a,b in terms:
    bd=[e for e in (a,b) if e!=bridge]
    if any(used>>e&1 for e in bd):continue
    key=(used|sum(1<<e for e in bd),bc+int(a==bridge)+int(b==bridge))
    if key in saved:inc.setdefault(key,[]).append(data)
  nxt={}
  for key,parts in inc.items():
   degree,mask,words,vec=saved[key];count=sum(x[2] for x in parts)
   if degree!=k or words!=count:raise ValueError('word count')
   errin=sum((x[1]/2 for x in parts),F(0));prev=[x[0] for x in parts]
   if k==6:cand=incoming(prev);err=errin
   else:
    cand=candidate(vec,k,model.W);rn=residual(model,model.matrix(mask),cand,prev);delta=gap(model,mask);err=(u6/delta)*(errin+rn)
    ledger.append(dict(k=k,key=[str(key[0]),key[1]],mask=str(mask),gap=str(delta),residual_norm_upper=str(rn),error=str(err)))
   nxt[key]=(cand,err,count)
  layer=nxt
 (v,d),error,count=layer[target]
 if count!=row['unordered_pair_sets']*720:raise ValueError('final word count')
 center=sum((a*F(x,d) for a,x in zip(model.ell,v)),F(0))/216;radius=u6*error/216
 return dict(bridge=bridge,source_json_sha=sha(file),source_vector_sha=z['vector_artifact']['sha256'],center=str(center),radius=str(radius),interval=[str(center-radius),str(center+radius)],excludes_zero=center-radius>0 or center+radius<0,ledger=ledger,scope='exact rational residual certificate of arbitrary dyadic candidates; adjacent ordered bilinear only')

def main():
 if len(sys.argv)!=3:raise ValueError('one saved bridge JSON and fresh result')
 pins=json.loads((Path(__file__).parent/'INPUT_BINDINGS.json').read_text())
 for p,h in pins.items():
  if sha(p)!=h:raise ValueError('input pin '+p)
 out=Path(sys.argv[2])
 if out.exists():raise ValueError('no overwrite')
 frame=json.loads((P/'FRAME_RESULT.json').read_text());prefix=json.loads((P/'PREFIXES.json').read_text());result=certify(sys.argv[1],frame,prefix)
 out.write_text(json.dumps(result,indent=2))
if __name__=='__main__':main()
