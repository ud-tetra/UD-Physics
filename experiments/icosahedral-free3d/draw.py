"""Scientific summary of exact mode count and finite free3D probes."""
from pathlib import Path
import argparse
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def main(source,out):
    s=json.loads(source.read_text())
    fig,ax=plt.subplots(2,2,figsize=(11.6,7.4),layout='constrained')
    values=s['equilibrium']['eigenvalues_numerical']
    ax[0,0].plot(np.arange(1,41),values,'o',ms=4,color='#265f8b')
    ax[0,0].axhline(0,color='grey',lw=.6)
    ax[0,0].set(title='Equilibrium: 6 rigid + 34 restoring modes',xlabel='Sorted mode',ylabel='Squared frequency (model units)')
    r=s['variational']['records'];tt=[0]+[x['u'] for x in r];gain=[1]+[x['maximum_reference_energy_amplitude_gain'] for x in r]
    ax[0,1].plot(tt,gain,'o-',color='#7d3d87')
    ax[0,1].axhline(1,color='grey',ls='--',lw=.8)
    ax[0,1].set(title='Transverse gain at five checkpoints',xlabel='Dimensionless u',ylabel='Reference energy amplitude gain',ylim=(.95,1.4))
    props=[[x for x in s['campaign'] if x['campaign']=='seeded_material_properties' and x['epsilon']==ep] for ep in [.01,.05]]
    x=np.arange(2);width=.32
    ax[1,0].bar(x-width/2,[100*max(r['volume_signal_leakage'] for r in p) for p in props],width,label='Cells about moving hub',color='#7d3d87')
    ax[1,0].bar(x+width/2,[100*max(r['shell_centroid_volume_signal_leakage'] for r in p) for p in props],width,label='Cells about shell mean centre',color='#5ab0b3')
    ax[1,0].set(title='Maximum nonuniform volume signal',ylabel='Signal amplitude fraction (%)',xticks=x,xticklabels=['±1%','±5%'],ylim=(0,22))
    ax[1,0].legend(frameon=False,fontsize=9)
    retained=[100*min(r['mean_volume_rms_retention'] for r in p) for p in props]
    bars=ax[1,1].bar(x,retained,.45,color='#16878d');ax[1,1].bar_label(bars,fmt='%.2f',padding=3)
    ax[1,1].set(title='Minimum mean-volume response retained',ylabel='RMS versus symmetric baseline (%)',xticks=x,xticklabels=['±1%','±5%'],ylim=(0,112))
    for a in ax.ravel():a.spines[['top','right']].set_visible(False);a.grid(axis='y',alpha=.14);a.set_axisbelow(True)
    fig.suptitle('Icosahedral breathing without radial guides',fontsize=17)
    fig.supxlabel('40 coordinates; free hub and shell. Property panels: 8 seeded probes per tolerance, u=0…100; finite observations.',fontsize=10)
    fig.savefig(out,dpi=180);plt.close(fig)


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--summary',type=Path,required=True);p.add_argument('--out',type=Path,required=True)
    a=p.parse_args();main(a.summary,a.out)
