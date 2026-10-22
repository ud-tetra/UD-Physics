"""Exact rational checks for nonlinear energy-domain certificates.

The inequalities/proofs are in README.md. No ODE sample is used as a proof.
"""
from fractions import Fraction as F
from pathlib import Path
import argparse,json

def calculate():
    Eh=F(17,10**7); Ep=F(17,250); E=Ep+Eh
    k=F(19,50); hm=F(9,5000); kh=F(9,50)
    # Strict lower bounds hm,kh use R²<1; all energy budgets are non-strict.
    sigma=F(1,500); epsilon=F(3,1000); delta=F(1,200)
    assert 2*Eh<sigma**2 and 2*Eh/k<epsilon**2 and 2*Eh/kh<delta**2
    endpoint=(1-epsilon)/2-delta
    median2=(1-epsilon)**2-(1+epsilon)**2/4
    assert median2>F(4,5)**2
    opposite=F(4,5)-delta
    assert endpoint==F(987,2000)>F(49,100) and opposite>endpoint
    # deltaG=(t*1^T+1*t^T-U)/2; shared energy, not two independent budgets.
    frobenius2=2*Eh*(3*(2+sigma)**2+(2+epsilon)**2/(2*k))
    assert frobenius2<F(1,125)**2
    # lambda_min(G_ref)=1/2. Det ratios and continuous initial orientation.
    spectral=F(2,125)
    assert (1-spectral)**3>F(39,40)**2
    assert (1+spectral)**3<F(41,40)**2
    # Full-pulse short-time continuation: housing and primary point speed caps.
    vh=F(9); vp=F(2,5); time=F(1,20); initial_length=F(99,200)
    assert 2*E/hm<vh**2 and 2*E/F(19,20)<vp**2
    pulse_length=initial_length-(vh+vp)*time
    assert pulse_length==F(1,40)>F(1,50)
    # Each relative spoke column changes by <2 vp t; ||Delta A||F <7t/5.
    assert F(7,4)**2>3
    assert F(7,5)*time/F(7,10)==F(1,10)
    assert F(7,10)**2<F(1,2)
    # An endpoint collapse on reference primary geometry has mount U=kh_exact/8.
    # beta=1/200,w=1,Omega=10 gives kh_exact=1/(5 R²).
    # R²>9/10 implies U<1/36 <13/200 (nominal pulse).
    assert F(11,5)**2<5 # sqrt5>11/5 => R²>9/10
    assert F(1,36)<F(13,200)
    # Even at maximal kh, a single housing can be moved to an endpoint with
    # cost U=kh/8; this is an energy-sublevel witness only at the lower beta.
    return {
        'status':'EXACT_CONDITIONAL_PASS_WITH_FULL_PULSE_OBSTRUCTION',
        'budgets':{'housing_only_energy_max':str(Eh),'pulse_plus_housing_energy_max':str(E)},
        'housing_only_all_time':{
            'spoke_strain_absolute_upper':str(sigma),'shell_edge_strain_absolute_upper':str(epsilon),
            'mount_displacement_upper':str(delta),'endpoint_strut_length_lower':str(endpoint),
            'opposite_anchor_strut_length_lower':str(opposite),'all_strut_length_lower':str(endpoint),
            'cell_gram_frobenius_error_squared_upper':str(frobenius2),
            'relative_gram_spectral_error_upper':str(spectral),
            'each_oriented_cell_volume_ratio_interval':[str(F(39,40)),str(F(41,40))],
            'mean_volume_ratio_interval':[str(F(39,40)),str(F(41,40))],
            'global_existence':True,'deadline_half_energy':'OPEN',
            'scope':'Every housing displacement/velocity phase of energy<=E_p/40000, alpha=0, primary reference and initially at rest, device z=zdot=0. Continuous qualified property box; nu>=0. Strict stated geometric bounds.'},
        'full_pulse_all_phase_short_time':{
            'time_interval':[str(F(0)),str(time)],'housing_speed_upper':str(vh),'primary_point_speed_upper':str(vp),
            'all_strut_length_lower':str(pulse_length),
            'each_oriented_cell_volume_ratio_interval':[str(F(9,10)**3),str(F(11,10)**3)],
            'scope':'Original alpha=1/10 pulse plus any allowed housing phase; all qualified properties. No u=100 nonlinear all-phase certificate.'},
        'full_pulse_energy_only_obstruction':{
            'witness':'Reference primary, alpha=z=0, velocities=0, one lower-beta housing moved from midpoint to either edge endpoint; other housings at midpoints.',
            'witness_energy':'1/(40 R²) <1/36 <13/200',
            'meaning':'The full-pulse total-energy sublevel contains a strut singularity. It cannot alone exclude collapse. This is not a trajectory from the allowed initial energy ball.'},
        'evidence':'Proof inequalities and Fraction assertions; no physical calibration or interval ODE claim.'}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--out',required=True,type=Path);args=p.parse_args()
    args.out.mkdir(parents=True,exist_ok=True)
    result=calculate();(args.out/'bounds.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
