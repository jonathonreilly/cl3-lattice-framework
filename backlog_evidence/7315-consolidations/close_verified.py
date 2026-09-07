import datetime,hashlib,json,subprocess
from pathlib import Path
E=Path(__file__).resolve().parent;R=Path('/Users/jonreilly/Projects/Physics');repo='jonathonreilly/qubit-lattice-axiom-framework'
C=json.loads((E/'COORDINATOR_VERIFICATION.json').read_text());D=json.loads((E/'MAPS.json').read_text());target=D['target'];rows={r['number']:r for r in D['rows']}
assert len(C['rows'])==21
assert not(E/'closed-actions.json').exists(),'Do not repeat completed or partial mutations; inspect preserved incremental receipt.'
for name,key in [('MAPS.json','map_sha256'),('REPORT.md','review_report_sha256'),('dispositions.json','dispositions_sha256'),('SEMANTIC_CHECKS.json','semantic_checks_sha256')]:
    assert hashlib.sha256((E/name).read_bytes()).hexdigest()==C[key]
def call(*a):return subprocess.check_output(a,cwd=R)
def live(n):return json.loads(call('gh','pr','view',str(n),'--repo',repo,'--json','number,state,isDraft,headRefOid,headRefName,baseRefOid'))
actions=[]
for c in C['rows']:
    r=rows[c['number']];assert r['number'] not in [6379,6858,6859]
    assert hashlib.sha256((E/r['source_tree_map']).read_bytes()).hexdigest()==r['source_tree_map_sha256']
    a,b=live(r['number']),live(7315)
    assert a['state']=='OPEN' and not a['isDraft'] and a['headRefOid']==r['head'] and a['headRefName']==r['original_branch'] and a['baseRefOid']==r['declared_base'],a
    assert b['state']=='OPEN' and not b['isDraft'] and b['headRefOid']==target['headRefOid'] and b['headRefName']==target['headRefName'],b
    refs=call('git','ls-remote','origin','refs/heads/'+r['original_branch'],'refs/heads/'+target['headRefName']).decode();mapping={x.split()[1]:x.split()[0] for x in refs.splitlines()}
    assert mapping['refs/heads/'+r['original_branch']]==r['head'] and mapping['refs/heads/'+target['headRefName']]==target['headRefOid']
    result=call('gh','pr','close',str(r['number']),'--repo',repo).decode()
    after,targetafter=live(r['number']),live(7315)
    assert after['state']=='CLOSED' and after['headRefOid']==r['head']
    assert targetafter['state']=='OPEN' and targetafter['headRefOid']==target['headRefOid']
    assert call('git','ls-remote','origin','refs/heads/'+r['original_branch']).decode().split()[0]==r['head']
    actions.append({'number':r['number'],'target_pr':7315,'before':a,'target_before':b,'after':after,'target_after':targetafter,'original_branch_preserved_at':r['head'],'closed_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'reason':'Complete original and inherited source retained in open successor, with four explicitly reviewed arithmetic/append-only versions. All85 authored source paths and inherited scientific, evidence, premise and review obligations transfer; no scientific PASS, main coverage or landing implied.','source_map_sha256':r['source_tree_map_sha256'],'response':result})
    (E/'closed-actions.json').write_text(json.dumps({'actions':actions,'scientific_review_granted':False,'source_landing':False,'branch_deletion':False},indent=2)+'\n')
    print('Closed',r['number'],'into open7315; branch preserved',flush=True)
