#PROJECT 1: Creating a brand name from names

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

print("Welcome home")