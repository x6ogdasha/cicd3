import unittest
from calcul import Calc

class TestCalc(unittest.TestCase):

   def setUp(self):
      self.calc = Calc()
   def test_plus(self):
      self.assertEqual(self.calc.plus(3,6),9)

   def test_minus(self):
      self.assertEqual(self.calc.minus(10,2),8)

   def test_umn(self):
      self.assertEqual(self.calc.umn(3,2),6)

   def test_delen(self):
      self.assertEqual(self.calc.delen(6,3),2)

   def mod(self):
      self.assertEqual(self.calc.mod(6,3),0)

   if __name__ == "__main__":
      unittest.main()
      
