"""Render finite pulse comparisons; these bars are not continuous-box bounds."""
from pathlib import Path
import argparse
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def main(summary,baseline,output):
    data=json.loads(summary.read_text());rows=[r for r in data['pulse_scan'] if r['gamma']==.5]
    # Prior source campaign, same corner sets, preparation and time window.
    prior=[100*r['maximum_leakage_0_100'] for r in json.loads(baseline.read_text())['corner_scan']]
    x=np.arange(4);width=.35
    plt.rcParams.update({'font.size':11,'axes.spines.top':False,'axes.spines.right':False})
    fig,ax=plt.subplots(1,2,figsize=(11,4.7),layout='constrained')
    ax[0].bar(x-width/2,prior,width,label='Undamped',color='#b9c4cf')
    values=[100*r['max_volume_leakage'] for r in rows]
    bars=ax[0].bar(x+width/2,values,width,label=r'Difference damping $\gamma=1/2$',color='#007f87')
    ax[0].bar_label(bars,fmt='%.2f',padding=3,fontsize=9)
    ax[0].set(ylabel='Maximum nonuniform volume signal (%)',title='Unequal motion is suppressed',ylim=(0,46))
    retention=[100*r['min_mean_rms_retention'] for r in rows]
    bars=ax[1].bar(x,retention,.55,color='#245ea2');ax[1].bar_label(bars,fmt='%.1f',padding=3)
    ax[1].set(ylabel='Minimum mean-volume RMS retained (%)',title='Breathing remains measurable',ylim=(0,112))
    ax[0].legend(frameon=False,fontsize=9,loc='upper left')
    for a in ax:
        a.set_xticks(x,['±1%','±5%','±10%','±20%']);a.set_xlabel('Spoke stiffness and outer inertia variation')
        a.grid(axis='y',alpha=.15);a.set_axisbelow(True)
    fig.suptitle('Hypothetical heart–shell model: passive outer-edge damping',fontsize=15)
    fig.supxlabel('256 corners per variation level; heart pulse a(0)=0.1; u=0…100. Signal norms, not energy fractions.',fontsize=10)
    fig.savefig(output,dpi=180);plt.close(fig)


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--summary',type=Path,required=True);p.add_argument('--baseline',type=Path,required=True);p.add_argument('--out',type=Path,required=True)
    args=p.parse_args();main(args.summary,args.baseline,args.out)
