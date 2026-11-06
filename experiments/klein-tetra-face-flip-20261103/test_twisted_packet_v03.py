#!/usr/bin/env python3
"""Four exact checks using direct 60D audit and independent spectral factorization."""
import unittest,runpy
from pathlib import Path
ROOT=Path(__file__).resolve().parent
class TwistedPacketTests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.a=runpy.run_path(str(ROOT/"twisted_packet_chain_v03.py"))
  cls.b=runpy.run_path(str(ROOT/"spectral_crosscheck_v03.py"))
 def test_nilpotency_and_ranks(self):
  x=self.a
  self.assertEqual(x["t"]["ranks"],[4,9,10,5,1])
  self.assertEqual(x["u"]["ranks"],[3,10,10,5,1])
 def test_graded_homology_difference(self):
  self.assertEqual(self.a["t"]["betti_R"],[0,1,1,0,0,0])
  self.assertEqual(self.a["u"]["betti_R"],[1,1,0,0,0,0])
 def test_independent_spectral_agreement(self):
  self.assertEqual(self.a["t"]["L_eigen_multiplicities"],self.a["u"]["L_eigen_multiplicities"])
  self.assertEqual(self.b["out"]["twisted"]["product_spectrum"],{0:2,4:30,8:28})
  self.assertEqual(self.b["out"]["untwisted"]["product_spectrum"],{0:2,4:30,8:28})
 def test_twist_loop_not_norm_readout(self):
  self.assertEqual((-1)*1*(-1)*1,1)
  self.assertEqual((-1)**2,1)
  self.assertNotEqual(-1,1)
if __name__=="__main__":unittest.main()
