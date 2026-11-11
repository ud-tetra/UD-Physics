import unittest
from fractions import Fraction as F
from autonomous_gate_v07 import stock,wedge,rhs,derivatives,aligned
class ScalarPortChecks(unittest.TestCase):
 def test_conservation_and_wedge(self):
  for r,y in [((F(1),F(0)),(F(0),F(1))),
              ((F(0),F(0)),(F(1),F(0))),
              ((F(1),F(1)),(F(2),F(-1)))]:
   self.assertEqual(derivatives(r,y),(0,0))
 def test_exact_aligned_solution(self):
  self.assertEqual(aligned(F(1)),(F(1,2),F(1,2)))
  self.assertEqual(aligned(F(10)),(F(100,101),F(1,101)))
 def test_phase_nonzero_floor(self):
  r,y=(F(1),F(0)),(F(0),F(1))
  self.assertEqual(wedge(r,y),1)
  self.assertEqual(stock(r,y),2)
  self.assertGreaterEqual(sum(t*t for t in y),wedge(r,y)**2/stock(r,y))
 def test_empty_reservoir_gate_zero(self):
  self.assertEqual(rhs((F(1),F(0)),(F(0),F(0))),
                   ((F(0),F(0)),(F(0),F(0))))
if __name__ == "__main__":unittest.main()
