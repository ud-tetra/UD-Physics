"""Illustrate exact volume formulas; plotting samples are not the proof."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

p=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'axes.spines.top':False,'axes.spines.right':False})
fig,axs=plt.subplots(1,2,figsize=(12,4.8),layout='constrained')
x=np.linspace(-.2,.2,201)
axs[0].plot(x,x,color='#087f8c',lw=3,label='Cells opposite vertices with x = +1 (two cells)')
axs[0].plot(x,-x,color='#d87035',lw=3,label='Cells opposite vertices with x = -1 (two cells)')
axs[0].axhline(0,color='#39424e',ls='--',lw=1.7,label='Total volume change')
axs[0].set(title='Move the heart; hold the shell fixed',xlabel='Heart shift along x (outer coordinates ±1)',ylabel='Fractional change from initial volume')
axs[0].text(.04,.91,'Redistribution: two cells grow, two shrink',transform=axs[0].transAxes,fontsize=11)
axs[0].legend(loc='lower left',fontsize=8,frameon=False)
y=(1+x)**3-1
axs[1].plot(x,y,color='#6a4494',lw=3,label='All four cells; total volume')
axs[1].axhline(0,color='#39424e',lw=1,alpha=.35)
axs[1].set(title='Dilate the shell; keep the heart centred',xlabel='Uniform shell dilation ε',ylabel='Fractional change from initial volume')
axs[1].text(.04,.91,'Collective breathing: every cell changes together',transform=axs[1].transAxes,fontsize=11)
axs[1].legend(loc='lower right',fontsize=8,frameon=False)
for ax in axs:ax.grid(alpha=.15);ax.set_xlim(-.2,.2)
fig.suptitle('Heart motion and volume breathing are distinct geometric modes',fontsize=15)
fig.savefig(p/'volume-modes.svg');fig.savefig(p/'volume-modes.png',dpi=160)
