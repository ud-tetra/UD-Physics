#!/usr/bin/env python3
"""Exact Q(sqrt5) enumeration of proper icosahedral rotations via graph automorphisms.

Uses integer graph isomorphism and exact algebraic field operations. No floating
angle tolerance, no symbolic simplification or approximate classification.
"""
import json,argparse
from pathlib import Path
from itertools import product,combinations
import networkx as nx
from exact_channels import Q5,PHI,PSI,ONE,ZERO
from fractions import Fraction as F

def dot(x,y):return sum((a*b for a,b in zip(x,y)),ZERO)
def minus(x,y):return [a-b for a,b in zip(x,y)]
def matmul(a,b):return [[sum((x*y for x,y in zip(row,col)),ZERO) for col in zip(*b)] for row in a]
def trans(a):return list(map(list,zip(*a)))
def det3(m):
 a,b,c=m
 return a[0]*(b[1]*c[2]-b[2]*c[1])-a[1]*(b[0]*c[2]-b[2]*c[0])+a[2]*(b[0]*c[1]-b[1]*c[0])
def inverse3(m):
 d=det3(m);assert d!=ZERO
 a,b,c=m
 cofs=[[b[1]*c[2]-b[2]*c[1],-(b[0]*c[2]-b[2]*c[0]),b[0]*c[1]-b[1]*c[0]],
       [-(a[1]*c[2]-a[2]*c[1]),a[0]*c[2]-a[2]*c[0],-(a[0]*c[1]-a[1]*c[0])],
       [a[1]*b[2]-a[2]*b[1],-(a[0]*b[2]-a[2]*b[0]),a[0]*b[1]-a[1]*b[0]]]
 return [[x/d for x in row] for row in trans(cofs)]

def construction():
 half=Q5(F(1,2));v=[]
 for s,t in product((-1,1),repeat=2):v.append([ZERO,Q5(s)*half,Q5(t)*PHI*half])
 for s,t in product((-1,1),repeat=2):v.append([Q5(s)*half,Q5(t)*PHI*half,ZERO])
 for s,t in product((-1,1),repeat=2):v.append([Q5(s)*PHI*half,ZERO,Q5(t)*half])
 edges=[(i,j) for i,j in combinations(range(12),2) if dot(minus(v[i],v[j]),minus(v[i],v[j]))==ONE]
 assert len(edges)==30
 return v,edges

def main():
 p=argparse.ArgumentParser();p.add_argument('--out',type=Path,required=True);a=p.parse_args()
 v,edges=construction();graph=nx.Graph();graph.add_nodes_from(range(12));graph.add_edges_from(edges)
 enum=list(nx.algorithms.isomorphism.GraphMatcher(graph,graph).isomorphisms_iter());assert len(enum)==120
 # Matrix columns are dictated exactly by 3 linearly independent reference vertex rows.
 idx=(0,1,4);basis=[v[i] for i in idx];ib=inverse3(basis)
 expected={'1':(1,12,30,Q5(3)),'2':(15,0,2,Q5(-1)),'3':(20,0,0,ZERO),'5a':(12,2,0,PHI),'5b':(12,2,0,PSI)}
 group={key:[] for key in expected}
 for d in enum:
  perm=[d[i] for i in range(12)]
  target=[v[perm[i]] for i in idx]
  rt=matmul(ib,target)
  assert matmul(v,rt)==[v[i] for i in perm], 'graph auto does not preserve exact Euclidean geometry'
  assert matmul(rt,trans(rt))==[[Q5(int(i==j)) for j in range(3)] for i in range(3)]
  determinant=det3(rt)
  assert determinant==ONE or determinant==Q5(-1)
  if determinant!=ONE:continue
  tr=sum((rt[k][k] for k in range(3)),ZERO)
  fix_v=sum(perm[i]==i for i in range(12))
  fix_e=sum({perm[i],perm[j]}=={i,j} for i,j in edges)
  order=1;cur=list(range(12))
  while True:
   cur=[perm[i] for i in cur]
   if cur==list(range(12)):break
   order+=1;assert order<=5
  cls= next((k for k,(count,fv,fe,trace) in expected.items() if trace==tr and fv==fix_v and fe==fix_e),None)
  assert cls is not None
  assert order=={'1':1,'2':2,'3':3,'5a':5,'5b':5}[cls]
  group[cls].append(perm)
 assert all(len(group[key])==expected[key][0] for key in group)
 assert sum(len(q) for q in group.values())==60
 result={'status':'PASS','evidence':'EXACT','field':'Q(sqrt(5)) using rational coefficient pairs','graph_vertices':12,'graph_edges':30,'automorphisms':len(enum),'proper_rotations':60,'class_counts':{k:len(v) for k,v in group.items()},'fixed_vertices':{k:expected[k][1] for k in group},'fixed_edges':{k:expected[k][2] for k in group},'rotation_trace':{k:expected[k][3].asdict() for k in group},'methods':['construct regular icosahedron in Q(sqrt5)','enumerate 120 graph automorphisms over exact integer adjacency','solve each rotation matrix in Q(sqrt5) from three independent vertices','verify all 12 vertex actions, exact orthogonality and determinant','retain 60 determinant +1 actions; count conjugacy invariants']}
 a.out.parent.mkdir(parents=True,exist_ok=True);a.out.write_text(json.dumps(result,indent=2)+'\n');print('PASS exact 60 rotations, 5 class signatures, vertex and edge fixed counts')
if __name__=='__main__':main()
