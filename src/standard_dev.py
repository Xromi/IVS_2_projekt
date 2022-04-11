import cProfile
import sys
from math_lib import *


def std_dev():
	text_input = sys.stdin.read().split()
	numbers=[]
	N=0
	sum=0

	for word in text_input:
		numbers.append(float(word))
		sum=my_add(sum, numbers[-1])
		N=my_add(N,1)



	r=my_multiply(my_power(my_divide(sum, N),2),N)
	sum=0

	for number in numbers:
		print(number)
		number=my_subtract(my_power(number, 2), r)
		sum=my_add(number, sum)


	a=my_divide(1, my_subtract(N,1))
	std_dev_value=my_root(my_multiply(a, sum),2)
	return std_dev_value

cProfile.run("std_dev()")
