"""Non-selection consistency checks and explicit primary-momentum field labels."""
from pathlib import Path
import argparse,json,hashlib

def main(out):
    p=out/'summary.json';report=json.loads(p.read_text());seed=report['seeded_pulse_challenge']
    for kind in ['linear','angular']:
        old=kind+'_momentum_drift';new='primary_'+kind+'_momentum_exchange'
        if old in seed:seed[new]=seed.pop(old)
    gap=abs(report['ringdowns'][2]['final_energy_fraction']-report['selected_linear_hidden']['worst_hidden_energy_fraction_u100'])
    assert gap<1e-4
    root=Path(__file__).resolve().parents[2];source=root/'artifacts/icosahedral-tolerances-20261022-a1/tolerances-001/files'
    sha={}
    for name in ['probes.json','baselines.json']:
        a=(out/name).read_bytes();assert a==(source/name).read_bytes();sha[name]=hashlib.sha256(a).hexdigest()
    report['postchecks']={'status':'PASS','nonlinear_vs_linear_worst_energy_fraction_change':gap,'frozen_input_sha256':sha,
                          'scope_checks':'linear_scope_checks.json; extra cf=0 cases are post-selection development, never used to select nu'}
    p.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report['postchecks'],indent=2))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--out',type=Path,required=True);main(p.parse_args().out)
