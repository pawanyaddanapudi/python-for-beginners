
############# ARGUMENTS ################
import sys

arg1 = sys.argv[1]
arg2 = sys.argv[2]
print(arg1)
print(arg2)

# Chapter : Conditions & Loops

############ IF/ELSE ######################
if 10<9:
    print("You are into if block")
    a = 10
    b = 20
    print(a*b)
else:
    print("You are into else block")
    a = 20
    b = 300
    print(a*b)

orskl_prompt = int(input("What is your experience(years) : "))
if orskl_prompt<5:
    print("You are the first level software engineer")
else:
    print("You are the second or highest level software engineer")

orskl_prompt = int(input("What is your experience(years) : "))
if orskl_prompt<5:
    print("You are the first level software engineer")
    print("Your salary range would be x$ - y$")
elif orskl_prompt<8:
    print("You are the second level software engineer")
    print("Your salary range would be a$ - d$")
elif orskl_prompt<12:
    print("You are the third level software engineer")
    print("Your salary range would be f$ - k$")
else:
    print("You are the highest level software engineer")
    print("Your salary range would be p$ - i$")


orskl_prompt = int(input("What is your experience(years) : "))
if orskl_prompt<5:
    if orskl_prompt<2:
        print("You are close to be a fresher")
    else:
        print("You are the first level software engineer")
        print("Your salary range would be x$ - y$")
elif orskl_prompt<8:
    print("You are the second level software engineer")
    print("Your salary range would be a$ - d$")
elif orskl_prompt<12:
    print("You are the third level software engineer")
    print("Your salary range would be f$ - k$")
else:
    print("You are the highest level software engineer")
    print("Your salary range would be p$ - i$")

orskl_prompt = int(input("What is your experience(years) : "))
if orskl_prompt<5:
    if orskl_prompt<2:
        print("You are close to be a fresher")
    else:
        print("You are the first level software engineer")
        print("Your salary range would be x$ - y$")
elif orskl_prompt<8:
    print("You are the second level software engineer")
    print("Your salary range would be a$ - d$")
elif orskl_prompt<12:
    print("You are the third level software engineer")
    print("Your salary range would be f$ - k$")



if 10 > 9:
    print("You are inside if loop")
else:
    print("You are inside else loop")

orskl_prompt = int(input("What is your experience (years) :"))
if orskl_prompt < 5:
    print("You are in the first level skilled engineers list")
elif orskl_prompt < 10:
    print("You are in second level skilled engineers list")
else:
    print("You are top level skilled engineers list")

# Nested IF loops
orskl_prompt = int(input("What is your experience (years) :"))
if orskl_prompt < 5:
    print("You are in the first level skilled engineers list")
    if orskl_prompt < 2:
        print("Looks like fresher")
    else:
        print("Over fresher experience")
elif orskl_prompt < 10:
    print("You are in second level skilled engineers list")
else:
    print("You are top level skilled engineers list")

