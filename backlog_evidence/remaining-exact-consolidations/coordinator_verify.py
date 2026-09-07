import csv,datetime,gzip,hashlib,io,json,subprocess,sys
from pathlib import Path
E=Path(__file__).resolve().parent;R=Path('/Users/jonreilly/Projects/Physics');sys.path.insert(0,str(R/'scripts'))
from science_fix_loop import generated_audit_output
D=json.loads((E/'candidate_screen.json').read_text());S=json.loads((E/'stage1_inventory_ancestry_deltas.json').read_text())
def sha(b):return hashlib.sha256(b).hexdigest()
def git(*a):return subprocess.check_output(['git',*a],cwd=R)
def source(p):return not generated_audit_output(p) and p!='docs/audit/data/citation_graph_manifest.json'
cache={}
def tree(ref):
    if ref not in cache:
        out={}
        for row in git('ls-tree','-r','-z',ref).split(b'\0'):
            if row:
                m,p=row.split(b'\t',1);out[p.decode()]=tuple(m.decode().split())
        cache[ref]=out
    return cache[ref]
assert sha((R/'scripts/science_fix_loop.py').read_bytes())==sha((E/'frozen_current_main_generated_classifier_source.py').read_bytes())
assert sha((E/'candidate_screen.json').read_bytes())=='aa0673fb4e69d4fe297a0c19cb03e5b2a61441c6a44f734eda2f956e443554d1'
reserved=set()
for n in (6379,6858,6859):
    r=S['rows'][str(n)];a,b=tree(r['merge_base']),tree(r['head'])
    reserved|={p for p in a.keys()|b.keys() if source(p) and a.get(p)!=b.get(p)}
rows=[];objects=set();authored=set();records=0
for r in D['selected']:
    assert r['original'] not in (6379,6858,6859) and r['successor'] not in (6379,6858,6859)
    head,base,target=r['original_head'],r['original_merge_base'],r['successor_head']
    assert git('merge-base','--all',head,r['original_declared_base']).decode().split()==[base]
    assert git('merge-base','--all',target,r['target_declared_base']).decode().split()==[r['target_merge_base']]
    git('merge-base','--is-ancestor',head,target)
    old,original,final=tree(base),tree(head),tree(target)
    assert not(reserved&set(final))
    delta={p for p in old.keys()|original.keys() if old.get(p)!=original.get(p)}
    declared={x['path']:x for x in r['original_delta']};assert set(declared)==delta and len(delta)==r['original_delta_count']
    for p,x in declared.items():
        for prefix,mapping in [('base',old),('head',original)]:
            assert x[prefix+'_mode']==(mapping[p][0] if p in mapping else '000000')
            assert x[prefix+'_blob']==(mapping[p][2] if p in mapping else None)
        if source(p):
            assert original.get(p)==final.get(p)
            assert p in original and p not in old
            authored.add(p);records+=1
    original_source={p:v for p,v in original.items() if source(p)}
    assert all(final.get(p)==v for p,v in original_source.items())
    compressed=(E/r['full_source_map']).read_bytes();data=gzip.decompress(compressed)
    assert sha(compressed)==r['full_source_map_gzip_sha256'] and sha(data)==r['full_source_map_sha256']
    reader=csv.reader(io.StringIO(data.decode()),delimiter='\t');header=next(reader)
    assert header==['path','original_mode','original_type','original_blob','target_mode','target_type','target_blob','kind']
    mapped={}
    for line in reader:
        p,*values=line;assert p not in mapped;mapped[p]=values
        assert tuple(values[:3])==original_source[p] and tuple(values[3:6])==final[p]
        assert values[6]==('controlled_data' if p.startswith('docs/audit/data/') else 'authored_or_inherited_source')
    assert set(mapped)==set(original_source) and len(mapped)==r['complete_original_source_count']
    objects|={v[2] for v in original.values()}|{v[2] for v in final.values()}|{head,base,target,r['target_merge_base']}
    rows.append({'number':r['original'],'target':r['successor'],'head':head,'branch':r['original_branch'],'declared_base':r['original_declared_base'],'base':base,'target_head':target,'target_branch':r['target_ref'].removeprefix('refs/heads/'),'source_tree_entries':len(mapped),'complete_delta_paths':len(delta),'authored_source_paths':sum(source(p) for p in delta),'source_map_sha256':sha(compressed),'all_mode_type_blob_rows_independently_verified':True,'source_deletions':0})
proc=subprocess.run(['git','cat-file','--batch-check=%(objectname) %(objecttype) %(objectsize)'],cwd=R,input=''.join(x+'\n' for x in sorted(objects)).encode(),capture_output=True,check=True)
assert not any(x.endswith(' missing') for x in proc.stdout.decode().splitlines())
assert len(rows)==7 and records==40 and len(authored)==40
receipt={'verified_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'current_main':git('rev-parse','HEAD').decode().strip(),'review_report_sha256':sha((E/'REPORT.md').read_bytes()),'candidate_screen_sha256':sha((E/'candidate_screen.json').read_bytes()),'rows':rows,'authored_source_records':records,'unique_authored_source_paths':len(authored),'source_deletions':0,'reserved_source_intersections':0,'available_objects':len(objects),'all_source_map_rows':sum(r['source_tree_entries'] for r in rows),'coordinator_read':'Read complete routing report and classifier/screen. Independently recomputed each complete original delta, full inherited/source tree, actual ancestry and reservation intersection, and verified every map row plus local object availability. All identical scientific, evidence, premise and review obligations transfer to the named open successors. No scientific PASS, main coverage or branch deletion.'}
(E/'COORDINATOR_VERIFICATION.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({k:v for k,v in receipt.items() if k not in ['rows','coordinator_read']}))
