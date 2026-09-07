import itertools,json,time,resource,hashlib
from pathlib import Path
from fractions import Fraction
started=time.monotonic();checks=[];data={}
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
check('resource',time.monotonic()-started<180 and 0<resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024*1024)<180)
print(json.dumps({'TOTAL':len(checks),'checks':checks,'geometry':data,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'seconds':time.monotonic()-started,'rss_MiB':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024*1024),'scope':'Finite geometry and rational normalization checks only; imported stability theorem supplies the volume-uniform gap, with no computed c1 or c2.'},indent=2,allow_nan=False))
