# 1.

a=10
def abc():
    print("TechieNest",a)
abc()

# 2.

a=10
def abc():
    print("TechieNest",a)
    def pqr():
        print("Jaipur")
    pqr()
def pqr():
    print("Hyderabad")
abc()
a=a+10
print(a)

# 3.

a=10
def abc():
    global a
    a=a**3
    print("TechieNest",a)
    def pqr():
        print("Jaipur")
    pqr()
    print("Hyderabad")
abc()
a=a+10
print(a)

# 4.
a=10
def abc():
    global a
    a=a**3
    print("TechieNest",a)
    def pqr():
        print("Jaipur")
    pqr()
def pqr():
    global a
    a=123
    print("Hyderabad",a+100)
abc()
a=a+10
print(a)
pqr()

