#!/usr/bin/env python3
"""Admissible counterexample to the original note's displayed Eq. (6).

No candidate runner imports. This checks a source equation, not an audit grade.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
os.environ['OMP_NUM_THREADS']='1'
import json
from pathlib import Path
import numpy as np
from scipy.linalg import eigh,expm
from scipy.integrate import quad

I=np.eye(2)
X=np.array([[0,1],[1,0]],complex)
Y=np.array([[0,-1j],[1j,0]],complex)
Z=np.diag([1.,-1.])
P=lambda a,b,c:np.kron(np.kron(a,b),c)
N=lambda a:float(np.linalg.norm(a,2))
comm=lambda a,b:a@b-b@a
h=P(X,I,I)
local_terms=[-P(Z,X,I),2*P(I,Y,I),-P(Z,Z,I)]
A=sum(local_terms)
B=3*P(I,Z,X)
H=A+B+h
qs=[(np.eye(8)+sign*P(Z,I,I))/2 for sign in [-1,1]]

def unitary(matrix):
    values,vectors=eigh(matrix)
    return lambda time:(vectors*np.exp(1j*time*values))@vectors.conj().T

UA,UAB=unitary(A),unitary(A+B)
def a(time):
    return N(UAB(time)@h@UAB(-time)-UA(time)@h@UA(-time))

time=.4
C=expm(-1j*time*(A+B))@expm(1j*time*H)
CP=expm(-1j*time*A)@expm(1j*time*(A+h))
actual=N(C-CP)
positive,positive_error=quad(a,0,time,epsabs=1e-12,epsrel=1e-12)
negative,negative_error=quad(lambda s:a(-s),0,time,epsabs=1e-12,epsrel=1e-12)
symmetric,symmetric_error=quad(lambda s:max(a(s),a(-s)),0,time,epsabs=1e-12,epsrel=1e-12)
# ||d alpha_s^K(h)/ds|| <= 2||K||||h||. Thus a(s) is Lipschitz
# with constant at most 2||h||(2||A||+||B||) = 4 sqrt(6)+6.
# Midpoint integration error is bounded by L*T^2/(4*N), independently
# of scipy's diagnostic quadrature estimate.
subintervals=1024
midpoint_average=sum(a((k+.5)*time/subintervals) for k in range(subintervals))*time/subintervals
lipschitz=4*np.sqrt(6)+6
midpoint_error_bound=lipschitz*time*time/(4*subintervals)
midpoint_upper=midpoint_average+midpoint_error_bound
column_lower=max(float(np.linalg.norm((C-CP)[:,j])) for j in range(8))
termwise_residual=max(N(comm(q,term)) for q in qs for term in local_terms+[B])
result=dict(
    scope='Read-only counterexample to original Eq. (6); no audit verdict',
    fixture=dict(sites=[0,1,2],X=[0],patch=[0,1],radius=1,interaction_range=1,
                 deleted='X_0',patch_remaining='-Z_0 X_1 + 2 Y_1 - Z_0 Z_1',
                 exterior='3 Z_1 X_2',Record='(I +/- Z_0)/2',tau=time),
    termwise_Record_commutator_residual=termwise_residual,
    exterior_deleted_commutator=N(comm(B,h)),
    actual_cocycle_difference=actual,
    basis_column_lower_bound=column_lower,
    incorrect_positive_time_integral=positive,
    positive_quadrature_estimate=positive_error,
    correct_negative_time_integral=negative,
    negative_quadrature_estimate=negative_error,
    corrected_symmetric_integral=symmetric,
    symmetric_quadrature_estimate=symmetric_error,
    positive_midpoint_integral=midpoint_average,
    positive_midpoint_analytic_discretization_error=midpoint_error_bound,
    positive_midpoint_upper=midpoint_upper,
    source_equation_6_is_violated=actual>positive,
    violation_survives_basis_column_and_Lipschitz_midpoint_bounds=bool(column_lower>midpoint_upper+1e-9),
    corrected_bounds_hold=actual<=negative+1e-12 and actual<=symmetric+1e-12,
    numerics_note='The midpoint discretization remainder is analytically bounded; matrix arithmetic is ordinary double precision, not interval-certified.')
out=Path(__file__).resolve().parent/'time-orientation-counterexample.json'
out.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
assert termwise_residual<1e-12
assert result['violation_survives_basis_column_and_Lipschitz_midpoint_bounds']
assert result['corrected_bounds_hold']
