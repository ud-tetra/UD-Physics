#!/usr/bin/env python3
"""Replays three distinct exact Klein bulk/interface/S4 checks in one suite."""
import unittest,runpy
from pathlib import Path
P=Path(__file__).resolve().parent
class BulkTests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.a=runpy.run_path(str(P/"bulk_prism_v04.py"))
  cls.b=runpy.run_path(str(P/"bulk_bridge_v04.py"))
  cls.c=runpy.run_path(str(P/"full_chain_seam_v04.py"))
  cls.e=runpy.run_path(str(P/"packet_intertwiner_v04.py"))
 def test_3d_tetrahedral_incidence(self):
  self.assertEqual(self.a["fvec"],[18,102,156,72])
  self.assertEqual(self.a["ranks"],[17,84,72])
 def test_both_klein_boundaries(self):
  self.assertEqual(self.a["bs"],[[6,18,12],[6,18,12]])
  self.assertEqual(sum(self.a["fvec"][i]*(-1)**i for i in range(4)),0)
 def test_typed_cellular_bridge(self):
  self.assertEqual([x.rank() for x in self.b["M"]],[2,5,4,1])
  self.assertEqual([len(x) for x in self.b["T"]],[4,14,20,15,6,1])
 def test_transport_nonuniqueness(self):
  self.assertEqual(len(self.c["cases"]),2)
  self.assertEqual({x["combined_top_sign"] for x in self.c["cases"]},{-1,1})
 def test_equivariant_even_packet_bridge(self):
  self.assertEqual(self.e["F0"].rank(),2)
  self.assertEqual(self.e["F1"].rank(),1)
  self.assertEqual(self.e["F0"].T*self.e["F0"],2*self.e["eye"](2))
  self.assertEqual(len(self.e["out"]["even_map"]["degree0"]),2)
if __name__=="__main__":unittest.main()
