# OS
# Date
# Sys
# Print
# Installation (PIP)
# Loading Packages
# Session & Process

import os
print(os.getpid())
MYPROCESSID = os.getpid()
print(MYPROCESSID)
print("MYPROCESSID")
print(os.getcwd())
print(os.getppid())
print(os.listdir())
os.name
print(os.name)
os.path
os.uname()


# sys package, which is by default available with Python installation
import sys
sys.version
# Print
print(sys.version)
print(sys.path)
# https://docs.python.org/3/library/sys.html#sys.platform
print(sys.platform)
PLATFORM = sys.platform
# Check the Variables panel for this variable after execution
print(PLATFORM)
print(sys.modules)

import pprint
pprint.pprint(sys.modules)


# os package, one of the default librarires available with Python installation
import os
os.name
os.path
os.uname()
os.getcwd()
os.getpid()
os.getppid()
print(os.listdir())
# Check activity monitor or Task Manager to identify this process

# Why Printing?
# Structured printing, not conventional
# https://docs.python.org/2/library/pprint.html
print(sys.modules)
print("Hello OrSkl,"
      "We are in the Python for Beginners course Session 3 today"
      "We will continue to learn.")
print("Hello OrSkl,\n"
      "We are in the Python for Beginners course Session 3 today\n"
      "We will continue to learn.")
import pprint
pprint.pprint(sys.modules)

# Installing new packages
# pip3 ?
# Utility to install new packages from pypi. For example
# https://pypi.org/project/linkedin/
import linkedin

import cassandra

# Pandas - very important package that every Python developer will know of
# to deal with tabular data, it also includes another mathematical computing package called numpy
# pip3 install numpy
# pip3 install pandas
import pandas
import numpy

# As and when we learn new topics, we will install the relevant packages on the fly and start coding


# Check sessions from command line or terminal
# Understand how to deal with them

