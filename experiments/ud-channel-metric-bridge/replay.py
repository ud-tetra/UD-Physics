"""Exact signed first-refinement readout, stdlib only."""
import json
from fractions import Fraction as Q
from itertools import combinations, permutations, product
from pathlib import Path


def mat(m,n,f):
    return [[Q(f(i,j)) for j in range(n)] for i in range(m)]


def tr(a): return list(map(list,zip(*a)))
def mul(a,b): return [[sum(x*y for x,y in zip(r,c)) for c in tr(b)] for r in a]
def sub(a,b): return [[x-y for x,y in zip(r,s)] for r,s in zip(a,b)]
def trace(a): return sum(a[i][i] for i in range(len(a)))
def rank(a):
    a = [r[:] for r in a]
    k = 0
    for j in range(len(a[0])):
        p = next((i for i in range(k,len(a)) if a[i][j]),None)
        if p is None: continue
        a[k],a[p]=a[p],a[k]
        a[k] = [x/a[k][j] for x in a[k]]
        for i in range(k+1,len(a)):
            a[i]=[x-a[i][j]*y for x,y in zip(a[i],a[k])]
        k += 1
    return k


def simplices(tops):
    return [s for d in range(1,5) for s in sorted({s for t in tops for s in combinations(t,d)})]


def incidence(s):
    return mat(len(s),len(s),lambda i,j: sum((-1)**k for k in range(len(s[j]))
               if len(s[j])>1 and s[j][:k]+s[j][k+1:]==s[i]))


def permutation(s,p):
    words=[tuple(p[i] for i in w) for w in s]
    return mat(len(s),len(s),lambda i,j: int(s[i]==tuple(sorted(words[j])))
               *(-1)**sum(a>b for a,b in combinations(words[j],2)))


def run():
    old=(0,1,2,3)
    top=[tuple(i for i in old if i!=j)+(4,) for j in old]
    s,n=simplices([old]),simplices(top)
    d,e=incidence(s),incidence(n)
    A,B=sub(d,tr(d)),sub(e,tr(e))
    F=mat(29,15,lambda i,j: (int(n[i]==s[j]) if s[j]!=old else
                        sum((-1)**(3+k) for k in old if n[i]==top[k])))
    assert mul(e,F)==mul(F,d)
    gram=mul(tr(F),F)
    assert gram==mat(15,15,lambda i,j:int(i==j)*(4 if i==14 else 1))
    L=mat(15,29,lambda i,j:F[j][i]/gram[i][i])
    N=sub(mat(29,29,lambda i,j:i==j),mul(F,L))
    R=mul(N,mul(B,F))
    J=mat(15,15,lambda i,j:A[i][j]/2)
    h=mat(15,1,lambda i,j:Q(1,2) if len(s[i])==1 else 0)
    V=mat(15,2,lambda i,j:int(i==14) if j==0 else J[i][14])
    pairs=[[(0,1),(2,3)],[(0,2),(1,3)],[(0,3),(1,2)]]
    Es=[mat(15,2,lambda i,j:s[i]==pair[j]) for pair in pairs]
    W={'000':h,'111':V}
    for label,dual,E in zip(('100','010','001'),('011','101','110'),Es):
        W[label]=E
        W[dual]=mul(J,E)
    P={label:mul(X,tr(X)) for label,X in W.items()}
    I=mat(15,15,lambda i,j:i==j)
    assert all(sum(X[i][j] for X in P.values())==I[i][j] for i,j in product(range(15),repeat=2))
    assert mul(tr(R),R)==sub(I,P['111'])
    blocks={label:mul(R,X) for label,X in P.items()}
    traces={k:int(trace(mul(tr(v),v))) for k,v in sorted(blocks.items())}
    assert list(traces.values())==[1,2,2,2,2,2,2,0]
    perms=list(permutations(old))
    for p in perms:
        U,Z=permutation(s,p),permutation(n,p+(4,))
        assert mul(Z,R)==mul(R,U)
        for X in P.values():
            assert mul(U,mul(X,tr(U))) in P.values()
    C=tr(R)
    f=mat(29,1,lambda i,j:n[i]==(4,))
    T=mul(N,mul(B,N))
    # On N, the only direction invisible at order zero is the centroid vertex.
    assert rank(N)==14 and rank(C)==13 and not any(map(any,mul(C,f)))
    assert mul(N,f)==f and mul(C,N)==C
    slope=mul(C,mul(T,f))
    expected=mat(15,1,lambda i,j:-int(len(s[i])==1))
    assert slope==expected
    assert rank(C+mul(C,T))==14
    # Full fine unit-metric evolution gives the same first derivative on N.
    assert mul(mul(C,B),N)==mul(C,T)
    # Even scalar support loses the sign of the centroid port.
    port=mul(tr(h),slope)[0][0]
    assert port==-2
    return {'permutations':len(perms),'sector_permutation_checks':len(perms)*len(P),
            'sector_leakage_traces':traces,'first_refinement_trace':13,
            'mean_per_label':'13/8','new_directions':14,'instantaneous_rank':rank(C),
            'one_derivative_rank':rank(C+mul(C,T)),
            'instantaneous_null_on_new':['centroid vertex (4,)'],
            'centroid_harmonic_signed_slope':str(port),
            'fine_basis':[list(w) for w in n], 'parent_basis':[list(w) for w in s],
            'signed_centroid_slope_by_parent_coordinate':[str(row[0]) for row in slope]}


if __name__=='__main__':
    print(json.dumps(run(),indent=2))
