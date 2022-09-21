#Anthony Nguyen
#PSID1938087

# 6.23 LAB: Smallest and largest numbers in a list
# Write a program that reads a list of integers into a list as long as the integers are greater than zero, then outputs the smallest and largest integers in the list.
#
# Ex: If the input is:
#
# 10
# 5
# 3
# 21
# 2
# -6
# the output is:
#
# 2 and 21

n = int(input())

# Setting min amd max
minVal = n
maxVal = n

# Looping til input is positive
while(n>0):
    # Checking n is smaller than minVal
    if(minVal>n):
        minVal = n # Updating minVal

    # Checking n is larger than maxVal
    if(maxVal<n):
        maxVal = n # Updating maxVal

    # Reading a number
    n = int(input())

# printing minVal and maxVal
print(minVal,"and",maxVal)