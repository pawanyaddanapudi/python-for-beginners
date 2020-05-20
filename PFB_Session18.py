# https://practice.geeksforgeeks.org/explore/?problemType=full&difficulty%5B%5D=0&page=1

# Problem 1 - Complexity: Easy
# https://practice.geeksforgeeks.org/problems/minimum-changes-to-make-all-substrings-distinct/0

orskl_total_tests = int(input("What are the total tests: "))
orskl_list = []
for i in range(orskl_total_tests):
    question = "What is your " + str(i+1) + " string: "
    orskl_text = str(input(question))
    orskl_list += [orskl_text]

print(orskl_list)
len(orskl_list[0])
len(set(orskl_list[0]))

for string in orskl_list:
    print(len(string) - len(set(string)))



orskl_total_tests = int(input("What are the total tests: "))
orskl_input_string = []
for i in range(orskl_total_tests):
    query = "Whats the "+ str(i+1) + " string of total " + str(orskl_total_tests) + " :"
    orskl_text = str(input(query))
    orskl_input_string += [orskl_text]


for string in orskl_input_string:
    distinct_count = len(set(string))
    full_count = len(string)
    duplicate_count = full_count - distinct_count
    print(duplicate_count)

# Problem 2 - Complexity: Medium
# https://practice.geeksforgeeks.org/problems/kth-smallest-element/0

orskl_total_tests = int(input("What are the total tests: "))
orskl_length = []
orskl_list = []
orskl_find = []

for i in range(orskl_total_tests):
    query = 'What is the ' + str(i+1) + ' test length? '
    orskl_length += [int(input(query))]
    query = 'What is the ' + str(i + 1) + ' test all integers? '
    orskl_list += [str(input(query))]
    query = 'What is the ' + str(i + 1) + ' test "nth element" integers? '
    orskl_find += [str(input(query))]

print(orskl_length)
print(orskl_list)

print(orskl_find)

print(orskl_list[0].split(" ").sort())
int_check = orskl_list[0].split(" ")
int_check.sort()
int_check

int_2 = list(map(int, orskl_list[0].strip().split(" ")))
int_2
int_2.sort()
print(int_2)
print(int_2[3])

for i in range(orskl_total_tests):
    length = orskl_length[i]
    orskl_l = orskl_list[i]
    orskl_li = list(map(int, orskl_l.strip().split(" ")))
    nth_element = int(orskl_find[i])
    orskl_li.sort()
    print(orskl_li[nth_element-1])



orskl_total_tests = int(input("What are the total tests: "))
orskl_length = []
orskl_list = []
orskl_find = []
for i in range(orskl_total_tests):
    query = "Whats the "+ str(i+1) + "th length of total " + str(orskl_total_tests) + " :"
    orskl_length += [int(input(query))]
    query = "Whats the " + str(i+1) + "th list of total " + str(orskl_total_tests) + " :"
    orskl_list += [str(input(query))]
    query = "Whats the " + str(i+1) + "th 'nth smallest element' of total " + str(orskl_total_tests) + " :"
    orskl_find += [int(input(query))]

orskl_length
orskl_list
orskl_find

for i in range(orskl_total_tests):
    input = orskl_list[i]
    input_list = list(map(int, input.strip().split(" ")))
    input_find = orskl_find[i]
    input_list.sort()
    print(input_list[input_find-1])


# Problem 3 - Complexity: Hard
# https://practice.geeksforgeeks.org/problems/maximum-of-minimum-for-every-window-size/0

# 10 20 30 50 10 70 30
#
# 1st iteration
#  max(min(10), min(20) , min(30), min(50), min(10), min(70), min(30)) - 1st element output = 70
# 2nd iteration
#  min(10,20), min(20, 30), min(30,50), min(50,10), min(10,70) min(70,30)
#  max(10          20             30           10          10          30) = 30
# 3rd iteration
# min(10,20, 30), min(20, 30, 50), min(30,50, 10), min(50,10, 70), min(10,70,30)
#    max( 10              20              10                  10          10) = 20


orskl_total_tests = int(input("What are the total tests: "))
orskl_length = []
orskl_list = []
for i in range(orskl_total_tests):
    query = "Whats the "+ str(i+1) + "th length of total " + str(orskl_total_tests) + " :"
    orskl_length += [int(input(query))]
    query = "Whats the " + str(i+1) + "th list of total " + str(orskl_total_tests) + " :"
    orskl_list += [str(input(query))]

input_list = list(map(int, orskl_list[0].strip().split(" ")))
input_list[0:1]
input_list[1:2]
input_list[2:3]
input_list[3:4]

input_list[0:2]
input_list[1:3]
input_list[2:4]
input_list[3:5]

output = []
for i in range(orskl_total_tests):
    input = orskl_list[i]
    input_list = list(map(int, input.strip().split(" ")))
    input_length = orskl_length[i]
    counter = 0
    while counter < input_length:
        mid_list = []
        for j in range(input_length-counter):
            mid_list += [min(input_list[j:j+1+counter])]
        output_int = max(mid_list)
        counter += 1
        output += [output_int]
    print(output)
    print(*(output))

print(output)

for i in range(orskl_total_tests):
    input = orskl_list[0]
    input_list = list(map(int, input.strip().split(" ")))
    input_length = orskl_length[i]
    counter = 0
    output = []
    while counter < input_length:
        mid_list = []
        for j in range(input_length-counter):
            #print(min(input_list[j:j + 1 + counter]))
            mid_list += [min(input_list[j:j + 1 + counter])]
        #print('###################')
        #print('Max is ', max(mid_list))
        output += [max(mid_list)]
        #print('###################')
        counter += 1
    print(output)
    print(*(output))


### References ####
# Python for Engineering & Analytics
# https://www.youtube.com/playlist?list=PLOu6DpGZzaARlItMeXKHp46jcWy8eLcqc
# https://github.com/pawanyaddanapudi/python-for-engineering-and-analytics
