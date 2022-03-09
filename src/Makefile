all: math_lib.o math_lib.so


math_lib.o: math_lib.c
	gcc -std=c11 -Wall -Wextra -pedantic -c -fPIC $^ -o $@

math_lib.so: math_lib.o
	gcc $^ -shared -o $@


install: math_lib.so
	pyinstaller --onefile --add-binary="math_lib.so:." --log-level=WARN --name="calc" calc.py
	rm -f -r __pycache__

test_math_lib: math_lib.so
	python3 ./test_math_lib.py math_lib.so

install_dependencies:
	sudo apt update
	sudo apt install build-essential doxygen python3
	pip3 install pyinstaller

doc:
	doxygen

.PHONY: clean doc run install_dependencies install all lib_test

run:
	./dist/calc

clean:
	rm -f -r *.so *.o *.spec build dist __pycache__  doc warning_doxygen.txt
