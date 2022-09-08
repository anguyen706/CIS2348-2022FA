#Anthony Nguyen
#PSID1938087

# 3.17 Creating passwords

# (1) Prompt the user to enter two words and a number, storing each into separate variables.
# Then, output those three values on a single line separated by a space. (Submit for 1 point)

# Ex: If the input is:
# yellow
# Daisy
# 6

# the output after the prompts is:
# You entered: yellow Daisy 6
# Note: User input is not part of the program output.

# (2) Output two passwords using a combination of the user input. Format the passwords as shown below. (Submit for 2 points, so 3 points total).

# Ex: If the input is:
# yellow
# Daisy
# 6

# the output after the prompts is:
# You entered: yellow Daisy 6
# First password: yellow_Daisy
# Second password: 6yellow6

# (3) Output the length of each password (the number of characters in the strings).
# (Submit for 2 points, so 5 points total).

# Ex: If the input is:
# yellow
# Daisy
# 6

# the output after the prompts is:
# You entered: yellow Daisy 6
# First password: yellow_Daisy
# Second password: 6yellow6

# Number of characters in yellow_Daisy: 12
# Number of characters in 6yellow6: 8

# FIXME (1): Finish reading another word and an integer into variables.
# Output all the values on a single line
favorite_color = input('Enter favorite color:\n')
favorite_flower = input("Enter favorite flower:\n")
number = input("Enter a number:\n")
print('You entered:', favorite_color, favorite_flower, number)

# FIXME (2): Output two password options
password1 = favorite_color + "_" + favorite_flower
password2 = number + favorite_color + number
print("\nFirst password: " + password1)
print("Second password: " + password2)


# FIXME (3): Output the length of the two password options
print("\nNumber of characters in " + password1 + ": " + str(len(password1)))
print("Number of characters in " + password2 + ": " + str(len(password2)))