"""Copied original255-event grammar only; no original arithmetic."""
def schedule():
 from itertools import combinations
 labels=list(combinations(range(6),2));kind=lambda a:'O'if a[0]//2==a[1]//2 else'P'
 local=['vacuum_inputs']+['vacuum_moment_raw']*7+['first_polynomial','source_inputs']+['source_moment_raw']*3+['residual_raw']
 stages=local*2;seen=set()
 for C in labels:
  for A in labels:
   if set(C)&set(A):continue
   kc,ka=kind(C),kind(A);ell=sum((2*k in C and 2*k+1 in A)or(2*k+1 in C and 2*k in A)for k in range(3));tag='PP'+str(ell)if kc==ka=='P'else kc+ka
   if tag not in seen:stages.append('cross_wick_raw');seen.add(tag)
   stages.append('ordered_word')
 stages.append('gate_inputs');out=[('binding',None),('scalar_inputs',None)]
 for mode in ['residual','variational']:out += [('choice_start',mode)]+[(s,mode)for s in stages]+[('choice_complete',mode)]
 return out+[('complete',None)]
