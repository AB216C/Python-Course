#PROJECT 1: Creating a brand name from names

print("Welcome, My brand Name generator is highlighted below")

city_name = input("what is the city you grew up in?\n")
pet_name = input("What is the name of your pet?\n")

print("My brand name is "+ city_name+ " " +pet_name)
#string
print("Hello"[2])
print("1234\n")
print("1234"+ "1234\n")
#integer
print(1234)
print(1234 + 1234)
#float

3.2234
#Boolean

True or False

#EXERCISES ON VARIABLES
street_name = "Ferdinand Niyongira"
print(street_name[4] + street_name[7])
num_char = str(len("Bathroom"))
print(num_char)
num_char2 = str(len(input("What is your age?")))
print(num_char2)
print("That name has " + num_char + " " + "characters")
print("My age has " + num_char2 + " " + "characters")
print(type(num_char))

a = 33333
# print(type(a))
# print(456.5+a)
# print(456.2 +float(455))
# print((456.2) + (455))
#
# a = 3
# b = 9
# print(str(a) + str(b))
# print(a+b)
# Two digit exercise
# Condition = Input two number
# output = 1 number

two_digit = input()

digit1 = int(two_digit[0])
digit2 = int(two_digit[1])

print(digit1)
print(digit2)
print(digit1 + digit2)


# BMI CALCULATOR BMI = WEIGHT/HEIGHT**2

height = float(input())
weight = int(input())

bmi = int(weight/(height * height))
print(bmi)

#rounding and shopping the final result

print(8/3)
print(8//3)
print(round(8/3))
print(int(8/3))
#recording scores during game sessions

score = 0
score -= 1
score -= 2
score += 3
print(score)

height = 1.6
winner = True

#Concatenate string, float numbers, and boolean
#Concatenate string, float numbers, and boolean using f-string function

print("your are winning because your height is " + str(height) + " meter " + "then you should be called a winner " + str(winner))
print(f"you are double winning because your height is {height} meter then you should be called a double winner {winner}")

#Project 2: Calculating number of weeks left based on how old you are. Considering the age limit is 90 years.

# OUTPUT: You have x weeks left.

age = int(input())

num_weeks_per_year = 52
num_weeks_in_90_years = 52 * 90
num_weeks_left = num_weeks_in_90_years - (num_weeks_per_year * age)

print(f"You have {num_weeks_left} left")

# DAY 2 FINAL PROJECT- TIP CALCULATOR
# PROBLEM LOOK LIKE THIS:
# A WELCOME MESSAGE TO THE TIP CALCULATOR
# Total bill
# HOW MUCH TIP IN PERCENTAGE WOULD YOU LIKE TO GIVE, 10, 12, 14, 15?
# How many people to split the bill
# final line: Each person should pay


print("Welcome to the tip calculator")
print("What was your total bill? $")
total_bill = int(input())

print("How much tip would you like to give? %")
tip_percentage = int(input())

print("How many people to split the bill")
num_people_split_bill = int(input())

bill_after_tip = total_bill + (total_bill * float((tip_percentage/100)))

tip_per_each =round((bill_after_tip / num_people_split_bill),2)
final_tip_each = "{:.2f}".format(tip_per_each)

print(f"Each Person should pay:$ {final_tip_each}")


# Writing rollercoaster instructions

print("Welcome all to the most famous Rollercoaster in North West of South Carolina")

print("what is your height? cm\n")

height = int(input())

if height == 120:
 print("You can board now")
else:
 print("Sorry you can not board today, wait till you get taller")


#Using % sign(Modulo) to tell if numbers are even or odd

print(4%2)
print(5%4)
print(8%2)
print(8%3)

number = int(input())

if number%2 == 0:
 print("This is even number")
else:
 print("This is odd number")

 # Writing rollercoaster instructions

 print("Welcome all to the most famous Rollercoaster in North West of South Carolina")

 print("what is your height?cm")

 print("what is your age")

 height = int(input())
 age = int(input())

 if height >= 120:
  print("You can board now")
 elif age < 16:
  print("Pay $5")
 elif 16 <= age <= 20:
  print("Pay $10")
 elif age > 20:
  print("Pay $20")
 else:
  print("Sorry you can not board today, wait till you get taller")


# BMI CALCULATOR BMI = WEIGHT/HEIGHT**2
print("what is your height?cm")
height = float(input())
print("what is your weight?kg")
weight = int(input())

bmi = int(weight/(height * height))

if bmi <= 18:
 print (f"Your bmi is {bmi}, You are underweight.")
elif 18 <= bmi <= 22:
 print(f"Your bmi is {bmi}, you have a normal weight")
elif 22 <= bmi <= 28.5:
 print(f"Your bmi is {bmi}, You are slightly overweight")
elif 28.5 <= bmi <= 32.56:
 print(f"Your bmi is {bmi}, You are obese")
else:
 print(f"Your bmi is {bmi}, You are clinically obese")

#Leap Year Calculator.NESTED CONDITIONS.
print("Welcome to the Leap Year calculator")

print("Enter the Year you are interested in")
year = int(input())

if year % 4 == 0:
 if year % 100 ==0:
   if year % 400 == 0:
       print("Leap year")
   else:
     print("Not Leap year")
 else:
   print("Leap Year")
else:
  print("Not Leap year")

  # Continuation: Roller Coaster project: ADDING EXTRA CONDITIONS

print("Welcome all to the most famous Rollercoaster in North West of South Carolina")

height = int(input("What's your height? cm "))
bill = 0
if height >= 120:
 print("You can board now")
 age = int(input("what's your age? "))
 if age < 12:
  print("Child tickets are $5 ")
  bill = 5
 elif age <= 20:
  print("Youth tickets are $10")
  bill = 10
 else:
  print("Adult tickets are $20")
  bill = 20
 photo = input("Do you want photo taken Y or NO ")
 if photo == "Y":
  bill = bill + 3
  print(f"Total bill will be {bill}")
else:
 print("Sorry you can not board today, wait till you get taller")

 # Python Pizza project
 print("Thank you for choosing Python Pizza deliveries!")
 size = input("What size of pizza do you want  S, M, or L?\n")
 add_pepperoni = input("Do you want pepperoni, Y or N?\n")
 add_extra_cheese = input("Do you want extra cheese, Y or N?\n")
 bill = 0
 if size == "S":
  print("Small pizza cost $15")
  bill = 15
  if add_pepperoni == "Y":
   bill = bill + 2
   if add_pepperoni == "N":
    bill = bill + 0
    if add_extra_cheese == "Y":
     bill = bill + 1
 elif size == "M":
  print("Medium pizza cost $20")
  bill = 20
  if add_pepperoni == "Y":
   bill = bill + 3
   if add_pepperoni == "N":
    bill = bill + 0
    if add_extra_cheese == "Y":
     bill = bill + 1
 elif size == "L":
  print("Large pizza cost $25")
  bill = 25
  if add_pepperoni == "Y":
   bill = bill + 3
   if add_pepperoni == "N":
    bill = bill + 0
    if add_extra_cheese == "Y":
     bill = bill + 1
 else:
  print("Please double check the menu for more info")
 print(f"Your final bill for today  will be ${bill}")
#WORKING ON ROLLERCOSTER PROJECT-ADDING OPERATOR
 print("Welcome all to the most famous Rollercoaster in North West of South Carolina")

 height = int(input("What's your height? cm "))
 bill = 0
 if height >= 120:
  print("You can ride rollercoaster")
  age = int(input("what's your age? "))
  if age < 12:
   print("Child tickets are $5 ")
   bill = 5
  elif age <= 20:
   print("Youth tickets are $10")
   bill = 10
  elif age >= 45 and age <= 55:
   print("Your got a free ticket")
   bill = 0
  else:
   print("Adult tickets are $20")
   bill = 20
  photo = input("Do you want photo taken Y or NO ")
  if photo == "Y":
   bill = bill + 3
   print(f"Total bill will be:$ {bill}")
 else:
  print("Sorry you can not board today, wait till you get taller")

# Roller coaster project continued with operators added. Extra condion and, or and not
print("Welcome all to the most famous Rollercoaster in North West of South Carolina")

height = int(input("What's your height? cm "))
bill = 0
if height >= 120:
 print("You can ride rollercoaster")
 age = int(input("what's your age? "))
 if age < 12:
  print("Child tickets are $5 ")
  bill = 5
 elif age <= 20:
  print("Youth tickets are $10")
  bill = 10
 elif age >=45 and age <= 55:
  print("Your got a free ticket")
  bill = 0
 else:
  print("Adult tickets are $20")
  bill = 20
 photo = input("Do you want photo taken Y or NO ")
 if photo == "Y":
  bill = bill + 3
  print(f"Total bill will be:$ {bill}")
else:
 print("Sorry you can not board today, wait till you get taller")

#Exciting project-LOVE CALCULATOR
print("Love calculator is calculating your score.....")

name1 = input("what is your name?\n")
name2 = input("What is your name?\n")

combined_names = name1 + name2

lower_names = combined_names.lower()

t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")

first_digit = t + r + u + e

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")

second_digit = l + o + v + e

score = int(str(first_digit) + str(second_digit))

if score < 10 and score > 90:
    print(f" Your score is {score}, you go together like coke and mentos")
elif score > 40 and score <50:
    print(f"Your score is {score}, you are alright together")
else:
    print(f"Your score is {score}")

#practicing LOVE CALCULATOR

name1 = input("What is your name?\n")
name2 = input("What is your lady's name?\n")

combined_names = name1 + name2
lower_names = combined_names.lower()

u = lower_names.count("u")
r = lower_names.count("r")
u = lower_names.count("u")
k = lower_names.count("k")
u = lower_names.count("u")
n = lower_names.count("n")
d = lower_names.count("d")
o = lower_names.count("o")

first_digit = u + r + k + u + n + d + o

n = lower_names.count("n")
y = lower_names.count("y")
a = lower_names.count("a")
r = lower_names.count("r")
w = lower_names.count("w")
o = lower_names.count("o")

second_digit = n + y + a + r + w + o

score = int(str(first_digit) + str(second_digit))

if score < 20 or score > 70:
    print(f"Your score is {score}, muzarambana")
elif score >=45 and score <=60:
    print(f"Your score is {score}, kandi biriko biraza")
else:
    print(f"Your score is {score}, nukwiminjiramo agafu")

#Island project

print("Welcome to Treasure Island")
print("Your mission is to find the treasure")

game1 = input("Where would you like to move, Left or right?\n").lower()
if game1 == "left":
    game2 = input("What next? you want to swim or wait\n").lower()
    if game2 == "wait":
        game3 = input("What color you prefer most? blue, red, yellow\n").lower()
        if game3 == "red":
            print("Game over")
        elif game3 == "blue":
            print("Game over")
        elif game3 == "yellow":
            print("You are a winner")
        else:
            print("Game over")
    else:
        print("Game over")
else:
    print("Game over")

# Randomization and python list

import random

random_integer = random.randint(1, 4)
print(random_integer)

random_float = random.random()
print(random_float)

random_float = random.uniform(10, 90)
print(random_float)

random_float1 = random.random() * 5
# print(random_float1)

love_score = random.randint(1, 100)
print(love_score)

#Creating toss coin random game:

toss_coin = random.randint(0, 1)
if toss_coin == 1:
 print("Heads")
else:
 print("Tails")

# Project: Choosing a random party person to pay a bill

import random
list = input("what's your names?\n")
my_list = list.split(",")
num_list = len(my_list)

rand_choice= random.randint(0, num_list-1)

print(my_list[rand_choice])

#Working with list
united_states = ['Texas','Luisiana','Oklahoma','Minesota']
num_united_states = len(united_states)

# print(united_states[num_united_states-2])

#nested list
South_states = ['Texas','Luisiana','Oklahoma']
South_states[-1] = 'New Mexico'
North_states = ['Nebraska','Ohio','Iowa','Colorado']
North_states.append('Kansas')
# print(South_states, North_states)
# print(South_states)

#Challenge-Exercise
fruits =['Strawberries','Nectarines','Apples','Grapes','Peaches','Cherries','Pears']
vegetables = ['Spinach','Kale','Tomatoes','Celery','Potatoes']

dirty_dozen = [fruits, vegetables]
print(dirty_dozen)
print(dirty_dozen[0])
print(dirty_dozen[1])
print(dirty_dozen[1][1])
print(dirty_dozen[1][2])
print(dirty_dozen[0][1])


#LOOPS IN PYTHON

fruits=["Apple","Peach","Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " pie")
    print(fruits)

fruits = ["Apple", "Peach", "Pear"]

# difference in indentation
for fruit in fruits:
    print(fruit)
    print(fruit + " pie")
print(fruits)

#print, input functiion and inserting a function into another function

input("What is your name?")
input("What's your favorite car?")
input("What is your favorite color?")

#inserting a function into another function

print("Hello" + input("What is your name?")+ "!")

# Variables
name = input("what is your name?")

length=len(name)
print(length)

#exercises on Variables/Output is switched to variables

a = input()
b = input()

c = a
a = b
b = c

print("a: " + a)
print("b: " + b)

z = input()
x = input()

y = z
z = x
x = y

print("z: " + z)
print("x: " + x)

#calling variables

name = "Jack"
name2 = "Joseph"

print(name)
print(name2)

print("Welcome all to the most famous Rollercoaster in North West of South Carolina")

height = int(input("What's your height? cm "))
bill = 0
if height >= 120:
 print("You can board now")
 age = int(input("what's your age? "))
 if age < 12:
  print("Child tickets are $5 ")
  bill = 5
 elif age <= 20:
  print("Youth tickets are $10")
  bill = 10
 else:
  print("Adult tickets are $20")
  bill = 20
 photo = input("Do you want photo taken Y or NO ")
 if photo == "Y":
  bill = bill + 3
  print(f"Total bill will be {bill}")
else:
 print("Sorry you can not board today, wait till you get taller")