import pathlib,json,argparse
if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('--out',required=True);args=a.parse_args();p=pathlib.Path(args.out);r=json.loads((p/'RESULT.json').read_text());d=json.loads((p/'DISPATCH.json').read_text())
 if d['exit'] or d['external_seconds']>=30 or r['rss_mib']>=384:raise ValueError('invalid profile')
 overhead=max(0.,d['external_seconds']-sum(x['initialization_seconds']+x['warmup_seconds']+x['measured_seconds']+x['checkpoint_seconds'] for x in r['cases']));rows=[]
 for c in r['cases']:
  rate=c['measured_seconds']/24576
  for tau in (12,36):
   n=3072*tau;total=64*n;cap=24*n;segments=[]
   for begin in range(0,total,cap):segments.append(1.5*(rate*min(cap,total-begin)+c['checkpoint_seconds']+overhead+(c['initialization_seconds'] if begin==0 else 0.)))
   rows.append(dict(V=c['V'],tau=tau,seconds_per_chain=sum(segments),segment_seconds=segments,chains=16))
 total=sum(x['seconds_per_chain']*16 for x in rows);maximum=max(max(x['segment_seconds']) for x in rows);result=dict(rows=rows,forecast_seconds=total,max_segment_seconds=maximum,gate=maximum<=160 and total<=11520,scope='empirical padded forecast, not rigorous runtime or efficiency bound');(p/'FORECAST.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
