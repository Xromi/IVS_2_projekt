# CalculateIT Makefile Target Guide
## Contents
1. [ Running CalculateIT calculator ](#running-calculateit-calculator)
2. [ Generating documentation ](#generating-documentation)
3. [ Testing ](#testing)
4. [ Building Debian package ](#building-debian-package)
5. [ Profiling ](#profiling)
6. [ Packing ](#packing)
7. [ Cleaning ](#cleaning)

---

## Running CalculateIT calculator
### `make install_run_dependencies`
  * installs required dependencies needed to run CalculateIT calculator
  * manual alternative:

		sudo apt update
		sudo apt install python3 python3-tk

### `make run`
  * runs CalculateIT calculator

---

## Generating documentation
### `make install_doc_dependencies`
  * installs required dependencies to generate Doxygen source documentation
  * manual alternative:

		sudo apt update
		sudo apt install doxygen

### `make doc`
  * generates Doxygen documentation of CalculateIT calculator

---

## Testing
### `make test`
  * runs tests of mathematical library *"math_lib"*
### `make test_exp_validity`
  * runs test of parser of expressions *"exp_parse"* and validator of expressions *"exp_validate"*
### `make test_exp_results`
  * runs tests of evaluator of expressions *"exp_eval"*
### `make test_all`
  * runs all tests

---

## Building Debian package
### `make install_build_dependencies`
  * installs required dependencies needed to build CalculateIT calculator Debian package
  * manual alternative:  

		sudo apt update
		sudo apt install build-essential python3 python3-tk python3-all python3-pip python3-stdeb dh-python dh-make
		pip3 install stdeb stem

### `make build`
  * builds Debian package of CalculateIT calculator

---

## Profiling
### `make profile`
  * profiles the calculation of standard deviation of *"standard_dev.py"* script

---
## Packing
### `make pack`
  * creates zip with following structure
    * **doc/** = generated source documentation
    * **install/** = installers
    * **repo/** = git repository

---
## Cleaning
### `make clean`
  * cleans all temporary and non-source files
