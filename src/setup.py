from setuptools import setup, find_packages

setup(
    name = "CalculateIT",
    version = "1.0",
    author = "CalculateIT",
    maintainer = "CalculateIT",
    description = "Simple but powerfull GUI calculator.",
    long_description="CalculateIT is high performance calculator suitable for researchers and computer science experts.",
    platform="Ubuntu 20.04",
    license = "GPLv3",
    url = "https://github.com/Xromi/IVS_2_projekt",
    packages=find_packages(include=['calculateit', 'calculateit.*']),
    entry_points = {
        'gui_scripts' : ['calculateit = calculateit.calc:main']
    },
    package_data = {'calculateit': ['dokumentace.pdf', 'calculateit_icon.gif']},
    data_files = [
        ('share/applications/', ['calculateit.desktop']),
        ('share/icons/calculateit', ['./calculateit/calculateit_icon.gif'])
    ],
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3.8",
        "Operating System :: POSIX :: Linux",
    ]
)