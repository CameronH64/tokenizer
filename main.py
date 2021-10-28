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
# f = open("SquareGame.jack")
jackText = f.read()
jackText += " "         # FOR DEBUGGING.

print("<tokens>")

                # len == 578 (I cut out text).
while position < len(jackText) - 1:          # While you haven't reached the end of the file.

    position += 1                           # Load the next character into the lexemeBuffer.
    lexemeBuffer += jackText[position]      # Append to the currentLexeme so the currentLexeme can be checked.

    if lexemeBuffer == "\n":
        lexemeBuffer = ""

    elif lexemeBuffer[0] == "/":                              # Can be a single line comment, multi-line comment, OR division operator.

        # Check if single line.
        if lexemeBuffer.endswith("/") and jackText[position + 1] != "*":                 # TOKEN: MUST be a single line comment. Read characters until end of LINE; clear lexemeBuffer.
            print("___(ignore) single line comment")

            while not lexemeBuffer.endswith("\n"):
                lexemeBuffer += jackText[position]
                position += 1
            lexemeBuffer = ""
            continue

        # Check if multi-line.
        elif jackText[position + 1] == "*":              # TOKEN: MUST be a multi-line line comment. Read characters until end of LINE; clear lexemeBuffer.
            print("___(ignore) multi-line comment")

            while not lexemeBuffer.endswith("*/"):
                lexemeBuffer += jackText[position + 1]
                position += 1
            lexemeBuffer = ""
            continue

        # MUST be division symbol
        else:
            print("<symbol> " + str(jackText[position]) + " </symbol>")
            position += 1
        lexemeBuffer = ""


                                                                                # The more important lexemes to tokenize.

    elif lexemeBuffer in keywords:
        print("<keyword> " + lexemeBuffer + " </keyword>")
        position += 1
        lexemeBuffer = ""
        continue

    elif lexemeBuffer.isalpha():
        print("<identifier> " + lexemeBuffer + " </identifier>")

        if jackText[position + 1].endswith(" "):
            lexemeBuffer += jackText[position]
            position += 1
        lexemeBuffer = ""
        continue

    elif lexemeBuffer == "\"":
        # A string constant has been detected!

        print("<stringConstant> " + lexemeBuffer + " </stringConstant>")

        if lexemeBuffer.endswith("\""):
            lexemeBuffer += jackText[position]
            position += 1
        lexemeBuffer = ""
        continue

    elif lexemeBuffer in digits:
        print("<integerConstant> " + lexemeBuffer + " </integerConstant>")

        while lexemeBuffer[-1] not in digits:
            lexemeBuffer += jackText[position]
            position += 1
        lexemeBuffer = ""

    # Detect nothing
    else:
        continue



print("</tokens>")

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