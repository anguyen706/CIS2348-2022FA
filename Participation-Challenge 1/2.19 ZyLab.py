#Anthony Nguyen
#PSID1938087

# 2.19 Cooking Measurement Converter

# Output each floating-point value with two digits after the decimal point, which can be achieved as follows:
# print(f'{your_value:.2f}')


# (1) Prompt the user for the number of cups of lemon juice, water, and agave nectar needed to make lemonade.
#  Prompt the user to specify the number of servings the recipe yields. Output the ingredients and serving size. (Submit for 2 points).

# Note: This zyLab outputs a newline after each user-input prompt. For convenience in the examples below, the user's input value is shown on the next line, but such values don't actually appear as output when the program runs.

# Enter amount of lemon juice (in cups):
# 2
# Enter amount of water (in cups):
# 16
# Enter amount of agave nectar (in cups):
# 2.5
# How many servings does this make?
# 6

# Lemonade ingredients - yields 6.00 servings
# 2.00 cup(s) lemon juice
# 16.00 cup(s) water
# 2.50 cup(s) agave nectar
# (2) Prompt the user to specify the desired number of servings. Adjust the amounts of each ingredient accordingly, and then output the ingredients and serving size. (Submit for 4 points, so 6 points total).

# How many servings would you like to make?
# 48

# Lemonade ingredients - yields 48.00 servings
# 16.00 cup(s) lemon juice
# 128.00 cup(s) water
# 20.00 cup(s) agave nectar
# (3) Convert the ingredient measurements from (2) to gallons. Output the ingredients and serving size. Note: There are 16 cups in a gallon. (Submit for 2 points, so 8 points total).

# Lemonade ingredients - yields 48.00 servings
# 1.00 gallon(s) lemon juice
# 8.00 gallon(s) water
# 1.25 gallon(s) agave nectar

#input the number so cups of lemon juice, water and agave nectar
cups_lemon_juice = float(input('Enter amount of lemon juice (in cups):\n'))
cups_water = float(input('Enter amount of water (in cups):\n'))
cups_agave_nectar = float(input('Enter amount of agave nectar (in cups):\n'))
# input the number of servings the recipe yields
cups_serving = float(input('How many servings does this make?\n'))

# display the input values
print('\nLemonade ingredients - yields %.2f servings' %(cups_serving))
print('%.2f cup(s) lemon juice' %(cups_lemon_juice))
print('%.2f cup(s) water'%(cups_water))
print('%.2f cup(s) agave nectar'%(cups_agave_nectar))

# input the desired number of servings
cups_serving_needed = float(input('\nHow many servings would you like to make?\n'))

# calculate the amount of each ingredient needed for 1 cup
lemon_juice_for_one = cups_lemon_juice/cups_serving
water_for_one= cups_water/cups_serving
agave_nectar_for_one = cups_agave_nectar/cups_serving

# calculate the amounts of each ingredient needed for desired servings
cups_lemon_juice_needed = lemon_juice_for_one*cups_serving_needed
cups_water_needed = water_for_one*cups_serving_needed
cups_agave_nectar_needed = agave_nectar_for_one*cups_serving_needed

# display the calculated amount of ingredients
print('\nLemonade ingredients - yields %.2f servings' %(cups_serving_needed))
print('%.2f cup(s) lemon juice' %(cups_lemon_juice_needed))
print('%.2f cup(s) water'%(cups_water_needed))
print('%.2f cup(s) agave nectar'%(cups_agave_nectar_needed))

# convert the calculated amount from cups to gallons (16 cups = 1 gallon)
gallons_lemon_juice = cups_lemon_juice_needed/16
gallons_water = cups_water_needed/16
gallons_agave_nectar = cups_agave_nectar_needed/16

# display the calculated amount of ingredients
print('\nLemonade ingredients - yields %.2f servings' %(cups_serving_needed))
print('%.2f gallon(s) lemon juice' %(gallons_lemon_juice))
print('%.2f gallon(s) water'%(gallons_water))
print('%.2f gallon(s) agave nectar'%(gallons_agave_nectar))
