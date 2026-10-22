"""Coordinate-derived scientific illustration; primal and cell dual kept separate."""
from pathlib import Path
import argparse
import importlib.util
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection


def main(out):
    spec=importlib.util.spec_from_file_location('audit',Path(__file__).with_name('analyze.py'))
    module=importlib.util.module_from_spec(spec)
    # dataclass resolves its module via sys.modules.
    import sys
    sys.modules[spec.name]=module;spec.loader.exec_module(module)
    vertices,edges,faces,cells,_,_=module.construction()
    v=np.array([[float(x) for x in p] for p in vertices]);centres=np.array([v[list(f)].mean(axis=0) for f in faces])
    fig=plt.figure(figsize=(11,5.4),layout='constrained');ax=fig.add_subplot(121,projection='3d');dual=fig.add_subplot(122,projection='3d')
    for i,j in edges:ax.plot(*v[[i,j]].T,color='#234b73',lw=1.2,alpha=.8)
    for i in range(1,13):ax.plot(*v[[0,i]].T,color='#d0761d',lw=.9,alpha=.65)
    cell=cells[0]
    from itertools import combinations
    ax.add_collection3d(Poly3DCollection([v[list(f)] for f in combinations(cell,3)],facecolor='#32a9c2',alpha=.16,edgecolor='none'))
    ax.scatter(*v[1:].T,s=22,color='#234b73');ax.scatter(*v[0],s=65,color='#d0761d',depthshade=False);ax.text(0,0,.12,'centre',color='#985213',fontsize=10)
    for i in range(20):
        for j in range(i+1,20):
            if len(set(cells[i])&set(cells[j]))==3:dual.plot(*centres[[i,j]].T,color='#7a3f83',lw=1.4,alpha=.8)
    dual.scatter(*centres.T,s=32,color='#7a3f83',depthshade=False)
    ax.set_title('Primal cone: 13 vertices, 42 edges\nOne of 20 tetrahedra highlighted',fontsize=12)
    dual.set_title('Cell adjacency: dodecahedral graph\n20 cells, 30 shared interfaces, degree 3',fontsize=12)
    for a in [ax,dual]:
        a.set_box_aspect((1,1,1));a.view_init(elev=18,azim=27);a.set_axis_off();a.set_proj_type('ortho')
    fig.suptitle('Icosahedron coned from its centre',fontsize=17)
    fig.supxlabel('Exact coordinate construction; the central primal vertex is not a node of the cell-adjacency graph.',fontsize=10)
    fig.savefig(out,dpi=180);plt.close(fig)


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--out',type=Path,required=True);main(p.parse_args().out)
