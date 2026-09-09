"""Disabled until independent append post-acceptance is bound and reviewed."""
def load(plan):
 if plan.get('status')!='ACCEPTED_ENTRY_INPUTS_BOUND':raise ValueError('NOTREADY: append POST_ACCEPTANCE and complete actual radius binding required')
 raise RuntimeError('Final accepted-schema binder deliberately unimplemented; no native entry access')
