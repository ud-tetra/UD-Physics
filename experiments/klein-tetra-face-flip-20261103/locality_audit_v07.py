#!/usr/bin/env python3
"""Exact v0.7 support audit of v0.6 integer P/S. Run beside extracted v0.6 ZIP scripts."""
import runpy,contextlib,io,json,collections
from pathlib import Path
P=Path(__file__).resolve().parent
with contextlib.redirect_stdout(io.StringIO()):
 z=runpy.run_path(str(P/'full_integral_bridge_v06.py'))
 s=runpy.run_path(str(P/'twisted_cover_source_v06.py'))
F=z['Sfin'];Q=z['Pfin'];rep=s['rep'];uf=s['uf'];simp=s['simp']
lookup=[]
for k in range(4):
 d={}
 for flag in simp[k]:
  for sheet in (0,1):d.setdefault(uf[k].root((sheet,flag)),(sheet,flag))
 lookup.append(d)
vv_index={frozenset(x):i for i,x in enumerate(rep[0])}
def vertex(sheet,flag):
 a=uf[0].root((sheet,(flag,)))
 bb=uf[0].root((1-sheet,(flag,)))
 return vv_index[frozenset((a,bb))]
cells=[]
for k in range(4):
 row=[]
 for a,_ in rep[k]:
  sheet,flag=lookup[k][a]
  row.append(frozenset(vertex(sheet,v) for v in flag))
 cells.append(row)
graph=[set() for _ in range(18)]
for e in cells[1]:
 assert len(e)==2
 a,b=e;graph[a].add(b);graph[b].add(a)
dist=[]
for v in range(18):
 ds={v:0};todo=collections.deque([v])
 while todo:
  a=todo.popleft()
  for w in graph[a]:
   if w not in ds:ds[w]=ds[a]+1;todo.append(w)
 assert len(ds)==18
 dist.append(ds)
rows=[]
for k in range(4):
 vals=[]
 for i,j,q in Q[k].row_list():
  if not q:continue
  source=cells[k][j]
  target=set().union(*(cells[k][a] for a in range(F[k].rows) if F[k][a,i]))
  pair=[dist[a][c] for a in source for c in target]
  haus=max(max(min(dist[a][c] for a in source) for c in target),
           max(min(dist[a][c] for c in target) for a in source))
  vals.append((min(pair),max(pair),haus,abs(int(q))))
 def hist(j):return dict(sorted(collections.Counter(x[j] for x in vals).items()))
 rows.append({'degree':k,'P_nonzero_count':len(vals),
              'minimum_distance_histogram':hist(0),
              'maximum_pair_distance_histogram':hist(1),
              'Hausdorff_distance_histogram':hist(2),
              'largest_absolute_coefficient':max(x[3] for x in vals)})
assert [r['P_nonzero_count'] for r in rows]==[18,181,50,1]
assert max(max(r['maximum_pair_distance_histogram']) for r in rows)==2
print(json.dumps({'vertex_graph_diameter':max(max(d.values()) for d in dist),
'result':rows,'scope':'one finite 72-tetrahedron complex; not uniform in refinement',
'status':'PASS_EXACT'},indent=2,sort_keys=True))
