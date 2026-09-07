import datetime,hashlib,json,subprocess
from pathlib import Path
E=Path(__file__).resolve().parent;R=Path('/Users/jonreilly/Projects/Physics');repo='jonathonreilly/qubit-lattice-axiom-framework'
C=json.loads((E/'COORDINATOR_VERIFICATION.json').read_text())
assert len(C['rows'])==7 and not(E/'closed-actions.json').exists(),'Inspect any previous partial or complete actions; do not repeat.'
assert hashlib.sha256((E/'candidate_screen.json').read_bytes()).hexdigest()==C['candidate_screen_sha256']
assert hashlib.sha256((E/'REPORT.md').read_bytes()).hexdigest()==C['review_report_sha256']
def call(*a):return subprocess.check_output(a,cwd=R)
def live(n):return json.loads(call('gh','pr','view',str(n),'--repo',repo,'--json','number,state,isDraft,headRefOid,headRefName,baseRefOid'))
actions=[]
for r in C['rows']:
    assert r['number'] not in (6379,6858,6859) and r['target'] not in (6379,6858,6859)
    a,b=live(r['number']),live(r['target'])
    assert a['state']=='OPEN' and not a['isDraft'] and a['headRefOid']==r['head'] and a['headRefName']==r['branch'] and a['baseRefOid']==r['declared_base'],a
    assert b['state']=='OPEN' and not b['isDraft'] and b['headRefOid']==r['target_head'] and b['headRefName']==r['target_branch'],b
    refs=call('git','ls-remote','origin','refs/heads/'+r['branch'],'refs/heads/'+r['target_branch']).decode();mapping={x.split()[1]:x.split()[0] for x in refs.splitlines()}
    assert mapping['refs/heads/'+r['branch']]==r['head'] and mapping['refs/heads/'+r['target_branch']]==r['target_head']
    result=call('gh','pr','close',str(r['number']),'--repo',repo).decode()
    after,targetafter=live(r['number']),live(r['target'])
    assert after['state']=='CLOSED' and after['headRefOid']==r['head']
    assert targetafter['state']=='OPEN' and targetafter['headRefOid']==r['target_head']
    assert call('git','ls-remote','origin','refs/heads/'+r['branch']).decode().split()[0]==r['head']
    actions.append({'number':r['number'],'target_pr':r['target'],'before':a,'target_before':b,'after':after,'target_after':targetafter,'original_branch_preserved_at':r['head'],'closed_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'reason':'All original authored and inherited source paths, modes, types and blobs are preserved exactly in the open successor. Complete scientific, evidence, premise and review obligations transfer. No scientific PASS or main coverage is granted.','source_map_sha256':r['source_map_sha256'],'response':result})
    (E/'closed-actions.json').write_text(json.dumps({'actions':actions,'scientific_review_granted':False,'source_landing':False,'branch_deletion':False},indent=2)+'\n')
    print('Closed',r['number'],'into open',r['target'],'; branch preserved',flush=True)
