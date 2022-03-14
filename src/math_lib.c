/**
 * @file math_lib.c
 * @author David Klajbl, Marián Tarageľ, Ondřej Chromý
 * @brief Implementation of mathematical library
 * @version 0.1
 * @date 2022-03-14
 */

#include "math_lib.h"
#include <math.h>
#include <stdio.h>

// Addition
double my_add(double x, double y){
	return x+y;
}

// Subtraction
double my_subtract(double x, double y){
	return x-y;
}

// Multiplication
double my_multiply(double x, double y){
	return x*y;
}

// Division
double my_divide(double x, double y){
	return x/y;
}

// Factorial
double my_factorial(double x){
	/*
	int f = 1;       
    for(int i = 1; i <= x; i++){    
    	f = f * i;
    }
    return f;
    */   
}

// Power
double my_power(double x, double y){
	return pow(x,y);
}

// Root
double my_root(double n, double x){
	/*
	return x;
	*/
}

// Logarithm
double my_log(double x){
	return log(x);
}
