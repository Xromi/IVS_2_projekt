# Jak používat Makefile

## 1. Nainstaluj dependencies (Ubuntu 20.04)
* Automaticky (pokud již máš nainstalovaný make)
  * **make install_dependencies**
* Manuálně
  1. sudo apt update
  2. sudo apt install **build-essential doxygen python3**
  3. pip3 install **pyinstaller**

## 2. Používej make
* ***make*** nebo ***make all***
  * Vytvoří matematickou knihovnu *"math_lib.so"*.
* ***make install***
  * Vytvoří spustitelnou binárku *"./dist/calc"* z programu *"calc.py"* a knihovny *"math_lib.so"*.
* ***make run***
  *  Spustí binárku vytvořenou pomocí *"make install"*
* ***make clean***
  *  Vyčistí všechny nepotřebné soubory.
* ***make doc***
  *  Vygeneruje dokumentaci.
* ***make test_math_lib***
  *  Spustí testovací skript (*"test_math_lib.py"*) matematické knihovny.

