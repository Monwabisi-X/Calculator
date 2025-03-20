import math
#Do not make any other imports i.e DO NOT import re

def add(a, b):
    """
    Add two numbers and return the result.
    """
    return a + b

def subtract(a, b):
    """
    Subtract the second number from the first and return the result.
    """
    return a - b

def multiply(a, b):
    """
    Multiply two numbers and return the result.
    """
    return a * b

def divide(a, b):
    """
    Divide the first number by the second and return the result.
    Handle division by zero by returning "Error: Division by zero".
    """
    return a / b if b != 0 else "Error: Division by zero"

def sqrt(a):
    """
    Return the square root of a number.
    Handle negative inputs by returning "Error: Negative input".
    """
    return math.sqrt(a) if a >= 0 else "Error: Negative input"

def modulus(a, b):
    """
    Return the remainder of the division of the first number by the second.
    Handle division by zero by returning "Error: Division by zero".
    """
    return a % b if b != 0 else "Error: Division by zero"

def exponent(a, b):
    """
    Return the result of raising the first number to the power of the second.
    """
    return a ** b

def factorial(a):
    """
    Return the factorial of a number.
    Handle negative inputs by returning "Error: Negative input".
    """
    return math.factorial(a) if a >= 0 else "Error: Negative input"

def log(a, base):
    """
    Return the logarithm of a number with a specified base.
    Handle invalid inputs by returning "Error: Invalid input".
    """
    return math.log(a, base) if a > 0 and (1> base > 0 or base > 1) else "Error: Invalid input"

def sin(a):
    """
    Return the sine of a number (in radians).
    """
    return math.sin(a)

def cos(a):
    """
    Return the cosine of a number (in radians).
    """
    return math.cos(a)

def tan(a):
    """
    Return the tangent of a number (in radians).
    Handle undefined cases by returning "Error: Undefined".
    """
    return math.tan(a) if a != math.radians(90) else "Error: Undefined"

def degrees_to_radians(degrees):
    """
    Convert degrees to radians.
    """
    return math.radians(degrees)

def radians_to_degrees(radians):
    """
    Convert radians to degrees.
    """
    return math.degrees(radians)

def evaluate_expression(expression: str):
    """
    Evaluate a mathematical expression using PEMDAS/BODMAS rules.
    The expression is a string, e.g., "3 / 7 * 8 % 3".
    This function will call other calculator functions in the correct order.
    DO NOT USE THE eval() expression.
    """
    new_expression = expression.split()
    # new_expression = expression.strip().replace(" ", "")
    # brackets = None
    # if "(" in new_expression:
    #     brackets = new_expression.split("(")[1].split(")")[0]

    for char in new_expression:
        index = new_expression.index(char)
        a = None
        b = None
        
        if len(new_expression) > 2:
            if new_expression[index + 1].isdigit() and new_expression[index + 2].isdigit():
                a = int(new_expression[index])
                b = int(new_expression[index + 2])
            
            if new_expression[index + 1] == "*":
                return multiply(a, b)

            elif new_expression[index + 1] == "/":
                return divide(a, b)

            elif new_expression[index + 1] == "+":
                return add(a, b)

            elif new_expression[index + 1] == "-":
                return subtract(a, b)
        
        c = int(new_expression[index].split("(")[1].split(")")[0])
        # return c
        
        if "sqrt" in new_expression[index]:
            return sqrt(c)
        
        if "factorial" in new_expression[index]:
            return factorial(c)

        # if "log" in new_expression[index]:
            # return log(c)

# string = "11+45-27*4+8"
print(evaluate_expression("sqrt(16)"))
