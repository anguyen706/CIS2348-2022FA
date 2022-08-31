#Anthony Nguyen
#PSID1938087

#2.12 Divide by X

# Write a program using integers user_num and x as input, and output user_num divided by x three times.
#Ex: If the input is:
# 2000
# 2

# Then the output is:
# 1000 500 250
# Note: In Python 3, integer division discards fractions. Ex: 6 // 4 is 1 (the 0.5 is discarded).

user_num = int(input())
x = int(input())
user_num = user_num//x
print(user_num,end=' ')
user_num = user_num//x
print(user_num,end=' ')
user_num = user_num//x
print(user_num)