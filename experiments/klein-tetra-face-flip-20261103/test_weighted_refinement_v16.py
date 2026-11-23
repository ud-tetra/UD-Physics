#!/usr/bin/env python3
"""Eight exact v1.6 positive-weight and observer/generator regression checks."""
import unittest
import sympy as s
import weighted_refinement_v16 as m
class K4Weighted(unittest.TestCase):
 def test_unit_matches_frozen_v15(self):
  vals=[str(m.alpha(n,lambda k:s.Integer(1))) for n in range(4)]
  self.assertEqual(vals,['1','5/4','31/16','245/64'])
 def test_quarter_proxy(self):
  vals=[str(m.alpha(n,lambda k:s.Rational(1,4)**(k-1))) for n in range(4)]
  self.assertEqual(vals,['1','5/4','91/64','1577/1024'])
 def test_direct_weighted_Schur(self):
  for g in (lambda k:s.Integer(1),lambda k:s.Rational(1,4)**(k-1)):
   for n,t,birth in m.levels(3):
    self.assertEqual(m.response(t,birth,g),m.alpha(n,g)*(4*s.eye(4)-s.ones(4)))
 def test_positive_generations_distinguishable(self):
  g=lambda k:s.Rational(1,5)**(k-1)
  for n in range(7):
   self.assertEqual(m.alpha(n+1,g)-m.alpha(n,g),
                    s.Rational(1,4)*s.Rational(11,4)**n*g(n+1))
 def test_intermittent_zero_generation_not_stop(self):
  g=lambda k:s.Integer(0) if k%2==0 else s.Integer(1)
  self.assertEqual(m.alpha(2,g),m.alpha(1,g))
  self.assertGreater(m.alpha(3,g),m.alpha(2,g))
 def test_candidate_limit(self):
  n=s.symbols('n',integer=True,nonnegative=True)
  alpha=s.Rational(9,5)-s.Rational(4,5)*s.Rational(11,16)**n
  self.assertEqual(s.limit_seq(alpha,n),s.Rational(9,5))
 def test_two_tolerance_scopes(self):
  q=s.Rational(11,16);eps=s.Rational(1,100)
  self.assertGreater(q**8/4,eps)
  self.assertLessEqual(q**9/4,eps)
  self.assertGreater(s.Rational(4,5)*q**11,eps)
  self.assertLessEqual(s.Rational(4,5)*q**12,eps)
 def test_weighted_fixed_complex_skew(self):
  n,t,birth=list(m.levels(2))[-1]
  self.assertTrue(m.weighted_current_check(t,birth,lambda k:s.Rational(1,4)**(k-1))['H_skew'])
if __name__=='__main__':unittest.main(verbosity=2)
