# write a menu driven program for calculator using functions

import math

# Function definitions
def add1(a, b):
    """Addition of a and b"""
    return a + b

def sub1(a, b):
    """Subtraction of a and b"""
    return a - b

def mul1(a, b):
    """Multiplication of a and b"""
    return a * b

def div1(a, b):
    """Division of a and b"""
    if b == 0:
        return "Cannot divide by zero"
    return a / b

def sq_root(x):
    """Square root of x"""
    if x < 0:
        return "Cannot find square root of negative number"
    return math.sqrt(x)

def power(y, z):
    """Power of y raised to z"""
    return math.pow(y, z)

def sin1(x):
    """Sine of angle in degrees"""
    return math.sin(math.radians(x))

def cos1(x):
    """Cosine of angle in degrees"""
    return math.cos(math.radians(x))

# Menu
print("Calculator Menu:")
print("1. ADD")
print("2. SUB")
print("3. MUL")
print("4. DIV")
print("5. SQRT")
print("6. POWER")
print("7. SIN")
print("8. COS")

# User input
choice = int(input("Enter your choice (1-8): "))

# Based on choice
if choice in [1, 2, 3, 4, 6]:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if choice == 1:
        print("Result:", add1(a, b))
    elif choice == 2:
        print("Result:", sub1(a, b))
    elif choice == 3:
        print("Result:", mul1(a, b))
    elif choice == 4:
        print("Result:", div1(a, b))
    elif choice == 6:
        print("Result:", power(a, b))

elif choice == 5:
    x = float(input("Enter a number: "))
    print("Result:", sq_root(x))

elif choice == 7:
    x = float(input("Enter angle in degrees: "))
    print("Result:", sin1(x))

elif choice == 8:
    x = float(input("Enter angle in degrees: "))
    print("Result:", cos1(x))

else:
    print("Invalid choice!")
