#basic calculator program

#input the numbers and the arithmetic operator
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operation = input("Enter operation (+,-,/,*,%,**): ")

#Perform the calculation based on the operation
if operation == "+":
    print(num1 + num2)

elif operation == "-":
    print(num1 - num2)

elif operation == "*":
    print(num1 * num2)

elif operation == "%":
    print(num1 % num2)

elif operation == "**":
    print(num1 ** num2)

elif operation == "/":
    if num2 != 0:
        print(num1 / num2)

    else:
        print("Error: cannot divide by zero")

else:
    print("Error: invalid operation")


