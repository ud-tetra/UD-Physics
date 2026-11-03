#!/usr/bin/env python3
"""Exact short-loop and directional selector audit on finite honeycomb quotients."""
import json
from collections import Counter, deque
from fractions import Fraction

U = ((1, 1), (-1, 1), (0, -2))


def carrier(m, n):
    N = m*m + m*n + n*n
    shifts = (0, m+n, n)
    edges = [(r, N+(r-shifts[t]) % N, t) for t in range(3) for r in range(N)]
    adjacency = [set() for _ in range(2*N)]
    lookup = {}
    for index, (a, b, _) in enumerate(edges):
        adjacency[a].add(b)
        adjacency[b].add(a)
        lookup[frozenset((a, b))] = index
    faces = [[(t*N+site % N, sign) for t, site, sign in
              ((0,r,1),(1,r+shifts[1],-1),(2,r+shifts[1],1),
               (0,r+shifts[1]-shifts[2],-1),
               (1,r+shifts[1]-shifts[2],1),(2,r,-1))]
             for r in range(N)]
    return N, edges, adjacency, lookup, faces


def rooted_layers(adjacency, root):
    dist = {root: 0}
    queue = deque([root])
    while queue:
        v = queue.popleft()
        for w in adjacency[v]:
            if w not in dist:
                dist[w] = dist[v]+1
                queue.append(w)
    return [sum(d == level for d in dist.values()) for level in range(max(dist.values())+1)]


def cycles6(adjacency):
    # A simple 6-cycle is canonically represented by its minimum vertex and
    # lexicographically smaller traversal direction.
    found = set()
    for root in range(len(adjacency)):
        def walk(path):
            if len(path) == 6:
                if root in adjacency[path[-1]]:
                    found.add(min(tuple(path), tuple([root]+list(reversed(path[1:])))))
                return
            for nxt in adjacency[path[-1]]:
                if nxt > root and nxt not in path:
                    walk(path+[nxt])
        walk([root])
    return sorted(found)


def harmonic_pairing(cycle, edges, lookup):
    out = [0, 0]
    for a, b in zip(cycle, cycle[1:]+cycle[:1]):
        idx = lookup[frozenset((a, b))]
        edge_a, edge_b, t = edges[idx]
        sign = 1 if (a, b) == (edge_a, edge_b) else -1
        out[0] += sign*U[t][0]
        out[1] += sign*U[t][1]
    return tuple(out)


def direction_selector(dx, dy):
    scores = (dx+dy, -dx+dy, -2*dy)
    top = max(scores)
    winners = [t for t, score in enumerate(scores) if score == top]
    return winners[0] if len(winners) == 1 else None


def three_step_count(adjacency, root):
    # Independent of cycle enumeration: two distinct root-to-v length-3 paths
    # form one six-cycle when the graph has no four-cycles.
    path_counts = Counter()
    for a in adjacency[root]:
        for b in adjacency[a] - {root}:
            for c in adjacency[b] - {a, root}:
                path_counts[c] += 1
    return sum(k*(k-1)//2 for k in path_counts.values())


def audit(m, n):
    N, edges, adj, lookup, faces = carrier(m, n)
    cycles = cycles6(adj)
    face_sets = {frozenset(idx for idx, _ in face) for face in faces}
    assert len(face_sets) == N
    face_cycles = []
    other_cycles = []
    for cycle in cycles:
        cycle_edges = frozenset(lookup[frozenset((a, b))]
                                for a, b in zip(cycle, cycle[1:]+cycle[:1]))
        (face_cycles if cycle_edges in face_sets else other_cycles).append(cycle)
    assert len(face_cycles) == N
    assert all(harmonic_pairing(c, edges, lookup) == (0, 0) for c in face_cycles)
    pairings = Counter(harmonic_pairing(c, edges, lookup) for c in other_cycles)
    assert all(p != (0, 0) for p in pairings)  # proves these are not face boundaries
    root_cycles = sum(0 in c for c in cycles)
    assert all(sum(root in c for c in cycles) == root_cycles for root in range(2*N))
    if (m,n) != (2,2):
        assert all(three_step_count(adj, root) == root_cycles for root in range(2*N))
    assert 6*len(cycles) == 2*N*root_cycles
    if N in (7,13,19,21):
        assert all(rooted_layers(adj, root)[:3] == [1, 3, 6] for root in range(2*N))
    return dict(m=m,n=n,N=N,layers=rooted_layers(adj,0),six_cycles=len(cycles),
                faces=len(face_cycles),extra=len(other_cycles),through_root=root_cycles,
                extra_pairings={str(k):v for k,v in sorted(pairings.items())})


if __name__ == '__main__':
    rows = [audit(m,n) for m,n in ((2,1),(3,1),(3,2),(4,1),(4,2),(2,2))]
    assert [row['extra'] for row in rows[:3]] == [21,0,0]
    assert [row['through_root'] for row in rows[:3]] == [12,3,3]
    assert [direction_selector(*d) for d in ((1,0),(0,1),(0,-1),(0,0))] == [0,None,2,None]
    # The order-three action on the registered native direction: R^3=I,
    # R^T diag(2,6) R=diag(2,6), and u_t R=u_(t-1 mod 3).
    R = ((Fraction(-1,2),Fraction(-3,2)),
         (Fraction(1,2),Fraction(-1,2)))
    def matmul(A,B):
        return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2))
                           for j in range(2)) for i in range(2))
    assert matmul(matmul(R,R),R) == ((1,0),(0,1))
    assert tuple(tuple(sum(R[k][i]*(2 if k==0 else 6)*R[k][j] for k in range(2))
                       for j in range(2)) for i in range(2)) == ((2,0),(0,6))
    assert all(tuple(sum(U[t][k]*R[k][j] for k in range(2)) for j in range(2))
               == U[(t-1)%3] for t in range(3))
    for dx,dy in ((1,0),(1,1),(2,-1),(-3,4),(-2,-1)):
        dnew = tuple(sum(R[j][i]*(dx,dy)[i] for i in range(2)) for j in range(2))
        chosen = direction_selector(dx,dy)
        if chosen is not None:
            assert direction_selector(*dnew) == (chosen+1)%3
    for N in (7,13,19):
        assert [tuple(Fraction(v, (2 if j==0 else 6)*N) for j,v in enumerate(U[t]))
                for t in range(3)] == [
                    (Fraction(1,2*N),Fraction(1,6*N)),
                    (Fraction(-1,2*N),Fraction(1,6*N)),
                    (Fraction(0),Fraction(-1,3*N))]
    print(json.dumps({'source_base':'b7d3205d59256335bbd78a91dbd596ed485573fc',
                      'quotients':rows},indent=2,sort_keys=True))
