#Anthony Nguyen
#PSID1938087

# 3.18 Painting a wall

# Program Specifications Write a program to calculate the cost to paint a wall.
# Amount of required paint is based on the wall area. Total cost includes paint and sales tax.

# Note: This program is designed for incremental development.
# Complete each step and submit for grading before starting the next step.
# Only a portion of tests pass after each step but confirm progress.

# Step 1 (2 pts). Read from input wall height, wall width, and cost of one paint can (floats).
# Calculate and output the wall's area to one decimal place using print(f"Wall area: {wall_area:.1f} sq ft");. Submit for grading to confirm 1 test passes.

# Ex: If the input is:

# 12.0
# 15.0
# 29.95
# the output is:

# Wall area: 180.0 sq ft
# Step 2 (2 pts). Calculate and output the amount of paint needed to three decimal places. One gallon of paint covers 350 square feet. Submit for grading to confirm 2 tests pass.

# Ex: If the input is:

# 12.0
# 15.0
# 29.95
# the output is:

# Wall area: 180.0 sq ft
# Paint needed: 0.514 gallons
# Step 3 (2 pts). Calculate and output the number of 1 gallon cans needed to paint the wall. Extra paint may be left over. Hint: Use ceil() from the math module to round up to the nearest gallon (int). Submit for grading to confirm 4 tests pass.

# Ex: If the input is:

# 12.0
# 15.0
# 29.95
# the output is:

# Wall area: 180.0 sq ft
# Paint needed: 0.5142 gallons
# Cans needed: 1 can(s)
# Step 4 (4 pts). Calculate and output the paint cost, sales tax of 7%, and total cost. Dollar values are output with two decimal places. Submit for grading to confirm all tests pass.

# Ex: If the input is:

# 8.0
# 8.0
# 49.20
# the output is:

# Wall area: 64.0 sq ft
# Paint needed: 0.183 gallons
# Cans needed: 1 can(s)
# Paint cost: $49.20
# Sales tax: $3.44
# Total cost: $52.64

from math import ceil

height = float(input())
width = float(input())

area = height * width
paint_needed = area / 350
cans = int(round(paint_needed))

print(f"Wall area: {area:.1f} sq ft")
print(f"Paint needed: {paint_needed:.3f} gallons")
print('Cans needed: ' + str(cans) + ' can(s)')

paintCost = float(input())
print(f"Paint cost: ${paintCost:.2f}")

salesTax = float(0.07 * paintCost)
print(f"Sales tax: ${salesTax:.2f}")

totalCost = float(paintCost + salesTax)
print(f"Total cost: ${totalCost:.2f}")