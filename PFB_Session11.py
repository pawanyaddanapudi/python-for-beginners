### Nested function ####
# def parent1():
#
#     # return valued from child1, 2, 3
#
#     def child1():
#
#         # child2 and child3 data is available
#
#         def child2():
#
#             #child2 function can return the value from child 3
#             def child3():
#
#                 return child3_data
#
#             return child2_data, child3_data
#
#         return child1_data, child2_data, child3 data
#
#     return parent1_data, child1_data, child2_data, child3 data

# Now when we execute parent() function, we get all the nested functions output

# Classes

class orskl_class():

    def orskl_print(self):
        print("You are executing print function inside a class")

    def orskl_addtion(self):
        print(20+30)

orskl_obj = orskl_class()

orskl_class.orskl_addtion(1)
orskl_class.orskl_print(2)

orskl_obj.orskl_print()
orskl_obj.orskl_addtion()

orskl_obj2 =  orskl_class()
orskl_obj2.orskl_print()

class orskl_class_input():

    def __init__(self, a, b):
        self.c = a*b

    def orskl_addition(self):
        return self.c+40

    def orskl_multiplication(self):
        return self.c*2


orskl_obj = orskl_class_input(10,20)
orskl_obj.c
orskl_obj.orskl_addition()

orskl_obj2 = orskl_class_input(30,30)
orskl_obj2.c
orskl_obj2.orskl_addition()

c = 200
c = 900



import datetime

class orskl_class():
    def today_datetime(self):
        return datetime.datetime.now()
    def student_count(self):
        return 100
    def compute_absquare(self, a, b):
        return a**2 + b**2 + 2*a*b

orskl_class1 = orskl_class()
orskl_class1.today_datetime()
orskl_class1.student_count()
orskl_class1.compute_absquare(2,3)
orskl_class1.a


orskl_class2 = orskl_class()
orskl_class2.today_datetime()
orskl_class2.student_count()
orskl_class2.compute_absquare(4,5)

# Initiation (__init__)
# Just like functions, you can also pass inputs to class, you will need to define them inside __init__ function in the
# class

class orskl_class_init2():
    def __init__(self, orskl_class_v1, orskl_class_v2):
        self.orskl_class_multi = orskl_class_v1*orskl_class_v2
    def today_datetime(self):
        return datetime.datetime.now()
    def student_count(self):
        return self.orskl_class_multi
    def compute_absquare(self, a, b):
        return a**2 + b**2 + 2*a*b

orskl_class1 = orskl_class_init2(10,20)
orskl_class1.today_datetime()
orskl_class1.orskl_class_multi
orskl_class1.student_count()
orskl_class1.compute_absquare(2,3)


orskl_class2 = orskl_class_init2(20,30)
orskl_class2.today_datetime()
orskl_class2.orskl_class_multi
orskl_class2.student_count()
orskl_class2.compute_absquare(4,5)

# Inheritance &
# Functions
class orskl_class_inheritance(orskl_class_init2):
    def orskl_print(self):
        print("Along with other functions, this class works")



orskl_class_inh1 = orskl_class_inheritance(10,20)
orskl_class_inh1.orskl_print()
orskl_class_inh1.today_datetime()
orskl_class_inh1.student_count()
orskl_class_inh1.compute_absquare(3,4)


class orskl_class_inheritance(orskl_class_init2):
    def __init__(self, orskl_v1, orskl_v2, orskl_v3, orskl_v4):
        self.orskl_addition = orskl_v3 + orskl_v4
        super().__init__(orskl_v1, orskl_v2)
    def orskl_add(self):
        return self.orskl_addition
    def orskl_print(self):
        print("Along with other functions, this class works")


orskl_class_inh1 = orskl_class_inheritance(10,20,30,40)
orskl_class_inh1.orskl_print()
orskl_class_inh1.today_datetime()
orskl_class_inh1.student_count()
orskl_class_inh1.orskl_add()
orskl_class_inh1.student_count()


