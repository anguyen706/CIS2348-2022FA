#Anthony Nguyen
#PSID1938087

# 6.17 CIS 2348 LAB: Password modifier
# Many user-created passwords are simple and easy to guess.
# rite a program that takes a simple password and makes it stronger
# by replacing characters using the key below, and by appending "q*s"
# to the end of the input string.
#
# i becomes !
# a becomes @
# m becomes M
# B becomes 8
# o becomes .
# Ex: If the input is:
#
# mypassword
# the output is:
#
# Myp@ssw.rdq*s

password = input()
result = ''

i = 0
while i < len(password):
    ch = password[i]
    if ch == 'i':
        result += '!'
    elif ch == 'a':
        result += '@'
    elif ch == 'm':
        result += 'M'
    elif ch == 'B':
        result += '8'
    elif ch == 'o':
        result += '.'
    else:
        result += ch
    i += 1

result += 'q*s'
print(result)