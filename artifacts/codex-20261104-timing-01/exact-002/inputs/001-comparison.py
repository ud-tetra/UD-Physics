#!/usr/bin/env python3
"""Exact full-versus-projected comparison; original blind witness and apex probe."""
import importlib.util
import json
from fractions import Fraction as Q
from pathlib import Path

p=Path(__file__).with_name('audit.py')
spec=importlib.util.spec_from_file_location('timing',p)
timing=importlib.util.module_from_spec(spec);spec.loader.exec_module(timing)
lin=timing.lin
iface=timing.iface

def main():
    d=timing.main(return_setup=True)
    M,P,H,Hinv=d['M'],d['P'],d['H'],d['Hinv']
    An,c,N,off=d['An'],d['c'],d['N'],d['newoffs']
    D=[r[:] for r in An]
    for i in range(5):
        for j,e in enumerate(N[1],off[1]):
            if e!=(0,1): D[i][j]=D[j][i]=Q(0)
    blind={}
    for name,A,expected_rank in [('all_active',An,5),('single_edge',D,7)]:
        K=lin.mul(Hinv,lin.mul(lin.mul(iface.switch.transpose(M),A),M))
        E=iface.switch.difference(lin.mul(A,M),lin.mul(M,K))
        v=c;vectors=[]
        for k in range(23):
            assert not any(lin.mvec(E,v))
            assert not any(lin.mvec(P,lin.mvec(K,v)))
            vectors.append(v);v=lin.mvec(K,v)
        dim=lin.rank([list(row) for row in zip(*vectors)])
        assert dim==expected_rank
        blind[name]={'krylov_dimension':dim,'zero_defect_powers':23,
                     'exact_all_times':'full target equals projected target; memory constant'}
    # Deliberate NEW preparation, preserving nominal reserve and crossing slope.
    alpha=Q(1,4)
    cp=c[:];cp[3]+=alpha
    assert timing.scalar(d['G'],cp)==Q(9,10)
    assert 2*iface.dot(lin.mvec(d['G'],cp),lin.mvec(d['Ao'],cp))==Q(-3)
    assert timing.scalar(H,cp)==Q(237,80)
    born=off[1]+N[1].index((3,4))
    assert not any(M[born])
    full=lin.mvec(M,cp);proj=cp
    vertex_derivatives=[];born_derivatives=[]
    for k in range(4):
        w=lin.mvec(M,proj)
        vertex_derivatives.append((full[4]-full[3])-(w[4]-w[3]))
        born_derivatives.append(full[born]-w[born])
        full=lin.mvec(An,full);proj=lin.mvec(d['K0'],proj)
    assert vertex_derivatives[:3]==[0,0,2*alpha]
    assert born_derivatives[:2]==[0,alpha]
    # Crucial remainder cancellation: original component is EXACTLY blind.
    # Only alpha*T e_3 enters the difference. ||T e_3||=1.
    e3=[Q(int(i==3)) for i in range(23)]
    assert timing.scalar(H,e3)==1
    assert Q(60)**2>(Q(2,6)*125)**2*2
    lo,hi=Q(1,240),Q(1,120)
    assert 1-60*hi==Q(1,2)
    sep=alpha*lo**2/2
    assert sep==Q(1,460800)
    budget=Q(1,1000000)
    assert budget<sep/2
    # Same error MODEL and same concrete four-error example as v0.1.
    # Old norm changes to 33/16; recheck the crossing-domain constants.
    assert iface.snorm(cp)==Q(33,16)
    assert Q(3,2)**2>Q(33,16)
    assert 3-Q(150)*Q(33,16)/600>Q(12,5)
    assert Q(12,5)-Q(45,1000)-Q(15,1000000)>2
    assert Q(12,5)/600>Q(1,1000)
    assert 144>Q(5,2)*25*Q(33,16)
    assert Q(7,4)**2>Q(237,80)
    assert 169>2*25*Q(237,80)
    assert 3*Q(1,1000)**2/2+Q(9,2)*Q(1,1000)<5*Q(1,1000)
    assert budget/78<Q(1,1000)
    assert budget/15+5*budget/78<Q(1,1000)
    assert lo>Q(1,2000)+Q(1,100000)
    example=[Q(1,200000000),Q(1,100000000),Q(1,100000000),Q(1,4000000)]
    used=sum(a*b for a,b in zip([78,15,13,1],example))
    assert used==Q(23,25000000)<budget
    result={'version':'v0.2-comparison','evidence':'EXACT_CONDITIONAL',
        'source_commit':'39d7c2d48a7670ae5b9d94402dcfd33b922d6e73',
        'original_witness':blind,
        'no_go':'No uniform full/projected discriminator on any error set including the original zero-error witness',
        'changed_preparation':{'added_old_vertex_3':str(alpha),'reserve':'9/10','gdot':'-3',
                               'old_stock':'33/16','event_stock':'237/80'},
        'all_active_probe':{'boundary_contrast':'x4-x3; full minus projected',
            'derivatives':list(map(str,vertex_derivatives)),
            'born_edge_34_derivatives':list(map(str,born_derivatives)),
            'separation':'Delta V(s)>=alpha*s^2-60alpha*s^3>=alpha*s^2/2',
            'sample_window':[str(lo),str(hi)],'separation_floor':str(sep),
            'joint_budget':'78epsilon+15r+13nu+eta<=1/1000000',
            'same_v01_example_budget_used':str(used)},
        'limitations':['new signed preparation is a deliberate probe, not native symmetry breaking',
            'all-active generator held fixed; immediate event; no ramp uncertainty',
            'projection and full flow are competing conditional laws; no selection between them',
            'midpoint is exact model function; floating implementation untested',
            'boundary sign/frame registration and physical instrumentation unprovided'],
        'physical_promotion':0}
    print(json.dumps(result,indent=2))
    return result

if __name__=='__main__':
    main()
