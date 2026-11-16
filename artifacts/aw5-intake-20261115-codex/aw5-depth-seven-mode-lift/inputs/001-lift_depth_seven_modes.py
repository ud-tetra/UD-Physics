"""Lift the two depth-seven constant-terminal poles in coherent top-cell signs."""
from collections import defaultdict
from itertools import combinations

from mpmath import iv
import numpy as np
from scipy.sparse import coo_matrix, eye
from scipy.sparse.csgraph import connected_components, shortest_path

from depth_seven_modes import DEPTH, dual_terminal, pole_bracket


def lift(z):
    ports = np.ones((1,4))
    for depth in range(DEPTH,1,-1):
        c,a = dual_terminal(z,depth-1)
        b = (c-a)/4
        avg = ports.mean(axis=1,keepdims=True)
        totals = avg/(1+3*b/(a-1))+(ports-avg)/(1+b*(3*a-1)/(a*a-1))
        children = []
        for i in range(4):
            child = [-b*(a*totals[:,i]+totals[:,j])/(a*a-1)
                     for j in range(4) if j != i]
            children.append(np.column_stack([*child,ports[:,i]]))
        ports = np.stack(children,axis=1).reshape(-1,4)
    return ports.ravel()


def graph():
    generations = [[(0,1,2,3)]]
    vertex = 4
    for _ in range(DEPTH):
        children = []
        for cell in generations[-1]:
            children.extend(cell[:i]+cell[i+1:]+(vertex,) for i in range(4))
            vertex += 1
        generations.append(children)
    cells = generations[-1]
    faces = defaultdict(list)
    for i,cell in enumerate(cells):
        for face in combinations(cell,3):
            faces[face].append(i)
    pairs,terminal = [], []
    for face,owners in faces.items():
        assert len(owners) in (1,2)
        if len(owners)==2:
            a,b=owners
            pairs.extend([(a,b),(b,a)])
        else:
            assert all(v<4 for v in face)
            terminal.append(owners[0])
    rows,cols = zip(*pairs)
    adjacency = coo_matrix((np.ones(len(rows)),(rows,cols)),shape=(len(cells),)*2).tocsr()
    assert len(terminal)==4 and connected_components(adjacency,directed=False)[0]==1
    return generations,adjacency,terminal


def orbit_error(generations,x):
    error = 0.0
    indices = {t:i for i,t in enumerate(generations[-1])}
    for j in range(3):
        mapping = dict(enumerate(range(4)))
        mapping[j],mapping[j+1] = j+1,j
        vertex=4
        for cells in generations[:-1]:
            centers = {t:vertex+i for i,t in enumerate(cells)}
            for t in cells:
                mapping[centers[t]] = centers[tuple(sorted(mapping[v] for v in t))]
            vertex += len(cells)
        moved=[indices[tuple(sorted(mapping[v] for v in t))] for t in generations[-1]]
        error=max(error,np.linalg.norm(x[moved]-x)/np.linalg.norm(x))
    return error


def measure(label,a,b,generations,adjacency,terminals,distance):
    omega, mass, _ = pole_bracket(0, a, b)
    lam = float(omega.mid)**2
    x = lift(-lam)
    assert np.max(abs(x[terminals]-1)) < 1e-12
    x /= np.linalg.norm(x)
    terminal_mass = float(np.sum(x[terminals]) ** 2 / (4 * lam))
    assert abs(terminal_mass - float(mass.mid)) < 1e-8
    residual=np.linalg.norm((4*eye(len(x))-adjacency)@x-lam*x)
    symmetry=orbit_error(generations,x)
    assert max(residual,symmetry)<1e-9
    counts=np.bincount(distance)
    shell_average=np.bincount(distance,weights=x)/counts
    radial=np.dot(counts,shell_average**2)
    angular=np.linalg.norm(x-shell_average[distance])**2
    assert abs(radial+angular-1)<1e-12
    averages = []
    for level in range(DEPTH + 1):
        blocks = x.reshape(4**level, -1)
        block_means = blocks.mean(axis=1)
        averages.append(float(blocks.shape[1] * np.dot(block_means, block_means)))
    details=np.diff(averages)
    domains=[connected_components(adjacency[mask][:,mask],directed=False)[0]
             if np.any(mask) else 0 for mask in (x>0,x<0)]
    print(f"{label}: eigen residual {residual:.3e}; S4 generator residual {symmetry:.3e}; "
          f"minimum absolute amplitude {min(abs(x)):.6e}")
    print(f"  face spectral mass from lift {terminal_mass:.12f}")
    print(f"  shell norm share {radial:.9f}; within-shell share {angular:.9f}; "
          f"shell/non-shell ratio {radial/angular:.9f}")
    print(f"  global mean share {averages[0]:.9f}; level detail "
          + ", ".join(f"{max(0.0,d):.9f}" for d in details))
    print(f"  positive/negative nodal domains {domains}; negative norm share {np.dot(x[x<0],x[x<0]):.9f}")


def main():
    iv.dps = 45
    generations,adjacency,terminals=graph()
    distance=shortest_path(adjacency,directed=False,indices=terminals,unweighted=True).min(axis=0).astype(int)
    print(f"{adjacency.shape[0]} top cells; {distance.max()+1} terminal-distance shells")
    measure("A","0.00648","0.00652",generations,adjacency,terminals,distance)
    measure("B","0.02996","0.03001",generations,adjacency,terminals,distance)


if __name__=="__main__":
    main()
