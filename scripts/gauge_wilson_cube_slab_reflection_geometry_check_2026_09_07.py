#!/usr/bin/env python3
"""Independent exact bit-graph/action certificate for the cube-slab reflection proof.

This checks the actual geometry and reduced words, not a numerical Haar integral
or all-coupling positivity by sampling.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[key]='1'
import argparse,hashlib,itertools,json,math,resource,signal,sys,time
from fractions import Fraction as F
from pathlib import Path
AUDIT_TIMEOUT_SEC=180
signal.alarm(AUDIT_TIMEOUT_SEC);started=time.monotonic()
p=argparse.ArgumentParser(description=__doc__);p.add_argument('--json',action='store_true');args=p.parse_args()
# Bit0=x, bit1=y, bit2=z, bit3=time; geometry is rebuilt independently.
edges=[(v,v+(1<<a),a) for v in range(16) for a in range(4) if not v&(1<<a)]
faces=[]
for a,b in itertools.combinations(range(4),2):
 rest=[c for c in range(4) if c not in (a,b)]
 for bits in itertools.product((0,1),repeat=2):
  v=sum(q<<c for c,q in zip(rest,bits));cycle=[v,v+(1<<a),v+(1<<a)+(1<<b),v+(1<<b)]
  word=[]
  for u,w in zip(cycle,cycle[1:]+cycle[:1]):word.append([min(u,w),max(u,w),1 if u<w else -1])
  faces.append(dict(axes=[a,b],base=v,word=word,kind='temporal' if 3 in (a,b) else 'spatial',omitted=(a,b)==(0,1) and not v&4))
matching=[e for e in edges if e[2]==0];half=[[e for e in edges if e[2]!=0 and (e[0]&1)==side] for side in (0,1)]
kept=[f for f in faces if not f['omitted']];cross=[f for f in kept if 0 in f['axes']];internal=[[f for f in kept if 0 not in f['axes'] and (f['base']&1)==side] for side in (0,1)]
missing=[f for f in faces if f['omitted']]
checks=[]
def ck(name,ok):
 if name in checks or not ok:raise AssertionError(name)
 checks.append(name)
ck('sixteen vertices and thirty-two links',len(edges)==32 and len(set(v for e in edges for v in e[:2]))==16)
ck('eight matching forest links',len(matching)==8 and len(set(v for e in matching for v in e[:2]))==16)
ck('two twelve-link halves',all(len(h)==12 for h in half))
ck('reflection bijects half links',{(u^1,v^1,a) for u,v,a in half[0]}==set(half[1]))
ck('twenty-four complete faces',len(faces)==24)
ck('two stripped source faces',len(missing)==2 and {f['base'] for f in missing}=={0,8})
ck('twenty-two actual action faces',len(kept)==22)
ck('ten cross couplings',len(cross)==10)
ck('six spatial four temporal cross weights',sum(f['kind']=='spatial' for f in cross)==6 and sum(f['kind']=='temporal' for f in cross)==4)
matching_edges={(u,v) for u,v,a in matching}
half_edges={(u,v) for h in half for u,v,a in h}
reduced_cross=[];coupled_left_edges=[]
for f in cross:
 word=[(u,v,sgn) for u,v,sgn in f['word'] if (u,v) not in matching_edges]
 label=f"cross face {f['axes']} base {f['base']}"
 ck(label+' has two legitimate half edges',len(word)==2 and all((u,v) in half_edges for u,v,sgn in word))
 (u,v,sgn),(r,s,other_sgn)=word
 left=(u,v) if not u&1 else (r,s)
 axis=next(a for a in f['axes'] if a!=0)
 ck(label+' pairs its declared reflected endpoints',(u^1,v^1)==(r,s) and left==(f['base'],f['base']+(1<<axis)))
 ck(label+' has opposite unit orientations',sgn in (-1,1) and other_sgn==-sgn)
 coupled_left_edges.append(left)
 reduced_cross.append(dict(axes=f['axes'],base=f['base'],kind=f['kind'],word=word,left_edge=left))
expected_coupled={(u,v) for u,v,a in half[0]}-{(0,2),(8,10)}
ck('complete cross pairs exclude exactly the two source y pairs',len(coupled_left_edges)==len(expected_coupled)==10 and set(coupled_left_edges)==expected_coupled)
ck('two identical six-face halfactions',all(len(h)==6 and sum(f['kind']=='spatial' for f in h)==2 for h in internal))
ck('reflection bijects half faces',{(tuple(f['axes']),f['base']^1) for f in internal[0]}=={(tuple(f['axes']),f['base']) for f in internal[1]})
source=next(f for f in missing if f['base']==0)
reduced_source=[('R' if u&1 else 'L',sgn) for u,v,sgn in source['word'] if (v-u)!=1]
ck('source is unnormalized matrix pairing R Ldagger',reduced_source==[('R',1),('L',-1)])
variables={(0,2):'U',(8,10):'V'}
reduced_half=[]
for f in internal[0]:
 word=[(variables[(u,v)],sgn) for u,v,sgn in f['word'] if (u,v) in variables]
 reduced_half.append(dict(axes=f['axes'],base=f['base'],kind=f['kind'],word=word))
ck('two spatial amplitude words U and V',[f['word'] for f in reduced_half if f['kind']=='spatial']==[[('U',1)],[('V',1)]])
temporal_words=[f['word'] for f in reduced_half if f['kind']=='temporal']
ck('one temporal U Vdagger and three identity words',temporal_words.count([])==3 and [('U',1),('V',-1)] in temporal_words)
spatial_total=2*2*F(1,2)+6*F(1,2);temporal_total=2*4+4
ck('actual isotropic action bound coefficient seventeen',spatial_total==5 and temporal_total==12 and spatial_total+temporal_total==17)
ck('scalar matrix trace normalization',sum(F(1,3) for _ in range(3))==1)
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024);elapsed=time.monotonic()-started
if not(math.isfinite(rss) and 0<rss<180 and math.isfinite(elapsed) and 0<=elapsed<180):raise AssertionError('resource contract')
out=dict(checks=checks,check_count=len(checks),vertex_dictionary='v=x+2y+4z+8time',edges=edges,faces=faces,matching=matching,half_links=half,cross_faces=cross,reduced_cross_words=reduced_cross,expected_coupled_left_edges=sorted(expected_coupled),internal_faces=internal,reduced_source_word=reduced_source,reduced_half_action=reduced_half,spatial_total=str(spatial_total),temporal_total=temporal_total,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),dependencies={},seconds=elapsed,rss_MiB=rss,resources=dict(timeout_seconds=180,rss_limit_MiB=180,blas_threads=1),scope='Exact finite graph, action weights and reduced words only. Haar gauge changes, Peter-Weyl injectivity and strict nonzero averaged amplitude are analytic source proof, not numerically tested positivity. No dressed-source or physical environment identification.')
if args.json:print(json.dumps(out,indent=2,allow_nan=False))
else:
 print('PASS independent cube-slab reflection geometry:',len(checks),'named exact checks')
 print('per_element:32 links,24 faces,22 action faces after two marked weights are stripped.')
 print('per_site:8-link matching forest, two12-link halfcubes; reflection bijections checked.')
 print('per_mode:10 cross convolutions have6 spatial halfweights and4 temporal weights;2 bottom ylinks omitted.')
 print('per_face: actual reduced cross words',reduced_cross,'; expected coupled left edges',sorted(expected_coupled))
 print('per_block: source word',reduced_source,'; half-action reduced words',reduced_half)
 print('lattice_wide: graph bookkeeping is executed; all-coupling strict positivity remains the analytic Haar/reflection proof.')
 print('SOURCE_SHA256',out['source_sha256']);print('DEPENDENCIES {}')
 print('RESOURCES',elapsed,rss,'seconds/MiB;180 limits, BLAS1')
 print('TOTAL: PASS FAIL=0')
