#Anthony Nguyen
#PSID1938087

# 7.29 LAB: Warm up: Text analyzer & modifier
# (1) Prompt the user to enter a string of their choosing. Output the string. (1 pt)
#
# Ex:
#
# Enter a sentence or phrase:
# The only thing we have to fear is fear itself.
#
# You entered: The only thing we have to fear is fear itself.
# (2) Complete the get_num_of_characters() function, which returns the number of characters in the user's string.
# We encourage you to use a for loop in this function. (2 pts)
#
# (3) Extend the program by calling the get_num_of_characters() function and then output the returned result. (1 pt)
#
# (4) Extend the program further by implementing the output_without_whitespace() function. output_without_whitespace()
# outputs the string's characters except for whitespace (spaces, tabs). Note: A tab is '\t'. Call the output_without_
# whitespace() function in main(). (2 pts)
#
# Ex:
#
# Enter a sentence or phrase:
# The only thing we have to fear is fear itself.
#
# You entered: The only thing we have to fear is fear itself.
#
# Number of characters: 46
# String with no whitespace: Theonlythingwehavetofearisfearitself.

def get_num_of_characters(input_str):
    count = 0
    for i in range(len(input_str)):
        count += 1
    return count


def output_without_whitespace(input_str):
    print('String with no whitespace: ', end='')
    for ch in input_str:
        if ch != ' ' and ch != '\t':
            print(ch, end='')
    print()


if __name__ == '__main__':
    input_str = input('Enter a sentence or phrase:\n')
    print('\nYou entered: ' + input_str)
    print('\nNumber of characters: ' + str(get_num_of_characters(input_str)))
    output_without_whitespace(input_str)