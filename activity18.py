"""
Maximillian White Activity 18
8/3/2022
"""
print("\n\n\t-------------- FOR LOOP -------------- ")
print("Example 11) for-else statement")
for n in range(7):
    print(n)
else:
    print("DONE!")
print("Example 10) use for loop to print num from 10 to -5 and skip numbers that are multiples of 4")
for num in range(10,-5,-1):
    if num%4 == 0:
        continue
    print(num)
    
print("Example 9) Nesting for loop and if statement")
for counter in range(10):

    if counter ==5:
        continue
    print("Now counting: ", counter)
    print("=*=*=*=*=*=*=*=*=*=*=*=")

print("Example 8) for loop in a string ")
msg="Hello World!"
for m in msg:
    print("character = ", m)
print("Example 7) for loop in a list")
colors =['yellow','red','blue','green','white','black']
for c in colors:
    print("color = ", c)

print("Example 6) for loop decrement counting")
for z in range(20,-10, -5):
    print("z = ", z)
print("Example 5) for loop with three arguments")
for y in range(2,30,3):
    print("y = ", y)

print("Example 4) for loop basics")
for x in range(1,5):
    print("Counting: ", x)


    

print("\n\t-------------- CONDITIONAL STATEMENT -------------- ")
# Example 3) and, or operators
age = int(input("Enter an age: "))
gender = input("Type M for male or F for female: ")
if age == 5 and gender =="M" or gender =="m":
    print("5 year-old boy!")
elif age== 5 and gender =="F" or gender =="f":
    print("5 year-old girl!")
else:
    print("Any other ages rather than 5")



# if-elif-else statement example 2)

if age == 5:
    print("Age = 5. Height should be around 102 cm and weight 14.8 lbs")
elif age==6:
    print("Age = 6. Height should be around 108 cm and weight 16.3 lbs")
elif age==7:
    print("Age = 7. Height should be around 113 cm and weight 18.0 lbs")
else:
    print("Unable to display height and weight")

# if statement, example1) check if an age in an adult using if-else

if age>=21:
    print("You are an adult!")
else:
    print("You are underage")
print("Welcome to the club!")
