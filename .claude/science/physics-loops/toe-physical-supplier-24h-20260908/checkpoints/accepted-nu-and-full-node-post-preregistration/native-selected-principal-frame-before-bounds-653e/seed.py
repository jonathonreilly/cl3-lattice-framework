"""Canonical sparse seed map; no history reader."""
def seed(index,gamma=0):
 if type(index)is not int or not 0<=index<399 or type(gamma)is not int or gamma not in(0,1):raise ValueError('canonical seed')
 if index>=396:return {(index,gamma):1}
 n,t=divmod(index,6);v=t//2
 # Same original half convention as reviewed a29 coefficient seed.
 chi=1 if v==0 else -1;eta=(-1,1)[t%2]
 from fractions import Fraction as F
 return {(6*n+v,gamma):F(-eta*chi,2),(6*n+3+v,gamma):F(1,2)}
