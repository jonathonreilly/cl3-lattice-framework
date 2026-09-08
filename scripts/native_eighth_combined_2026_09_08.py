"""Portable exact H8 control, adapted from preserved research source."""
AUDIT_TIMEOUT_SEC=180
import argparse, signal
if __name__=='__main__':
 signal.alarm(AUDIT_TIMEOUT_SEC)
 parser=argparse.ArgumentParser();parser.add_argument('--json',action='store_true');parser.parse_args()
from pathlib import Path
from fractions import Fraction as F
from itertools import product
from math import comb
import json,hashlib
base=Path(__file__).resolve().parents[1]
source=base/'outputs/native_eighth_local_2026_09_08.json';rows=json.loads(source.read_text())['rows'];tab={(r['shape'],tuple(r['bits'])):F(r['connected8']) for r in rows}
def c(s,b):return tab[s,tuple(b)]
def choose(n,k):return comb(n,k) if 0<=k<=n else 0
def a(b,d):return 2 if b==d else 3
parts={}
parts['one']=3*c('one',(0,))
parts['pair']=F(3,2)*sum(a(*b)*c('pair',b) for b in product((0,1),repeat=2))
parts['star3']=sum(choose(3,k)*choose(3,3-k)*c('star3',(1,)*k+(0,)*(3-k)) for k in range(4))
parts['path3']=F(3,2)*sum(a(b[0],b[1])*a(b[1],b[2])*c('path3',b) for b in product((0,1),repeat=3))
parts['star4']=sum(choose(3,k)*choose(3,4-k)*c('star4',(1,)*k+(0,)*(4-k)) for k in range(5))
# Author fork edges: two ordinary leaves0,1, internal2, distant leaf3.
parts['fork4']=3*sum(choose(3-b0,k)*choose(2+b0,2-k)*a(b0,d)*c('fork4',(1,)*k+(0,)*(2-k)+(b0,d)) for b0 in (0,1) for k in range(3) for d in (0,1))
parts['path4_unrestricted']=F(3,2)*sum(a(b[0],b[1])*a(b[1],b[2])*a(b[2],b[3])*c('path4',b) for b in product((0,1),repeat=4))
w={b:c('cycle4',b)-sum(c('path4',b[r:]+b[:r]) for r in range(4)) for b in product((0,1),repeat=4)}
checks=0
def req(v,m):
 global checks
 checks+=1
 if not v:raise RuntimeError(m)
for b,v in w.items():
 for r in range(4):req(w[b[r:]+b[:r]]==v,'rotation')
 req(w[b[::-1]]==v,'reflection');req(w[tuple(1-x for x in b)]==v,'complement')
# W=A+B domainwalls+C product sigma+D alternating indicator.
bs=[(0,0,0,0),(0,0,0,1),(0,0,1,1),(0,1,0,1)]
def features(b):return [F(1),F(sum(b[i]!=b[(i+1)%4] for i in range(4))),F((-1)**sum(b)),F(all(b[i]!=b[(i+1)%4] for i in range(4)))]
mat=[features(b)+[w[b]] for b in bs]
for i in range(4):
 j=next(j for j in range(i,4) if mat[j][i]);mat[i],mat[j]=mat[j],mat[i];x=mat[i][i];mat[i]=[v/x for v in mat[i]]
 for j in range(4):
  if j!=i:
   x=mat[j][i];mat[j]=[v-x*u for v,u in zip(mat[j],mat[i])]
coef=[mat[i][4] for i in range(4)]
for b in w:req(sum(x*y for x,y in zip(features(b),coef))==w[b],'four-invariant decomposition')
out=dict(checks=checks,scalar_parts={k:str(v) for k,v in parts.items()},C_tree=str(sum(parts.values())),W={''.join(map(str,k)):str(v) for k,v in w.items()},decomposition=dict(zip(['constant','domainwalls','four_sigma_product','flippability'],map(str,coef))),input_sha256=hashlib.sha256(source.read_bytes()).hexdigest())
(Path(__file__).resolve().parents[1]/'outputs/native_eighth_combined_2026_09_08.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
