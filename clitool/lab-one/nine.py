def calculator():
    operation = input("Please choose an operation (+, -, *, /): ")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if operation == '+':
        print(num1 + num2)
    elif operation == '-':
        print(num1 - num2)
    elif operation == '*':
        print(num1 * num2)
    elif operation == '/':
        if num2 == 0:
            print("Error: Division by zero is not allowed")
        else:
            print(num1 / num2)
    else:
        print("Invalid operator")

calculator()