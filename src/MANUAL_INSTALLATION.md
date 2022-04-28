# Manual Installation of CalculateIT Calculator

## 1. Make sure **src/** is your current directory

## 2. Install required dependencies
### a) either by using
    make install_build_dependencies
### b) or by manually running these commands
    sudo apt update
    sudo apt install build-essential python3 python3-tk python3-all python3-pip python3-stdeb dh-python dh-make
    pip3 install stdeb stem

## 3. Build package using
    make build

## 4. Install Debian package by running
    sudo dpkg -i ./calculateit_1.0-1_all.deb
---
---
# Manual Uninstall of CalculateIT Calculator
## Run
    sudo dpkg -r calculateit
