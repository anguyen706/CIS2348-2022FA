#Anthony Nguyen
#PSID1938087

# 7.20 LAB: A jiffy
# A "jiffy" is the scientific name for 1/100th of a second.
# Define a function named jiffies_to_seconds that takes the number of
# "jiffies" as a parameter, and returns the number of seconds.
# Then, write a main program that reads the number of jiffies (float) as an input,
# calls function jiffies_to_seconds() with the input as argument,
# and outputs the number of seconds.

# Output each floating-point value with three digits after the decimal point,
# which can be achieved as follows:
# print(f'{your_value:.3f}')

# Ex: If the input is:
# 15.25

# the output is:
# 0.152

# The program must define and call the following function:
# def jiffies_to_seconds(user_jiffies)

def jiffies_to_seconds(user_jiffies):
    return user_jiffies / 100

def main():
    jiffies = float(input())
    sec = jiffies_to_seconds(jiffies)
    print(f'{sec:.3f}')

if __name__ == '__main__':
    main()
