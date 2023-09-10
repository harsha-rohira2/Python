"""
1. In Python Anonymous function is a friend that is defined without a name
2. Function can be expand in one line i.e Lambda
3. Propose of Lambda is to Save memory
"""

# Addtion of two numbers
x = lambda a,b : a+b
print(x(5,10))                      # output  15

# Print the Maximum number
x = lambda a,b : a if a>b else b
print(x(5,10))                      # Output   10

# Print the square of number
x = lambda n : n ** 2
print(x(5))                         # output  25

# print power of number
x = lambda a,b : a**b
print(x(2,9))                       # output 512