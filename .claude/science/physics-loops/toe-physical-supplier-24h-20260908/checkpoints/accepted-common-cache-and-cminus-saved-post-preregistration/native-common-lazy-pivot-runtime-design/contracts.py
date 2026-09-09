"""Pure contract helpers only; no input reader, matrix builder or pivot invocation."""
from fractions import Fraction as F

def labels(augmented=False):
 a=[{'kind':'pole','node':n,'source':s,'eta':eta,'plus':2*n+1,'minus':2*n,'residual_weight':2} for n in range(66) for s in range(3) for eta in(-1,1)]
 if augmented:a.extend({'kind':'append','source':s,'eta':1,'residual_weight':1} for s in range(3))
 return a

def residual_upper(diagonal_upper,augmented=False):
 lab=labels(augmented)
 if len(diagonal_upper)!=len(lab):raise ValueError('dimension')
 if any(F(v)<0 for v in diagonal_upper):raise ValueError('negative PSD upper')
 return sum((F(v)*x['residual_weight'] for v,x in zip(diagonal_upper,lab)),F())

def target(augmented=False):return F(1,10**6*(1062 if augmented else 1058))

def native(*args,**kwargs):raise RuntimeError('DESIGN ONLY: no cost/runtime/rounding certificate')
