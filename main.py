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

# Character read and write code learned and adapted from these sites:
# https://www.geeksforgeeks.org/python-program-to-read-character-by-character-from-a-file/
# https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
# https://www.quora.com/How-do-you-check-for-end-of-file-in-Python
# https://www.guru99.com/reading-and-writing-files-in-python.html#6

symbolsList = ['(', ')', '[', ']', '{', '}', ',', ';', '=', '.', '+', '-', '*', '/', '&', '|', '~', '<', '>']
keywords = ['class', 'constructor', 'method', 'function', 'int', 'boolean', 'char', 'void', 'var', 'static',
            'field', 'let', 'do', 'if', 'else', 'while', 'return', 'true', 'false', 'null', 'this']

position = - 1
lexemeBuffer = ""

f = open("Main.jack")
# f = open("SquareGame.jack")
jackText = f.read()

file = open("MainT.xml", "w+")


# print("<tokens>")
file.write("<tokens>\n")

while position < len(jackText) - 2:  # While you haven't reached the end of the file.

    position += 1  # Load the next character into the lexemeBuffer.
    lexemeBuffer += jackText[position]  # Append to the currentLexeme so the currentLexeme can be checked.

    if lexemeBuffer == "\n":
        lexemeBuffer = ""




    elif lexemeBuffer == "/":  # Can be a single line comment, multi-line comment, OR division operator.

        # lexemeBuffer += jackText[position]

        # Check if single line comment.
        if jackText[position + 1] == "/":

            while jackText[position + 1] != "\n":
                lexemeBuffer += jackText[position]
                position += 1
            lexemeBuffer = ""

        # Check if multi-line comment.
        elif jackText[position + 1] == "*":

            while not lexemeBuffer.endswith("*/"):
                lexemeBuffer += jackText[position + 1]
                position += 1
            lexemeBuffer = ""

        # MUST be division symbol
        elif jackText[position + 1] == " ":
            # print("<symbol> " + lexemeBuffer + " </symbol>")
            file.write("<symbol> " + lexemeBuffer + " </symbol>\n")
            position += 1

        lexemeBuffer = ""







        # The more important lexemes to tokenize.

    elif lexemeBuffer.isalpha() or lexemeBuffer == "_":

        while jackText[position + 1] not in symbolsList and jackText[position + 1] != " ":
            position += 1
            lexemeBuffer += jackText[position]

        if lexemeBuffer in keywords:
            # print("<keyword> " + lexemeBuffer + " </keyword>")
            file.write("<keyword> " + lexemeBuffer + " </keyword>\n")
            lexemeBuffer = ""
        else:
            # print("<identifier> " + lexemeBuffer + " </identifier>")
            file.write("<identifier> " + lexemeBuffer + " </identifier>\n")
            lexemeBuffer = ""



    elif lexemeBuffer == "\"":

        position += 1       # Because we can't count the first quotation mark itself.

        while jackText[position + 1] != "\"":
            lexemeBuffer += jackText[position]
            position += 1

        position += 1
        lexemeBuffer += jackText[position]
        # print("<stringConstant> " + lexemeBuffer[1:-1] + "  </stringConstant>")
        file.write("<stringConstant> " + lexemeBuffer[1:-1] + "  </stringConstant>\n")
        lexemeBuffer = ""



    elif lexemeBuffer.isdigit():

        while jackText[position + 1].isdigit():
            lexemeBuffer += jackText[position]
            position += 1

        # print("<integerConstant> " + lexemeBuffer + " </integerConstant>")
        file.write("<integerConstant> " + lexemeBuffer + " </integerConstant>\n")

        lexemeBuffer = ""


    elif lexemeBuffer in symbolsList:

        if lexemeBuffer == "<":
            # print("<symbol> &lt; </symbol>")
            file.write("<symbol> &lt; </symbol>\n")


        elif lexemeBuffer == ">":
            # print("<symbol> &gt; </symbol>")
            file.write("<symbol> &gt; </symbol>\n")


        elif lexemeBuffer == "\"":
            # print("<symbol> &quot; </symbol>")
            file.write("<symbol> &quot; </symbol>\n")


        elif lexemeBuffer == "&":
            # print("<symbol> &amp; </symbol>")
            file.write("<symbol> &amp; </symbol>\n")

        else:
            # print("<symbol> " + lexemeBuffer + " </symbol>")
            file.write("<symbol> " + lexemeBuffer + " </symbol>\n")

        lexemeBuffer = ""


    elif lexemeBuffer == " ":
        lexemeBuffer = ""

    elif lexemeBuffer == "\t":
        lexemeBuffer = ""

    # Detect nothing
    else:
        continue

# print("</tokens>")
file.write("</tokens>\n")
exit()

