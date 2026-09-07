"""Addendum only: initial-cutoff #8002 head to reviewed closure head."""
from pathlib import Path
import hashlib,json,subprocess
E=Path(__file__).resolve().parent;SEVEN=E.parent;ROOT=E.parents[2]
R='/Users/jonreilly/Projects/Physics';OLD='be102438f655dd18019634fa46ab7aba8b1a14d9';NEW='726bafb889a85efadc62dbd81d51efb66c2cdf90';BASE='d61adbe4cb0bcb245235b6525b6ff577cafb6bb1';LAND='a8f84aaad75fdcb790ba6ba094e4275e237d9a5a';MAIN='7887b4481feae2800c04c7c42ddac9554f2c2b9f'
def git(*args):return subprocess.check_output(['git','-C',R,*args])
def sha(b):return hashlib.sha256(b).hexdigest()
def save(p,v):(E/p).write_text(json.dumps(v,indent=2)+'\n')
def tree(r):
 d={}
 for row in git('ls-tree','-rz',r).split(b'\0'):
  if row:
   a,p=row.split(b'\t',1);mode,typ,blob=a.decode().split();d[p.decode()]={'mode':mode,'type':typ,'blob':blob}
 return d
T={h:tree(h) for h in [BASE,OLD,NEW,LAND,MAIN]};cache={}
def content(h,p):
 v=T[h].get(p)
 if v is None:return None
 b=v['blob']
 if b not in cache:cache[b]=git('cat-file','blob',b)
 return cache[b]
def ident(h,p):
 v=T[h].get(p)
 return None if v is None else {**v,'sha256':sha(content(h,p))}
snapshot=json.loads((ROOT/'open-pr-details.json').read_text());initial=next(r for r in snapshot['pull_requests'] if r['number']==8002)
assert initial['headRefOid']==OLD
parents=git('show','-s','--format=%P',NEW).decode().split();assert parents==[OLD]
assert git('merge-base',BASE,OLD).decode().strip()==BASE
assert git('merge-base',OLD,NEW).decode().strip()==OLD
transition=[p for p in sorted(set(T[OLD])|set(T[NEW])) if T[OLD].get(p)!=T[NEW].get(p)]
expected={'.claude/science/physics-loops/admissibility-induced-law-20260906/'+f for f in ['HANDOFF.md','OPPORTUNITY_QUEUE.md','STATE.yaml','TRACE_GATE.md']}
assert set(transition)==expected
old_delta=[p for p in sorted(set(T[BASE])|set(T[OLD])) if T[BASE].get(p)!=T[OLD].get(p)]
new_delta=[p for p in sorted(set(T[BASE])|set(T[NEW])) if T[BASE].get(p)!=T[NEW].get(p)]
assert len(old_delta)==12 and len(new_delta)==16 and set(new_delta)-set(old_delta)==expected
assert all(T[OLD][p]==T[NEW][p] for p in old_delta)
full=json.loads((SEVEN/'PER_PR_LANDING_INVENTORY.json').read_text());review=next(r for r in full if r['pr']==8002);accepted={r['path']:r for r in review['paths']}
assert set(accepted)==set(new_delta)
paths=[]
for p in old_delta:
 a=accepted[p];assert ident(OLD,p)==a['original_head']
 paths.append({'path':p,'initial_status':'A' if p not in T[BASE] else 'M','initial_base':ident(BASE,p),'initial_cutoff_head':ident(OLD,p),'reviewed_head':ident(NEW,p),'initial_equals_reviewed':True,'accepted_landing':ident(LAND,p),'current_main':ident(MAIN,p),'existing_review_disposition':a['accepted_disposition'],'no_new_claim_review_needed':True})
save('INITIAL_AUTHORED_SCOPE.json',{'pr':8002,'initial_base':BASE,'initial_head':OLD,'reviewed_head':NEW,'all12_original_paths_in_accepted_map':True,'deleted_paths':[],'moved_paths':[],'paths':paths})
newrows=[]
for p in transition:
 a=content(OLD,p);b=content(NEW,p);assert b.startswith(a);assert T[OLD][p]['mode']==T[NEW][p]['mode']
 newrows.append({'path':p,'initial':ident(OLD,p),'reviewed':ident(NEW,p),'accepted_landing':ident(LAND,p),'current_main':ident(MAIN,p),'append_only':True,'added_lines':len(b.splitlines())-len(a.splitlines()),'existing_review_disposition':accepted[p]['accepted_disposition'],'claim_treatment':'historical source-PR/queue/trace declarations; added Gaussian, route-closure and landed wording was covered by original findings 7/8 and history correction, not accepted as unqualified physics'})
assert sum(r['added_lines'] for r in newrows)==36
save('TRANSITION_PATH_DISPOSITIONS.json',newrows)
(E/'initial-to-reviewed.diff').write_bytes(git('diff','--no-ext-diff',OLD,NEW))
branches=json.loads((SEVEN/'BRANCH_RECOVERY.json').read_text());assert branches['heads'][initial['headRefName']]==NEW
old_initial_total=sum(len(r['paths']) for r in full if r['pr']!=8002)+len(old_delta)
old_initial_unique=len({p['path'] for r in full if r['pr']!=8002 for p in r['paths']}|set(old_delta))
proofs=['backlog-admissibility-review/REVIEW.md','backlog-admissibility-review/CORRECTED_SOURCE_CONFIRMATION.md','backlog-admissibility-review/INTEGRATION_CONFIRMATION.md','backlog-admissibility-review/corrected_constituent_content_dispositions.json','backlog-wave2-validation/frozen-integration.json','backlog-wave2-validation/landed-actions.json']
evidence={p:sha((ROOT/p).read_bytes()) for p in proofs}
summary={'pr':8002,'initial_snapshot_captured_utc':snapshot['captured_utc'],'initial_snapshot_file':'open-pr-details.json','initial_snapshot_sha256':sha((ROOT/'open-pr-details.json').read_bytes()),'initial_head':OLD,'reviewed_and_closed_head':NEW,'base':BASE,'direct_parent_verified':True,'initial_tree':git('rev-parse',OLD+'^{tree}').decode().strip(),'reviewed_tree':git('rev-parse',NEW+'^{tree}').decode().strip(),'transition_paths':4,'transition_added_lines':36,'transition_deleted_lines':0,'all_other_tree_paths_mode_blob_identical':len(T[OLD])-4,'initial_authored_paths':12,'reviewed_authored_paths':16,'initial_source_covered':True,'transition_already_in_existing_review_scope':True,'initial_head_recoverable_as_direct_parent_of_preserved_remote_head':True,'remote_branch_evidence':'../BRANCH_RECOVERY.json','seven_reviewed_head_change_records':233,'seven_initial_head_change_records':old_initial_total,'seven_initial_unique_touched_paths':old_initial_unique,'count_effect':'No PR-count or science-coverage demotion from this transition. #8002 remains one completely disposed/landed original PR. Any joined 27/20 totals otherwise verified by coordinator are unchanged by this head mismatch; their other constituents are outside this addendum.','precise_head_join':'For #8002 record initial be102438 separately from reviewed/closed/remote 726bafb. Do not say all117 closure heads equal initial snapshot heads.','existing_acceptance_evidence':evidence,'new_proof_review_or_gates_or_actions':False}
save('TRANSITION_RECEIPT.json',summary)
report=f'''# #8002 initial-head transition addendum

**Resolved: the initial snapshot scope is fully accounted for.** The original frozen seven-landing report is unchanged; this addendum distinguishes the cutoff head from the later reviewed/closed head.

- Initial254 snapshot at `{snapshot['captured_utc']}`: **`{OLD}`**.
- Reviewed and closed head: **`{NEW}`**.
- Actual original delta base: `{BASE}`.
- Accepted landing: `{LAND}`; checked current main: `{MAIN}`.

Actual Git proves that the reviewed head is the **direct child** of the initial head. The single intervening commit adds **36 lines to four existing campaign files**: HANDOFF.md, OPPORTUNITY_QUEUE.md, STATE.yaml and TRACE_GATE.md. All four changes are append-only with unchanged modes. There are no deletions, renames, mathematical note changes, runner changes, cache changes or manifest changes. Every other tree path retains its exact mode/blob.

The initial authored delta has **12 paths**, all byte/mode-identical at the later reviewed head. Each of those twelve paths is already in the accepted sixteen-path #8002 disposition map. Thus its mathematical statement, runner, original cache, gravity probe and original history/control payload were included in the source review, with the same accepted corrections and qualifications previously recorded. The note’s original reversed-suprema/boundary scope and unsupported Gaussian/gravity transfer were corrected or withdrawn; this addendum does not reapprove the original wording.

The four added close-out surfaces also were **already included in the original full review**. In particular the review’s findings 7 and 8 explicitly cite the newly appended queue’s “Exactly computable block criteria are closed,” its Gaussian twin, and the matching state wording; the final confirmation narrows these and distinguishes source handoff from landing. They are not unreviewed extra physics smuggled into a cutoff identity. Their exact original/reviewed/accepted/current dispositions are in `TRANSITION_PATH_DISPOSITIONS.json`.

The preserved remote #8002 branch points to `{NEW}` according to the fresh branch check bound in the seven-landing report. Its direct parent `{OLD}` is therefore also recoverable. Existing original objects and the complete initial authored map are independently available locally; no branch mutation or fetch was necessary.

**Count consequence:** #8002 remains one original PR whose complete initial science scope was disposed and landed. This head mismatch does not change otherwise verified 27/20 PR or science-coverage totals; other constituents of those totals are outside this bounded addendum. The correct join is “116 exact snapshot-head matches plus one verified #8002 head transition,” not “all117 closure heads equal the cutoff snapshot.” At the source-record level, the frozen seven-landing inventory has 233 records at reviewed closure heads; using the initial #8002 head gives **229** records, still **167** distinct touched paths because those four campaign paths were already present in earlier constituents. Neither distinction changes the number of PRs.

`INITIAL_AUTHORED_SCOPE.json` binds all twelve original paths by base/initial/reviewed/accepted/current mode, blob and SHA256. `TRANSITION_PATH_DISPOSITIONS.json` binds all four additions and their existing review disposition. `initial-to-reviewed.diff` is the complete actual diff. `TRANSITION_RECEIPT.json` binds source identities, ancestry, recoverability and existing acceptance evidence. No new proof review, gate, formal claim audit, source/GitHub/planning change or action was performed.
'''
(E/'ADDENDUM.md').write_text(report)
save('ADDENDUM_HASHES.json',{p.name:sha(p.read_bytes()) for p in sorted(E.iterdir()) if p.is_file() and p.name!='ADDENDUM_HASHES.json'})
print(json.dumps({'ADDENDUM.md':sha((E/'ADDENDUM.md').read_bytes()),'TRANSITION_RECEIPT.json':sha((E/'TRANSITION_RECEIPT.json').read_bytes()),'initial_records':old_initial_total,'initial_unique_paths':old_initial_unique},indent=2))
