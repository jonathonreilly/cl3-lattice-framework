from pathlib import Path
from fractions import Fraction as F
import sys,types,json,hashlib,shutil
B=Path('/private/tmp/toe-24h-probes-20260908');P=B/'native-selected-principal-saved-design';R=B/'native-selected-principal-saved-root-review';E=B/'native-selected-principal-saved-cold-review';E.mkdir(exist_ok=True)
m=types.ModuleType('checker');m.__file__=str(P/'checker.py');exec(compile(Path(m.__file__).read_bytes(),m.__file__,'exec'),m.__dict__)
S=1<<192;Q=1<<256;rows=[]
for i in range(24):
 for j in range(i,24):rows.append({'a':i,'b':j,'g':[S if i==j else 0]*2,'j':[S//256 if (i,j)==(0,1)else 0]*2})
c,r,labels,embedding=m.reconstruct(list(range(24)),rows)
assert len(labels)==48 and all(x==0 for row in r for x in row)
expected=[[F(int(i==j))for j in range(48)]for i in range(48)]
for i,j,sgn in [(0,3,1),(3,0,1),(1,2,-1),(2,1,-1)]:expected[i][j]=F(sgn,256)
assert c==expected
stages={};ans=m.certificate(c,r,[[F(int(i==j))for j in range(48)]for i in range(48)],embedding,lambda name,data:stages.__setitem__(name,data))
assert ans['e']==F(1,128)
# Every embedding column has two half entries, hence Frobenius norm sqrt(24).
a=stages['coefficient_box']['radius']*F(127,128)**2/F(1,128)
assert (a*Q).denominator==1 and (a-F(1,Q))**2<24<=a*a
assert ans['width_pass']is False and ans['l1_pass']is True
# Noncommuting matrix factors: directly expanded 2x2 expected entries.
A=[[2,3],[5,7]];T=[[11,13],[0,17]]
assert m.multiply(m.multiply(m.transpose(T),A),T)==[[242,847],[1221,4129]]
checks={'complete_synthetic_paired48_reconstruction':True,'mixed_Gamma_signs':True,'zero_radius_identity_plus_skew_pair':True,'analytic_frobenius_error_1_over_128':True,'embedding_sqrt24_upward_grid':True,'flags_false_true':True,'noncommuting_product_expansion':True,'native_events_or_matrices_loaded':False}
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();f=json.loads((P/'RUNTIME_FREEZE.json').read_text());rf=json.loads((R/'ROOT_FREEZE.json').read_text())
for n,h in f['inputs'].items():assert sha(Path(n))==h,n
for n,h in rf['files'].items():assert sha(R/n)==h,n
assert rf['worker_freeze']==sha(P/'RUNTIME_FREEZE.json')
(E/'CONTROLS.json').write_text(json.dumps(checks,indent=2)+'\n');shutil.copy2(__file__,E/'controls.py')
(E/'REVIEW.md').write_text('''# Independent saved selected-matrix checker review

PASS for worker 288db3cc and root 64f4fd92. Root read the complete checker, replay, worker, dispatcher and schema, and every monitor change from reviewed 406b. All 7762 transitive runtime pins and all root source pins passed. This checker imports no original selected builder, candidate generator, native reader, oracle or interval implementation. Original entry truth is inherited through immutable accepted input authentication.

The independent reconstruction uses all 300 saved selected-entry pairs, exact half-seed/Gamma embedding signs and paired symmetry. Its (T-transpose C)T association and k-first contraction differ from the producer's T-transpose(CT). Exact positive-upper T is a legitimate candidate regardless of how it was proposed; replaying Cholesky proposal arithmetic is not needed for the stated posterior certificate. Directed dyadic endpoints, Frobenius upper roots, inverse correction, ET box and unchanged width/l1 gates match the proof.

Seven independent synthetic predicates use a full fabricated 48-column paired Gram with one nonzero mixed block: expected signed entries are independently specified, the exact error is 1/128 and the embedding norm is sqrt(24). A separate noncommuting 2x2 product has manually expanded expected entries. No actual IDs, T, events, Gram or native table was loaded. Author nonnumeric-status repair and its control are preserved with fe72 predecessor; final result e/radius/flags are exposed for external binding.

The whole five-orbit acceptance schema checks literal flags/timings, exact accepted e/radius, complete intermediate stage order/shapes and final partial. Author full synthetic five-orbit fixture plus five adverse cases passed. Structural acceptance is reused where stated, not counted as independent entry evaluation. The saved worker persists each independent matrix/error/box before comparing and retains failures. One 120/119.5/119-second,384-MiB contract includes final pins and root parsing; its fit is not presumed. Source readiness and metadata activation passed without reconstruction. Exact remote preregistration and external resource reconciliation precede acceptance. No physical calculation is rerun, and no failed coefficient gate is promoted.
''')
print({'worker':sha(P/'RUNTIME_FREEZE.json'),'root':sha(R/'ROOT_FREEZE.json'),'pins':len(f['inputs']),'review':sha(E/'REVIEW.md')})
