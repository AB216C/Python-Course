#Variables
day_name = "Tuesday"
temp = -15
month = "December"

print(f"Today, it is {day_name}, the month of {month} and the temperature is {temp}")

#Boolean with True

light_is_on = True

if light_is_on:
    print("Welcome Home")
    print("Get ready to make some noise and party")
    print("Jesus, Allelluia")
else:
    print("stay outside")
#Boolean with False
light_is_on = False

if light_is_on:
    print("Welcome Home")
    print("Get ready to make some noise and party")
    print("Jesus, Allelluia")
else:
    print("stay outside")

#Boolean with Comparison

age = int(input("How old are you?\n"))

if age >= 18:
    print("You are adult")
else:
    print("you are young")

#Boolean with Comparison
age = 23
if age >= 18:
    print("You are adult")
else:
    print("you are young")
#checking odd and even numbers
# True for odd and false for even numbers

number = 4
if int(number%2)==0:
    print("False")
else:
    print("True")
#using input() function
# True for odd and false for even numbers

number = int(input("which number are you trying?\n"))

if number%2==0:
    print("False")
else:
    print("True")
#randomization 1
random_number = random.randint(1,8)

if random_number == random.randint(1,3):
    print("Yes")
elif random_number == random.randint(4,6):
    print("No")
else:
    print("Maybe")

#randomization 2

answer = random.randint(1,3)

if answer == 1:
    print("Yes")
elif answer == 2:
    print("No")
else:
    print("Maybe")

#randomization 3

lucky_number = random.randint(1,100)

fortune_number = random.randint(1,3)
fortune_text = ''
if fortune_number == 1:
    fortune_text = 'you are getting married'
elif fortune_number == 2:
    fortune_text = 'you are getting engaged soon'
else:
    fortune_text = 'sorry, please try next time'
print(f"Your lucky number is: {lucky_number} and your fortune text is: {fortune_text}" )


#List functions
fav_numbers = [1, 3, 6]
print(fav_numbers[-1])

fav_movies = ["Catuni", "Dance"]

fav_movies.append("Iron_Man")
fav_movies.insert(1, "My_heart")
fav_movies.append("The boss")
fav_movies.insert(4,"1 by 1")
del(fav_movies[0])
del(fav_movies[1])
del(fav_movies[1])
del(fav_movies[1])
del(fav_movies[1])

print(fav_movies)

#basic calculator
a = int(input("num1\n"))

b = float(input("num2\n"))

sum= a + b
print(f"Total will be:{sum}")

# using "find", "replace", and "in" a string

course = "Python for beginners"

print(course.find('y'))
print(course.find('beg'))
print(course.find('Python'))
print(course.find('python'))

new_title=course.replace('for','4')
print(new_title)
print(course.replace('beg','xy'))
print(course)

print("python" in course)
print("Python" in course)
#Mathematical operators

print(10//2)
print(10%2)
print(10/2)

print(10*2)
print(10**2)
#These operators return boolean
x = 4<3
y = 4==3
z=4>3
print(x)
print(y)
print(z)


price = 5

print(price < 2 or price < 4)
print(price == 5 and price > 4)
print(price < 4 or price > 7)
print( not price > 10)
print(not price > 2)

# if statements
temperature=int(input("What's the temperature in degree celsius?\n"))

if temperature > 30:
    print("Wait, it is too hot")
    print("Drink too much water")
    print("if you feel not okay, contact emergency")
elif temperature <= 20:
    print("It is too cold")
    print("Put on warm clothes and wear gloves")
else:
    print("We got a good weather")

# while loops: Printing sequence of numbers in a short time
print(1)
print(2)
print(3)
print(4)
print(5)
# #While loop
# #tips: i = Initial number
#        while = add condition
#            i = i + x = repetition desired
i = -10
while i <=100:
    print(i)
    i = i + 1

k = 0
while k <=50:
    print(k)
    k = k + 1

j = -2
while j <=40:
    print(j)
    j = j + 5

x = 2
while x <=100:
    print(x*"*")
    x = x + 1

z = 1
while z <=50:
    print(z*"Ndiyo")
    z = z + 1

# Refreshing list exercises
fruits = ["Mango", "Apple", "Banana", "Grapes", "Banana"]
print("Mango" in fruits)
print(fruits[1:4])
print(fruits)
fruits.insert(1, 'Peach')
print(fruits)

# list & list methods

fruits = ["apple", "banana", "pineapple", "Peach" ]
fruits.append("strawberry")
fruits.insert(0,"maji")
fruits.remove("apple")
fruits.insert(1,"Apple")

print( "Apple" in fruits)
print(fruits)
print("Mango" in fruits)
print("Embe" in fruits)
print(1 in fruits)
print(fruits[3])
print(fruits[0:2])
print(fruits[1:4])

# for loop function: Accessing individual items in the list

list = [3, 5, 5, 34, 56]
for number in list:
    print(number)

my_list = ["birds", "Ugali", "Chicken","Milk"]
for item in my_list:
    print(item)

#range: creating a sequence of numbers using range function
#range=can store a certain sequence of numbers
#range=can store a sequence of numbers or objects in a list
# this list or sequence can be accessed using for loop

numbers = range(12)
for digits in numbers:
    print(digits)

my_numbers = range(5,12)
for digit in my_numbers:
    print(digit)

# #Exception1: Adding a number in a range as an interval
my_list = range(5,12,3)
for digit in my_list:
    print(digit)

my_list = range(5,22,4)
for digit in my_list:
    print(digit)

#Exception2: Calling individual digits from a range without storing them

for digit in range(20):
    print(digit)

#Tuple: a lit that is immutable
#Tuple: once a list is made, it can't get changed by anyone
#With Tuple, you can only show index of a numuber and count frequence of a number

my_list = (3,4,5,5,34,56)
print(my_list.index(5))
print(my_list.count(5))
print(my_list.count(0))
print(my_list.count(34))

while loop
for loop
range
list and list methods

i = 100
while -10 <= i <=100:
    print(i)
    i = i - 1

numbers = range(10)
for number in numbers:
    print(numbers)

my_list = [1,3,4,5,6]
for item in my_list:
    print(item)

my_list2 = ["Jane", "Joseph", "Jin"]
for item2 in my_list2:
    print(item2)

numbers= range(1,100,2)
for items in numbers:
    print(items)

i = 100
while -10 <= i <=100:
    print(i*"x")
    i = i - 1

my_list3= ["Jan", "Jess", 1, 4, "moja", "mbili"]
print(5 in my_list3)
print(my_list3[3])
print(my_list3[2:5])
my_list3.insert(0,"tisa")
my_list3.append("GEN-Z")
my_list3.remove(1)
print(my_list3)
my_list3.sort()