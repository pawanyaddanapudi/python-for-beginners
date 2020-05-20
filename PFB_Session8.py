############ FOR loops  ######################

orskl_List = [ 10, 20, 30, 40, 50]
orskl_list2 = []

for list_element in orskl_List:
    print(list_element)
    orskl_list2 += [list_element*3]

orskl_list2
list_element

Orskl_List2 = ["Hello", "ORSKL", "Class", "Python"]
for var1 in Orskl_List2:
    print(var1)


range(5)
for number in range(10):
    print(number, "times")

list(range(5))
list(range(1,5))
list(range(2,5))
list(range(3,10,2))


for index_no in range(len(Orskl_List2)):
    print(index_no)
    print(Orskl_List2[index_no])

# Nested
Orskl_list4 = [500, 600, 700]
for var1 in Orskl_List2:
    print(var1)
    for a in Orskl_list4:
        print(var1, a, a / 100)


##### While loops #########
a = 0

1 == 0
0 == 0

a = 2
while  a > 0:
    print("Inside the loop")
    a = int(input("Whats the new a value?: "))


while int(input("Whats the input value?: ")) > 0:
    print("In the loop")

from time import sleep
from datetime import datetime

while int(input("Whats the input value?: ")) > 0:
    print(datetime.now(), "In the loop")
    sleep(3)
    print(datetime.now(), "In the loop")

a = 0
while a == 0:
    for i in range(5):
        print(i)
        if i == 4:
            print("Break now")
            a = 1
