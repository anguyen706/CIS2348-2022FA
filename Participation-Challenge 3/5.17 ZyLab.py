#Anthony Nguyen
#PSID1938087

# 5.17 LAB: Seasons
# Write a program that takes a date as input and outputs the date's season in the northern hemisphere. The input is a string to represent the month and an int to represent the day.
#
# Ex: If the input is:
#
# April
# 11
# the output is:
#
# Spring
# In addition, check if the string and int are valid (an actual month and day).
#
# Ex: If the input is:
#
# Blue
# 65
# the output is:
#
# Invalid
# The dates for each season in the northern hemisphere are:
# Spring: March 20 - June 20
# Summer: June 21 - September 21
# Autumn: September 22 - December 20
# Winter: December 21 - March 19

if __name__ == '__main__':
    inputMonth = input()
    inputDay = int(input())

    if inputMonth == "January" and 1 <= inputDay <= 31:
        print("Winter")
    elif inputMonth == "February" and 1 <= inputDay <= 29:
        print("Winter")
    elif inputMonth == "April" and 1 <= inputDay <= 30:
        print("Spring")
    elif inputMonth == "May" and 1 <= inputDay <= 30:
        print("Spring")
    elif inputMonth == "July" and 1 <= inputDay <= 31:
        print("Summer")
    elif inputMonth == "August" and 1 <= inputDay <= 31:
        print("Summer")
    elif inputMonth == "October" and 1 <= inputDay <= 31:
        print("Autumn")
    elif inputMonth == "November" and 1 <= inputDay <= 30:
        print("Autumn")
    elif inputMonth == "March" and 20 <= inputDay <= 31:
        print("Spring")
    elif inputMonth == "June" and 1 <= inputDay <= 20:
        print("Spring")
    elif inputMonth == "June" and 21 <= inputDay <= 30:
        print("Summer")
    elif inputMonth == "September" and 1 <= inputDay <= 21:
        print("Summer")
    elif inputMonth == "September" and 22 <= inputDay <= 30:
        print("Autumn")
    elif inputMonth == "December" and 0 <= inputDay <= 20:
        print("Autumn")
    elif inputMonth == "December" and 21 <= inputDay <= 30:
        print("Winter")
    elif inputMonth == "March" and 1 <= inputDay <= 19:
        print("Winter")
    else:
        print("Invalid")


