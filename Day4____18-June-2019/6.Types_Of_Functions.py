#TYPES OF FUNCTIONS IN PYTHON

# 1. Python Function with no Argument and no return values

def Adding():
    a=20
    b=30
    Sum=a+b
    print("After calling the function the sum is: ",Sum)
Adding()



# 2. Python function with No arguments and with return values

def Multiplication():
    a=10
    b=25
    Multi=a*b
    return Multi
print("After Calling the function the multiplication is: ", Multiplication())


# 3. Python function with Arguments and No return Value

def Multiplication(a,b):
    Multi=a*b
    print("After calling the function The multiplication is: ", Multi)
Multiplication(10,20)

# 4. Python Function with Arguments and Return Values

def Addition(a,b):
    Sum=a+b
    return Sum
print("After Calling the function the Addition of two numbers is: ",Addition(10,20))
