/**
 * @file math_lib.h
 * @author David Klajbl, Marián Tarageľ, Ondřej Chromý
 * @brief Mathematical library
 * @version 0.1
 * @date 2022-03-14
 */

#ifndef CLIB_H
#define CLIB_H

/**
 * @brief Addition of two numbers
 * 
 * @param x First term
 * @param y Second term
 * @return Sum of x and y
 */
double my_add(double x, double y);

/**
 * @brief Subtraction of two numbers
 * 
 * @param x First term
 * @param y Second term
 * @return Difference of x and y
 */
double my_subtract(double x, double y);

/**
 * @brief Multiplication of two numbers
 * 
 * @param x First factor
 * @param y Second factor
 * @return Product of x and y
 */
double my_multiply(double x, double y);

/**
 * @brief Division of two numbers
 * 
 * @param x Dividend
 * @param y Divisor
 * @return Quotient of x and y
 */
double my_divide(double x, double y);

/**
 * @brief Factorial of a number
 * 
 * @todo implementation
 * 
 * @param x Non-negative integer
 * @return Factorial of x
 */
double my_factorial(double x);

/**
 * @brief Exponentiation of two numbers
 * 
 * @todo implementation
 * 
 * @param x Base
 * @param y Exponent
 * @return Value of x to the power of y
 */
double my_power(double x, double y);

/**
 * @brief N-th root of a number
 * 
 * @todo implementation
 * 
 * @param n Degree
 * @param x Radicand
 * @return Value of n-th root of x
 */
double my_root(double n, double x);

/**
 * @brief Natural logarithm of a number 
 * 
 * @todo implementation
 * 
 * @param x Number whose logarithm is calculated
 * @return Value of natural logarithm of x
 */
double my_log(double x);

#endif
