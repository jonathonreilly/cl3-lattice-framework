import sys,runpy,time,subprocess,os,signal,json,math
from pathlib import Path
C=runpy.run_path(str(Path(__file__).with_name('common.py')));globals().update({k:v for k,v in C.items() if not k.startswith('__')})
start=time.monotonic();ck(len(sys.argv)==2,'fresh output argument');out=Path(sys.argv[1]).resolve();ck(not out.exists() and P not in out.parents,'fresh external output');out.mkdir(parents=True);(out/'STARTED').write_text(str(start));receipts=[]
def kill(proc,known):
 try:os.killpg(proc.pid,signal.SIGKILL)
 except ProcessLookupError:pass
 for pid in known:
  try:os.kill(pid,signal.SIGKILL)
  except ProcessLookupError:pass
try:
 pin=verify();plan=read(P/'PLAN.json');forecast=read(P/'FORECAST.json');ck(forecast['aggregate_forecast_seconds']<1440 and forecast['shards']==52,'forecast gate')
 for mode in ('produce','replay'):
  for sid in range(52):
   # Reserve every still-future process forecast, finalization, and a complete hard cell.
   future=(51-sid)*forecast['production_seconds_per_shard']+52*forecast['independent_replay_seconds_per_shard'] if mode=='produce' else (51-sid)*forecast['independent_replay_seconds_per_shard']
   ck(time.monotonic()-start+180+future+60<1800,'shared reserve')
   tag=f'{mode}_{sid:02d}';t=time.monotonic();known=set();peak=0;proc=None;error=None
   with (out/(tag+'.stdout')).open('wb') as so,(out/(tag+'.stderr')).open('wb') as se:
    try:
     proc=subprocess.Popen(['/usr/bin/time','-lp',sys.executable,'-I','-B',str(P/'worker.py'),mode,str(sid),str(out)],stdout=so,stderr=se,start_new_session=True)
     while proc.poll() is None:
      ps=subprocess.run(['/bin/ps','-axo','pid=,ppid=,rss='],capture_output=True,text=True,timeout=.3,check=True);entries=[tuple(map(int,x.split())) for x in ps.stdout.splitlines()];family={proc.pid};changed=True
      while changed:
       old=len(family);family.update(pid for pid,ppid,rss in entries if ppid in family);changed=len(family)!=old
      known.update(family);rss=sum(rss*1024 for pid,ppid,rss in entries if pid in family);peak=max(peak,rss)
      ck(rss<=384*1048576 and time.monotonic()-t<179.5 and time.monotonic()-start<1800,'watchdog');time.sleep(.02)
     ck(proc.returncode==0,'nonzero process')
    except BaseException as e:error=repr(e);raise
    finally:
     if proc is not None:kill(proc,known);proc.wait()
     receipt=dict(mode=mode,shard=sid,seconds=time.monotonic()-t,peak_tree_bytes=peak,error=error,returncode=None if proc is None else proc.returncode);receipts.append(receipt);(out/'RECEIPTS.json').write_text(json.dumps(receipts,indent=2)+'\n')
   lines=(out/(tag+'.stderr')).read_text().splitlines();wall=[float(x.split()[1]) for x in lines if x.startswith('real ')];rss=[int(x.split()[0]) for x in lines if 'maximum resident set size' in x];ck(len(wall)==len(rss)==1 and math.isfinite(wall[0]) and 0<wall[0]<=180 and 0<rss[0]<=384*1048576,'external receipt')
   receipt.update(shell_seconds=wall[0],shell_rss=rss[0],output_sha=sha(out/(tag+'.json')));(out/'RECEIPTS.json').write_text(json.dumps(receipts,indent=2)+'\n')
 allrows=[]
 for sid in range(52):
  a=read(out/f'produce_{sid:02d}.json');b=read(out/f'replay_{sid:02d}.json');ck(a['freeze']==b['freeze']==pin and a['rows']==b['rows'],'final replay');rowscheck(a['rows'],plan['shards'][sid],plan);allrows.extend(a['rows'])
 ck(len(allrows)==4986 and len({r['case']['mask'] for r in allrows})==4986 and sum(len(r['case']['keys']) for r in allrows)==5110,'full coverage');ck(time.monotonic()-start<1800,'final shared cap')
 result=dict(status='COMPLETE',freeze=pin,masks=4986,keys=5110,positive=sum(r['positive'] for r in allrows),nonpositive=sum(not r['positive'] for r in allrows),minimum=str(min(Fraction(r['gap_lower']) for r in allrows)),seconds=time.monotonic()-start,receipts_sha=sha(out/'RECEIPTS.json'))
 (out/'COMPLETE.json').write_text(json.dumps(result,indent=2)+'\n')
except BaseException as e:
 (out/'FAILED.json').write_text(json.dumps(dict(error=repr(e),seconds=time.monotonic()-start,receipts=receipts),indent=2)+'\n');raise
