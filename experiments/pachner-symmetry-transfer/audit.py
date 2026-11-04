#!/usr/bin/env python3
"""Exact apex/base equivariant transfer obstruction on the 2->3 overlay."""
import importlib.util
import json
from fractions import Fraction as Q
from pathlib import Path

source=Path(__file__).parents[1]/'pachner-event-actuator'/'audit.py'
spec=importlib.util.spec_from_file_location('act',source)
act=importlib.util.module_from_spec(spec); spec.loader.exec_module(act)
prior=act.prior; lin=act.lin

def rep(labels,p):
    index={key:i for i,key in enumerate(labels)}
    out=[[Q(0) for _ in labels] for _ in labels]
    for j,(degree,s) in enumerate(labels):
        word=[p[i] for i in s]
        target=(degree,tuple(sorted(word)))
        inversions=sum(word[i]>word[k] for i in range(len(word)) for k in range(i+1,len(word)))
        out[index[target]][j]=Q((-1)**inversions)
    return out

def mul(A,B): return lin.mul(A,B)
def mvec(A,v): return [sum(a*b for a,b in zip(row,v)) for row in A]
def transpose(A): return [list(row) for row in zip(*A)]
def nullspace(A):
    A=[row[:] for row in A]; n=len(A[0]); piv=[]; r=0
    for j in range(n):
        k=next((i for i in range(r,len(A)) if A[i][j]),None)
        if k is None:continue
        A[r],A[k]=A[k],A[r]
        z=A[r][j]; A[r]=[x/z for x in A[r]]
        for i in range(len(A)):
            if i!=r and A[i][j]:
                z=A[i][j]; A[i]=[x-z*y for x,y in zip(A[i],A[r])]
        piv.append(j);r+=1
    free=[j for j in range(n) if j not in piv]
    vectors=[]
    for j in free:
        v=[Q(0)]*n;v[j]=Q(1)
        for i,k in enumerate(piv):v[k]=-A[i][j]
        vectors.append(v)
    return vectors

def main():
    old=[(0,1,2,3),(0,1,2,4)]
    new=[(0,1,3,4),(0,2,3,4),(1,2,3,4)]
    O=lin.simplices(old);N=lin.simplices(new)
    old_only=[(k,s) for k in range(4) for s in O[k] if s not in N[k]]
    new_only=[(k,s) for k in range(4) for s in N[k] if s not in O[k]]
    assert old_only==[(2,(0,1,2)),(3,(0,1,2,3)),(3,(0,1,2,4))]
    assert len(new_only)==7
    generators={'base_swap':(1,0,2,3,4),'base_cycle':(1,2,0,3,4),'apex_swap':(0,1,2,4,3)}
    Ro={name:rep(old_only,p) for name,p in generators.items()}
    Rn={name:rep(new_only,p) for name,p in generators.items()}
    for D in list(Ro.values())+list(Rn.values()):
        assert mul(transpose(D),D)==[[Q(i==j) for j in range(len(D))] for i in range(len(D))]
    # All exact rational equivariant Y:Q^3->Q^7 solve Y Ro=Rn Y.
    rows=[]
    for name in generators:
        a,b=Ro[name],Rn[name]
        for i in range(7):
            for j in range(3):
                row=[Q(0)]*21
                for k in range(3):row[3*i+k]+=a[k][j]
                for k in range(7):row[3*k+j]-=b[i][k]
                rows.append(row)
    basis=nullspace(rows)
    assert len(basis)==1 and lin.rank(rows)==20
    base_basis=nullspace(rows[:42])
    assert len(base_basis)==3 and lin.rank(rows[:42])==18
    for vector in base_basis:
        B=[[vector[3*i+j] for j in range(3)] for i in range(7)]
        assert lin.rank(B)==1
        assert all(B[i]==[Q(0)]*3 for i,(k,s) in enumerate(new_only) if k!=3)
    # Every old-only coordinate is base-sign, while the new base-sign
    # subspace is one-dimensional, so every base-equivariant image has rank<=1.
    Y=[[basis[0][3*i+j] for j in range(3)] for i in range(7)]
    assert lin.rank(Y)==1
    assert all(mul(Y,Ro[name])==mul(Rn[name],Y) for name in generators)
    # Apex-swap eigenspaces: old-even dimension 2, new-even dimension 0.
    apex_old=Ro['apex_swap'];apex_new=Rn['apex_swap']
    assert lin.rank([[apex_old[i][j]-Q(i==j) for j in range(3)] for i in range(3)])==1
    assert lin.rank([[apex_new[i][j]-Q(i==j) for j in range(7)] for i in range(7)])==7
    even=[ [Q(1),Q(0),Q(0)], [Q(0),Q(1),Q(1)] ]
    for v in even:
        assert mvec(apex_old,v)==v and mvec(Y,v)==[Q(0)]*7
    odd=[Q(0),Q(1),Q(-1)]
    image=mvec(Y,odd)
    assert lin.rank([image])==1
    # Normalize the unique rational intertwiner so Y(odd) is the primitive
    # signed top combination; then ||odd||²=2 and ||Y odd||²=3.
    factor=next(x for x in image if x)
    Y=[[x/factor for x in row] for row in Y]
    image=mvec(Y,odd)
    assert sum(x*x for x in odd)==2 and sum(x*x for x in image)==3
    assert all(image[i]==0 for i,(k,s) in enumerate(new_only) if k!=3)
    for name in ('base_swap','base_cycle'):
        sign=Q(-1) if name=='base_swap' else Q(1)
        assert mvec(Rn[name],image)==[sign*x for x in image]
    assert mvec(Rn['apex_swap'],image)==[-x for x in image]
    # Minimal real-algebraic two-memory construction: both memory modes
    # transform as base-sign/apex-even. m1=f, m2=(t3+t4)/sqrt(2),
    # new top vector=(t3-t4)/sqrt(6)*(1,-1,1).
    # Verify its Gram entirely in Q, before adjoining the exact radicals.
    Gmemory=[[Q(1),Q(0),Q(0)],[Q(0),Q(1,2),Q(1,2)],[Q(0),Q(1,2),Q(1,2)]]
    Gnew=[[Q(0),Q(0),Q(0)],[Q(0),Q(1,2),Q(-1,2)],[Q(0),Q(-1,2),Q(1,2)]]
    assert [[Gmemory[i][j]+Gnew[i][j] for j in range(3)] for i in range(3)]==[[Q(i==j) for j in range(3)] for i in range(3)]
    # Real isometry on the odd line needs scale sqrt(2/3); rational scale
    # impossible because v_3(2/3)=-1 is odd (a rational square has even valuations).
    assert Q(2,3).numerator==2 and Q(2,3).denominator==3
    assert sum(len(O[k]) for k in range(4))-len(old_only)==20
    assert sum(len(N[k]) for k in range(4))-len(new_only)==20
    print(json.dumps({'source_base':'15cc72b0203288a3c5b67563a0a18285bdc17d0a',
        'old_only':[{'degree':k,'simplex':list(s)} for k,s in old_only],
        'new_only':[{'degree':k,'simplex':list(s)} for k,s in new_only],
        'group_generators':{k:list(v) for k,v in generators.items()},
        'intertwiner_linear_constraints':len(rows),'constraint_rank':lin.rank(rows),
        'base_only_intertwiner_dimension':len(base_basis),'base_only_maximum_rank':1,
        'intertwiner_dimension':len(basis),'maximum_intertwiner_rank':lin.rank(Y),
        'apex_even_dimensions':{'old':2,'new':0},
        'old_even_kernel_generators':['face012','top0123+top0124'],
        'old_odd_top_difference':[str(x) for x in odd],
        'new_image_of_old_odd':[{'degree':k,'simplex':list(s),'coefficient':str(image[i])}
                                 for i,(k,s) in enumerate(new_only) if image[i]],
        'odd_norm_squared':{'old':'2','new_primitive':'3'},
        'real_odd_isometry_scale_squared':'2/3',
        'rational_odd_isometry':'NO (prime valuation at 2 and 3 odd)',
        'minimal_real_two_memory_candidate':{
            'memory_representation':'two base-sign/apex-even unit modes',
            'm1':'face012 amplitude',
            'm2':'(top0123+top0124)/sqrt(2)',
            'new_signed_top_amplitude':'(top0123-top0124)/sqrt(6) on each of (0134,-0234,1234)',
            'gram_memory':[[str(x) for x in row] for row in Gmemory],
            'gram_new':[[str(x) for x in row] for row in Gnew],
            'gram_total':'I_3 exactly'},
        'no_full_isometric_transfer':'YES under shared-coordinate fixation and S3xC2 equivariance',
        'shell_amplitude_count':20,
        'instant_shell_guard_witness':'zero state and unit old face012 have identical shell amplitudes at the event; instantaneous shell-only guard cannot distinguish them',
        'gate_update':'OPEN: Q165/Q166/Q169/Q170/Q173/Q177-Q179 do not source an autonomous event register or reset.'},indent=2,sort_keys=True))

if __name__=='__main__':main()
