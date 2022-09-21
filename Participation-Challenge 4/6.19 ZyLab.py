#Anthony Nguyen
#PSID1938087

# 6.19 LAB: Print string in reverse
# Write a program that takes in a line of text as input,
# and outputs that line of text in reverse. The program repeats, ending when the user enters "Done", "done", or "d" for the line of text.
#
# Ex: If the input is:
#
# Hello there
# Hey
# done
# then the output is:
#
# ereht olleH
# yeH

string_input = input()

while (string_input != "Done" and string_input != "done" and string_input != "d"):

    for i in range(len(string_input) - 1, -1, -1):  # reverse looping
        print(string_input[i], end='')

    print()
    string_input = input()