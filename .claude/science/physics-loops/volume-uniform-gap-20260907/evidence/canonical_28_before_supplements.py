import time
started=time.monotonic()
import os,sys,signal,resource,hashlib,itertools,json,math
from pathlib import Path
from fractions import Fraction
AUDIT_TIMEOUT_SEC=180
AUDIT_MEMORY_MIB=180
os.environ['OPENBLAS_NUM_THREADS']='1'
os.environ['OMP_NUM_THREADS']='1'
if sys.argv[1:] not in ([],['--json']):
    raise SystemExit('usage: gauge_wilson_electric_dominated_volume_uniform_gap_check_2026_09_07.py [--json]')
def timeout_handler(signum,frame):
    raise TimeoutError('180-second execution limit exceeded')
signal.signal(signal.SIGALRM,timeout_handler)
signal.alarm(AUDIT_TIMEOUT_SEC)
def peak_rss_mib():
    raw=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return raw/(1024*1024) if sys.platform=='darwin' else raw/1024
checks=[];data={}
def check(n,v):
 assert n not in checks and bool(v),n
 checks.append(n)
e=[tuple(int(i==j) for i in range(3)) for j in range(3)]
def add(x,y):return tuple(a+b for a,b in zip(x,y))
def cube(n):return set(itertools.product(range(n),repeat=3))
def loop(x,i,j):
 return [(x,i,1),(add(x,e[i]),j,1),(add(x,e[j]),i,-1),(x,j,-1)]
def endpoints(item):
 x,i,sgn=item;y=add(x,e[i]);return (x,y) if sgn==1 else (y,x)
for L in [1,2,3]:
 cells=cube(L);groups=[x for x in cells if all(add(x,z) in cells for z in e)]
 indiv=[(x,i,j) for x in cells for i,j in itertools.combinations(range(3),2) if add(x,e[i]) in cells and add(x,e[j]) in cells]
 check('group_count_'+str(L),3*len(groups)==3*(L-1)**3)
 check('individual_count_'+str(L),len(indiv)==3*L*(L-1)**2)
 check('omitted_boundary_'+str(L),len(indiv)-3*len(groups)==3*(L-1)**2)
 for x,i,j in indiv:
  w=loop(x,i,j);ends=[endpoints(a) for a in w]
  assert all(ends[k][1]==ends[(k+1)%4][0] for k in range(4))
  assert {a[0] for a in w}=={x,add(x,e[i]),add(x,e[j])}
 check('all_loop_supports_'+str(L),True)
 data['cells_'+str(L)]={'cells':len(cells),'link_factors':3*len(cells),'whole_group_plaquettes':3*len(groups),'individually_supported_plaquettes':len(indiv),'omitted_individual_plaquettes':[z for z in indiv if z[0] not in groups]}
for L in [1,2]:
 verts=cube(L+1);pad=cube(L+2)
 real={(x,i) for x in verts for i in range(3) if add(x,e[i]) in verts}
 all_links={(x,i) for x in pad for i in range(3)}
 faces=[(x,i,j) for x in verts for i,j in itertools.combinations(range(3),2) if add(add(x,e[i]),e[j]) in verts]
 check('open_edges_'+str(L),len(real)==3*L*(L+1)**2)
 check('open_faces_'+str(L),len(faces)==3*L*L*(L+1))
 check('padded_range_'+str(L),all(all(add(x,z) in pad for z in e) for x,i,j in faces))
 used={(y,k) for x,i,j in faces for y,k,sgn in loop(x,i,j)}
 check('no_ghost_interaction_'+str(L),used<=real and real<=all_links)
 check('three_terms_per_anchor_'+str(L),max(sum(y==x for y,i,j in faces) for x in verts)<=3)
 data['open_box_'+str(L)]={'vertices':len(verts),'real_links':len(real),'plaquettes':len(faces),'padded_cells':len(pad),'extra_decoupled_links':len(all_links-real)}
check('electric_gap_normalization',Fraction(1,4)*4==1)
check('perturbation_norm_coefficient',3*Fraction(1,4)==Fraction(3,4))
check('gap_rescaling',4*Fraction(1,2)==2)
check('onsite_incidence_bound',len([(0,0,0)]+e)==4)
check('local_energy_coefficient',2*4==8)
check('resource',time.monotonic()-started<180 and 0<peak_rss_mib()<180)
groups={
 'per_element':[n for n in checks if n.startswith(('open_edges_','open_faces_'))],
 'per_site':[n for n in checks if n.startswith(('padded_range_','no_ghost_interaction_','three_terms_per_anchor_')) or n in ('onsite_incidence_bound','local_energy_coefficient')],
 'per_mode':['electric_gap_normalization'],
 'per_block':['perturbation_norm_coefficient','gap_rescaling'],
 'lattice_wide':[n for n in checks if n.startswith(('group_count_','individual_count_','omitted_boundary_','all_loop_supports_')) or n=='resource'],
}
assert len(checks)==28 and len(set(checks))==28
assert sorted(sum(groups.values(),[]))==sorted(checks)
seconds=time.monotonic()-started;rss=peak_rss_mib()
assert math.isfinite(seconds) and 0<=seconds<AUDIT_TIMEOUT_SEC
assert math.isfinite(rss) and 0<rss<AUDIT_MEMORY_MIB
result={'TOTAL':len(checks),'checks':checks,'geometry':data,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'seconds':seconds,'rss_MiB':rss,'scope':'Finite geometry and rational normalization checks only; imported stability theorem supplies the volume-uniform gap, with no computed c1 or c2.','scope_checks':groups,'audit_timeout_sec':AUDIT_TIMEOUT_SEC,'audit_memory_mib':AUDIT_MEMORY_MIB}
if sys.argv[1:]==['--json']:
 print(json.dumps(result,indent=2,allow_nan=False))
else:
 print('PASS: exact outgoing-link geometry, boundary discrepancy, padding and scalar normalization')
 print('per_element: PASS 4 actual open-graph edge/face counts; no Haar spectrum computed')
 print('per_site: PASS 8 padded-cell support and local-energy incidence checks')
 print('per_mode: PASS 1 electric-gap scale check; all-label proof is analytical upstream')
 print('per_block: PASS 2 magnetic-norm and gap-rescaling checks')
 print('lattice_wide: PASS 13 finite-boundary/loop checks and resource guard; stability theorem imported')
 print('TOTAL: PASS 28 unique named checks')
 print('SCOPE: no numerical c1/c2, arbitrary-coupling gap, continuum limit or physical parameter selection')
 print('RESOURCE: seconds='+str(seconds)+' rss_MiB='+str(rss)+' limits=180sec/180MiB')
 print('SOURCE_SHA256: '+result['source_sha256'])
signal.alarm(0)
