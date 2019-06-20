# 1.
def abc():
    print("TechieNest")
def pqr():
    print("Jaipur")
def both():
    abc()
    pqr()
both()

# 2.

def abc():
    print("TechieNest")
    def pqr():
        print("Jaipur")
    pqr()
def mno():
    print("Delhi")

abc()
#pqr()
mno()

# 3.

def abc():
    print("TechieNest")
    def pqr():
        print("Jaipur")
    pqr()
def mno():
    print("Delhi")
def pqr():
    print("Hyderabad")
    mno()
abc()
pqr()





