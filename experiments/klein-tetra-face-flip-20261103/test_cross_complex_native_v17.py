#!/usr/bin/env python3
"""Minimal GitHub regression for K4 cross-complex theorem v1.7."""
import contextlib,io,runpy,unittest
from pathlib import Path
import sympy as s
class NativeAdmission(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  with contextlib.redirect_stdout(io.StringIO()):
   cls.z=runpy.run_path(str(Path(__file__).resolve().parent/'cross_complex_native_v17.py'))
 def test_chain_map(self):
  z=self.z
  self.assertEqual(z['D1']*z['Q'],z['Q']*z['D0'])
 def test_full_stock_defect(self):
  z=self.z
  self.assertEqual(z['Q'].T*z['Q']-s.eye(15),s.diag(*([0]*14+[3])))
 def test_new_top_unique(self):
  z=self.z
  self.assertEqual(z['m1'][2].rank(),4)
 def test_half_top_no_chain(self):
  z=self.z
  self.assertNotEqual(z['m1'][2]*(z['F'][3]/2),z['m0'][2])
 def test_shell_two_mode(self):
  z=self.z
  self.assertEqual(z['A1']*z['v'],z['w'])
  self.assertEqual(z['A1']*z['w'],-z['v'])
  self.assertEqual(z['v'].dot(z['v']),1)
  self.assertEqual(z['w'].dot(z['w']),1)
 def test_old_frequency(self):
  z=self.z
  self.assertEqual(z['A0']**2*z['oldv'],-4*z['oldv'])
 def test_all_1024_masks(self):
  z=self.z
  self.assertEqual(len(z['chainmasks']),2)
  self.assertEqual(len(z['s4mask']),4)
 def test_Q171_sign_gate(self):
  z=self.z
  i=z['b1'][2].index((0,1,2))
  j=z['b1'][3].index((0,1,2,4))
  self.assertEqual(z['m1'][2][i,j],-1)
  self.assertEqual(z['A1'][z['o1'][3]+j,z['o1'][2]+i],1)
if __name__=='__main__':unittest.main(verbosity=2)
