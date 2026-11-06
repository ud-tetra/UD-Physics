"""Exact conditional count-recorder and ordered-label readout bounds."""
import json
from pathlib import Path
from itertools import product
from collections import defaultdict

def main():
    widths=[]
    for w in range(1,9):
        K=2**w-1
        # Source audit's stop invariant R+h=N; terminal is (K,1).
        assert K+1==2**w
        widths.append(dict(width=w,acknowledged_max=K,pending_at_stop=1,source_count_at_stop=2**w))
    # Separate hypothetical coupling to three labeled flips; count R and
    # endpoint theta are insufficient to decode event order.
    fibers=defaultdict(list)
    for word in product(range(3),repeat=2):
        theta=0
        for p in word: theta^=1<<p
        fibers[(2,theta)].append(word)
    assert (0,1) in fibers[(2,3)] and (1,0) in fibers[(2,3)]
    assert len(fibers[(2,0)])==3
    out=dict(status='EXACT_CONDITIONAL',source_recorder_widths=widths,
             conditional_product_readout='(acknowledged count R, pending h, theta) under separately assumed labeled XOR coupling',
             two_step_collisions=dict(AB_BA_same=(2,0,3),AA_BB_CC_same=(2,0,0)),
             source_status='finite recorder source audit only; no sourced coupling to Q198 or packet endpoint',physical_promotion=0)
    Path(__file__).with_name('results.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps(dict(status=out['status'],width_3_stop=widths[2],two_step_fiber_count=len(fibers[(2,3)]))))
if __name__=='__main__':main()
