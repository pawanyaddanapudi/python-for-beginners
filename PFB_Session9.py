
#################### Default functions ####################
abs(-20)
dict()
len([1,2,3,4])
set()
min([1,2,3,4])
max([1,2,3,4])
max([19,30,40,50])
input("Please input some number")
from datetime import datetime
datetime.now()

####################  User defined ####################
def orskl_absquare(a,b):
    y = a**2 + b**2 + 2*a*b
    return y

orskl_absquare(2,3)
orskl_absquare(4,5)

def orskl_absquare(a,b):
    global y
    y = a**2 + b**2 + 2*a*b
    return y

b = orskl_absquare(2,3)
print(y)
print(b)

def orskl_func():
    print("Its an empty function")

orskl_func()

def orskl_absquare(a,b):
    y = a**2 + b**2 + 2*a*b
    z = y**3
    return z

orskl_absquare(2,3)
x = orskl_absquare(2,3)
print(x)
print(a)
print(b)
print(y)

####################  Lambda - Anonymous ####################
orskl_absquare_lambda = lambda a, b: a**2 + b**2 + 2*a*b
orskl_absquare_lambda(2,3)
orskl_absquare_lambda(4,5)

################### Map, filter ####################
# map


y = [1,2,3,4]
x = []
for i in y:
    x += [i*2]

x

def orskl_multiple(x):
    return x * 2

orskl_map = map(orskl_multiple, [1, 2, 3, 4])
list(orskl_map)

def orskl_absquare(a,b):
    y = a**2 + b**2 + 2*a*b
    return y

orskl_map2 = map(orskl_absquare, [1, 2, 3, 4],[1,2,3,4])
list(orskl_map2)


orskl_map3 = map(lambda x,y: x**2 + y**2 + 2*x*y, [1,2,3,4],[1,2,3,4])
orskl_map3 = map(lambda x,y: x**2 + y**2 + 2*x*y, [1, 2, 3, 4],[1,2,3,4])
list(orskl_map3)

orskl_absquare(3,3)

# Filter
orskl_list2 = [1, 2, 3, 4, 5]

orskl_filter = filter(lambda x: x % 2 == 0, orskl_list2)
list(orskl_filter)

