def Calculator():
    num1 = float(input("Enter Number First : "))
    operator = input("Enter Operator [+, - , * , / ] : ")
    num2 = float(input("Enter Number Second : "))

    if operator == "+":
        print("Addition of ", num1, "+", num2, " = ", num1 + num2)
    elif operator == "-":
        print("Subtraction of ", num1, "-", num2, " = ", num1 - num2)
    elif operator == "*":
        print("Multiplication of ", num1, "*", num2, " = ", num1 * num2)
    elif operator == "/" and num2 != 0:
        print("Division of ", num1, "/", num2, " = ", num1 / num2)
    else:
        print("Invalid Input")


Calculator()
