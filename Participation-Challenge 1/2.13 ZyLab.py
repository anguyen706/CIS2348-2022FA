#Anthony Nguyen
#PSID1938087

# 2.13 Driving Cost
# Driving is expensive. Write a program with a car's gas mileage (miles/gallon)
# and the cost of gas (dollars/gallon) as floating-point input, and output the gas cost for 20 miles, 75 miles, and 500 miles.

#Output each floating-point value with two digits after the decimal point, which can be achieved as follows:
#print(f'{your_value1:.2f} {your_value2:.2f} {your_value3:.2f}')

# Ex: If the input is:
# 20.0
# 3.1599
# where the gas mileage is 20.0 miles/gallon and the cost of gas is $3.1599/gallon, the output is:

# 3.16 11.85 79.00
# Note: Real per-mile cost would also include maintenance and depreciation.

total_dist = float(input())
per_gal = float(input())
per_mi = per_gal / total_dist
your_value1 = per_mi * 20
your_value2 = per_mi * 75
your_value3 = per_mi * 500

print(f'{your_value1:.2f} {your_value2:.2f} {your_value3:.2f}')

