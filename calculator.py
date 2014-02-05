 # No setup
    # repeat forever:
    #     read input
    #     tokenize input
    #     if the first token is 'q', quit
    #     otherwise decide which math function to call based on the tokens we read
import arithmetic

while True:
    raw_data = raw_input("> ")
    tokens = raw_data.split(" ")
    num1 = int(tokens[1])

    if tokens[0] == "q":
        quit()
    elif tokens[0] == "+":
        num2 = int(tokens[2])
        print arithmetic.add(num1, num2)
    elif tokens[0] == "-":
        num2 = int(tokens[2])
        print arithmetic.subtract(num1, num2)
    elif tokens[0] == "*":
        num2 = int(tokens[2])
        print arithmetic.multiply(num1, num2)
    elif tokens[0] == "/":
        num2 = int(tokens[2])
        print arithmetic.divide(num1, num2)
    elif tokens[0] == "square":
        print arithmetic.square(num1)
    elif tokens[0] == "cube":
        print arithmetic.cube(num1)
    elif tokens[0] == "pow":
        num2 = int(tokens[2])
        print arithmetic.power(num1, num2)
    elif tokens[0] == "mod":
        num2 = int(tokens[2])
        print arithmetic.mod(num1, num2)
    else:
        print "I don't understand."
