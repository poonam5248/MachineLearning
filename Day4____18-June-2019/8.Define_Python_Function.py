# Calling a Function

def my_function():
  print("Hello from a function")
my_function()

# Parameter Values

def my_function(fname):
  print(fname + " Kaur")

my_function("Poonam")
my_function("Harjeet")
my_function("Mandeep")

# Default Parameter Values

def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

# Passing a List as a Parameter

def my_function(food):
  for x in food:
    print(x)

fruits = ["Apple", "Banana", "Mango"]

my_function(fruits)

# Return Values

def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

# Recursion

def tri_recursion(k):
  if(k>0):
    result = k+tri_recursion(k-1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)



