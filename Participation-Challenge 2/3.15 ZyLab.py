#Anthony Nguyen
#PSID1938087

# 3.15 Input and formatted output: House real estate summary

# Sites like Zillow get input about house prices from a database and provide nice summaries for readers.
# Write a program with two inputs, current price and last month's price (both integers).
# Then, output a summary listing the price, the change since last month, and the estimated monthly mortgage computed as (current_price * 0.051) / 12.

# Output each floating-point value with two digits after the decimal point, which can be achieved as follows:
# print(f'{your_value:.2f}')

# Ex: If the input is:
# 200000
# 210000

# the output is:
# This house is $200000. The change is $-10000 since last month.
# The estimated monthly mortgage is $850.00.
# Note: Getting the precise spacing, punctuation, and newlines exactly right is a key point of this assignment.
# Such precision is an important part of programming.

current_price = int(input())
last_months_price = int(input())

change_in_price = current_price - last_months_price
monthly_mortgage = (current_price * 0.051) / 12

print(f'This house is ${current_price}. The change is ${change_in_price} since last month.')
print(f'The estimated monthly mortgage is ${monthly_mortgage:.2f}.')