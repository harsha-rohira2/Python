# Print GCD Number (Greatest Common Divisor)
num1=int(input("Enter num1: "))
num2=int(input("Enter num2: "))
GCD=1
for i in range(1,min(num1, num2)):
    if num1 % i == num2 % i ==0:
        GCD=i
print("GCD is ", GCD)