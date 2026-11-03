#!/usr/bin/env python3
"""Separate symbolic audit of the exact rank-four relaxed Gram witness.
Same-run cross-check, not independent peer review or empirical evidence.
"""
import argparse,json
from fractions import Fraction
from itertools import combinations
from pathlib import Path
import sympy as S

def main(path):
    data=json.loads(Path(path).read_text());D=data['coordinate_denominator']
    i,j,k=data['face_indices'];X=[None]*12;other=[n for n in range(12) if n!=k]
    for n,row in zip(other,data['independent_vertex_numerators']):X[n]=S.Matrix([S.Rational(x,D) for x in row])
    p,q=[S.Rational(x,data['dependent_coefficients_denominator']) for x in data['dependent_coefficients_numerators']]
    X[k]=p*X[i]+q*X[j]
    face=S.Matrix.hstack(*[X[n] for n in (i,j,k)])
    total=S.Matrix.hstack(*X)
    assert face.rank()==2 and total.rank()==4
    assert S.det(face.T*face)==0
    # Verify the original face belongs to the exact icosahedral graph without numerical edge sorting.
    phi=(1+S.sqrt(5))/2
    verts=sorted({tuple(v/2 for v in triple) for a in (-1,1) for b in (-1,1)
        for triple in [(0,a,b*phi),(a,b*phi,0),(b*phi,0,a)]},key=lambda row:tuple(float(x) for x in row))
    assert len(verts)==12
    edges=[(a,b) for a,b in combinations(range(12),2)
           if S.simplify(sum((verts[a][h]-verts[b][h])**2 for h in range(3))-1)==0]
    assert len(edges)==30 and all(tuple(sorted(pair)) in edges for pair in combinations((i,j,k),2))
    G=S.Rational(19,20);K=S.Rational(19,50)
    alpha=S.Rational(data['alpha_numerator'],data['alpha_denominator'])
    R=S.sqrt((5+S.sqrt(5))/8)
    spokes=[S.sqrt(v.dot(v))/R-1 for v in X]
    edge=[S.sqrt((X[a]-X[b]).dot(X[a]-X[b]))-1 for a,b in edges]
    E=(alpha**2+sum(v*v for v in spokes)+G*sum((v-alpha)**2 for v in spokes)+K*sum(v*v for v in edge))/2
    num=S.N(E,48)
    assert num<S.Rational(1,20) and num>0
    return {'face_rank_exact':face.rank(),'full_rank_exact':total.rank(),
            'face_gram_determinant_exact':str(S.det(face.T*face)),
            'reference_edges_verified_exactly':len(edges),
            'potential_high_precision_decimal':str(num),
            'status':'SYMBOLIC_RANK_EXACT / NUMERICAL_HIGH_PRECISION_ENERGY; primary Fraction enclosure establishes strict inequality'}
if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--witness',type=Path,required=True);parser.add_argument('--out',type=Path,required=True);a=parser.parse_args()
    result=main(a.witness);a.out.write_text(json.dumps(result,indent=2)+'\n');print(result)
