from pathlib import Path
import json,hashlib,shutil,datetime
W=Path('/private/tmp/toe-physical-supplier-24h-20260908');P=W/'.claude/science/physics-loops/toe-physical-supplier-24h-20260908';B=Path('/private/tmp/toe-24h-probes-20260908');D=P/'checkpoints/coarse-continuation-result-spectral-preregistration';D.mkdir();sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
prefixes=('native-degree10-spectral-residual','native-spectral-residual-root','native-spectral-residual-cold-review','native-spectral-parent-root-review','native-adaptive-spectral-root-cold-review','native-residual-spectral-inverse','native-residual-optimal-tau-stretch','native-optimal-tau-cold-review','native-positive-tau-parameter-review','native-coarse-witness-continuation','native-witness-packaging-inventory')
names=[s.name for s in B.iterdir()if s.is_dir()and s.name.startswith(prefixes)]
for n in sorted(set(names)):
 for f in sorted((B/n).rglob('*')):
  if not f.is_file()or'__pycache__'in f.parts:continue
  dest=D/f.relative_to(B);dest.parent.mkdir(parents=True,exist_ok=True);h=sha(f);shutil.copy2(f,dest);assert sha(dest)==h==sha(f)
for n in ['CHECKPOINT85_REMOTE_VERIFICATION.json','ACTIVATION86.json','POST84_ACCEPTANCE_PREPARATION_FAILURE.json','POST84_ACCEPTANCE_HELPER_INITIAL.py']:shutil.copy2(B/n,D/n)
acts=json.loads((P/'STATE.yaml').read_text());s.update(cycle=86,last_checkpoint_utc=now,last_progress_utc=now,next_action='Verify remote86 then execute NEW spectral residual estimator once30s384MiB. Witness composite completed but allten exclusionsfalse; do not rerun. Prepare coherent stronger-estimator PR and continue first-principles dual residual proof stretch.')
s['checkpoint86_preregistrations']=acts
v=json.loads((B/'native-coarse-witness-continuation-root-review/ROOT_ACCEPTANCE.json').read_text());s['coarse_witness_continuation_completed']={k:v[k]for k in ['result_sha256','external_seconds','external_rss_bytes','sampled_whole_tree_peak']};s['coarse_witness_continuation_completed'].update(root_acceptance_sha256=sha(B/'native-coarse-witness-continuation-root-review/ROOT_ACCEPTANCE.json'),cases=10,exclusions=0,inherited_cases=3,new_nodes=2436)
(P/'STATE.yaml').write_text(json.dumps(s,indent=2)+'\n')
report=f'''# Physics campaign SSH status

Updated {now}. The campaign continues until 2026-09-10 10:27:17 UTC subject to usable quota.44 science PRs delivered, latest8079 remotely verified. Main remains e95797cc.64 inactive worktrees removed;55GiB free. Quota83% consumed at02:44UTC; no reset redeemed. No coordination PR or main merge. Formal audit remains unrun.

The new composite coarse witness completed successfully once in113.57 seconds,87,408,640B external RSS and133,922,816B whole-tree peak. Result d69b839f; root acceptance af8f9d1e. It retains three original cases and76 events verbatim, resumes the original case3 panel, and adds2436 nodes. All15 output files and205 events passed root validation, including independent final high/mixed assembly and49-entry norm/radius arithmetic. The original299.83s protocol remains a preserved failure. Raw adapter contractions and native selected-frame/scalar truth remain inherited.

All ten coarse witness exclusions are FALSE. The certified local norm lower bounds range approximately9.79e-9 to1.20e-5, below the required0.022 threshold; all numerical radii are small. This is an inconclusive witness, not evidence that the true global state error is small, not a no-go, and not a fine-consumer certificate. The seven local rows and conservative omitted-tail/metric charges limit this route. Stateweighted control remains open.

The completed posterior estimates remain inconclusive: degree20 residual error6778.5093 around576.3565 and variational error7979.7212 around644.0920. Their saved results and accepted roots are already remote85. The error reduction is real but alpha still has no certified sign.

Checkpoint86 preregisters the NEW spectral inverse-residual estimator. Worker9d8a5730/root2ed13e39;30s external/29.5s root/29s worker,384MiB. It reuses existing vacuum and lower source moments, computes only eight missing s3/s4 source moments across the two classes and two choices, and tests five fixed positive tau values plus one bounded dyadic proposal per residual. Midpoints only propose a parameter; all certified bounds use original directed intervals, including the negative coefficient of the first moment. Proposal cap failure is retained and falls back to fixed1; a negative certified upper bound refuses arithmetic. No p/q coefficients or nominal values change. All9098 full input hashes and source-only readiness pass. Independent worker/root review covers the adaptive candidate and580–588 successful events. Exact remote86 verification is required before launch.

A first-principles dual-residual identity and sharp Kneser-spectrum remainder are under source-only derivation. They are prospective and have no native values. The stronger-estimator milestone is being packaged as one coherent support PR after the spectral outcome. Continue physics; alpha and physical model selection remain open.
'''
for n in ['STATUS.md','EIGHTY_SIXTH_RESULTS.md']:(P/n).write_text(report)
with(P/'HANDOFF.md').open('a')as fp:fp.write('\n'+report)
print({'files':len(m),'bytes':sum((D/n).stat().st_size for n in m),'scientific_inputs':len(required)})
