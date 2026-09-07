#!/usr/bin/env python3
"""Exact SU3 Dirichlet and finite projector adverse controls, block38."""
import time,os,resource,json
START=time.monotonic()
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
import sympy as s
checks={}
def ck(name,cond):
 checks[name]=bool(cond)
 assert checks[name],name
def zero(M):return all(s.simplify(x)==0 for x in M)
def unit(i,n):return s.eye(n)[:,i]
I=s.I;r=s.sqrt
lam=[s.Matrix([[0,1,0],[1,0,0],[0,0,0]]),s.Matrix([[0,-I,0],[I,0,0],[0,0,0]]),s.diag(1,-1,0),s.Matrix([[0,0,1],[0,0,0],[1,0,0]]),s.Matrix([[0,0,-I],[0,0,0],[I,0,0]]),s.Matrix([[0,0,0],[0,0,1],[0,1,0]]),s.Matrix([[0,0,0],[0,0,-I],[0,I,0]]),s.diag(1,1,-2)/r(3)]
T=[x/r(2) for x in lam]
for a,Ta in enumerate(T):
 ck('generator_%d_hermitian_traceless'%a,Ta==Ta.H and s.trace(Ta)==0)
ck('all_64_trace_pairings',all(s.simplify(s.trace(a*b))==int(i==j) for i,a in enumerate(T) for j,b in enumerate(T)))
ck('full_fundamental_casimir',zero(sum((x*x for x in T),s.zeros(3))-s.Rational(8,3)*s.eye(3)))
A=s.Matrix([[s.Rational(3,5),s.Rational(4,5),0],[-s.Rational(4,5),s.Rational(3,5),0],[0,0,1]])
B=s.Matrix([[1,0,0],[0,s.Rational(5,13),s.Rational(12,13)],[0,-s.Rational(12,13),s.Rational(5,13)]])
C=s.diag(I,-I,1)
for name,M in [('prefix',A),('link',B),('suffix',C)]:ck(name+'_actual_SU3',M.H*M==s.eye(3) and M.det()==1)
for orient in ['forward','inverse']:
 U=A*(B if orient=='forward' else B.H)*C
 total=0
 for a,Ta in enumerate(T):
  D=A*(I*Ta*B if orient=='forward' else -I*B.H*Ta)*C
  ck(orient+'_generator_%d_cross_trace_zero'%a,s.simplify(s.trace(U.H*D))==0)
  total+=s.trace(D.H*D)/3
 ck(orient+'_normalized_derivative_casimir',s.simplify(total)==s.Rational(8,3))
 ck(orient+'_electric_increment_four',s.simplify(s.Rational(3,2)*total)==4)
identity_D=A*(I*s.eye(3)*B)*C
ck('U1_identity_generator_cross_term_adverse',s.trace((A*B*C).H*identity_D)==3*I)
# Creation on one cell with actual and ghost factors, ordered00,01,10,11.
vhat=unit(2,4)*unit(0,4).T;G=s.diag(1,0,1,0);S=s.eye(4)+s.Rational(2,7)*vhat;Sinv=s.eye(4)-s.Rational(2,7)*vhat
ck('creation_nilpotent',vhat*vhat==s.zeros(4))
ck('finite_dressing_inverse',S*Sinv==s.eye(4))
ck('ghost_vacuum_creation_commutes',vhat*G==G*vhat)
ck('ghost_vacuum_dressing_commutes',S*G==G*S and Sinv*G==G*Sinv)
bad=unit(1,4)*unit(0,4).T
ck('ghost_exciting_creation_adverse',bad*G!=G*bad)
# Two three-level cells: charges0,+1,-1, vacuum0 in each.
q=s.diag(0,1,-1);Q=s.kronecker_product(q,s.eye(3))+s.kronecker_product(s.eye(3),q)
neutral=s.kronecker_product(unit(1,3),unit(2,3))*unit(0,9).T
charged=s.kronecker_product(unit(1,3),unit(0,3))*unit(0,9).T
ck('neutral_creation_equivariance',Q*neutral==neutral*Q)
ck('charged_creation_non_equivariance_adverse',Q*charged!=charged*Q)
elapsed=time.monotonic()-START;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if os.uname().sysname=='Darwin' else1024)
ck('resource_bounds',elapsed<180 and 0<rss<180)
print(json.dumps({'status':'PASS','checks':checks,'check_count':len(checks),'su3_generators':8,'orientations':2,'source_dimension':9,'ghost_toy_dimension':4,'gauge_toy_dimension':9,'elapsed_sec':elapsed,'peak_rss_mib':rss,'scope':'Exact SU3 Dirichlet identities and finite adverse algebra; no replacement for imported coordinate/domain theorem.'},indent=2))
