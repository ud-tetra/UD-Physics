"""Static scientific figure from the saved joint-window results."""
from pathlib import Path
import argparse,csv,json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def main(out):
    rows=list(csv.DictReader((out/'linear.csv').open()));summary=json.loads((out/'summary.json').read_text())
    x=np.linspace(.04,.05,501);housing=[];breathing=[]
    for id in dict.fromkeys(r['id'] for r in rows):
        group=[r for r in rows if r['id']==id]
        h=[];b=[]
        for r in group:
            delta=abs(x-float(r['nu']));h.append((np.sqrt(float(r['worst_housing_energy_fraction']))+1e-6+100*float(r['strength_generator_norm'])*delta)**2)
            b.append((float(r['linear_pulse_rms'])-float(r['all_phase_readout_rms_bound'])-1e-6-float(r['breathing_rms_lipschitz_bound'])*delta)/float(r['original_linear_rms']))
        housing.append(np.min(h,axis=0));breathing.append(np.max(b,axis=0))
    h=np.max(housing,axis=0);b=np.min(breathing,axis=0)
    full=list(csv.DictReader((out/'full_housing_linear.csv').open()));full_curves=[]
    for id in dict.fromkeys(r['id'] for r in full):
        group=[r for r in full if r['id']==id];curves=[]
        for r in group:
            nu=float(r['nu']);ld=float(r['strength_generator_norm']);L=min(100*ld,np.sqrt(100*ld/(2*nu)))
            curves.append((np.sqrt(float(r['worst_full_housing_energy_fraction']))+1e-6+L*abs(x-nu))**2)
        full_curves.append(np.min(curves,axis=0))
    h=np.max(full_curves,axis=0)
    fig,ax=plt.subplots(1,3,figsize=(13,4),layout='constrained')
    ax[0].plot(x,h,color='#216789',label='Numerical strength enclosure');ax[0].axhline(.5,ls='--',color='#b65c27',lw=1,label='Half-energy target')
    nodes=sorted(set(float(r['nu']) for r in full));maxima=[max(float(r['worst_full_housing_energy_fraction']) for r in full if float(r['nu'])==nu) for nu in nodes]
    ax[0].scatter(nodes,maxima,color='#216789',s=18,label='Worst evaluated parameter case')
    ax[0].set(xlabel='Strength nu',ylabel='Worst housing energy fraction at u=100',title='180D housing phase space; 50 parameter sets',ylim=(.1,.56));ax[0].legend(fontsize=8);ax[0].grid(alpha=.2)
    ax[1].plot(x,b,color='#216789',label='All-phase linear lower enclosure');ax[1].axhline(.8,ls='--',color='#b65c27',lw=1,label='Breathing target')
    pulses=list(csv.DictReader((out/'pulses.csv').open()))
    for nu in [.04,.05]:
        values=[float(r['breathing_retention']) for r in pulses if float(r['nu'])==nu];ax[1].scatter([nu], [min(values)],marker='s',color='#b65c27',s=35)
    ax[1].scatter([],[],marker='s',color='#b65c27',label='Minimum nonlinear endpoint pulse')
    ax[1].set(xlabel='Strength nu',ylabel='Breathing RMS / matching original baseline',title='Housing energy <= pulse energy /40000',ylim=(.77,1.01));ax[1].legend(fontsize=8);ax[1].grid(alpha=.2)
    for nu,col in [(.04,'#216789'),(.05,'#b65c27')]:
        data=np.genfromtxt(out/f'full-housing-ringdown-{nu}.csv',delimiter=',',names=True);ax[2].plot(data['u'],data['energy_fraction'],color=col,label=f'nu={nu}')
    ax[2].axhline(.5,ls='--',color='#777777',lw=1);ax[2].set(xlabel='Dimensionless time u',ylabel='Total energy / initial housing energy',title='Worst-case nonlinear housing-only runs',ylim=(0,1.03));ax[2].legend(fontsize=8);ax[2].grid(alpha=.2)
    fig.suptitle('UD Discovery · joint housing ringdown / breathing window · development evidence',fontsize=13)
    fig.savefig(out/'jointwindow-summary.png',dpi=160);plt.close(fig)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--out',type=Path,required=True);main(p.parse_args().out)
