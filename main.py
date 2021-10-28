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


symbolsList = ['(', ')', '[', ']', '{', '}', ',', ';', '=', '.', '+', '-', '*', '/', '&', '|', '~', '<', '>']
keywords = ['class', 'constructor', 'method', 'function', 'int', 'boolean', 'char', 'void', 'var', 'static',
            'field', 'let', 'do', 'if', 'else', 'while', 'return', 'true', 'false', 'null', 'this']

charCheck = 1

eof = False
position = 0
lexemeBuffer = ""

# Determining and tokenizing lexemes.

# NOTE: Need to find way to append to currentLexeme (done) AND use just the most recent character. Step through code.

f = open("Main.jack")
# f = open("SquareGame.jack")
jackText = f.read()
jackText += " "  # FOR DEBUGGING.

print("<tokens>")

# len == 578 (I cut out text).
while position < len(jackText) - 1:  # While you haven't reached the end of the file.

    position += 1  # Load the next character into the lexemeBuffer.
    lexemeBuffer += jackText[position]  # Append to the currentLexeme so the currentLexeme can be checked.

    if lexemeBuffer == "\n":
        lexemeBuffer = ""




    elif lexemeBuffer[0] == "/":  # Can be a single line comment, multi-line comment, OR division operator.

        lexemeBuffer += jackText[position]

        # Check if single line comment.
        if lexemeBuffer[0:1] == "/":

            while jackText[position + 1] != "\n":
                lexemeBuffer += jackText[position]
                position += 1
            lexemeBuffer = ""

        # Check if multi-line comment.
        elif lexemeBuffer[0:1] == "*":

            while not lexemeBuffer.endswith("*/"):
                lexemeBuffer += jackText[position + 1]
                position += 1
            lexemeBuffer = ""

        # MUST be division symbol
        elif lexemeBuffer[0:1] == " ":
            lexemeBuffer += jackText[position + 1]

            print("<symbol> " + lexemeBuffer + " </symbol>")
            position += 1
        lexemeBuffer = ""

        # The more important lexemes to tokenize.





    elif lexemeBuffer.isalpha() or lexemeBuffer == "_":

        while jackText[position + 1] not in symbolsList and jackText[position + 1] != " ":
            position += 1
            lexemeBuffer += jackText[position]

        if lexemeBuffer in keywords:
            print("<keyword> " + lexemeBuffer + " </keyword>")
            lexemeBuffer = ""
        else:
            print("<identifier> " + lexemeBuffer + " </identifier>")
            lexemeBuffer = ""



    elif lexemeBuffer == "\"":

        position += 1       # Because we can't count the first quotation mark itself.

        while jackText[position + 1] != "\"":
            lexemeBuffer += jackText[position]
            position += 1

        position += 1
        lexemeBuffer += jackText[position]
        print("<stringConstant> " + lexemeBuffer[1:-1] + " </stringConstant>")

        lexemeBuffer = ""



    elif lexemeBuffer.isdigit():

        while jackText[position + 1].isdigit():
            lexemeBuffer += jackText[position]
            position += 1

        print("<integerConstant> " + lexemeBuffer + " </integerConstant>")

        lexemeBuffer = ""


    elif lexemeBuffer in symbolsList:
        print("<symbol> " + lexemeBuffer + " </symbol>")

        if jackText[position + 1] not in symbolsList:
            lexemeBuffer = ""
            continue
        else:
            position += 1
            lexemeBuffer = jackText[position]
            print("<symbol> " + lexemeBuffer + " </symbol>")
            lexemeBuffer = ""



    elif lexemeBuffer == " ":
        lexemeBuffer = ""

    elif lexemeBuffer == "\t":
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
