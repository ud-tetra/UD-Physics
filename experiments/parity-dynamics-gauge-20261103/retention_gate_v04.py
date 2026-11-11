#!/usr/bin/env python3
"""QPB1 signed-edge stroboscopic admissibility and parity closure: exact."""
import itertools, json
from collections import Counter
import sympy as S

simp = [list(itertools.combinations(range(4), k)) for k in (1, 2, 3, 4)]
labels = sum(simp, [])
ix = {t: i for i, t in enumerate(labels)}
D = S.zeros(15)
for layer in simp[1:]:
    for t in layer:
        for j in range(len(t)):
            D[ix[t[:j]+t[j+1:]], ix[t]] = (-1)**j
A = D-D.T
J = A/2
E = S.zeros(6,15)
for j in range(6):
    E[j,4+j] = 1
Q = E.col_join(E*J)
F = S.eye(15)+A/2+A**2/4
R = S.zeros(12)
for j in range(6):
    R[j,6+j] = 1
    R[6+j,j] = -1
assert D*D == S.zeros(15)
assert A**3 == -4*A
assert Q.rank() == 12
assert Q*F == R*Q
assert F.T*F == S.eye(15)
assert F**4 == S.eye(15)
section = Q.T*(Q*Q.T).inv()
assert Q*section == S.eye(12)
assert F*section == section*R
edges = list(itertools.combinations(range(4),2))
eix = {e:i for i,e in enumerate(edges)}
pairs = [(0,5),(1,4),(2,3)] # lex edges: 01,02,03,12,13,23
def theta(word):
    return sum((((((word>>i)&1)^((word>>j)&1)))<<k)
               for k,(i,j) in enumerate(pairs))
def step(q,p):
    return p,q^63
counts=Counter()
for q in range(64):
    for p in range(64):
        v = (theta(q),theta(p))
        counts[v]+=1
        q1,p1=step(q,p)
        assert (theta(q1),theta(p1))==(v[1],v[0])
assert len(counts)==64 and set(counts.values())=={64}
assert theta(0)==theta(0) and theta(1)!=theta(0)
def action(word, g):
    res=0
    for j,(a,b) in enumerate(edges):
        aa,bb=g[a],g[b]
        dest=eix[tuple(sorted((aa,bb)))]
        res |= ((((word>>j)&1) ^ int(aa>bb))<<dest)
    return res
G=list(itertools.permutations(range(4)))
for g in G:
    induced={}
    for word in range(64):
        a,c=theta(word),theta(action(word,g))
        if a in induced:
            assert induced[a]==c
        induced[a]=c
    assert len(induced)==8 and len(set(induced.values()))==8
    for q in range(64):
        for p in range(64):
            q1,p1=step(q,p)
            assert step(action(q,g),action(p,g))==(
                action(q1,g),action(p1,g))
            assert (theta(action(q1,g)),theta(action(p1,g)))==(
                induced[theta(p)],induced[theta(q)])
# Same admitted sign report but different native norm: energy cannot be
# reconstructed from any sign-only retention record.
v = section*S.ones(12,1)
assert Q*v == S.ones(12,1)
assert (2*v).dot(2*v) == 4*v.dot(v)
out = {
 "source":"QPB1 unit-metric K4 x'=Ax, A=D-D^T",
 "domain":"all 12 edge quadratures nonzero at sampled observations",
 "domain_invariant_under_strobe":True,
 "source_native_frequency":"2 angular units per dimensionless u",
 "selected_strobe":"u=pi/4; chosen observation schedule, not physical clock",
 "exact_strobe":"F=I+A/2+A^2/4",
 "edge_quadrature_rank":12,
 "full_sign_alphabet":4096,
 "theta_pair_states":64,
 "sign_words_per_theta_pair":64,
 "theta_pair_law":"(theta_q,theta_p)->(theta_p,theta_q)",
 "theta_q_only_autonomous":False,
 "theta_q_history_minimal_classes":64,
 "S4_signed_permutations":24,
 "S4_sign_pairs_tested":98304,
 "norm_not_determined_by_sign":True,
 "irreversible_retention_source":"OPEN: no action-compatible native update or source receipt",
 "physical_promotion":0,
 "checks":"PASS"
}
print(json.dumps(out,sort_keys=True,indent=2))
