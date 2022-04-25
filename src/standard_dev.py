import cProfile
import sys
from calculateit.math_lib.math_lib import *


def std_dev():
	text_input = sys.stdin.read().split()
	numbers=[]
	N=0
	sum=0
	psum=0

	for word in text_input:
		numbers.append(float(word))

	
	for number in numbers:
		sum=my_add(number, sum);
		psum=my_add(psum, my_power(number, 2))
		N=my_add(N,1)

	
	average=my_divide(sum, N)
	std_dev=my_root(2,my_divide(my_subtract(psum, my_multiply(N, my_power(average, 2))), my_subtract(N, 1)))
	return std_dev

cProfile.run("std_dev()")

