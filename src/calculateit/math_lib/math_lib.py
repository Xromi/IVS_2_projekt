## @file math_lib.py
# @author Marián Tarageľ, David Klajbl
# @brief Implementation of mathematical library
# @version 0.3
# @date 2022-03-26

pi = 3.141592653589793
e = 2.718281828459045

##
# @brief Addition of two numbers
#
# @param x First term
# @param y Second term
#
# @exception TypeError Function raises TypeError when first or second term is not float or int data type
#
# @return Sum of x and y
def my_add(x, y):
	if (type(x) != float and type(x) != int) or (type(y) != float and type(y) != int):
		raise TypeError("First and second term have to be float or int numbers.")
	else:
		return x + y

##
# @brief Subtraction of two numbers
#
# @param x First term
# @param y Second term
#
# @exception TypeError Function raises TypeError when first or second term is not float or int data type
#
# @return Difference of x and y
def my_subtract(x, y):
	if (type(x) != float and type(x) != int) or (type(y) != float and type(y) != int):
		raise TypeError("First and second term have to be float or int numbers.")
	else:
		return x - y

##
# @brief Multiplication of two numbers
#
# @param x First factor
# @param y Second factor
#
# @exception TypeError Function raises TypeError when first or second factor is not float or int data type
#
# @return Product of x and y
def my_multiply(x, y):
	if (type(x) != float and type(x) != int) or (type(y) != float and type(y) != int):
		raise TypeError("First and second factor have to be float or int numbers.")
	else:
		return x * y

##
# @brief Division of two numbers
#
# @param x Dividend
# @param y Divisor
#
# @exception ZeroDivisionError Function raises ZeroDivisionError if divisor is zero
# @exception TypeError         Function raises TypeError when divident or divisor is not float or int data type
#
# @return Quotient of x and y
def my_divide(x, y):
	if (type(x) != float and type(x) != int) or (type(y) != float and type(y) != int):
		raise TypeError("Divident and divisor have to be float or int numbers.")
	else:
		return x / y

## 
# @brief Factorial of a number
# 
# @param x Non-negative integer
#
# @exception ValueError Function raises ValueError if x is negative or none integeral value
#
# @return Factorial of x
def my_factorial(x):
	if (x > 20):
		raise OverflowError
	if (type(x) != int):
		raise TypeError("Number have to be int number.")
	elif x < 0:
		raise ValueError("Number have to be non-negative integer.")
	f = 1
	if x == 0 or x == 1:
		return f
	else:
		for i in range(1, x + 1):
			f *= i
		return f

##
# @brief Exponentiation of two numbers
#
# @param x Base
# @param y Exponent
#
# @exception ValueError Function raises ValueError when base is a negative number and 1/exponent is not an odd number
# @exception TypeError  Function raises TypeError when base or exponent is not float or int data type
#
# @return Value of x to the power of y
def my_power(x, y):
	if (type(x) != float and type(x) != int) or (type(y) != float and type(y) != int):
		raise TypeError("Base and exponent have to be float or int numbers.")
	elif x < 0:
		if not (float(abs(1/y)).is_integer() and abs(1/y)%2 == 1):
			raise ValueError("Root of negative number has to be odd integer.")
		else:
			return -((-x) ** (y))
	else:
		return x ** y

##
# @brief N-th root of a number
#
# @param n Degree
# @param x Radicand
#
# @exception ValueError Function raises ValueError when redicant is a negative number and degree is not an odd number
# @exception ValueError	Function raises ValueError when base or exponent is not float or int data type
#
# @return Value of n-th root of x
def my_root(n, x):
	return my_power(x, (1 / n))

##
# @brief Modulo of a number
#
# @param x Dividend
# @param y Divisor
#
# @exception ZeroDivisionError Function raises ZeroDivisionError if divisor is zero
# @exception TypeError         Function raises TypeError when divident or divisor is not float or int data type
#
# @return Value of modulo
def my_modulo(x, y):
	if (type(x) != float and type(x) != int) or (type(y) != float and type(y) != int):
		raise TypeError("Divident and divisor have to be float or int numbers.")
	else:
		return x % y
