def myfun():
    print("Good morning")
myfun()

# Addition 2 number in function
def myfun():
    a = int(input("Enter num1: "))
    b = int(input("Enter num2: "))
    c = a + b
    print("Addition is : ", c)
myfun()

# A Paramaterized Function addition of 2 numbers
def myfun(x,y):
    a = x
    b = y
    c = a + b
    print("addition is:",c)
myfun(10,20)

# Swap 2 number using Function
def swap(x,y):
    a = x
    b = y
    a,b=b,a
    print("swap of A is",a)
    print("Swap of B is",b)
swap(10,20)

# Arbitury Arrugument with function
def myfun(*sub):
    print(" my favorate subject is ",sub[2])
myfun("C","CPP","Python")

# Key Aribtury Arguments with function
def myfun(**allsub):
    print(" my favorate subject is ",allsub["sub1"])
myfun(sub1 = "C", sub2="Cpp", sub3="Python")

