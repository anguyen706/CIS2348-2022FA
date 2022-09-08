#Anthony Nguyen
#PSID1938087

# 3.13 Phone Number Breakdown

# Given an integer representing a 10-digit phone number, output the area code, prefix,
# and line number using the format (800) 555-1212.

# Ex: If the input is:

# 8005551212
# the output is:

# (800) 555-1212
# Hint: Use % to get the desired rightmost digits.
# Ex: The rightmost 2 digits of 572 is gotten by 572 % 100, which is 72.

#  Hint: Use // to shift right by the desired amount.
#  Ex: Shifting 572 right by 2 digits is done by 572 // 100, which yields 5.
#  (Recall integer division discards the fraction).

# For simplicity, assume any part starts with a non-zero digit. So 0119998888 is not allowed.

phone_number = int(input())

if __name__ == '__main__':
    area_code = phone_number // 10000000
    prefix = (phone_number % 10000000) // 10000
    line_number = phone_number % 10000
    print("({}) {}-{}".format(area_code,prefix,line_number))