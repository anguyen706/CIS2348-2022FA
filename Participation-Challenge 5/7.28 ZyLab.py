#Anthony Nguyen
#PSID1938087

# 7.28 LAB: Output values in a list below a user defined amount - functions
# Write a program that first gets a list of integers from input. The input begins with an integer indicating the
# number of integers that follows. Then, get the last value from the input, and output all integers less than
# or equal to that value.

# Ex: If the input is:
# 5
# 50
# 60
# 140
# 200
# 75
# 100

# the output is:
# 50
# 60
# 75

# The 5 indicates that there are five integers in the list, namely 50, 60, 140, 200, and 75. The 100 indicates that
# the program should output all integers less than or equal to 100, so the program outputs 50, 60, and 75.

# Such functionality is common on sites like Amazon, where a user can filter results. Utilizing functions will help
# to make your main very clean and intuitive.

# Your code must define and call the following two functions:
# def get_user_values()
# def ints_less_than_or_equal_to_threshold(user_values, upper_threshold)

# Note: ints_less_than_or_equal_to_threshold() returns the new array.

def get_user_values(): #defining get_user_values function
    n=int(input()) #taking user input count n of numbers to be taken
    user_values=[] #declaring an array named user_values
    for i in range(n): #looping up to n values
        user_values.append(int(input())) #at each iteration appending user input value to user_values array
    upper_threshold=int(input()) #taking user input upper_threshold value
    return ints_less_than_or_equal_to_threshold(user_values, upper_threshold) #calling other function

def ints_less_than_or_equal_to_threshold(user_values, upper_threshold): #defining a function with parameters
    new_array=[] #declaring a new array
    for i in range(len(user_values)): #looping the values of user_values array
        if(user_values[i]<upper_threshold): #at each value of the user_values array compared with upper_threshold
            new_array.append(user_values[i]) #if value is less than upper_threshold then appending into new_array
    for i in range(len(new_array)): #looping through new_array values
        print(new_array[i]) #at each iteration printing the new_array values

get_user_values() #calling the get_user_values function