#Anthony Nguyen
#PSID1938087

# 2.15 Using Math Functions
# Given three floating-point numbers x, y, and z,
#     1) output x to the power of z,
#     2) x to the power of (y to the power of z),
#     3) the absolute value of (x minus y),
#     4) and the square root of (x to the power of z).

# Output each floating-point value with two digits after the decimal point, which can be achieved as follows:
# print(f'{your_value1:.2f} {your_value2:.2f} {your_value3:.2f} {your_value4:.2f}')

# Ex: If the input is:

# 5.0
# 1.5
# 3.2
# Then the output is:

# 172.47 361.66 3.50 13.13

import math
x = float(input())
y = float(input())
z = float(input())

your_value1 = math.pow(x, z)
your_value2 = math.pow(x, math.pow(y, z))
your_value3 = math.fabs(x - y)
your_value4 = math.sqrt(math.pow(x, z))


print(f'{your_value1:.2f} {your_value2:.2f} {your_value3:.2f} {your_value4:.2f}')