#!/usr/bin/env python3
"""Exact conditional continuous-time gain gate for UD 3D symmetric A5 adjoints.
Does not prove its nodal or derivative premises; see CONTINUOUS_GAIN_GATE_023.md.
"""
from fractions import Fraction as F
from pathlib import Path
import argparse, json
MESH=(0,1,2,4,6,10,20,40,70,80,90,100)
NODE=F(1,10000)
DERIV=F(1,1000)
LIMIT=F(1,40)
def exact_gate():
    assert all(y>x for x,y in zip(MESH,MESH[1:]))
    longest=max(y-x for x,y in zip(MESH,MESH[1:]))
    bound=NODE+F(longest,2)*DERIV
    spare=LIMIT-bound
    assert longest==30 and bound==F(151,10000) and spare==F(99,10000)
    return {'mesh':list(MESH),'max_gap':longest,'conditional_node_gate':str(NODE),
            'conditional_derivative_gate':str(DERIV),'conditional_uniform_gain':str(bound),
            'nonlinear_remainder_allowance':str(spare),'orientation_threshold':str(LIMIT),
            'proof':'Nearest node distance <=15; integrate L_prime in operator norm.'}
def main():
    p=argparse.ArgumentParser()
    p.add_argument('--source',type=Path)
    p.add_argument('--out',type=Path)
    a=p.parse_args()
    result={'evidence':'EXACT_CONDITIONAL','theorem':exact_gate(),
            'status':'NODE_AND_DERIVATIVE_PREMISES_OPEN'}
    if a.source:
        data=json.loads(a.source.read_text())
        sample={0:0.0}
        for row in data['sampled_results']:
            sample[int(row['u'])]=float(row['representative']['gain'])
        assert tuple(sorted(sample))==MESH and max(sample.values())<float(NODE)
        result['development_node_samples']={str(k):v for k,v in sample.items()}
        result['development_note']='Numerical samples do not verify true nodal inequalities.'
    text=json.dumps(result,indent=2,sort_keys=True)+'\n'
    if a.out:
        a.out.parent.mkdir(parents=True,exist_ok=True)
        a.out.write_text(text)
    print(text)
if __name__=='__main__':main()
