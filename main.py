# Cameron Holbrook
# Tokenizer

"""

Four tokens:
symbols
reserved words
constants
identifiers


"""
import symtable

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



file = open('Main.jack', 'r')           # Open file in read mode.

currentLexeme = ""

while 1:

    # read character by character.
    char = file.read(1)
    if not char:        # If you reach the end of the file, break out of the loop.
        break

    currentLexeme.append(char)
    print(currentLexeme)

file.close()
