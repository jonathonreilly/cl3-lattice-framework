from pathlib import Path
P=Path('/private/tmp/toe-24h-probes-20260908/native-degree20-ward-root-review')
s=(P/'schema.py').read_text().replace('DEGREE10','DEGREE20').replace('<=205','<=255')
s=s.replace("bind=json.loads", "omega5=box(ev[1]['data']['omega5']);req(0<omega5[0]<=omega5[1]<168,'omega5 range')\n bind=json.loads")
s=s.replace("idx=2;statuses=[]", "req(omega5==box(json.loads(Path(bind['omega5']['result']).read_text())['interval']),'omega5 source copy')\n idx=2;statuses=[]")
s=s.replace("stages=['moments','polynomial','source_moments','residual_raw']*2+['ordered_word']*90+['gate_inputs']", "local_stages=['vacuum_inputs']+['vacuum_moment_raw']*7+['first_polynomial','source_inputs']+['source_moment_raw']*3+['residual_raw']\n stages=local_stages*2; seen=set()\n for C,A in pairs:\n  kc='O' if C[0]//2==C[1]//2 else 'P';ka='O' if A[0]//2==A[1]//2 else 'P';ell=sum((2*k in C and 2*k+1 in A)or(2*k+1 in C and 2*k in A)for k in range(3));tag=kc+ka+(str(ell)if kc==ka=='P'else'')\n  if tag not in seen:stages.append('cross_wick_raw');seen.add(tag)\n  stages.append('ordered_word')\n stages.append('gate_inputs')")
a=s.index("  req(len(body)==99")
b=s.index("  E=sqrt",a)
s=s[:a]+'''  req(len(body)==124 and status in('INDETERMINATE_SIGN','POSITIVE_CERTIFICATE','NEGATIVE_CERTIFICATE'),'completed choice grammar')
  cls={}
  for off,k in((0,'P'),(14,'O')):
   for e in body[off:off+14]:req(e['data']['kind']==k,'class event')
   for j,e in enumerate(body[off+1:off+8]):req(type(e['data']['index'])is int and e['data']['index']==j,'vacuum moment index');box(e['data']['real']);box(e['data']['imaginary'])
   for j,e in enumerate(body[off+10:off+13]):req(type(e['data']['index'])is int and e['data']['index']==j,'source moment index');box(e['data']['real']);box(e['data']['imaginary'])
   poly=body[off+8]['data'];raw=body[off+13]['data'];pp=poly['coefficients'];req(type(pp)is list and len(pp)==3,'quadratic coefficients');pv=[rat(x)for x in pp]
   for v in pv: req(abs(v)<=2**32 and (v*2**128).denominator==1,'fixed polynomial grid')
   req(len(poly['certified_pivots'])==3 and all(box(x)[0]>0 for x in poly['certified_pivots']),'positive pivot copies')
   rr=box(raw['r2']);tt=box(raw['t2']);req(rr[1]>=0 and tt[1]>=0,'norm upper');q=rat(raw['q']);req(abs(q)<=2**32 and (q*2**128).denominator==1,'constant grid')
   ct=raw['counts'];req(type(ct['wick_states'])is int and 0<=ct['wick_states']<=4096 and type(ct['complex_products'])is int and 0<=ct['complex_products']<=200000,'Wick counters')
   cls[k]={'p':pv,'q':q,'r2':(max(F(0),rr[0]),rr[1]),'t2':(max(F(0),tt[0]),tt[1]),'counts':ct}
  nominal=pt(0);orbits={};cached={};position=28
  for j,(C,A)in enumerate(pairs):
   kc='O'if C[0]//2==C[1]//2 else'P';ka='O'if A[0]//2==A[1]//2 else'P';ell=sum((2*k in C and 2*k+1 in A)or(2*k+1 in C and 2*k in A)for k in range(3));tag=kc+ka+(str(ell)if kc==ka=='P'else'')
   if tag not in cached:
    d=body[position]['data'];position+=1
    req(d['classes']==[kc,ka] and type(d['ell'])is int and d['ell']==ell,'cross class')
    # Wick base/correction arithmetic is explicitly inherited. Reconcile the stated real-part assembly independently.
    req(len(d['base'])==len(d['correction'])==2,'complex pair');base=box(d['base'][0]);box(d['base'][1]);corr=box(d['correction'][0]);box(d['correction'][1]);val=add(base,scale(corr,cls[ka]['q']));req(box(d['value'])==val,'cross real assembly');cached[tag]=val
   d=body[position]['data'];position+=1;val=cached[tag]
   req(type(d['index'])is int and d['index']==j+1 and d['C']==list(C)and d['A']==list(A)and all(type(z)is int for z in d['C']+d['A']),'ordered pair census')
   req(type(d['ell'])is int and d['ell']==ell and d['orbit']==tag,'ordered geometry')
   nominal=add(nominal,val);req(box(d['value'])==val and box(d['cumulative'])==nominal,'word accumulation')
   old=orbits.setdefault(tag,{'count':0,'sum':pt(0)});old['count']+=1;old['sum']=add(old['sum'],val)
  req(position==123 and len(cached)==5,'cross schedule')
  gate=body[-1]['data'];req(box(gate['nominal'])==box(row['nominal'])==nominal,'nominal final')
  for k in('P','O'):
   req([rat(v)for v in gate['rows'][k]['p']]==cls[k]['p'] and rat(gate['rows'][k]['q'])==cls[k]['q'] and gate['rows'][k]['counts']==cls[k]['counts'],'candidate copies')
   for name in('r2','t2'):req(box(gate['rows'][k][name])==cls[k][name],'residual copies')
  req(type(row['cross_wick_classes'])is int and row['cross_wick_classes']==5,'five Wick classes')
''' +s[b:]
s=s.replace("'independent_word_and_error_reconciliation':True", "'independent_word_accumulation_and_error_reconciliation':True,'native_wick_and_word_arithmetic_inherited':True")
(P/'schema.py').write_text(s)
s=(P/'run_once.py').read_text().replace('native-low-degree-ward-runtime-design','native-degree20-ward-gate-design').replace('degree10','degree20')
(P/'run_once.py').write_text(s)
compile((P/'schema.py').read_text(),str(P/'schema.py'),'exec')
