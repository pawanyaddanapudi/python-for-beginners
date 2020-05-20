# Date
# Text
# Numeric
# Boolean
# Object
# Data Operations
# Prompt Inputs

# Date
import datetime
print(datetime.datetime.now())

from datetime import datetime
print(datetime.now())


from datetime import date
print(date.today())

from datetime import datetime, timedelta
print(datetime.today())

print(datetime.today() + timedelta(days=1))

print(datetime.today() - timedelta(days=1))

print(datetime.today() + timedelta(days=-1))

print(datetime.today() - timedelta(days=-1))

print(datetime.today() + timedelta(hours=1))

ORSKL_3Days = date.today() - timedelta(days=3)
type(ORSKL_3Days)


# Text
# Variables creation starts now
OrSkl_text = "This is ORSKLs Python for beginners course"
print(OrSkl_text)
# How to check type of variable
# Variable value will be replaced with same name
OrSkl_text
type(OrSkl_text)
OrSkl_text_num = "110"
ORSKL = '110'
print(OrSkl_text_num)
type(OrSkl_text_num)

# Numeric
OrSkl_num = 30
print(OrSkl_num)
type(OrSkl_num)
print(OrSkl_num + 2)
print(OrSkl_num * 2)
print(OrSkl_num ** 2)
print(OrSkl_num / 2)
print(OrSkl_text + 2)


# Now if we have to print Number, Text & Date in one print
print(OrSkl_text + OrSkl_num + ORSKL_3Days)
print(OrSkl_text + str(OrSkl_num) + str(ORSKL_3Days))

print(OrSkl_text + " started on " + str(ORSKL_3Days) + " and runs for " + str(OrSkl_num) + " days")
print(OrSkl_text , OrSkl_num , ORSKL_3Days)

print(OrSkl_text , str(OrSkl_num) , str(ORSKL_3Days))

print(OrSkl_text , "started on " , ORSKL_3Days , "and runs for " , OrSkl_num , "days")
print('{var1} started on {var2} and runs for {var3} days'.format(
	var1=OrSkl_text, var2=ORSKL_3Days, var3=OrSkl_num))

print('{0} started on {1} and runs for {2} days'.format(
	OrSkl_text, ORSKL_3Days, OrSkl_num))


# Boolean
OrSkl_bool = True
OrSkl_boolean = True
print(OrSkl_bool)
OrSkl_bool = False
print(OrSkl_bool)

# variable to variable
OrSkl_var2 = OrSkl_text
print(OrSkl_var2)


# Objects
class OrsklClass:
	"This is our fourth class"
	a = 10
	def func(self):
		print('Hello')

# create a new OrsklClass
Orskl_ob = OrsklClass()
type(Orskl_ob)
print(Orskl_ob.a)
Orskl_ob.func()

import os
print(os.getpid())

# Prompt inputs
a = input()
print(a)
type(a)
a = int(input())
print(a)
type(a)

