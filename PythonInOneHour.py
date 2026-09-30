#print ("hello")

#age = 20
#print(age)

#first_name = "Mathis"
#print(first_name)


#its_raining = True  

#name = input("What is your name? ")
#print("Hello " + name)
#   
#input = input("what is your birth year? ")
#age = 2024 - int(input)
#print("You are " + str(age) + " years old.")
#my_age = 20
#print("I am " + str(my_age) + " years old.")

#birth_year = input("What is your birth year? ")
#age = 2026 - int(birth_year)
#print("You are " + str(age) + " years old.")

#first = input("first: ")
#second = input("second: ")
#sum = float(first) + float(second)
#print("Sum: " + str(sum))   
# 
#print(10 + 3)   # 13
#print(10 - 3)   # 7
#print(10 * 3)   # 30
#print(10 / 3)   # 3.333...
#print(10 // 3)  # 3   (ganzzahlige Division)
#print(10 % 3)   # 1   (Rest)
#print(2 ** 3)   # 8   (hoch)
# 
#alter = 17
#if alter >= 18:
#    print("volljährig")
#elif alter >= 16:
#    print("fast")
#else:
#    print("minderjährig")  

#for i in range(5):        # 0,1,2,3,4
#    print(i)

#x = 0
#while x < 3:               # solange x kleiner 3
#    print(x)
#    x = x + 1    








#Week 2

x= 100
var= "mathisboss"
print(x*var)

if x == 100:
    print("mathisboss is written 100 times")
else: 
    print("mathisboss is not written 100 times")

# print("Hello, World!")
# x = 1
# student_name = "Mathis"
# print(student_name)
# rating = 4.99
# is_raining = True
# print(len(student_name))
# print(student_name[0])
# course = "Python for Beginners"
# print(course.upper())
# temperature = 35
# if temperature > 30:
#    print("It's a hot day")
# if 10 == "10":
#    print("a")
# elif "bag" > "apple" and "bag" > "cat":
#    print("b")
# else:
#    print("c")
# succeful = True
# for number in range(3):
# if succeful:
# print("Attempt")
# break


# number = 100000000000000000000000000
# while number > 0:
# print(number)
# number //= 2

import time
from eth_hash.auto import keccak
print("0x" + keccak("".encode("utf-8")).hex())
s1 = "The Senate shall be composed of two Senators from each State, chosen by the Legislature thereof, for six Years; and each Senator shall have one Vote."
s2 = "The Senate shall be composed of two Senators from each State, chosen by the Legislature thereof, for six Years, and each Senator shall have one Vote."
print("0x" + keccak(s1.encode("utf-8")).hex())
print("0x" + keccak(s2.encode("utf-8")).hex())
i = 0
while True:
    h = keccak(str(i).encode("utf-8")).hex()
    if h.startswith("0"):
        print("String:", i, "Hash: 0x" + h)
        break
    i += 1


def finde(nullen):
    ziel = "0" * nullen
    start = time.time()
    i = 0
    while True:
        h = keccak(str(i).encode("utf-8")).hex()
        if h.startswith(ziel):
            dauer = time.time() - start
            print(
                f"{nullen} Nullen: String = {i}, Hash = 0x{h}, Versuche = {i+1}, Zeit = {dauer:.2f} s")
            return
        i += 1


finde(5)   # a)
finde(6)   # b)
finde(7)   # b) 


