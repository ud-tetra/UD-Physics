"""Scientific overview:joint tolerance probes,module bound,and housing counterexample."""
from pathlib import Path
import argparse,csv,json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def main(source,out):
    rows=list(csv.DictReader((source/'campaign.csv').open()));curve=list(csv.DictReader((source/'mount-mode-curve.csv').open()));bounds=json.loads((source/'bounds.json').read_text())
    fig,ax=plt.subplots(1,3,figsize=(14,4.7),layout='constrained')
    groups=['boundary','interior','challenge']
    for i,g in enumerate(groups):
        rr=[r for r in rows if r['group']==g]
        ax[0].scatter(np.full(len(rr),i)+np.linspace(-.12,.12,len(rr)),[100*float(r['mean_volume_rms_vs_original_undamped']) for r in rr],s=28,color=['#237f78','#4476a6','#b75a45'][i])
    ax[0].axhline(80,color='grey',ls=':',lw=1);ax[0].set_xticks(range(3),['Budget boundary','Budget interior','Challenges'],rotation=20,ha='right')
    ax[0].set(ylabel='Mean-volume RMS retained (%)',title='Prepared joint probes: 20/20 budget passes',ylim=(65,101));ax[0].grid(axis='y',alpha=.2)
    om=np.linspace(1,4,301);Z=5*(2j*om+5)/(50-2*om*om+5j*om);delta=-.01;cf=.001
    ratio=(delta*delta*Z.real+cf/5)/((1+delta/2)**2*Z.real+cf/20)
    ax[1].plot(om,100*ratio,color='#237f78');ax[1].axhline(100*bounds['module']['dissipative_diagonal_ratio_approx'],color='#b75a45',ls=':',label='Exact uniform upper bound')
    ax[1].set(xlabel='Dimensionless angular frequency',ylabel='Common / differential dissipation (%)',title='Declared bare-module error budget');ax[1].legend(fontsize=8);ax[1].grid(alpha=.2)
    t=np.array([float(r['u']) for r in curve]);measured=np.array([float(r['measured_housing_mode']) for r in curve]);analytic=np.array([float(r['analytic_housing_mode']) for r in curve]);keep=t<=2
    ax[2].plot(t[keep],measured[keep]*1e4,color='#b75a45',label='Full 560-phase housing mode');ax[2].plot(t[keep],analytic[keep]*1e4,color='#333333',ls=':',lw=1,label='Exact undamped harmonic')
    ax[2].set(xlabel='Dimensionless time u',ylabel='Housing displacement / 1e-4',title='54 housing modes remain undamped');ax[2].legend(fontsize=8,loc='lower left');ax[2].grid(alpha=.2)
    fig.suptitle('Joint tolerance study: coherent breathing with an unresolved housing sector',fontsize=13)
    fig.savefig(out,dpi=160);plt.close(fig)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--source',type=Path,required=True);p.add_argument('--out',type=Path,required=True);a=p.parse_args();main(a.source,a.out)
