# Check the string without Loop
txt = "Python is Object Orientation Programming Language"
print("Object" in txt)              # Output     True

# String Concatenation
a = "Python"
b = "Programms"
c = a +" " + b
print (c)                           # Output     Python Programms

# Capatialization
txt = "hello, and welcome"
x = txt.capitalize()
print(x)                            # Output    Hello, and welcome

# Casefold ( Convert string in lower case )
txt = "Hello, and Welcome"
x = txt.casefold()
print(x)                            # Output    hello, and welcome

# Center String
txt = "Python"
x = txt.center(20)
x1 = txt.center(20,"0")
print(x,x1)                         # Output            Python        0000000Python0000000

# split
a ='hello world'
print(a.split())                    # Output     ['hello', 'world']

# Format function (named indexes)
txt = "language {name}, duration{month}".format(name = "python", month=2)
print(txt)                         # Output      language python, duration2

# Format function (number indexes)
txt = "language {0}, duration{1}".format("python",2)
print(txt)                          # Output     language python, duration2

