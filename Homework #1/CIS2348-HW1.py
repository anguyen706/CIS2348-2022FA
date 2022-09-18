#Anthony Nguyen
#PSID1938087

# CIS 2348 Homework 1
# Coding Problem 1
# Overview
# Write a short Python program for problems.
# Calculate the age of person based on current date und the birthday of the
# user. The program should:
# * Prompt the user to enter the current date by month, day and year
# * Prompt the user to enter the birthday by month, day and year
# * Output the age of the user in years
# * Output a "Happy Birthday!" message if the current date is the user's
# actual birthday.
# * Have nice looking output as shown in the example below
# Example Output
# Birthday Calculator
# Current day
# Month: 9
# Day: 13
# Year: 2005
# Birthday
# Month: 9
# Day: 21
# Year: 1981
# You are 23 years old.

# ZyLabs coding exercises in ZyBooks
# Complete all the ZyLabs in Homework 1 on ZyBooks. You should write all
# your code in the PyCharm environment and then submit in ZyBooks as well
# as commit to your Github repository.
# The solution to each ZyLabs problem should be in its own .py file.

# For your reference, the ZyLabs for this homework assignment are:
# 1.12, 1.20, 2.19, 3.19, 5.22

# At the top of each Python file, you must include a comment block that
# includes both your name and PSID.

# What to Turn In
# Create a folder in your repository for yourself on Github.
# Add and commit your all .py files to your private repository in the
# Github. Do NOT commit any of the other files, and do not zip the files together.
# Submit the link to your Github repository containing your homework via Blackboard.

print('Birthday Calculator\nCurrent day')
cm1 = int(input('Month: '))
cd1 = int(input('Day: '))
cy1 = int(input('Year: '))
print('Birthday')
dob_m2 = int(input('Month: '))
dob_d2 = int(input('Day: '))
dob_y2 = int(input('Year: '))
years = cy1-dob_y2-1
if(dob_m2<cm1):
    years+=1
elif(cm1==dob_m2):
    if(dob_d2<cd1):
        years+=1
if(cm1==dob_m2 and cd1==dob_d2):#printing hbd if current day is birthday
    print('Happy Birthday!')
print('You are '+str(years)+" years old.")