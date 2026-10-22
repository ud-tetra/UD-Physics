"""Exact-coordinate mathematical schematic; rendering uses matplotlib/numpy."""
from pathlib import Path
from itertools import combinations
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

here=Path(__file__).resolve().parent
v=np.array([(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1),(0,0,0)],dtype=float)
colors=['#4477AA','#EE7733','#228833','#AA3377']
tops=[tuple(j for j in range(4) if j!=i)+(4,) for i in range(4)]
fig=plt.figure(figsize=(11,4.9),layout='constrained')
for panel,explode in enumerate([False,True],start=1):
 ax=fig.add_subplot(1,2,panel,projection='3d')
 if not explode:
  for i,t in enumerate(tops):
   face=[j for j in t if j!=4]
   ax.add_collection3d(Poly3DCollection([v[face]],facecolor=colors[i],alpha=.16,edgecolor=colors[i],linewidth=.8))
  for a,b in combinations(range(4),2):ax.plot(*v[[a,b]].T,color='#39424E',lw=1.1)
  for a in range(4):ax.plot(*v[[a,4]].T,color='#AA3377',lw=1.6)
  ax.scatter(*v[4],color='#AA3377',s=38,depthshade=False)
  ax.text(.08,.02,.08,'G',fontsize=11,weight='bold')
  for i in range(4):ax.text(*(v[i]*1.12),f'v{i}',fontsize=11)
 else:
  for i,t in enumerate(tops):
   shift=v[list(t)].mean(axis=0)*1.35
   coords=v+shift
   for face in combinations(t,3):
    outer=4 not in face
    ax.add_collection3d(Poly3DCollection([coords[list(face)]],facecolor=colors[i],alpha=.3 if outer else .08,edgecolor=colors[i],linewidth=1.2 if outer else .7))
   ax.scatter(*coords[4],s=17,color=colors[i],depthshade=False)
   ax.text(*(coords[list(t)].mean(axis=0)+np.array([0,0,.15])),f'T{i}',fontsize=11)
 ax.set_xlim(-1.9,1.9);ax.set_ylim(-1.9,1.9);ax.set_zlim(-1.9,1.9)
 ax.set_box_aspect([1,1,1]);ax.view_init(elev=19,azim=29);ax.set_axis_off()
 ax.set_title('Centre split: four cells fill one tetrahedron' if not explode else 'Exploded view: one outer face per cell',fontsize=12,pad=2)
fig.text(.5,.025,'G is the common centre. The exploded view separates shared faces for visibility.',ha='center',fontsize=10,color='#39424E')
fig.savefig(here/'four-cell-tetrahedron.png',dpi=180,bbox_inches='tight',facecolor='white')
fig.savefig(here/'four-cell-tetrahedron.svg',bbox_inches='tight',facecolor='white')
