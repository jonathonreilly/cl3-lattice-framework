import pathlib,json,hashlib,subprocess,difflib,shutil,ast
S=pathlib.Path('/private/tmp/toe-24h-probes-20260908');P=S/'native-u1-pair-and-support-port';W=pathlib.Path('/private/tmp/toe-native-u1-pair-and-all-sector-support-20260908');pack=W/'.claude/science/physics-loops/native-u1-pair-and-all-sector-support-20260908'
new=json.loads((P/'CANONICAL.json').read_text());names={'pair_author':'native-u1-pair-creation','pair_independent':'native-u1-pair-creation-cold-review','support_author':'native-u1-all-sector-connectivity-root','support_independent':'native-u1-all-sector-connectivity-cold-review'}
omit={'executed_predicates','seconds','rss_mib','rss_MiB','peak_MiB','source_sha'};comparisons={}
for k,n in names.items():
 old=json.loads((S/n/'RESULT.json').read_text());a={x:y for x,y in old.items() if x not in omit};b={x:y for x,y in new['parts'][k].items() if x not in omit};assert a==b,(k,set(a)^set(b));comparisons[k]='all non-resource/non-source-hash scientific JSON fields exactly equal'
(P/'PAYLOAD_COMPARISON.json').write_text(json.dumps(comparisons,indent=2)+'\n')
mutants=[]
for kind,old,newstr in [('pair_author','(-1, ((b, 1, True), (wv, -1, True)))','(1, ((b, 1, True), (wv, -1, True)))'),('support_author','want[a] -= 1','want[a] += 1')]:
 source=W/'scripts'/f'native_u1_pair_support_{kind}_2026_09_08.py';a=source.read_text();assert a.count(old)==1;b=a.replace(old,newstr)
 # Preserve portable fixture read while executing in scratch, without changing predicates.
 seedexpr=f"Path(__file__).resolve().parents[1] / '.claude/science/physics-loops/native-u1-pair-and-all-sector-support-20260908/inputs/GLOBAL_D4_SEED.json'"
 b=b.replace('pathlib.'+seedexpr,repr(str(pack/'inputs/GLOBAL_D4_SEED.json')))
 # Convert replacement string literal to Path object where required.
 b=b.replace(seedexpr,"Path("+repr(str(pack/'inputs/GLOBAL_D4_SEED.json'))+")")
 if kind=='pair_author':b=b.replace('rawpath = '+repr(str(pack/'inputs/GLOBAL_D4_SEED.json')),'rawpath = pathlib.Path('+repr(str(pack/'inputs/GLOBAL_D4_SEED.json'))+')')
 f=P/(kind+'_MUTANT.py');f.write_text(b);(P/(kind+'_MUTANT.diff')).write_text(''.join(difflib.unified_diff(a.splitlines(True),b.splitlines(True))))
 r=subprocess.run(['python3','-OO',str(f)],capture_output=True,text=True,timeout=180);(P/(kind+'_MUTANT.stdout')).write_text(r.stdout);(P/(kind+'_MUTANT.stderr')).write_text(r.stderr);assert r.returncode!=0 and 'RuntimeError' in r.stderr and 'FileNotFoundError' not in r.stderr
 mutants.append(dict(kind=kind,exit=r.returncode,stderr=r.stderr,scope='actual mathematical failure; portable fixture path adjusted for scratch execution'))
(P/'MUTANTS.json').write_text(json.dumps(mutants,indent=2)+'\n')
for f in P.iterdir():
 if f.is_file():shutil.copy2(f,pack/'evidence'/f.name)
for name in ['DERIVATION.md','DERIVATION_BEFORE_ABSOLUTE_PHASE_CORRECTION.md','ABSOLUTE_PHASE_CORRECTION.md']:
 src=S/'native-low-charge-u1-dictionary'/name
 if src.exists():
  dst=pack/'evidence/parent-phase-history';dst.mkdir(exist_ok=True);shutil.copy2(src,dst/name)
files={
'ASSUMPTIONS_AND_IMPORTS.md':'Finite native edge algebra; supplied relaxed cycle/low-charge domain; corrected redundant U1 map with optional bD. No extra physical register. Support theorem assumes every edge move available; Hamiltonian corollary requires every real coefficient nonzero. Eulerian orientation and finite directed-cycle decomposition are standard graph facts.',
'ROUTE_PORTFOLIO.md':'Two independently reviewed routes are assembled: direct off-D CAR/Pauli phase identity; constructive directed sink-cut and cycle support path. Their conclusions are combined without importing T-only energy statements.',
'NO_GO_LEDGER.md':'Preserve incorrect absolute hole-basis phase in parent history and corrected s0. D-conserving tests cannot identify bD; pair controls do. Connected support does not erase closed minus phase or imply Perron positivity. Projected A is not an involution. Missing/nonzero coefficient qualifier is preserved in original source history.',
'LITERATURE_BRIDGES.md':'This packet uses the existing native dictionary parents and standard finite graph decomposition. No new literature novelty or physical QED identification is claimed. It is a conditional mathematical extension of supplied carrier operations.',
'ARTIFACT_PLAN.md':'Retrospective assembly index: complete frozen proofs and reviews; four portable live helpers; one primary reading nine inputs; paired JSON; actual -OO mathematical mutants. No prospective timing is invented for this port.',
'CLAIM_STATUS_CERTIFICATE.md':'conditional-support bounded_theorem. General identities are proved in source; finite controls are selected columns/routes, not a full Hilbert census. No audit verdict, retained promotion, physical occurrence, mixing or energy conclusion.',
'REVIEW_HISTORY.md':'Pair review 13ea78b9 and connectivity review c5df4b6d are copied under evidence. The nonzero coefficient qualifier was reviewed in the same session. Canonical independent root/orbital review is pending; this assembly does not self-certify it.',
'PR_BACKLOG.md':'Root owns independent review and later graph/registry/cache/publication. This agent has not committed, pushed, or edited the graph.',
'STATUS.md':'Canonical source and four helpers assembled; primary -OO execution passed with exact scientific payload comparisons. Frozen originals and actual altered-formula failures preserved. Independent canonical review pending.',
'HANDOFF.md':'Review note and live runner, portable D4 seed closure, explicit predicate transformations and scientific JSON equality. Source graph is intentionally untouched. L8 numerical production is unrelated and unchanged.',
'QUEUE.md':'Independent canonical review; root decides later graph/registry and publication workflow. No requested additional science or numerical sampling.',
'TRACE.md':'Raw pair a20d5be8 and connectivity4c75aa74 are preserved verbatim inside the note. Portable transformations convert assertions/conditional raises into counted explicit predicates and replace scratch I/O with JSON stdout; all mathematical payloads match.',
'REVIEW.md':'Assembly validation only: four original scientific payloads match canonical -OO outputs after excluding timing/RSS and runtime source hash. Both targeted canonical mathematical mutants fail. This is not the independent canonical review.',
'ASSUMPTIONS.md':'See ASSUMPTIONS_AND_IMPORTS.md for the complete active scope.',
}
for n,t in files.items():(pack/n).write_text('# '+n[:-3].replace('_',' ')+'\n\n'+t+'\n')
(pack/'STATE.yaml').write_text('status: conditional-support\nphase: canonical-review-pending\nscience_changed: false\npublication_authority: root\n')
(pack/'N1_N8.md').write_text('''# Scope ledger N1–N8

N1: finite supplied native algebra and low domain only.
N2: exact corrected phase and all nonzero-edge premise are explicit.
N3: selected finite controls do not replace the analytic proof.
N4: original failed phase/qualifier hypotheses remain preserved.
N5: primary emits actual per_element/per_site/per_mode/per_block/lattice_wide scopes and executed predicate totals.
N6: no Perron, mixing, gap, or fixed-D energy transfer.
N7: no physical pair-production/preparation/coupling-selection conclusion.
N8: independent canonical review and later audit remain distinct; no audit verdict assigned.
''')
sourcefiles=[W/'docs/NATIVE_U1_PAIR_OPERATOR_AND_ALL_LOW_SUPPORT_NOTE_2026-09-08.md',W/'scripts/native_u1_pair_and_all_low_support_2026_09_08.py']+list((W/'scripts').glob('native_u1_pair_support_*_2026_09_08.py'))+[pack/'inputs/GLOBAL_D4_SEED.json']
freeze={str(f.relative_to(W)):hashlib.sha256(f.read_bytes()).hexdigest() for f in sourcefiles};(pack/'SOURCE_FREEZE.json').write_text(json.dumps(freeze,indent=2)+'\n')
(pack/'PACK_INDEX.md').write_text('# Packet index\n\n'+''.join('- ['+str(f.relative_to(pack))+']('+str(f.relative_to(pack))+')\n' for f in sorted(pack.rglob('*')) if f.is_file() and f.name!='PACK_INDEX.md'))
print(json.dumps(freeze,indent=2))
