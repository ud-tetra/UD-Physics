#!/usr/bin/env python3
"""Exact constructor regression tests for coupled K4 parity clock v1.4."""
import unittest,runpy,contextlib,io
from pathlib import Path
ROOT=Path(__file__).resolve().parent
class CoupledClockV14(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  with contextlib.redirect_stdout(io.StringIO()):
   cls.c=runpy.run_path(str(ROOT/'coupled_clock_v14.py'))
   cls.g=runpy.run_path(str(ROOT/'gray_pair_flip_v14.py'))
 def test_effective_frame_six(self):
  self.assertEqual(len(self.c['S3']),6)
  self.assertEqual(len(self.c['S4']),24)
 def test_finite_frame_capacity(self):
  self.assertEqual(len(self.c['P48']),48)
  self.assertEqual(len(self.c['P192']),192)
 def test_period_eight_under_chosen_successor(self):
  c=self.c
  for x in c['P48']:
   y=x
   for _ in range(8):y=c['t48'](y)
   self.assertEqual(y,x)
 def test_no_affine_eight_cycle(self):
  c=self.c
  self.assertEqual(len(c['mats']),168)
  self.assertEqual(sum(c['cycles'].values()),1344)
  self.assertEqual(c['cycles'][8],0)
 def test_current(self):
  c=self.c
  self.assertEqual((c['delta'],c['incoming'],c['outgoing']),(14,59,45))
  self.assertEqual(sum(c['stocks'].values()),sum(c['new'].values()))
 def test_gray_locality(self):
  g=self.g
  self.assertEqual(g['flips'],[0,1,0,2,0,1,0,2])
  self.assertEqual(len(g['cycles']),12)
  self.assertEqual(len(g['unoriented']),6)
 def test_raw_edge_covariance_cases(self):
  g=self.g
  self.assertEqual(len(g['RAW'])*len(g['S4']),1536)
  self.assertEqual(len(g['RAW'])*len(g['S4'])**2,36864)
 def test_native_rank_obstruction(self):
  self.assertEqual(self.g['native_ranks'],(1,2,2,2,2,2,2,2))
  self.assertEqual(self.g['native_ranks'].count(1),1)
if __name__=='__main__':unittest.main(verbosity=2)
