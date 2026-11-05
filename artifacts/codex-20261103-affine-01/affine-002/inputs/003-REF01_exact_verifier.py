#!/usr/bin/env python3
"""REF01 development verifier. Run with no arguments for exact controls,
or pass JSON with P, R, C, G matrices (integers or rational strings).
P embeds coarse coordinates; R restricts fine coordinates; C and G are
coarse and fine Gram matrices. Declared premise: RP=I and P^T G=C R.
Physical promotion: 0. See https://github.com/ud-tetra/UD/issues/136.
"""
from fractions import Fraction as F
import json
import sys

def matrix(rows):
    if not isinstance(rows,list) or not rows or not all(
        isinstance(r,list) and r and len(r)==len(rows[0]) for r in rows):
        raise ValueError("expected a nonempty rectangular matrix")
    if any(type(x) not in (int,str) for r in rows for x in r):
        raise ValueError("use integers or rational strings, never JSON floats")
    return [[F(x) for x in r] for r in rows]

def tr(a):
    return list(map(list,zip(*a)))

def mul(a,b):
    if len(a[0])!=len(b):
        raise ValueError("incompatible dimensions")
    return [[sum(x*y for x,y in zip(r,c)) for c in tr(b)] for r in a]

def eye(n):
    return [[int(i==j) for j in range(n)] for i in range(n)]

def spd(a):
    if a!=tr(a):
        return False
    s=[r[:] for r in a]
    for k in range(len(s)):
        p=s[k][k]
        if p<=0:
            return False
        for i in range(k+1,len(s)):
            for j in range(k+1,len(s)):
                s[i][j]-=s[i][k]*s[k][j]/p
    return True

def check(data):
    p,r,c,g=(matrix(data[k]) for k in ("P","R","C","G"))
    n,m=len(p),len(p[0])
    if any((len(a),len(a[0]))!=shape for a,shape in
           [(r,(m,n)),(c,(m,m)),(g,(n,n))]):
        raise ValueError("expected P:n×m, R:m×n, C:m×m, G:n×n")
    lhs,rhs=mul(tr(p),g),mul(c,r)
    residual=[[str(x-y) for x,y in zip(a,b)] for a,b in zip(lhs,rhs)]
    checks=dict(retraction=mul(r,p)==eye(m),coarse_spd=spd(c),
                fine_spd=spd(g),adjoint_compatibility=lhs==rhs)
    passed=all(checks.values())
    d=n-m
    return dict(checks=checks,compatible=passed,residual=residual,
                family_dimension=d*(d+1)//2 if passed else None,
                native_selection="OPEN",physical_promotion=0)

def demo():
    m=matrix([[2,1,-1],[1,3,-2],[-1,-1,4]])
    b=[[1],[-1],[0]]
    residual=mul(m,b)
    assert residual==[[1],[-2],[0]] and not spd(m)
    base=dict(P=[[1],[1]],R=[[1,0]],C=[[1]])
    cases=[
        ("compatible_nondiagonal",base|dict(G=[[2,-1],[-1,1]]),True),
        ("second_metric_same_premises",base|dict(G=[[3,-2],[-2,2]]),True),
        ("identity_incompatible",base|dict(G=eye(2)),False),
        ("singular_compatible_equation",base|dict(G=[[1,0],[0,0]]),False),
        ("indefinite_compatible_equation",base|dict(G=[[0,1],[1,-1]]),False),
        ("compatible_diagonal_other_premises",base|dict(P=[[1],[0]],G=eye(2)),True),
        ("invalid_retraction",base|dict(R=[[2,0]],G=[[2,-1],[-1,1]]),False),
    ]
    results={}
    for label,data,want in cases:
        result=check(data)
        assert result["compatible"]==want,label
        results[label]=result
    return dict(mock_rejected=True,mock_Mb=[str(v[0]) for v in residual],
                controls=results,physical_promotion=0)

if __name__=="__main__":
    if len(sys.argv)==1:
        print(json.dumps(demo(),indent=2))
    elif len(sys.argv)==2:
        with open(sys.argv[1],encoding="utf-8") as f:
            result=check(json.load(f))
        print(json.dumps(result,indent=2))
        sys.exit(0 if result["compatible"] else 1)
    else:
        sys.exit("usage: python REF01_exact_verifier.py [candidate.json]")
