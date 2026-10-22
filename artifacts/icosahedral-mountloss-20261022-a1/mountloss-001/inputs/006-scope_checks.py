"""Post-selection checks of the cf=0 proof scope; no strength selection here."""
from pathlib import Path
import argparse,json
from analyze import linear_probe
from mountloss import MountLoss

def main(out):
    p=json.loads((out/'probes.json').read_text())[1];rows=[]
    for id,kwargs in [('nominal-cf0',{'cf':0}),('scatter-cf0',{'cf':0,'housing_weights':p['housing_weights'],'ratio_error':p['ratio_error'],**p['primary']}),('low-housing-mass-cf0',{'cf':0,'beta':.005})]:
        row,_=linear_probe(MountLoss(nu=.02,**kwargs));row['id']=id
        assert row['least_nonrigid_decay_rate']>0;rows.append(row)
    (out/'linear_scope_checks.json').write_text(json.dumps({'status':'PASS','exposure':'additional post-selection checks; no retuning','rows':rows},indent=2)+'\n')
    print(json.dumps(rows,indent=2))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--out',type=Path,required=True);main(p.parse_args().out)
