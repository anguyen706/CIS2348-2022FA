#Anthony Nguyen
#PSID1938087

# 7.30 LAB*: Program: Authoring assistant
# (1) Prompt the user to enter a string of their choosing. Store the text in a string. Output the string. (1 pt)
#
# Ex:
#
# Enter a sample text:
# we'll continue our quest in space.  there will be more shuttle flights and more shuttle crews and,  yes;
# more volunteers, more civilians,  more teachers in space.  nothing ends here;  our hopes and our journeys continue!
#
# You entered: we'll continue our quest in space.  there will be more shuttle flights and more shuttle crews and,  yes;
# more volunteers, more civilians,  more teachers in space.  nothing ends here;  our hopes and our journeys continue!
#
# (2) Implement the print_menu() function to print the following command menu. (1 pt)
#
# Ex:
#
# MENU
# c - Number of non-whitespace characters
# w - Number of words
# f - Fix capitalization
# r - Replace punctuation
# s - Shorten spaces
# q - Quit
#
# (3) Implement the execute_menu() function that takes 2 parameters: a character representing the user's choice and the
# user provided sample text. execute_menu() performs the menu options, according to the user's choice, by calling the
# appropriate functions described below. (1 pt)
#
#
# (4) In the main program, call print_menu() and prompt for the user's choice of menu options for analyzing/editing the
# string. Each option is represented by a single character.
#
# If an invalid character is entered, continue to prompt for a valid choice. When a valid option is entered, execute
# the option by calling execute_menu(). Then, print the menu and prompt for a new option. Continue until the user
# enters 'q'. Hint: Implement Quit before implementing other options. (1 pt)
#
# Ex:
#
# MENU
# c - Number of non-whitespace characters
# w - Number of words
# f - Fix capitalization
# r - Replace punctuation
# s - Shorten spaces
# q - Quit
#
# Choose an option:
#
# (5) Implement the get_num_of_non_WS_characters() function. get_num_of_non_WS_characters() has a string parameter
# and returns the number of characters in the string, excluding all whitespace. Call get_num_of_non_WS_characters()
# in the execute_menu() function, and then output the returned value. (4 pts)
#
# Ex:
#
# Enter a sample text:
# we'll continue our quest in space.  there will be more shuttle flights and more shuttle crews and,  yes;  more
# volunteers, more civilians,  more teachers in space.  nothing ends here;  our hopes and our journeys continue!
#
# You entered: we'll continue our quest in space.  there will be more shuttle flights and more shuttle crews and,
# yes;  more volunteers, more civilians,  more teachers in space.  nothing ends here;  our hopes and our journeys
# continue!
#
# MENU
# c - Number of non-whitespace characters
# w - Number of words
# f - Fix capitalization
# r - Replace punctuation
# s - Shorten spaces
# q - Quit
#
# Choose an option:
# c
# Number of non-whitespace characters: 181
#
# (6) Implement the get_num_of_words() function. get_num_of_words() has a string parameter and returns the number of
# words in the string. Hint: Words end when a space is reached except for the last word in a sentence. Call
# get_num_of_words() in the execute_menu() function, and then output the returned value. (3 pts)
#
# Ex:
#
# Number of words: 35
#
# (7) Implement the fix_capitalization() function. fix_capitalization() has a string parameter and returns an updated
# string, where lowercase letters at the beginning of sentences are replaced with uppercase letters.
# fix_capitalization() also returns the number of letters that have been capitalized. Call fix_capitalization() in
# the execute_menu() function, and then output the number of letters capitalized followed by the edited string.
# Hint 1: Look up and use Python functions .islower() and .upper() to complete this task. Hint 2: Create an empty
# string and use string concatenation to make edits to the string. (3 pts)
#
# Ex:
#
# Number of letters capitalized: 3
# Edited text: We'll continue our quest in space.  There will be more shuttle flights and more shuttle crews and,
# yes;  more volunteers, more civilians,  more teachers in space.  Nothing ends here;  our hopes and our journeys
# continue!
#
# (8) Implement the replace_punctuation() function. replace_punctuation() has a string parameter and two keyword
# argument parameters exclamation_count and semicolon_count. replace_punctuation() updates the string by replacing
# each exclamation point (!) character with a period (.) and each semicolon (;) character with a comma (,).
# replace_punctuation() also counts the number of times each character is replaced and outputs those counts.
# Lastly, replace_punctuation() returns the updated string. Call replace_punctuation() in the execute_menu()
# function, and then output the edited string. (3 pts)
#
# Ex:
#
# Punctuation replaced
# exclamation_count: 1
# semicolon_count: 2
# Edited text: we'll continue our quest in space.  there will be more shuttle flights and more shuttle crews and,  yes,
# more volunteers, more civilians,  more teachers in space.  nothing ends here,  our hopes and our journeys continue.
#
# (9) Implement the shorten_space() function. shorten_space() has a string parameter and updates the string by
# replacing all sequences of 2 or more spaces with a single space. shorten_space() returns the string.
# Call shorten_space() in the execute_menu() function, and then output the edited string.
# Hint: Look up and use Python function .isspace(). (3 pt)
#
# Ex:
#
# Edited text: we'll continue our quest in space. there will be more shuttle flights and more shuttle crews and, yes;
# more volunteers, more civilians, more teachers in space. nothing ends here; our hopes and our journeys continue!

# print_menu() prints a menu to the user from which the user will choose an option.
def print_menu(text):
    # Displays the menu to the user.
    print("\nMENU")
    print("c - Number of non-whitespace characters")
    print("w - Number of words")
    print("f - Fix capitalization")
    print("r - Replace punctuation")
    print("s - Shorten spaces")
    print("q - Quit")

    # Prompts the user to choose an option from the menu.
    option = input("\nChoose an option:\n")

    # When the option entered by the user is not valid then prints an error message and asks the user to enter a new option.
    while (option not in ['c', 'w', 'f', 'r', 's', 'q']):
        option = input("Invalid choice! Enter a valid option: ")

    # If c is entered calls the get_num_of_non_WS_characters
    if (option == 'c'):
        non_WS = get_num_of_non_WS_characters(text)
        # prints the total number of non-whitespace characters.
        print("\nNumber of non-whitespace characters:", non_WS)

    # If w is entered calls the get_num_of_words
    elif (option == 'w'):
        num_of_words = get_num_of_words(text)
        # prints the total number of words.
        print("\nNumber of words:", num_of_words)

    # If f is entered calls the fix_capitalization
    elif (option == 'f'):
        count, cap_text = fix_capitalization(text)
        # Prints the number of letters capitalized and the edited text.
        print("\nNumber of letters capitalized:", count)
        print("Edited text:", cap_text)

    # If r is entered calls the replace_punctuation
    elif (option == 'r'):
        # exclamation_count and semicolon_count has a default value of 0.
        punc_string = replace_punctuation(text, exclamation_count=0, semicolon_count=0)
        # Prints the edited text
        print("Edited text:", punc_string)

    # If s is entered then calls the shorten_space function.
    elif (option == 's'):
        space_string = shorten_space(text)
        # Prints the edited text
        print("\nEdited text:", space_string)

    # Finally returns the option entered by the user and text entered by the user.
    return option, text


# get_num_of_non_WS_characters gets the total number of non white space characters in the text.
def get_num_of_non_WS_characters(text):
    # text.count(" ") gives the total number of white spaces which when subtracted from the length of the string gives the total number of non white space characters.
    return len(text) - text.count(" ")


# get_num_of_words returns the total number of words in the string.
def get_num_of_words(text):
    # We initialize count to 0.
    count = 0
    # split(" ") splits the string whenever space occurs.
    # split() will return an array of splitted words.
    # Now we traverse through the array
    for char in text.split(" "):
        # If the length of the word is greater than 0 we increment count by 1
        if (len(char) > 0):
            count += 1
            # finally we return the count.
    return count


# fix_capitalization capitalizes all the starting letters of a sentence.
def fix_capitalization(text):
    # We initialize  an empty string named cap_text.
    cap_text = ""
    # We initialize count to 0
    count = 0
    # We declare a variable named start that is assigned a value true.
    # This keeps track if a word is the start word of a sentence or not.
    start = True

    # Now we traverse through the text.
    for string in text:
        # If the word is a starting word and it contains only alphabets then we capitalize the start word.
        if (start and string.isalpha()):
            # We check if the start letter is lower case
            if string.islower():
                # If true then we increment count by 1 and convert the letter to upper case.
                count += 1
                # We concatenate the capitalized word to cap_text.
                cap_text += string.upper()
                # Then we assign false to start.
                start = False
        # Else if the string has ? or . or ! then we assign true to start.
        elif (string in '?.!'):
            start = True
            # We also concatenate the word to cap_text
            cap_text += string
        # else we concatenate the word to cap_text.
        else:
            cap_text += string
    # finally we return the count and cap_text.
    return count, cap_text


# This function will replace the punctuation marks.
def replace_punctuation(text, exclamation_count, semicolon_count):
    # First we create a copy of the text in punc_string
    punc_string = text
    # Then we traverse through the punc_string.
    for char in punc_string:
        # If the character is an exclamation mark then we replace it with . and increment the exclamation_count by 1.
        if (char == "!"):
            punc_string = punc_string.replace(char, ".")
            exclamation_count += 1

        # If the character is a semicolon then we replace it with , and increment the semicolon_count by 1.
        elif (char == ";"):
            punc_string = punc_string.replace(char, ",")
            semicolon_count += 1

    # finally we print the semicolon_count and exclamation_count
    print("\nPunctuation replaced")
    print("exclamation_count:", exclamation_count)
    print("semicolon_count:", semicolon_count)
    # Atlast we return the string with all the punctuation removed
    return punc_string


# shorten space function will remove all the consecutive spaces and replace it with one space.
def shorten_space(text):
    # First we initialize a empty string.
    space_string = ""
    # Now we traverse through the string.
    for char in text:
        # If the character is not space then we concatenate it to the space_string.
        if (char != " "):
            space_string += char
        # else if the charater is a space but the last character of the space_string is not a space then we concatenate it to the space_string.
        elif (char == " " and space_string[len(space_string) - 1] != " "):
            space_string += char
    # finally we return the string with all the consecutive spaces replaced with a single space.
    return space_string


# Prompts the user to enter a string
text = input("Enter a sample text:\n")
# Prints the string entered by the user.
print("\nYou entered:", text)

# Calls the print_menu() function with string as a parameter.
# This will keep calling the print_menu function until user wishes to quit.
while (True):
    # print_menu function will return the option entered by the user and the text entered by the user.
    option, text = print_menu(text)
    # If the user enters q then the program will stop.
    if (option == 'q'):
        break