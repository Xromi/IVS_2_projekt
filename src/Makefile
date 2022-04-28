all:
	echo "Nothing to build."

##############

install_run_dependencies:
	sudo apt update
	sudo apt install python3 python3-tk

run:
	python3 -m calculateit.calc

##############

install_doc_dependencies:
	sudo apt update
	sudo apt install doxygen

doc:
	doxygen Doxyfile

##############

test:
	python3 -m tests.math_lib_tests.test_math_lib

test_exp_validity:
	python3 -m tests.exp_parser_tests.validity

test_exp_results:
	python3 -m tests.exp_parser_tests.result

test_all: test test_exp_validity test_exp_results

##############

install_build_dependencies:
	sudo apt update
	sudo apt install build-essential python3 python3-tk python3-all python3-pip python3-stdeb dh-python dh-make
	pip3 install stdeb stem

build:
	python3 setup.py --command-packages=stdeb.command sdist_dsc
	cd deb_dist && cd calculateit-1.0 && dpkg-buildpackage -rfakeroot -uc -b
	cd deb_dist && mv *.deb ..
	rm -rf CalculateIT* dist deb_dist debian

##############

profile:
	python3 ./standard_dev.py < tests/standard_dev_test_data/1000_n.txt

##############

zip_name=xhorva17_xchrom19_xklajb00_xtarag01

pack: clean doc build
	rm -rf $(zip_name) $(zip_name).zip
	mkdir $(zip_name) $(zip_name)/doc $(zip_name)/install $(zip_name)/repo
	rsync -a ../ $(zip_name)/repo/ --exclude $(zip_name) --exclude *.deb --exclude doc --exclude warning_doxygen.txt
	cp -r doc/html/* $(zip_name)/doc
	cp *.deb $(zip_name)/install
	zip -r $(zip_name).zip $(zip_name)
	rm -rf $(zip_name)

##############

.PHONY: clean doc profile run pack all \
		install_run_dependencies install_build_dependencies \
		build build_clean \
		test test_all test_exp_results test_exp_validity test_math_lib

clean:
	rm -rf doc warning_doxygen.txt $(zip_name) $(zip_name).zip *deb
	find . -type d -name "__pycache__" -prune -exec rm -rf {} \;
