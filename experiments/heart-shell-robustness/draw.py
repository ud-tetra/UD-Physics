"""Plot computed pulse and exact small-signal harmonic shape; requires analyze.py outputs."""
from pathlib import Path
import argparse
import importlib.util
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

root=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('robust',root/'analyze.py');a=importlib.util.module_from_spec(spec);spec.loader.exec_module(a)
p=argparse.ArgumentParser();p.add_argument('--summary',type=Path,required=True);args=p.parse_args()
d=json.loads(args.summary.read_text());worst=next(s for s in d['corner_scan'] if s['epsilon']==.05)['worst_pattern']
g=1+.05*np.fromstring(worst['stiffness_pattern'],sep=',');m=1+.05*np.fromstring(worst['inertia_pattern'],sep=',')
t=np.linspace(0,20,1601);x,_,_=a.trajectory(g,m,t);q=x[:,1:];s=1+q
y=np.column_stack([np.prod(s[:,[j for j in range(4) if j!=i]],axis=1)-1 for i in range(4)])
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'axes.spines.top':False,'axes.spines.right':False})
fig,axs=plt.subplots(1,2,figsize=(12,4.5),layout='constrained')
for i,c in enumerate(['#087f8c','#d87035','#6a4494','#888f99']):axs[0].plot(t,y[:,i],color=c,lw=1.4,label=f'Cell opposite vertex {i+1}')
axs[0].plot(t,y.mean(axis=1),color='#252c34',lw=1,ls='--',label='Mean cell response')
axs[0].set(title='Prepared pulse with ±5% imperfections',xlabel='Dimensionless parameter u',ylabel='Fractional cell-volume change')
axs[0].legend(loc='upper right',fontsize=7,frameon=False)
lam=np.linspace(0,7,3001);eps=.05
for eta,label,c in [(0,'Spoke stiffness only','#087f8c'),(.05,'Aligned stiffness and inertia','#6a4494'),(-.05,'Opposed stiffness and inertia','#d87035')]:
    n=eps*(1-lam)+lam*eta;den=4-lam-eps*eps+eps*lam*eta
    # Bounded projection fraction avoids dividing by vanishing mean volume amplitude.
    leak=np.abs(n)/np.sqrt(9*den*den+n*n)
    axs[1].plot(lam,100*leak,color=c,lw=2,label=label)
axs[1].axvline(4,color='#555e68',lw=1,ls='--',label='Reference differential mode')
axs[1].set(title='Frequency-dependent loss of coherence',xlabel='Squared model angular frequency ω²',ylabel='Differential fraction of linear volume signal (%)',ylim=(0,103),xlim=(0,7))
axs[1].legend(loc='upper right',fontsize=8,frameon=False)
for ax in axs:ax.grid(alpha=.15)
fig.suptitle('Stable motion can remain coherent after a pulse and become unequal near a differential resonance',fontsize=12)
fig.savefig(root/'robustness.svg');fig.savefig(root/'robustness.png',dpi=160)
