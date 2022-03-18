std_opt = -std=c11 -Wall -Wextra -pedantic

unit_tests: math_lib_unit_tests.c 
	gcc ${std_opt} math_lib_unit_tests.c -o math_lib_unit_tests ../src/math_lib.o -lm
