# Cameron Holbrook
# Tokenizer

"""

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
# https://www.quora.com/How-do-you-check-for-end-of-file-in-Python


# stringConstants need to be interpreted as-is.
# integerConstants need to be interpreted as-is.
# Boolean... need to choose.
# identifiers need to be differentiated with integerConstants; difference is _.

listOfTokens = []           # Insert tokens when lexeme is identified. Then, create new file, and output it all. Don't forget newlines.
                            # Note to future self: May try to append them all, then append the last </token> tag.

whiteList = ['//', '/*', '*/', '/**', ' ', '\n']
symbolsList = ['(', ')', '[', ']', '{', '}', ',', ';', '=', '.', '+', '-', '*', '/', '&', '|', '~', '<', '>']
reservedList = ['class', 'constructor', 'method', 'function', 'int', 'boolean', 'char', 'void', 'var', 'static',
                 'field', 'let', 'do', 'if', 'else', 'while', 'return', 'true', 'false', 'null', 'this']
lookAhead = ["/", "*"]

position = 0
lexemeBuffer = ""
eof = False
charCheck = 1

# Determining and tokenizing lexemes.

# NOTE: Need to find way to append to currentLexeme (done) AND use just the most recent character. Step through code.

f = open("Main.jack")
jackText = f.read()

while eof is False:          # While you haven't reached the end of the file.

    # Now, I can utilize jackText, since it has all of the characters in it.
    # Be sure to have line of code that makes eof valid. Probably eof = None.

    lexemeBuffer = lexemeBuffer + jackText[position + 1]   # Append to the currentLexeme so the currentLexeme can be checked.

    # Check if lexeme (5 tokens total)

    if jackText[position] == "/":                   # Could be a symbol or comment. Likely symbol.

        if jackText[position + 1] == "/":                 # TOKEN: MUST be a single line comment. Read characters until end of LINE; clear lexemeBuffer.
            print("single line comment")

            while jackText[position + 1] != "\n":       # Go to the end of the line, ignoring every character.
                print("single line comment " + str(position))
                position += 1

            # position += 1       # One extra increment to get to the next line.
            lexemeBuffer = ""

    if lexemeBuffer == "\"":                         # TOKEN: MUST be an integerString.
        print("<stringConstant>")
        position += 1

    else:                                               # No lexeme found; go to next iteration.
        position += 1

    # eof = True


print("Exiting now...")
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