"""Compare two distinct coupling models, without identifying their energies."""
from pathlib import Path
import argparse
import csv
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def main(source,out):
    with source.open() as stream:
        rows=list(csv.DictReader(stream))
    def column(name):return np.array([float(r[name]) for r in rows])
    t=column('u');selected=t<=20
    chain=20*(column('chain_g_half_cell')**2+column('chain_g_half_surface')**2)
    volume=100*(column('mechanical_total_volume_ratio')-1)
    fig,axes=plt.subplots(2,1,figsize=(10,6.2),layout='constrained',sharex=True)
    axes[0].plot(t[selected],100*chain[selected],color='#7b3f85',lw=1.6)
    axes[0].axhline(100*5/17,color='#7b3f85',ls='--',alpha=.6,label='Exact maximum 5/17')
    axes[0].set(title='Oriented chain coupling: proper rotations retained',ylabel='Cell + surface model energy (%)',ylim=(0,34))
    axes[0].legend(frameon=False,fontsize=9)
    axes[1].plot(t[selected],volume[selected],color='#087e8b',lw=1.7)
    axes[1].axhline(0,color='grey',lw=.6)
    axes[1].set(title='Separate passive strain model: all 120 spatial symmetries retained',ylabel='Total geometric volume change (%)',xlabel='Dimensionless model parameter u')
    for a in axes:a.spines[['top','right']].set_visible(False);a.grid(alpha=.15)
    fig.suptitle('Icosahedral centre-to-shell coupling: two explicit constructions',fontsize=14)
    fig.supxlabel('Different state spaces: chain seed = 1, coupling = 1/2; mechanical heart strain = 0.1, g = 1, edge k = 2/5.',fontsize=9)
    fig.savefig(out,dpi=180);plt.close(fig)


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--data',type=Path,required=True);p.add_argument('--out',type=Path,required=True)
    a=p.parse_args();main(a.data,a.out)
