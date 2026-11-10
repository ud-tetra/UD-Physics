#!/usr/bin/env python3
"""Exact rational 4D flattened-cell Gram-relaxation witness.

This is a mathematical counterexample to rank-unrestricted Gram barrier methods,
NOT a physically admissible 3D icosahedral state or a dynamical trajectory.
"""
import argparse, json, hashlib
from fractions import Fraction as Q
from itertools import combinations
from math import isqrt
from pathlib import Path

def sqrt_enclosure(x, scale=10**12):
    assert x>=0
    n=isqrt(x.numerator*scale*scale//x.denominator)
    return Q(n,scale),Q(n+1,scale)

def det(matrix):
    a=[[Q(v) for v in row] for row in matrix];n=len(a);product=Q(1)
    for k in range(n):
        i=next((j for j in range(k,n) if a[j][k]!=0),None)
        if i is None:return Q(0)
        if i!=k:a[i],a[k]=a[k],a[i];product=-product
        p=a[k][k];product*=p
        for j in range(k+1,n):
            t=a[j][k]/p
            for h in range(k+1,n):a[j][h]-=t*a[k][h]
            a[j][k]=Q(0)
    return product

def dot(x,y):return sum((u*v for u,v in zip(x,y)),Q(0))
def minus(x,y):return [u-v for u,v in zip(x,y)]
def square_norm(x):return dot(x,x)

def verify(source):
    data=json.loads(Path(source).read_text())
    N=data['coordinate_denominator'];p,q=(Q(v,data['dependent_coefficients_denominator']) for v in data['dependent_coefficients_numerators'])
    face=data['face_indices'];i,j,k=face
    others=[z for z in range(12) if z!=k]
    X=[None]*12
    for ix,coord in zip(others,data['independent_vertex_numerators']):X[ix]=[Q(t,N) for t in coord]
    X[k]=[p*a+q*b for a,b in zip(X[i],X[j])]
    assert all(len(v)==4 for v in X)
    # One rank-2 face: exact relation and non-collinear independent face vectors.
    assert all(X[k][z]==p*X[i][z]+q*X[j][z] for z in range(4))
    assert X[i][0]*X[j][1]-X[i][1]*X[j][0] != 0
    face_gram=[[dot(X[u],X[v]) for v in face] for u in face]
    assert det(face_gram)==0
    # Full Gram rank>=4 through exact 4x4 minor.
    inds=None;minor=None
    for selected in combinations([v for v in range(12) if v!=k],4):
        val=det([X[z] for z in selected])
        if val!=0:inds=selected;minor=val;break
    assert inds is not None
    G=Q(19,20);K=Q(19,50);alpha=Q(data['alpha_numerator'],data['alpha_denominator'])
    # Original reference graph over Q(sqrt(5)): each coordinate stored as
    # (rational coefficient of 1, rational coefficient of sqrt(5)).
    # Floating keys determine only the frozen public vertex ordering, never
    # the member classification or the energy inequalities.
    import math
    zero=(Q(0),Q(0))
    unit=lambda a:(Q(a,2),Q(0))
    golden=lambda b:(Q(b,4),Q(b,4))  # +/-phi/2 = +/- (1+sqrt5)/4
    verts=sorted(set(v for a in (-1,1) for b in (-1,1)
               for v in ((zero,unit(a),golden(b)),
                         (unit(a),golden(b),zero),
                         (golden(b),zero,unit(a)))),
               key=lambda v:tuple(float(c[0]+c[1]*math.sqrt(5)) for c in v))
    def exact_squared_ref_dist(a,b):
        constant=Q(0);radical=Q(0)
        for c,d in zip(verts[a],verts[b]):
            h=c[0]-d[0];t=c[1]-d[1]
            constant+=h*h+5*t*t; radical+=2*h*t
        return constant,radical
    edges=[(a,b) for a,b in combinations(range(12),2)
           if exact_squared_ref_dist(a,b)==(Q(1),Q(0))]
    assert len(verts)==12 and len(edges)==30
    assert tuple(face) in [t for t in combinations(range(12),3) if all(tuple(sorted(pair)) in edges for pair in combinations(t,2))]
    # Exact algebraic reference radius interval; no use of floating phi to evaluate energy.
    rt5lo,rt5hi=sqrt_enclosure(Q(5))
    radlo,radhi=sqrt_enclosure((Q(5)+rt5lo)/8)[0],sqrt_enclosure((Q(5)+rt5hi)/8)[1]
    def s_range(v):
        l,u=sqrt_enclosure(square_norm(v))
        return l/radhi-1,u/radlo-1
    def e_range(v):
        l,u=sqrt_enclosure(square_norm(v))
        return l-1,u-1
    def bound(a,b):return max(abs(a),abs(b))**2
    spokes=[s_range(x) for x in X]
    ends=[e_range(minus(X[a],X[b])) for a,b in edges]
    assert all(square_norm(x)>0 for x in X)
    assert all(square_norm(minus(X[a],X[b]))>0 for a,b in edges)
    exact_bound=(alpha*alpha+sum(bound(l,h) for l,h in spokes)+G*sum(bound(l-alpha,h-alpha) for l,h in spokes)+K*sum(bound(l,h) for l,h in ends))/2
    assert exact_bound<Q(1,20),(float(exact_bound),float(Q(1,20)))
    pulse=Q(1360051,20000000)
    assert Q(1,20)<pulse
    result={
      'evidence':'EXACT / CONDITIONAL rational witness, mathematical PSD Gram relaxation ONLY',
      'source_sha256':hashlib.sha256(Path(source).read_bytes()).hexdigest(),
      'member_count':{'spokes':len(spokes),'edges':len(ends)},
      'original_face_indices':face,
      'face_rank':2,'face_gram_determinant':str(det(face_gram)),
      'full_vertex_coordinate_dimension':4,'nonzero_four_by_four_minor_vertices':list(inds),
      'nonzero_four_by_four_minor_sign':1 if minor>0 else -1,
      'alpha':str(alpha),'g':str(G),'k':str(K),
      'energy_upper_float_for_display_only':float(exact_bound),
      'certified_energy_strictly_less_than':'1/20',
      'original_pulse_energy':'1360051/20000000',
      'strict_pulse_comparison':'E_4Drelax <1/20<1360051/20000000',
      'source_exposure':'Geometry, original pulse threshold, and numerical 4D solution were examined first; rational coordinates rounded from post-exposure optimizer. This is a constructed counterexample to a relaxation, not independent prediction.',
      'interpretation':'Any valid lower energy bound > pulse cannot hold across all PSD Gram matrices unless it includes spatial rank<=3 or equivalently restrictive 3D constraints. It does not refute the 3D barrier or physically reopen extra spatial dimensions.',
      'limits':['No lower bound for original 3D cell collapse','4D positions not permissible in original Euclidean R3 mechanics','No u100 nonlinear breathing/ringdown theorem']
    }
    return result

if __name__=='__main__':
    a=argparse.ArgumentParser();a.add_argument('--witness',type=Path,required=True);a.add_argument('--out',type=Path,required=True);v=a.parse_args()
    result=verify(v.witness);v.out.parent.mkdir(parents=True,exist_ok=True);v.out.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print('EXACT PASS: rank-2 flat face, full rank-4 configuration, strict energy bound E<1/20<original pulse')
    print('Energy bound (display only):',result['energy_upper_float_for_display_only'])
