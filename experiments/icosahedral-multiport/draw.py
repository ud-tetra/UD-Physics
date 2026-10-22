"""Scientific plot comparing exposed development designs and finite port dynamics."""
from pathlib import Path
import argparse,csv,json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def main(source,out):
    old=list(csv.DictReader((Path(__file__).resolve().parents[2]/'artifacts/icosahedral-damping-20261022-a1/damping-001/files/campaign.csv').open()))
    a=list(csv.DictReader((source/'campaign.csv').open()));b=list(csv.DictReader((source/'readout-campaign.csv').open()));freq=list(csv.DictReader((source/'frequency.csv').open()))
    fig,ax=plt.subplots(1,3,figsize=(14,4.8),layout='constrained')
    for i,(label,rows) in enumerate([('No loss',[r for r in old if float(r['cs'])==float(r['ce'])==0]),('Ordinary loss',[r for r in old if float(r['cs'])==float(r['ce'])==.02]),('Difference A',a),('Difference B',b)]):
        leak=[100*float(r['volume_signal_leakage']) for r in rows];ret=[100*float(r.get('mean_volume_rms_retention',1)) for r in rows]
        ax[0].scatter([i]*len(leak),leak,s=26,color=['#777777','#a45b4d','#d99537','#247d75'][i],alpha=.75)
        ax[1].scatter([i]*len(ret),ret,s=26,color=['#777777','#a45b4d','#d99537','#247d75'][i],alpha=.75)
    for aplot in ax[:2]:
        aplot.set_xticks(range(4),['No loss','Ordinary','Difference A','Difference B'],rotation=22,ha='right');aplot.grid(axis='y',alpha=.2)
    ax[0].axhline(5,color='grey',ls=':',lw=1);ax[0].set(ylabel='Hub-relative volume mismatch (%)',title='Nine exposed nonlinear preparations')
    ax[1].axhline(80,color='grey',ls=':',lw=1);ax[1].set(ylabel='Matched mean-volume RMS retained (%)',title='Breathing signal retained over u 0–100',ylim=(60,103))
    for label,color in [('A','#d99537'),('B','#247d75')]:
        rr=[r for r in freq if r['phase']==label];ax[2].loglog([float(r['omega']) for r in rr],[float(r['real_force_over_velocity']) for r in rr],color=color,label=f'Design {label}')
    for om in [np.sqrt(8-np.sqrt(37)),np.sqrt(8+np.sqrt(37))]:ax[2].axvline(om,color='grey',ls=':',lw=1)
    ax[2].set(xlabel='Dimensionless angular frequency',ylabel='Dissipative part of force / velocity',title='Finite spring–inerter–damper port');ax[2].legend();ax[2].grid(alpha=.15)
    fig.suptitle('Passive differential network: exact ideal protection, finite design tests',fontsize=13)
    fig.savefig(out,dpi=160);plt.close(fig)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--source',type=Path,required=True);p.add_argument('--out',type=Path,required=True);a=p.parse_args();main(a.source,a.out)
