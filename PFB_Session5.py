# Lists(Arrays)
# Dictionaries (JSON)
# Tuples
# Set
# DataFrames(Tables)
# Arguments


############# LISTS / ARRAYS ################

# Creating list
Orskl_list = [10, 20, 30, 40]
Orskl_list2 = ["hello", "Orskl", "Class"]
Orskl_list_3 = [10, 20, 30, 40, "hello", "Orskl", "Class"]
orskl_list4 = [10, 20, 30, 40, 10, "hello", "Orskl", "Class"]

len(Orskl_list_3)

# Read list
print(orskl_list4)
orskl_list4[3]
orskl_list4[5]
orskl_list4[0]
orskl_list4[4]
# Indexes of list starts with 0
orskl_list4[0:5]
orskl_list4[0:4]
orskl_list4[0:8]

orskl_list4[1:5]
orskl_list4[3:6]

orskl_list4[:]
orskl_list4

orskl_list4[::1]
orskl_list4[::2]
orskl_list4[::3]
orskl_list4[0:4:2]
orskl_list4[::-1]

# Values of odd positions/indexes
len(orskl_list4)
# Program to extract from 0 until len(orskl_list5), odd numbers first.
# Pass the numbers, as indexes to read those values
# Or simply
orskl_list4[1::2]


# Operations
orskl_list4[0] + orskl_list4[3]

#adding element
orskl_list4 += [250]
orskl_list4 = orskl_list4 + [250]
orskl_list4
orskl_list4.insert(1,300)
orskl_list4

# delete element
del orskl_list4[7]
orskl_list4

orskl_list4.pop(3)
orskl_list4

del orskl_list4[0:3]
orskl_list4

orskl_list4.remove('hello')
orskl_list4

# Nested lists
orskl_list5 = [ 10, 20, 30, 50, [0.5, 0.6, 0.7, 0.8]]
orskl_list5[2]
orskl_list5[4]
orskl_list5[4][2]

#replace
orskl_list5[1] = 50
orskl_list5

Orskl_List = [ 10, 20, 30, 40]
Orskl_List2 = ["Hello", "ORSKL", "Class", "Python"]
Orskl_List3 = [ 10.045, 20.987, 30.9888, 40.8764, 'Machine Learning']

# No of elements in the list
len(Orskl_List)


# Reading elements of list

Orskl_List[0]
Orskl_List[1]
Orskl_List[2]

#Slicing lists
Orskl_List[0:4]
Orskl_List[0:5]

Orskl_List[:]
Orskl_List[1:]

Orskl_List[0:5:2]
Orskl_List3[0:5:2]
Orskl_List3[::2]
Orskl_List3[::-2]
Orskl_List3[::-1]

# Operations
Orskl_List[0] + Orskl_List[1]

# Delete element or elements
Orskl_List.pop(0)
Orskl_List
Orskl_List = [ 10, 20, 30, 40]
del Orskl_List[0]
Orskl_List
Orskl_List = [ 10, 20, 30, 40]
del Orskl_List[0:2]
Orskl_List


Orskl_List = [ 10, 20, 30, 40]
Orskl_List.pop(1)
Orskl_List

Orskl_List = [ 10, 20, 30, 40]
Orskl_List.remove(10)
Orskl_List
Orskl_List.remove(20)
Orskl_List

# Adding to existing list
Orskl_List = [ 10, 20, 30, 40]
Orskl_List += [100]
Orskl_List = Orskl_List + [100]
Orskl_List
Orskl_List.insert(2,150)
Orskl_List

# Nested Lists
Orskl_List_nested = [ 10, 20, 30, 40, ['a','b','c'], 50, 60]
Orskl_List_nested[5]
Orskl_List_nested[4]
Orskl_List_nested[4][0]


