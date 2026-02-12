# WAP menu driven program for calculator - add, sub, mult, divide, sqrt, power, sin , cos
# Create your own functions and call them . Every functions should take parameters and return the result.

import math

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

def sqrt(a):
    return a**0.5

def power(a,b):
    return a**b

def sin(angle_degree):
    angle_rad = math.pi / 180 * angle_degree
    return math.sin(angle_rad)

def cos(angle_degree):
    angle_rad = math.pi / 180 * angle_degree
    return math.cos(angle_rad)

print("Calculator Menu : "
"1. ADD "
"2. SUB "
"3. MUL "
"4. DIV "
"5. SQRT "
"6. POWER "
"7. SIN "
"8. COS "
"9. EXIT")

choice = int(input("Enter your choice :- "))
print(choice)

match(choice):
    case 1:
            a = int(input("Enter first numbers: "))
            b = int(input("Enter second numbers: "))
            c = add(a,b)
            print("Addition is", c)

    case 2:
            a = int(input("Enter first numbers: "))
            b = int(input("Enter second numbers: "))
            c = sub(a,b)
            print("Subtraction is", c)

    case 3 :
            a = int(input("Enter first numbers: "))
            b = int(input("Enter second numbers: "))
            c = mul(a,b)
            print("Multiplication is", c)

    case 4 :
            a = int(input("Enter first numbers: "))
            b = int(input("Enter second numbers: "))
            c = div(a,b)
            print("Division is", c)

    case 5 :
            # int(input("Enter One numbers:", num))
            # c = math.sqrt(num)
            # print("Square Root:",c)

            a = int(input("Enter one numbers: "))
            c = sqrt(a)
            print("Square root is",c)

    case 6 : 
            a = int(input("Enter first numbers: "))
            b = int(input("Enter second numbers: "))
            c = power(a,b)
            print("Power is", c)
            
    
    # case 7 :
    #         pi=3.14
    #         a = float(input("Enter Angle in the Degrees : "))
    #         r = d*(pi/180)
    #         print("Sin:",r)

    case 7 :
            a = int(input("Enter Angle in the Degrees : "))
            r = sin(a)
            print("Sin:",r)
    
    case 8 :
            a = int(input("Enter Angle in the Degrees : "))
            r = cos(a)
            print("Cos:",r)
    
    # case 9 :
          
    #       print("Exit")

    case _:   #default case
        print("Invalid Choice of Number")