"""Exact finite driven-parity history collision enumeration."""
from itertools import product
from collections import defaultdict
from pathlib import Path
import json

def endpoint(word, initial=0):
    x=initial
    for p in word: x ^= 1 << p
    return x

def counts(word): return tuple(word.count(p) for p in range(3))

def main():
    masks={}
    for n in range(1,7):
        fibers=defaultdict(list)
        for word in product(range(3),repeat=n): fibers[endpoint(word)].append(word)
        assert sum(map(len,fibers.values()))==3**n
        assert len(fibers)<=8
        masks[n]={"histories":3**n,"reachable_endpoints":len(fibers),"max_fiber":max(map(len,fibers.values())),"lower_bound_extra_bits":(max(map(len,fibers.values()))-1).bit_length()}
    a,b=(0,1),(1,0)
    assert a!=b and endpoint(a)==endpoint(b)==3 and counts(a)==counts(b)==(1,1,0)
    c=[(0,0),(1,1),(2,2)]
    assert all(endpoint(w)==0 for w in c)
    for mask in range(8):
        for initial in range(8):
            final=initial^mask
            assert final^mask==initial  # fixed-mask closed bijection
    out={"status":"EXACT_CONDITIONAL","alphabet":"three labeled opposite-pair flips 0,1,2","update":"theta_next=theta xor (1<<event)","two_step_collision":{"ordered_words":[list(a),list(b)],"same_final":3,"same_counts":[1,1,0],"return_words":[list(w) for w in c]},"counts_by_length":masks,"closed_fixed_mask":"bijective; inverse uses same xor mask","claim_boundary":"conditional driven toy law; no UD physical archive or source event update"}
    Path(__file__).with_name('results.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps({"status":out['status'],"two_step_max_fiber":masks[2]['max_fiber'],"six_step_max_fiber":masks[6]['max_fiber']}))
if __name__=='__main__':main()
