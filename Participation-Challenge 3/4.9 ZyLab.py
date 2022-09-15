# Anthony Nguyen
# PSID1938087

# 4.9 LAB: Guess the random number
# Given the code that reads a list of integers, complete the number_guess() function, which should choose a random number between 1 and 100 by calling random.randint() and then output if the guessed number is too low, too high, or correct.
#
# Import the random module to use the random.seed() and random.randint() functions.
#
# random.seed(seed_value) seeds the random number generator using the given seed_value.
# random.randint(a, b) returns a random number between a and b (inclusive).
# For testing purposes, use the seed value 900, which will cause the computer to choose the same random number every time the program runs.
#
# Ex: If the input is:
#
# 32 45 48 80
# the output is:
#
# 32 is too low. Random number was 80.
# 45 is too high. Random number was 30.
# 48 is correct!
# 80 is too low. Random number was 97.

import random # importing random module

def number_guess(num):
    rand_num=random.randint(1,100) # generating a random number between 1-100
    if(num > rand_num):
        print("{} is too high. Random number was {}.".format(num,rand_num))
    elif(num < rand_num):
        print("{} is too low. Random number was {}.".format(num,rand_num))
    else:
        print("{} is correct!".format(num))

if __name__ == '__main__':
    random.seed(900);

    user_input=input()
    tokens=user_input.split()
    for token in tokens:
        num=int(token)
        number_guess(num) # calling the number_guess() func