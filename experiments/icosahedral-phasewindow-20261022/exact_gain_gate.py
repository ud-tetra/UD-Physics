#!/usr/bin/env python3
"""Exact rational conditional mesh lemmas; numerical CSV is only screened, NEVER certified."""
from fractions import Fraction as F
from pathlib import Path
import argparse,json,csv

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--csv',type=Path,required=True);ap.add_argument('--out',type=Path,required=True)
 a=ap.parse_args()
 step=F(1,40);half=step/2
 node_pos=F(1,10000); node_vel=F(13,20000); global_acc=F(1,100)
 assert node_pos==F(1,10000) and node_vel==F(13,20000) and global_acc==F(1,100)
 continuous_vel=node_vel+half*global_acc
 continuous_pos=node_pos+half*continuous_vel
 remaining=F(1,40)-continuous_pos
 assert continuous_vel<F(1,1000) and continuous_pos<F(1,40) and remaining>0
 rows=list(csv.DictReader(a.csv.open()))
 assert len(rows)==4001
 assert all(abs(float(row['u'])-i/40)<1e-11 for i,row in enumerate(rows))
 def top(key):return max(rows,key=lambda r:float(r[key]))
 peaks={key:{'u':float(top(key)['u']),'value':float(top(key)[key])} for key in ('position_gain','velocity_gain','acceleration_gain')}
 numeric_pass={"position_nodes":peaks['position_gain']['value']<float(node_pos),
               "velocity_nodes":peaks['velocity_gain']['value']<float(node_vel),
               "acceleration_samples_only":peaks['acceleration_gain']['value']<float(global_acc)}
 assert all(numeric_pass.values())
 result={'status':'EXACT_CONDITIONAL_PLUS_NUMERICAL_SCREEN_NOT_VALIDATED','mesh_nodes':4001,'mesh_step':str(step),'mesh_nearest_distance':str(half),
  'premises_not_yet_certified':{'position_nodes':str(node_pos),'velocity_nodes':str(node_vel),'continuous_acceleration':str(global_acc)},
  'exact_consequences_if_premises_certified':{'continuous_velocity':str(continuous_vel),'continuous_position':str(continuous_pos),'nonlinear_remainder_allowance':str(remaining)},
  'numerical_screen':{'source_csv':a.csv.name,'sampled_peaks':peaks,'pass_against_proposed_margins':numeric_pass,'not_formal_enclosure':True},
  'qualification':'All-time linear operator bound conditional on THREE unproved validated estimates. The ordinary DOP853 + cubic coefficient interpolation samples do not establish them. Uniform nonlinear remainder and all 120 housing strut positivity still OPEN.'}
 a.out.parent.mkdir(parents=True,exist_ok=True);a.out.write_text(json.dumps(result,indent=2)+'\n')
 print('PASS exact conditional interpolation:',str(continuous_vel),str(continuous_pos),'nonlinear allowance',str(remaining))
 print('NUMERICAL ONLY sampled peaks',peaks)
if __name__=='__main__':main()
