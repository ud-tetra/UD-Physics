"""Prospective action-anchor arithmetic/provenance intake, never empirical scoring.

Receipt presence is metadata only. This program cannot establish a physical
same-carrier map, calibration independence, traceability or measurement coverage.
"""
from fractions import Fraction as F
from pathlib import Path
import argparse,json

RECEIPTS=['carrier_map_receipt','unit_preparation_receipt','action_pullback_receipt','clock_map_receipt']

def inspect(record):
    reasons=[];nodes={};state={};h_paths=[];tainted=[]
    for k in RECEIPTS:
        if not isinstance(record.get(k),str) or not record[k].strip():reasons.append('MISSING_'+k.upper())
    raw=record.get('calibration_nodes',[])
    if not isinstance(raw,list):return {'status':'BLOCKED','reasons':['INVALID_CALIBRATION_GRAPH'],'empirical_score':'UNSCORED'}
    for n in raw:
        if not isinstance(n,dict) or not isinstance(n.get('id'),str) or not n['id'] or n['id'] in nodes:
            reasons.append('INVALID_OR_DUPLICATE_NODE');continue
        nodes[n['id']]=n
    def visit(key):
        if key not in nodes:raise ValueError('UNKNOWN_CALIBRATION_PARENT:'+key)
        if state.get(key)==1:raise ValueError('CALIBRATION_CYCLE')
        if state.get(key)==2:return
        state[key]=1;n=nodes[key]
        if not isinstance(n.get('parents'),list) or not all(isinstance(p,str) for p in n['parents']):raise ValueError('INVALID_PARENTS')
        for p in n['parents']:visit(p)
        for flag in ['uses_candidate_relation','uses_hbar_in_anchor_formula']:
            if type(n.get(flag)) is not bool:raise ValueError('UNDECLARED_DEPENDENCE:'+key)
        if n.get('h_traceability') not in ['none_claimed','SI_definition','quantum_standard','unknown']:raise ValueError('INVALID_TRACEABILITY:'+key)
        if not isinstance(n.get('provenance_receipt'),str) or not n['provenance_receipt'].strip():raise ValueError('MISSING_CALIBRATION_RECEIPT:'+key)
        state[key]=2
    try:
        for key in nodes:visit(key)
    except ValueError as e:reasons.append(str(e))
    def ancestors(key,seen=None):
        seen=set() if seen is None else seen
        if key not in nodes or key in seen:return seen
        seen.add(key)
        parents=nodes[key].get('parents',[])
        if not isinstance(parents,list):return seen
        for p in parents:
            if isinstance(p,str):ancestors(p,seen)
        return seen
    values={};units={'mass':'kg','length':'m','omega':'rad/s'}
    anchors=record.get('anchors',{})
    if not isinstance(anchors,dict):anchors={};reasons.append('INVALID_ANCHORS')
    for key,unit in units.items():
        n=anchors.get(key)
        try:
            if not isinstance(n,dict) or n.get('unit')!=unit:raise ValueError('UNIT_OR_RECORD')
            if not isinstance(n.get('interval'),list) or len(n['interval'])!=2 or not all(isinstance(v,str) for v in n['interval']):raise ValueError('INTERVAL_FORMAT')
            lo,hi=map(F,n['interval'])
            if not 0<lo<=hi:raise ValueError('NONPOSITIVE_OR_REVERSED')
            source=n.get('calibration_node')
            if source not in nodes:raise ValueError('MISSING_CALIBRATION_NODE')
            values[key]=(lo,hi)
            for p in ancestors(source):
                dep=nodes[p]
                if dep.get('uses_candidate_relation') or dep.get('uses_hbar_in_anchor_formula'):tainted.append(p)
                if dep.get('h_traceability')!='none_claimed':h_paths.append(p)
        except (ValueError,TypeError,ZeroDivisionError):reasons.append('INVALID_ANCHOR:'+key)
    if tainted:reasons.append('TARGET_OR_HBAR_DERIVED_ANCHOR:'+','.join(sorted(set(tainted))))
    if any(nodes[k].get('h_traceability')=='unknown' for k in set(h_paths)):reasons.append('UNKNOWN_H_TRACEABILITY')
    mode=record.get('independence_mode')
    if mode not in ['target_independent_disclosed_SI','strict_h_free_full_chain']:reasons.append('UNDECLARED_INDEPENDENCE_MODE')
    elif mode=='strict_h_free_full_chain' and h_paths:reasons.append('H_DEPENDENT_TRACEABILITY')
    if record.get('unit_preparation_selected_using_candidate') is not False:reasons.append('UNIT_PREPARATION_INDEPENDENCE_UNESTABLISHED')
    result={'status':'BLOCKED' if reasons else 'METADATA_COMPLETE_FOR_EXTERNAL_REVIEW','reasons':reasons,
      'h_dependent_ancestor_nodes':sorted(set(h_paths)),'independence_mode':mode,'empirical_score':'UNSCORED',
      'scope':'Metadata and exact interval arithmetic only; receipt strings do not establish a physical map or independent measurement.'}
    if not reasons and len(values)==3:
        ml,mh=values['mass'];ll,lh=values['length'];wl,wh=values['omega']
        lo,hi=ml*wl*ll*ll,mh*wh*lh*lh
        result['conditional_A0_interval_J_s']=[str(lo),str(hi)]
        result['specific_action_A0_over_2_interval']=[str(lo/2),str(hi/2)]
        result['relative_half_width']=str((hi-lo)/(hi+lo))
        if record.get('data_status')!='EMPIRICAL':result['status']='SYNTHETIC_OR_PROSPECTIVE_ONLY'
    return result

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('record',type=Path);a=p.parse_args()
    print(json.dumps(inspect(json.loads(a.record.read_text())),indent=2))
