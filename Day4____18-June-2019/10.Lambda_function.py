# Lambda Function

# One parameter

x = lambda a : a + 10
print("Addition: ",x(5))

# Two Parameter

x = lambda a, b : a * b
print("Multiplication: ",x(5, 6))

# Three Parameter

x = lambda a, b, c : a + b + c
print("Sum: ",x(5, 6, 5))


# Use of Lambda Function  # doubler
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print("Doubler: ",mydoubler(11))

# Tripler

def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)

print("Tripler: ",mytripler(11))

# Doubler and Tripler

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print("Doubler: ",mydoubler(12)) 
print("Tripler: ",mytripler(12))
