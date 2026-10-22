"""Scientific plot from captured numerical tables; no generated illustration."""
from pathlib import Path
import argparse,csv,json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def main(source,out):
    s=json.loads((source/'summary.json').read_text())
    rows=list(csv.DictReader((source/'design-scan.csv').open()));campaign=list(csv.DictReader((source/'campaign.csv').open()))
    fig,ax=plt.subplots(1,2,figsize=(11,4.5),layout='constrained')
    for cs,color in [(0,'#246a8e'),(.005,'#de953b'),(.02,'#a94f71')]:
        r=[x for x in rows if float(x['cs'])==cs]
        ax[0].plot([float(x['soft_envelope_at_100']) for x in r],[float(x['mean_volume_rms_retention']) for x in r],color=color,label=f'spoke c_s={cs:g}')
    ax[0].axvspan(0,.5,color='#9bbf9b',alpha=.16);ax[0].axhspan(.8,1.02,color='#9bbf9b',alpha=.16)
    ax[0].axvline(.5,color='grey',ls=':',lw=1);ax[0].axhline(.8,color='grey',ls=':',lw=1)
    ax[0].set(xlabel='Soft linear mode envelope at u=100',ylabel='Collective mean-volume RMS retained (u 0–100)',xlim=(0,1.02),ylim=(.35,1.02),title='Specified 80% / 50% screen: 0 of 363 grid points')
    ax[0].legend(fontsize=8,loc='lower right')
    labels=['No loss','Edge .005','Edge .02','Spoke .02 + edge .02']
    for i,(cs,ce) in enumerate([(0,0),(0,.005),(0,.02),(.02,.02)]):
        r=[x for x in campaign if float(x['cs'])==cs and float(x['ce'])==ce]
        for j,A0 in enumerate([.025,.1,.2]):
            rr=[x for x in r if float(x['amplitude'])==A0]
            ax[1].scatter([i+(j-1)*.12]*len(rr),[100*float(x['volume_signal_leakage']) for x in rr],s=27,marker=['o','s','^'][j],color=['#246a8e','#de953b','#a94f71'][j],label=f'A0={A0:g}' if i==0 else None)
    ax[1].set_xticks(range(4),labels,rotation=17,ha='right')
    ax[1].set(ylabel='Hub-relative volume-signal mismatch (%)',title='Finite free3D probes:3 property points ×3 amplitudes')
    ax[1].legend(fontsize=8)
    for a in ax:a.grid(alpha=.18)
    fig.suptitle('Icosahedral centre cone: ordinary passive axial losses',fontsize=13)
    fig.savefig(out,dpi=170);plt.close(fig)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--source',type=Path,required=True);p.add_argument('--out',type=Path,required=True);a=p.parse_args();main(a.source,a.out)
