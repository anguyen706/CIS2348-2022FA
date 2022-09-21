#Anthony Nguyen
#PSID1938087

# 6.16 LAB: Password modifier
# Many user-created passwords are simple and easy to guess.
# Write a program that takes a simple password and makes it stronger
# by replacing characters using the key below, and by appending "!" to
# the end of the input string.
#
# i becomes 1
# a becomes @
# m becomes M
# B becomes 8
# s becomes $
# Ex: If the input is:
#
# mypassword
# the output is:
#
# Myp@$$word!
# Hint: Python strings are immutable, but support string concatenation.
# Store and build the stronger password in the given password variable.

password = input()
result = ''

i = 0
while i < len(password):
    ch = password[i]
    if ch == 'i':
        result += '1'
    elif ch == 'a':
        result += '@'
    elif ch == 'm':
        result += 'M'
    elif ch == 'B':
        result += '8'
    elif ch == 'o':
        result += '$'
    else:
        result += ch
    i += 1

result += '!'
print(result)