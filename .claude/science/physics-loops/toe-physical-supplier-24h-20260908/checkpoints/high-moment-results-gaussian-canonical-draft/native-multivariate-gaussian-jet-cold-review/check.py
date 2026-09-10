# Independent formal trace collapse only; no table, jet, or native callback.
import sys,json
from fractions import Fraction
from pathlib import Path
sys.path.insert(0,str(Path('/private/tmp/toe-24h-probes-20260908/native-multivariate-gaussian-jet-design')))
import core
n=0;summary={}
for kind in ('pair','reflected'):
 W=core.words(kind);count=0
 for alpha,row in W.items():
  collapsed={}
  for word,q in row.items():
   defects=[z for z in word if z]
   if len(defects)==1:
    key=(defects[0],len(word)-1);collapsed[key]=collapsed.get(key,Fraction())+q
  if sum(alpha)>=2:assert all(v==0 for v in collapsed.values()),(kind,alpha,collapsed);n+=1
  count+=len(row)
 assert count==({'pair':566,'reflected':2219}[kind]);n+=1
 summary[kind]=count
# Same rectangle downward closure ensures omitted indices cannot contribute.
for kind,mask in core.MASKS.items():
 for alpha in core.indices(mask):
  for beta in core.indices(mask):
   gamma=core.minus(alpha,beta)
   if all(x>=0 for x in gamma):assert core.inside(gamma,mask)
 n+=1
print(json.dumps({'status':'PASS','independent_formal_checks':n,'word_counts':summary,'native_calls':0,'table_calls':0,'jet_calls':0}))
