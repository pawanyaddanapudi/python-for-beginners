# Lists(Arrays)
# Dictionaries (JSON)

# List comprehensions

orskl_string = 'ORSKL TECH'
extract_text = []
for each_alphabet in orskl_string:
    extract_text.append(each_alphabet)

print(extract_text)

extract_text2 = list(map(lambda x: x, orskl_string))
print(extract_text2)

extract_text3 = [x for x in orskl_string]
print(extract_text3)

orskl_even =[]
for x in range(20):
    if x % 2 == 0:
        orskl_even.append(x)

print(orskl_even)

orskl_even2 = [ x for x in range(20) if x%2 == 0 ]
print(orskl_even2)

for each_alphabet in orskl_string:
    extract_text.append(each_alphabet)

print(extract_text)

extract_text2 = [each_alphabet for each_alphabet in  orskl_string]
print(extract_text2)

extract_text3 = list(map(lambda each_alphabet: each_alphabet, orskl_string))
print(extract_text3)



orskl_num_list = [ x for x in range(20) if x % 2 == 0]
print(orskl_num_list)

orskl_num_list2 = [y for y in range(100) if y % 2 == 0 if y % 5 == 0]
print(orskl_num_list2)

orskl_obj = ["Even" if i%2==0 else "Odd" for i in range(10)]
print(orskl_obj)


# Dictionary comprehension

orskl_dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
orskl_dict1

orskl_dict1.keys()

orskl_dict1.values()

orskl_dict1.items()
[('a', 1), ('b', 2), ('c', 3), ('d', 4)]

orskl_dict_variable = {key:value for (key,value) in orskl_dict1.items()}
print(orskl_dict_variable)

orskl_dict2 = {}
for k in orskl_dict1.keys():
    orskl_dict2[k] = orskl_dict1[k]*100

print(orskl_dict2)

orskl_dict3 = {k:v*100 for (k,v) in orskl_dict1.items()}
print(orskl_dict3)

orskl_dict4 = {k*2:v for (k,v) in orskl_dict1.items()}
print(orskl_dict4)

orskl_dict_variable = {key:value for (key,value) in orskl_dict1.items()}
orskl_double_dict1 = {k:v*2 for (k,v) in orskl_dict1.items()}
orskl_double_dict1
orskl_dict1_keys = {k*2:v for (k,v) in orskl_dict1.items()}
orskl_dict1_keys


orskl_numbers = range(10)
orskl_new_dict_for = {}

# Add values to `new_dict` using for loop
for n in orskl_numbers:
    if n%2==0:
        orskl_new_dict_for[n] = n**2

print(orskl_new_dict_for)

orskl_new_dict_comp = {n:n**2 for n in orskl_numbers if n%2 == 0}

print(orskl_new_dict_comp)

# External files
# Save
# Read
# Append
# https://docs.python.org/3/library/functions.html#open

# Create a file
f = open("OutputFileData.txt", "w")
f.write("This is the first line of the file")
f.close()

f = open("OutputFileData2.txt", "a")
f.write("This is the first line of the file using append mode")
f.close()

f = open("OutputFileData.txt", "w")
f.write("This is the second line of the file")
f.close()

f = open("OutputFileData2.txt", "a")
f.write("")
f.write("This is the second line of the file")
f.close()

f = open("OutputFileData.txt", "r")
orskl_read_from_file = f.read()
f.close()
print(orskl_read_from_file)

f = open("OutputFileData2.txt", "a")
f.write("")
f.write("This is the thrird line of the file")
f.close()

f = open("OutputFileData2.txt", "a+")
f.write("")
f.write("This is the fourth line of the file")
f.close()

import os
if os.path.exists("OutputFileData.txt"):
    os.remove("OutputFileData.txt")

os.remove("OutputFileData2.txt")
os.rmdir("")


orskl_string = "This chapter covers topics of dealing with external files"
orskl_Students = 100
f = open("OutputFileData.txt", "a")
f.write(orskl_string)
f.write("")
f.close()
f = open("OutputFileData.txt", "a")
f.write(orskl_Students)
f.write("")
f.close()


f = open("OutputFileData.txt", "w")
f.write(orskl_string)
f.write("")
f.close()

import os
os.remove("OutputFileData.txt")

if os.path.exists("OutputFileData.txt"):
    os.remove("OutputFileData.txt")

