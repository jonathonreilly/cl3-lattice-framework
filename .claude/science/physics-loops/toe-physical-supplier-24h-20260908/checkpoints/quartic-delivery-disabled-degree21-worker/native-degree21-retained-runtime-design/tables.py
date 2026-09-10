"""Literal shifted tables; R is an inert certified radial-moment callback."""
import radial,arithmetic as a
from assembly import SIGNATURES

def wrap(base,mapping,shifts,limit):
 def get(n,i,j):
  if any(type(x)is not int for x in(n,i,j))or not 0<=n<=limit or not 0<=i<len(mapping)or not 0<=j<len(mapping):raise a.Refused('literal shifted table indices')
  return base(n+shifts[i]+shifts[j],mapping[i],mapping[j])
 return get

def nominal(R,left_C,right_A,opposite):
 if (left_C,right_A,opposite)not in {(x,y,z)for x,y,z,_ in SIGNATURES}:raise a.Refused('disjoint signature')
 D,B=radial.radial_tables(R,2 if right_A=='O'else 0,2 if left_C=='O'else 0,0,opposite,6)
 return tuple(wrap(M,(0,1,2,0),(0,0,0,1),4)for M in(D,B))
def inner(R,kind):
 if kind not in('P','O'):raise a.Refused('inner class')
 o=2 if kind=='O'else 0;D,B=radial.radial_tables(R,o,o,2,o,8)
 return tuple(wrap(M,(0,1,1),(0,0,1),6)for M in(D,B))
