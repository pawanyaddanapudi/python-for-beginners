
# Modules
# Create
# Load
# Execute
# Maintain


# __init__.py file used to be mandatory


orskl_obj = lib1.pack1.PFB_Session14_mod1.orskl_mod1_class1()
orskl_obj.orskl_mod1_class1_func1(10,20)
orskl_obj.orskl_mod1_class1_func2(10,20)
orskl_obj.orskl_modl1_class1_func3(10,20)
orskl_name()


from lib1.pack1 import PFB_Session14_mod1

orskl_obj = PFB_Session14_mod1.orskl_mod1_class1()
orskl_obj.orskl_mod1_class1_func1(10,20)
orskl_obj.orskl_mod1_class1_func2(10,20)
orskl_obj.orskl_modl1_class1_func3(10,20)

PFB_Session14_mod1.orskl_mod1_func1(10, 20)
PFB_Session14_mod1.orskl_mod1_func2()


from lib1.pack1 import orskl_mod1_func2

orskl_mod1_func2()

import orsklmodules

orskl_obj = orsklmodules.orskl_class()
orskl_obj.student_count()

from orsklmodules import orskl_class
orskl_obj = orskl_class()
orskl_obj.student_count()

from orsklmodules import orskl_func
orskl_func()

import orsklmodules as orskl

orskl.orskl_func()

# Module is a file which contains various Python functions and global variables.
# It is simply just .py extension file which has python executable code.
#
# Package is a collection of modules. Create a directory and move the module, PyCharm does a magic
# It must contains an __init__.py file as a flag so that the python interpreter processes it as such.
# The __init__.py could be an empty file without causing issues.
#
# Library is a collection of packages.
#
