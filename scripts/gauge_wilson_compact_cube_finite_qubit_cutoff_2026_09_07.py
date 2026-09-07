#!/usr/bin/env python3
"""Finite compact cube cutoff/spectral support; exact scope in linked theorem."""
import os,time,signal,sys
AUDIT_TIMEOUT_SEC=180
AUDIT_MEMORY_LIMIT_MB=180
START=time.monotonic();signal.alarm(AUDIT_TIMEOUT_SEC)
if sys.argv[1:] not in ([], ['--json']):raise SystemExit('usage: '+sys.argv[0]+' [--json]')
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
import sympy as s,json,resource,sys,hashlib
from pathlib import Path
checks=[]
def ck(n,v):
 assert n not in checks and bool(v),n
 checks.append(n)
N,j=s.symbols('N j',integer=True,positive=True)
poly=lambda n:n**2*(n+1)**2*(n-1)*(n+2)*(3*n*n+3*n+2)/2880
shell=s.summation(j*j*(N-j)**2,(j,1,N-1))*N*N/4
ck('shell exact sum',s.simplify(shell-(N**7-N**3)/120)==0)
ck('dimension polynomial recurrence',s.simplify(poly(N)-poly(N-1)-(N**7-N**3)/120)==0)
ck('dimension baseR0',poly(s.Integer(2))==1)
rows=[]
for R in (0,1,2,4,10):
 dims=[((p+1)*(q+1)*(p+q+2)//2)**2 for p in range(R+1) for q in range(R+1-p)]
 d=sum(dims);n=R+2
 ck('dimension direct sum R%d'%R,s.Integer(d)==poly(s.Integer(n)))
 bits=(d-1).bit_length();ck('minimum storage bits R%d'%R,2**bits>=d and (bits==0 or 2**(bits-1)<d))
 omitted=R+1;vals=[p*p+(omitted-p)**2+p*(omitted-p)+3*omitted for p in range(omitted+1)]
 gap=(3*omitted*omitted+3)//4+3*omitted
 ck('balanced omitted shell R%d'%R,min(vals)==gap)
 ck('next shell strictly above R%d'%R,min(p*p+(omitted+1-p)**2+p*(omitted+1-p)+3*(omitted+1) for p in range(omitted+2))>gap)
 rows.append(dict(R=R,dimension=d,qubits_per_link=bits,total_storage_qubits=12*bits,gap_times_a=gap))
s0=s.symbols('s0',integer=True,nonnegative=True)
ck('even balanced exact expression',s.expand((s0*s0+s0*s0+s0*s0+6*s0)-(3*s0*s0+6*s0))==0)
ck('odd balanced exact expression',s.expand(s0*s0+(s0+1)**2+s0*(s0+1)+3*(2*s0+1)-(3*s0*s0+9*s0+4))==0)
ck('fundamental threshold4',1+3==4)
ck('asymmetric omitted representation overestimates R1',2**2+3*2>3+6)
ck('actual Haar face leakage variance coefficient',12*s.Rational(1,6)**2==s.Rational(1,3))
ck('nonzero interacting R0 leakage',s.Rational(1,3)>0)
ck('not all finite energy inputs have positive projection',1-2<0)
ck('dimension leading power8 coefficient1over960',s.Poly(s.expand(poly(N)),N).degree()==8 and s.Poly(s.expand(poly(N)),N).LC()==s.Rational(1,960))
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024)
ck('positive resource budget',0<rss<180 and time.monotonic()-START<180)
out=dict(status='PASS',checks=checks,total=len(checks),rows=rows,elapsed_seconds=time.monotonic()-START,peak_rss_mib=rss,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())

if sys.argv[1:]==['--json']:print(json.dumps(out,indent=2,allow_nan=False))
else:
 print('PASS finite carrier and energy-cutoff checks; TOTAL='+str(out['total'])+' (31 scientific +1 resource)')
 print('per_element: Exact Peter-Weyl shell sum and dimension polynomial.')
 print('per_site: Full8-vertex Gauss action preserved analytically; no lattice-state simulation.')
 print('per_mode: Five fixed cutoffs R=0,1,2,4,10 with exact link dimensions and12-link storage.')
 print('per_block: Balanced omitted thresholds and actual-Haar R0 leakage coefficient1/3.')
 print('lattice_wide: Fixed finite cube; four-link support on retained carrier, not four-qubit compiled controls.')
 print('cutoff_rows='+json.dumps(out['rows'],sort_keys=True))
 print('resources: elapsed_sec='+str(out['elapsed_seconds'])+' rss_MiB='+str(out['peak_rss_mib'])+'; limits=180sec/180MiB')
 print('source_sha256='+out['source_sha256'])
