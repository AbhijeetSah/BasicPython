#WAP to find division of two numbers
try:
    x=int(input("Enter first number: "))
    y=int(input("ENter second number: "))
    z=x/y
    print("Result=",z)
except ValueError:
    print("Enter number only")
except ArithmeticError:
    print("second number can't be zero")
    
