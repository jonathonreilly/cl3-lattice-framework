"""Portable exact rational replay; original certify arithmetic unchanged."""
import hashlib
from pathlib import Path
from itertools import combinations
from fractions import Fraction as F
from native_weak_electric_rational_core_2026_09_08 import ExactModel,candidate,incoming,residual,gap,upper_sqrt
from native_weak_electric_candidate_decoder_2026_09_08 import load
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()

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
