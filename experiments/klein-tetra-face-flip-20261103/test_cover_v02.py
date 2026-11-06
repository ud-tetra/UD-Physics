#!/usr/bin/env python3
"""Compare independent triangular incidence lift and Schreier CW implementation."""
import unittest,runpy
from pathlib import Path
ROOT=Path(__file__).resolve().parent
class CoverTests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.tri=runpy.run_path(str(ROOT/"cover_audit_v02.py"))
  cls.cw=runpy.run_path(str(ROOT/"independent_cw_v02.py"))
 def test_exact_torus_homology(self):
  self.assertEqual((self.tri["B1"].rank(),self.tri["B2"].rank()),(1,3))
  self.assertEqual((self.cw["B1"].rank(),self.cw["B2"].rank()),(1,1))
 def test_independently_equal_homology(self):
  self.assertEqual(self.tri["result"]["cover"]["H1_Z"],self.cw["result"]["orientable_cover"]["H1_Z"])
  self.assertEqual(self.tri["result"]["cover"]["H2_Z"],self.cw["result"]["orientable_cover"]["H2_Z"])
 def test_flat_faces_global_flip(self):
  d=self.tri
  self.assertEqual(d["F"]*d["R"].inv()*d["X"].inv(),d["I"])
  self.assertEqual(d["F"].inv()*d["R"].inv()*d["X"],d["I"])
  self.assertEqual(int(d["F"].det()),-1)
 def test_cover_orientation_is_exact(self):
  self.assertEqual([int(t) for t in self.tri["pull"]],[1,1,0,0,1,1])
  self.assertEqual(self.tri["B2"].nullspace(),[self.tri["S"].Matrix([-1,1,-1,1])])
if __name__=="__main__":unittest.main()
