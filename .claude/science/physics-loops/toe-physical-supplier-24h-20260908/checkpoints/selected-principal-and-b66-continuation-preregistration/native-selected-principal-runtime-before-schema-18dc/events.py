import json
from fractions import Fraction
class Events:
 def __init__(self,path):self.file=open(path,'x');self.count=0
 def __call__(self,stage,data):
  if stage=='candidate_pivot':data={k:v for k,v in data.items()if k!='partial_L'}
  elif stage=='candidate_inverse_entry':data={'i':data['i'],'j':data['j'],'value':data['T'][data['i']][data['j']]}
  elif stage=='candidate_factor_row':data={'row':data['row'],'values':data['L'][data['row']]}
  self.file.write(json.dumps({'sequence':self.count,'stage':stage,'data':data},default=lambda x:str(x)if isinstance(x,Fraction)else None)+'\n');self.file.flush();self.count+=1
 def close(self):self.file.close()
