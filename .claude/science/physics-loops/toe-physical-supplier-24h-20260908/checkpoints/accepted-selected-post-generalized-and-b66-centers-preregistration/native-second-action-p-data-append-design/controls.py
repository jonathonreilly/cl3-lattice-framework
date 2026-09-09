"""Tiny independent local identities; no stream/full family calls."""
from fractions import Fraction as F
import core as c
n=0
def check(x):
 global n
 if not x:raise ValueError('check '+str(n))
 n+=1
def contains(box,x):return F(box[0],c.S)<=x<=F(box[1],c.S)
for orbit in c.ORBITS:
 old,new=c.geometry(orbit)
 for u in range(3):
  for v in range(3):
   g,j=c.ward(u,v,orbit);f=new[(2,0,1)[v]];check(contains(g,-sum(a*b for a,b in zip(new[u],f))/F(4)));check(j==(0,0))
   g,j=c.qpair(u,v,F(5,2),F(15),orbit);I,O,T,N=c.form(new[u],new[v]);check(contains(j,-F(5,2)*N/4+F(15)*O/24));check(g==(0,0))
   a,b=c.selfpair(u,v,orbit);check(contains(a,F(6*I-O,4)));check(b==(0,0))
 check(contains(c.qpair(2,2,F(5,2),F(15),orbit)[1],-F(15,4)))
 for sig in(-1,1):
  for u in range(3):
   for v in range(3):
    qg,qj=F(1,7),F(-2,9);s=F(3,2);b=F(2,3);mu=F(5,2);I,O,T,N=c.form(new[u],old[v]);g,j=c.pole(u,v,s,sig,c.rational(b),mu,(c.rational(qg),c.rational(qj)),orbit)
    check(contains(g,-sig*s*qg+b*I/2));check(contains(j,-sig*s*qj-b*mu*T/12))
# Decisive literal alternatives: qD sign, Ward free permutation, plus sigma.
check(not contains(c.qpair(2,2,F(5,2),F(15),c.ORBITS[0])[1],F(15,4)))
check(c.ward(2,0,c.ORBITS[0])[0]!=c.ward(2,1,c.ORBITS[0])[0])
g,j=c.pole(0,0,F(2),1,c.rational(1),F(5,2),(c.rational(1),c.rational(0)),c.ORBITS[0]);check(not contains(g,F(2)))
check(5*(3*402+6)==6060);check(5*(3*(132+2)+3)==2025)
print(__import__('json').dumps({'status':'PASS_TINY_LOCAL_P_IDENTITIES','checks':n,'stream_calls':0,'saved_data_reads':0}))
