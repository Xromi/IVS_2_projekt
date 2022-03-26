import unittest
import math_lib

from math import e

class TestMathLib(unittest.TestCase):

	def test_my_add(self):
		self.assertEqual(math_lib.my_add(1, 1), 2)
		self.assertEqual(math_lib.my_add(1, -1), 0)
		self.assertEqual(math_lib.my_add(-1, -1), -2)
		self.assertEqual(math_lib.my_add(1, -5), -4)
		self.assertEqual(math_lib.my_add(5, 2.5), 7.5)

		with self.assertRaises(TypeError):
			math_lib.my_add(5, "2.5")
		
	def test_my_subtract(self):
		self.assertEqual(math_lib.my_subtract(1, 1), 0)
		self.assertEqual(math_lib.my_subtract(1, -1), 2)
		self.assertEqual(math_lib.my_subtract(-1, -1), 0)
		self.assertEqual(math_lib.my_subtract(1, -5), 6)
		self.assertEqual(math_lib.my_subtract(5, 2.5), 2.5)	
	
	def test_my_multiply(self):
		self.assertEqual(math_lib.my_multiply(1, 1), 1)
		self.assertEqual(math_lib.my_multiply(1, -1), -1)
		self.assertEqual(math_lib.my_multiply(-1, 1), -1)
		self.assertEqual(math_lib.my_multiply(-1, -1), 1)
		self.assertEqual(math_lib.my_multiply(5, 2.5), 12.5)	
		
	def test_my_divide(self):
		self.assertEqual(math_lib.my_divide(1, 1), 1.0)
		self.assertEqual(math_lib.my_divide(1, -1), -1.0)
		self.assertEqual(math_lib.my_divide(-1, 1), -1.0)
		self.assertEqual(math_lib.my_divide(-1, -1), 1.0)
		self.assertEqual(math_lib.my_divide(5, 2.5), 2.0)
		
		with self.assertRaises(ZeroDivisionError):
			math_lib.my_divide(5, 0)
		
	def test_my_factorial(self):
		self.assertEqual(math_lib.my_factorial(0), 1)
		self.assertEqual(math_lib.my_factorial(1), 1)
		self.assertEqual(math_lib.my_factorial(5), 120)
		self.assertEqual(math_lib.my_factorial(10), 3628800)
		
		#negative factorial
		with self.assertRaises(ValueError):
			math_lib.my_factorial(-5)
            
	def test_my_power(self):
		self.assertEqual(math_lib.my_power(1, 1), 1)
		self.assertEqual(math_lib.my_power(1, -1), 1)
		self.assertEqual(math_lib.my_power(-1, 1), -1)
		self.assertEqual(math_lib.my_power(-1, -1), -1)
		self.assertEqual(math_lib.my_power(5, 5), 3125)	
		self.assertEqual(math_lib.my_power(-27, 1/3), -3)	

	def test_my_root(self):
		self.assertEqual(math_lib.my_root(1, 1), 1.0)
		self.assertEqual(math_lib.my_root(1, -1), -1.0)
		self.assertEqual(math_lib.my_root(-1, 1), 1.0)
		self.assertEqual(math_lib.my_root(-1, -1), -1.0)
		self.assertEqual(math_lib.my_root(2, 25), 5.0)
		self.assertEqual(math_lib.my_root(3, -27), -3)
		self.assertEqual(math_lib.my_root(-3, -8), -1/2)
		
		#even degree root of a negative number
		with self.assertRaises(ValueError):
			math_lib.my_root(2, -5)
		
		with self.assertRaises(ValueError):
			math_lib.my_root(-4, -5)
		
	def test_my_log(self):
		self.assertEqual(math_lib.my_log(1), 0)
		self.assertEqual(math_lib.my_log(e), 1)
		
		#natural logarithm of a negative number
		with self.assertRaises(ValueError):
			math_lib.my_log(-5)

		#natural logarithm of zero
		with self.assertRaises(ValueError):
			math_lib.my_log(0)

if __name__ == "__main__":
    unittest.main()
