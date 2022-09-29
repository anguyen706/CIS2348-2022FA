#Anthony Nguyen
#PSID1938087

# 7.18 LAB: Driving costs - functions
# Write a function driving_cost() with input parameters miles_per_gallon,
# dollars_per_gallon, and miles_driven, that returns the dollar cost to drive
# those miles. All items are of type float. The function called with arguments
# (20.0, 3.1599, 50.0) returns 7.89975.

# Define that function in a program whose inputs are the car's miles per gallon
# and the price of gas in dollars per gallon (both float).
# Output the gas cost for 10 miles, 50 miles, and 400 miles,
# by calling your driving_cost() function three times.

# Output each floating-point value with two digits after the decimal point,
# which can be achieved as follows:
# print(f'{your_value:.2f}')

# Ex: If the input is:

# 20.0
# 3.1599
# the output is:

# 1.58
# 7.90
# 63.20
# Your program must define and call a function:
# def driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven)

def driving_cost(miles_per_gallon, dollars_per_gallon, driven_miles):
    return driven_miles / miles_per_gallon * dollars_per_gallon

if __name__ == '__main__':
    miles_per_gallon = float(input())
    dollars_per_gallon = float(input())

    print("%.2f" % (driving_cost(miles_per_gallon, dollars_per_gallon,10)))
    print("%.2f" % (driving_cost(miles_per_gallon, dollars_per_gallon,50)))
    print("%.2f" % (driving_cost(miles_per_gallon, dollars_per_gallon,400)))