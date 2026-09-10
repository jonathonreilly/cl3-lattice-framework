"""Pure physical table map; no suppliers are loaded here."""
import core as C
from engine import scalar,need
def tables(moment_boxes,kind):
 need(kind in ('P','O')and type(kind)is str,'literal class');need(type(moment_boxes)is dict and set(moment_boxes)==set(map(str,range(11))),'absolute M0..10')
 M={j:scalar(moment_boxes[str(j)])for j in range(11)};need(M[0]==C.point(1),'absolute M0=1');need(all(x[1]==(0,0)for x in M.values()),'real absolute moments')
 def t(j):return C.mul(C.point(2),M[j])if kind=='P'else C.divide(M[j+2],3)
 def imaginary(x):return ((0,0),x[0])
 D={};B={}
 for j in range(9):
  if j%2==0:
   D[str(j)]=[[M[j],C.ZERO],[C.ZERO,t(j)]];v=imaginary(C.divide(M[j+1],6));B[str(j)]=[[C.divide(M[j],2),v],[C.neg(v),C.divide(t(j),2)]]
  else:
   v=imaginary(C.divide(M[j+1],3));D[str(j)]=[[C.ZERO,C.neg(v)],[v,C.ZERO]];v=C.divide(v,2);B[str(j)]=[[C.neg(C.divide(M[j],2)),C.neg(v)],[v,C.neg(C.divide(t(j),2))]]
 # Convert tuple boxes to canonical JSON structural lists without changing endpoints.
 import json
 return json.loads(json.dumps(D)),json.loads(json.dumps(B))
