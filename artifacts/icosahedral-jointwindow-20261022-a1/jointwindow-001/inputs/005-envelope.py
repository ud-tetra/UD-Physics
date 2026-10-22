"""Exact piecewise-linear extremum locations for float64 interpolation bounds."""
from pathlib import Path
import argparse,csv,json
import numpy as np

LOW=.04;HIGH=.05
def extreme(nodes,values,slopes,lower_envelope,maximum):
    # f_j(x)=values_j+slopes_j*abs(x-nodes_j). All possible changes of active
    # affine piece occur at a cusp or at a pairwise intersection.
    points={LOW,HIGH,*nodes}
    for j in range(len(nodes)):
        for k in range(j):
            breaks=sorted({LOW,HIGH,nodes[j],nodes[k]})
            for a,b in zip(breaks,breaks[1:]):
                if b-a<1e-15:continue
                mid=(a+b)/2;s1=slopes[j]*(1 if mid>=nodes[j] else -1);s2=slopes[k]*(1 if mid>=nodes[k] else -1)
                c1=values[j]-s1*nodes[j];c2=values[k]-s2*nodes[k]
                if abs(s1-s2)>1e-12:
                    x=(c2-c1)/(s1-s2)
                    if a<=x<=b:points.add(float(x))
    p=np.array(sorted(points));curves=np.asarray(values)[:,None]+np.asarray(slopes)[:,None]*abs(p[None,:]-np.asarray(nodes)[:,None])
    curve=np.min(curves,axis=0) if lower_envelope else np.max(curves,axis=0)
    index=int(np.argmax(curve) if maximum else np.argmin(curve));return float(curve[index]),float(p[index])

def main(out):
    rows=list(csv.DictReader((out/'linear.csv').open()));result=[]
    for id in dict.fromkeys(r['id'] for r in rows):
        group=sorted([r for r in rows if r['id']==id],key=lambda r:float(r['nu']));nodes=[float(r['nu']) for r in group]
        h,hn=extreme(nodes,[np.sqrt(float(r['worst_housing_energy_fraction']))+1e-6 for r in group],[100*float(r['strength_generator_norm']) for r in group],True,True)
        base=float(group[0]['original_linear_rms'])
        b,bn=extreme(nodes,[(float(r['linear_pulse_rms'])-float(r['all_phase_readout_rms_bound'])-1e-6)/base for r in group],[-float(r['breathing_rms_lipschitz_bound'])/base for r in group],False,False)
        result.append({'id':id,'continuous_strength_housing_energy_upper':h*h,'housing_upper_at_nu':hn,'continuous_strength_all_phase_linear_retention_lower':b,'retention_lower_at_nu':bn})
    maxh=max(result,key=lambda r:r['continuous_strength_housing_energy_upper']);minb=min(result,key=lambda r:r['continuous_strength_all_phase_linear_retention_lower'])
    report={'status':'PASS' if maxh['continuous_strength_housing_energy_upper']<=.5 and minb['continuous_strength_all_phase_linear_retention_lower']>=.8 else 'OPEN_OR_FAILED',
            'method':'all cusps and pairwise affine-piece intersections; float64 inputs,not verified interval arithmetic',
            'maximum_housing_energy_upper':maxh,'minimum_all_phase_linear_retention_lower':minb,'per_case':result}
    (out/'envelopes.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({k:v for k,v in report.items() if k!='per_case'},indent=2))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--out',type=Path,required=True);main(p.parse_args().out)
