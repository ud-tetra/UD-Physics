import unittest
from fractions import Fraction as F

class TestPort(unittest.TestCase):
 def test_rotation_and_old_area_change(self):
  a,b=F(3,5),F(4,5)
  self.assertEqual(a*a+b*b,1)
  r=(F(2),F(0));y=(F(0),F(1))
  # M=[[a,-b],[b,a]], rdot=M*y, ydot=-M^T*r
  rd=(-b,a);yd=(-2*a,2*b)
  old_dot=rd[0]*y[1]-rd[1]*y[0]+r[0]*yd[1]-r[1]*yd[0]
  self.assertEqual(old_dot,3*b)
  self.assertEqual(2*(r[0]*rd[0]+r[1]*rd[1]+y[0]*yd[0]+y[1]*yd[1]),0)
 def test_rotated_area_conserved(self):
  a,b=F(3,5),F(4,5);r=(F(2),F(0));y=(F(0),F(1))
  rd=(-b,a);yd=(-2*a,2*b)
  ry=(-b,a);rydot=(-2*(a*a+b*b),-2*a*b+2*a*b)
  dx=rd[0]*ry[1]-rd[1]*ry[0]+r[0]*rydot[1]-r[1]*rydot[0]
  self.assertEqual(dx,0)
 def test_reservoir_minimum(self):
  N=F(2);Dr=F(3,5)
  self.assertEqual(Dr*Dr/N,F(9,50))
  self.assertEqual((N-F(8,5))/2,F(1,5))
 def test_odd_mode_endpoint(self):
  # exact sine/cosine at multiples pi/2 by mod-4 arithmetic
  def sc(k): return ((0,1),(1,0),(0,-1),(-1,0))[k%4]
  self.assertEqual(sc(1),(1,0))
  self.assertEqual(sc(2),(0,-1))
  self.assertEqual(sc(3),(-1,0))
  # 1:3 transfers two channels; 1:2 leaves second source occupied.
  self.assertEqual((sc(1)[1],sc(3)[1]),(0,0))
  self.assertNotEqual((sc(1)[1],sc(2)[1]),(0,0))

if __name__=='__main__':unittest.main()
