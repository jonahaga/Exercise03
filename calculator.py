 # No setup
    # repeat forever:
    #     read input
    #     tokenize input
    #     if the first token is 'q', quit
    #     otherwise decide which math function to call based on the tokens we read
import arithmetic

# while True:
#     raw_data = raw_input("> ")
#     tokens = raw_data.split(" ")
#     num1 = int(tokens[1])

#     if tokens[0] == "q":
#         quit()
#     elif tokens[0] == "+":
#         num2 = int(tokens[2])
#         print arithmetic.add(num1, num2)
#     elif tokens[0] == "-":
#         num2 = int(tokens[2])
#         print arithmetic.subtract(num1, num2)
#     elif tokens[0] == "*":
#         num2 = int(tokens[2])
#         print arithmetic.multiply(num1, num2)
#     elif tokens[0] == "/":
#         num2 = int(tokens[2])
#         print arithmetic.divide(num1, num2)
#     elif tokens[0] == "square":
#         print arithmetic.square(num1)
#     elif tokens[0] == "cube":
#         print arithmetic.cube(num1)
#     elif tokens[0] == "pow":
#         num2 = int(tokens[2])
#         print arithmetic.power(num1, num2)
#     elif tokens[0] == "mod":
#         num2 = int(tokens[2])
#         print arithmetic.mod(num1, num2)
#     else:
#         print "I don't understand."


while True:
    raw_data = raw_input("> ")
    tokens = raw_data.split(" ")
    valid_digits = ["0","1","2","3","4","5","6","7","8","9"]

    if tokens[0] == "q":
        quit()
    
    elif len(tokens) > 3:
        print "Please only input 1 or 2 integers."
    
    elif len(tokens) > 2:
        if tokens[1] in valid_digits and tokens[2] in valid_digits:
            num1 = float(tokens[1])
            num2 = float(tokens[2])
            if tokens[0] == "+":
                print arithmetic.add(num1, num2)
            elif tokens[0] == "-":
                print arithmetic.subtract(num1, num2)
            elif tokens[0] == "*":
                print arithmetic.multiply(num1, num2)
            elif tokens[0] == "/":
                print arithmetic.divide(num1, num2)
            elif tokens[0] == "pow":
                print arithmetic.power(num1, num2)
            elif tokens[0] == "mod":
                print arithmetic.mod(num1, num2)
            elif tokens[0] == "square":
                print "Please only square one number at a time."
            elif tokens[0] == "cube":
                print "Please only cube one number at a time."
            else:
                print "Please use a valid operator."
        else:
            print "Please use a valid operator followed by integers."

    elif len(tokens) == 2:
        if tokens[1] in valid_digits:
            num1 = float(tokens[1])
            if tokens[0] == "square":
                print arithmetic.square(num1)
            elif tokens[0] == "cube":
                print arithmetic.cube(num1)
            elif tokens[0] == "*":
                print "Please multiply 2 integers."
            elif tokens[0] == "/":
                print "Please divide 2 integers."
            elif tokens[0] == "+":
                print "Please add 2 integers."
            elif tokens[0] == "-":
                print "Please subtract 2 integers."
            elif tokens[0] == "mod":
                print "Please find the remainder of 2 integers."
            elif tokens[0] == "pow":
                print "Don't forget the exponent."
            else:
                print "Please use a valid operator."
        else:
            print "Please use a valid operator followed by integers."

    else:
        print "I don't understand."
