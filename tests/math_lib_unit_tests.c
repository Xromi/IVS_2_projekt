#include <stdio.h>
#include <math.h>
#include "tau/tau.h"
#include "../src/math_lib.h"


TAU_MAIN()


TEST(BasicArithmetic, Addition) {
	CHECK_EQ(my_add(1, 1), 2);
	CHECK_EQ(my_add(7.8, 13.25), 21.05);
	CHECK_EQ(my_add(0.0000000001, 0.9999999999), 1);
	CHECK_EQ(my_add(0.0000000001, 0.0000000001), 0.0000000002);
	CHECK_EQ(my_add(0.00000000000000000001, 0.99999999999999999999), 1);
	CHECK_EQ(my_add(0.00000000000000000001, 0.00000000000000000001), 0.00000000000000000002);
	CHECK_EQ(my_add(3.1415926535, 2.526667), 5.668259653);
	CHECK_EQ(my_add(922388543.54667788, 675807.675845788), 923064351.2);
	CHECK_EQ(my_add(0.54667788, 0.675845788), 1.2);
	CHECK_EQ(my_add(0.54667788, 0.675845788), 1.2);
	CHECK_EQ(my_add(-0.544667, 123.4445), 122.899833);
	CHECK_EQ(my_add(14667.65478834, -922388543.54667788), -922373875.9);
	CHECK_EQ(my_add(9223372036854775807.1, 1), 9223372036854775808.1);
}

TEST(BasicArithmetic, Subtraction) {
	CHECK_EQ(my_subtract(1, 1), 0);
	CHECK_EQ(my_subtract(-1, -1), 0);
	CHECK_EQ(my_subtract(1, 0.9999999999), 0.0000000001);
	CHECK_EQ(my_subtract(5467723.76589945, 34.519999996), 5467689.24610);
	CHECK_EQ(my_subtract(0.5466778810, 0.675845788), -0.129167908);
	CHECK_EQ(my_subtract(0.675845788, 0.54667788), 0.129167908);
	CHECK_EQ(my_subtract(0, 10), -10);
}

TEST(BasicArithmetic, Multiply) {
	CHECK_EQ(my_multiply(5,10), 50);
	CHECK_EQ(my_multiply(9223372036854775807, 2), 0);
	CHECK_EQ(my_multiply(9223372036854775807, 100), 0);
	CHECK_EQ(my_multiply(9223372036854775807, 9223372036854775807), 0);
	CHECK_EQ(my_multiply(0.000001, 0.000001), 0);
}

TEST(BasicArithmetic, Division) {
	CHECK_EQ(my_divide(5,1), 5);
	CHECK_EQ(my_divide(1,5), 0.2);
	CHECK_EQ(my_divide(0.00002, 0.00001), 2);
	CHECK_EQ(my_divide(1, 9223372036854775807), 0);
}


TEST(BasicArithmetic, Factorial) {
}


TEST(BasicArithmetic, Power) {

}


TEST(BasicArithmetic, Root) {

}

TEST(BasicArithmetic, Logarithm) {
	/*
	CHECK_EQ();
	CHECK_EQ();
	CHECK_EQ();
	CHECK_EQ();
	CHECK_EQ();
*/
}

TEST(VariableManipulation, Test1) {

}

TEST(VariableManipulation, Test2) {

}


TEST(VariableManipulation, Test3) {

}

TEST(ChainedExpression, Test1) {

}

TEST(ChainedExpression, Test2) {

}

TEST(ChainedExpression, Test3) {

}
















