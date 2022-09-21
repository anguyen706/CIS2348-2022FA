#Anthony Nguyen
#PSID1938087

# 6.15 LAB: Count input length without spaces, periods, exclamation points, or commas
# Given a line of text as input, output the number of characters excluding spaces, periods,
# exclamation points, or commas.
#
# Ex: If the input is:
#
# Listen, Mr. Jones, calm down.
# the output is:
#
# 21
# Note: Account for all characters that aren't spaces, periods,
# exclamation points, or commas (Ex: "r", "2", "?").

user_text = input()

count = 0
for x in user_text:
    if not (x in " .,!"): # if x != '', ., or ,
        count += 1
print(count)