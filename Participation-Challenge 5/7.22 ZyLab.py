#Anthony Nguyen
#PSID1938087

# 7.22 LAB: Convert to binary - functions
# Write a program that takes in a positive integer as input, and outputs a
# string of 1's and 0's representing the integer in binary. For an integer x,
# the algorithm is:

# As long as x is greater than 0
#    Output x % 2 (remainder is either 0 or 1)
#    x = x // 2
# Note: The above algorithm outputs the 0's and 1's in reverse order.
# You will need to write a second function to reverse the string.

# Ex: If the input is:
# 6

# the output is:
# 110

# The program must define and call the following two functions.
# Define a function named int_to_reverse_binary() that takes an integer
# as a parameter and returns a string of 1's and 0's representing the integer
# in binary (in reverse). Define a function named string_reverse() that takes
# an input string as a parameter and returns a string representing the input
# string in reverse.
# def int_to_reverse_binary(integer_value)
# def string_reverse(input_string)

def integer_to_reverse_binary(integer_value):  # function integer_to_reverse_binary
    output = ""
    while integer_value > 0:  # while loop run till integer value is greater than 0
        output += str(integer_value % 2)  # concat string
        integer_value //= 2  # divide number by 2
    return output


def reverse_string(input_string):  # function reverse_string
    output_string = ""
    i = 0
    while i < len(input_string):  # while loop run till input string length
        output_string = input_string[i] + output_string  # concat string
        i += 1
    return output_string


if __name__ == '__main__':
    integer_value = int(input(""))  # input integer value
    input_string = integer_to_reverse_binary(integer_value)  # call function integer_to_reverse_binary
    print(reverse_string(input_string))  # call function reverse_string