from calculator.my_functions import *

operand = int(input("Enter the operand (0 for sum, 1 for subtract, 2 for divide, 3 for multiply): "))
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

try:
    if operand == 0:
        result = sum(num1, num2)
        print(f"The sum is: {result}")
    elif operand == 1:
        if num1 == 0 or num2 == 0:
            raise ValueError("subtracting zero from a number")
        result = subtract(num1, num2)
        print(f"The difference is: {result}")
    elif operand == 2:
        if num2 == 0:
            raise ZeroDivisionError("can't divide by zero")
        result = divide(num1, num2)
        print(f"The quotient is: {result}")
    elif operand == 3:
        if num1 == 0 or num2 == 0:
            raise ValueError("Multiply with Zero")
        result = multiply(num1, num2)
        print(f"The product is: {result}")
except ValueError as e:
    print(f"Error: {e}")
except ZeroDivisionError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")