
def kg_to_lbs(weight):
    return weight / 0.45

def lbs_to_kg(weight):
    return weight * 0.45

def F_to_C(temperature):
    return(temperature-32)*(5/9)

def C_to_F(temperature):
    return(temperature * 9/5) + 32

def find_max(list_numbers):

    max_number=list_numbers [0]

    for item in list_numbers:
        if item > max_number:
            max_number = item
    return(max_number)


