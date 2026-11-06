#!/usr/bin/env python3
"""Eight exact native-K4 projector tests, including v0.9 independent replay."""
import unittest,runpy,contextlib,io
from pathlib import Path
import sympy as s
ROOT=Path(__file__).resolve().parent
class NativeEight(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  with contextlib.redirect_stdout(io.StringIO()):
   cls.n=runpy.run_path(str(ROOT/'NATIVE_EIGHT_PROJECTORS_v1.1.py'))
   cls.v=runpy.run_path(str(ROOT/'k4_two_refinements_v09.py'))
 def test_orthogonal_complete(self):
  q=self.n['Q']
  self.assertEqual(sum(q.values(),s.zeros(15)),s.eye(15))
  for t,P in q.items():
   self.assertEqual(P.T,P);self.assertEqual(P*P,P)
   for u,N in q.items():
    if t!=u:self.assertEqual(P*N,s.zeros(15))
 def test_ranks_and_24_permutations(self):
  q=self.n['Q']
  self.assertEqual([int(q[t].rank()) for t in sorted(q)],[1,2,2,2,2,2,2,2])
  self.assertEqual(self.n['out']['S4_signed_actions_checked'],24)
 def test_gram_rank13_identity(self):
  a=self.n
  self.assertEqual(a['R01'].T*a['R01'],s.eye(15)-a['Q']['111'])
 def test_independent_v09_native_refinement(self):
  b=self.v;a=self.n
  self.assertEqual(a['R01'],b['x01'][2]*b['x01'][0]-b['x01'][0]*b['x01'][3])
  self.assertEqual(a['R12'],b['x12'][2]*b['x12'][0]-b['x12'][0]*b['x12'][3])
  self.assertEqual(a['R02'],b['E02'])
 def test_sector_leakage(self):
  scores=self.n['score']
  self.assertEqual({t:str(x) for t,x in scores.items()},
   {'000':'1','001':'2','010':'2','011':'2','100':'2','101':'2','110':'2','111':'0'})
 def test_A_swaps_paired_spaces(self):
  a=self.n
  for u,v in zip(('100','010','001'),('011','101','110')):
   self.assertEqual(a['J']*a['Q'][u]*a['J'].T,a['Q'][v])
   self.assertEqual(a['A']*(a['Q'][u]+a['Q'][v]),(a['Q'][u]+a['Q'][v])*a['A'])
 def test_refinement_complement_and_commutation_failure(self):
  a=self.n
  self.assertEqual(str(sum(a['score12'].values())),'27')
  self.assertEqual(str(s.trace(a['rest']*a['R12'].T*a['R12'])),'25')
  self.assertEqual(str(sum(a['score02'].values())),'151/4')
  self.assertEqual((a['B02']*a['A']-a['A']*a['B02']).rank(),14)
 def test_rate_and_metric_dependence(self):
  r=self.n['R01']
  self.assertEqual(sum(x*x for x in (2*r)),52)
  self.assertEqual(2*sum(x*x for x in r),26)
if __name__=='__main__':unittest.main(verbosity=2)
