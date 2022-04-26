#install: math_lib.so
#	pyinstaller --onefile --add-binary="math_lib.so:." --log-level=WARN --name="calc" calc.py
# 	rm -f -r __pycache__

install_dependencies:
	sudo apt update
	sudo apt install build-essential doxygen python3

doc:
	doxygen Doxyfile

run:
	python3 -m calculateit.calc

test:
	python3 -m tests.math_lib_tests.test_math_lib

test_exp_validity:
	python3 -m tests.exp_parser_tests.validity

test_exp_results:
	python3 -m tests.exp_parser_tests.result

test_all: test test_exp_validity test_exp_results

build-clean:
	rm -f -r CalculateIT.egg-info dist deb_dist CalculateIT-1.0.tar.gz debian

build-deb:
	python3 setup.py --command-packages=stdeb.command sdist_dsc
	cd deb_dist && cd calculateit-1.0 && dpkg-buildpackage -rfakeroot -uc -b
	cd deb_dist && mv *.deb ..

build: build-deb build-clean

profile:
	python3 ./standard_dev.py < tests/standard_dev_test_data/1000_n.txt

.PHONY: clean doc install_dependencies test_math_lib

clean:
	rm -f -r *.so *.o *.spec __pycache__  doc warning_doxygen.txt
