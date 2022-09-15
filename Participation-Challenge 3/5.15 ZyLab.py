#Anthony Nguyen
#PSID1938087

# 5.15 LAB: Smallest number
# Write a program whose inputs are three integers, and whose output is the smallest of the three values.
#
# Ex: If the input is:
#
# 7
# 15
# 3
# the output is:
#
# 3

first = int(input())
second = int(input())
third = int(input())

# calculate smallest n
smallest = first
if second < smallest:
    smallest = second
if third < smallest:
    smallest = third

print(smallest)