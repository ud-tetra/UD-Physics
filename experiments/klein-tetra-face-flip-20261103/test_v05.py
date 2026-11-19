#!/usr/bin/env python3
"""Exact regression tests: 72-tet orientation coefficients, rational homology comparison, native invariant hull."""
import unittest,runpy
from pathlib import Path
P=Path(__file__).resolve().parent
class V05Checks(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.a=runpy.run_path(str(P/'twisted_72_boundary_v05.py'))
  cls.b=runpy.run_path(str(P/'rational_comparison_v05.py'))
  cls.c=runpy.run_path(str(P/'invariant_hull_v05.py'))
 def test_twisted_rank_and_smith(self):
  self.assertEqual(cls_result(self.a,'ranks'),[18,83,72])
  self.assertEqual(self.a['diag'],[1]*17+[2])
 def test_integral_boundary_nilpotency(self):
  B=self.a['boundary'];S=self.a['S']
  self.assertEqual(B[1]*B[2],S.zeros(18,156))
  self.assertEqual(B[2]*B[3],S.zeros(102,72))
 def test_rational_comparison_chainmap(self):
  m=self.b['Phi'];s=self.b['Bs'];d=self.b['dC']
  for k in (1,2,3):self.assertEqual(d[k-1]*m[k],m[k-1]*s[k])
  self.assertEqual([z.rank() for z in m],[0,1,1,0])
 def test_native_hull_and_corr(self):
  H=self.c['H'];Pj=self.c['P'];A=self.c['A'];Rp=self.c['Rp'];S=self.c['S']
  self.assertEqual(H.rank(),5)
  self.assertEqual(Pj*A,A*Pj)
  self.assertEqual(Rp*H,H)
  self.assertEqual((H[:,0].T*(-Rp)*H[:,0])[0],-(H[:,0].T*H[:,0])[0])
def cls_result(o,name):return o[name]
if __name__=='__main__':unittest.main()
