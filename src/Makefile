
#install: math_lib.so
#	pyinstaller --onefile --add-binary="math_lib.so:." --log-level=WARN --name="calc" calc.py
# 	rm -f -r __pycache__

install_dependencies:
	sudo apt update
	sudo apt install build-essential doxygen python3

doc:
	doxygen Doxyfile

.PHONY: clean doc install_dependencies test_math_lib

clean:
	rm -f -r *.so *.o *.spec __pycache__  doc warning_doxygen.txt
