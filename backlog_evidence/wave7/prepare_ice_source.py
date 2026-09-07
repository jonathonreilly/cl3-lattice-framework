import ast, hashlib, json, os, subprocess
from pathlib import Path

E=Path(__file__).resolve().parent; C=E.parent
W=Path('/Users/jonreilly/Projects/Physics-worktrees/integration-backlog-wave7-20260907')
A=Path('/Users/jonreilly/Projects/Physics-worktrees/review-backlog-light-ice-20260907')
BASE='e043c95b37bd46d80e97c39f36c8b3cb7643c62f'
RAW='2814c6768e4d7b38048f70ad7883b4951cb12da3'
MANIFEST='docs/audit/data/citation_graph_manifest.json'
def git(*a,cwd=W): return subprocess.check_output(['git',*a],cwd=cwd)
def sha(b): return hashlib.sha256(b).hexdigest()
def tree(ref):
    out={}
    for row in git('ls-tree','-r','-z',ref).split(b'\0'):
        if row:
            m,p=row.split(b'\t',1); mode,kind,blob=m.decode().split(); out[p.decode()]=(mode,blob)
    return out
F=C/'backlog-light-ice-fixes'
I={r['path']:r for r in json.loads((F/'final_6_path_inventory.json').read_text())}
P=json.loads((F/'original_SOURCE_PREPARATION.json').read_text())
H=json.loads((F/'INPUT_CLOSURE.json').read_text())
PROTECTED={**json.loads((F/'PROTECTED_PARENT_HASHES.json').read_text()),**H['off_unit_input_hashes']}
assert len(I)==6 and git('rev-parse','HEAD').decode().strip()==BASE
assert not git('status','--porcelain').strip()
base,raw=tree(BASE),tree(RAW)
reserved=set(json.loads((C/'backlog-light-germ-review/provenance-and-inputs.json').read_text())['reserved_science_paths'])
assert not (set(I)&set(base)) and not(set(I)&reserved)
covered=set(); constituents=[]
for r in P['unit']['constituents']:
    mb=git('merge-base','--all',r['base'],r['head']).decode().split()
    assert mb==[r['merge_base']],(r,mb)
    old,head=tree(mb[0]),tree(r['head'])
    delta={p for p in old.keys()|head.keys() if old.get(p)!=head.get(p)}
    assert len(delta)==r['original_delta_paths']==4
    authored=delta-{MANIFEST}
    assert len(authored)==3 and authored<=set(I)
    assert all(p not in old and p in head and head[p]==raw[p] for p in authored)
    covered|=authored
    constituents.append({'pr':r['pr'],'head':r['head'],'actual_original_base':mb[0], 'complete_delta':[{'path':p,'base':old.get(p),'original_head':head.get(p),'raw_successor':raw.get(p),'final':I.get(p),'disposition':'regenerated_manifest' if p==MANIFEST else 'preserved_with_reviewed_scope_corrections'} for p in sorted(delta)]})
assert covered==set(I)
for p,v in I.items():
    data=(A/p).read_bytes()
    assert sha(data)==v['final_sha256'] and sha(git('show',RAW+':'+p))==v['original_sha256']
    assert raw[p][1]==v['original_raw_blob'] and raw[p][0]==v['mode']
    target=W/p; assert not target.exists(); target.parent.mkdir(parents=True,exist_ok=True)
    target.write_bytes(data); os.chmod(target,0o755 if v['mode']=='100755' else 0o644)
    assert git('hash-object',str(target)).decode().strip()==v['final_blob']
modules={p.stem:str(p.relative_to(W)) for p in (W/'scripts').glob('*.py')}; parsed={}
def scan(p):
    if p in parsed: return parsed[p]
    t=ast.parse((W/p).read_text()); imports=set(); decl=[]; timeout=None; calls=[]
    for n in ast.walk(t):
        if isinstance(n,ast.ImportFrom) and n.module and n.module.split('.')[0] in modules: imports.add(modules[n.module.split('.')[0]])
        if isinstance(n,ast.Import):
            for a in n.names:
                if a.name.split('.')[0] in modules: imports.add(modules[a.name.split('.')[0]])
        if isinstance(n,ast.Call) and ((isinstance(n.func,ast.Name) and n.func.id in {'open','exec','eval','__import__'}) or (isinstance(n.func,ast.Attribute) and n.func.attr in {'read_text','read_bytes','read','load','loadtxt','read_csv','import_module','spec_from_file_location','run','check_output','Popen','system'})): calls.append(ast.unparse(n))
    for n in t.body:
        if isinstance(n,ast.Assign):
            names={a.id for a in n.targets if isinstance(a,ast.Name)}
            if 'AUDIT_INPUT_PATHS' in names: decl=list(ast.literal_eval(n.value))
            if 'AUDIT_TIMEOUT_SEC' in names: timeout=ast.literal_eval(n.value)
    parsed[p]={'imports':sorted(imports),'declared':decl,'timeout':timeout,'dynamic_io_calls_for_review':calls}; return parsed[p]
def closure(p):
    todo=list(scan(p)['imports']); seen=set()
    while todo:
        q=todo.pop()
        if q not in seen: seen.add(q);todo+=scan(q)['imports']
    return seen
inputs=[]
for p in I:
    if not p.startswith('scripts/'): continue
    s=scan(p); c=closure(p)
    assert c==set(H['runners'][p]['actual_import_closure'])
    assert c<=set(s['declared']) and s['declared']==H['runners'][p]['final_declaration'] and s['timeout']==120
    assert not((c|set(s['declared']))&reserved)
    for q in s['declared']: assert (W/q).is_file(),q
    inputs.append({'runner':p,**s,'actual_transitive_imports':sorted(c),'input_hashes':{q:sha((W/q).read_bytes()) for q in s['declared']}})
for p,v in PROTECTED.items():
    assert p in base and sha((W/p).read_bytes())==v and sha(git('show',BASE+':'+p))==v,p
for p,v in json.loads((F/'FINAL_INPUT_HASHES.json').read_text()).items(): assert sha((W/p).read_bytes())==v,p
assert all(not x['dynamic_io_calls_for_review'] for x in parsed.values()),parsed
git('add','--',*I)
index={}
for row in git('ls-files','--stage','-z').split(b'\0'):
    if row:
        m,p=row.split(b'\t',1);mode,blob,stage=m.decode().split();assert stage=='0';index[p.decode()]=(mode,blob)
assert all(index.get(p)==v for p,v in base.items()) and set(index)-set(base)==set(I)
git('diff','--cached','--check')
patch=git('diff','--cached','--binary',BASE);(E/'ice-science-source.patch').write_bytes(patch)
d={'base':BASE,'raw_source':RAW,'source_paths':I,'all_existing_main_path_modes_blobs_unchanged':True,'existing_main_paths_preserved':len(base),'complete_original_source_dispositions':constituents,'original_scope_union_equals_final_scope':True,'input_closure':inputs,'all_actual_modules':parsed,'protected_context_hashes':PROTECTED,'reserved_selected_and_import_intersection':[],'correction_patch_sha256':sha((F/'author-correction.patch').read_bytes()),'source_patch_sha256':sha(patch),'staged_source_tree':git('write-tree').decode().strip(),'coordinator_read':'All1429 lines of author correction read, all finding dispositions and finite trial-state/connected-component derivative/sampling/effective-phase critical context inspected. Independent complete original review exists; same-session final correction confirmation remains required.'}
(E/'ice-source-preparation.json').write_text(json.dumps(d,indent=2)+'\n')
print(json.dumps({'paths':len(I),'constituents':len(constituents),'actual_modules':len(parsed),'protected_contexts':len(PROTECTED),'existing_main_paths_preserved':len(base),'source_tree':d['staged_source_tree']}))
