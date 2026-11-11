import unittest
from fractions import Fraction as F
class PortTests(unittest.TestCase):
 def test_exchange(self):
  a,b=F(3,5),F(4,5)
  self.assertEqual(a*a+b*b,1)
  r,y=F(2),F(3)
  x,z=a*r+b*y,-b*r+a*y
  self.assertEqual(x*x+z*z,r*r+y*y)
 def test_reciprocal(self):
  def swap(a,b):return b,-a
  self.assertEqual(swap(*swap(F(0),F(1))),(F(0),F(-1)))
 def test_source_conservation(self):
  self.assertEqual(sum(v*v for v in (F(0),F(1))),sum(v*v for v in (F(1),F(0))))
 def test_current_zero(self):
  self.assertEqual(2*0*1,2*1*0)
  self.assertNotEqual(0,1)
if __name__=='__main__':unittest.main()
