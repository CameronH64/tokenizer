# Cameron Holbrook
# Tokenizer

"""

Four tokens:
symbols
reserved words
constants
identifiers

PSEUDOCODE:

    Read character by character

    Each time a character is read, see if it's a lexeme.

    If it's a lexeme, identify the token
    Then, output the lexeme (with labels) to .xml.



    Else, continue with reading characters.

    Do this until end of file is reached.

"""


whileSpaceandCommentsDictionary = { 'WSaC': ['//', '/*', '*/', '/**'] }
symbolsDictionary = { 'symbols': ['(', ')', '[', ']', '{', '}', ',', ';', '=', '.', '+', '-', '*', '/', '&', '|', '~', '<', '>'] }
reservedWordsDictionary = { 'reservedWords': ['class', 'constructor', 'method', 'function', 'int', 'boolean', 'char', 'void', 'var', 'static', 'field', 'let', 'do', 'if', 'else', 'while', 'return', 'true', 'false', 'null', 'this'] }
# The constants and identifiers tokens don't need a dictionary; they can be calculated.


# Character read code adapted from GeeksforGeeks:
# https://www.geeksforgeeks.org/python-program-to-read-character-by-character-from-a-file/


def identify_token(lexeme):

    """Once the lexeme is found, its token needs to be identified."""

    # If lexeme equals [token] return [token]
    # else if ...

    # Or use multiple for loops, checking the lexeme in each dictionary.

    # Need to have one for comments, but DON'T write to the .xml file.

def write_token(token):


def read_lexeme():

    currentLexeme = ""          # Start with an empty lexeme.

    while 1:

        # read character by character.
        char = file.read(1)
        if not char:  # If you reach the end of the file, break out of the loop.
            break

        currentLexeme = currentLexeme + char  # Concatenate the just-read char to the end of the file.

        digit = currentLexeme[0].isdigit()

        if digit:
            continue
        else:

        # Do an identify_lexeme here somewhere.

        currentLexeme = ""      # Reset the currentLexeme.

        return lexeme



################## Code Execution Start

file = open('Main.jack', 'r')           # Open file in read mode.

endOfFile = False

while not endOfFile:
    read_lexeme()



file.close()






