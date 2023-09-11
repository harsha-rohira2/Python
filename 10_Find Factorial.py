# Find the Factorial
n = 23
fact = 1

for i in range(1, n + 1):
    fact = fact * i

print("The factorial is :")
print(fact)

# Using Functions
def factorial(num):
    fact=1
    i=1
    if num<0:
        print("Enter number: ")
    else:
        while(i<=num):
            fact*=i
            i=i+1
    return fact
