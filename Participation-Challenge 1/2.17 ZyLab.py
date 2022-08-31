#Anthony Nguyen
#PSID1938087

# 2.17 Warm up: Variables, input, and type conversion

# (1) Prompt the user to input an integer between 32 and 126, a float, a character, and a string, storing each into separate variables.
# Then, output those four values on a single line separated by a space. (Submit for 2 points).

# Note: This zyLab outputs a newline after each user-input prompt.
# For convenience in the examples below, the user's input value is shown on the next line,
# but such values don't actually appear as output when the program runs.

# Enter integer (32 - 126):
# 99
# Enter float:
# 3.77
# Enter character:
# z
# Enter string:
# Howdy
# 99 3.77 z Howdy

# (2) Extend to also output in reverse. (Submit for 1 point, so 3 points total).

# Enter integer (32 - 126):
# 99
# Enter float:
# 3.77
# Enter character:
# z
# Enter string:
# Howdy
# 99 3.77 z Howdy
# Howdy z 3.77 99

# (3) Extend to convert the integer to a character by using the 'chr()' function, and output that character.
# (Submit for 2 points, so 5 points total).

# Enter integer (32 - 126):
# 99
# Enter float:
# 3.77
# Enter character:
# z
# Enter string:
# Howdy
# 99 3.77 z Howdy
# Howdy z 3.77 99
# 99 converted to a character is c

#---------------------------------------------------------------

# FIXME (1): Finish reading other items into variables,
# then output the four values on a single line separated by a space

user_int = int(input('Enter integer (32 - 126):\n'))

user_flt = float(input('Enter float:\n'))

user_char = input('Enter character:\n')

user_str = input('Enter string:\n')

# FIXME (2): Output the four values in reverse
print(user_int, user_flt, user_char, user_str)
print(user_str, user_char, user_flt, user_int)

# FIXME (3): Convert the integer to a character, and output that character
character = chr(user_int)
print(user_int, 'converted to a character is', character)