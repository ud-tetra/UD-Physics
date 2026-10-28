"""Exact S4 root-selection and oriented K4 support-current symmetry audit."""

import itertools
import json

V=range(4)
E=list(itertools.combinations(V,2))
perms=list(itertools.permutations(V))


def edge_action(p,edge):
    a,b=(p[i] for i in edge)
    return tuple(sorted((a,b))), (1 if a<b else -1)


def main():
    assert len(perms)==24 and len(E)==6
    transposition_witness={}
    for e in E:
        p=list(V)
        p[e[0]],p[e[1]]=p[e[1]],p[e[0]]
        image,sgn=edge_action(p,e)
        assert image==e and sgn==-1
        transposition_witness[str(e)]=tuple(p)
    # Transitivity forces invariant vertex amplitude uniform.
    orbit={p[0] for p in perms}
    assert orbit==set(V)
    roots={i:sum(p[i]==i for p in perms) for i in V}
    assert set(roots.values())=={6}
    # A symmetric probability distribution on four candidate roots is uniform.
    root_probabilities=['1/4']*4
    # For invariant oriented edge y=0, Q166 J_ie=2 B_ie x_i y_e=0.
    current_support_nonzero=0
    print(json.dumps({'S4_order':24,'K4_oriented_edge_count':6,
                      'invariant_vertex_dimension':1,
                      'invariant_oriented_edge_dimension':0,
                      'root_orbit_size':4,'root_stabilizer_order':6,
                      'equivariant_random_root_weights':root_probabilities,
                      'symmetric_Q166_vertex_edge_current_nonzero_entries':current_support_nonzero,
                      'edge_sign_flip_witnesses':transposition_witness},
                     indent=2,sort_keys=True))


if __name__=='__main__':
    main()
