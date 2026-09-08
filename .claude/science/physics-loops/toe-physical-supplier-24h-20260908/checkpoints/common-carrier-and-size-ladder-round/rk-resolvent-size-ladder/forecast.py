import json,math,pathlib
p=pathlib.Path(__file__).resolve().parent;rows=[]
for L,b in [(8,32),(8,128),(8,512),(16,32),(16,128),(16,2048)]:
 d=json.loads((p/f'PROFILE_L{L}.json').read_text());w=1+sum(1/(k*2*math.sin(math.pi/L)**2) for k in [.25,.5,1])+7
 # Include all measured hot cost, scale by expected elementary work, threefold cushion and10s setup.
 seconds=3*d['hot_seconds']*32*(64*w+b)/(8*w+8)+10
 rows.append(dict(L=L,burn=b,expected_sweeps_per_origin=w,forecast_per_shard=seconds,forecast_logical=4*seconds,within160=seconds<=160))
micros=sum(json.loads((p/f).read_text())['seconds' if f=='MICRO.json' else 'total_seconds'] for f in ['MICRO.json','PROFILE_L8.json','PROFILE_L16.json'])
out=dict(cells=rows,micros=micros,total=micros+sum(r['forecast_logical'] for r in rows));out['gate']=all(r['within160'] for r in rows) and out['total']<=2300
(p/'FORECAST_PRODUCTION.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
