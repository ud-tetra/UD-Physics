"""Illustrate the exact prepared-heart solution; no numerical ODE integration."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

root=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'axes.spines.top':False,'axes.spines.right':False})
u=np.linspace(0,20,1601);a0=1/10
a=a0*(np.cos(u)+4*np.cos(np.sqrt(6)*u))/5
b=a0*(np.cos(u)-np.cos(np.sqrt(6)*u))/5
fig,axs=plt.subplots(1,2,figsize=(12,4.4),layout='constrained')
axs[0].plot(u,a,color='#087f8c',lw=1.9,label='Internal heart strain a')
axs[0].plot(u,b,color='#d87035',lw=2,label='Uniform shell dilation b')
axs[0].set(title='Stored heart strain drives the shell',xlabel='Dimensionless evolution parameter u',ylabel='Dimensionless strain')
axs[0].legend(loc='upper right',fontsize=9,frameon=False)
axs[1].plot(u,(1+b)**3-1,color='#6a4494',lw=2.4,label='Exact volume response: (1+b)³ − 1')
axs[1].plot(u,3*b,color='#555e68',ls='--',lw=1,label='Linear response: 3b')
axs[1].set(title='All four cell volumes change together',xlabel='Dimensionless evolution parameter u',ylabel='Fractional change from reference volume')
axs[1].legend(loc='upper right',fontsize=8,frameon=False)
for ax in axs:ax.axhline(0,color='#526170',lw=.7,alpha=.5);ax.grid(alpha=.14);ax.set_xlim(0,20)
fig.suptitle('Positive-energy candidate: heart–shell volume breathing',fontsize=15)
fig.savefig(root/'heart-volume-response.svg');fig.savefig(root/'heart-volume-response.png',dpi=160)
