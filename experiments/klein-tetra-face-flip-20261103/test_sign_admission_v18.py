#!/usr/bin/env python3
"""Eight exact source-native signed-current and admission replay checks."""
import unittest,runpy,contextlib,io
from pathlib import Path
import sympy as s
class SignAdmission(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  with contextlib.redirect_stdout(io.StringIO()):
   cls.z=runpy.run_path(str(Path(__file__).resolve().parent/'sign_admission_v18.py'))
 def test_frozen_signed_B3(self):
  z=self.z
  self.assertEqual(z['sigma'],-1)
  self.assertEqual(z['A1'][z['o1'][3]+z['to'],z['o1'][2]+z['fo']],1)
 def test_exact_full_stock_defect(self):
  z=self.z;self.assertEqual(z['F'].T*z['F']-s.eye(15),3*z['e']*z['e'].T)
 def test_invariant_no_defect_rank(self):
  z=self.z;self.assertEqual(z['P'].rank(),13);self.assertEqual(z['A0']*z['P'],z['P']*z['A0'])
 def test_first_leakage_gram(self):
  z=self.z;self.assertEqual(z['Rleak'].T*z['Rleak'],z['P'])
 def test_intertwining_obstruction(self):
  z=self.z;self.assertEqual((z['Err']*z['P']).rank(),13)
 def test_crossing_second_derivative(self):
  z=self.z;u,a,beta=z['u'],z['a'],z['beta']
  self.assertEqual(s.simplify(s.diff(z['S'],u,2).subs({a:0,u:0})),8*beta**2)
 def test_prepared_switch_derivative_jump(self):
  z=self.z;self.assertEqual((z['Err']*z['b']).dot(z['Err']*z['b']),9)
 def test_all_signed_S4(self):
  self.assertEqual(self.z['out']['S4_signed_checks'],24)
if __name__=='__main__':unittest.main(verbosity=2)
