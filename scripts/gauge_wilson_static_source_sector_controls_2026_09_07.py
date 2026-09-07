#!/usr/bin/env python3
"""Exact finite support controls; the analytic theorem is in the source note."""
import os, sys, time, signal, resource, json, hashlib, math
from pathlib import Path
AUDIT_TIMEOUT_SEC = 180
AUDIT_RSS_LIMIT_MIB = 180
_started = time.monotonic()
for _name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_name] = '1'
if sys.argv[1:] not in ([], ['--json']):
    raise SystemExit('usage: '+Path(__file__).name+' [--json]')
def _timeout(signum, frame):
    raise TimeoutError('180-second audit budget exceeded')
signal.signal(signal.SIGALRM, _timeout)
signal.alarm(AUDIT_TIMEOUT_SEC)
def _rss():
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / (1048576 if sys.platform == 'darwin' else 1024)
def _finite(value):
    if isinstance(value, float) and not math.isfinite(value):
        raise AssertionError('nonfinite output')
    if isinstance(value, dict):
        for item in value.values(): _finite(item)
    elif isinstance(value, (list, tuple)):
        for item in value: _finite(item)
def _emit(out, expected, scopes):
    assert out['TOTAL'] == expected == len(set(out['checks']))
    assert 0 < _rss() < AUDIT_RSS_LIMIT_MIB
    assert time.monotonic() - _started < AUDIT_TIMEOUT_SEC
    assert sum(v['checks'] for v in scopes.values()) == expected
    out['N5_scopes'] = scopes
    out['resource_limits'] = {'seconds': AUDIT_TIMEOUT_SEC, 'rss_MiB': AUDIT_RSS_LIMIT_MIB}
    _finite(out)
    if sys.argv[1:] == ['--json']:
        print(json.dumps(out, sort_keys=True, indent=2, allow_nan=False))
    else:
        print('PASS '+Path(__file__).name)
        for key, item in scopes.items(): print(key+': '+str(item['checks'])+' checks; '+item['scope'])
        print('TOTAL: '+str(expected))
        print('seconds: '+str(out['seconds'])+'; rss_MiB: '+str(out['rss_MiB']))
        print('source_sha256: '+out['source_sha256'])
    signal.alarm(0)
import itertools
from fractions import Fraction as F
started=_started; checks=[]
def ck(n,b):
 if n in checks or not b:raise AssertionError(n)
 checks.append(n)
def incidence(vertices,edges):return [[int(v==a)-int(v==b) for a,b in edges] for v in vertices]
def solve(A,b):
 R=[[int(x)%3 for x in row]+[int(y)%3] for row,y in zip(A,b)];m=len(R);n=len(R[0])-1;piv=[];r=0
 for c in range(n):
  k=next((k for k in range(r,m) if R[k][c]),None)
  if k is None:continue
  R[r],R[k]=R[k],R[r];q=pow(R[r][c],-1,3);R[r]=[(q*x)%3 for x in R[r]]
  for k in range(m):
   if k!=r:
    q=R[k][c];R[k]=[(x-q*y)%3 for x,y in zip(R[k],R[r])]
  piv.append(c);r+=1
 if any(not any(row[:-1]) and row[-1] for row in R):return [],piv
 free=[j for j in range(n) if j not in piv];out=[]
 for vals in itertools.product(range(3),repeat=len(free)):
  z=[0]*n
  for j,x in zip(free,vals):z[j]=x
  for k,j in enumerate(piv):z[j]=(R[k][-1]-sum(R[k][c]*z[c] for c in free))%3
  assert all((sum(x*y for x,y in zip(row,z))-v)%3==0 for row,v in zip(A,b));out.append(z)
 return out,piv
def component(edges,flow,x):
 reached={x};changed=True
 while changed:
  changed=False
  for (a,b),v in zip(edges,flow):
   if v and (a in reached or b in reached):
    old=len(reached);reached.update((a,b));changed|=len(reached)>old
 return reached
def distance(edges,x,y):
 reached={x};front={x};d=0
 while y not in reached:
  d+=1;nxt=set()
  for a,b in edges:
   if a in front:nxt.add(b)
   if b in front:nxt.add(a)
  nxt-=reached
  if not nxt:raise ValueError('disconnected')
  reached|=nxt;front=nxt
 return d
def flows(vertices,edges,x,y,keep=None):
 A=incidence(vertices,edges);b=[int(v==x)-int(v==y) for v in vertices]
 if keep is not None:A=[A[i] for i in keep];b=[b[i] for i in keep]
 return solve(A,b)
vertices=list(itertools.product(range(2),repeat=3));edges=[]
for x in vertices:
 for i in range(3):
  if x[i]==0:
   y=list(x);y[i]=1;edges.append((x,tuple(y)))
ck('actual_unit_cube_8_vertices_12_links',len(vertices)==8 and len(edges)==12)
cube=[]
for y,expected in [((1,0,0),1),((1,1,0),2),((1,1,1),3)]:
 sol,piv=flows(vertices,edges,(0,0,0),y);support=[sum(v!=0 for v in z) for z in sol];d=distance(edges,(0,0,0),y)
 ck('cube_distance_'+str(expected),d==expected)
 ck('cube_rank7_nullity5_'+str(expected),len(piv)==7 and len(sol)==243)
 ck('cube_source_component_'+str(expected),all(y in component(edges,z,(0,0,0)) for z in sol))
 ck('cube_exact_support_threshold_'+str(expected),min(support)==d)
 branching=sum(any(v not in [(0,0,0),y] and sum(z[j]!=0 for j,e in enumerate(edges) if v in e)==3 for v in vertices) for z in sol)
 cube.append({'source':[(0,0,0),y],'distance':d,'minimum':min(support),'branching_flow_count':branching,'all_affine_flows':sol})
linev=list(range(5));linee=list(zip(range(4),range(1,5)));full,_=flows(linev,linee,0,4);partial,_=flows(linev,linee,0,4,[0,2,4])
ck('line_full_gauss_threshold4',min(sum(x!=0 for x in z) for z in full)==4)
ck('line_dropped_gauss_threshold2',min(sum(x!=0 for x in z) for z in partial)==2)
ck('line_disconnected_source_components_adverse',any(4 not in component(linee,z,0) for z in partial))
uv=[(0,0),(1,0),(1,1),(0,1)];ue=[(uv[0],uv[1]),(uv[1],uv[2]),(uv[3],uv[2])];ge=ue+[(uv[0],uv[3])]
actual,_=flows(uv,ue,uv[0],uv[3]);ghost,_=flows(uv,ge,uv[0],uv[3]);fixed=[z for z in ghost if z[-1]==0]
ck('actual_U_graph_distance3',distance(ue,uv[0],uv[3])==3 and min(sum(x!=0 for x in z) for z in actual)==3)
ck('unfixed_ghost_shortcut1',distance(ge,uv[0],uv[3])==1 and min(sum(x!=0 for x in z) for z in ghost)==1)
ck('fixed_ghost_restores3',min(sum(x!=0 for x in z) for z in fixed)==3 and all(z[-1]==0 for z in fixed))
normcases=[]
for name,norms in [('equal',[F(1)]*9),('one_to_nine',list(map(F,range(1,10)))),('pythagorean',[F(5,13)]*3+[F(13,17)]*3+[F(17,25)]*3)]:
 lhs=sum(norms)**2;rhs=9*sum(x*x for x in norms)
 ck('nine_component_Cauchy_'+name,lhs<=rhs);normcases.append({'name':name,'norms':list(map(str,norms)),'lhs_squared':str(lhs),'rhs_squared':str(rhs)})
ck('source_factor3_saturated',sum([F(1)]*9)**2==9*sum([F(1)]*9))
ck('source_factor1_adverse',sum([F(1)]*9)**2>sum([F(1)]*9))
eta=F(1,4);g=F(3);off=F(1,4);threshold=(1-eta)*g
ck('toy_relative_column_bound',max(off/F(3),off/F(5))<=eta)
a=F(3)-threshold;b=F(5)-threshold
ck('toy_shifted_positive_principal_minors',a>0 and b>0 and a*b-off*off>0)
z=F(2);ck('toy_restricted_Neumann_safe',eta*g/(g-z)<1)
zbad=F(5,2);ck('toy_sufficient_bound_adverse',eta*g/(g-zbad)>1)
H0=[[F(int(i==j)*v) for j in range(4)] for i,v in enumerate([0,1,3,5])];P=[[F(int(i==j and i>=2)) for j in range(4)] for i in range(4)]
V=[[F(0) for j in range(4)] for i in range(4)];V[2][3]=V[3][2]=off
bad=[row[:] for row in V];bad[1][2]=bad[2][1]=F(1,10)
def mul(A,B):return [[sum(a*b for a,b in zip(row,col)) for col in zip(*B)] for row in A]
ck('toy_preserves_charge_projection',mul(V,P)==mul(P,V))
ck('toy_broken_sector_adverse',mul(bad,P)!=mul(P,bad))
ck('global_low_neutral_level_not_charged',min(x for x in [0,1,3,5] if x)>0 and min([1,3,5])==1<g)
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1048576 if sys.platform=='darwin' else 1024)
ck('positive_resources',0<rss<180 and time.monotonic()-started<180)
out={'TOTAL':len(checks),'checks':checks,'cube_vertices':vertices,'cube_edges':edges,'cube_cases':cube,'line_full_flows':full,'line_dropped_gauss_flows':partial,'U_graph_flows':actual,'ghost_flows':ghost,'fixed_ghost_flows':fixed,'nine_source_norm_cases':normcases,'toy':{'H0':[0,1,3,5],'charged_threshold':str(g),'off_diagonal':str(off),'eta':str(eta),'guaranteed_lower':str(threshold),'safe_z':str(z),'insufficient_z':str(zbad)},'seconds':time.monotonic()-started,'rss_MiB':rss,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'Exact finite graph F3 necessary-charge controls and explicit norm/resolvent toys; not a proof of the imported dressed-coordinate estimate or a finite approximation to the interacting SU3 spectrum.'}

_emit(out, 32, {'per_element': {'checks': 1, 'scope': 'actual unit cube geometry'}, 'per_site': {'checks': 6, 'scope': 'boundary Gauss and ghost-shortcut controls'}, 'per_mode': {'checks': 5, 'scope': 'nine-source norm inequality controls'}, 'per_block': {'checks': 12, 'scope': 'three complete affine cube source-flow censuses'}, 'lattice_wide': {'checks': 8, 'scope': 'seven explicit resolvent/sector toys and resources; no imported-theorem proof'}})
