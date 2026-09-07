import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[k]='1'
import signal,time,resource,sys,json,hashlib,contextlib,io,runpy,math
from pathlib import Path
from fractions import Fraction as F
signal.alarm(180);start=time.monotonic()
import numpy as np
from scipy.linalg import expm,eigvalsh
AUDIT_TIMEOUT_SEC=180
AUDIT_INPUT_PATHS=['scripts/native_edge_record_reduced_cell_full_isometry_2026_09_07.py']
source=Path(__file__).resolve().parents[1]/AUDIT_INPUT_PATHS[0]
dependency_hash=hashlib.sha256(source.read_bytes()).hexdigest()
with contextlib.redirect_stdout(io.StringIO()):native=runpy.run_path(str(source))
remaining=180-(time.monotonic()-start)
if remaining<=0:raise TimeoutError('overall clock budget exhausted')
signal.setitimer(signal.ITIMER_REAL,remaining)
if hashlib.sha256(source.read_bytes()).hexdigest()!=dependency_hash:raise AssertionError('helper source changed')
checks=0;worst=0.
def ck(v):
 global checks
 checks+=1
 if not v:raise AssertionError(checks)
def close(a,b):
 global worst
 e=float(np.max(np.abs(np.asarray(a)-np.asarray(b))));worst=max(worst,e);ck(e<2e-12)
L=17;g=np.pi/2;couplings=np.array([g*math.sqrt((j+1)*(L-j)) for j in range(L)])
H=np.diag(couplings,1)+np.diag(couplings,-1)
close(eigvalsh(H),g*np.arange(-L,L+1,2))
for h,u,t in native['pulses']:ck(not native['comm'](u,native['K']))
rows=[]
for t in [0.,.99,1.,1.01,2.]:
 c=math.cos(g*t);z=-1j*math.sin(g*t)
 analytic=np.array([math.sqrt(math.comb(L,j))*c**(L-j)*z**j for j in range(L+1)])
 actual=expm(-1j*t*H)[:,0];close(actual,analytic);close(np.vdot(analytic,analytic),1)
 eta=sum(math.comb(L,j)*abs(c)**(2*(L-j))*abs(z)**(2*j) for j in range(9))
 if .99<=t<=1.01:ck(eta<1/2000)
 rows.append({'time':t,'unfinished_binomial_probability':eta,'retained_trace_bound':min(2,2*math.sqrt(eta)),'discard_clock_trace_bound':min(2,2*eta),'clock_amplitudes':[[float(x.real),float(x.imag)] for x in analytic]})
close(expm(-1j*H)[:,0],np.eye(18,dtype=complex)[:,-1]*(-1j)**17)
close(expm(-2j*H)[:,0],np.eye(18,dtype=complex)[:,0]*(-1)**17)
pi=F(22,7);eta_bound=17*pi*pi/F(360000)
ck(eta_bound<F(1,2000));ck(4*eta_bound<F(1,400));ck(2*eta_bound<F(1,1000))
ck(17*pi/2<27);ck(9*pi/2<15);ck(17*pi/2+F(11,2)<33);ck(17*15+F(11,2)<261)
ck(native['checks']==163);ck(len(native['outs'])==8);ck(len(native['pulses'])==9)
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024);ck(0<rss<180);ck(time.monotonic()-start<180)
payload={'scope':'Gauge-reduced18position clock with actual native nine-pulse dependency, not2^27simulation; retained original freeK; finitewindow only','checks':checks,'native_exact_checks':native['checks'],'worst_clock_residual':worst,'L':L,'positions':18,'native_steps':9,'identity_padding_steps':8,'g':'pi/2','T':1,'window_radius':'1/100','eta_rational_upper':str(eta_bound),'retained_uniform_trace_bound':'1/20','discard_uniform_trace_bound':'1/1000','onehot_interaction_norm':'17pi/2','onehot_total_norm_upper':33,'natural_full_extension_norm_upper':261,'register_qubits':27,'rows':rows,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'dependencies':{AUDIT_INPUT_PATHS[0]:dependency_hash},'resources':{'timeout_seconds':180,'rss_limit_MiB':180,'blas_threads':1},'seconds':time.monotonic()-start,'rss_MiB':rss}
if '--json' in sys.argv:print(json.dumps(payload,indent=2,allow_nan=False))
else:
 print('PASS reduced native autonomous clock:37 clock assertions plus163 separately accounted native isometry assertions')
 print('CERTIFICATE retained trace <1/20; discard clock trace <1/1000; window[.99,1.01]')
 print('per_element: actual nine native unitaries commute original freeK; gauge amplitudes and recurrence checked')
 print('per_site:27 reduced registers, one-hot clock18; no physical parent-register count claim')
 print('per_mode: all8 ready input columns through exact native isometry; reference extension by gauge proof')
 print('per_block:17 links,8 identity padding steps; onehot total norm<33, natural full extension<261')
 print('lattice_wide: checked and not executed -- no2^27 simulation, NN implementation or permanent completion')
 print('SOURCE_SHA256',payload['source_sha256'])
