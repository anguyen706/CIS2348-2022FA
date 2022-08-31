#Anthony Nguyen
#PSID1938087

# 2.20 Food Receipt

# Note: When accuracy is essential, floats are not used to represent currency due to rounding and accumulation errors.
# Python provides several primitives specifically developed to implement financial applications. However, these topics are beyond the scope of this lab.
# Output each floating-point value with two digits after the decimal point, which can be achieved as follows:
# print(f'{your_value:.2f}')

# (1) Prompt the user to input a food item name, price, and quantity. Output an itemized receipt. (Submit for 2 points)

# Note: This zyLab outputs a newline after each user-input prompt. For convenience in the examples below,
# the user's input value is shown on the next line, but such values don't actually appear as output when the program runs.

#-----------------------------------------------
# Enter food item name:
# hot dog
# Enter item price:
# 2.00
# Enter item quantity:
# 5

# RECEIPT
# 5 hot dog @ $2.00 = $10.00
# Total cost: $10.00
#-----------------------------------------------

# (2) Extend the program to prompt the user for a second item. Output an itemized receipt. (Submit for 2 points, so 4 points total)

# Enter food item name:
# hot dog
# Enter item price:
# 2.00
# Enter item quantity:
# 5

# RECEIPT
# 5 hot dog @ $2.00 = $10.00
# Total cost: $10.00

# Enter second food item name:
# ice cream
# Enter item price:
# 2.50
# Enter item quantity:
# 4

# RECEIPT
# 5 hot dog @ $2.00 = $10.00
# 4 ice cream @ $2.50 = $10.00
# Total cost: $20.00
#-----------------------------------------------

# (3) Extend again to output a third receipt that adds a mandatory 15% gratuity to the total cost.
# Output the total cost, the cost of gratuity, and the grand total. (Submit for 3 points, so 7 points total)

# Enter food item name:
# hot dog
# Enter item price:
# 2.00
# Enter item quantity:
# 5

# RECEIPT
# 5 hot dog @ $2.00 = $10.00
# Total cost: $10.00


# Enter second food item name:
# ice cream
# Enter item price:
# 2.50
# Enter item quantity:
# 4

# RECEIPT
# 5 hot dog @ $2.00 = $10.00
# 4 ice cream @ $2.50 = $10.00
# Total cost: $20.00

# 15% gratuity: $3.00
# Total with tip: $23.00
#-----------------------------------------------

# 1.prompt the user for a first item details
itemName = input("Enter food item name:\n")
itemPrice = float(input("Enter item price:\n"))
quantity = int(input("Enter item quantity:\n"))
# calculate first total price
totalPrice = itemPrice * quantity

# output the first item receipt
print("\nRECEIPT")
print('{} {} @ ${:.2f} = ${:.2f}'.format(quantity,itemName, itemPrice, totalPrice))
print('Total cost: ${:.2f}\n'.format(totalPrice))

# 2.prompt the user for a second item details
secondItemName = input('\nEnter second food item name:\n')
secondItemPrice = float(input('Enter item price:\n'))
secondQuantity=int(input('Enter item quantity:\n'))
# calculate second total price
secondTotalPrice = secondItemPrice * secondQuantity

# output the second item receipt
print('\nRECEIPT')
print('{} {} @ ${:.2f} = ${:.2f}'.format(quantity, itemName, itemPrice, totalPrice))
print('{} {} @ ${:.2f} = ${:.2f}'.format(secondQuantity,secondItemName, secondItemPrice, secondTotalPrice))
# calculate total cost
totalCost = totalPrice + secondTotalPrice
print('Total cost: ${:.2f}\n'.format(totalCost))

# calculate tip amount
tipAmount = 15/100 * totalCost

# output the tip amount and total amount with tip
print('15% gratuity: ${:.2f}'.format(tipAmount))
print('Total with tip: ${:.2f}'.format(totalCost + tipAmount))