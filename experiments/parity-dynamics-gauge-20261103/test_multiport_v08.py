import unittest
from fractions import Fraction as F
class TestPort(unittest.TestCase):
 def test_rotation(self):
  a,b=F(3,5),F(4,5)
  self.assertEqual(a*a+b*b,1)
 def test_wedge_change(self):
  self.assertEqual(F(4,5)*(4-1),F(12,5))
 def test_generic_floor(self):
  self.assertEqual((F(2)-F(8,5))/2,F(1,5))
 def test_modes(self):
  self.assertEqual((0,-1),(0,-1))
if __name__=='__main__':unittest.main()
