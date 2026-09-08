from pathlib import Path
B=Path(__file__).parent;src=B.parent/'continuous-time-l2-production-post-review/review.py';t=src.read_text()
changes={"continuous-time-l2-calibration')":"continuous-time-l2-precision-followup')","555f59fa753ff6718361dbdd33520d1a1e952db77cf26d06960e840ee1f63ad4":"22ab56cb8ac792a01e857b66d69b21b25e083f626f7664a6a0c4b351ed670741","for b in [16,64]":"for b in [64]","range(4):":"range(16):","202609350000":"202609360000","len(rows)==128":"len(rows)==256","rows[j:j+8]":"rows[j:j+16]","range(0,128,8)":"range(0,256,16)","sum(mh)==3072":"sum(mh)==6144","burn+128":"burn+256","mean(x[:64]),mean(x[64:])":"mean(x[:128]),mean(x[128:])","[(1,3),(5,7),(0,1),(2,3),(4,5),(6,7)]":"[(0,1),(2,3)]","for i in [1,3,5,7]":"for i in [0,1,2,3]","final_paths_replayed=128":"final_paths_replayed=256,final_readouts_recomputed=3072"}
for a,b in changes.items():
 if a not in t:raise ValueError(a)
 t=t.replace(a,b)
# range(4) occurs in literal flip too: retain exactly four face edges.
t=t.replace('for k in range(16))','for k in range(4))')
needle="reported=json.loads((folder/'ANALYSIS.json').read_text());targets=target_table();arms=[];raw_hashes={}"
replace="""reported=json.loads((folder/'ANALYSIS.json').read_text());targets=target_table();arms=[];raw_hashes={}
 complete=json.loads((folder/'COMPLETE.json').read_text());ledger=json.loads((folder/'LEDGER.json').read_text());started=json.loads((folder/'STARTED.json').read_text());ar=json.loads((folder/'ANALYSIS.OUTER.json').read_text())
 need(complete['freeze']==FREEZE and complete['jobs']==64 and complete['analysis_sha']==sha(folder/'ANALYSIS.json'),'complete binding')
 need(180.930914<=complete['charged_seconds']<3600 and started['prior_cost_seconds']==180.930914 and started['jobs']==64 and started['chains']==256,'aggregate/prior')
 need(len(ledger['jobs'])==64 and len(list(folder.glob('a*_s*/RESULT.json')))==64 and len(reported['arms'])==4 and len(reported['contrasts'])==2,'full study shape')
 need(ar['returncode']==0 and 0<ar['seconds']<=180 and 0<ar['outer_rss_bytes']<=384*1048576 and ar['stdout_sha']==sha(folder/'ANALYSIS.stdout') and (folder/'ANALYSIS.stdout').read_bytes()==(folder/'ANALYSIS.json').read_bytes(),'analysis receipt')"""
if needle not in t:raise ValueError('needle')
t=t.replace(needle,replace)
t=t.replace("need(len(z['chains'])==4,'four chains')","need(len(z['chains'])==4,'four chains');need(rec==ledger['jobs'][arm*16+shard],'ledger receipt identity')")
(B/'review.py').write_text(t)
