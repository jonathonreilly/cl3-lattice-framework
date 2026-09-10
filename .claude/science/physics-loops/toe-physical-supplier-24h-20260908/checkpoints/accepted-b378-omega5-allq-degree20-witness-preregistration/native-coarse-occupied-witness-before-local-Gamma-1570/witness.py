"""Literal finite block algebra; adapters must supply certified real/imag intervals."""
from fractions import Fraction as F
# Stored operator blocks are -i times physical projector differences. All columns are R/i rephased real; strip the SAME global i from node and high terms. Frobenius norms are unchanged.
from interval import add,mul,neg,const

def sub(a,b):return add(a,neg(b))
def mm(a,b):
 if not a or not b or any(len(r)!=len(b) for r in a):raise ValueError('matrix shape')
 out=[]
 for row in a:
  rr=[]
  for j in range(len(b[0])):
   x=const(0)
   for k in range(len(b)):x=add(x,mul(row[k],b[k][j]))
   rr.append(x)
  out.append(rr)
 return out

def coarse_block(local,node_selected,selected_local,high_local,high_selected):
 # Y=I is intentional; its full Frobenius error .00213 is external, not silently omitted.
 projection=mm(node_selected,selected_local);hp=mm(high_selected,selected_local)
 if len(local)!=7 or any(len(r)!=7 for r in local):raise ValueError('fixed7block')
 return [[add(sub(local[i][j],projection[i][j]),sub(high_local[i][j],hp[i][j])) for j in range(7)] for i in range(7)]
def norm_lower_squared(block):
 x=F(0)
 for row in block:
  for lo,hi in row:
   if lo>hi:raise ValueError('interval order')
   v=0 if lo<=0<=hi else min(abs(lo),abs(hi));x+=v*v
 return x
