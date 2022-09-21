#Anthony Nguyen
#PSID1938087

# 6.24 LAB: Output values in a list below a user defined amount
# Write a program that first gets a list of integers from input.
# The input begins with an integer indicating the number of integers that follow. Then, get the last value from the input, which indicates a threshold. Output all integers less than or equal to that last threshold value.
#
# Ex: If the input is:
#
# 5
# 50
# 60
# 140
# 200
# 75
# 100
# the output is:
#
# 50,60,75,
# The 5 indicates that there are five integers in the list, namely 50, 60, 140, 200,
# and 75. The 100 indicates that the program should output all integers less
# than or equal to 100, so the program outputs 50, 60, and 75.

# For coding simplicity, follow every output value by a comma, including the last one.
#

# Such functionality is common on sites like Amazon, where a user can filter results.

# reading a number
size = int(input())

# Creating a list
lst = []

# Looping for size times
for i in range(size):
    lst.append(int(input())) # Appending input to th end of list

# Reading threshold value
threshold = int(input())

# Looping through each value in list
for x in lst:
    if x < threshold: # Comparing x and threshold
        print(x,end=",") #value of x