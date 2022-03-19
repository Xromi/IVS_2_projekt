## @file math_lib.py
# @author Marián Tarageľ
# @brief Implementation of mathematical library
# @version 0.2
# @date 2022-03-19

from math import *

##
# @brief Addition of two numbers
#
# @param x First term
# @param y Second term
# @return Sum of x and y
def my_add(x, y):
	return x + y

##
# @brief Subtraction of two numbers
#
# @param x First term
# @param y Second term
# @return Difference of x and y
def my_subtract(x, y):
	return x - y

##
# @brief Multiplication of two numbers
#
# @param x First factor
# @param y Second factor
# @return Product of x and y
def my_multiply(x, y):
	return x * y

##
# @brief Division of two numbers
#
# @param x Dividend
# @param y Divisor
# @return Quotient of x and y
def my_divide(x, y):
	return x / y

## 
# @brief Factorial of a number
# 
# @param x Non-negative integer
# @return Factorial of x
def my_factorial(x):
    return factorial(x)

##
# @brief Exponentiation of two numbers
#
# @param x Base
# @param y Exponent
# @return Value of x to the power of y
def my_power(x, y):
	return x ** y

##
# @brief N-th root of a number
#
# @param n Degree
# @param x Radicand
# @return Value of n-th root of x
def my_root(n, x):
	return x ** (1 / n)