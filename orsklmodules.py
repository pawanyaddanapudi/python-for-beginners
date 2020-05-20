
import datetime
class orskl_class_input():

    def __init__(self, a, b):
        self.c = a*b

    def orskl_addition(self):
        return self.c+40

    def orskl_multiplication(self):
        return self.c*2


class orskl_class():
    def today_datetime(self):
        return datetime.datetime.now()
    def student_count(self):
        return 100
    def compute_absquare(self, a, b):
        return a**2 + b**2 + 2*a*b

def orskl_func():
    print("Its an empty function")