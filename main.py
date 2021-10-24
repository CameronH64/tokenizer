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

# Character read code learned and adapted from these sites:
# https://www.geeksforgeeks.org/python-program-to-read-character-by-character-from-a-file/
# https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files


# Some setup
whiteList = ['//', '/*', '*/', '/**', ' ', '\n']
symbolsList = ['(', ')', '[', ']', '{', '}', ',', ';', '=', '.', '+', '-', '*', '/', '&', '|', '~', '<', '>']
reservedList = ['class', 'constructor', 'method', 'function', 'int', 'boolean', 'char', 'void', 'var', 'static',
                 'field', 'let', 'do', 'if', 'else', 'while', 'return', 'true', 'false', 'null', 'this']
# stringConstants need to be interpreted as-is.
# integerConstants need to be interpreted as-is.
# Boolean... need to choose.
# identifiers need to be differentiated with integerConstants; difference is _.

listOfTokens = []           # Insert tokens when lexeme is identified. Then, create new file, and output it all. Don't forget newlines.
                            # Note to future self: May try to append them all, then append the last </token> tag.

filePosition = 1
endOfFile = False

whiteOrSymbol = False

# Determining and tokenizing lexemes.

# NOTE: Need to find way to append to currentLexeme (done) AND use just the most recent character. Step through code.

while not endOfFile:
    with open('Main.jack', 'r') as file:            # Open file in read mode.
        read_data = file.read(filePosition)         # Read a single character in the file.
        currentLexeme = str(read_data)              # The reason the file can be opened so many times is because
                                                    # the file position is always being properly updated.
    # Check if lexeme (7 tokens total)

    if currentLexeme in symbolsList:                   # Could be a symbol or comment. Need to check here.

        if currentLexeme in whiteList:                 # TOKEN: Check if it's a comment or white space.
            print("Comment.")
            print(str(read_data))
            filePosition += 1
            continue

        elif currentLexeme in symbolsList:             # TOKEN: MUST be a symbol, since wasn't in whiteList list.
            print("Confirmed to be a symbol.")
            print(str(read_data))

            # Do whatever, since it's confirmed a symbol.
            filePosition += 1
            continue

    elif currentLexeme == "\"":                        # TOKEN: MUST be an integerString.
        print("Probably a stringConstant.")
        print(str(read_data))
        filePosition += 1
        continue

    else:                                               # No lexeme found; go to next iteration.
        filePosition += 1
        continue


    # break                                           # Break out of while loop.

exit()




# List of tokens:

# White space and tokens (not outputted, so doesn't count.
# <keyword>
# <identifier>
# <symbol>
# <stringConstant>
# <integerConstant>

# (Not in .xml example output)
# <booleanConstant>
# <null>        ?
#