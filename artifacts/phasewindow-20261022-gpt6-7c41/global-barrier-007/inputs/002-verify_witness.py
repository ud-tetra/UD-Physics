#!/usr/bin/env python3
"""Exact rational certificate: a collapsed centre-face tetrahedron at E<1/8.

Uses SymPy only for exact icosahedral edge enumeration; all subsequent
energy inequalities are rational using integer-square-root interval enclosures. A *constructive upper*
barrier witness, not a globally minimized energy or a trajectory.
"""
import json, math, argparse
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations

D=10**10

def ri(q):
    """Interval for sqrt(nonnegative rational) with denominator D, exactly."""
    assert q>=0
    z=math.isqrt(q.numerator*D*D//q.denominator)
    lo=F(z,D);hi=F(z+1,D)
    assert lo*lo<=q<hi*hi
    return (lo,hi)

def square_bound(a,b):
    return max(a*a,b*b)

def parse(x):return F(x)

def ico_edges():
    # Build exact Q(sqrt5) icosahedron vertex graph by comparing squared edge
    # distances with 1, using integer pair Q(sqrt5) represented by SymPy only
    # for the enumeration; final energy arithmetic uses stdlib Fraction.
    import sympy as s
    phi=(1+s.sqrt(5))/2
    pts=[]
    for a in [-1,1]:
        for b in [-1,1]:
            pts +=[(s.Integer(0),a,b*phi),(a,b*phi,s.Integer(0)),(b*phi,s.Integer(0),a)]
    pts=sorted([tuple(s.simplify(t/2) for t in v) for v in pts],key=lambda z:tuple(float(t) for t in z))
    edges=[]
    for i,j in combinations(range(12),2):
        dd=sum((pts[i][h]-pts[j][h])**2 for h in range(3))
        if s.simplify(dd-1)==0: edges.append([i,j])
    assert len(edges)==30
    return edges

def verify(obj):
    edges=ico_edges()
    vec=[None]*12
    for idx,coords in obj['independent_vertex_coordinates_as_rationals'].items():
        vec[int(idx)]=[parse(t) for t in coords]
    c=obj['dependent_vertex'];i,j,k=obj['face_indices'];assert c['index']==k
    p,q=parse(c['p']),parse(c['q'])
    vec[k]=[p*vec[i][d]+q*vec[j][d] for d in range(3)]
    # Exact determinant vanishes by linearity of vector combination.
    def dot(a,b):return sum(x*y for x,y in zip(a,b))
    def cross(a,b):return [a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]]
    det=dot(vec[i],cross(vec[j],vec[k]))
    assert det==0
    phi5lo,phi5hi=ri(F(5))
    Rlo=ri((F(5)+phi5lo)/8)[0];Rhi=ri((F(5)+phi5hi)/8)[1]
    alpha=parse(obj['alpha']);g=F(19,20);ke=F(19,50)
    total_rad_upper=F(0);rad_bounds=[]
    for v in vec:
        rlo,rhi=ri(dot(v,v))
        slo=rlo/Rhi-1;shi=rhi/Rlo-1
        rad_bounds.append((slo,shi))
        total_rad_upper+=square_bound(slo,shi)+g*square_bound(slo-alpha,shi-alpha)
    total_edge_upper=F(0)
    edge_bounds=[]
    for a,b in edges:
        d=[vec[a][h]-vec[b][h] for h in range(3)]
        lo,hi=ri(dot(d,d))
        edge_bounds.append((lo,hi))
        total_edge_upper+=ke*square_bound(lo-1,hi-1)
    E_hi=(alpha*alpha+total_rad_upper+total_edge_upper)/2
    E_reference=F(1360051,20000000)
    assert E_hi<F(1,8)
    assert E_hi>E_reference
    # Compute exact lower bound for each housing-to-anchor strut in witness:
    face_set=[]
    for a,b,c in combinations(range(12),3):
        if all(sorted([v,w]) in edges for v,w in [(a,b),(a,c),(b,c)]):face_set.append((a,b,c))
    assert len(face_set)==20
    min_strut_squared=None
    for a,b in edges:
        midpoint=[(vec[a][h]+vec[b][h])/2 for h in range(3)]
        adj=[face for face in face_set if a in face and b in face]
        assert len(adj)==2
        anchor=[a,b]+[next(k for k in face if k not in (a,b)) for face in adj]
        for v in anchor:
            squared=dot([midpoint[h]-vec[v][h] for h in range(3)],[midpoint[h]-vec[v][h] for h in range(3)])
            if min_strut_squared is None or squared<min_strut_squared:min_strut_squared=squared
    assert min_strut_squared>0
    # Separate exact *local* obstruction witness: three face radial lengths
    # stay exactly R, while the three face vertices lie on a single great
    # circle at polar angles -pi/4, 0, +pi/4. Their face-edge lengths are
    # sqrt(R^2*(2-sqrt(2))) twice and sqrt(2*R^2) once. This ignores 27
    # other shell edges, so it is NOT a global physical configuration cost.
    sqrt2lo,sqrt2hi=ri(F(2))
    r2lo=(F(5)+phi5lo)/8;r2hi=(F(5)+phi5hi)/8
    short2lo=r2lo*(2-sqrt2hi);short2hi=r2hi*(2-sqrt2lo)
    long2lo=2*r2lo;long2hi=2*r2hi
    shortlo=ri(short2lo)[0];short_hi=ri(short2hi)[1]
    longlo=ri(long2lo)[0];long_hi=ri(long2hi)[1]
    E_local_hi=ke*(2*square_bound(shortlo-1,short_hi-1)+square_bound(longlo-1,long_hi-1))/2
    assert E_local_hi<E_reference
    return {
     'status':'EXACT_COLLAPSED_CELL_WITNESS',
     'face':obj['face_indices'],'determinant_exact':'0',
     'energy_rational_interval_upper':str(E_hi),
     'energy_upper_float_for_display':float(E_hi),
     'energy_proven_less_than':'1/8',
     'pulse_reference_total_energy':'1360051/20000000',
     'pulse_energy_float_for_display':float(E_reference),
     'local_only_flat_face_energy_upper':str(E_local_hi),
     'local_only_flat_face_energy_upper_float':float(E_local_hi),
     'local_only_scope':'Six face members only; other 27 shell edges and 9 spokes omitted, so it cannot disprove a global energy barrier.',
     'minimum_strut_squared_exact':str(min_strut_squared),
     'min_strut_lower_rational':str(ri(min_strut_squared)[0]),
     'all_30_shell_edges_positive':all(lo>0 for lo,hi in edge_bounds),
     'all_12_spokes_positive':all(slo>-1 for slo,shi in rad_bounds),
     'scope':'Constructive upper bound on lowest possible zero-cell-determinant energy; NOT a universal lower bound, a dynamical trajectory, or a u100 safety certificate.'
    }

if __name__=='__main__':
    a=argparse.ArgumentParser();a.add_argument('--witness',type=Path,required=True);a.add_argument('--out',type=Path,required=True);args=a.parse_args()
    data=verify(json.loads(args.witness.read_text()))
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(data,indent=2)+'\n')
    print('PASS: exact coplanarity and conservative E<1/8:',data['energy_upper_float_for_display'])
