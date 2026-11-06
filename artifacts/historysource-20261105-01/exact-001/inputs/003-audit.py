"""Exact finite-dimensional receipt-index lineage ambiguity witnesses."""
import json
from pathlib import Path

def rank_1(t): return int(t != 0)

def main():
    # Both L^- and L^+ have dimension one over Q; T=0 or T=1.
    cases=[]
    for t in (0,1):
        rank=rank_1(t)
        ker=1-rank; coker=1-rank
        cases.append(dict(continuation_scalar=t,domain_dim=1,codomain_dim=1,
                          kernel_dim=ker,cokernel_dim=coker,index=ker-coker,
                          net_budget=1-1))
    assert cases[0]['index']==cases[1]['index']==0
    assert cases[0]['kernel_dim']!=cases[1]['kernel_dim']
    # Net source/sink balance alone cannot distinguish simultaneous renewal.
    balances=[dict(source=x,sink=x,net=x-x) for x in (0,1)]
    assert balances[0]['net']==balances[1]['net']==0
    out=dict(status='EXACT_CONDITIONAL',source_rows=['Q194','Q195','Q198','Q200','Q205','Q208','Q210','Q151','Q154','Q158'],continuation_witnesses=cases,source_sink_witnesses=balances,scope='formal receipts only; source admissibility and environment retention open',physical_promotion=0)
    Path(__file__).with_name('results.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps(dict(status=out['status'],indices=[c['index'] for c in cases],kernel_dims=[c['kernel_dim'] for c in cases])))
if __name__=='__main__':main()
