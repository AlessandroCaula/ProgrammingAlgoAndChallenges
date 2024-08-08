# Day 23

## Simple Calculator

'''
Create a simple calculator. The calculator should be able to perform basic math operations, add, subtract, divide and multiply. The calculator should take input from users. 
The calculator should be able to handle ZeroDivisionError, NameError, and ValueError. 
'''

def calculator():
    try:
        num1 = float(input("Enter number: "))
        opt = input("Pick operator (+,-,*,/): ")
        if opt not in ["+", "-", "*", "/"] or len(opt) > 1:
            return "Invalid operator"
        num2 = float(input("Enter second number: "))
        if opt == "+":
            return "Ans is: ", num1 + num2
        if opt == "-":
            return "Ans is: ", num1 - num2
        if opt == "*":
            return "Ans is: ", num1 * num2
        if opt == "/":
            return "Ans is: ", num1 / num2   
    except ValueError:
        return "Please enter a valid number"
    except ZeroDivisionError:
        return "You cannot divide a number by zero"
            
print(calculator())