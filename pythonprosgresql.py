print("------------ Exercise a ------------")
numOfFruits = int(input("Enter the number of fruits: "))
fruits = []
for x in range(1, numOfFruits + 1):
    newFruit = input("Fruit %s : " %(x))
    fruits.append(newFruit)
print("User created a list of %s items and entered the values: %s" %(x,fruits))
print("\n ------------ Exercise b ------------")
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
if num1 == num2:
    num2 = int(input("Please enter a number that is different from number 1: "))
if num1 < num2:
    min = num1
    max = num2
if num1 > num2:
    min = num2
    max = num1
while max != min:
    print(min)
    min += 1
print("\n ------------ Exercise c ------------")
import math
r = int(input("Enter a radius: "))
h = int(input("Enter a height: "))
def volumeCylinder(h, r):
    v = round(((r*r)*math.pi*h), 2)
    return v
volume = volumeCylinder(h, r)
print("The volume with radius %s and height %s is %s" %(r,h,volume))

print("\n ------------ Exercise d ------------")
import random
rollAmount = int(input("How many times do you want to roll? "))
for x in range(1, rollAmount + 1):
    rollResults = random.randint(1,6)
    print("Roll %s = %s" %(x, rollResults))
print("\n ------------ End ------------ ")
