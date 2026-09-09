from pathlib import Path
import sys,json,hashlib,shutil,subprocess,os
E=Path(__file__).resolve().parent;R=Path('/Users/jonreilly/Projects/Physics');V=E/'api-view'
base=json.loads((E/'SOURCE_BINDING.json').read_text())['current_main']
sys.dont_write_bytecode=True
sys.path[:0]=[str(R/'scripts'),str(R/'docs/audit/scripts')]
import build_citation_graph as cg, audit_packet_script_deps as dp, runner_cache as rc, forensic_evidence_readiness as fe
inventory={}
def put(rel,data):
 p=V/rel;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(data);inventory[rel]=hashlib.sha256(data).hexdigest()
# A bounded actual-main overlay: complete primary static source closure plus
# every surviving explicit pinned input. Historical missing bodies stay missing.
paths=set(json.loads((E/'STATIC_RUNTIME_CLOSURE.json').read_text()))
paths.update(x['path'] for x in json.loads((E/'PIN_CLOSURE.json').read_text())['rows'])
for rel in sorted(paths):
 p=E/'originals'/rel
 if p.is_file():put(rel,p.read_bytes());continue
 run=subprocess.run(['git','show',base+':'+rel],cwd=R,capture_output=True)
 if run.returncode==0:put(rel,run.stdout)
for p in (E/'originals').rglob('*'):
 if p.is_file():put(p.relative_to(E/'originals').as_posix(),p.read_bytes())
cg.REPO_ROOT=V;dp.REPO_ROOT=V;dp.SCRIPTS_DIR=V/'scripts';rc.REPO_ROOT=V
note=next((V/'docs').glob('THIRD_PAIR*'));rel=note.relative_to(V).as_posix();body=note.read_text();cid=cg.claim_id_from_path(note);primary=cg.extract_runner(body,rel)
a=cg.helper_runner_paths_for_claim(cid,primary);b=dp.helper_runner_paths_for_claim(cid,Path(primary).stem)
assert a==b
checker='scripts/frontier_cycle930_third_pair_rc3_independent_check_2026_07_28.py'
r={'overlay_source_base':base,'note':rel,'id':cid,'primary':primary,'graph_helpers':a,'packet_helpers':b,'required_checker_omitted':checker not in a,'overlay_hashes':inventory,'runners':{},'tool_sha256':{str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest() for p in [Path(cg.__file__),Path(dp.__file__),Path(rc.__file__),Path(fe.__file__)]}}
for rel in [primary,checker]:
 r['runners'][rel]={'declared_inputs':rc.declared_input_paths(V/rel),'source_issue':fe._runner_source_issue(rel,V),'cache_status':rc.cache_status(rel)}
(E/'ACTUAL_CONSUMERS_COMPLETE_OVERLAY.json').write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps({k:v for k,v in r.items() if k not in ['overlay_hashes','tool_sha256','graph_helpers','packet_helpers']},indent=2));print('helpers',len(a),'required_checker_omitted',r['required_checker_omitted'])
