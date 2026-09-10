"""Inert signed radial formula adapters. R supplies certified absolute moments."""
import arithmetic as a

def radial_tables(R,opposite_A,opposite_C,shared,opposite_cross,max_degree=5):
 if any(type(x)is not int for x in (opposite_A,opposite_C,shared,opposite_cross,max_degree)):raise a.Refused('literal table metadata')
 if opposite_A not in (0,2)or opposite_C not in (0,2)or not 0<=shared<=2 or not 0<=opposite_cross<=2 or not 0<=max_degree<=8:raise a.Refused('table metadata range')
 def Q(n,i,j):
  if i==j==0:return R(n)
  if i==0 or j==0:return a.ZERO
  same=2 if i==j else shared;opp=(opposite_A if i==1 else opposite_C)if i==j else opposite_cross
  # Signed opposite source: R(n+2)/6 - R(n), never its unsigned negative.
  z=a.mul(a.point(same-opp),R(n))
  return a.add(z,a.mul(a.point(opp,6),R(n+2)))if opp else z
 def O(n,i,j):
  if (i==0)==(j==0):return a.ZERO
  return a.mul(a.imaginary(-1 if i==0 else 1,3),R(n+1))
 def D(n,i,j):
  if type(n)is not int or not 0<=n<=max_degree:raise a.Refused('ordinary degree')
  return Q(n,i,j)if n%2==0 else O(n,i,j)
 def B(n,i,j):
  if type(n)is not int or not 0<=n<=max_degree:raise a.Refused('projected degree')
  return a.divide(a.add(Q(n,i,j),a.neg(O(n,i,j)))if n%2==0 else a.add(O(n,i,j),a.neg(Q(n,i,j))),2)
 return D,B
