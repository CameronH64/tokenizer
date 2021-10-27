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
keywords = ['class', 'constructor', 'method', 'function', 'int', 'boolean', 'char', 'void', 'var', 'static',
                 'field', 'let', 'do', 'if', 'else', 'while', 'return', 'true', 'false', 'null', 'this']
lookAhead = ["/", "*"]
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

charCheck = 1

eof = False
position = 0
lexemeBuffer = ""


# Determining and tokenizing lexemes.

# NOTE: Need to find way to append to currentLexeme (done) AND use just the most recent character. Step through code.

f = open("Main.jack")
jackText = f.read()
                # len == 578 (I cut out text).
while position < len(jackText):          # While you haven't reached the end of the file.

    position += 1                           # Load the next character into the lexemeBuffer.
    lexemeBuffer += jackText[position]      # Append to the currentLexeme so the currentLexeme can be checked.

    # Check if a comment.
    if lexemeBuffer[0] == "/":                              # Can be a single line comment, multi-line comment, or division operator.

        # Check if single line.
        if lexemeBuffer.endswith("/") and jackText[position + 1] != "*":                 # TOKEN: MUST be a single line comment. Read characters until end of LINE; clear lexemeBuffer.
            print("single line comment")

            while not lexemeBuffer.endswith("\n"):
                lexemeBuffer += jackText[position]
                position += 1
            lexemeBuffer = ""
            continue

    # Check if multi-line.
    elif jackText[position + 1] == "*":              # TOKEN: MUST be a multi-line line comment. Read characters until end of LINE; clear lexemeBuffer.
        print("multi-line comment")

        while not lexemeBuffer.endswith("*/"):
            lexemeBuffer += jackText[position]
            position += 1
        lexemeBuffer = ""
        continue

    # Detect keyword
    elif lexemeBuffer in keywords:                         # TOKEN: MUST be an integerString.
        print("<keyword>")
        position += 1
        lexemeBuffer = ""
        continue

    # Detect stringConstant
    elif lexemeBuffer[0] == "\"":                                               # No lexeme found; go to next iteration.

        # A string constant has been detected!

        print("<integerConstant>")

        while not lexemeBuffer.endswith("\""):
            lexemeBuffer += jackText[position]
            position += 1
        lexemeBuffer = ""
        continue

    # Detect integerConstant
    elif lexemeBuffer in digits:
        print("<integerConstant>")

        while lexemeBuffer[-1] not in digits:
            lexemeBuffer += jackText[position]
            position += 1
        lexemeBuffer = ""

    # Detect identifier
    elif lexemeBuffer[0] == letter or number or _:

        while lexemeBuffer[-1] not in digits:
            lexemeBuffer += jackText[position]
            position += 1
        lexemeBuffer = ""



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