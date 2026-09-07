import ast,hashlib,json,os,subprocess
from pathlib import Path
E=Path(__file__).resolve().parent;C=E.parent;F=C/'backlog-record-collision-fixes'
W=Path('/Users/jonreilly/Projects/Physics-worktrees/integration-backlog-wave7-20260907');A=Path('/Users/jonreilly/Projects/Physics-worktrees/fix-backlog-record-collision-8005-20260907')
BASE='e043c95b37bd46d80e97c39f36c8b3cb7643c62f';MANIFEST='docs/audit/data/citation_graph_manifest.json'
def git(*a):return subprocess.check_output(['git',*a],cwd=W)
def sha(b):return hashlib.sha256(b).hexdigest()
def tree(ref):
    out={}
    for row in git('ls-tree','-r','-z',ref).split(b'\0'):
        if row:
            m,p=row.split(b'\t',1);mode,kind,blob=m.decode().split();out[p.decode()]={'mode':mode,'kind':kind,'blob':blob}
    return out
assert (F/'HANDOFF.md').is_file() and (F/'FINAL_RECEIPT.json').is_file()
assert not(E/'record-source-preparation.json').exists()
I=json.loads((F/'FINAL_INVENTORY.json').read_text());H=json.loads((F/'INPUT_BINDING.json').read_text());M=json.loads((F/'MAIN_PRESERVATION.json').read_text());ICE=json.loads((E/'ice-source-preparation.json').read_text())
assert {r['path'] for r in I['paths'] if not r.get('selected')}=={MANIFEST}
paths={r['path']:r for r in I['paths'] if r.get('selected')};icepaths=set(ICE['source_paths']);assert len(paths)==81 and not(set(paths)&icepaths)
assert git('rev-parse','HEAD').decode().strip()==BASE and I['base']==BASE and H['base']==BASE
assert git('write-tree').decode().strip()==ICE['staged_source_tree']
assert sha((F/'candidate.patch').read_bytes())==I['candidate_patch_sha256'] and sha((F/'author-correction.patch').read_bytes())==I['author_correction_patch_sha256']
base=tree(BASE);author=tree(I['candidate_tree']);old=tree(I['raw_original_head']);oldbase=tree(I['raw_original_base']);active=tree(I['raw_active_head']);activebase=tree(I['raw_active_base'])
for head,parent in [(I['raw_original_head'],I['raw_original_base']),(I['raw_active_head'],I['raw_active_base'])]:assert git('merge-base','--all',head,parent).decode().split()==[parent]
delta={p for p in oldbase.keys()|old.keys() if oldbase.get(p)!=old.get(p)};active_delta={p for p in activebase.keys()|active.keys() if activebase.get(p)!=active.get(p)}
original_paths=set(paths)-set(I['additional_authorized_paths']);assert delta==active_delta==original_paths|{MANIFEST} and len(delta)==80
assert all(old[p]==active[p] for p in original_paths)
movement={p for p in old.keys()|active.keys() if old.get(p)!=active.get(p)}-delta
assert len(movement)==78 and movement=={r['path'] for r in M['all_78_parent_only_head_movement_paths']}
for p in movement:assert old.get(p)==oldbase.get(p) and active.get(p)==activebase.get(p) and author.get(p)==base.get(p)
assert not(set(base)-set(author))
tools_changed={'docs/audit/scripts/build_citation_graph.py','scripts/audit_packet_script_deps.py'}
assert {p for p in base if author[p]!=base[p]}==tools_changed
assert set(author)-set(base)==set(paths)-tools_changed
reserved=set(json.loads((C/'backlog-light-germ-review/provenance-and-inputs.json').read_text())['reserved_science_paths']);assert not(set(paths)&reserved)
for p,r in paths.items():
    data=(A/p).read_bytes();assert sha(data)==r['final_sha256'] and author[p]==r['final']
    if p in original_paths:assert sha(git('show',I['raw_original_head']+':'+p))==r['original_sha256'] and old[p]['blob']==r['original_blob']
    dst=W/p;assert p in tools_changed or not dst.exists() or dst.read_bytes()==data;dst.parent.mkdir(parents=True,exist_ok=True);dst.write_bytes(data);os.chmod(dst,0o755 if r['final']['mode']=='100755' else 0o644)
    assert git('hash-object',str(dst)).decode().strip()==r['final']['blob']
# Independently discover imports and literal Python paths, then read their actual I/O calls.
modules={};todo=[p for p in paths if p.startswith('scripts/native_edge_record_')];assert len(todo)==6
while todo:
    p=todo.pop()
    if p in modules:continue
    t=ast.parse((W/p).read_bytes());imports=set();literals=set();reads=[];dynamic=[];decl=[]
    for n in ast.walk(t):
        names=[x.name for x in n.names] if isinstance(n,ast.Import) else [n.module] if isinstance(n,ast.ImportFrom) and n.module else []
        for name in names:
            q='scripts/'+name.removeprefix('scripts.').split('.')[0]+'.py'
            if (W/q).is_file():imports.add(q)
        if isinstance(n,ast.Constant) and isinstance(n.value,str) and n.value.startswith('scripts/') and n.value.endswith('.py'):literals.add(n.value)
        if isinstance(n,ast.Call):
            name=ast.unparse(n.func)
            if name.endswith(('read_text','read_bytes','open')):reads.append({'line':n.lineno,'call':ast.unparse(n)})
            if name.startswith('subprocess.') or name in {'eval','exec','__import__'} or 'spec_from_file_location' in name or 'import_module' in name:dynamic.append({'line':n.lineno,'call':ast.unparse(n)})
    for n in t.body:
        if isinstance(n,ast.Assign) and any(isinstance(x,ast.Name) and x.id=='AUDIT_INPUT_PATHS' for x in n.targets):decl=list(ast.literal_eval(n.value))
    assert not((imports|literals|set(decl))&reserved)
    modules[p]={'sha256':sha((W/p).read_bytes()),'ordinary_imports':sorted(imports),'literal_python_paths':sorted(literals),'declared_inputs':decl,'read_calls':reads,'dynamic_calls':dynamic};todo+=list(imports|literals)
assert set(modules)==set(H['module_closure']) and len(modules)==7
for p,r in modules.items():
    expected=H['module_closure'][p];assert r['sha256']==expected['sha256'] and r['ordinary_imports']==expected['local_imports'] and r['declared_inputs']==expected['declared_inputs']
    assert set(r['literal_python_paths'])<=set(expected['actual_transitive_mutable_inputs'])
    assert r['read_calls']==expected['actual_read_calls']
for r in M['112_reviewed_parent_sources_sha256']:
    p,v=r['path'],r['sha256'];assert sha((W/p).read_bytes())==v and sha(git('show',BASE+':'+p))==v
for r in H['canonical_caches']:
    assert sha((W/r['cache']).read_bytes())==r['cache_sha256'] and sha((W/r['runner']).read_bytes())==r['source_sha256']
    for p,v in r['input_sha256'].items():assert sha((W/p).read_bytes())==v
git('add','--',*paths);integrated=tree(git('write-tree').decode().strip())
assert {p for p in base if integrated[p]!=base[p]}==tools_changed and set(integrated)-set(base)==(set(paths)|icepaths)-tools_changed
for p,r in ICE['source_paths'].items():assert sha((W/p).read_bytes())==r['final_sha256']
git('diff','--cached','--check');patch=git('diff','--cached','--binary',BASE);(E/'combined-science-source.patch').write_bytes(patch)
out={'base':BASE,'original_pr':8005,'original_head':I['raw_original_head'],'original_base':I['raw_original_base'],'active_head':I['raw_active_head'],'active_base':I['raw_active_base'],'full_original_delta':[{ 'path':p,'base':oldbase.get(p),'original':old.get(p),'active':active.get(p),'final':integrated.get(p),'disposition':'regenerated_manifest' if p==MANIFEST else paths[p]['author_disposition']} for p in sorted(delta)],'original_all_source_survives_head_move':True,'all_78_parent_only_movements_preserve_current_main':True,'final_source_paths':paths,'actual_module_closure':modules,'reviewed_parent_hashes':M['112_reviewed_parent_sources_sha256'],'existing_main_paths_preserved':len(base),'only_current_main_changes':sorted(tools_changed),'source_deletions':[],'staged_source_tree':git('write-tree').decode().strip(),'correction_patch_sha256':I['author_correction_patch_sha256'],'source_patch_sha256':sha(patch),'coordinator_read':'Complete author correction and finding dispositions; proof-critical charge/basis/control and actual subprocess/self-hash input context. Full original review remains with same reviewer. No cross-science import or physical identification between ice and Record; helper registry additions preserve all existing entries/functions. Final same-session confirmation required.'}
(E/'record-source-preparation.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'record_paths':len(paths),'ice_paths':len(icepaths),'actual_record_modules':len(modules),'main_paths_preserved':len(base),'combined_source_tree':out['staged_source_tree']}))
