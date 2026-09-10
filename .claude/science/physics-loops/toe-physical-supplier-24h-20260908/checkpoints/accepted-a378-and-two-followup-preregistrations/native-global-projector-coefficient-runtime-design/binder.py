"""Inert accepted-A378 binder. No oracle, geometry, or producer imports."""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib,re,math

def need(x,m):
    if not x: raise ValueError(m)

def sha(p):
    h=hashlib.sha256()
    with Path(p).open('rb') as f:
        for block in iter(lambda:f.read(1048576),b''):h.update(block)
    return h.hexdigest()

def read(p):
    return json.loads(Path(p).read_text())

def scalar(x,bits=32768):
    need(type(x) is str and len(x)<=(40000 if bits==50000 else 20000) and re.fullmatch(r'-?(?:0|[1-9][0-9]*)(?:/[1-9][0-9]*)?',x) is not None,'canonical rational syntax')
    v=F(x);need(str(v)==x,'canonical reduced rational')
    need(max(abs(v.numerator).bit_length(),v.denominator.bit_length())<=bits,'input bit cap')
    return v

def pair(x,bits=32768):
    need(type(x) is list and len(x)==2,'interval pair')
    a,b=(scalar(v,bits) for v in x);need(a<=b,'interval order');return a,b

def seconds(x,cap):
    need(type(x) in (int,float) and math.isfinite(x) and 0<x<=cap,'finite resource seconds')

def integer(x,value,label):
    need(type(x) is int and x==value,label)

def load(binding,retain):
    need(binding['status']=='BOUND_ACCEPTED_A378','acquisition binder NOT_READY')
    for p,h in binding['inputs'].items():need(sha(p)==h,'acquisition input pin '+p)
    out=Path(binding['output'])
    need(sorted(p.name for p in out.iterdir())==binding['output_membership'],'acquisition exact membership')
    root=read(binding['root_acceptance'])
    need(type(binding['root_acceptance_expected']) is dict and root==binding['root_acceptance_expected'],'exact reviewed ROOT_ACCEPTANCE')
    need(root['status']==binding['root_acceptance_status'],'root accepted status')
    need(binding['root_acceptance_status'].startswith('ACCEPTED'),'literal accepted family')
    need(root['all_A_width_gates'] is True,'root A targets')
    integer(root['points'],378,'root points')
    need(root['result_sha256']==sha(out/'RESULT.json') and root['nodes_sha256']==sha(out/'NODES.json'),'root result binding')
    need(root['worker_freeze']==binding['worker_freeze_sha256'] and root['root_freeze']==binding['root_freeze_sha256'],'root source binding')
    seconds(root['external_seconds'],180)
    need(type(root['external_rss_bytes']) is int and 0<root['external_rss_bytes']<=384*1048576,'external RSS')
    need(type(root['sampled_whole_tree_peak']) is int and 0<root['sampled_whole_tree_peak']<=384*1048576,'accepted tree RSS')
    receipt=read(binding['root_receipt']);need(receipt['pass'] is True and receipt['failure'] is None and type(receipt['returncode']) is int and receipt['returncode']==0,'producer root execution')
    seconds(receipt['seconds'],180)
    need(type(receipt['sampled_whole_tree_peak']) is int and 0<receipt['sampled_whole_tree_peak']<=384*1048576,'root tree memory')
    need(receipt['worker_freeze']==binding['worker_freeze_sha256'],'root worker binding')
    schema=read(binding['schema_acceptance'])
    need(root['schema_sha256']==sha(binding['schema_acceptance']),'root schema hash')
    need(schema['status']=='ACCEPTED_NEW_A378_SCHEMA' and schema['all_targets_met'] is True,'accepted geometry and A targets')
    integer(schema['count'],378,'schema count')
    need(schema['result_sha256']==sha(out/'RESULT.json') and schema['nodes_sha256']==sha(out/'NODES.json'),'schema final binding')
    complete=read(out/'WORKER_COMPLETE.json')
    need(complete['status']=='COMPLETE' and complete['freeze_sha256']==binding['worker_freeze_sha256'],'producer WORKER_COMPLETE')
    seconds(complete['seconds'],179)
    need(type(complete['rss_bytes']) is int and 0<complete['rss_bytes']<=384*1048576,'worker memory')
    need(complete['result_sha256']==sha(out/'RESULT.json') and complete['nodes_sha256']==sha(out/'NODES.json'),'worker output binding')
    result=read(out/'RESULT.json');nodes=read(out/'NODES.json')
    need(result['status']=='COMPLETE' and result['scope']=='A-only378scalar acquisition' and result['all_targets_met'] is True,'producer scientific status')
    integer(result['count'],378,'result count');integer(nodes['count'],378,'nodes count')
    need(len(result['rows'])==len(nodes['rows'])==378,'all378 rows')
    seconds(result['seconds'],179);need(result['seconds']<=complete['seconds']<=receipt['seconds'],'nested producer times')
    partial=read(out/'PARTIAL.json')
    need(partial=={'current':{'stage':'retained','id':377},'completed':378,'target_met':True},'producer final partial')
    rows=[];last=F(0);panels={};rule={}
    for i,n in enumerate(nodes['rows']):
        retain('input_row_before_check',{'id':i,'node':n})
        integer(n['id'],i,'node id');j,k=divmod(i,21);j-=16
        integer(n['panel'],j,'panel');integer(n['root'],k,'root index')
        sl,sh=pair(n['s_interval']);wl,wh=pair(n['weight_interval'],50000);a=F(4)**j
        need(a<sl<=sh<4*a and sl>last and wl>0,'mapped ordered geometry');last=sh
        need(sh-sl<=F(1,2**160) and wh-wl<=F(1,2**160),'geometry widths')
        need(scalar(n['s'])==(sl+sh)/2 and scalar(n['weight'],50000)==(wl+wh)/2,'exact geometry midpoints')
        x=(2*sl/(3*a)-F(5,3),2*sh/(3*a)-F(5,3));w=(2*wl/(3*a),2*wh/(3*a))
        if k in rule:need(rule[k]==(x,w),'same mapped rule')
        else:rule[k]=(x,w)
        # Avoid an exact sum of heterogeneous geometry denominators.
        grid=2**192
        dlo=F((wl.numerator*grid)//wl.denominator,grid)
        dhi=F(-((-wh.numerator*grid)//wh.denominator),grid)
        panels.setdefault(j,[F(0),F(0)]);panels[j][0]+=dlo;panels[j][1]+=dhi
        rawpath=out/f'RAW_{i:03d}.json';need(schema['raw_sha256'][rawpath.name]==sha(rawpath),'accepted raw hash')
        raw=read(rawpath);integer(raw['id'],i,'raw id');seconds(raw['seconds'],179)
        r=raw['raw'];integer(r['terms'],160,'oracle terms');need(scalar(r['s'])==scalar(n['s']),'A midpoint argument')
        al,ah=pair(r['A']);need(0<al<=ah and ah-al<=F(1,10**30),'certified A width')
        need(result['rows'][i]==dict(raw,target_met=True),'raw result exact equality')
        rows.append(dict(id=i,root=(sl,sh),weight=(wl,wh),A=(al,ah)))
    for j,(lo,hi) in panels.items():need(lo<=3*F(4)**j<=hi,'panel weight sum')
    need(rule[10][0]==(F(0),F(0)),'central rule zero')
    for k in range(10):need(rule[k][0]==tuple(-v for v in reversed(rule[20-k][0])) and rule[k][1]==rule[20-k][1],'rule symmetry')
    retain('accepted_inputs_loaded',{'count':378,'acquisition_result_sha256':sha(out/'RESULT.json')})
    return rows
