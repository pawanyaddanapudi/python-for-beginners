
##################### Nested Functions ####################

def orskl_nested_fun():
    print("YOu are inside the function")
    def orskl_absquare(a, b):
        y = a ** 2 + b ** 2 + 2 * a * b
        def orskl_absum(a,b):
            return a + b
        return y, orskl_absum(10,20)
    return orskl_absquare(10,20)

orskl_nested_fun()

orskl_nested_fun.orskl_absquare(10,20)

def orskl_nested_fnc():
    print("You are inside the function")
    def orskl_absquare(a, b):
        y = a ** 2 + b ** 2 + 2 * a * b
        return y
    orskl_absquare(10,20)


orskl_nested_fnc()

orskl_nested_fnc()

def orskl_nested_fnc():
    print("You are inside the function")
    def orskl_absquare(a, b):
        y = a ** 2 + b ** 2 + 2 * a * b
        return y
    return orskl_absquare(2,3)

orskl_nested_fnc()


###################### Iterators #####################
orskl_list = [ 10, 20, 30, 40 , 50]
orskl_iter = iter(orskl_list)
orskl_iter
print(next(orskl_iter))
print(next(orskl_iter))
print(next(orskl_iter))
print(next(orskl_iter))
print(next(orskl_iter))
print(next(orskl_iter))


###################### Regular Expressions #####################
# https://docs.python.org/3/library/re.html?highlight=re#module-re
import re
orskl_String = "Orskl Python for Beginners Course"
re.findall("[e$]",orskl_String)
re.findall("s$", orskl_String)
len(re.findall("[e*]", orskl_String))

re.split(" ",orskl_String)
re.split("\s",orskl_String)
re.split("for",orskl_String)

y = re.search("e+", orskl_String)
y.start()
y = re.search("P+", orskl_String)
y.start()
y = re.search("\s*", orskl_String)
y.start()
y = re.findall("\s*", orskl_String)
y
y = re.findall("[\s*]", orskl_String)
y
y = re.findall("[o*]", orskl_String)
y

####################### Handling Exceptions ######################
# try block
# Exception block
# Final block
print(a)

try:
    print(a)
except:
    pass

a = 10
b = 10
try:
    print(a)
    print(b)
except:
    print(" I did not fina value a")
finally:
    print("Try block execution completed")


try:
    print(a)
    print(z)
except Exception as orskl_e:
    print(" I did not fina value a")
    print(orskl_e)
finally:
    print("Try block execution completed")

try:
    print(a)
except Exception as E:
    print("All good")
finally:
    print("Try block execution completed")


def orskl_exception():
    orskl = 1
    try:
        print(orskl)
    except Exception as error:
        print(error)

try:
    print(orskl_String)
except:
    pass

orskl_exception()

