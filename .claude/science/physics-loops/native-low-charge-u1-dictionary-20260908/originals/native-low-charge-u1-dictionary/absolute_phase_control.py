import pathlib,json
count=0;old_failures=0
for m in range(1,9):
 for subset in range(1<<m):
  I=[i for i in range(m) if subset>>i&1];b=(1<<m)-1;sign=1
  for i in reversed(I):sign*=(-1)**((b&((1<<i)-1)).bit_count());b^=1<<i
  if b!=((1<<m)-1)^subset or sign!=(-1)**sum(I):raise RuntimeError('absolute basis identity')
  old_failures+=sign!=(-1)**(sum(I)-len(I)*(len(I)-1)//2);count+=1
if not old_failures:raise RuntimeError('old phase mutant survived')
out={'absolute_basis_columns':count,'old_identity_failures':old_failures,'correct_s0':'(-1)^sumI','tested_map_optional_block_phase':'(-1)^[D(D-1)/2]','PASS':True}
pathlib.Path(__file__).with_name('ABSOLUTE_PHASE_RESULT.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
