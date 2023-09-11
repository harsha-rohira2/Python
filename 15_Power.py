# print power function
num,num1 = 2,5
print(pow(num,num1))

# Print power function using Itration
num=int(input("Enter num: "))
power=int(input("Enter power you want:"))
result=1
for i in range(power):
    result=result * num
print("Power of ", num, "is", result)