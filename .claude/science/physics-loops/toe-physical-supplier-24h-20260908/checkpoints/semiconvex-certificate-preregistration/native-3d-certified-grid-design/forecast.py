"""Pure forecast calculation; no execution or eigenvalues at import."""
import math
from itertools import product

def calculate(result,external_seconds):
 if not math.isfinite(external_seconds) or not 0<external_seconds<=30:raise ValueError('external profile cap')
 expected=[(r,j) for r in (0,1,3,5,10,15) for j in product((0,4,8,12),(0,8),(0,8))]
 if len(result['rows'])!=96:raise ValueError('fixed96 coverage')
 totals=[]
 for row,(r,j) in zip(result['rows'],expected):
  if (row['rep'],tuple(row['index']))!=(r,j):raise ValueError('fixed matrix identity')
  ts=[row[n] for n in ('build_seconds','eigh_seconds','certificate_seconds','serialization_seconds')]
  if any(not math.isfinite(x) or x<=0 for x in ts):raise ValueError('positive complete timers')
  totals.append(sum(ts))
 if sum(totals)>external_seconds:raise ValueError('external accounting')
 overhead=external_seconds-sum(totals);perjob=2*(1024*max(totals)+overhead);aggregate=24*perjob+external_seconds+60
 return dict(grid_matrices=6*32**3,unique_matrices=6*16**3,multiplicity=8,matrices_per_job=1024,jobs=24,max_observed_complete_matrix_seconds=max(totals),overhead_charged_per_job=overhead,padded_job_seconds=perjob,aggregate_seconds=aggregate,forecast_gate=perjob<=150 and aggregate<=2880,proposed_hard_job_seconds=180,proposed_hard_aggregate_seconds=3600,scope='empirical scheduling forecast only; grid unlaunched')
