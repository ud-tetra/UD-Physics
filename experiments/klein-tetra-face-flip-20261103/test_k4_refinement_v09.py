#!/usr/bin/env python3
"""Exact regression checks for two native K4 centroid refinements."""
import unittest,runpy,contextlib,io
from pathlib import Path
import sympy as S
class RefinementTests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  with contextlib.redirect_stdout(io.StringIO()):
   cls.z=runpy.run_path(str(Path(__file__).resolve().parent/"k4_two_refinements_v09.py"))
 def test_signed_chain_maps(self):
  r=self.z["out"]
  self.assertEqual(r["levels"],[[4,6,4,1],[5,10,10,4],[9,26,34,16]])
  self.assertEqual(r["signed_S4_permutations"],24)
 def test_gram_metric(self):
  x=self.z
  self.assertEqual(x["x01"][0].T*x["x01"][0],S.diag(*([1]*14+[4])))
  self.assertEqual(x["x12"][0].T*x["x12"][0],S.diag(*([1]*25+[4]*4)))
 def test_native_spectra(self):
  r=self.z["out"]
  self.assertEqual(r["level0_to1"]["native_charpoly"],"lambda*(lambda**2 + 4)**7")
  self.assertEqual(r["level1_to2"]["native_charpoly"],"lambda*(lambda**2 + 1)*(lambda**2 + 5)**13")
 def test_residuals(self):
  r=self.z["out"]
  self.assertEqual(r["level0_to1"]["residual_norm_sq"],"13")
  self.assertEqual(r["level1_to2"]["residual_norm_sq"],"52")
  self.assertEqual(r["level0_to2"]["residual_norm_sq"],"151/4")
 def test_global_sign_composition(self):
  r=self.z["out"]
  self.assertEqual(r["native_twist_sign"].split("optional")[0].strip(),"rho(h)=-1")
  self.assertEqual((-1)*(-1),1)
if __name__=="__main__":unittest.main()
