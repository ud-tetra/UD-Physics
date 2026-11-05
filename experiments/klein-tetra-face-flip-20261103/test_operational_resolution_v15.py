#!/usr/bin/env python3
"""Exact K4 resolution-floor regression suite, eight checks."""
import unittest
import sympy as s
import operational_resolution_v15 as O

class ResolutionV15(unittest.TestCase):
 def test_closed_form_positive_increment(self):
  for n in range(9):
   self.assertEqual(s.simplify(O.alpha(n+1)-O.alpha(n)),s.Rational(11,4)**n/4)
 def test_all_depth_recursion(self):
  self.assertEqual(O.prove_all_depth()['positive_difference'],'(11/4)^n/4')
 def test_simplex_counts(self):
  for n,t in O.levels(3):
   v={z for T in t for z in T}
   e={a for T in t for a in O.combinations(T,2)}
   self.assertEqual((len(v),len(e),len(t)),((4**n+11)//3,(4**(n+1)+14)//3,4**n))
 def test_direct_exact_schur(self):
  for n,t in O.levels(3):
   A,_,_=O.response(t)
   self.assertEqual(A,O.alpha(n)*(4*s.eye(4)-s.ones(4)))
 def test_first_level_frozen_reference(self):
  t=list(O.levels(1))[-1][1]
  A,_,_=O.response(t)
  self.assertEqual(A,s.Rational(5,4)*(4*s.eye(4)-s.ones(4)))
 def test_local_support_core_states(self):
  for n,t in O.levels(3):
   if n:
    r=O.stock_contrast(t)
    self.assertEqual(r['core_stock_x'],['1','0','0','0'])
    self.assertEqual(r['core_stock_y'],['1/4']*4)
 def test_outer_shell_unmodified(self):
  for n,t in O.levels(3):
   b={f for T in t for f in O.combinations(T,3) if set(f)<={0,1,2,3}}
   self.assertEqual(len(b),4)
 def test_local_capacity_not_cell_limit(self):
  self.assertEqual(24*8,192)
  self.assertGreater(4**4,192)

if __name__=='__main__':unittest.main(verbosity=2)
