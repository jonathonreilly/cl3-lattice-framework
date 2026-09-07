import csv,datetime,gzip,hashlib,io,json,subprocess,sys
from pathlib import Path
E=Path(__file__).resolve().parent;R=Path('/Users/jonreilly/Projects/Physics');sys.path.insert(0,str(R/'scripts'))
from science_fix_loop import generated_audit_output
D=json.loads((E/'MAPS.json').read_text());S=json.loads((E/'SEMANTIC_CHECKS.json').read_text());T=D['target']['headRefOid']
allowed={(r['path'],r['old'],r['new']) for r in S['version_dispositions']}
assert len(allowed)==4
def sha(b):return hashlib.sha256(b).hexdigest()
def git(*a):return subprocess.check_output(['git',*a],cwd=R)
cache={}
def tree(ref):
    if ref in cache:return cache[ref]
    out={}
    for row in git('ls-tree','-r','-z',ref).split(b'\0'):
        if row:
            m,p=row.split(b'\t',1);mode,kind,blob=m.decode().split();out[p.decode()]=(mode,blob)
    cache[ref]=out;return out
def source(p):return not generated_audit_output(p) and p!='docs/audit/data/citation_graph_manifest.json'
target=tree(T);rows=[];authored=set();records=0
for r in D['rows']:
    head=r['head'];base=r['actual_merge_base'];assert git('merge-base','--all',head,r['declared_base']).decode().split()==[base]
    git('merge-base','--is-ancestor',head,T)
    old=tree(base);original=tree(head);delta={p for p in old.keys()|original.keys() if old.get(p)!=original.get(p)}
    declared={x['path']:x for x in r['complete_original_delta']};assert set(declared)==delta
    for p in delta:
        x=declared[p]
        assert x['base_mode_blob']==(list(old[p]) if p in old else None)
        assert x['original_mode_blob']==(list(original[p]) if p in original else None)
        assert x['target_mode_blob']==(list(target[p]) if p in target else None)
        assert (x['kind']=='source')==source(p)
        if source(p):
            assert p in original and p in target
            authored.add(p);records+=1
    original_source={p:v for p,v in original.items() if source(p)}
    differences={p for p,v in original_source.items() if target.get(p)!=v}
    assert differences==set(r['differing_sources'])
    for p in differences:
        assert target[p][0]==original[p][0] and (p,original[p][1],target[p][1]) in allowed
    mapdata=(E/r['source_tree_map']).read_bytes();assert sha(mapdata)==r['source_tree_map_sha256']
    reader=csv.reader(io.StringIO(gzip.decompress(mapdata).decode()),delimiter='\t');header=next(reader);mapped={}
    assert header==['path','original_mode','original_blob','target_mode','target_blob','exact']
    for line in reader:
        p,om,ob,tm,tb,exact=line;assert p not in mapped;mapped[p]=((om,ob),(tm,tb))
        assert exact==str((om,ob)==(tm,tb))
    assert set(mapped)==set(original_source) and len(mapped)==r['source_tree_entries']
    assert all(pair==(original_source[p],target[p]) for p,pair in mapped.items())
    rows.append({'number':r['number'],'head':head,'branch':r['original_branch'],'base':base,'target':7315,'target_head':T,'source_tree_entries':len(mapped),'complete_delta_paths':len(delta),'authored_source_paths':sum(source(p) for p in delta),'differing_source_paths':sorted(differences),'source_map_sha256':sha(mapdata),'all_mode_blob_rows_independently_verified':True})
assert len(rows)==21 and len(authored)==85 and records==86
receipt={'verified_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'current_main':git('rev-parse','HEAD').decode().strip(),'review_report_sha256':sha((E/'REPORT.md').read_bytes()),'dispositions_sha256':sha((E/'dispositions.json').read_bytes()),'map_sha256':sha((E/'MAPS.json').read_bytes()),'semantic_checks_sha256':sha((E/'SEMANTIC_CHECKS.json').read_bytes()),'rows':rows,'distinct_source_versions':S['version_dispositions'],'authored_source_records':records,'unique_authored_source_paths':len(authored),'source_deletions':0,'coordinator_read':'Complete routing report, all four source diffs and semantic limits read. Existing claim/assertion/gate/input strings are retained; exact rational substitutions and append-only history preserve the review obligation. This is consolidation into open7315, not scientific PASS, arbitrary-input equivalence or main coverage. All inherited source/premise scope transfers; no reserved action or raw landing.'}
(E/'COORDINATOR_VERIFICATION.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({'parents':len(rows),'unique_source_paths':len(authored),'source_change_records':records,'fully_verified_source_map_rows':sum(r['source_tree_entries'] for r in rows),'source_deletions':0,'source_versions_reconciled':len(allowed)}))
