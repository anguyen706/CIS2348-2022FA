#Anthony Nguyen
#PSID1938087

# 5.21 LAB*: Program: Automobile service invoice
# (1) Output a menu of automotive services and the corresponding cost of each service. (2 pts)
#
# Ex:
#
# Davy's auto shop services
# Oil change -- $35
# Tire rotation -- $19
# Car wash -- $7
# Car wax -- $12
#
#
#
# (2) Prompt the user for two services from the menu. (2 pts)
#
# Ex:
#
# Select first service:
# Oil change
# Select second service:
# Car wax
#
#
#
# (3) Output an invoice for the services selected. Output the cost for each service and the total cost. (3 pts)
#
#
# Davy's auto shop invoice
#
# Service 1: Oil change, $35
# Service 2: Car wax, $12
#
# Total: $47
#
#
#
# (4) Extend the program to allow the user to enter a dash (-), which indicates no service. (3 pts)
#
# Ex:
#
# Davy's auto shop services
# Oil change -- $35
# Tire rotation -- $19
# Car wash -- $7
# Car wax -- $12
#
# Select first service:
# Tire rotation
# Select second service:
# -
#
# Davy's auto shop invoice
#
# Service 1: Tire rotation, $19
# Service 2: No service
#
# Total: $19

services = {
    'Oil change': 35,
    'Tire rotation': 19,
    'Car wash': 7,
    'Car wax': 12
}

# print menu
print("Davy's auto shop services")
for service, cost in services.items():
    # print the service with its cost
    print(f'{service} -- ${cost}')

first_service = input('\nSelect first service:\n')
second_service = input('Select second service:\n')

print("\nDavy's auto shop invoice\n")

# get cost of first service
try:
    first_service_cost = services[first_service]
    print(f'Service 1: {first_service}, ${first_service_cost}')
except:
    print('Service 1: No service')
    first_service_cost = 0

# get the cost of second service
try:
    second_service_cost = services[second_service]
    print(f'Service 2: {second_service}, ${second_service_cost}')
except:
    print('Service 2: No service')
    second_service_cost = 0

# print total cost
total_cost = first_service_cost + second_service_cost
# print total cost
print(f'\nTotal: ${total_cost}')