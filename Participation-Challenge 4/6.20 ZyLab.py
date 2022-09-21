#Anthony Nguyen
#PSID1938087

# 6.20 LAB: Countdown until matching digits
# Write a program that takes in an integer in the range 11-100 as input. The output is a countdown starting from the integer, and stopping when both output digits are identical.
#
# Ex: If the input is:
#
# 93
# the output is:
#
# 93
# 92
# 91
# 90
# 89
# 88
# Ex: If the input is:
#
# 11
# the output is:
#
# 11
# Ex: If the input is:
#
# 9
# or any value not between 11 and 100 (inclusive), the output is:
#
# Input must be 11-100

n = int(input())

if 11 <= n <= 100:
    while n % 11 != 0:
        print(n)
        n -= 1
    print(n)
else:
    print('Input must be 11-100')