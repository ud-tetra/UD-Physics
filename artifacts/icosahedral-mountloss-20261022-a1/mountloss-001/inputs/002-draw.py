"""Static scientific summary from saved numerical outputs; no resimulation."""
from pathlib import Path
import argparse,json,csv
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def main(out):
    report=json.loads((out/'summary.json').read_text());scan=list(csv.DictReader((out/'scan.csv').open()));rows=list(csv.DictReader((out/'campaign.csv').open()))
    fig,ax=plt.subplots(1,3,figsize=(13,4),layout='constrained')
    x=[float(r['nominal_breathing_retention']) for r in scan];y=[float(r['worst_hidden_energy_fraction_u100']) for r in scan]
    ax[0].plot(x,y,'o-',color='#23678a');ax[0].axvline(.8,color='#a55524',ls='--',lw=1);ax[0].axhline(.5,color='#a55524',ls='--',lw=1)
    for a,b,r in zip(x,y,scan):ax[0].annotate(r['nu'],(a,b),xytext=(3,5),textcoords='offset points',fontsize=8)
    selected=report['selection']['selected'];ax[0].plot(selected['nominal_breathing_retention'],selected['worst_hidden_energy_fraction_u100'],'o',ms=11,mfc='none',mec='#cd622a',mew=2)
    ax[0].set(xlabel='Nominal breathing RMS / original',ylabel='Worst hidden-sector energy fraction at u=100',title='Declared nine-strength tradeoff',xlim=(.55,1.0),ylim=(-.04,1.1));ax[0].grid(alpha=.2)
    for file,label,col in [('old-cycle-no-loss.csv','Original mount','#777777'),('old-cycle-with-loss.csv','Four-cycle, added loss','#23678a'),('worst-hidden-with-loss.csv','Worst linear phase, nonlinear run','#c0642b')]:
        data=np.genfromtxt(out/file,delimiter=',',names=True);ax[1].plot(data['u'],data['mechanical_energy_fraction'],label=label,color=col)
    ax[1].set(xlabel='Dimensionless time u',ylabel='Total mechanical energy / initial',title='Separate housing preparations',ylim=(0,1.06));ax[1].legend(fontsize=8,loc='lower left');ax[1].grid(alpha=.2)
    ret=[float(r['breathing_retention']) for r in rows];colors=['#23678a' if r['group']!='challenge' else '#c0642b' for r in rows]
    ax[2].bar(np.arange(1,len(rows)+1),ret,color=colors);ax[2].axhline(.8,color='#a55524',ls='--',lw=1)
    ax[2].axvline(20.5,color='#555555',lw=.8);ax[2].set(xlabel='Frozen case (1–20 budget; 21–24 challenge)',ylabel='Breathing RMS / original undamped',title='Selected nu=0.02, full nonlinear assembly',ylim=(0,1.05));ax[2].grid(axis='y',alpha=.2)
    fig.suptitle('UD Discovery · four-anchor housing loss · development evidence',fontsize=13)
    fig.savefig(out/'mountloss-summary.png',dpi=160);plt.close(fig)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--out',type=Path,required=True);main(p.parse_args().out)
