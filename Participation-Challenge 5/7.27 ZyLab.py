#Anthony Nguyen
#PSID1938087

# 7.27 LAB: Multiples of ten in a list
# Write a program that reads a list of integers, and outputs whether the list contains all multiples of 10,
# no multiples of 10, or mixed values. Define a function named is_list_mult10 that takes a list as a parameter,
# and returns a boolean that represents whether the list contains all multiples of ten. Define a function named is_
# list_no_mult10 that takes a list as a parameter and returns a boolean that represents whether the list contains
# no multiples of ten.

# Then, write a main program that takes an integer, representing the size of the list,
# followed by the list values. The first integer is not in the list.

# Ex: If the input is:
# 5
# 20
# 40
# 60
# 80
# 100

# the output is:
# all multiples of 10

# Ex: If the input is:
# 5
# 11
# -32
# 53
# -74
# 95

# the output is:
# no multiples of 10

# Ex: If the input is:
# 5
# 10
# 25
# 30
# 40
# 55

# the output is:
# mixed values

# The program must define and call the following two functions. is_list_mult10() returns true if all integers in the
# list are multiples of 10 and false otherwise. is_list_no_mult10() returns true if no integers in the list are
# multiples of 10 and false otherwise.
# def is_list_mult10(my_list)
# def is_list_no_mult10(my_list)

# function to check if all values of list is multiple of 10
def is_list_mult10(my_list):
    for i in my_list:
        if i % 10 != 0:
            return False
    return True


def is_list_no_mult10(my_list):
    for i in my_list:
        if i % 10 == 0:
            return False
    return True


if __name__ == '__main__':
    num = int(input())
    my_list = []
    for i in range(0, num):
        my_list.append(int(input()))

    is_multiple = is_list_mult10(my_list)
    is_not_Multiple = is_list_no_mult10(my_list)

    if (is_multiple == True) and (is_not_Multiple == False):
        print("all multiples of 10")

    elif is_multiple == False and is_not_Multiple == True:
        print("no multiples of 10")

    else:
        print("mixed values")