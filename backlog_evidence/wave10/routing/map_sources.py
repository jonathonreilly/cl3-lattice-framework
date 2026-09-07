from pathlib import Path
import subprocess,json,hashlib,datetime,ast,concurrent.futures,csv,io
E=Path(__file__).parent;R=Path('/Users/jonreilly/Projects/Physics');S=E.parent/'backlog-remaining-duplicate-screen';stage=json.load(open(S/'stage1_inventory_ancestry_deltas.json'));main='b0f7089ea5dd6e26e0d58a8a36a77d36c50a8e7a';ns=[6282,6285,6287,6377,6379,6858,6859];reserved={6379,6858,6859};h=lambda b:hashlib.sha256(b).hexdigest();g=lambda *a:subprocess.check_output(['git',*a],cwd=R)
shallow=Path(g('rev-parse','--git-path','shallow').decode().strip());shallow=shallow if shallow.is_absolute() else R/shallow;shabefore=h(shallow.read_bytes())
def live(n):
 data=subprocess.check_output(['gh','pr','view',str(n),'--repo','jonathonreilly/qubit-lattice-axiom-framework','--json','number,title,state,isDraft,headRefOid,baseRefOid,headRefName,baseRefName,changedFiles,url,updatedAt']);p=json.loads(data);(E/(str(n)+'-final-live.json')).write_bytes(data);old=stage['rows'][str(n)];assert p['headRefOid']==old['head'] and p['baseRefOid']==old['declared_base'] and p['state']=='OPEN' and not p['isDraft'];return n,p
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex: metadata=dict(ex.map(live,ns))
classifier=g('show',main+':scripts/science_fix_loop.py');assert classifier==(S/'frozen_current_main_generated_classifier_source.py').read_bytes();(E/'frozen_generated_classifier_source.py').write_bytes(classifier);t=ast.parse(classifier);wanted={'GENERATED_AUDIT_DATA_NAMES','GENERATED_AUDIT_DOCS','generated_audit_output'};nodes=[x for x in t.body if isinstance(x,ast.Assign) and any(isinstance(v,ast.Name) and v.id in wanted for v in x.targets) or isinstance(x,ast.FunctionDef) and x.name in wanted];scope={};exec(compile(ast.Module(body=nodes,type_ignores=[]),'<classification only>','exec'),scope)
def kind(p):
 if p=='docs/audit/data/citation_graph_manifest.json':return 'generated_topology_acknowledgment'
 return 'generated_audit_output' if scope['generated_audit_output'](p) else 'source'
objects=set();trees={}
def tree(ref):
 if ref in trees:return trees[ref]
 d={};raw=g('ls-tree','-rz',ref)
 for row in raw.split(b'\0'):
  if row:
   a,p=row.split(b'\t',1);mode,typ,blob=a.decode().split();d[p.decode()]={'mode':mode,'type':typ,'blob':blob};objects.add(blob)
 trees[ref]=d;return d
mt=tree(main);target=metadata[6377]['headRefOid'];tt=tree(target);delta={};refs=[]
for n,p in metadata.items():
 head=p['headRefOid'];base=p['baseRefOid'];assert g('cat-file','-t',head).strip()==b'commit';mb=g('merge-base','--all',base,head).decode().splitlines();assert mb==[base];commit=g('cat-file','commit',head);(E/(str(n)+'-commit.txt')).write_bytes(commit);parents=[x.split()[1] for x in commit.decode().splitlines() if x.startswith('parent ')];assert base in parents,(n,parents,base)
 a,b=tree(base),tree(head);paths=sorted(p for p in set(a)|set(b) if a.get(p)!=b.get(p));assert len(paths)==p['changedFiles'];assert set(paths)=={x['path'] for x in stage['rows'][str(n)]['original_delta']};rows=[]
 for path in paths:rows.append({'path':path,'kind':kind(path),'base':a.get(path),'head':b.get(path),'target':tt.get(path),'current_main':mt.get(path),'status':'A' if path not in a else 'D' if path not in b else 'M'})
 delta[str(n)]={'head':head,'declared_base':base,'actual_merge_base':base,'direct_parent_proven':True,'paths':rows};(E/(str(n)+'-original.patch')).write_bytes(g('diff','--binary','--no-renames',base,head))
 refrows=[]
 for ref in ['refs/heads/'+p['headRefName'],'refs/remotes/origin/'+p['headRefName']]:
  q=subprocess.run(['git','rev-parse','--verify',ref],cwd=R,capture_output=True,text=True);v=q.stdout.strip() if q.returncode==0 else None;assert v in [head,None];refrows.append({'ref':ref,'resolved':v,'available':q.returncode==0})
 refs.append({'number':n,'head':head,'remote_branch_live_head':head,'local_recovery_refs':refrows,'recover_commit_command':['git','show',head]})
(E/'ORIGINAL_DELTAS.json').write_text(json.dumps(delta,indent=2)+'\n');(E/'RECOVERY_REFS.json').write_text(json.dumps(refs,indent=2)+'\n')
reservedpaths={r['path'] for n in reserved for r in delta[str(n)]['paths'] if r['kind']=='source'};assert len(reservedpaths)==12;reservedblobs={r['head']['blob'] for n in reserved for r in delta[str(n)]['paths'] if r['kind']=='source' and r['head']};screen=[]
for n in [6282,6285,6287,6377]:
 t=tree(metadata[n]['headRefOid']);pathhits=sorted(set(t)&reservedpaths);blobhits=[p for p,v in t.items() if v['blob'] in reservedblobs];assert not pathhits and not blobhits;screen.append({'number':n,'reserved_path_intersections':pathhits,'reserved_new_blob_any_path_intersections':blobhits})
(E/'RESERVATION_SCREEN.json').write_text(json.dumps({'reserved_live_heads':{str(n):metadata[n]['headRefOid'] for n in sorted(reserved)},'all12reserved_authored_paths':sorted(reservedpaths),'screens':screen,'reserved_PRs_not_routing_targets':True,'no_reservation_waiver':True},indent=2)+'\n')
ledger='.claude/science/physics-loops/toe-axiom-closure-20260809/NO_GO_LEDGER.md';memo='docs/MINIMAL_AXIOMS_2026-06-29.md';manifest='docs/audit/data/citation_graph_manifest.json';summaries=[]
for n in [6282,6285,6287]:
 p=metadata[n];head=p['headRefOid'];bt=tree(p['baseRefOid']);ot=tree(head);author={x['path'] for x in delta[str(n)]['paths']};mismatch=[];added=[];deleted=[];rows=[];counts={}
 assert subprocess.run(['git','merge-base','--is-ancestor',head,target],cwd=R).returncode==0
 for path in sorted(set(bt)|set(ot)|set(tt)):
  b,o,t=bt.get(path),ot.get(path),tt.get(path);typ=kind(path)
  if o==t:dis='exact_original_mode_type_blob' if o else 'original_deletion_preserved'
  elif not o:dis='target_addition' if t else 'absent_both';added.append(path) if t else None
  elif not t:dis='original_source_deleted';deleted.append(path)
  elif path==ledger:
   old=g('cat-file','blob',o['blob']);new=g('cat-file','blob',t['blob']);assert new.startswith(old) and len(new)>len(old) and o['mode']==t['mode'];dis='strict_byte_prefix_preserved_with_unreviewed_append';(E/(str(n)+'-ledger-append.diff')).write_bytes(g('diff',head,target,'--',path));mismatch.append({'path':path,'kind':typ,'original':o,'target':t,'old_bytes':len(old),'target_bytes':len(new),'strict_byte_prefix':True,'append_sha256':h(new[len(old):]),'disposition':dis})
  elif path==memo:
   assert n in [6282,6285] and t==mt[path];dis='owner_approved_current_main_premise_epoch_reconciliation_with_old_blob_recovery';mismatch.append({'path':path,'kind':typ,'original':o,'target':t,'current_main':mt[path],'disposition':dis});(E/(str(n)+'-axiom-epoch.diff')).write_bytes(g('diff',head,target,'--',path))
  elif path==manifest:dis='generated_topology_different_no_scientific_status_transfer';mismatch.append({'path':path,'kind':typ,'original':o,'target':t,'disposition':dis})
  else:raise AssertionError((n,path,o,t))
  origin='original_authored_delta' if path in author else 'original_inherited' if o else 'target_addition_or_preserved_base_deletion';counts[dis]=counts.get(dis,0)+1
  row={'path':path,'kind':typ,'origin':origin,'disposition':dis}
  for prefix,entry in [('base',b),('original',o),('target',t),('main',mt.get(path))]:
   for k in ['mode','type','blob']:row[prefix+'_'+k]=entry.get(k,'') if entry else ''
  rows.append(row)
 assert not deleted;out=io.StringIO();w=csv.DictWriter(out,fieldnames=list(rows[0]),delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows);f=str(n)+'-complete-source-map.tsv';(E/f).write_text(out.getvalue());sourcecount=sum(kind(p)=='source' for p in ot);targetaddedsource=[p for p in added if kind(p)=='source'];summaries.append({'original':n,'target':6377,'original_head':head,'target_head':target,'base':p['baseRefOid'],'visible_ancestry_positive':True,'all_raw_original_path_count':len(ot),'all_original_source_count':sourcecount,'map_rows':len(rows),'disposition_counts':counts,'source_mismatches':[m for m in mismatch if m['kind']=='source'],'all_nonexact_original_paths':mismatch,'source_deletions':[],'authored_deletions':[x['path'] for x in delta[str(n)]['paths'] if x['status']=='D' and x['kind']=='source'],'target_added_source_count':len(targetaddedsource),'target_added_source_paths':targetaddedsource,'map_file':f,'map_sha256':h((E/f).read_bytes())})
# Preserve complete exact old/current memo and all relevant historical ledger snapshots outside the repository.
recovery=E/'recovery';recovery.mkdir(exist_ok=True);recovered=[]
for n in [6282,6285,6287,6377]:
 for p in [memo,ledger]:
  o=tree(metadata[n]['headRefOid'])[p];data=g('cat-file','blob',o['blob']);dest=recovery/(str(n)+'-'+Path(p).name);dest.write_bytes(data);recovered.append({'source_pr':n,'source_commit':metadata[n]['headRefOid'],'path':p,'mode':o['mode'],'blob':o['blob'],'sha256':h(data),'external_file':str(dest),'git_recovery_spec':metadata[n]['headRefOid']+':'+p})
assert tree(target)[memo]==mt[memo];(E/'RECOVERED_HISTORICAL_BLOBS.json').write_text(json.dumps(recovered,indent=2)+'\n')
# Every leaf object referenced by all original/base/target/main maps is locally available.
obj=sorted(objects);r=subprocess.run(['git','cat-file','--batch-check=%(objectname) %(objecttype) %(objectsize)'],cwd=R,input=('\n'.join(obj)+'\n').encode(),capture_output=True,check=True);lines=r.stdout.decode().splitlines();assert len(lines)==len(obj) and all(' missing' not in x for x in lines);(E/'AVAILABLE_OBJECTS.tsv').write_text(r.stdout.decode().replace(' ','\t'))
assert h(shallow.read_bytes())==shabefore
out={'captured_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'current_main':main,'target':6377,'target_head':target,'target_raw_paths':len(tt),'target_source_paths':sum(kind(p)=='source' for p in tt),'complete_original_delta_maps':'ORIGINAL_DELTAS.json','classifier_sha256':h(classifier),'generated_paths_never_omitted_from_raw_maps':True,'shallow_repository':True,'shallow_boundary_sha256_unchanged':shabefore,'ancestry_claim':'positive visible ancestry and actual direct parents only; no negative shallow inference','network_fetches':0,'github_mutations':0,'objects_verified_available':len(lines),'rows':summaries,'scientific_verdict':'NOT_REVIEWED','routing_assessment':'pending full nonexact-content disposition narrative'};(E/'MAP_SUMMARY.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='rows'},indent=2));print(json.dumps([{k:v for k,v in x.items() if k not in ['target_added_source_paths','source_mismatches','all_nonexact_original_paths']} for x in summaries],indent=2))
