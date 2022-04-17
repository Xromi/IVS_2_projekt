
#install: math_lib.so
#	pyinstaller --onefile --add-binary="math_lib.so:." --log-level=WARN --name="calc" calc.py
# 	rm -f -r __pycache__

install_dependencies:
	sudo apt update
	sudo apt install build-essential doxygen python3

doc:
	doxygen Doxyfile

test_math_lib: ./tests/math_lib_tests/test_math_lib.py
	python3 -m tests.math_lib_tests.test_math_lib

test_exp_parser_valididy:
	python3 -m tests.exp_parser_tests.test_expr_validity

test_exp_parser_results:
	python3 -m tests.exp_parser_tests.test_expr_result

.PHONY: clean doc install_dependencies test_math_lib

clean:
	rm -f -r *.so *.o *.spec __pycache__  doc warning_doxygen.txt
