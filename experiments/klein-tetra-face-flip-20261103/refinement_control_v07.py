#!/usr/bin/env python3
"""Exact refinement-hop obstruction for endpoint-anchored integral retractions."""
import json
rows=[]
for m in (2,4,8,16,32,64):
 labels=[int(i>m//2) for i in range(m+1)]
 assert labels[0]==0 and labels[-1]==1
 # P0 maps refined vertices to one original endpoint, P1 on a refined
 # edge is the change of its endpoint label times the coarse edge.
 edge=[labels[i]-labels[i-1] for i in range(1,m+1)]
 assert sum(edge)==1
 actual=max(i if labels[i]==0 else m-i for i in range(m+1))
 unavoidable=max(min(i,m-i) for i in range(m+1))
 assert actual==unavoidable==m//2
 rows.append({'refined_edges':m,'necessary_radius_lower_bound':unavoidable,
              'constructive_radius':actual,'nonzero_coarse_edge_images':sum(bool(x) for x in edge)})
print(json.dumps({
 'hypotheses':'subdivided interval with original two endpoints retained as target; integral P0 augmentation preserving, fixed endpoints',
 'theorem':'every source vertex image has nonzero coefficient at one endpoint, so max fine graph-hop radius >= floor(m/2)',
 'samples':rows,'no_uniform_refined_graph_hop_bound':True,
 'limitations':'not a physical metric, not a no-go for coarse-cell locality or multiscale packet operators',
 'status':'PASS_EXACT'},indent=2,sort_keys=True))
